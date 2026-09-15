#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
grid_table_to_html.py — 把 Word 转换素材里的 grid table 还原成带合并单元格的 HTML。

背景
----
笔记里的手写表格来自 Word 的 pandoc 素材。素材里的 grid table 长这样：

    +----------------+---------------------------+---------------------------+
    | 分布函数       | $$F(x) = P(X \\leq x)$$   | $$F(x,y) = ...$$          |
    |                +---------------------------+---------------------------+
    |                | $F(x)$是$\\mathbb{R}$上的单调非减右连续函数         |
    +----------------+---------------------------+---------------------------+

`+---+` 分隔线在哪里断、在哪里连，就编码了 Word 里的合并单元格。
搬运时这层结构被丢了 —— 单元格被平铺成一串 <th>，于是「分布函数」跑到第 1 列、
整行合并的公式挤进第 1 格，读起来全错位。

为什么不用 pandoc 直接转
------------------------
1. pandoc 的 HTML writer 会把 TeX 数学写成 HTML/Unicode（`<em>F</em>(<em>x</em>)`），
   LaTeX 全丢；加 `--mathjax` 也只是把数学 AST 重新序列化，复杂构造会走样。
2. 更关键：素材本身几何不自洽 —— 满行合并的行比边框短了几个字符
   （`| 一维随机变量 …    |` 的右竖线没对齐到边框的 `+`）。
   pandoc 的 grid 解析器遇到这种就**静默截断**：整张表只留第一行，其余丢掉。
   实测 13 张表里有 11 张被这样截断。

所以这里自己解析：容忍几像素级别的错位，结构靠边框（`+` 位置）定，内容原样取。
单元格内容按 pandoc 的约定还原：同一格内的换行是**排版折行**，用空格连接；
空行才是真正的分段。

输出风格与仓库现有表格一致：
  * 外层 `<div class="table-scroll">`
  * 显式 `<thead>` / `<tbody>`（漏了 `<tbody>` 会被浏览器自动补一个，与 Vue 编译出的
    vnode 树不一致 → hydration 重建表格 → 表格内公式在闪现一次后全部变空白）
  * 单元格内容前后留空行，这样 markdown-it 才会把 `$$...$$` 当数学渲染

用法
----
    python tools/grid_table_to_html.py out/概率论与数理统计.md --list
    python tools/grid_table_to_html.py out/概率论与数理统计.md --n 2 -o table2.html
    python tools/grid_table_to_html.py out/概率论与数理统计.md --lines 187 247
