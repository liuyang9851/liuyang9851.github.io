// 检查每个手写 HTML 表格是否显式写了 <tbody>。
//
// 为什么必须检查：VitePress 会把 markdown 编译成 Vue 组件，客户端加载的是
// 「lean」版本——里面的静态子树被替换成 createStaticVNode('', n) 占位，
// 靠 hydration 复用服务端已渲染好的 DOM。
//
// 但浏览器解析 <table><tr> 时会**自动补一个 <tbody>**，而 Vue 编译出来的
// vnode 树里没有 <tbody>。两边结构不一致 → hydration mismatch → Vue 丢掉
// 服务端 DOM、按 vnode 重建整张表 → 占位里的空字符串被真的插进去 →
// 表格内所有 MathJax 公式（公式字形是静态子树）**在一瞬间的闪现之后变成空白**。
//
// 显式写 <tbody> 让两边结构一致，公式就不会消失。实测：
// 概率论「分布函数」表漏写 <tbody>，整张表 31 个公式全部变空白。
import fs from 'node:fs'
import path from 'node:path'

const ROOT = process.cwd()
const SKIP_DIRS = new Set(['node_modules', '.vitepress', '.git', 'out', 'tools', 'public'])

function walk(dir, out = []) {
  for (const name of fs.readdirSync(dir)) {
    if (SKIP_DIRS.has(name)) continue
    const p = path.join(dir, name)
    const st = fs.statSync(p)
    if (st.isDirectory()) walk(p, out)
    else if (name.endsWith('.md')) out.push(p)
  }
  return out
}

const files = walk(ROOT).sort()
let checked = 0
const bad = []

for (const file of files) {
  const src = fs.readFileSync(file, 'utf8')
  const re = /<table>[\s\S]*?<\/table>/g
  let m
  while ((m = re.exec(src))) {
    checked++
    const block = m[0]
    if (/<tbody[\s>]/.test(block)) continue
    const line = src.slice(0, m.index).split('\n').length
    const math = (block.match(/\$\$?/g) || []).length
    bad.push({ file: path.relative(ROOT, file), line, math })
  }
}

console.log(`手写 HTML 表格 : ${checked} 个`)
console.log(`缺 <tbody>     : ${bad.length} 个`)

if (bad.length) {
  console.log()
  for (const b of bad) {
    console.log(`  ✗ ${b.file}:${b.line}  （表内 $ 符号 ${b.math} 个）`)
  }
  console.log()
  console.log('请在 <table> 后补 <tbody>、在 </table> 前补 </tbody>。')
  console.log('否则该表内的公式会在页面加载后被 Vue hydration 清成空白。')
  process.exit(1)
}

console.log()
console.log('✓ 所有手写 HTML 表格都显式声明了 <tbody>')
