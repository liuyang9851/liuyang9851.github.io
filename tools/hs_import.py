#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
hs_import.py — 把高中数学笔记的 .docx 批量转成站点页面。

一份文档要做四件事：
  1. pandoc 转 **JSON AST**（保住 OMML 公式、抽出图片）
  2. 整篇 markdown 由 AST 渲染：表格换成手写 HTML 并保留 rowspan/colspan。
     pandoc 的 markdown 输出会把合并单元格写成 pipe table（合并信息全丢），
     还会**整张丢掉畸形表格**，所以不再用它的 markdown 结果。
  3. 公式里的中文包 \\text{}
  4. 图片搬到 public/images/hs/<slug>/，路径改写成绝对路径

表格一律输出 `<div class="table-scroll">` + 显式 `<thead>/<tbody>`，
没有 `<tbody>` 时 Vue hydration 会把表里的公式清空（见 validate-tables.mjs）。

用法：
    python tools/hs_import.py "D:/数学/高中数学笔记/A/A1 集合与常用逻辑术语.docx" --slug hs-a01
    python tools/hs_import.py "…/A2 xxx.docx" --slug hs-a02 --title "一元二次函数、方程和不等式"
"""
import argparse
import json
import os
import re
import shutil
import sys

import pypandoc

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_table_to_html import ordered_items, render_inlines, render_table  # noqa: E402
from wrap_math_cjk import transform as wrap_cjk  # noqa: E402
from docx_to_md import fix_chinese_in_math  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, 'notes')
IMAGES = os.path.join(ROOT, 'public', 'images', 'hs')


# ------------------------------------------------------- 2. 整篇由 AST 渲染
# 为什么不再「pandoc markdown + 拼接表格」
# ----------------------------------------
# pandoc 的 markdown writer 遇到**畸形表格会整张丢掉**（实测 A3 文档第 17 张表：
# 表头行只有 3 个格、列数却是 5，pandoc 写 markdown 时直接略过），于是
# 「markdown 里有 16 张表 / AST 里有 17 张」永远对不上，拼接只能放弃。
# 现在改成**整篇由 AST 渲染**：段落、标题、列表、图片全部自己写，
# 表格走 render_table（带 rowspan/colspan），pandoc 只负责 --extract-media。
def _caption_text(caption):
    """pandoc 3 的 Caption 是 [短标题或 null, [Block]]（旧版是三元组，兼容一下）。"""
    blocks = caption[-1]
    parts = []
    for b in blocks or []:
        if b['t'] in ('Para', 'Plain'):
            parts.append(render_inlines(b['c']).strip())
    return ' '.join(p for p in parts if p)


def _list_md(items, ordered, start=1):
    lines, n = [], start
    for item in items:
        prefix = f'{n}. ' if ordered else '- '
        n += 1
        sub = render_doc_blocks(item)
        if not sub:
            lines.append(prefix.rstrip())
            continue
        lines.append(prefix + sub[0])
        pad = ' ' * len(prefix)
        lines.extend(pad + s for s in sub[1:])
    return '\n'.join(lines)


def render_doc_blocks(blocks):
    """把顶层块渲染成一串 markdown 片段（每段之间由调用方补空行）。"""
    out = []
    for blk in blocks:
        t = blk['t']
        c = blk.get('c')
        if t == 'Header':
            lvl, _attr, inlines = c
            out.append('#' * min(max(int(lvl), 1), 6) + ' ' + render_inlines(inlines).strip())
        elif t in ('Para', 'Plain'):
            text = render_inlines(c).strip()
            # 行间公式前后被 render_inlines 加了空行，这里按空行切开
            for piece in re.split(r'\n\s*\n', text):
                if piece.strip():
                    out.append(piece.strip())
        elif t == 'BulletList':
            out.append(_list_md(c, False))
        elif t == 'OrderedList':
            start, items = ordered_items(c)
            out.append(_list_md(items, True, start))
        elif t == 'BlockQuote':
            inner = '\n\n'.join(render_doc_blocks(c))
            out.append('\n'.join(('> ' + l) if l.strip() else '>' for l in inner.split('\n')))
        elif t == 'CodeBlock':
            attr, text = c
            lang = (attr[1] or [''])[0] if attr and attr[1] else ''
            out.append(f'```{lang}\n{text.rstrip()}\n```')
        elif t == 'RawBlock':
            out.append(c[1])
        elif t == 'HorizontalRule':
            out.append('---')
        elif t == 'Table':
            html = render_table(c, 1)
            cap = _caption_text(c[1])
            out.append(html + (f'\n\n*{cap}*' if cap else ''))
        elif t == 'Figure':
            # pandoc 3：图片被包在 Figure 里，c = [attr, caption, blocks]
            out.extend(render_doc_blocks(c[2]))
        elif t == 'Div':
            out.extend(render_doc_blocks(c[1]))
        elif t == 'LineBlock':
            out.append('\n'.join(render_inlines(l).strip() for l in c))
        elif t == 'DefinitionList':
            for term, defs in c:
                head = render_inlines(term).strip()
                for d in defs:
                    out.append(head + '\n\n' + '\n\n'.join(render_doc_blocks(d)))
        else:
            sys.stderr.write(f'[warn] 未处理的顶层块 {t}\n')
    return [o for o in out if o.strip()]


def render_doc(ast):
    return '\n\n'.join(render_doc_blocks(ast['blocks'])) + '\n'


# ---------------------------------------------------------------- 3/4. 图片
def wmf_to_png(src, dest, dpi=150):
    """WMF/EMF（Word 里插的矢量图）浏览器不认，构建时会 Rollup failed to resolve import。

    Pillow 在 Windows 上能读 WMF（走系统 GDI），必须给 dpi，
    否则按 72dpi 出来的图糊。
    """
    from PIL import Image
    im = Image.open(src)
    im.load(dpi=dpi)
    im.convert('RGB').save(dest, 'PNG')


def move_images(media_dir, slug, md):
    """把 media 里的图片搬到 public/images/hs/<slug>/，并改写 markdown 里的路径。"""
    if not os.path.isdir(media_dir):
        return md, 0
    files = []
    for cur, _dirs, names in os.walk(media_dir):
        for n in sorted(names):
            files.append(os.path.join(cur, n))
    if not files:
        return md, 0
    dest = os.path.join(IMAGES, slug)
    os.makedirs(dest, exist_ok=True)
    mapping = {}
    for k, src in enumerate(files, 1):
        ext = os.path.splitext(src)[1].lower() or '.png'
        if ext in ('.wmf', '.emf'):
            new = f'img{k:02d}.png'
            try:
                wmf_to_png(src, os.path.join(dest, new))
            except Exception as e:              # 转不了就原样拷过去（构建会报错，好在看得见）
                sys.stderr.write(f'[warn] {os.path.basename(src)} 转 PNG 失败：{e}\n')
                new = f'img{k:02d}{ext}'
                shutil.copyfile(src, os.path.join(dest, new))
        else:
            new = f'img{k:02d}{ext}'
            shutil.copyfile(src, os.path.join(dest, new))
        mapping[os.path.basename(src)] = new
    # 改写引用（pandoc 写的是 media/xxx 或 media/media/xxx）
    def repl(m):
        path = m.group(2)
        base = os.path.basename(path)
        if base in mapping:
            return f'{m.group(1)}/images/hs/{slug}/{mapping[base]}{m.group(3)}'
        return m.group(0)
    md = re.sub(r'(!\[[^\]]*\]\()([^)]*?)(\))', repl, md)
    return md, len(files)


# ---------------------------------------------------------------- 5. 杂项修复
def fix_math(md):
    """修 Word 转换常见的小毛病。"""
    n = 0
    # a) `$$x$` / `$x$$` —— 定界符写坏的（表格里最常见，幸好表格已改成 AST 渲染）
    before = md
    md = re.sub(r'\$\$([^$\n]+)\$', r'$\1$', md)
    md = re.sub(r'(?<!\$)\$([^$\n]+)\$\$', r'$\1$', md)
    if md != before:
        n += 1
    # b) 公式里带 `\ ` 反斜杠空格的怪写法（\ $）
    md = md.replace('\\ $', '\\$').replace('$\\  ', '$')
    return md, n


def title_of(docx, ast, override=None):
    if override:
        return override
    base = os.path.splitext(os.path.basename(docx))[0]
    base = re.sub(r'^(A|B)\d+\s*', '', base)
    base = re.sub(r'^附录[：:]\s*', '', base)
    return base.strip()


def describe(ast, title):
    """取正文第一段当 description。"""
    for b in ast['blocks']:
        if b['t'] in ('Para', 'Plain'):
            txt = json.dumps(b, ensure_ascii=False)
            plain = ''.join(re.findall(r'"c": "([^"]+)"', txt))
            plain = re.sub(r'\s+', ' ', plain).strip()
            if len(plain) > 12:
                return (title + '：' + plain)[:110]
    return title


def render_page(docx, slug, group, title_override=None, seq=None):
    workdir = os.path.join(ROOT, 'out', 'hs', slug)
    os.makedirs(workdir, exist_ok=True)
    media = os.path.join(workdir, 'media')
    ast = json.loads(pypandoc.convert_file(
        docx, 'json', format='docx', extra_args=['--extract-media', media]))

    md = render_doc(ast)
    md = fix_chinese_in_math(md)
    md, nfix = fix_math(md)
    md = md.replace('\r\n', '\n')
    md, nwrap = wrap_cjk(md)
    md, nimgs = move_images(media, slug, md)

    title = title_of(docx, ast, title_override)
    front = '---\ntitle: {t}\nhs_seq: {s}\ndescription: {d}\n---\n\n'.format(
        t=json.dumps(title, ensure_ascii=False),
        s=json.dumps(seq or '', ensure_ascii=False),
        d=json.dumps(describe(ast, title), ensure_ascii=False))
    # 正文第一行常常是标题本身，去掉重复
    body = md.lstrip('\n')
    first, _, rest = body.partition('\n')
    if first.strip() in (title, '# ' + title):
        body = rest.lstrip('\n')
    page = front + '# ' + title + '\n\n' + body
    path = os.path.join(NOTES, slug + '.md')
    open(path, 'w', encoding='utf-8').write(page)
    return {'slug': slug, 'group': group, 'title': title, 'path': path,
            'chars': len(page), 'tables': len([b for b in ast['blocks'] if b['t'] == 'Table']),
            'images': nimgs, 'cjk_wrapped': nwrap, 'len': len(page)}


def run_manifest(path, only=None):
    items = json.load(open(path, encoding='utf-8'))
    out = []
    for it in items:
        if only and it['slug'] not in only:
            continue
        if it.get('skip'):
            out.append({'slug': it['slug'], 'skipped': it['skip']})
            continue
        if not os.path.exists(it['docx']):
            out.append({'slug': it['slug'], 'error': '文件不存在'})
            continue
        try:
            info = render_page(it['docx'], it['slug'], it.get('group', 'A'),
                               it.get('title'), it.get('seq'))
            out.append(info)
        except Exception as e:
            out.append({'slug': it['slug'], 'error': str(e)[:200]})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('docx', nargs='?')
    ap.add_argument('--slug')
    ap.add_argument('--group', default='A')
    ap.add_argument('--title')
    ap.add_argument('--seq', help='侧边栏序号，如 A1 / B6 / 附录 3')
    ap.add_argument('--manifest', help='JSON 清单，批量导入')
    ap.add_argument('--only', help='只处理这些 slug（逗号分隔）')
    args = ap.parse_args()

    if args.manifest:
        only = set(args.only.split(',')) if args.only else None
        for info in run_manifest(args.manifest, only):
            print(json.dumps(info, ensure_ascii=False))
        return

    if not args.docx or not args.slug:
        ap.error('需要 docx + --slug，或用 --manifest')
    print(json.dumps(render_page(args.docx, args.slug, args.group, args.title, args.seq),
                     ensure_ascii=False))


if __name__ == '__main__':
    main()
