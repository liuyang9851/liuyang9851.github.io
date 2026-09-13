// Verify the exact macro option shape used in docs/.vitepress/config.mts
// actually reaches MathJax through markdown-it-mathjax3.
import MarkdownIt from 'markdown-it'
import mathjax3 from 'markdown-it-mathjax3'

const macros = {
  A: '\\mathbf{A}', B: '\\mathbf{B}', I: '\\mathbf{I}',
  x: '\\mathbf{x}', zero: '\\mathbf{0}'
}

const md = new MarkdownIt().use(mathjax3, { tex: { macros } })

const cases = [
  ['macro', '$\\A\\x = \\B$'],
  ['explicit', '$\\mathbf{A}\\mathbf{x} = \\mathbf{B}$'],
  ['builtin-accents', '$\\I \\A$'],
  ['source-formula', '$\\sum_{k=1}^{n}a_{ki}A_{kj}$'],
  ['cases-env', '$$\\sum_{k=1}^{n}a_{ki}A_{kj}=\\begin{cases}D, & i=j\\\\0, & i\\neq j\\end{cases}$$']
]

let bad = 0
for (const [name, src] of cases) {
  const html = md.render(src)
  const err = html.includes('merror') || html.includes('data-mjx-error') ||
              html.includes('MathJax:')
  if (err) bad++
  console.log(name.padEnd(18), err ? 'ERROR' : 'ok')
}

// decisive: does \A produce the same SVG as \mathbf{A}?
const m = md.render('$\\A$')
const e = md.render('$\\mathbf{A}$')
const norm = s => s.replace(/\s+/g, ' ').trim()
console.log()
console.log('\\A === \\mathbf{A} :', norm(m) === norm(e))
console.log('  \\A        ->', norm(m).slice(0, 100))
console.log('  \\mathbf{A}->', norm(e).slice(0, 100))

// and confirm it does NOT render as an accent (which is what builtin \A would do)
console.log()
console.log('contains mjx-accent (builtin \\A behaviour):', m.includes('mjx-accent'))

console.log()
console.log(bad === 0 && norm(m) === norm(e)
  ? 'CONFIG MACROS WORK'
  : 'CONFIG MACROS NOT APPLIED')
