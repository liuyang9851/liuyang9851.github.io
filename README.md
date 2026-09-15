# liuyang9851.github.io

个人博客与学习笔记。基于 VitePress 构建，公式用 MathJax 渲染，托管在 GitHub Pages。

线上地址：<https://liuyang9851.github.io/>

> 📘 **要手动发布 Word 笔记？看 [PUBLISHING.md](./PUBLISHING.md)**
> —— 完整流程、文件放哪、复杂格式怎么写、出问题怎么查。

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
├─ public/
│  └─ .nojekyll            让 GitHub Pages 跳过 Jekyll 处理
├─ tools/
│  ├─ docx_to_md.py        Word → Markdown 素材转换
│  ├─ grid_table_to_html.py 素材里的表格 → 带合并单元格的 HTML
│  ├─ wrap_math_cjk.py     公式里的中文包 \text{}
│  ├─ validate-math.mjs    离线校验所有 TeX 表达式能否渲染
│  ├─ validate-tables.mjs  校验手写表格是否显式写了 <tbody>
│  └─ validate-config.mjs  校验宏定义是否真的生效
├─ index.md                首页
├─ about.md                关于本站
└─ README.md               本文件（已在 srcExclude 中排除，不会发布成页面）
```

> **本仓库是用户主页仓库**（`<username>.github.io`），站点根路径是 `/`，
> 所以 config 里**不能**设 `base`。若以后改用普通仓库，
> 才需要加 `base: '/仓库名/'`。

## 发布

推送到 `main` 即自动构建并部署，**无需手动构建，也不需要提交任何产物**。

站点来源设置：仓库 **Settings → Pages → Build and deployment → Source**
必须是 **GitHub Actions**。

```bash
# 日常更新流程
# 1. 编辑 notes/ 下的 markdown
npm run check      # 离线校验全部公式（可选但强烈建议）
git add -A
git commit -m "docs: 新增第 02 章"
git push           # 推送后自动部署，约 1 分钟生效
```

线上地址：<https://liuyang9851.github.io/>

### 认证方式：已使用 SSH

本仓库的 `origin` 已配置为 SSH，**不需要任何 token，push 时不会提示输入凭据**：

```
origin  git@github.com:liuyang9851/liuyang9851.github.io.git
```

> ⚠️ **在新机器上克隆时，记得也用 SSH 地址**，否则会退回 HTTPS
> 并重新遇到下面那些凭据问题：
>
> ```bash
> git clone git@github.com:liuyang9851/liuyang9851.github.io.git
> ```
>
> 已有 HTTPS 克隆时，一条命令切换：
>
> ```bash
> git remote set-url origin git@github.com:liuyang9851/liuyang9851.github.io.git
> ```

**SSH 相比 HTTPS + token 的好处**（本项目踩过的坑，SSH 全部规避）：

- 没有 token 过期、scope 不足的问题
- 不受「OAuth App token 不能推送 workflow 文件」的限制
- 不受 Git Credential Manager 缓存旧凭据的影响
- 想给仓库加新 workflow 时无需处理任何权限

**换机器时怎么配 SSH**：

```bash
# 1. 生成密钥（已有可跳过）
ssh-keygen -t ed25519 -C "你的邮箱"

# 2. 把公钥加到 GitHub：https://github.com/settings/keys
#    复制 ~/.ssh/id_ed25519.pub 的全部内容

# 3. 验证
ssh -T git@github.com
# 看到 "Hi <用户名>! You've successfully authenticated" 即成功
# （返回 exit code 1 是正常的，GitHub 不提供 shell 访问）
```

### 如果网络限制导致 22 端口不通

部分网络会封 SSH 的 22 端口。GitHub 提供 **SSH over 443**，在
`~/.ssh/config` 里加一段即可：

```
Host github.com
  HostName ssh.github.com
  Port 443
  User git
```

验证：`ssh -T git@github.com`

> 注意：SSH 本身**不解决**「完全连不上 github.com」的问题。
> 如果网络需要代理，SSH 也要单独走代理，可加：
> `ProxyCommand connect -H 127.0.0.1:7897 %h %p`
> 或者干脆继续用 HTTPS（HTTPS 更容易走系统代理）。

### ⚠️ 若改用 HTTPS + token：token 类型有硬性限制

`.github/workflows/` 下的文件对凭据类型有要求。如果 push 报错：

```
refusing to allow an OAuth App to create or update workflow
`.github/workflows/deploy.yml` without `workflow` scope
```

**先看 token 前缀**，这比 scope 列表更能说明问题：

| 前缀          | 类型                                      | 能否推 workflow                       |
|---------------|-------------------------------------------|---------------------------------------|
| `ghp_`        | 经典 PAT                                  | ✅                                     |
| `gho_`        | OAuth App token（`gh auth login` 产生的） | ❌ 即使 scope 里有 `workflow` 也会被拒 |
| `github_pat_` | 细粒度 PAT                                | ❌ 不支持该权限                        |

必须用 `ghp_` 开头的经典 token，权限勾 `repo` + `workflow`，
创建链接：<https://github.com/settings/tokens/new?scopes=repo,workflow>

另外注意 **Git Credential Manager 会缓存旧凭据**，新建 token 后如果 push 仍然失败，
大概率是它在用缓存。清除方式：

```bash
"protocol=https`nhost=github.com`n`n" | git credential reject
```

或者临时显式指定凭据绕过缓存：

```bash
git push https://liuyang9851:你的token@github.com/liuyang9851/liuyang9851.github.io main
```


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

### 从 Word 搬表格：两个必踩的坑

**一、合并单元格的结构只存在于 pandoc 的 grid table 里。**
素材里的表格是 `+---+---+` 画出来的，分隔线在哪里断开就代表哪里合并。
如果只把单元格内容抄成 `<th>` 平铺，合并信息就丢了：行标签会跑到第 1 列、
整行合并的公式会挤进第 1 格。用工具还原：

```bash
python tools/grid_table_to_html.py out/概率论与数理统计.md --list      # 看有哪些表
python tools/grid_table_to_html.py out/概率论与数理统计.md --n 2 -o t2.html
python tools/wrap_math_cjk.py t2.html -o t2.html                       # 公式里的中文包 \text{}
```

（不要直接用 `pandoc -t html`：它会把 TeX 数学转成 HTML/Unicode，LaTeX 全丢。）

**二、手写 `<table>` 必须显式写 `<tbody>`。**
浏览器解析 `<table><tr>` 时会自动补一个 `<tbody>`，而 Vue 编译出的 vnode 树里没有，
两边结构不一致 → hydration mismatch → Vue 重建整张表。而 VitePress 客户端加载的
lean 产物里，静态子树是 `createStaticVNode('', n)` 占位 —— 重建时占位里的空字符串
被真的插进去，**表格里的公式就会在闪现一次后全部变成空白**（容器、尺寸、可见性
全都正常，只是没有笔画，常规排查根本看不出来）。
`npm run check` 里的 `validate-tables.mjs` 会拦住这种表。

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
npm run check                    # 公式渲染 + 表格 + 配置，一次跑完
node tools/validate-math.mjs     # 扫描 notes/ 下所有 .md 的 TeX
node tools/validate-tables.mjs   # 手写表格是否都写了 <tbody>
node tools/validate-config.mjs   # 确认宏定义生效
npm run build                    # 确认能构建
```

`validate-math.mjs` 会把每条公式离线渲染一遍。**这一步很重要**：MathJax 是
浏览器端渲染，TeX 写错了 `npm run build` 照样成功，只有打开页面才会看到
一片红色报错。脚本会在提交前把这类错误挡下来，并打印 文件:行号。
