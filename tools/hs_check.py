#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""hs_check.py — 导入后的对账：docx 里的顶层表格数 vs 页面里渲染出来的表数。

导入工具最怕「悄悄少一张表」——pandoc 的 markdown writer 就会整张丢掉畸形表格，
所以每批导完都跑一遍这个：表数一致、图片路径都已改写成 /images/... 才算过。

    python -X utf8 tools/hs_check.py            # 全部
    python -X utf8 tools/hs_check.py hs-a03     # 指定几篇
"""
import json
import os
import re
import sys

import pypandoc

sys.path.insert(0, 'tools')

items = json.load(open('tools/hs_manifest.json', encoding='utf-8'))
only = sys.argv[1:]
bad = 0
for it in items:
    if only and it['slug'] not in only:
        continue
    if not os.path.exists(it['docx']):
        print('缺文件', it['slug'], it['docx'])
        continue
    ast = json.loads(pypandoc.convert_file(it['docx'], 'json', format='docx'))
    blocks = ast['blocks']
    ntab = sum(1 for b in blocks if b['t'] == 'Table')
    types = {}
    for b in blocks:
        types[b['t']] = types.get(b['t'], 0) + 1
    if not os.path.exists(f'notes/{it["slug"]}.md'):
        print(f'{it["slug"]:10s} 还没导入（顶层表={ntab}）')
        continue
    md = open(f'notes/{it["slug"]}.md', encoding='utf-8').read()
    html_tab = md.count('<div class="table-scroll">')
    imgs = len(re.findall(r'!\[[^\]]*\]\(', md))
    raw_img = len(re.findall(r'!\[[^\]]*\]\(media/', md))
    flag = '' if (ntab == html_tab and raw_img == 0) else '  <<< 对不上'
    if flag:
        bad += 1
    print(f'{it["slug"]:10s} 顶层表={ntab:2d} 页面表={html_tab:2d} 图片={imgs:2d} '
          f'未改写图={raw_img} 块={types}{flag}')
print('对不上的文档数:', bad)
sys.exit(1 if bad else 0)
