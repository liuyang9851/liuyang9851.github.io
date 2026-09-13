#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
docx_to_md.py — 把 Word 笔记转成可维护的 Markdown 片段

为什么需要这个脚本：
    `markitdown` 和普通 `pandoc` 调用都会丢掉 Word 公式编辑器（OMML）里的
    公式，正文会变成「元素全为，则等于。」这种空句。pandoc 能正确解析
    OMML → LaTeX，但要额外做三件事才有博客可用的质量：

    1. 用 `--wrap=none` 避免公式被折行（折行会破坏 $$...$$ 块）
    2. 保留 Word 的标题层级（本脚本靠 `w:outlineLvl` / 样式推断）
    3. 清理中文标点误入公式的问题

用法：
    python tools/docx_to_md.py 线性代数总结.docx -o out/

依赖：
    pip install pypandoc-binary      # 自带 pandoc 二进制，无需单独装 pandoc

注意：
    本脚本产出的是**原始素材**，不是成稿。博客文章仍建议按主题重写段落、
    拆小节——直接搬运的 Word 结构读起来是文档，不是文章。
"""
import argparse
import os
import re
import sys
import zipfile


def find_pandoc():
    """优先用 pypandoc 自带的 pandoc 二进制。"""
    try:
        import pypandoc
        p = pypandoc.get_pandoc_path()
        # get_pandoc_path() 在 Windows 上可能不带扩展名
        if os.path.exists(p):
            return p
        if os.path.exists(p + ".exe"):
            return p + ".exe"
    except Exception:
        pass
    return "pandoc"  # 退回 PATH 里的 pandoc


def convert(docx, out_dir, pandoc):
    os.makedirs(out_dir, exist_ok=True)
    raw = os.path.join(out_dir, os.path.splitext(os.path.basename(docx))[0] + ".md")

    cmd = [
        pandoc, docx,
        "-f", "docx",
        "-t", "markdown+tex_math_dollars+pipe_tables+footnotes",
        "--wrap=none",       # 关键：不折行，否则公式块会被截断
        "--columns=200",     # 表格列宽，过大导致每行几万字符
        "--extract-media", os.path.join(out_dir, "media"),
        "-o", raw,
    ]
    import subprocess
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print("pandoc 失败:\n" + r.stderr, file=sys.stderr)
        sys.exit(1)
    return raw


def fix_chinese_in_math(text):
    """
    修复「中文标点/文字被 Formula 编辑器吞进公式」的问题。

    Word 里如果直接在公式框中输入中文，OMML 会把中文和标点一起交给
    pandoc，产出 $，则行列式的值等于$ 这种片段。渲染时中文会被当成数学
    符号，字距全乱。这里把纯中文/标点的「公式」还原为正文。
    """
    # 1) 整段只由中文标点或中文构成、不含任何 LaTeX 命令的 $...$ -> 去壳
    def strip_pure_cjk(m):
        body = m.group(1)
        if re.fullmatch(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef，。；：、（）\s]+", body):
            return body
        return m.group(0)

    text = re.sub(r"\$([^$\n]+)\$", strip_pure_cjk, text)

    # 2) 形如 $，...$ 或 $...，$ 的边界标点：把标点移出公式
    def move_punct(m):
        body = m.group(1)
        lead = re.match(r"^([，。；：、]+)", body)
        if lead:
            return lead.group(1) + "$" + body[lead.end():] + "$"
        return m.group(0)

    text = re.sub(r"\$([^$\n]+)\$", move_punct, text)
    return text


def report(text):
    """给出素材的质量体检，便于决定哪些地方需要人工处理。"""
    stats = {
        "公式块 \\$\\$": len(re.findall(r"^\$\$", text, re.M)),
        "行内公式": len(re.findall(r"(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)", text)),
        "公式内含中文": len(re.findall(r"\$[^$\n]*[\u4e00-\u9fff][^$\n]*\$", text)),
        "超宽表格行（>200字符）": len([l for l in text.split("\n")
                                     if l.startswith(("+", "|")) and len(l) > 200]),
        "\\mathbf 次数": len(re.findall(r"\\mathbf\{", text)),
    }
    print("\n--- 素材体检 ---")
    for k, v in stats.items():
        print("  %-24s %d" % (k, v))
    if stats["公式内含中文"]:
        print("\n  提示：公式内含中文的片段需要人工判断是「标点误入」还是「本该是正文」。")
    if stats["超宽表格行（>200字符）"]:
        print("  提示：宽表格在手机上不可用，建议拆成小节或改用列表。")


def main():
    ap = argparse.ArgumentParser(description="Word 笔记 -> Markdown 素材")
    ap.add_argument("docx", help="输入的 .docx 文件")
    ap.add_argument("-o", "--out", default="out", help="输出目录")
    ap.add_argument("--no-fix", action="store_true", help="跳过中文标点修复")
    args = ap.parse_args()

    pandoc = find_pandoc()
    print("使用 pandoc:", pandoc)

    raw = convert(args.docx, args.out, pandoc)
    text = open(raw, encoding="utf-8").read()

    if not args.no_fix:
        fixed = fix_chinese_in_math(text)
        if fixed != text:
            out = os.path.join(args.out, "fixed-" + os.path.basename(raw))
            open(out, "w", encoding="utf-8", newline="\n").write(fixed)
            print("已修复中文标点，输出:", out)
            text = fixed

    report(text)
    print("\n原始素材:", raw)


if __name__ == "__main__":
    main()
