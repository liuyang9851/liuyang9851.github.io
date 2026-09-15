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
import zipfile

ROOT = r'D:\数学\高中数学笔记'
out = []
used = {}


def body_stats(path):
    """不开 Word、不跑 pandoc，直接从 .docx 里数正文文字/表格/公式/图片。

    有几份文档是**空壳**（只有标题和几个小标题，正文一个字没写，例如
    「附录：放缩常用不等式」「附录：高等数学速通」）。这种直接标 skip，
    否则站点上会出现两页只有标题的空白页。

    判据不能只看字数 —— 「附录：三角公式速查表」「圆锥曲线硬解定理表」正文
    几乎全是公式和表格，`<w:t>` 里没几个字。表格 / OMML 公式 / 图片任一存在
    就算有内容。
    """
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            xml = z.read('word/document.xml').decode('utf-8', 'ignore')
            media = sum(1 for n in names if n.startswith('word/media/'))
            embed = sum(1 for n in names if n.startswith('word/embeddings/'))
    except Exception:
        return {}
    return {
        'chars': len(re.sub(r'\s+', '', ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', xml)))),
        'tables': len(re.findall(r'<w:tbl[ >]', xml)),
        'math': len(re.findall(r'<m:oMath[ >]', xml)),
        'media': media,
        'embed': embed,
    }


def add(item):
    s = body_stats(item['docx'])
    if (s.get('chars', 0) < 200 and not s.get('media') and not s.get('embed')
            and not s.get('tables') and not s.get('math')):
        item['skip'] = (f"空壳文档：正文 {s.get('chars', 0)} 字，"
                        '无表格/公式/图片，源文件里就没内容')
    out.append(item)


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
    add({'docx': path.replace('\\', '/'), 'slug': f'hs-a{int(n):02d}',
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
        add({'docx': path.replace('\\', '/'), 'slug': slug, 'group': 'B',
                    'seq': f'B{n}', 'title': title})
    else:
        m2 = re.match(r'Bx\s+(.+)\.docx$', name)
        if m2:
            add({'docx': path.replace('\\', '/'), 'slug': 'hs-bx', 'group': 'B',
                        'seq': 'Bx', 'title': m2.group(1)})

# 附录
app_files = [p for p in sorted(glob.glob(os.path.join(ROOT, '附录', '*.docx')))
             if not os.path.basename(p).startswith('~$')]
for i, path in enumerate(app_files, 1):
    name = os.path.basename(path)
    title = re.sub(r'^附录[：:]\s*', '', name[:-5]).strip()
    add({'docx': path.replace('\\', '/'), 'slug': f'hs-app{i:02d}', 'group': '附录',
                'seq': f'附录 {i}', 'title': title})

# 按 slug 排序，A → B → 附录
order = {'A': 0, 'B': 1, '附录': 2}
out.sort(key=lambda x: (order[x['group']], x['slug']))
open('tools/hs_manifest.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
print(f'共 {len(out)} 份，其中空壳跳过 {sum(1 for i in out if "skip" in i)} 份')
for it in out:
    mark = '  [skip] ' + it['skip'] if 'skip' in it else ''
    print(f"  {it['seq']:<7} {it['slug']:<12} {it['title']}{mark}")
