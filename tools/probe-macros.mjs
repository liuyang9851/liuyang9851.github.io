/**
 * 宏定义渲染探针
 *
 * 存在的理由：`validate-math.mjs` 只检查公式**是否报错**，但写错宏定义
 * 是不会报错的——例如把 rk 定义成 \operatorname{r}，渲染出的就是 r(A)，
 * 语法完全合法却是错的。这个脚本对比「宏渲染结果」与「展开后的字面写法」
 * 是否逐字节一致，从而抓住这类静默错误。
 *
 * 用法：node tools/probe-macros.mjs
 */
import MarkdownIt from 'markdown-it'
import mathjax3 from 'markdown-it-mathjax3'
import fs from 'node:fs'
import path from 'node:path'

const ROOT = path.resolve(import.meta.dirname, '..')

function loadMacros() {
  const cfg = fs.readFileSync(path.join(ROOT, '.vitepress', 'config.mts'), 'utf8')
  const block = cfg.match(/export const macros\s*=\s*\{([\s\S]*?)\n\}/)
  if (!block) {
    console.error('无法从 config.mts 解析 macros')
    process.exit(1)
  }
  const out = {}
  for (const m of block[1].matchAll(/(\w+)\s*:\s*'((?:[^'\\]|\\.)*)'/g)) {
    out[m[1]] = m[2].replace(/\\\\/g, '\\')
  }
  return out
}

const macros = loadMacros()
const md = new MarkdownIt().use(mathjax3, { tex: { macros } })

const render = tex => md.render('$' + tex + '$')

// 每个宏都必须满足：\name 的渲染结果 === 其定义展开后的渲染结果
// 这能抓出「宏指向了错误的定义」这类静默 bug。
let failures = []

console.log('=== 1. 每个宏的展开一致性 ===')
for (const [name, def] of Object.entries(macros)) {
  const viaMacro = render('\\' + name)
  const viaDef = render(def)
  const same = viaMacro === viaDef
  if (!same) {
    // 给出可读的诊断：宏实际渲染出的字符码 vs 定义渲染出的字符码
    const codes = h => [...h.matchAll(/data-c="([0-9A-F]+)"/g)]
      .map(m => String.fromCodePoint(parseInt(m[1], 16))).join('')
    failures.push(name)
    console.log(`  ✗ \\${name}  宏渲染=[${codes(viaMacro)}]  定义渲染=[${codes(viaDef)}]`)
  } else {
    console.log(`  ✓ \\${name}`)
  }
}

console.log()
console.log('=== 2. 关键宏的语义抽查 ===')
const expectations = [
  ['\\A', '\\mathbf{A}', '粗体 A'],
  ['\\L', '\\mathbf{\\Lambda}', '粗体 Lambda'],
  ['\\rk(\\A)', '\\operatorname{rk}(\\A)', 'rk 正体算子'],
  ['\\tr(\\A)', '\\operatorname{tr}(\\A)', 'tr 正体算子'],
  ['\\diag\\{a\\}', '\\operatorname{diag}\\{a\\}', 'diag 正体算子'],
  ['\\Eij', '\\mathbf{E}(i,j)', '初等矩阵 E(i,j)'],
  ['\\A\\x = \\B', '\\mathbf{A}\\mathbf{x} = \\mathbf{B}', '矩阵方程'],
]
for (const [viaMacro, viaDef, desc] of expectations) {
  const ok = render(viaMacro) === render(viaDef)
  if (!ok) failures.push(desc)
  console.log(`  ${ok ? '✓' : '✗'} ${desc}`)
}

console.log()
if (failures.length) {
  console.log('✗ 发现 ' + failures.length + ' 处问题：' + failures.join(', '))
  process.exit(1)
}
console.log('✓ 全部 ' + Object.keys(macros).length + ' 个宏渲染正确')
