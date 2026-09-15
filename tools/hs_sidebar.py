#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
hs_sidebar.py — 根据 notes/hs-*.md 自动生成「高中数学」侧边栏与总览页条目。

每导入一批新页面就跑一次：它扫描 notes/hs-*.md，按 slug 前缀（a/b/app）分组，
重写 .vitepress/config.mts 里 `// >>> hs-notes` 与 `// <<< hs-notes` 之间的内容，
以及 notes/index.md 里 `<!-- >>> hs-notes -->` 与 `<!-- <<< hs-notes -->` 之间的内容。

slug 约定：
    hs-a01   A 类（基础）
    hs-b01   B 类（拓展）
    hs-app01 附录
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, 'notes')
CONFIG = os.path.join(ROOT, '.vitepress', 'config.mts')
INDEX = os.path.join(NOTES, 'index.md')

GROUPS = [
    ('a', '高中数学（A · 基础）'),
    ('b', '高中数学（B · 拓展）'),
    ('app', '高中数学（附录）'),
]


def title_of(path):
    text = open(path, encoding='utf-8').read()
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', text, re.M)
    return m.group(1) if m else os.path.splitext(os.path.basename(path))[0]


def seq_of(path):
    text = open(path, encoding='utf-8').read()
    m = re.search(r'^hs_seq:\s*"?(.*?)"?\s*$', text, re.M)
    return m.group(1).strip() if m else ''


def collect():
    pages = {}
    for name in sorted(os.listdir(NOTES)):
        m = re.match(r'^hs-(app|\w)(\d+)-?.*\.md$', name)
        if not m:
            continue
        kind = 'app' if m.group(1) == 'app' else m.group(1)
        slug = name[:-3]
        num = int(m.group(2))
        full = os.path.join(NOTES, name)
        pages.setdefault(kind, []).append((num, slug, title_of(full), seq_of(full)))
    for k in pages:
        # 按序号排，序号相同按 slug（B1 有两个文件）
        pages[k].sort(key=lambda x: (x[0], x[1]))
    return pages


def build_sidebar(pages):
    out = []
    for kind, label in GROUPS:
        items = pages.get(kind) or []
        if not items:
            continue
        out.append('        {')
        out.append("          text: '%s'," % label)
        out.append('          collapsed: true,')
        out.append('          items: [')
        for num, slug, title, seq in items:
            text = (seq + ' · ' + title) if seq else (str(num) + ' · ' + title)
            out.append("            { text: %s, link: '/notes/%s' }," %
                       (repr(text).replace('\\', '\\\\'), slug))
        out.append('          ]')
        out.append('        },')
    text = '\n'.join(out)
    return ('        // >>> hs-notes（下面三段由 tools/hs_sidebar.py 自动生成，勿手改）\n'
            + text + '\n'
            + '        // <<< hs-notes')


def build_index(pages):
    lines = ['<!-- >>> hs-notes（由 tools/hs_sidebar.py 自动生成） -->', '', '## 高中数学', '']
    for kind, label in GROUPS:
        items = pages.get(kind) or []
        if not items:
            continue
        lines.append('### ' + label)
        lines.append('')
        lines.append('| 序号 | 主题 | 核心内容 |')
        lines.append('| --- | --- | --- |')
        for num, slug, title, seq in items:
            lines.append('| [%s · %s](./%s) | %s | 见正文 |' % (seq or num, title, slug, title))
        lines.append('')
    lines.append('<!-- <<< hs-notes -->')
    return '\n'.join(lines)


def replace_between(text, start_marker, end_marker, new):
    a = text.find(start_marker)
    b = text.find(end_marker)
    if a < 0 or b < 0:
        raise SystemExit(f'找不到标记 {start_marker} / {end_marker}')
    b += len(end_marker)
    return text[:a] + new + text[b:]


def main():
    pages = collect()
    total = sum(len(v) for v in pages.values())
    cfg = open(CONFIG, encoding='utf-8').read()
    cfg = replace_between(cfg, '        // >>> hs-notes', '        // <<< hs-notes', build_sidebar(pages))
    open(CONFIG, 'w', encoding='utf-8').write(cfg)

    idx = open(INDEX, encoding='utf-8').read()
    if '<!-- >>> hs-notes' in idx:
        idx = replace_between(idx, '<!-- >>> hs-notes', '<!-- <<< hs-notes', build_index(pages))
    else:
        idx = idx.rstrip() + '\n\n' + build_index(pages) + '\n'
    open(INDEX, 'w', encoding='utf-8').write(idx)
    print(f'侧边栏/总览已更新：A {len(pages.get("a", []))} 篇，B {len(pages.get("b", []))} 篇，'
          f'附录 {len(pages.get("app", []))} 篇，共 {total} 篇')


if __name__ == '__main__':
    main()
