// verify-pages.mjs — 浏览器验收（静态 HTML 里看不出来的问题都在这里）。
//
// 为什么非要开浏览器：VitePress 的 lean 构建会把表格换成 createStaticVNode 占位，
// 页面 hydration 时若结构对不上（典型原因是手写 <table> 少了 <tbody>），
// 占位符会被重新插成空节点 —— 静态 HTML 里公式好好的，浏览器里却全没了。
//
// 每篇检查：公式数（与 dist 里的静态 HTML 对比，少了就是被 hydration 吃掉）、
// 空白公式、空表、没包 .table-scroll 的裸表格、断图、横向溢出（docW ≤ winW）。
//
// 用法（先起静态服务器，例如 npx http-server .vitepress/dist -p 4180）：
//     node tools/verify-pages.mjs hs-a01 hs-a02
//
// 只依赖 Node 内置能力（fetch + WebSocket）+ 本机 chrome-headless-shell；
// 换机器要改下面的 CHROME 路径。
import { spawn } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { setTimeout as sleep } from 'node:timers/promises';

const CHROME = 'C:/Users/ZhangHu/AppData/Local/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-win64/chrome-headless-shell.exe';
const BASE = 'http://127.0.0.1:4180';
const PORT = 9333;

const slugs = process.argv.slice(2);

const chrome = spawn(CHROME, [
  '--headless', `--remote-debugging-port=${PORT}`, '--no-sandbox',
  '--disable-gpu', '--window-size=1280,900', 'about:blank',
], { stdio: 'ignore' });

async function cdpTarget() {
  for (let i = 0; i < 60; i++) {
    try {
      // 注意：/json/version 给的是 **browser** 目标的 socket，它没有 Page 域；
      // 要连页面目标（about:blank），得走 /json/list。
      const r = await fetch(`http://127.0.0.1:${PORT}/json/list`);
      const list = await r.json();
      const page = list.find((t) => t.type === 'page' && t.webSocketDebuggerUrl);
      if (page) return page.webSocketDebuggerUrl;
    } catch { /* 还没起来 */ }
    await sleep(250);
  }
  throw new Error('chrome 没起来');
}

class Session {
  constructor(ws) { this.ws = ws; this.id = 0; this.pending = new Map(); }
  static async open(url) {
    const ws = new WebSocket(url);
    await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
    const s = new Session(ws);
    ws.onmessage = (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id && s.pending.has(msg.id)) {
        const { res, rej } = s.pending.get(msg.id);
        s.pending.delete(msg.id);
        msg.error ? rej(new Error(JSON.stringify(msg.error))) : res(msg.result);
      }
    };
    return s;
  }
  send(method, params = {}) {
    const id = ++this.id;
    this.ws.send(JSON.stringify({ id, method, params }));
    return new Promise((res, rej) => {
      this.pending.set(id, { res, rej });
      setTimeout(() => { if (this.pending.delete(id)) rej(new Error(method + ' 超时')); }, 30000);
    });
  }
}

const EXPR = `(() => {
  const q = (s) => document.querySelectorAll(s).length;
  const mjx = [...document.querySelectorAll('mjx-container')];
  const empty = mjx.filter(c => !c.querySelector('svg path, svg use, svg g')).length;
  const tables = [...document.querySelectorAll('.vp-doc table')];
  const badTable = tables.filter(t => t.querySelectorAll('th,td').length === 0).length;
  const de = document.documentElement;
  return {
    mjx: mjx.length, empty,
    tables: tables.length, badTable,
    rawTable: q('.vp-doc > table'),
    winW: window.innerWidth, docW: Math.max(de.scrollWidth, document.body.scrollWidth),
    title: document.querySelector('.vp-doc h1')?.textContent || '',
    images: [...document.querySelectorAll('.vp-doc img')].filter(i => !i.complete || i.naturalWidth === 0).length,
  };
})()`;

try {
  const wsUrl = await cdpTarget();
  const sess = await Session.open(wsUrl);
  await sess.send('Page.enable');
  await sess.send('Runtime.enable');
  let bad = 0;
  for (const slug of slugs) {
    const url = `${BASE}/notes/${slug}`;
    // 构建产物里的公式数（MathJax 是构建期渲染的）：hydration 把表格内容清空的话，
    // 页面上的公式数会比静态 HTML 少一块。
    let staticMjx = -1;
    try {
      const html = readFileSync(`.vitepress/dist/notes/${slug}.html`, 'utf8');
      staticMjx = html.split('<mjx-container').length - 1;
    } catch { /* 文件不在就跳过这项 */ }
    await sess.send('Page.navigate', { url });
    await sleep(2500);
    const { result } = await sess.send('Runtime.evaluate', { expression: EXPR, returnByValue: true });
    const r = result.value;
    const over = r.docW > r.winW + 1;
    const lost = staticMjx >= 0 && r.mjx < staticMjx;
    const ok = r.empty === 0 && r.badTable === 0 && r.rawTable === 0 && !over && r.images === 0 && !lost;
    if (!ok) bad++;
    console.log(
      `${ok ? 'ok  ' : 'FAIL'} ${slug.padEnd(9)} 公式=${String(r.mjx).padStart(4)}/${staticMjx}` +
      ` 空白公式=${r.empty} 表格=${String(r.tables).padStart(3)} 空表=${r.badTable} 裸table=${r.rawTable}` +
      ` 断图=${r.images} docW=${r.docW} winW=${r.winW} ${r.title}${lost ? ' <<< hydration 吃掉了公式' : ''}`);
  }
  console.log(bad === 0 ? '全部通过' : `${bad} 篇有问题`);
  process.exitCode = bad === 0 ? 0 : 1;
} finally {
  chrome.kill();
}
