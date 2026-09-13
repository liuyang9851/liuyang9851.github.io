// 校验所有笔记里的 TeX 表达式能否被 MathJax 正确渲染。
//
// 为什么需要它：MathJax 是**浏览器端渲染**，TeX 写错了 `vitepress build`
// 依然会成功，只有打开页面才会看到一片红色报错。这个脚本在构建前离线
// 把它逐条渲染一遍，把错误挡在提交之前。
//
// 用法：
//   node tools/validate-math.mjs            # 扫描 notes/ 下所有 .md
//   node tools/validate-math.mjs a.md b.md  # 只校验指定文件
import fs from 'node:fs'
import path from 'node:path'

const ROOT = path.resolve(import.meta.dirname, '..')
const NOTES_DIR = path.join(ROOT, 'notes')

function collectMarkdown() {
  const args = process.argv.slice(2)
  if (args.length) return args.map(a => path.resolve(a))
  if (!fs.existsSync(NOTES_DIR)) return []
  return fs.readdirSync(NOTES_DIR)
    .filter(f => f.endsWith('.md'))
    .map(f => path.join(NOTES_DIR, f))
}

// ---- 搭建 MathJax 渲染环境 -------------------------------------------------
const { mathjax } = await import('mathjax-full/js/mathjax.js')
const { TeX } = await import('mathjax-full/js/input/tex.js')
const { SVG } = await import('mathjax-full/js/output/svg.js')
const { liteAdaptor } = await import('mathjax-full/js/adaptors/liteAdaptor.js')
const { RegisterHTMLHandler } = await import('mathjax-full/js/handlers/html.js')
const { AllPackages } = await import('mathjax-full/js/input/tex/AllPackages.js')

const adaptor = liteAdaptor()
RegisterHTMLHandler(adaptor)

// 宏定义必须与实际渲染用的完全一致，否则会出现「这里校验通过、
// 浏览器里却渲染失败」。为杜绝两份定义漂移，这里直接从 config.mts 解析。
function loadMacros() {
  const cfg = fs.readFileSync(path.join(ROOT, '.vitepress', 'config.mts'), 'utf8')
  const block = cfg.match(/export const macros\s*=\s*\{([\s\S]*?)\n\}/)
  if (!block) {
    console.error('无法从 .vitepress/config.mts 解析 macros，请检查该导出是否存在')
    process.exit(1)
  }
  const macros = {}
  for (const m of block[1].matchAll(/(\w+)\s*:\s*'((?:[^'\\]|\\.)*)'/g)) {
    macros[m[1]] = m[2].replace(/\\\\/g, '\\')
  }
  return macros
}

const macros = loadMacros()
console.log('已从 config.mts 载入宏：', Object.keys(macros).join(' '))

const tex = new TeX({ packages: AllPackages, macros })
const svg = new SVG({ fontCache: 'local' })
const doc = mathjax.document('', { InputJax: tex, OutputJax: svg })

function render(src, display) {
  const out = adaptor.outerHTML(doc.convert(src, { display }))
  return out
}

// ---- 抽取表达式 -----------------------------------------------------------
function extract(md) {
  const exprs = []
  for (const m of md.matchAll(/\$\$([\s\S]+?)\$\$/g)) exprs.push(['display', m[1], m.index])
  const withoutDisplay = md.replace(/\$\$[\s\S]+?\$\$/g, m => ' '.repeat(m.length))
  for (const m of withoutDisplay.matchAll(/(?<!\$)\$([^$\n]+)\$(?!\$)/g)) {
    exprs.push(['inline', m[1], m.index])
  }
  return exprs
}

function lineOf(md, index) {
  return md.slice(0, index).split('\n').length
}

// ---- 主流程 ---------------------------------------------------------------
const files = collectMarkdown()
if (!files.length) {
  console.log('没有找到待校验的 Markdown 文件')
  process.exit(0)
}

let totalOk = 0
const failures = []

for (const file of files) {
  const md = fs.readFileSync(file, 'utf8')
  const exprs = extract(md)
  const rel = path.relative(ROOT, file)
  let ok = 0

  for (const [kind, src, index] of exprs) {
    try {
      const out = render(src, kind === 'display')
      if (out.includes('merror') || out.includes('data-mjx-error')) {
        failures.push([rel, lineOf(md, index), kind, src.trim(), 'MathJax 报错'])
      } else {
        ok++
      }
    } catch (e) {
      failures.push([rel, lineOf(md, index), kind, src.trim(), String(e.message)])
    }
  }
  totalOk += ok
  console.log(`  ${rel.padEnd(34)} ${String(ok).padStart(3)}/${String(exprs.length).padEnd(3)} 通过`)
}

console.log()
console.log('渲染成功 :', totalOk)
console.log('失败     :', failures.length)
for (const [f, line, kind, src, err] of failures) {
  console.log(`\n  ✗ ${f}:${line}  [${kind}]`)
  console.log(`    ${src.slice(0, 100)}`)
  console.log(`    ${err.slice(0, 120)}`)
}

console.log()
console.log(failures.length === 0
  ? '✓ 所有 TeX 表达式均可正常渲染'
  : '✗ 存在无法渲染的公式，请修正后再提交')
process.exit(failures.length === 0 ? 0 : 1)
