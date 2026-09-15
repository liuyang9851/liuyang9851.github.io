# 手动发布流程

把 Word 笔记转成 Markdown 并发布到 <https://liuyang9851.github.io/> 的完整步骤。

---

## 一、最短流程（5 步）

```powershell
cd D:\Programming\liuyang9851.github.io

# 1. 转换 Word（生成素材 + 体检报告）
python tools\docx_to_md.py "D:\数学\大学数学笔记\线性代数总结.docx" -o out

# 2. 手动整理：把要发布的内容写进 notes\03-vector.md
#    （不是直接复制素材，见第三节）

# 3. 自检（公式语法 + 宏定义）
npm run check

# 4. 本地预览，确认排版
npm run dev          # 浏览器打开 http://localhost:5173

# 5. 发布
git add -A
git commit -m "docs: 新增第 03 章 向量与线性空间"
git push
```

push 之后约 1 分钟自动上线（GitHub Actions 构建）。**不需要手动构建，也不需要提交任何产物。**

> `origin` 已配置为 SSH，push 时不会要求输入密码或 token。

---

## 二、推送后确认部署

打开 <https://github.com/liuyang9851/liuyang9851.github.io/actions>

看到 **Deploy to GitHub Pages** 变成绿色 ✓ 就成功了。红色 ✗ 说明构建失败，
点进去看日志——最常见的原因是公式写错（见第五节）。

**如果构建失败，线上还是旧版本**，不会发布半成品。

---

## 三、文件和目录放哪里

| 你的内容 | 放到 | 说明 |
| --- | --- | --- |
| 章节正文 | `notes/03-vector.md` | 命名用 `NN-主题.md`，两位数编号 |
| 图片 | `public/images/xxx.png` | 引用写 `/images/xxx.png`（绝对路径） |
| 笔记总览 | `notes/index.md` | 手动加一行到章节表 |
| 侧边栏 | `.vitepress/config.mts` | 手动加一条 `items` |
| 首页卡片 | `index.md` | 可选 |

### 新建章节后必须登记两处

**1. `notes/index.md` 的章节表：**

```markdown
| [03 · 向量与线性空间](./03-vector) | 向量 | 线性相关性、极大无关组、秩 |
```

**2. `.vitepress/config.mts` 的 sidebar：**

```ts
sidebar: {
  '/notes/': [
    {
      text: '线性代数',
      items: [
        { text: '总览', link: '/notes/' },
        { text: '01 · 行列式', link: '/notes/01-determinant' },
        { text: '02 · 矩阵', link: '/notes/02-matrix' },
        { text: '03 · 向量与线性空间', link: '/notes/03-vector' }   // ← 加这行
      ]
    }
  ]
}
```

漏了第 1 处：总览页看不到入口。
漏了第 2 处：左侧边栏没有这一章，读者进得去但出不来。

---

## 四、每篇文章的固定开头

```markdown
---
title: 向量与线性空间
description: 一句话摘要，会显示在搜索结果里。
---

# 03 · 向量与线性空间

[[toc]]

正文从这里开始……
```

- `title`：标签页标题，也是侧边栏/hover 显示的文本
- `description`：搜索引擎摘要，不写会退回站点默认描述
- `[[toc]]`：自动生成本页目录（基于 `##` `###`）
- 标题用 `#`，小节用 `##`，不要跳级

---

## 五、公式：唯一的硬性约束

这是**唯一会导致部署失败**的地方。MathJax 是浏览器端渲染，
`npm run check` 会离线把每条公式渲染一遍，写错了会在本地就报出来并指出**文件:行号**。

### 常用写法

```markdown
行内公式：设 $\A$ 为 $n$ 阶方阵

独立成行（居中显示）：
$$
\A^{-1} = \frac{1}{|\A|}\A^{*}
$$
```

`$$` 必须**单独占一行**，且前后各留一个空行。

### 用宏，不要手写 \mathbf

已有宏（在全站可用）：`\A \B \C \D \E \I \O \P \T \L \x \y \zero \Eij \Eic \Eijc \tr \rk \diag \rank`

```latex
\A\x = \B          ✅ 简洁
\mathbf{A}\mathbf{x} = \mathbf{B}    ❌ 冗长
```

要新增宏，改 `.vitepress/config.mts` 里的 `export const macros`，
然后**必须**跑 `npm run check` —— 它会验证每个宏的渲染结果与定义是否一致。

> ⚠️ 这个检查不是走过场。开发第 02 章时，我把 `rk` 误定义成
> `\operatorname{r}`（少了个 k），全文 `\rk(\A)` 都渲染成 `r(A)`。
> 语法完全合法，只有宏探针能抓出来。

### 中文标点不要放进公式

```markdown
❌  $，则行列式的值等于$        ← 中文被当数学符号，字距全乱
✅  ，则行列式的值等于 $0$
```

批量转换后常见这个问题，`docx_to_md.py` 会自动修一部分，剩下的要人工看。

---

## 六、更复杂的格式怎么处理

### 表格

普通 Markdown 表格即可：

```markdown
| 类型 | 操作 |
| --- | --- |
| 第一类 | 对调两行 |
```

**注意**：表格在手机上放不下时会横向滚动（已在
`.vitepress/theme/custom.css` 处理），所以可以放心用宽表。

