#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""hs_manifest.py — 扫描 D:\\数学\\高中数学笔记 下的 A / B / 附录，生成 tools/hs_manifest.json。

清单里每条记录一份 .docx 的：源文件、页面 slug、分组、侧边栏序号、标题，
hs_import.py --manifest 直接吃这个文件批量导入。

    python -X utf8 tools/hs_manifest.py

注意跳过 Word 的 `~$xxx.docx` 锁文件（文档打开时才会出现，pandoc 转不了）。
"""
import glob
import json
import os
import re

ROOT = r'D:\数学\高中数学笔记'
out = []
used = {}


def slug_for(base):
    s = re.sub(r'[^0-9a-zA-Z]+', '-', base).strip('-').lower()
    if s in used:
        used[s] += 1
        s = f'{s}-{used[s]}'
    else:
        used[s] = 1
    return s


# A 类
for path in sorted(glob.glob(os.path.join(ROOT, 'A', 'A*.docx'))):
    name = os.path.basename(path)
    if name.startswith('~$'):
        continue
    m = re.match(r'A(\d+)\s+(.+)\.docx$', name)
    n, title = m.group(1), m.group(2)
    out.append({'docx': path.replace('\\', '/'), 'slug': f'hs-a{int(n):02d}',
                'group': 'A', 'seq': f'A{int(n)}', 'title': title})

# B 类
seen = {}
for path in sorted(glob.glob(os.path.join(ROOT, 'B', 'B*.docx'))):
    name = os.path.basename(path)
    if name.startswith('~$'):
        continue
    m = re.match(r'B(\d+)\s+(.+)\.docx$', name)
    if m:
        n, title = int(m.group(1)), m.group(2)
        key = f'b{n:02d}'
        seen[key] = seen.get(key, 0) + 1
        slug = f'hs-b{n:02d}' + (chr(ord('a') + seen[key] - 1) if seen[key] > 1 else '')
        out.append({'docx': path.replace('\\', '/'), 'slug': slug, 'group': 'B',
                    'seq': f'B{n}', 'title': title})
    else:
        m2 = re.match(r'Bx\s+(.+)\.docx$', name)
        if m2:
            out.append({'docx': path.replace('\\', '/'), 'slug': 'hs-bx', 'group': 'B',
                        'seq': 'Bx', 'title': m2.group(1)})

# 附录
app_files = [p for p in sorted(glob.glob(os.path.join(ROOT, '附录', '*.docx')))
             if not os.path.basename(p).startswith('~$')]
for i, path in enumerate(app_files, 1):
    name = os.path.basename(path)
    title = re.sub(r'^附录[：:]\s*', '', name[:-5]).strip()
    out.append({'docx': path.replace('\\', '/'), 'slug': f'hs-app{i:02d}', 'group': '附录',
                'seq': f'附录 {i}', 'title': title})

# 按 slug 排序，A → B → 附录
order = {'A': 0, 'B': 1, '附录': 2}
out.sort(key=lambda x: (order[x['group']], x['slug']))
open('tools/hs_manifest.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
print(f'共 {len(out)} 份')
for it in out:
    print(f"  {it['seq']:<7} {it['slug']:<12} {it['title']}")