"""
import argparse
import json
import re
import sys
import unicodedata

BORDER = re.compile(r'^\s*\+[-=:+]+\+\s*$')
TOLERANCE = 1          # 竖线允许偏离边界多少个**显示列**

# 说明：素材按显示宽度对齐，边界位置本来是严丝合缝的（实测竖线就在 0/69/266 列）。
# 容差给大了反而危险 —— 公式里的 `\text{|}`、`|x|` 离边界一两列时会被误当成
# 单元格分隔线，把公式从中间劈开。所以只留 1 列余量。


def char_width(ch):
    """东亚全角字符占 2 个显示列。

    素材是按**显示宽度**对齐的（Word 转换工具按视觉宽度补空格）：
    同一列的竖线在『字符下标』上会漂移（中文多一个字符就左移一格），
    但在『显示列』上严丝合缝。所以这里必须按显示宽度算，否则会张冠李戴。
    """
    return 2 if unicodedata.east_asian_width(ch) in ('W', 'F') else 1


def visual_offsets(line):
    """返回 (每个字符的起始显示列, 整行显示宽度)。"""
    offs = []
    v = 0
    for ch in line:
        offs.append(v)
        v += char_width(ch)
    return offs, v


def find_bar(line, offs, target, tol=TOLERANCE):
    """找显示列 target 附近的那根竖线，返回它的字符下标。"""
    best = None
    for ci, ch in enumerate(line):
        if ch != '|':
            continue
        d = abs(offs[ci] - target)
        if d <= tol and (best is None or d < best[0]):
            best = (d, ci)
    return best[1] if best else None


def read_lines(path):
    """读文件并把 CRLF/CR 统一成 LF（素材是 Word 转出来的，行尾是 CRLF）。"""
    text = open(path, encoding='utf-8').read()
    return text.replace('\r\n', '\n').replace('\r', '\n').split('\n')


# ---------------------------------------------------------------- 定位表格
def find_tables(lines):
    """返回 [(起始行(1-based), 结束行, [行文本])]。表格 = 从边框行开始的连续 `+`/`|` 块。"""
    out = []
    i = 0
    while i < len(lines):
        if BORDER.match(lines[i]):
            start = i
            j = i
            while j < len(lines) and re.match(r'^\s*[+|]', lines[j]):
                j += 1
            chunk = lines[start:j]
            if any(re.match(r'^\s*\|', l) for l in chunk):
                out.append((start + 1, j, chunk))
            i = j
        else:
            i += 1
    return out


def boundaries(chunk):
    """列边界 = 所有边框行里 `+` 出现过的位置（并集，排序）。"""
    pos = {}
    for line in chunk:
        if BORDER.match(line):
            for i, ch in enumerate(line):
                if ch == '+':
                    pos[i] = pos.get(i, 0) + 1
    cols = sorted(pos)
    # 去掉只出现一次的孤立位置（多半是公式里的加号被误判）
    if len(cols) > 2:
        keep = [c for c in cols if pos[c] >= 2]
        if len(keep) >= 2:
            cols = keep
    return cols


def separator_segment(line, a, b):
    """取显示列 (a, b) 之间的字符（用于判断这一段是横线还是空格）。"""
    offs, _w = visual_offsets(line)
    return ''.join(ch for ci, ch in enumerate(line) if a < offs[ci] < b)


def is_separator(line, cols):
    """分隔线：每个列区间里只有 `-`/`=`/`:`/空格（按显示列切）。

    注意要接受**部分分隔线**（形如 `|     +-----+-----+`）—— 前半段没有横线，
    正表示那一列的单元格要跨到下一行（rowspan）。
    """
    has_dash = False
    for k in range(len(cols) - 1):
        seg = separator_segment(line, cols[k], cols[k + 1])
        if seg.strip(' -=:'):
            return False
        if re.search(r'[-=]', seg):
            has_dash = True
    return has_dash


# ---------------------------------------------------------------- 解析
def parse(chunk, cols):
    """返回 rows：[[cell, ...], ...]，cell = {start, colspan, rowspan, lines}"""
    rows = []
    continuing = {}          # 列号 -> cell（跨行合并，仍在继续）
    emitted = set()          # 已经输出过的 cell（用 id 认）
    warnings = []

    k = 0
    while k < len(chunk):
        line = chunk[k]
        if BORDER.match(line) or is_separator(line, cols):
            k += 1
            continue

        # ---- 一个行块：连续的正文行（可能被同格折行分成多行） ----
        cells = dict(continuing)
        block = []
        while k < len(chunk) and not BORDER.match(chunk[k]) and not is_separator(chunk[k], cols):
            block.append(chunk[k])
            k += 1

        for bl in block:
            offs, _w = visual_offsets(bl)
            marks = []
            for i, p in enumerate(cols):
                ci = find_bar(bl, offs, p)
                if ci is not None:
                    marks.append((i, ci))
            if not marks:
                warnings.append(f'行没有竖线，已跳过: {bl[:60]!r}')
                continue
            if marks[0][0] != 0:
                warnings.append(f'行首不在边界上: {bl[:60]!r}')
            for (i, ci), (j, cj) in zip(marks, marks[1:]):
                cell = cells.get(i)
                if cell is None or cell['colspan'] != j - i:
                    cell = {'start': i, 'colspan': j - i, 'rowspan': 1, 'lines': []}
                    cells[i] = cell
                seg = bl[ci + 1:cj].strip()
                cell['lines'].append(seg)

        # ---- 行块结束：看下一行的分隔线决定谁继续向下 ----
        # 跨行合并的格只在「起始行」输出一次，后续行里要跳过（它已经带 rowspan 了）
        row = [cells[i] for i in sorted(cells) if id(cells[i]) not in emitted]
        emitted.update(id(c) for c in row)
        rows.append(row)

        nxt = chunk[k] if k < len(chunk) else None
        nxt_open = {}
        if nxt is not None and (BORDER.match(nxt) or is_separator(nxt, cols)):
            for i in sorted(cells):
                cell = cells[i]
                # 该格覆盖的每个列区间：只要有一个区间下面没有横线，就继续跨行
                spans = range(cell['start'], cell['start'] + cell['colspan'])
                closed = True
                for c in spans:
                    if c + 1 >= len(cols):
                        continue
                    seg = separator_segment(nxt, cols[c], cols[c + 1])
                    if '-' not in seg and '=' not in seg:
                        closed = False
                if not closed:
                    cell['rowspan'] += 1
                    nxt_open[cell['start']] = cell
        continuing = nxt_open

    return rows, warnings


# ---------------------------------------------------------------- 渲染
def _cjk(ch):
    return bool(ch) and '\u3000' <= ch <= '\u9fff' or bool(ch) and '\uff00' <= ch <= '\uffef'


def join_wrapped(parts):
    """把同一格里的折行接回去。

    中文折行不能补空格：「分布列/概」+「率密度函数」拼出来必须是
    「分布列/概率密度函数」，补了空格就变成「分布列/概 率密度函数」。
    西文/公式折行则按惯例补一个空格。
    """
    s = parts[0]
    for nxt in parts[1:]:
        if _cjk(s[-1:]) or _cjk(nxt[:1]):
            s += nxt
        else:
            s += ' ' + nxt
    return s


def cell_text(cell):
    """同一格里的换行是折行 → 接回去；空行才是分段。"""
    out, para = [], []
    for raw in cell['lines']:
        s = raw.strip()
        if s == '':
            if para:
                out.append(join_wrapped(para))
                para = []
        else:
            para.append(s)
    if para:
        out.append(join_wrapped(para))
    return [re.sub(r'[ \t]{2,}', ' ', p).strip() for p in out if p.strip()]


def render(rows, header_rows=1):
    parts = ['<div class="table-scroll">', '<table>']
    head, body = rows[:header_rows], rows[header_rows:]
    if head:
        parts.append('<thead>')
        parts.append(render_rows(head, 'th'))
        parts.append('</thead>')
    parts.append('<tbody>')
    parts.append(render_rows(body, 'td'))
    parts.append('</tbody>')
    parts.append('</table>')
    parts.append('</div>')
    return '\n'.join(parts)


def render_rows(rows, tag):
    out = []
    for row in rows:
        cells = []
        for cell in row:
            attrs = ''
            if cell.get('rowspan', 1) > 1:
                attrs += f' rowspan="{cell["rowspan"]}"'
            if cell.get('colspan', 1) > 1:
                attrs += f' colspan="{cell["colspan"]}"'
            paras = cell_text(cell)
            if paras:
                body = '\n\n'.join(paras)
                cells.append(f'<{tag}{attrs}>\n\n{body}\n\n</{tag}>')
            else:
                cells.append(f'<{tag}{attrs}></{tag}>')
        out.append('<tr>\n' + '\n'.join(cells) + '\n</tr>')
    return '\n'.join(out)


# ---------------------------------------------------------------- CLI
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('file')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--n', type=int, help='第几张表（从 1 开始）')
    ap.add_argument('--lines', nargs=2, type=int)
    ap.add_argument('--head', type=int, default=1, help='表头行数，默认 1')
    ap.add_argument('--json', action='store_true', help='输出结构 JSON（自检用）')
    ap.add_argument('-o', '--out')
    args = ap.parse_args()

    lines = read_lines(args.file)
    tables = find_tables(lines)

    if args.list:
        print(f'{args.file}: {len(tables)} 张 grid table\n')
        for n, (a, b, chunk) in enumerate(tables, 1):
            cols = boundaries(chunk)
            rows, warns = parse(chunk, cols)
            spans = sum(1 for r in rows for c in r if c['rowspan'] > 1 or c['colspan'] > 1)
            dollars = sum(l.count('$') for l in chunk)
            first = ' | '.join((cell_text(c) or ['·'])[0][:26] for c in rows[0]) if rows else ''
            print(f'#{n:2} line {a}-{b}  列={len(cols) - 1} 行={len(rows)} '
                  f'合并格={spans} $={dollars}')
            print(f'     首行: {first}')
            if warns:
                print(f'     [warn] {len(warns)} 条: {warns[0]}')
        return

    if args.lines:
        a, b = args.lines
        chunk = [l for l in lines[a - 1:b]]
        if not BORDER.match(chunk[0]):
            for cand in tables:
                if cand[0] <= a <= cand[1]:
                    chunk = cand[2]
                    break
        selected = [chunk]
    elif args.n:
        if not 1 <= args.n <= len(tables):
            sys.exit(f'没有第 {args.n} 张表（共 {len(tables)} 张）')
        selected = [tables[args.n - 1][2]]
    else:
        sys.exit('需要 --list / --n / --lines 之一')

    if args.json:
        payload = []
        for chunk in selected:
            cols = boundaries(chunk)
            rows, warns = parse(chunk, cols)
            payload.append({
                'cols': len(cols) - 1,
                'rows': [[{'rs': c['rowspan'], 'cs': c['colspan'], 'text': cell_text(c)} for c in r] for r in rows],
                'warnings': warns
            })
        print(json.dumps(payload, ensure_ascii=False, indent=1))
        return

    htmls = []
    for chunk in selected:
        cols = boundaries(chunk)
        rows, warns = parse(chunk, cols)
        for w in warns[:5]:
            sys.stderr.write(f'[warn] {w}\n')
        htmls.append(render(rows, args.head))
    html = '\n\n'.join(htmls)
    if args.out:
        open(args.out, 'w', encoding='utf-8').write(html + '\n')
        sys.stderr.write(f'wrote {args.out} ({len(html)} 字符)\n')
    else:
        sys.stdout.write(html + '\n')


if __name__ == '__main__':
    main()
