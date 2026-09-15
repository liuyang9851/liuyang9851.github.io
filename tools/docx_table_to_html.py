#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
docx_table_to_html.py — 把 Word 文档里的表格还原成带合并单元格的 HTML。

和 grid_table_to_html.py 的区别
------------------------------
那个工具吃的是 pandoc 转出来的 markdown 素材（grid table）；
这个直接吃 **.docx**，用于那些没有留素材的章节（线性代数、物理……）。

为什么绕 pandoc 的 JSON AST
--------------------------
* `pandoc -t html`：结构对（有 rowspan/colspan），但**数学会变成 HTML/Unicode**
  （`<em>F</em>(<em>x</em>)`），LaTeX 全丢。
* `pandoc -t markdown`：LaTeX 保住了，但带合并单元格的表会被写成 pipe table，
  **合并信息丢掉**（实测线性代数总结.docx 5 张表、11 处合并，markdown 输出里一处不剩）。
* `pandoc -t json`：Cell 节点上直接有 rowspan/colspan，Math 节点里是原始 TeX。两边都保住。

输出风格与仓库现有表格一致：`<div class="table-scroll">` + 显式 `<thead>/<tbody>`，
单元格内容前后留空行（这样 markdown-it 才会把 `$$...$$` 当数学渲染）。
公式里的中文没包 `\\text{}`，需要的话再跑一遍 `tools/wrap_math_cjk.py`。

用法
----
    python tools/docx_table_to_html.py 线性代数总结.docx --list
    python tools/docx_table_to_html.py 线性代数总结.docx --n 1 -o t1.html
    python tools/docx_table_to_html.py 线性代数总结.docx --n 1 --head 1 -o t1.html
