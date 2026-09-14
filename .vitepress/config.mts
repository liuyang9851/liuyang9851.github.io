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
  title: '刘扬的博客',
  description: '学习笔记与技术记录',

  // 本仓库是用户主页仓库（<username>.github.io），站点根路径为 /，
  // 因此**不需要**设置 base。若将来换成普通仓库，才需要加 base: '/仓库名/'。
  // 源码在仓库根目录，所以显式指定 srcDir 与 outDir。
  srcDir: '.',
  outDir: '.vitepress/dist',

  // 仓库根目录放了很多非页面文件（README、发布说明、备份等），
  // 若不排除，VitePress 会把它们也渲染成公开页面。
  srcExclude: ['README.md', 'PUBLISHING.md', '*.bak', 'node_modules/**', 'tools/**', 'out/**'],

  markdown: {
    math: true,
    lineNumbers: false,

    config(md) {
      md.use(mathjax3, { tex: { macros } })

      /**
       * 用滚动容器包裹每个表格。
       *
       * 为什么不在 CSS 里做：VitePress 把整篇文章放进一个 wrapper div，
       * 用 `div:has(> table)` 这类选择器会误伤整个正文容器（实测把
       * 5202px 高的正文块设成了横向滚动区）。在渲染阶段精确包裹最可靠。
       */
      md.renderer.rules.table_open = () => '<div class="table-scroll"><table>'
      md.renderer.rules.table_close = () => '</table></div>'
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
            { text: '02 · 矩阵', link: '/notes/02-matrix' },
            { text: '03 · 向量与线性空间', link: '/notes/03-vector' },
            { text: '04 · 线性方程组', link: '/notes/04-linear-system' },
            { text: '05 · 特征值理论', link: '/notes/05-eigen' },
            { text: '06 · 二次型理论', link: '/notes/06-quadratic' }
          ]
        },
        {
          text: '信息论与最优化',
          items: [
            { text: '07 · 信息论基础', link: '/notes/07-information-theory' },
            { text: '08 · 最优化基础', link: '/notes/08-optimization' }
          ]
        },
        {
          text: '微积分',
          items: [
            { text: '09 · 极限', link: '/notes/09-limits' },
            { text: '10 · 导数与微分', link: '/notes/10-derivative' },
            { text: '11 · 积分', link: '/notes/11-integral' },
            { text: '12 · 微分方程', link: '/notes/12-ode' },
            { text: '13 · 重积分与曲线曲面积分', link: '/notes/13-multiple-integral' },
            { text: '14 · 级数', link: '/notes/14-series' }
          ]
        },
        {
          text: '其它数学',
          items: [
            { text: '15 · 三角类函数', link: '/notes/15-trigonometric' },
            { text: '16 · 解析几何', link: '/notes/16-analytic-geometry' },
            { text: '17 · 概率论与数理统计', link: '/notes/17-probability' }
          ]
        },
        {
          text: '大学物理',
          items: [
            { text: '22 · 质点运动学', link: '/notes/22-mechanics-kinematics' },
            { text: '23 · 质点动力学与刚体', link: '/notes/23-mechanics-dynamics' },
            { text: '24 · 振动与波动', link: '/notes/24-oscillation-wave' },
            { text: '25 · 狭义相对论', link: '/notes/25-relativity' },
            { text: '26 · 热学', link: '/notes/26-thermodynamics' },
            { text: '27 · 静电场', link: '/notes/27-electrostatics' },
            { text: '28 · 磁场', link: '/notes/28-magnetism' },
            { text: '29 · 电磁感应与电磁波', link: '/notes/29-induction-maxwell' },
            { text: '30 · 光学', link: '/notes/30-optics' },
            { text: '31 · 量子物理', link: '/notes/31-quantum' }
          ]
        },
        {
          text: '微积分（完整版）',
          items: [
            { text: '32 · 函数再研究', link: '/notes/32-calc-functions' },
            { text: '33 · 极限与泰勒公式', link: '/notes/33-calc-limits' },
            { text: '34 · 导数与微分', link: '/notes/34-calc-differential' },
            { text: '35 · 最值与微分中值定理', link: '/notes/35-calc-optimization' },
            { text: '36 · 不定积分', link: '/notes/36-calc-antiderivative' },
            { text: '37 · 定积分及其应用', link: '/notes/37-calc-definite-integral' },
            { text: '38 · 微分方程（一阶）', link: '/notes/38-calc-ode-first' },
            { text: '39 · 高阶线性微分方程', link: '/notes/39-calc-ode-higher' },
            { text: '40 · 重积分与曲线曲面积分', link: '/notes/40-calc-multiple-integral' },
            { text: '41 · 级数', link: '/notes/41-calc-series' }
          ]
        },
        {
          text: '编程与工具',
          items: [
            { text: '18 · 数据库系统概论', link: '/notes/18-database' },
            { text: '19 · Java 笔记', link: '/notes/19-java' },
            { text: '20 · Linux 笔记', link: '/notes/20-linux' },
            { text: '21 · Vim 操作手册', link: '/notes/21-vim' }
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
