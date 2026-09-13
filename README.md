# liuyang9851.github.io

个人博客与学习笔记。基于 VitePress 构建，公式用 MathJax 渲染，托管在 GitHub Pages。

线上地址：<https://liuyang9851.github.io/>

## 快速开始

```bash
npm install
npm run dev        # 本地预览 http://localhost:5173
npm run build      # 构建到 .vitepress/dist
npm run preview    # 预览构建结果
```

## 目录结构

```
.
├─ .vitepress/
│  ├─ config.mts           站点配置 + 全站 TeX 宏定义（export const macros）
│  └─ dist/                构建产物（已 gitignore，由 CI 生成）
├─ .github/workflows/
│  └─ deploy.yml           推送到 main 后自动构建并发布
├─ notes/
│  ├─ index.md             笔记总览
│  └─ 01-determinant.md    第 01 章：行列式
├─ tools/
│  ├─ docx_to_md.py        Word → Markdown 素材转换
│  ├─ validate-math.mjs    离线校验所有 TeX 表达式能否渲染
│  └─ validate-config.mjs  校验宏定义是否真的生效
├─ index.md                首页
├─ about.md                关于本站
└─ README.md               本文件（已在 srcExclude 中排除，不会发布成页面）
```

> **本仓库是用户主页仓库**（`<username>.github.io`），站点根路径是 `/`，
> 所以 config 里**不能**设 `base`。若以后改用普通仓库，
> 才需要加 `base: '/仓库名/'`。

## 发布

推到 `main` 即自动部署（`.github/workflows/deploy.yml`）。

首次需要在仓库 **Settings → Pages → Build and deployment → Source** 选择
**GitHub Actions**。之后每次 push 会自动构建并发布，无需手动操作。

## 写作约定

### 公式用宏，别手写 \mathbf

`config.mts` 里 `export const macros` 定义了全站宏：

```latex
\A \x = \B          % 等价于 \mathbf{A}\mathbf{x} = \mathbf{B}
```

已定义：`\A \B \C \D \E \I \O \P \T \x \y \zero`

原始笔记中矩阵/向量是粗体、标量是常规体，这个区别有语义，所以不能把
`\mathbf` 一律删掉。用宏改写后源码可读性大幅提升；将来想统一换数学字体
（例如全站改成 `\boldsymbol`），只改 `config.mts` 一处即可。

### 中文标点不要放进公式

Word 公式编辑器会把中文标点一起吞进公式，转换后得到
`$，则行列式的值等于$`。渲染时中文会被当成数学符号，字距全乱。正确写法：

```markdown
❌  $，则行列式的值等于$
✅  ，则行列式的值等于 $0$
```

### 表格宽度

Markdown 表格在手机上过宽会横向溢出。汇总性大表建议改成小节 + 列表，
或用 `::: details` 折叠。

## 迁移笔记

```bash
python tools/docx_to_md.py "D:/数学/大学数学笔记/线性代数总结.docx" -o out/
```

输出 `out/线性代数总结.md`（原始素材）+ 体检报告。
**这是素材不是成稿**——直接搬运的 Word 结构读起来是文档而不是文章。
请参考第 01 章的做法：拆小节、补上下文、修公式缺陷，再放进 `notes/`。

新章节写完后，记得在 `.vitepress/config.mts` 的 `sidebar` 和
`notes/index.md` 的表格里登记。

## 提交前自检

```bash
node tools/validate-math.mjs     # 扫描 notes/ 下所有 .md 的 TeX
node tools/validate-config.mjs   # 确认宏定义生效
npm run build                    # 确认能构建
```

`validate-math.mjs` 会把每条公式离线渲染一遍。**这一步很重要**：MathJax 是
浏览器端渲染，TeX 写错了 `npm run build` 照样成功，只有打开页面才会看到
一片红色报错。脚本会在提交前把这类错误挡下来，并打印 文件:行号。
