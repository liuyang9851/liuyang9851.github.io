import { defineConfig } from 'vitepress'
import mathjax3 from 'markdown-it-mathjax3'

/**
 * 全站 TeX 宏定义。
 *
 * 原始 Word 笔记中矩阵/向量是粗体、标量是常规体，这个区别有语义，
 * 转换后得到大量 \mathbf{...}。这里给常用符号起单字母别名：
 *
 *     \A  ===  \mathbf{A}
 *
 * 想统一改数学字体样式（例如全站换成 \boldsymbol 或 \mathbb），
 * 只改这一处即可。
 *
 * 注意：这个对象被 tools/validate-math.mjs 引用，保证校验用的宏与
 * 实际渲染用的宏永远一致——两边写两份迟早会漂移。
 */
export const macros = {
  A: '\\mathbf{A}',
  B: '\\mathbf{B}',
  C: '\\mathbf{C}',
  D: '\\mathbf{D}',
  E: '\\mathbf{E}',
  I: '\\mathbf{I}',
  O: '\\mathbf{O}',
  P: '\\mathbf{P}',
  T: '\\mathbf{T}',
  L: '\\mathbf{\\Lambda}',
  x: '\\mathbf{x}',
  y: '\\mathbf{y}',
  zero: '\\mathbf{0}',
  // 初等矩阵与常用运算符
  Eij: '\\mathbf{E}(i,j)',
  Eic: '\\mathbf{E}(i(c))',
  Eijc: '\\mathbf{E}(i,j(c))',
  tr: '\\operatorname{tr}',
  rk: '\\operatorname{rk}',
  diag: '\\operatorname{diag}',
  rank: '\\operatorname{rank}'
}

/**
 * 站点配置
 */
export default defineConfig({
  lang: 'zh-CN',
  title: '刘洋的博客',
  description: '学习笔记与技术记录',

  // 本仓库是用户主页仓库（<username>.github.io），站点根路径为 /，
  // 因此**不需要**设置 base。若将来换成普通仓库，才需要加 base: '/仓库名/'。
  // 源码在仓库根目录，所以显式指定 srcDir 与 outDir。
  srcDir: '.',
  outDir: '.vitepress/dist',

  // 仓库根目录放了很多非页面文件（README、许可证、备份等），
  // 若不排除，VitePress 会把它们也渲染成公开页面。
  srcExclude: ['README.md', '*.bak', 'node_modules/**', 'tools/**'],

  markdown: {
    math: true,
    lineNumbers: false,

    config(md) {
      md.use(mathjax3, { tex: { macros } })
    }
  },

  themeConfig: {
    outline: { level: [2, 3], label: '本页目录' },

    nav: [
      { text: '首页', link: '/' },
      { text: '笔记', link: '/notes/' }
    ],

    sidebar: {
      '/notes/': [
        {
          text: '线性代数',
          items: [
            { text: '总览', link: '/notes/' },
            { text: '01 · 行列式', link: '/notes/01-determinant' },
            { text: '02 · 矩阵', link: '/notes/02-matrix' }
          ]
        }
      ]
    },

    docFooter: { prev: '上一篇', next: '下一篇' },

    search: { provider: 'local' },

    lastUpdated: {
      text: '最后更新于',
      formatOptions: { dateStyle: 'short', timeStyle: 'short' }
    }
  }
})