**但不要**在单元格里塞长公式——单元格宽度会很难看。长公式单独成行写在表格下方。

### 折叠块 / 提示框

VitePress 专有语法，**只在 VitePress 里有效，粘到 GitHub 上会显示成纯文本**：

```markdown
::: tip 记忆方式
三个反序的都是矩阵结果，行列式是数值结果。
:::

::: warning 原文笔误
原文写的是「仍是对角阵」，应为「仍是三角阵」。
:::

::: details 点开看证明
（长推导放这里，默认折叠）
:::
```

可用类型：`tip` `info` `warning` `danger` `details`

### 定理 / 定义排版

第 01、02 章的惯例：

- 定理、性质用**加粗引导词**：`**定理。** 若……`
- 容易记混的地方加一个 `::: tip` 提示
- 原文有笔误的地方加 `::: warning` 并在文末汇总

参考 `notes/02-matrix.md` 的写法。

### 图片

```markdown
![描述文字](/images/determinant.png)
```

图片放 `public/images/`，引用路径以 `/` 开头（不要写 `./` 或 `../`）。

### 数学上标 / 下标 / 希腊字母

```latex
\A^{T}  \A^{-1}  a_{ij}  \alpha \beta \lambda \Lambda
```

---

## 七、Word 转换的已知局限

`tools\docx_to_md.py` 用 pandoc 解析 OMML 公式，能保住全部公式，
但下面这些必须人工处理：

| 问题 | 表现 | 处理 |
| --- | --- | --- |
| 中文标点进公式 | `$，则行列式的值等于$` | 把标点移出 `$` |
| 手工画的表格 | 单元格错位、单行几百字符 | 重画成 Markdown 表格 |
| 分式写成斜杠 | `- b_i/a_i` | 改成 `-\frac{b_i}{a_i}` |
| 中文被打进公式框 | `$证明：$` | 移到正文 |
| 空模板表 | 只有表头没内容 | 直接删掉 |

**素材不是成稿。** 直接发布的 Word 结构读起来是文档而不是文章——
第 01、02 章都做了重写：拆小节、补证明思路、把性质做成速查表。

---

## 八、命令速查

```powershell
npm run dev            # 本地预览（改完即时刷新）
npm run check          # 公式 + 宏自检 ← 推送前必跑
npm run build          # 只构建，不部署（CI 会自动做）
npm run preview        # 预览构建产物

npm run check          # 等价于下面四条依次执行：
#   node tools/probe-macros.mjs      宏定义是否写对
#   node tools/validate-math.mjs     所有公式能否渲染
#   node tools/validate-config.mjs   宏配置是否生效
#   node tools/validate-tables.mjs   手写表格是否都写了 <tbody>

git push               # 发布
```

### 整个文件夹批量上线（高中数学笔记那类）

```powershell
python -X utf8 tools\hs_manifest.py             # 扫 A / B / 附录，生成 tools\hs_manifest.json
python -X utf8 tools\hs_import.py --manifest tools\hs_manifest.json --only hs-a01,hs-a02
python -X utf8 tools\hs_sidebar.py              # 重生成侧边栏 + notes/index.md
python -X utf8 tools\hs_check.py                # 对账：docx 表数 == 页面表数
node tools\verify-pages.mjs hs-a01 hs-a02       # 浏览器验收（公式没被 hydration 吃掉）
```

`hs_import.py` 是**整篇由 pandoc JSON AST 渲染**的：pandoc 的 markdown writer 会把
带合并单元格的表压成 pipe table（合并全丢），还会**整张丢掉畸形表格**，
所以它的 markdown 结果一概不用，只借它抽图片。

---

## 九、出问题怎么办

| 现象 | 原因 | 处理 |
| --- | --- | --- |
| Actions 红色 ✗ | 公式写错 | 看日志定位，本地 `npm run check` 复现 |
| 页面公式显示成红色 | TeX 语法错 | 同上 |
| 表格里公式闪一下就空白 | 手写表漏了 `<tbody>`，hydration 重建表格 | `npm run check` 会报；补 `<tbody>` |
| 表格内容错位、标签跑到别的列 | 搬 Word 表格时丢了合并单元格 | 用 `tools/grid_table_to_html.py` 从素材还原 |
| 新章节侧边栏没有 | 忘了登记 config.mts | 见第三节 |
| 页面 404 | 文件名和 link 不一致 | 检查文件名大小写 |
| 中文变成方块 | 少见，字体未加载 | 刷新；仍不行看 CSS |
| push 被拒 | 极少数网络问题 | 见 README 的凭据排查表 |
| 导入后少了一张表 | pandoc markdown writer 会丢掉畸形表格 | 已改为 AST 渲染；`tools/hs_check.py` 对账 |
| 行内公式变成居中大公式 | pandoc 3 的 `Math` 类型是对象，字符串比较失效 | 用 `docx_table_to_html.math_kind()` |
| 构建报 `Rollup failed to resolve import ...wmf` | Word 里的矢量图是 .wmf/.emf，浏览器不认 | `hs_import.py` 会自动转 PNG |

**构建失败不会影响线上**——线上保持上一个成功版本，可以从容修复。
