/**
 * 方案 B 兜底：把构建产物落盘到 docs/，供 GitHub Pages 以
 * 「Deploy from a branch」方式直接发布，完全不需要 CI 权限。
 *
 * 什么时候用它：
 *   仓库凭据缺少 workflow scope、无法推送 .github/workflows/ 时使用。
 *
 * 用法：
 *   npm run build:pages
 *   git add docs && git commit -m "build: 更新站点" && git push
 *   仓库 Settings → Pages → Source 选 "Deploy from a branch"，main / /docs
 *
 * 注意：
 *   - 本项目的 VitePress 源码就在仓库根，而 docs/ 是纯产物目录。
 *     两者不重叠，所以不会互相干扰。
 *   - 根目录的 node_modules / .vitepress / tools 会被复制进 docs/，
 *     已由 docs/.gitignore 排除，不会进入提交。
 */
import fs from 'node:fs'
import path from 'node:path'
import { execSync } from 'node:child_process'

const ROOT = path.resolve(import.meta.dirname, '..')
const DIST = path.join(ROOT, '.vitepress', 'dist')
const TARGET = path.join(ROOT, 'docs')

console.log('1/3 构建站点…')
execSync('npm run build', { cwd: ROOT, stdio: 'inherit' })

if (!fs.existsSync(DIST)) {
  console.error('构建产物不存在：' + DIST)
  process.exit(1)
}

console.log('2/3 清空 docs/ …')
fs.rmSync(TARGET, { recursive: true, force: true })
fs.mkdirSync(TARGET, { recursive: true })

console.log('3/3 复制产物到 docs/ …')
fs.cpSync(DIST, TARGET, { recursive: true })

// .nojekyll 让 GitHub Pages 跳过 Jekyll 处理。
// 注意：public/.nojekyll 已由 VitePress 自动复制到产物根，
// 这里再补一次是为了防止 public/ 被删时静默失效。
fs.writeFileSync(path.join(TARGET, '.nojekyll'), '')

// docs/.gitignore：只让 docs/ 里的产物进入提交，
// 复制进来的源码目录会被排除掉。
fs.writeFileSync(
  path.join(TARGET, '.gitignore'),
  '/node_modules/\n/.vitepress/\n/tools/\n/public/\n/*.md\n!/404.html\n'
)

const count = (function walk(d) {
  let n = 0
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    n += e.isDirectory() ? walk(path.join(d, e.name)) : 1
  }
  return n
})(TARGET)

console.log(`\n完成：${count} 个文件已写入 docs/`)
console.log('接下来：')
console.log('  git add docs && git commit -m "build: 更新站点" && git push')
console.log('  Settings → Pages → Source 选 "Deploy from a branch"，main / /docs')
