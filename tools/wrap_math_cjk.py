#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
wrap_math_cjk.py — 把公式里的中文包进 \\text{}。

为什么需要：MathJax 对数学环境里的中文会走字体回退，直接写
`$$...np非整...$$` 虽然能显示，但和正文里的中文不是一个排法；
而 `\\text{非整}` 才是正确的「公式里的正文字」。仓库里既有笔记大多已经这么写
（notes/17-probability.md 里 17 个含中文的公式，14 个用了 \\text{}），
但 Word 素材是裸露的 —— 从素材重做表格时会把这条约定冲掉，所以补这一道。

只处理数学环境内部，且**跳过已经包在 \\text{...} 里的部分**，所以可以反复运行。

用法：
    python tools/wrap_math_cjk.py table.html                 # 打印结果
    python tools/wrap_math_cjk.py table.html -o out.html
    python tools/wrap_math_cjk.py notes/x.md --in-place
"""
import argparse
import re
import sys

CJK = re.compile(r'[\u3000-\u303f\u4e00-\u9fff\uff00-\uffef]+')


def is_cjk(ch):
    return bool(CJK.match(ch))


def wrap_span(tex):
    """给一段公式（不含 $ 定界符）里的中文加 \\text{}。"""
    out = []
    i = 0
    n = len(tex)
    text_depth = 0        # 当前是否在 \text{...} 里（以及嵌套层级）
    brace_stack = []      # 记录每个 { 是不是 \text{ 开的
    while i < n:
        ch = tex[i]
        if tex.startswith('\\text{', i) or tex.startswith('\\text {', i):
            # 进入 \text{...}
            j = tex.index('{', i)
            out.append(tex[i:j + 1])
            brace_stack.append(True)
            text_depth += 1
            i = j + 1
            continue
        if ch == '{':
            out.append(ch)
            brace_stack.append(False)
            i += 1
            continue
        if ch == '}':
            out.append(ch)
            if brace_stack:
                was_text = brace_stack.pop()
                if was_text:
                    text_depth -= 1
            i += 1
            continue
        if ch == '\\':
            # 反斜杠命令整体抄过去（避免把 \begin{array} 之类拆开）
            m = re.match(r'\\[A-Za-z]+|\\.', tex[i:])
            if m:
                out.append(m.group(0))
                i += len(m.group(0))
                continue
        if is_cjk(ch) and text_depth == 0:
            m = CJK.match(tex, i)
            out.append('\\text{' + m.group(0) + '}')
            i = m.end()
            continue
        out.append(ch)
        i += 1
    return ''.join(out)


def transform(text):
    """扫描整段文本，只改 $...$ / $$...$$ 内部。"""
    out = []
    i = 0
    n = len(text)
    count = 0
    while i < n:
        ch = text[i]
        if ch == '\\' and i + 1 < n:
            out.append(text[i:i + 2])
            i += 2
            continue
        if ch == '$':
            delim = '$$' if text.startswith('$$', i) else '$'
            end = text.find(delim, i + len(delim))
            if end == -1:
                out.append(ch)
                i += 1
                continue
            inner = text[i + len(delim):end]
            wrapped = wrap_span(inner)
            if wrapped != inner:
                count += 1
            out.append(delim + wrapped + delim)
            i = end + len(delim)
            continue
        out.append(ch)
        i += 1
    return ''.join(out), count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('file')
    ap.add_argument('-o', '--out')
    ap.add_argument('--in-place', action='store_true')
    args = ap.parse_args()

    text = open(args.file, encoding='utf-8').read()
    result, count = transform(text)

    if args.in_place:
        open(args.file, 'w', encoding='utf-8').write(result)
        sys.stderr.write(f'{args.file}: 处理了 {count} 个公式\n')
    elif args.out:
        open(args.out, 'w', encoding='utf-8').write(result)
        sys.stderr.write(f'wrote {args.out}: 处理了 {count} 个公式\n')
    else:
        sys.stdout.write(result)
        sys.stderr.write(f'处理了 {count} 个公式\n')


if __name__ == '__main__':
    main()