"""
import argparse
import json
import re
import sys

import pypandoc


def load_ast(path):
    return json.loads(pypandoc.convert_file(path, 'json', format='docx'))


def tables_of(ast):
    return [b['c'] for b in ast['blocks'] if b['t'] == 'Table']


# ---------------------------------------------------------------- 渲染
def math_kind(kind):
    """pandoc 2 里 Math 的类型是字符串，pandoc 3 里是 {'t': 'InlineMath'}。

    不兼容这一步会把**所有行内公式当成行间公式**（`$k$` → `$$k$$`），
    表格单元格里就会出现一堆居中的大公式。
    """
    if isinstance(kind, dict):
        return kind.get('t')
    return kind


def render_inlines(inlines):
    out = []
    for node in inlines:
        t = node['t']
        c = node.get('c')
        if t == 'Str':
            out.append(c)
        elif t in ('Space', 'SoftBreak', 'LineBreak'):
            out.append(' ')
        elif t == 'Math':
            kind, tex = c
            tex = re.sub(r'\s*\n\s*', ' ', tex).strip()
            if math_kind(kind) == 'InlineMath':
                out.append(f'${tex}$')
            else:
                # 行间公式前后必须换行 —— 见 render_blocks 里的说明：
                # `$$k$$次幂` 这种「公式后面还跟文字」会让 markdown-it 的 math_block
                # 规则一路吞到下一个以 $$ 结尾的行，把后面的 HTML 也吃进公式里。
                out.append(f'\n\n$${tex}$$\n\n')
        elif t == 'Emph':
            out.append('*' + render_inlines(c) + '*')
        elif t == 'Strong':
            out.append('**' + render_inlines(c) + '**')
        elif t == 'Strikeout':
            out.append('~~' + render_inlines(c) + '~~')
        elif t == 'Subscript':
            out.append('<sub>' + render_inlines(c) + '</sub>')
        elif t == 'Superscript':
            out.append('<sup>' + render_inlines(c) + '</sup>')
        elif t in ('Underline', 'Cite', 'SmallCaps'):
            out.append(render_inlines(c[1] if t == 'Cite' else c))
        elif t == 'Code':
            out.append('`' + c[1] + '`')
        elif t == 'RawInline':
            out.append(c[1])
        elif t == 'Quoted':
            out.append('“' + render_inlines(c[1]) + '”')
        elif t == 'Link':
            # c = [attr, inlines, [url, title]]
            out.append('[' + render_inlines(c[1]) + '](' + c[2][0] + ')')
        elif t == 'Image':
            # c = [attr, alt_inlines, [url, title]] —— 必须保留 url，否则图片全丢
            out.append('![' + render_inlines(c[1]) + '](' + c[2][0] + ')')
        elif t == 'Span':
            out.append(render_inlines(c[1]))
        elif t == 'Note':
            out.append('')
        else:
            sys.stderr.write(f'[warn] 未处理的内联节点 {t}\n')
            out.append(render_inlines(c) if isinstance(c, list) else str(c))
    return ''.join(out)


def render_blocks(blocks):
    paras = []
    for blk in blocks:
        t = blk['t']
        c = blk.get('c')
        if t in ('Para', 'Plain'):
            # 段落里若混着行间公式（render_inlines 会把它前后加空行），
            # 这里按空行切开，保证每个 `$$...$$` 独占一行。
            # 否则 `$$k$$次幂` 会被 markdown-it 的 math_block 规则当成
            # 「开了没关」，一路吞掉后面的 HTML（实测直接让构建报
            # Can't find handler for document）。
            text = render_inlines(c).strip()
            for piece in re.split(r'\n\s*\n', text):
                if piece.strip():
                    paras.append(piece.strip())
        elif t == 'LineBlock':
            paras.append(' '.join(render_inlines(l).strip() for l in c).strip())
        elif t == 'RawBlock':
            paras.append(c[1])
        elif t == 'BulletList':
            paras.append('；'.join(render_inlines(i[0]['c']) for i in c))
        elif t == 'OrderedList':
            paras.append('；'.join(render_inlines(i[0]['c']) for i in c))
        elif t == 'BlockQuote':
            # 单元格里的引用块：直接取里面的段落，别丢内容
            paras.extend(render_blocks(c))
        elif t == 'Table':
            # 单元格里嵌套的表格：渲染成嵌套 <table>（不要再套 .table-scroll）
            paras.append(render_table(c, 1, wrap=False))
        elif t == 'Header':
            paras.append(render_inlines(c[2]).strip())
        else:
            sys.stderr.write(f'[warn] 未处理的块节点 {t}\n')
    return [p for p in paras if p]


def render_cell(cell, tag):
    _attr, _align, rowspan, colspan, blocks = cell
    attrs = ''
    if rowspan and rowspan > 1:
        attrs += f' rowspan="{rowspan}"'
    if colspan and colspan > 1:
        attrs += f' colspan="{colspan}"'
    paras = render_blocks(blocks)
    if not paras:
        return f'<{tag}{attrs}></{tag}>'
    body = '\n\n'.join(paras)
    return f'<{tag}{attrs}>\n\n{body}\n\n</{tag}>'


def rows_to_html(rows, tag):
    out = []
    for row in rows:
        out.append('<tr>\n' + '\n'.join(render_cell(c, tag) for c in row[1]) + '\n</tr>')
    return '\n'.join(out)


def body_rows_of(body):
    """pandoc 的 TableBody 是 [attr, rowheadcols, 行头行[], 表体行[]] —— 两个行列表。

    只取第三个会得到空表：docx 转出来的表，行都在**第四个**里。
    """
    _attr, _rowheadcols, head_rows, rows = body
    return list(head_rows) + list(rows)


def top_level_tables(ast):
    """只收集**顶层**表格。

    表格单元格里还可能嵌着表格（Word 里很常见）。pandoc 的 markdown 会把它们
    写在父表格的单元格里，检测时只算一张 —— 所以计数也要按顶层算，否则
    「markdown 找到 16 张 / AST 有 17 张」会一直对不上。
    """
    out = []

    def walk(blocks):
        for b in blocks:
            t = b['t']
            if t == 'Table':
                out.append(b['c'])          # 不递归进表格内部
            elif t in ('BlockQuote', 'Div'):
                walk(b['c'] if isinstance(b['c'], list) else [])
            elif t in ('BulletList', 'OrderedList'):
                for item in b['c']:
                    walk(item)
            elif t == 'DefinitionList':
                for _term, defs in b['c']:
                    for d in defs:
                        walk(d)
    walk(ast['blocks'])
    return out


def render_table(table, head_rows=1, wrap=True):
    _attr, _caption, colspecs, head, bodies, _foot = table
    head_rows_list = head[1]
    body_rows = []
    for body in bodies:
        body_rows.extend(body_rows_of(body))

    if body_rows:
        thead, tbody = head_rows_list, body_rows
    else:
        n = head_rows if head_rows else 0
        thead, tbody = head_rows_list[:n], head_rows_list[n:]

    parts = ['<div class="table-scroll">'] if wrap else []
    parts.append('<table>')
    if thead:
        parts += ['<thead>', rows_to_html(thead, 'th'), '</thead>']
    parts += ['<tbody>', rows_to_html(tbody, 'td'), '</tbody>', '</table>']
    if wrap:
        parts.append('</div>')
    return '\n'.join(parts)


def stats(table):
    _a, _c, colspecs, head, bodies, _f = table
    body = [r for b in bodies for r in body_rows_of(b)]
    rows = len(head[1]) + len(body)
    spans = sum(1 for r in head[1] for c in r[1] if c[2] > 1 or c[3] > 1)
    spans += sum(1 for r in body for c in r[1] if c[2] > 1 or c[3] > 1)
    math = len(re.findall(r'"t": "Math"', json.dumps(table)))
    first = ''
    if head[1]:
        first = ' | '.join((render_blocks(c[4]) or ['·'])[0][:24] for c in head[1][0][1])
    elif body:
        first = ' | '.join((render_blocks(c[4]) or ['·'])[0][:24] for c in body[0][1])
    return len(colspecs), rows, spans, math, first


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('docx')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--n', type=int)
    ap.add_argument('--head', type=int, default=1, help='表头行数，默认 1；0 表示没有表头')
    ap.add_argument('-o', '--out')
    args = ap.parse_args()

    ts = tables_of(load_ast(args.docx))

    if args.list:
        print(f'{args.docx}: {len(ts)} 张表\n')
        for i, t in enumerate(ts, 1):
            cols, rows, spans, math, first = stats(t)
            print(f'#{i}  列={cols} 行={rows} 合并格={spans} 公式={math}')
            print(f'     首行: {first}')
        return

    if not args.n or not 1 <= args.n <= len(ts):
        sys.exit(f'需要 --n 1..{len(ts)}')

    html = render_table(ts[args.n - 1], args.head)
    if args.out:
        open(args.out, 'w', encoding='utf-8').write(html + '\n')
        sys.stderr.write(f'wrote {args.out} ({len(html)} 字符)\n')
    else:
        sys.stdout.write(html + '\n')


if __name__ == '__main__':
    main()
