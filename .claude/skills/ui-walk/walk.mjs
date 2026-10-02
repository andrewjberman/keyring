// /ui-walk walker: logs the Opal UI walker service account into the LOCAL dev build (localhost, `bun run dev:live`),
// walks pages like a person (search, tabs, dropdowns, expands, drill rows, account pickers), screenshots every step,
// and runs in-page checks for frontend defects. READ-ONLY by construction: a network guard aborts every request
// outside the admitted classes. Output goes to the gitignored tmp/ui-walk/<stamp>/ because screenshots carry
// client data.
//
// Usage (from any cwd):
//   node .claude/skills/ui-walk/walk.mjs [--base http://localhost:5174] [--route /investor-reporting]
//        [--client "Thiessen, Anna"]... [--max-minutes 40] [--no-arm] [--keep-armed] [--headed] [--no-login]
//        [--day "<security>=<YYYY-MM-DD>"]...
//        [--security "VLO US"]... [--thread "Valero"] [--deep]
//
// By default it ARMS the account, walks, and DISARMS in a finally block (always, even on failure).
import { createRequire } from 'node:module'
import { execFileSync } from 'node:child_process'
import { mkdirSync, writeFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import path from 'node:path'
import { isSignInPage } from './signin_detect.mjs'

// UI_WALK_ROOT lets a copy of this file in a linked worktree drive the shared tree's portal/node_modules and tmp/.
const ROOT = process.env.UI_WALK_ROOT || fileURLToPath(new URL('../../../', import.meta.url))
const require = createRequire(path.join(ROOT, 'portal', 'package.json'))
const { chromium } = require('playwright-core')
const ACCOUNT = path.join(ROOT, '.claude', 'skills', 'ui-walk', 'ui_walker_account.py')
const EMAIL = 'opal-ui-walker@opal.test'

// ---- args ---------------------------------------------------------------------------------------------------------
const argv = process.argv.slice(2)
const opt = { base: 'http://localhost:5174', routes: [], clients: [], securities: [], maxMinutes: 40, arm: true, keepArmed: false, headed: false, deep: false, login: true, settleExtraMs: 0, periodsPerAccount: false, days: [], thread: null, expectTexts: [], reloadReopen: false }
for (let i = 0; i < argv.length; i++) {
  const a = argv[i]
  if (a === '--base') opt.base = argv[++i]
  else if (a === '--route') {
    // Git Bash (MSYS) rewrites a leading-slash argv into "C:/Program Files/Git/<route>" before node sees it; undo that.
    opt.routes.push(argv[++i].replace(/^[A-Za-z]:[\\/].*?[\\/]Git(?=[\\/])/i, '').replace(/\\/g, '/'))
  }
  else if (a === '--client') opt.clients.push(argv[++i])
  else if (a === '--security') opt.securities.push(argv[++i])
  else if (a === '--thread') opt.thread = argv[++i]
  else if (a === '--max-minutes') opt.maxMinutes = Number(argv[++i])
  else if (a === '--no-arm') opt.arm = false
  else if (a === '--keep-armed') opt.keepArmed = true
  else if (a === '--headed') opt.headed = true
  else if (a === '--deep') opt.deep = true
  else if (a === '--model-scope') opt.modelScope = true
  else if (a === '--account-drill') opt.accountDrill = true
  else if (a === '--open-request') opt.openRequest = argv[++i]
  else if (a === '--composer-picker') opt.composerPicker = true
  else if (a === '--dashboard-window') opt.dashboardWindow = true
  // --press "<label>" (repeatable, plain routes only): press that tab/radio/button by its exact label after the load, wait
  // for the page to settle (PRESS_SETTLE_MS), shoot and check; a DO_NOT_CLICK word is refused. For a chart behind a tab.
  else if (a === '--press') (opt.presses = opt.presses || []).push(String(argv[++i] || ''))
  else if (a === '--holdings-aggregates') opt.holdingsAggregates = true
  else if (a === '--performance-state') opt.performanceState = true
  else if (a === '--expect-text') opt.expectTexts.push(String(argv[++i] || ''))
  else if (a === '--reload-reopen') opt.reloadReopen = true
  else if (a === '--no-login') opt.login = false
  // Extra wait after every settle, for a read whose answer lands after networkidle (a retained Performance
  // reopen fires after the account switch, so a 1200 ms settle screenshots "Loading"). Default 0: unchanged.
  else if (a === '--settle-extra-ms') opt.settleExtraMs = Number(argv[++i])
  else if (a === '--periods-per-account') opt.periodsPerAccount = true
  // --day "<security>=<YYYY-MM-DD>" (repeatable): open that name's timeline day by its date and record its article rows.
  else if (a === '--day') {
    const v = String(argv[++i] || '')
    const at = v.lastIndexOf('=')
    if (at < 1 || !/^\d{4}-\d{2}-\d{2}$/.test(v.slice(at + 1))) throw new Error('--day wants "<security>=<YYYY-MM-DD>", got ' + v)
    opt.days.push({ security: v.slice(0, at), date: v.slice(at + 1) })
  }
  else throw new Error('unknown argument ' + a)
}
if (!opt.routes.length) opt.routes.push('/investor-reporting')
if (!/^http:\/\/(localhost|127\.0\.0\.1):\d+$/.test(opt.base)) throw new Error('REFUSED: --base must be a localhost dev build (the protected dev channel)')
const deadline = Date.now() + opt.maxMinutes * 60000

const stamp = new Date().toISOString().replace(/[-:]/g, '').replace(/\..+/, 'Z')
const OUT = path.join(ROOT, 'tmp', 'ui-walk', stamp)
mkdirSync(path.join(OUT, 'shots'), { recursive: true })
const log = (...m) => console.log(new Date().toISOString().slice(11, 19), ...m)

// ---- account ------------------------------------------------------------------------------------------------------
const py = (cmd, extraEnv = {}, ...args) => execFileSync('python', [ACCOUNT, cmd, ...args], { encoding: 'utf8', env: { ...process.env, ...extraEnv }, stdio: ['ignore', 'pipe', 'pipe'] })

// ---- the network guard: the admitted classes ----------------------------------------------------------------------
const ADMITTED_POST = [/\/auth\/login$/, /\/auth\/refresh$/, /\/auth\/logout$/,
  /\/api\/scoped\/investor-reporting\/directory\/resolve$/, /\/api\/scoped\/investor-reporting\/selections$/]
const DO_NOT_CLICK = /export|generate|submit|upload|delete|remove|save|send|approve|execute|reset|sign ?out|log ?out|logout|create|contact support/i
const guard = []
const netlog = []
const apiIssues = []
const consoleErrors = []
const findings = []
const drillPaths = []
const leadLists = []
let shotN = 0
let stubbed = 0
let step = 'start'

function pathOnly(u) { try { const x = new URL(u); return x.pathname } catch { return u } }

async function shot(page, label) {
  shotN += 1
  const file = `shots/${String(shotN).padStart(3, '0')}-${label.replace(/[^a-z0-9]+/gi, '-').slice(0, 60)}.png`
  await page.screenshot({ path: path.join(OUT, file), fullPage: true }).catch((e) => log('shot failed', e.message.split('\n')[0]))
  return file
}

// ---- in-page checks -----------------------------------------------------------------------------------------------
const CHECKS = () => {
  const out = []; const vw = innerWidth; const vh = innerHeight
  const vis = (el) => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && s.opacity !== '0' }
  const trail = (el) => { const a = []; let e = el; for (let i = 0; e && e.tagName && i < 5; i++, e = e.parentElement) { let t = e.tagName.toLowerCase(); const ds = e.getAttribute('data-slot'); if (ds) t += `[data-slot=${ds}]`; else if (e.id) t += '#' + e.id; else if (e.getAttribute('role')) t += `[role=${e.getAttribute('role')}]`; a.unshift(t) } return a.join(' > ') }
  const box = (el) => { const r = el.getBoundingClientRect(); return [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)] }
  // 1. an open popover covered by another element (dropdowns behind nav bars)
  // elementFromPoint skips pointer-events:none, so a tooltip (pointer-events-none) read covered at every point
  // (DSGN_AMGTV1-Z-S11). Hit-test with pointer events on for this popover's subtree only, then restore
  // (round21/checks/hoverprobe.mjs's method).
  for (const p of [...document.querySelectorAll('[role=listbox],[role=menu],[role=dialog],[role=tooltip],[data-radix-popper-content-wrapper]')].filter(vis)) {
    const r = p.getBoundingClientRect(); let covered = 0; let by = null
    const pe = document.createElement('style')
    pe.textContent = '[data-walk-hit], [data-walk-hit] * { pointer-events: auto !important; }'
    p.setAttribute('data-walk-hit', ''); document.head.appendChild(pe)
    for (const fx of [0.2, 0.5, 0.8]) for (const fy of [0.1, 0.5, 0.9]) {
      const x = r.left + r.width * fx; const y = r.top + r.height * fy
      if (x < 0 || y < 0 || x >= vw || y >= vh) continue
      const top = document.elementFromPoint(x, y)
      if (top && !p.contains(top)) { covered++; by = by || top }
    }
    pe.remove(); p.removeAttribute('data-walk-hit')
    if (covered) out.push({ check: 'occluded-popover', observed: `${covered} of 9 sample points of an open ${p.getAttribute('role') || 'popover'} are covered by another element`, selector: trail(p), covered_by: by ? trail(by) : null, covered_by_text: by ? (by.innerText || '').trim().slice(0, 60) : null, rect: box(p), rule: 'an open dropdown renders above every page element (z-order)' })
  }
  // 2. unconnected fields, placeholders, raw codes, sample content
  // raw-code: any underscore-joined identifier, either case. The old pattern took only upper-case segments of 3+ chars,
  // so it read 0 on pages printing ey_ntm, cash_mv and VLO_US_Equity in prose (DSGN_AMGTV1 round-21 ruling 3).
  const pats = [[/\bnot supplied\b/i, 'not-supplied'], [/\bunavailable\b/i, 'unavailable'], [/\bvalue pending\b/i, 'value-pending'], [/^\s*unknown\s*$/i, 'unknown'], [/\bwithheld\b/i, 'withheld'], [/\bn\/a\b/i, 'n-a'], [/illustrative sample/i, 'sample-content'], [/\b[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+\b/, 'raw-code']]
  const seen = new Map(); const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT)
  while (tw.nextNode()) {
    const n = tw.currentNode; const t = n.nodeValue.trim(); const el = n.parentElement
    if (!t || !el || ['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(el.tagName) || !vis(el)) continue
    for (const [re, kind] of pats) if (re.test(t)) { const k = kind + '|' + t.slice(0, 80); const c = seen.get(k) || { n: 0, el, t }; c.n++; seen.set(k, c) }
  }
  for (const [k, c] of seen) {
    const kind = k.split('|')[0]
    const check = kind === 'raw-code' ? 'raw-code' : kind === 'sample-content' ? 'sample-content' : 'unconnected-field'
    out.push({ check, subtype: kind, observed: `"${c.t.slice(0, 120)}" x${c.n}`, selector: trail(c.el), rect: box(c.el), rule: check === 'raw-code' ? 'FWD-15: no raw system code on the face' : check === 'sample-content' ? 'no illustrative sample on a live page' : 'a field with no connection shows a placeholder (unconnected endpoint?)' })
  }
  // 3. duplicate choices in a list
  for (const lb of document.querySelectorAll('[role=listbox],[role=menu],select')) {
    if (lb.tagName !== 'SELECT' && !vis(lb)) continue
    const opts = [...lb.querySelectorAll('[role=option],[role=menuitem],option')].map((o) => (o.innerText || o.textContent || '').trim()).filter(Boolean)
    const cnt = {}; opts.forEach((o) => { cnt[o] = (cnt[o] || 0) + 1 })
    const d = Object.entries(cnt).filter(([, v]) => v > 1)
    if (d.length) out.push({ check: 'duplicate-options', observed: d.map(([k, v]) => `"${k.slice(0, 60)}" x${v}`).join('; '), options_total: opts.length, selector: trail(lb), rule: 'every choice in a list is distinguishable' })
  }
  // 4. more than one full-width navy band (#0A1733)
  const bands = [...document.querySelectorAll('body *')].filter((e) => getComputedStyle(e).backgroundColor === 'rgb(10, 23, 51)' && e.getBoundingClientRect().width > vw * 0.5 && e.getBoundingClientRect().height > 20 && vis(e))
  const topBands = bands.filter((b) => !bands.some((o) => o !== b && o.contains(b)))
  if (topBands.length > 1) out.push({ check: 'design:bands', observed: `${topBands.length} full-width #0A1733 bands`, selectors: topBands.slice(0, 8).map(trail), rule: 'DESIGN.md C3: one band per page' })
  // 5. low-contrast text
  const lum = (c) => { const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(',').map(Number); const [r, g, b] = p.slice(0, 3).map((v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4) }); return { L: 0.2126 * r + 0.7152 * g + 0.0722 * b, a: p.length > 3 ? p[3] : 1 } }
  const bgOf = (el) => { for (let e = el; e; e = e.parentElement) { const s = getComputedStyle(e); const l = lum(s.backgroundColor); if (l && l.a > 0.5) return { l, c: s.backgroundColor } } return { l: lum('rgb(244, 246, 250)'), c: 'rgb(244, 246, 250)' } }
  const low = []
  for (const el of document.querySelectorAll('body *')) {
    if (!vis(el) || ![...el.childNodes].some((n) => n.nodeType === 3 && n.nodeValue.trim())) continue
    const s = getComputedStyle(el); const f = lum(s.color); if (!f) continue
    const b = bgOf(el); const ratio = (Math.max(f.L, b.l.L) + 0.05) / (Math.min(f.L, b.l.L) + 0.05)
    if (ratio < 3.0) low.push({ text: (el.innerText || '').trim().slice(0, 50), ratio: +ratio.toFixed(2), color: s.color, background: b.c, selector: trail(el) })
  }
  if (low.length) out.push({ check: 'design:contrast', observed: `${low.length} text element(s) under 3:1 contrast`, samples: low.slice(0, 12), rule: 'portal colour law: no light text on light grounds (DESIGN.md C3/C5)' })
  // 6. tinted status blocks
  for (const el of document.querySelectorAll('[role=alert],[role=status],[data-slot*=error],[data-slot*=status]')) {
    if (!vis(el)) continue
    const bg = getComputedStyle(el).backgroundColor; const l = lum(bg)
    if (l && l.a > 0.05 && !['rgb(255, 255, 255)', 'rgb(244, 246, 250)', 'rgb(10, 23, 51)'].includes(bg)) out.push({ check: 'design:tinted-status', observed: `status/alert block with background ${bg}`, text: (el.innerText || '').trim().slice(0, 80), selector: trail(el), rule: 'DESIGN.md C12: a status is an icon beside navy text, never a tinted block' })
  }
  // 7. mixed money and date formats
  const body = document.body.innerText
  const money = [/USD\s?\d/.test(body) ? 'USD 1,234' : null, /\$\d/.test(body) ? '$1,234' : null].filter(Boolean)
  if (money.length > 1) out.push({ check: 'format:money', observed: `money written as ${money.join(' and ')} on one page`, rule: 'one money format' })
  const dates = [[/\b\d{4}-\d{2}-\d{2}\b/, '2026-09-22'], [/\b(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(st|nd|rd|th)?,? \d{4}/, 'September 22nd, 2026'], [/\b\d{2}\/\d{2}\/\d{4}\b/, '09/22/2026']].filter(([re]) => re.test(body)).map(([, e]) => e)
  if (dates.length > 1) out.push({ check: 'format:dates', observed: `${dates.length} date formats: ${dates.join(' | ')}`, rule: 'one date format' })
  // 8. charts: duplicate slice colours, one-slice pies, "Unknown" labels
  for (const svg of document.querySelectorAll('svg')) {
    if (!vis(svg)) continue
    const secs = [...svg.querySelectorAll('.recharts-pie-sector path, path.recharts-sector')]
    if (!secs.length) continue
    const fills = secs.map((p) => p.getAttribute('fill') || getComputedStyle(p).fill); const cnt = {}; fills.forEach((f) => { cnt[f] = (cnt[f] || 0) + 1 })
    const d = Object.entries(cnt).filter(([, v]) => v > 1)
    if (d.length) out.push({ check: 'chart:duplicate-colour', observed: `${secs.length} slices; ${d.map(([f, v]) => `${f} x${v}`).join('; ')}`, selector: trail(svg), rule: 'no two slices share a colour' })
    if (secs.length === 1) out.push({ check: 'chart:single-slice', observed: 'a pie with one slice', selector: trail(svg), rule: 'no one-slice pie (an unnecessary drill layer)' })
    const unk = [...svg.querySelectorAll('text')].filter((t) => /^unknown$/i.test(t.textContent.trim())).length
    if (unk) out.push({ check: 'chart:unknown-label', observed: `${unk} chart label(s) read "Unknown"`, selector: trail(svg), rule: 'chart labels match the table' })
  }
  // 9. truncated labels and horizontal page scroll
  const trunc = [...document.querySelectorAll('body *')].filter((e) => vis(e) && getComputedStyle(e).textOverflow === 'ellipsis' && e.scrollWidth > e.clientWidth + 1).slice(0, 10).map((e) => ({ text: (e.innerText || '').trim().slice(0, 60), selector: trail(e) }))
  if (trunc.length) out.push({ check: 'layout:truncated', observed: `${trunc.length} truncated label(s)`, samples: trunc, rule: 'labels are readable' })
  if (document.documentElement.scrollWidth > vw + 1) out.push({ check: 'layout:horizontal-scroll', observed: `page scrolls horizontally (${document.documentElement.scrollWidth}px > ${vw}px)`, rule: 'no horizontal page scroll' })
  return out
}

let walkVoid = false
class WalkVoid extends Error {}
async function checks(page, label) {
  if (label !== 'login-failed') {
    const probe = await page.evaluate(() => {
      const vis = (el) => { if (!el) return false; const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' }
      return { path: location.pathname, hasEmail: vis(document.querySelector('#email')), hasPassword: vis(document.querySelector('#password')) }
    }).catch(() => null)
    if (probe && isSignInPage(probe)) {
      walkVoid = true
      const file = await shot(page, label)
      findings.push({ step: label, screenshot: file, claim: 'measured', check: 'walker:signed-out', observed: `step ${label} landed on the sign-in page (${probe.path})` })
      log(`WALK VOID: step ${label} landed on the sign-in page`)
      throw new WalkVoid(`step ${label} landed on the sign-in page`)
    }
  }
  const file = await shot(page, label)
  const items = await page.evaluate(CHECKS).catch((e) => [{ check: 'walker:error', observed: 'checks failed: ' + e.message.split('\n')[0] }])
  for (const it of items) findings.push({ step: label, screenshot: file, claim: 'measured', ...it })
  log(`STEP ${label}: ${items.length} finding(s); shot ${file}`)
  return items
}

const settle = async (page, ms = 1200) => {
  await page.waitForLoadState('networkidle', { timeout: 35000 }).catch(() => {})
  await page.waitForTimeout(ms + opt.settleExtraMs)
}
const timeLeft = () => Date.now() < deadline

// ---- generic exploration of one scope ------------------------------------------------------------------------------
async function exploreScope(page, scopeSel, label) {
  // expand every closed <details>
  const sums = page.locator(`${scopeSel} details:not([open]) > summary`)
  const nSum = await sums.count().catch(() => 0)
  for (let i = 0; i < Math.min(nSum, 20) && timeLeft(); i++) {
    const s = page.locator(`${scopeSel} details:not([open]) > summary`).first()
    const txt = ((await s.innerText().catch(() => '')) || '').trim()
    if (DO_NOT_CLICK.test(txt)) break
    await s.click({ timeout: 3000 }).catch(() => {})
    await settle(page, 500)
  }
  if (nSum) await checks(page, `${label}-expanded`)
  // native selects: read options (duplicates are checked in CHECKS); walk each option for account pickers
  const selects = page.locator(`${scopeSel} select`)
  const nSel = await selects.count().catch(() => 0)
  for (let i = 0; i < nSel && timeLeft(); i++) {
    const sel = selects.nth(i)
    const name = (await sel.getAttribute('aria-label').catch(() => null)) || `select-${i}`
    const values = await sel.locator('option').evaluateAll((os) => os.map((o) => ({ v: o.value, t: (o.textContent || '').trim() }))).catch(() => [])
    for (const o of values.slice(0, 8)) {
      if (!timeLeft()) break
      await sel.selectOption(o.v).catch(() => {})
      await page.waitForLoadState('networkidle', { timeout: 6000 }).catch(() => {})
      await page.waitForTimeout(1200 + opt.settleExtraMs)
      await checks(page, `${label}-${name}-${o.t.slice(0, 24)}`)
    }
  }
  // popup triggers (custom dropdowns / menus)
  const triggers = page.locator(`${scopeSel} [aria-haspopup]:not(select), ${scopeSel} [aria-expanded="false"]`)
  const nTr = Math.min(await triggers.count().catch(() => 0), 12)
  for (let i = 0; i < nTr && timeLeft(); i++) {
    const t = triggers.nth(i)
    const txt = ((await t.innerText().catch(() => '')) || '').trim()
    if (DO_NOT_CLICK.test(txt)) continue
    await t.click({ timeout: 3000 }).catch(() => {})
    await page.waitForTimeout(600)
    await checks(page, `${label}-open-${txt.slice(0, 24) || i}`)
    await page.keyboard.press('Escape').catch(() => {})
    await page.waitForTimeout(300)
  }
}

// ---- AMGT Security Analysis: every Lead Panel combination, then each --security with its overlay and five tabs -----
// Friday faces (rulings R5/R6): Trending only, no list or chart view; Chatter = month bubbles, Price = bars. A --security is picked by clicking its row text in the lead panel, else typed into "Search any ticker".
// Starring is a write and stays blocked by the network guard.
const AMGT_TABS = ['Thesis', 'Exec Management', 'Peers', 'Model', 'Posture']
async function clickLabel(page, name) {
  for (const role of ['tab', 'radio', 'button']) {
    const l = page.getByRole(role, { name, exact: true }).first()
    if (await l.count().catch(() => 0)) return l.click({ timeout: 4000 }).then(() => true).catch(() => false)
  }
  const t = page.getByText(name, { exact: true }).first()
  if (await t.count().catch(() => 0)) return t.click({ timeout: 4000 }).then(() => true).catch(() => false)
  return false
}
async function amgtLeadState(page, subject) {
  const okS = await clickLabel(page, subject)
  if (!okS) findings.push({ step, check: 'walker:control-missing', claim: 'measured', observed: `control not found or not clickable: ${subject}` })
  await settle(page, 1500)
}
// ---- price wait: the Price face fills after the route answers; wait for the first bar before the read and the shot ----
const PRICE_WAIT_MS = 30000
let priceWaitMs = null
let lastPriceBody = null
async function waitPriceBars(page) {
  const t0 = Date.now()
  const got = await page.locator('[data-price-bar]').first().waitFor({ timeout: PRICE_WAIT_MS }).then(() => true).catch(() => false)
  priceWaitMs = Date.now() - t0
  log(`PRICE WAIT: ${got ? 'bar present' : 'NO BAR'} after ${priceWaitMs} ms`)
  if (got) return
  findings.push({ step, claim: 'measured', check: 'price:no-bars-after-wait', observed: `no [data-price-bar] after waiting ${priceWaitMs} ms (limit ${PRICE_WAIT_MS} ms)`, wait_ms: priceWaitMs, rule: 'FWD-22: the Price face shows its bars' })
  const txt = await page.evaluate(() => document.body.innerText).catch((e) => `DOM text read failed: ${e.message}`)
  writeFileSync(path.join(OUT, 'price-face-dom.txt'), String(txt))
  writeFileSync(path.join(OUT, 'price-response-body.txt'), lastPriceBody === null ? 'no lead-panel/rankings/trending/price response was seen in the network log' : lastPriceBody)
}
// ---- price bars: read every bar of the Price face (lead-lists.json) --------------------------------------------------
// Reads only what the page prints: each bar's data-price-bar attribute, its name-state attribute and its visible text.
async function readPriceBars(page, list) {
  const rows = await page.locator('[data-price-bar]').evaluateAll((els) => els.map((el) => ({
    bar: el.getAttribute('data-price-bar'),
    name_state: el.getAttribute('data-row-name-state') || el.closest('[data-row-name-state]')?.getAttribute('data-row-name-state') || null,
    text: ((el.closest('li') || el).innerText || '').replace(/\s+/g, ' ').trim(),
  }))).catch(() => [])
  leadLists.push({ list, row_count: rows.length, price_wait_ms: priceWaitMs, rows })
  log(`LEAD LIST ${list}: ${rows.length} price bar(s) read`)
}
// ---- chatter: read the month bubbles, then press the month cursor ---------------------------------------------------
async function readBubbles(page, list) {
  const n = await page.locator('[data-bubble], [data-chatter-bubble]').count().catch(() => 0)
  log(`LEAD BUBBLES ${list}: ${n} bubble(s) read`)
  const raw = await page.locator('[data-bubble]').evaluateAll((els) => els.filter((el) => {
    const key = (el.getAttribute('data-bubble') || '').trim()
    return key && (el.innerText || '').replace(/\s+/g, ' ').trim() === key
  }).length).catch(() => 0)
  if (raw) findings.push({ step, claim: 'measured', check: 'chatter:raw-key-label', observed: `${raw} of ${n} bubble(s) show their data-bubble key as the visible label`, count: raw, rule: 'design law: a code or key never sits in visible text' })
  const cur = page.getByRole('button', { name: 'Earlier month' }).first()
  if (await cur.count().catch(() => 0)) {
    const pressed = await cur.click({ timeout: 4000 }).then(() => true).catch(() => false)
    if (pressed) { await settle(page, 1000); await checks(page, `lead-${list}-cursor`) }
  } else findings.push({ step, check: 'walker:control-missing', claim: 'measured', observed: 'control not found: Earlier month' })
}

// ---- FWD-1: one company picked BY ITS NAME, then the thread hop by hop ----------------------------------------------
// The name is found by its price bar's row, on Trending x Price. Never by
// ticker and never through the ticker search box. A name no row prints is a measured finding and the thread stops.
async function walkThread(page, route, name) {
  step = `thread ${name}`
  await page.goto(opt.base + route, { waitUntil: 'domcontentloaded', timeout: 30000 })
  await settle(page, 2500)
  await amgtLeadState(page, 'Price')
  const rows = page.locator('[data-price-bar]')
  const lead = page.locator('li:has([data-price-bar])').filter({ hasText: name }).first()
  const nRows = await rows.count().catch(() => 0)
  if (!(await lead.count().catch(() => 0))) {
    findings.push({ step, check: 'thread:name-not-found', claim: 'measured', observed: `no row of the Trending x Price list (${nRows} rows) reads the company name "${name}"`, rule: 'FWD-1: the PM picks the company out of the list by its name' })
    log(`THREAD: no row reads "${name}" (${nRows} rows)`)
    return
  }
  await lead.scrollIntoViewIfNeeded().catch(() => {})
  await checks(page, 'thread-1-list')
  step = `thread ${name} open`
  await lead.click({ timeout: 4000 }).catch(() => {})
  await settle(page, 3000)
  await checks(page, 'thread-2-header-cards')
  step = `thread ${name} financials`
  const fin = page.locator('[data-header-card="financials"]').first()
  if (await fin.count().catch(() => 0)) {
    await fin.click({ timeout: 4000 }).catch(() => {})
    await settle(page, 1500)
    await checks(page, 'thread-3-financials-window')
    await page.keyboard.press('Escape').catch(() => {})
    await page.waitForTimeout(400)
  } else findings.push({ step, check: 'walker:control-missing', claim: 'measured', observed: 'the Financials header card was not found' })
  step = `thread ${name} thesis`
  if (!(await clickLabel(page, 'Thesis'))) findings.push({ step, check: 'walker:control-missing', claim: 'measured', observed: 'tab not found: Thesis' })
  await settle(page, 2500)
  await checks(page, 'thread-4-thesis-cards')
  step = `thread ${name} recommendation`
  const rec = page.locator('[data-thesis-card="recommendation"]').first()
  if (await rec.count().catch(() => 0)) {
    await rec.click({ timeout: 4000 }).catch(() => {})
    await settle(page, 1500)
    await checks(page, 'thread-5-recommendation-window')
    await page.keyboard.press('Escape').catch(() => {})
    await page.waitForTimeout(400)
  } else findings.push({ step, check: 'walker:control-missing', claim: 'measured', observed: 'the Recommendation card was not found' })
}

// ---- the company timeline: one day pressed, one event opened (or its absence recorded) ------------------------------
// ---- the opened day's STATE, not a fixed sleep: /timeline/day answers in ~5.5 s for a day with articles, so a 1,500 ms settle shot
// every opened day as a skeleton. The panel marks all three states under the opened day's container; the wait polls them and
// returns the first seen, or 'ceiling' when none appears (a held route is its own result, never graded as rows).
const DAY_STATE_CEILING_MS = 20000
async function waitForDayState(page, date) {
  const box = `[data-timeline-selected-day="${date}"]`
  const states = [
    ['rows', `${box} [data-timeline-dissection="SERVED"] [data-timeline-article]`],
    ['empty', `${box} [data-timeline-day-empty]`],
    ['failed', `${box} [data-timeline-dissection="FAILED"]`],
  ]
  const t0 = Date.now()
  for (;;) {
    for (const [state, sel] of states) {
      if (await page.locator(sel).count().catch(() => 0)) return { state, waited_ms: Date.now() - t0 }
    }
    if (Date.now() - t0 >= DAY_STATE_CEILING_MS) return { state: 'ceiling', waited_ms: Date.now() - t0 }
    await page.waitForTimeout(250)
  }
}

// The timeline sits in the opened name's header. The newest day is the last bar the panel draws. The panel may build no
// event layer, and then the walk says so as a finding rather than passing silently.
async function walkTimeline(page, sec) {
  step = `timeline ${sec}`
  const bars = page.locator('[data-day-bar]')
  const nBars = await bars.count().catch(() => 0)
  if (nBars) {
    const bar = bars.last()
    let pressed = await bar.click({ timeout: 4000, force: true }).then(() => true).catch(() => false)
    if (!pressed) pressed = await bar.dispatchEvent('click').then(() => true).catch(() => false)
    if (!pressed) findings.push({ step, check: 'walker:control-missing', claim: 'measured', observed: `the newest of ${nBars} day bar(s) could not be pressed` })
    else {
      const newestDate = await bar.getAttribute('data-day-bar').catch(() => null)
      if (newestDate) {
        const got = await waitForDayState(page, newestDate)
        timelineDays.push({ via: 'newest', security: sec, date: newestDate, pressed, state: got.state, waited_ms: got.waited_ms })
      }
    }
  } else findings.push({ step, check: 'timeline:no-day-bar', claim: 'measured', observed: 'the company page carries no day bar to press', rule: 'FWD-5: a day-by-day line the PM can press' })
  await checks(page, `${sec}-timeline-day`)
  const ev = page.locator('[data-timeline-event]')
  if (await ev.count().catch(() => 0)) {
    const evPressed = await ev.first().click({ timeout: 4000, force: true }).then(() => true).catch(() => false)
    const evSpan = await ev.first().getAttribute('data-timeline-event').catch(() => null)
    const evDate = evSpan ? evSpan.split('..')[0] : null
    if (evPressed && evDate) {
      const got = await waitForDayState(page, evDate)
      timelineDays.push({ via: 'event', security: sec, date: evDate, pressed: evPressed, state: got.state, waited_ms: got.waited_ms })
    }
    await checks(page, `${sec}-timeline-event`)
  } else findings.push({ step, check: 'timeline:no-event-element', claim: 'measured', observed: `no [data-timeline-event] element on the ${sec} timeline (the panel builds no event layer, or none is served)`, rule: 'FWD-6: bursts of coverage appear as marked events with a headline' })
}

// ---- timeline days named with --day: press the day's bar by its date, read the opened dissection's article rows in the order
// the page lists them, and keep them for timeline-days.json (the CVO reads the order the page shows).
const timelineDays = []
async function walkTimelineDays(page, sec) {
  for (const { date } of opt.days.filter((d) => d.security === sec)) {
    if (!timeLeft()) return
    step = `amgt ${sec} timeline day ${date}`
    const bar = page.locator(`[data-day-bar="${date}"]`).first()
    let pressed = false
    if (await bar.count().catch(() => 0)) {
      pressed = await bar.click({ timeout: 4000 }).then(() => true).catch(() => false)
      if (!pressed) pressed = await bar.dispatchEvent('click').then(() => true).catch(() => false)
    } else {
      findings.push({ step, check: 'timeline:day-not-found', claim: 'measured', observed: `no timeline bar for ${date} on ${sec}` })
    }
    const got = pressed ? await waitForDayState(page, date) : { state: 'ceiling', waited_ms: 0 }
    await checks(page, `${sec}-timeline-day-${date}`)
    const rows = pressed && got.state === 'rows' ? await page.locator(`[data-timeline-selected-day="${date}"] li`).allInnerTexts().catch(() => []) : []
    timelineDays.push({ via: 'day', security: sec, date, pressed, state: got.state, waited_ms: got.waited_ms, article_rows_in_page_order: rows })
  }
}

// ---- the picked name's and each tab's LOAD STATE, not a fixed sleep: a name with no dossier issues /overlay and a fixed 3 s settle
// shot "Loading identity header". Panels mark data-panel-state = loading | error | empty | no-permission; wait until none loads.
const LOAD_STATE_CEILING_MS = 45000
async function waitForLoaded(page) {
  const t0 = Date.now()
  for (;;) {
    const loading = await page.locator('[data-panel-state="loading"]').count().catch(() => 0)
    const errored = await page.locator('[data-panel-state="error"]').count().catch(() => 0)
    if (!loading) return { state: errored ? 'error' : 'loaded', waited_ms: Date.now() - t0 }
    if (Date.now() - t0 >= LOAD_STATE_CEILING_MS) return { state: 'ceiling', waited_ms: Date.now() - t0 }
    await page.waitForTimeout(250)
  }
}
const loadStates = []

async function walkSecurityAnalysis(page, route) {
  for (const subject of ['Chatter', 'Price']) {
    if (!timeLeft()) return
    step = `amgt lead Trending-${subject}`
    await amgtLeadState(page, subject)
    if (subject === 'Price') await waitPriceBars(page)
    await checks(page, `lead-Trending-${subject}`)
    if (subject === 'Price') await readPriceBars(page, 'Trending x Price')
    else await readBubbles(page, 'Trending-Chatter')
  }
  if (opt.thread) await walkThread(page, route, opt.thread)
  for (const sec of opt.securities) {
    if (!timeLeft()) return
    step = `amgt select ${sec}`
    await page.goto(opt.base + route, { waitUntil: 'domcontentloaded', timeout: 30000 })
    await settle(page, 2500)
    await amgtLeadState(page, 'Price')
    let picked = false
    const row = page.getByText(sec, { exact: true }).first()
    if (await row.count().catch(() => 0)) picked = await row.click({ timeout: 4000 }).then(() => true).catch(() => false)
    if (!picked) {
      const box = page.getByPlaceholder('Search any ticker')
      await box.fill(sec).catch(() => {})
      await box.press('Enter').catch(() => {})
    }
    await page.waitForTimeout(400)
    const pickWait = await waitForLoaded(page)
    loadStates.push({ security: sec, step: 'overlay', state: pickWait.state, waited_ms: pickWait.waited_ms })
    await checks(page, `${sec}-overlay`)
    await walkTimelineDays(page, sec)
    await walkTimeline(page, sec)
    for (const tab of AMGT_TABS) {
      if (!timeLeft()) return
      step = `amgt ${sec} tab ${tab}`
      if (!(await clickLabel(page, tab))) findings.push({ step, check: 'walker:control-missing', claim: 'measured', observed: `tab not found: ${tab}` })
      await page.waitForTimeout(400)
      const tabWait = await waitForLoaded(page)
      loadStates.push({ security: sec, step: tab, state: tabWait.state, waited_ms: tabWait.waited_ms })
      await checks(page, `${sec}-${tab}`)
      await exploreScope(page, 'body', `${sec}-${tab}`)
      if (opt.deep) await pressAll(page, 'body', `${sec}-${tab}`, 10)
    }
  }
}

// ---- periods per account: on the Performance tab, select EACH account of the picker and press each period preset once,
// so a period figure is read for every account rather than for whichever account the select loop left selected.
// Presets are matched by their exact label; a preset that is not on the page is simply not pressed. No write is reachable.
const PERIOD_WORDS = /^(YTD|QTD|1Y|3Y|Since inception)$/i
async function periodsPerAccount(page, scopeSel, label) {
  const selects = page.locator(`${scopeSel} select`)
  const nSel = await selects.count().catch(() => 0)
  for (let i = 0; i < nSel && timeLeft(); i++) {
    const sel = selects.nth(i)
    const name = (await sel.getAttribute('aria-label').catch(() => null)) || `select-${i}`
    const values = await sel.locator('option').evaluateAll((os) => os.map((o) => ({ v: o.value, t: (o.textContent || '').trim() }))).catch(() => [])
    for (const o of values.slice(0, 8)) {
      if (!timeLeft()) break
      await sel.selectOption(o.v).catch(() => {})
      await settle(page, 2500)
      const btns = page.locator(`${scopeSel} button:visible`)
      const n = await btns.count().catch(() => 0)
      const labels = []
      for (let k = 0; k < n; k++) labels.push((((await btns.nth(k).innerText().catch(() => '')) || '')).replace(/\s+/g, ' ').trim())
      for (const txt of labels.filter((t) => PERIOD_WORDS.test(t))) {
        if (!timeLeft()) break
        const b = page.locator(`${scopeSel} button:visible`, { hasText: new RegExp(`^${txt.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}$`, 'i') }).first()
        await b.click({ timeout: 3000 }).catch(() => {})
        await settle(page, 2500)
        await checks(page, `${label}-${name}-${o.t.slice(0, 24)}-period-${txt.slice(0, 16)}`)
      }
    }
  }
}

// ---- deep mode: press every enabled, admitted button in a tab once (presets, variants, chips, toggles) -------------
// One button per round, the DOM re-read each round because a press can re-render the tab. Never pressed: anything the
// DO_NOT_CLICK words match, the tab strip's own tabs, disabled buttons. Writes are still blocked by the network guard,
// and file pickers are <input type=file>, never a <button>, so no OS dialog opens.
const TAB_WORDS = /^(performance|holdings|analysis)$/i
async function pressAll(page, scopeSel, label, maxPresses = 18) {
  const seen = new Set()
  for (let round = 0; round < maxPresses && timeLeft(); round++) {
    const btns = page.locator(`${scopeSel} button:visible`)
    const n = await btns.count().catch(() => 0)
    let pressed = false
    for (let i = 0; i < n && timeLeft(); i++) {
      const b = btns.nth(i)
      const txt = (((await b.innerText().catch(() => '')) || (await b.getAttribute('aria-label').catch(() => '')) || '')).replace(/\s+/g, ' ').trim()
      if (!txt || seen.has(txt) || DO_NOT_CLICK.test(txt) || TAB_WORDS.test(txt)) continue
      seen.add(txt)
      if (await b.isDisabled().catch(() => true)) continue
      await b.click({ timeout: 3000 }).catch(() => {})
      await settle(page, 1800)
      await checks(page, `${label}-press-${txt.slice(0, 28)}`)
      // light follow-up: open any <details> the press revealed (selects are walked once per tab, not per press)
      const sums = page.locator(`${scopeSel} details:not([open]) > summary`)
      const nSum = Math.min(await sums.count().catch(() => 0), 6)
      for (let k = 0; k < nSum; k++) {
        const s = page.locator(`${scopeSel} details:not([open]) > summary`).first()
        if (DO_NOT_CLICK.test(((await s.innerText().catch(() => '')) || ''))) break
        await s.click({ timeout: 3000 }).catch(() => {})
        await page.waitForTimeout(400)
      }
      if (nSum) await checks(page, `${label}-after-${txt.slice(0, 16)}-expanded`)
      // close anything the press opened (a card's "View breakdown" dialog blocked the next tab click on 2026-09-27)
      await page.keyboard.press('Escape').catch(() => {})
      await page.waitForTimeout(400)
      pressed = true
      break
    }
    if (!pressed) break
  }
  return [...seen]
}

// ---- --model-scope: pick ONE model inside the Holdings card and read what the tab shows under that scope -------
// (DSGN_IRPTV1 FAST item 42, 1.0.0_SA_CTO 103536). The pick control is `[data-slot=breakdown-row-scope]`, offered in
// a card tile's breakdown dialog. The step opens card buttons one at a time (an account tile re-scopes the tab, so
// the buttons are re-read each round) until a pick control appears, presses the first one, and records the scope
// line, the map's chips, the Sleeve select and the table's row count. A pick is page state only: it sends nothing.
const modelScopes = []
// ---- --holdings-aggregates: the served per-security fold beside the page's own fold, per holdings answer ----------
// (DSGN_IRPTV1 next-list 0c, walk-2 W2-11.) For every holdings response the walk receives, compare each served
// `security_aggregates` item with (a) the sum of its ACTUAL member nodes (basis OBSERVED or ASSIGNED) -- what the
// route says it folded -- and (b) the page's own fold, which sums EVERY security node of that id, a model's TARGET
// nodes included. Counts only; no name and no figure of any client is written. `class_totals` plus the remainder is
// checked against the custody total. One record per distinct selection path.
const holdingsAggregates = []
// ---- --performance-state: the Performance tab's STATE, not a fixed sleep (DSGN_IRPTV1 FAST item 57) ----------------
// A performance answer can land after the 2,500 ms settle, so the tab's first shot reads "Loading" (walk
// 20261001T083028Z: three of three). The tab marks its two finished states: `[data-slot=reporting-refusal-words]` (a
// worded refusal) and `[data-slot=reporting-body]` (an answer). The wait polls them every 250 ms and returns the first
// seen, or 'ceiling' -- its own result, never graded as an answer. Recorded: the state, the wait, the refusal's own
// sentence (page copy, no client data) and whether the code disclosure stands open. No figure of any client is written.
const PERFORMANCE_STATE_CEILING_MS = 45000
const performanceStates = []
async function waitForPerformanceState(page) {
  const tab = '[data-slot="reporting-tab"]'
  const t0 = Date.now()
  for (;;) {
    if (await page.locator(`${tab} [data-slot="reporting-refusal-words"]`).count().catch(() => 0)) {
      const message = ((await page.locator(`${tab} [data-slot="reporting-refusal-message"]`).first().innerText().catch(() => '')) || '').replace(/\s+/g, ' ').trim()
      const codeOpen = await page.locator(`${tab} [data-slot="reporting-refusal-code-disclosure"][open]`).count().catch(() => 0)
      return { state: 'refusal', waited_ms: Date.now() - t0, message, code_disclosure_open: codeOpen > 0 }
    }
    if (await page.locator(`${tab} [data-slot="reporting-body"]`).count().catch(() => 0)) return { state: 'body', waited_ms: Date.now() - t0 }
    if (Date.now() - t0 >= PERFORMANCE_STATE_CEILING_MS) return { state: 'ceiling', waited_ms: Date.now() - t0 }
    await page.waitForTimeout(250)
  }
}
const seenHoldingsPaths = new Set()
function readHoldingsAggregates(p, j) {
  const d = j && j.data
  if (!d || !Array.isArray(d.nodes) || seenHoldingsPaths.has(p)) return
  seenHoldingsPaths.add(p)
  const idOf = (n) => (n.security_id ? `${n.security_id.namespace}:${n.security_id.value}` : null)
  const securities = d.nodes.filter((n) => n.node_kind === 'SECURITY' || n.node_kind === 'CASH')
  const actual = securities.filter((n) => n.basis === 'OBSERVED' || n.basis === 'ASSIGNED')
  const sum = (rows, f) => rows.reduce((t, n) => t + (typeof f(n) === 'number' ? f(n) : 0), 0)
  const near = (a, b, tol) => typeof a === 'number' && typeof b === 'number' && Math.abs(a - b) <= tol
  const rec = {
    selection: p.split('/').pop().slice(0, 16),
    security_nodes: securities.length, actual_nodes: actual.length, target_nodes: securities.filter((n) => n.basis === 'TARGET').length,
    aggregates_served: Array.isArray(d.security_aggregates) ? d.security_aggregates.length : null,
  }
  if (Array.isArray(d.security_aggregates)) {
    let amountEqActual = 0; let weightEqActual = 0; let amountEqPageFold = 0; let weightEqPageFold = 0
    for (const a of d.security_aggregates) {
      const id = `${a.security_id.namespace}:${a.security_id.value}`
      const mine = actual.filter((n) => idOf(n) === id)
      const all = securities.filter((n) => idOf(n) === id)
      if (near(sum(mine, (n) => n.amount && n.amount.value), a.amount.value, 0.005)) amountEqActual += 1
      if (a.weight === null || near(sum(mine, (n) => n.percentages && n.percentages.of_total), a.weight, 1e-6)) weightEqActual += 1
      if (near(sum(all, (n) => n.amount && n.amount.value), a.amount.value, 0.005)) amountEqPageFold += 1
      if (a.weight === null || near(sum(all, (n) => n.percentages && n.percentages.of_total), a.weight, 1e-6)) weightEqPageFold += 1
    }
    const servedIds = new Set(d.security_aggregates.map((a) => `${a.security_id.namespace}:${a.security_id.value}`))
    const pageIds = new Set(securities.map(idOf).filter(Boolean))
    Object.assign(rec, {
      amount_equals_actual_sum: amountEqActual, weight_equals_actual_of_total_sum: weightEqActual,
      amount_equals_page_fold: amountEqPageFold, weight_equals_page_fold: weightEqPageFold,
      page_identities: pageIds.size, page_identities_with_no_served_aggregate: [...pageIds].filter((id) => !servedIds.has(id)).length,
    })
  }
  if (Array.isArray(d.class_totals) && d.custody_totals && d.custody_totals.total_market_value) {
    const classes = sum(d.class_totals, (c) => c.amount && c.amount.value)
    const rest = d.class_totals_remainder && d.class_totals_remainder.amount ? d.class_totals_remainder.amount.value : null
    rec.class_lines = d.class_totals.length
    rec.remainder_weight = d.class_totals_remainder ? d.class_totals_remainder.weight : null
    rec.classes_plus_remainder_equals_custody = rest === null ? null : near(classes + rest, d.custody_totals.total_market_value.value, 0.01)
  }
  holdingsAggregates.push(rec)
}
// ---- --open-request <REQ-id>: open ONE listed analysis request and read what its dialog shows -------------------
// (IRPT RULINGS batch 61 item 6 / CTO condition 9: one READY request walked on the local build against the real
// backend, sections on screen.) The row is found by `data-request-id`; when that id is not listed, the first row whose
// state reads Ready is opened instead and the record says so. Opening a request issues GETs only.
const REQUEST_DETAIL_CEILING_MS = 90000   // 45,000 until walk 20261001T142136Z, whose sections landed 0.5 s after it
const openedRequests = []
// The hops of ONE open (IRPT RULINGS batch 88 item 4 E4: "30.2 seconds from the press to the sections is measured by
// hop before anything is changed"). While a recorder is set, every Investor Reporting analysis or status request the
// page makes is timed from the press: when it was sent, when its answer had fully arrived, and what it answered. For
// the sections answer the served counts are read too (sections, undated sections), so the rows the page renders can
// be set beside what was served. Counts and times only; no value of any report is written.
let requestHops = null
const hopStart = new WeakMap()
function hopKind(p) {
  if (/\/analysis\/requests\/[^/]+$/.test(p)) return 'request-read'
  if (/\/analysis\/requests$/.test(p)) return 'request-list'
  if (/\/analysis\/[^/]+\/sections$/.test(p)) return 'sections'
  if (/\/status\/[^/]+$/.test(p)) return 'status-job'
  if (/\/status$/.test(p)) return 'status-summary'
  return /\/investor-reporting\/(analysis|status)/.test(p) ? 'other-analysis' : null
}
function noteHopRequest(req) {
  const kind = requestHops ? hopKind(pathOnly(req.url())) : null
  if (!kind) return
  hopStart.set(req, Date.now())
  // sent per kind, so a read that was sent and never answered inside the window shows as sent minus answered
  requestHops.sent = requestHops.sent || {}
  requestHops.sent[kind] = (requestHops.sent[kind] || 0) + 1
}
function noteHopResponse(req, res, json, headers) {
  if (!requestHops || !hopStart.has(req)) return
  const p = pathOnly(req.url())
  const kind = hopKind(p)
  const row = { kind, sent_ms: hopStart.get(req) - requestHops.t0, answered_ms: Date.now() - requestHops.t0, http: res.status(), state: json?.status?.state ?? null, reason: json?.status?.public_reason_code ?? null }
  row.took_ms = row.answered_ms - row.sent_ms
  // WHERE the time went, from the browser's own resource timing: `queued_ms` is from the page issuing the request to
  // the request leaving on a connection (a dev build speaks HTTP/1.1 to localhost, six connections per host, so a
  // burst of reads queues here); `server_ms` is from the request leaving to the first byte of the answer.
  try {
    const t = req.timing()
    row.queued_ms = t.requestStart >= 0 ? Math.round(t.requestStart) : null
    row.server_ms = t.requestStart >= 0 && t.responseStart >= 0 ? Math.round(t.responseStart - t.requestStart) : null
  } catch { row.queued_ms = null; row.server_ms = null }
  // Batch 89 item 4: does the page declare the dates capability on a status read? The header's own value, as sent.
  // POSITIVE CONTROL beside it: whether the same request carried an Authorization header (every scoped read does),
  // so a null here is "the header was not sent", never "this reader cannot see request headers".
  if (kind === 'status-job' || kind === 'status-summary') {
    const h = headers || {}
    row.status_dates_header = h['x-irpt-status-dates'] ?? null
    row.saw_authorization_header = typeof h.authorization === 'string' && h.authorization.length > 0
  }
  if (kind === 'sections' && json && json.data) {
    row.served_sections = Array.isArray(json.data.sections) ? json.data.sections.length : null
    row.served_undated_sections = Array.isArray(json.data.undated_sections) ? json.data.undated_sections.length : null
  }
  requestHops.rows.push(row)
}
async function openRequest(page, label, requestId, afterReload = false) {
  const rows = page.locator('[data-row="owned-analysis-request"]')
  for (let w = 0; w < 40 && !(await rows.count().catch(() => 0)); w++) await page.waitForTimeout(500)
  const listed = await page.evaluate(() => [...document.querySelectorAll('[data-row="owned-analysis-request"]')].map((r) => ({
    id: r.getAttribute('data-request-id'), state: (r.querySelector('[data-slot="owned-request-state"]') || {}).textContent || null })))
  let target = listed.find((r) => r.id === requestId)
  const byId = Boolean(target)
  if (!target) target = listed.find((r) => /^Ready\b/.test(r.state || ''))
  const rec = { label, asked: requestId, listed: listed.length, listed_ready: listed.filter((r) => /^Ready\b/.test(r.state || '')).length, opened: target ? target.id : null, opened_by_id: byId, row_state: target ? target.state : null }
  if (!target) {
    await checks(page, `${label}-request-not-listed`)
    findings.push({ step: `${label}-open-request`, check: 'analysis:no-ready-request-listed', claim: 'measured', observed: `${listed.length} request(s) listed, none Ready and none with the asked id`, rule: 'a READY request opens with its sections on screen' })
    openedRequests.push(rec); return
  }
  // The recorder runs from the Analysis tab's own click when the walk started it there (the list's per-row status
  // reads are sent before any press); every hop's time is from that origin and `press_ms` places the press on it.
  const t0 = Date.now()
  if (!requestHops) requestHops = { t0, rows: [] }
  rec.press_ms = t0 - requestHops.t0
  rec.row_states_at_press = listed.reduce((acc, r) => { const k = (r.state || 'none').replace(/\s+--.*$/, '').slice(0, 40); acc[k] = (acc[k] || 0) + 1; return acc }, {})
  await page.locator(`[data-row="owned-analysis-request"][data-request-id="${target.id}"] button`).first().click({ timeout: 5000 }).catch(() => {})
  const detail = page.locator('[data-slot="owned-request-detail"]')
  await detail.waitFor({ state: 'visible', timeout: 15000 }).catch(() => {})
  // What the page showed WHEN, from the press: the dialog, its status words, the sections block (first seen, 250 ms steps).
  const marks = { dialog_visible_ms: Date.now() - t0, status_words_ms: null, sections_block_ms: null }
  let read = null
  while (Date.now() - t0 < REQUEST_DETAIL_CEILING_MS) {
    read = await page.evaluate(() => {
      const d = document.querySelector('[data-slot="owned-request-detail"]')
      if (!d) return null
      const status = d.querySelector('[role="status"]')
      const text = d.innerText || ''
      const block = '[data-slot="owned-report-sections"]'
      return {
        status_words: status ? status.textContent : null,
        section_blocks: d.querySelectorAll(block).length,
        // EXACT counts by the page's own markers: one card per served section, one row per value in it.
        section_cards: d.querySelectorAll(`${block} [data-row="native-section"]`).length,
        section_value_rows: d.querySelectorAll(`${block} [data-row="native-section-value"]`).length,
        // The OLD count (`section_items`), kept and now explained: it never counted cards. Inside the block its
        // selector matches the extraction-coverage panel's own <section> and every <li> of that panel's gap list
        // (behind "Technical details"); a card is a <div data-row="native-section"> and matches none of it.
        coverage_gap_items: d.querySelectorAll(`${block} [data-slot="extraction-coverage"] li`).length,
        coverage_panels: d.querySelectorAll(`${block} [data-slot="extraction-coverage"]`).length,
        section_items: d.querySelectorAll(`${block} section, ${block} li, ${block} [data-section-id]`).length,
        correction_words: (d.querySelector('[data-slot="request-correction-words"]') || {}).textContent || null,
        sections_unavailable_words: /Report sections are not available/.test(text),
        checking: /Checking request status/.test(text),
        text_chars: text.length,
      }
    }).catch(() => null)
    if (read && read.status_words && !read.checking && marks.status_words_ms === null) marks.status_words_ms = Date.now() - t0
    if (read && read.section_blocks > 0 && marks.sections_block_ms === null) marks.sections_block_ms = Date.now() - t0
    if (read && !read.checking && (read.section_blocks > 0 || read.sections_unavailable_words)) break
    await page.waitForTimeout(250)
  }
  rec.waited_ms = Date.now() - t0
  rec.detail = read
  rec.marks = marks
  await page.waitForTimeout(600)                 // a late answer of an already-sent request still lands in the hops
  rec.hops = requestHops.rows.slice().sort((a, b) => a.sent_ms - b.sent_ms)
  rec.hops_sent_by_kind = requestHops.sent || {}
  requestHops = null
  // --expect-text "<words>" (repeatable): how many times the opened dialog's own text carries each string, counted
  // case-sensitively, with where it stands: on the dialog's face, or only inside a closed <details>.
  if (opt.expectTexts.length) {
    rec.expect_text = await page.evaluate((wanted) => {
      const d = document.querySelector('[data-slot="owned-request-detail"]')
      if (!d) return null
      const count = (hay, needle) => needle ? hay.split(needle).length - 1 : 0
      const all = d.textContent || ''
      const closed = [...d.querySelectorAll('details:not([open])')].map((x) => x.textContent || '').join('\n')
      return wanted.map((w) => ({ text: w, in_dialog: count(all, w), inside_closed_details: count(closed, w) }))
    }, opt.expectTexts).catch(() => null)
  }
  await checks(page, `${label}-request-open`)
  await page.locator('[data-slot="owned-request-detail"]').evaluate((d) => { d.scrollTop = d.scrollHeight }).catch(() => {})
  await page.waitForTimeout(400)
  await checks(page, `${label}-request-open-end`)
  openedRequests.push(rec)
  await page.keyboard.press('Escape').catch(() => {})
  await page.waitForTimeout(400)
  // --reload-reopen: reload the page and open the SAME request again, so "it is still there after a reload" is a
  // read and not a belief. A reload may drop the client selection; that is recorded as its own fact, and the request
  // is re-opened only if its row is listed again. One reload per request (the second open never reloads).
  if (opt.reloadReopen && !afterReload) {
    const reload = { reloaded: false, client_kept: null, analysis_tab_pressed: false, rows_listed: 0 }
    await page.reload({ waitUntil: 'domcontentloaded', timeout: 30000 }).then(() => { reload.reloaded = true }).catch(() => {})
    await settle(page, 4000)
    const who = ((await page.locator('[data-slot="identity-card"]').first().innerText().catch(() => '')) || '').replace(/\s+/g, ' ')
    reload.client_kept = who.length > 0 && !/No client selected/.test(who)
    const tab = page.locator('[data-slot="tab-shell"] .overflow-x-auto button', { hasText: /^analysis$/i }).first()
    if (await tab.count().catch(() => 0)) {
      requestHops = { t0: Date.now(), rows: [] }
      await tab.click().catch(() => {})
      reload.analysis_tab_pressed = true
      const rows2 = page.locator('[data-row="owned-analysis-request"]')
      for (let w = 0; w < 120 && !(await rows2.count().catch(() => 0)); w++) await page.waitForTimeout(500)
      reload.rows_listed = await rows2.count().catch(() => 0)
    }
    await checks(page, `${label}-after-reload`)
    rec.reload = reload
    if (reload.rows_listed > 0) await openRequest(page, `${label}-after-reload`, requestId, true)
    else requestHops = null
  }
}

const SEARCH_ANSWER_CEILING_MS = 30000
const searchTimings = []
// ---- --account-drill (DSGN_IRPTV1 FAST item 65; Andrew-direct 2026-10-02 ~04:3xZ: an account drill on the Total Assets
// card must not be a full page refresh). On the Holdings tab's default view: wait until the tab's background one-account
// reads are done (no holdings read out for 2.5 s, up to ACCOUNT_DRILL_WARM_CEILING_MS), press the card's first tile, and
// poll every 40 ms until the one-account view is shown ("Back to all accounts" present, no "Opening" line). Counts and
// times only: no client name and no figure is written. Then it returns to every account.
const accountDrills = []
const ACCOUNT_DRILL_WARM_CEILING_MS = 60000
async function accountDrill(page, label) {
  const reads = []          // { kind, sent, answered }
  const byReq = new Map()
  const onRequest = (req) => {
    const p = pathOnly(req.url())
    const kind = /\/investor-reporting\/holdings\//.test(p) ? 'holdings' : (req.method() === 'POST' && /\/investor-reporting\/selections$/.test(p)) ? 'selection' : null
    if (!kind) return
    const r = { kind, sent: Date.now(), answered: null, status: null }
    reads.push(r); byReq.set(req, r)
  }
  const onDone = (req, status) => { const r = byReq.get(req); if (r && r.answered === null) { r.answered = Date.now(); r.status = status } }
  const onResponse = (res) => onDone(res.request(), res.status())
  const onFailed = (req) => onDone(req, 'failed')
  page.on('request', onRequest); page.on('response', onResponse); page.on('requestfailed', onFailed)
  const t0 = Date.now()
  let quietSince = Date.now()
  while (Date.now() - t0 < ACCOUNT_DRILL_WARM_CEILING_MS) {
    if (reads.some((r) => r.answered === null)) quietSince = Date.now()
    else if (Date.now() - quietSince >= 2500) break
    await page.waitForTimeout(100)
  }
  const warmMs = Date.now() - t0
  const background = reads.filter((r) => r.kind === 'holdings').map((r) => (r.answered === null ? null : r.answered - r.sent))
  const tiles = page.locator('[data-slot="holdings-drill-tree"] [aria-haspopup="dialog"]')
  const tileCount = await tiles.count()
  const rec = { label, tiles: tileCount, warm_wait_ms: warmMs, background_holdings_reads: background.length,
    background_selection_posts: reads.filter((r) => r.kind === 'selection').length,
    background_holdings_took_ms: background, drill: null }
  if (tileCount > 0) {
    const pressAt = Date.now(); const before = reads.length
    await tiles.first().click().catch(() => {})
    let tabGone = false; let opening = false; let shownMs = null
    while (Date.now() - pressAt < 30000 && shownMs === null) {
      const s = await page.evaluate(() => ({
        tab: !!document.querySelector('[data-slot="holdings-tab"]'),
        opening: !!document.querySelector('[data-slot="holdings-account-opening"]'),
        back: !!document.querySelector('[data-slot="holdings-all-accounts"]'),
      })).catch(() => ({ tab: false, opening: false, back: false }))
      if (!s.tab) tabGone = true
      if (s.opening) opening = true
      if (s.tab && s.back && !s.opening) shownMs = Date.now() - pressAt
      else await page.waitForTimeout(40)
    }
    const after = reads.slice(before)
    rec.drill = { ms_to_account_view: shownMs, tab_body_left_the_page: tabGone, opening_line_shown: opening,
      reads_after_press: after.map((r) => ({ kind: r.kind, sent_ms: r.sent - pressAt, took_ms: r.answered === null ? null : r.answered - r.sent })),
      account_view_offered: shownMs !== null }
    await page.keyboard.press('Escape').catch(() => {})
    await shot(page, `${label}-account-drill`)
    await checks(page, `${label}-account-drill`)
    await page.locator('[data-slot="holdings-all-accounts"]').first().click().catch(() => {})
    await page.waitForTimeout(800)
  }
  page.off('request', onRequest); page.off('response', onResponse); page.off('requestfailed', onFailed)
  accountDrills.push(rec)
  if (rec.drill && rec.drill.tab_body_left_the_page) findings.push({ step: `${label}-account-drill`, check: 'account-drill:page-reload', claim: 'measured', observed: 'the Holdings tab body left the page during an account drill', rule: 'an account drill on the Total Assets card is not a page reload (Andrew-direct 2026-10-02)' })
}

// ---- --composer-picker (DSGN_IRPTV1 FAST item 70; walk-2 W2-04 / W2-05): on the Analysis tab, take the composer to its
// analysis-type step (the Client portfolio card), then press the Multi-Comp card (the picker must open at once, Done closed
// at 0 picks), pick the first two Opal models, Done; press the Comparison card, search 'spy', pick the first ETF, Done;
// press Overview. Records the served catalogue read (status, took, entry counts by kind), the loose input box count at rest
// and at the end, and the names the composer prints. Page state only: the catalogue read is a GET and Generate is never
// pressed. Opal model and ETF names are the firm's catalogue, not client data.
const composerPickers = []
async function composerPicker(page, label) {
  const reads = []
  const onResponse = async (res) => {
    if (!/\/analysis\/comparisons$/.test(pathOnly(res.url()))) return
    const r = { status: res.status(), took_ms: null, entries: null, models: null, etfs: null }
    try { const t = res.request().timing(); r.took_ms = t.responseEnd > 0 ? Math.round(t.responseEnd) : null } catch { /* timing unread */ }
    try { const body = await res.json(); const e = (body && body.data && body.data.entries) || []; r.entries = e.length; r.models = e.filter((x) => x.name_source === 'model_catalogue').length; r.etfs = r.entries - r.models } catch { /* not JSON */ }
    reads.push(r)
  }
  page.on('response', onResponse)
  const rec = { label, reached_type_step: false, catalogue_reads: reads, loose_input_at_rest: null }
  const names = () => page.evaluate(() => [...document.querySelectorAll('[data-slot="comparison-name"]')].map((e) => (e.textContent || '').trim()))
  const looseInput = async () => (await page.getByRole('textbox', { name: 'Compare with an Opal model' }).count().catch(() => 0)) + (await page.locator('[data-slot="add-comparison"]').count().catch(() => 0))
  const pickerOpen = async () => (await page.locator('[data-slot="comparison-picker"]').count().catch(() => 0)) > 0
  const variant = () => page.locator('[data-slot="variant-resolved"]').first().textContent({ timeout: 2000 }).catch(() => null)
  const card = (word) => page.locator('[data-slot="variant-card"]').filter({ hasText: word }).first()
  try {
    // the Client card IS the step to the analysis-type page (AnalysisTab choosePortfolio -> page 2); Next would leave it
    await page.locator('[data-slot="analysis-portfolio-card"][data-portfolio="client"]').first().click({ timeout: 5000 })
    await page.locator('[data-slot="variant-card"]').first().waitFor({ state: 'visible', timeout: 10000 })
    rec.reached_type_step = true
    // the catalogue is read when the composer mounts; give a slow answer up to 15 s before the cards are pressed
    const tw = Date.now()
    while (Date.now() - tw < 15000 && !reads.length) await page.waitForTimeout(100)
    rec.entry_words = ((await page.locator('[data-slot="composer-picker-entry"]').first().textContent({ timeout: 1000 }).catch(() => null)) || '').trim().slice(0, 160) || null
    rec.loose_input_at_rest = await looseInput()
    await card('Multi-Comp').click(); await page.waitForTimeout(600)
    const multi = { picker_opened: await pickerOpen() }
    if (multi.picker_opened) {
      multi.done_disabled_at_0 = await page.locator('[data-slot="picker-done"]').isDisabled().catch(() => null)
      multi.models_offered = await page.locator('[data-slot="picker-model"]').count()
      await shot(page, `${label}-picker-multicomp`)
      await checks(page, `${label}-picker-multicomp`)
      for (let i = 0; i < Math.min(2, multi.models_offered); i++) await page.locator('[data-slot="picker-model"]').nth(i).click()
      multi.done_disabled_after = await page.locator('[data-slot="picker-done"]').isDisabled().catch(() => null)
      if (multi.done_disabled_after === false) { await page.locator('[data-slot="picker-done"]').click(); await page.waitForTimeout(500) }
      else { await page.locator('[data-slot="picker-cancel"]').click().catch(() => {}); await page.waitForTimeout(300) }
      multi.names = await names(); multi.variant = await variant(); multi.picker_open_after = await pickerOpen()
    }
    rec.multicomp = multi
    await card('Comparison').click(); await page.waitForTimeout(600)
    const one = { picker_opened: await pickerOpen() }
    if (one.picker_opened) {
      await page.locator('[data-slot="picker-search"]').fill('spy'); await page.waitForTimeout(300)
      one.search_matches = await page.locator('[data-slot="picker-etf"]').count()
      await shot(page, `${label}-picker-comparison`)
      if (one.search_matches > 0) { await page.locator('[data-slot="picker-etf"]').first().click(); await page.locator('[data-slot="picker-done"]').click(); await page.waitForTimeout(500) }
      else { await page.locator('[data-slot="picker-cancel"]').click().catch(() => {}); await page.waitForTimeout(300) }
      one.names = await names(); one.variant = await variant()
    }
    rec.comparison = one
    await page.locator('[data-slot="composer-comparisons"]').first().scrollIntoViewIfNeeded().catch(() => {})
    await shot(page, `${label}-picker-named`)
    await checks(page, `${label}-picker-named`)
    await card('Overview').click(); await page.waitForTimeout(500)
    rec.overview = { names: await names(), variant: await variant(), picker_open: await pickerOpen() }
    rec.loose_input_at_end = await looseInput()
  } catch (e) { rec.error = String(e.message || e).split('\n')[0].slice(0, 200) }
  await page.keyboard.press('Escape').catch(() => {})
  page.off('response', onResponse)
  composerPickers.push(rec)
  if (rec.loose_input_at_rest > 0 || rec.loose_input_at_end > 0) findings.push({ step: `${label}-picker`, check: 'composer:loose-input', claim: 'measured', observed: 'the composer shows a comparison input box outside the picker on the live client', rule: 'W2-05: no input box outside the picker' })
  if (rec.multicomp && rec.multicomp.picker_opened === false) findings.push({ step: `${label}-picker`, check: 'composer:no-picker', claim: 'measured', observed: 'the Multi-Comp card did not open the comparison picker', rule: 'W2-05: the card opens the picker' })
}

// ---- --dashboard-window (IRPT_DASHBD FWD-1, plan section 4; DSGN_IRPTV1 FAST item 72): on the Performance tab, select
// each account of the picker (first 8) and time, from the select, the dashboard's manifest and series reads (status, ms,
// the series' transfer size in bytes) and the painted chart (a drawn recharts area inside the dashboard chart slot), up to
// DASHBOARD_PAINT_CEILING_MS; an account with no dashboard records where the tab's own body showed instead. On a dashboard
// it presses each window preset once and counts EVERY /api/ request sent in the 1.5 s after the press (the window is
// computed in the browser, so the expected count is 0). Counts, times, sizes and the as-of words only: no figure.
const dashboardWindows = []
const DASHBOARD_PAINT_CEILING_MS = 60000
const PRESS_SETTLE_MS = 12000
// The recorder starts at the Performance tab's own press, so the tab's default account (the picker has no "All accounts"
// entry) is timed from the press; every other account is timed from its select, and the default one again last (warm).
let dashRec = null
function startDashboardRecorder(page) {
  const reads = []
  const byReq = new Map()
  const onRequest = (req) => {
    const p = pathOnly(req.url())
    if (!/^\/api\//.test(p)) return
    const m = p.match(/\/investor-reporting\/reporting\/[^/]+\/(manifest|series)$/)
    const r = { kind: m ? m[1] : 'other', sent: Date.now(), answered: null, status: null, transfer_bytes: null }
    reads.push(r); byReq.set(req, r)
  }
  const onResponse = async (res) => {
    const r = byReq.get(res.request()); if (!r || r.answered !== null) return
    r.answered = Date.now(); r.status = res.status()
    if (r.kind === 'series') { try { r.transfer_bytes = (await res.request().sizes()).responseBodySize } catch { /* size unread */ } }
  }
  const onFailed = (req) => { const r = byReq.get(req); if (r && r.answered === null) { r.answered = Date.now(); r.status = 'failed' } }
  page.on('request', onRequest); page.on('response', onResponse); page.on('requestfailed', onFailed)
  dashRec = { reads, t0: Date.now(), stop: () => { page.off('request', onRequest); page.off('response', onResponse); page.off('requestfailed', onFailed) } }
}
async function dashboardWindow(page, label) {
  const tab = '[data-slot="reporting-tab"]'
  if (!dashRec) startDashboardRecorder(page)
  const reads = dashRec.reads
  const picker = page.locator('[data-slot="performance-account-picker"] select').first()
  // the account list can answer after the tab's settle: wait for the picker's options (up to the ceiling)
  await picker.locator('option').first().waitFor({ state: 'attached', timeout: DASHBOARD_PAINT_CEILING_MS }).catch(() => {})
  const options = await picker.locator('option').evaluateAll((os) => os.map((o) => o.value)).catch(() => [])
  const current = await picker.inputValue().catch(() => null)
  const others = options.filter((v) => v !== current).slice(0, 7)
  // [value or null for the default view, the clock's start, warm?]
  const plan = [[null, dashRec.t0, false], ...others.map((v) => [v, null, false]), ...(current !== null && others.length ? [[current, null, true]] : [])]
  const rec = { label, accounts_in_picker: options.length, accounts: [] }
  for (let i = 0; i < plan.length && timeLeft(); i++) {
    const [value, start, warm] = plan[i]
    const from = value === null ? 0 : reads.length
    const t0 = start === null ? Date.now() : start
    if (value !== null) await picker.selectOption(value).catch(() => {})
    let paintedMs = null; let bodyMs = null
    while (Date.now() - t0 < DASHBOARD_PAINT_CEILING_MS) {
      const s = await page.evaluate((tabSel) => ({
        painted: !!document.querySelector(`${tabSel} [data-slot="dashboard-performance-chart"] .recharts-area-area[d]`),
        refused: !!document.querySelector(`${tabSel} [data-slot="dashboard-performance-refusal"]`),
        body: !!document.querySelector(`${tabSel} [data-slot="reporting-body"]`),
        dashboard: !!document.querySelector(`${tabSel} [data-slot="reporting-dashboard"]`),
      }), tab).catch(() => ({ painted: false, refused: false, body: false, dashboard: false }))
      const mine = reads.slice(from)
      if (s.painted || s.refused) { paintedMs = s.painted ? Date.now() - t0 : null; break }
      // The tab's own body counts only for an account with no series read at all: a covered account shows its own body
      // until the dashboard answers, and an account read in the background earlier sends no manifest on its select.
      const manifests = mine.filter((r) => r.kind === 'manifest')
      const settledNoSeries = !mine.some((r) => r.kind === 'series') && manifests.every((r) => r.answered !== null)
        && (value !== null || manifests.length > 0)
      if (s.body && !s.dashboard && settledNoSeries) { bodyMs = Date.now() - t0; break }
      await page.waitForTimeout(50)
    }
    const mine = reads.slice(from)
    const one = (kind) => mine.filter((r) => r.kind === kind).map((r) => ({ status: r.status, sent_ms: r.sent - t0, took_ms: r.answered === null ? null : r.answered - r.sent, transfer_bytes: r.transfer_bytes }))
    const acct = { step: i + 1, clock_from: value === null ? 'tab press' : 'select', warm_return: warm,
      manifest: one('manifest'), series: one('series'), other_api_requests: mine.filter((r) => r.kind === 'other').length,
      ms_to_painted_chart: paintedMs, ms_to_tab_body: bodyMs,
      dashboard_refused: await page.locator(`${tab} [data-slot="dashboard-performance-refusal"]`).count().catch(() => 0) > 0,
      data_through: ((await page.locator(`${tab} [data-slot="dashboard-data-through"]`).first().innerText({ timeout: 500 }).catch(() => '')) || '').trim() || null,
      chart_days: await page.locator(`${tab} [data-slot="dashboard-performance-chart"]`).first().getAttribute('data-days', { timeout: 500 }).catch(() => null),
      presets: [] }
    if (paintedMs !== null && !warm) {
      await shot(page, `${label}-dashboard-${i + 1}`)
      const presets = await page.locator(`${tab} [data-slot="dashboard-window-controls"] button[data-preset]`).evaluateAll((bs) => bs.map((b) => b.getAttribute('data-preset'))).catch(() => [])
      for (const id of presets) {
        const before = reads.length
        await page.locator(`${tab} [data-slot="dashboard-window-controls"] button[data-preset="${id}"]`).first().click({ timeout: 3000 }).catch(() => {})
        await page.waitForTimeout(1500)
        acct.presets.push({ preset: id, requests_after_press: reads.length - before,
          pressed: await page.locator(`${tab} button[data-preset="${id}"][aria-pressed="true"]`).count().catch(() => 0) > 0,
          measured_days: await page.locator(`${tab} [data-field="window.measuredDays"]`).first().innerText({ timeout: 500 }).catch(() => null) })
      }
      await checks(page, `${label}-dashboard-${i + 1}-presets`)
    }
    rec.accounts.push(acct)
  }
  // The picker's entries after the reads, every digit masked: the basis words a suffix carries, never a figure or a number.
  await page.waitForTimeout(1500)
  rec.picker_entries_masked = await picker.locator('option').evaluateAll((os) => os.map((o) => (o.textContent || '').replace(/\d/g, '#').trim())).catch(() => [])
  dashRec.stop(); dashRec = null
  dashboardWindows.push(rec)
  for (const a of rec.accounts) {
    const extra = a.presets.filter((p) => p.requests_after_press > 0)
    if (extra.length) findings.push({ step: `${label}-dashboard-${a.step}`, check: 'dashboard:window-request', claim: 'measured', observed: `a dashboard window press sent ${extra.map((p) => `${p.preset}:${p.requests_after_press}`).join(', ')} request(s)`, rule: 'IRPT_DASHBD plan section 4: a window change is computed in the browser' })
  }
}

async function modelScope(page, label, maxPresses = 10) {
  const read = () => page.evaluate(() => {
    const scope = document.querySelector('[data-slot="holdings-model-scope"]')
    const sleeve = document.querySelector('[data-slot="security-filter-sleeve"]')
    const chips = [...document.querySelectorAll('[data-slot="treemap-model-filter-option"]')]
    return {
      scope_line: scope ? scope.textContent.trim() : null,
      scope_model: scope ? scope.getAttribute('data-model') : null,
      chips: chips.length,
      chips_pressed: chips.filter((b) => b.getAttribute('aria-pressed') === 'true').map((b) => b.textContent.trim()),
      chips_locked: chips.filter((b) => b.disabled).length,
      sleeve_value: sleeve ? sleeve.value : null,
      sleeve_locked: sleeve ? sleeve.disabled : null,
      // security rows only: the panel's class-totals block is a table of its own and is hidden under a scope
      table_rows: document.querySelectorAll('[data-slot="security-list"] tbody tr:not([data-slot="class-total"]):not([data-slot="class-totals-remainder"])').length,
      table_empty_words: /No securities match these filters/.test((document.querySelector('[data-slot="security-list"]') || {}).innerText || ''),
      map_tiles: document.querySelectorAll('[data-slot="holdings-treemap"] [data-slot="treemap-tile"], [data-slot="holdings-treemap"] svg g rect').length,
    }
  })
  const before = await read()
  const seen = new Set()
  let pickText = null
  const opened = []
  for (let round = 0; round < maxPresses && timeLeft() && pickText === null; round++) {
    const btns = page.locator('[data-slot="holdings-drill-tree"] button:visible')
    // an account tile re-scopes the tab and its answer can take seconds: wait for the card's buttons to be back
    for (let w = 0; w < 20 && !(await btns.count().catch(() => 0)); w++) await page.waitForTimeout(500)
    const n = await btns.count().catch(() => 0)
    const texts = []
    for (let i = 0; i < n; i++) texts.push(((await btns.nth(i).innerText().catch(() => '')) || (await btns.nth(i).getAttribute('aria-label').catch(() => '')) || '').replace(/\s+/g, ' ').trim())
    // a breakdown opener first (it is where the pick control lives), then the Models tile, then the rest in page order
    const rank = (t) => (/view breakdown/i.test(t) ? 0 : /models/i.test(t) ? 1 : 2)
    const order = texts.map((t, i) => i).sort((a, b) => rank(texts[a]) - rank(texts[b]) || a - b)
    let pressed = false
    for (const i of order) {
      const b = btns.nth(i)
      const txt = texts[i]
      if (!txt || seen.has(txt) || DO_NOT_CLICK.test(txt)) continue
      seen.add(txt)
      if (await b.isDisabled().catch(() => true)) continue
      await b.click({ timeout: 3000 }).catch(() => {})
      await settle(page, 1800)
      opened.push(txt.slice(0, 40))
      pressed = true
      const pick = page.locator('[data-slot="breakdown-row-scope"]:visible').first()
      if (await pick.count().catch(() => 0)) {
        pickText = ((await pick.innerText().catch(() => '')) || '').replace(/\s+/g, ' ').trim()
        await checks(page, `${label}-model-pick-offered`)
        await pick.click({ timeout: 3000 }).catch(() => {})
        await settle(page, 1500)
      } else {
        await page.keyboard.press('Escape').catch(() => {})
        await page.waitForTimeout(400)
      }
      break
    }
    if (!pressed) break
  }
  const after = await read()
  await checks(page, `${label}-model-scope`)
  await page.locator('[data-slot="security-list"]').scrollIntoViewIfNeeded().catch(() => {})
  await page.waitForTimeout(400)
  await checks(page, `${label}-model-scope-table`)
  modelScopes.push({ label, opened, pick_offered: pickText !== null, pick_text: pickText, before, after })
  if (pickText === null) findings.push({ step: `${label}-model-scope`, check: 'model-scope:no-pick-offered', claim: 'measured', observed: `no model pick control appeared after opening ${opened.length} card button(s)`, rule: 'a card breakdown that lists models offers the scope pick (W2-22)' })
  // leave the tab as it was found: the scope line's own control returns to all models
  await page.locator('[data-slot="holdings-all-models"]').first().click({ timeout: 3000 }).catch(() => {})
  await page.waitForTimeout(400)
}

// ---- drill: every top-level row, then its first drillable child, down to 4 levels ------------------------------
// Rows are the SliceTable's `tr[data-slot=slice-row]` (clickable when data-child-count > 0); the breadcrumb is
// `nav[data-slot=holdings-breadcrumbs]`, whose first entry ("All holdings") returns to the top.
const DRILLABLE = 'tr[data-slot="slice-row"]:not([data-child-count="0"])'
async function drill(page, scopeSel, label) {
  const paths = []
  const crumbs = async () => ((await page.locator(`${scopeSel} nav[data-slot="holdings-breadcrumbs"]`).first().innerText().catch(() => '')) || '').replace(/\s+/g, ' ').trim()
  const toTop = async () => { await page.locator(`${scopeSel} nav[data-slot="holdings-breadcrumbs"]`).getByText('All holdings').first().click({ timeout: 3000 }).catch(() => {}); await settle(page, 700) }
  await toTop()
  const allRows = await page.locator(`${scopeSel} tr[data-slot="slice-row"]`).count().catch(() => 0)
  const topCount = Math.min(await page.locator(`${scopeSel} ${DRILLABLE}`).count().catch(() => 0), 4)
  log(`DRILL: ${allRows} slice row(s) at the top, ${topCount} drillable`)
  for (let top = 0; top < topCount && timeLeft(); top++) {
    await toTop()
    const steps = []
    for (let depth = 1; depth <= 4 && timeLeft(); depth++) {
      const row = depth === 1 ? page.locator(`${scopeSel} ${DRILLABLE}`).nth(top) : page.locator(`${scopeSel} ${DRILLABLE}`).first()
      if (!(await row.count().catch(() => 0))) break
      const txt = ((await row.locator('[data-slot="slice-label"]').first().innerText().catch(() => '')) || '').trim()
      const kids = Number(await row.getAttribute('data-child-count').catch(() => '0')) || 0
      await row.click({ timeout: 3000 }).catch(() => {})
      await settle(page, 900)
      const rowsAfter = await page.locator(`${scopeSel} tr[data-slot="slice-row"]`).count().catch(() => 0)
      const where = await crumbs()
      steps.push({ depth, clicked: txt.slice(0, 60), child_count: kids, rows_after: rowsAfter, breadcrumb: where.slice(0, 160) })
      await checks(page, `${label}-row${top + 1}-drill${depth}`)
      if (rowsAfter === 1) findings.push({ step: `${label}-row${top + 1}-drill${depth}`, check: 'drill:single-child-level', claim: 'measured', observed: `under "${txt.slice(0, 60)}" the next level has exactly one row (breadcrumb: ${where.slice(0, 100)})`, rule: 'no drill layer with a single child (an unnecessary layer)' })
    }
    paths.push({ top: top + 1, steps })
  }
  await toTop()
  return paths
}

// ---- main ---------------------------------------------------------------------------------------------------------
let armedHere = false
let holder = null
let browser
const t0 = Date.now()
try {
  let password = null
  if (opt.login) {
    if (opt.arm) { const armOut = py('arm'); log(armOut.trim()); holder = (armOut.match(/^HOLDER (\S+)/m) || [])[1] || null; armedHere = true } else log(py('status').trim())
    password = py('secret', { UI_WALK_CHILD: '1' })
  } else log('NO LOGIN: signed-out control, the walker account is not touched')
  try {
    browser = await chromium.launch({ channel: 'msedge', headless: !opt.headed })
  } catch {
    browser = await chromium.launch({ headless: !opt.headed })
  }
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } })
  const page = await context.newPage()
  page.on('console', (m) => { if (m.type() === 'error') consoleErrors.push({ step, text: m.text().slice(0, 300) }) })
  page.on('pageerror', (e) => consoleErrors.push({ step, text: 'PAGE ERROR: ' + String(e).slice(0, 300) }))
  page.on('request', noteHopRequest)
  page.on('response', async (res) => {
    const req = res.request(); const p = pathOnly(req.url())
    netlog.push([req.method(), res.status(), p].join('\t'))
    if (/lead-panel\/rankings\/trending\/price/.test(p)) lastPriceBody = await res.text().then((t) => `HTTP ${res.status()}\n${t}`).catch((e) => `body read failed: ${e.message}`)
    if (!/\/api\//.test(p)) return
    let reason = null; let state = null; let ok = null
    let body = null
    try {
      const j = await res.json(); body = j; ok = j.ok ?? null; state = j.status?.state ?? null; reason = j.status?.public_reason_code ?? null
      if (opt.holdingsAggregates && /\/investor-reporting\/holdings\//.test(p)) readHoldingsAggregates(p, j)
    } catch { /* not json */ }
    if (requestHops && hopStart.has(req)) noteHopResponse(req, res, body, await req.allHeaders().catch(() => req.headers()))
    if (res.status() >= 400 || ok === false || (reason && !/READY$/.test(reason))) apiIssues.push({ step, method: req.method(), path: p, http: res.status(), ok, state, reason })
  })
  await page.route('**/*', (route) => {
    const req = route.request(); const m = req.method(); const p = pathOnly(req.url())
    if (m === 'GET' || m === 'HEAD' || m === 'OPTIONS') return route.continue()
    if (ADMITTED_POST.some((re) => re.test(p))) return route.continue()
    // The portal's own telemetry posts every ~10 s from login. Answer it locally (it never leaves the browser) so
    // the page does not log a failed flush on every tick and drown the real console errors.
    if (/\/analytics\/ingest$/.test(p)) { stubbed += 1; return route.fulfill({ status: 204, body: '' }) }
    guard.push([step, m, p].join('\t'))
    return route.abort('blockedbyclient')
  })

  // login through the local dev build
  if (opt.login) {
    step = 'login'
    await page.goto(opt.base + '/login', { waitUntil: 'domcontentloaded', timeout: 30000 })
    await page.fill('#email', EMAIL)
    await page.fill('#password', password)
    await page.click('button[type=submit]')
    await page.waitForURL((u) => !/\/login/.test(u.pathname), { timeout: 30000 }).catch(() => {})
    await settle(page)
    if (/\/login/.test(new URL(page.url()).pathname)) {
      await checks(page, 'login-failed')
      throw new Error('login did not complete (still on /login) -- see the login-failed shot')
    }
    log('LOGGED IN at', page.url())
  }

  for (const route of opt.routes) {
    if (!timeLeft()) break
    step = `route ${route}`
    await page.goto(opt.base + route, { waitUntil: 'domcontentloaded', timeout: 30000 })
    await settle(page, 2500)
    await checks(page, `${route}-load`)
    if (route.startsWith('/investor-reporting')) {
      // the client search: the empty-query state, then each client
      const combo = page.getByRole('combobox', { name: 'Client search' })
      if (await combo.count().catch(() => 0)) {
        step = 'search-empty'
        await combo.click().catch(() => {})
        await page.waitForTimeout(1200)
        await checks(page, 'search-open-empty')
        for (const client of opt.clients) {
          if (!timeLeft()) break
          step = `search ${client}`
          // Clear the box for real: after a pick the page holds the accepted label, and fill('') alone can leave the
          // previous query in place (a 2026-09-27 walk searched both names run together).
          await combo.click().catch(() => {})
          await combo.press('Control+A').catch(() => {})
          await combo.press('Backspace').catch(() => {})
          await combo.fill('').catch(() => {})
          const left = await combo.inputValue().catch(() => '')
          if (left) findings.push({ step: `search-${client}`, check: 'walker:input-not-cleared', claim: 'measured', observed: `the search box still held "${left}" before typing`, rule: 'each search starts from an empty box' })
          await combo.pressSequentially(client, { delay: 40 }).catch(() => {})
          const typedAt = Date.now()
          // Two times, from the last keystroke: when the list FIRST holds an option carrying every typed token
          // (the client is findable), and when the search has ANSWERED (the box stops reading "Loading"), each up to
          // SEARCH_ANSWER_CEILING_MS. The usual screenshot is taken once, at 2.5 s: what a person sees first.
          const typedTokens = client.toLowerCase().split(/[\s,&]+/).filter(Boolean)
          let firstMatchMs = null
          let answeredMs = null
          let shotTaken = false
          while (Date.now() - typedAt < SEARCH_ANSWER_CEILING_MS && (firstMatchMs === null || answeredMs === null)) {
            const state = await page.evaluate((tokens) => {
              const box = document.querySelector('[role="combobox"][aria-label="Client search"]')
              const listId = box ? box.getAttribute('aria-controls') : null
              const list = listId ? document.getElementById(listId) : null
              const options = list ? [...list.querySelectorAll('[role="option"]')].map((o) => (o.textContent || '').toLowerCase()) : []
              return {
                busy: /Loading clients/.test(document.body.innerText || ''),
                matched: options.some((o) => tokens.every((t) => o.includes(t))),
              }
            }, typedTokens).catch(() => ({ busy: true, matched: false }))
            const elapsed = Date.now() - typedAt
            if (firstMatchMs === null && state.matched) firstMatchMs = elapsed
            if (answeredMs === null && !state.busy && elapsed > 400) answeredMs = elapsed
            if (!shotTaken && elapsed >= 2500) { shotTaken = true; await checks(page, `search-${client}`) }
            await page.waitForTimeout(200)
          }
          if (!shotTaken) { await page.waitForTimeout(Math.max(0, 2500 - (Date.now() - typedAt))); await checks(page, `search-${client}`) }
          searchTimings.push({ client_chars: client.length, first_match_ms: firstMatchMs, answered_ms: answeredMs, ceiling_ms: SEARCH_ANSWER_CEILING_MS })
          log('SEARCH TIMING', JSON.stringify(searchTimings[searchTimings.length - 1]))
          if (answeredMs === null || answeredMs > 2500) await checks(page, `search-${client}-answered`)
          // Rank within THIS search's own listbox (aria-controls), never page-wide: the Firm <select> options also carry
          // role=option and sit earlier in the DOM (the same walk read "#5 of 17" for a client shown first of 13).
          const listId = await combo.getAttribute('aria-controls').catch(() => null)
          const optLoc = listId ? page.locator(`[id="${listId}"]`).getByRole('option') : page.getByRole('listbox').last().getByRole('option')
          const opts = await optLoc.allInnerTexts().catch(() => [])
          const tokens = client.toLowerCase().split(/[\s,]+/).filter(Boolean)
          const rank = opts.findIndex((o) => tokens.every((t) => o.toLowerCase().includes(t)))
          if (rank > 0) findings.push({ step: `search-${client}`, check: 'search:ranking', claim: 'measured', observed: `the option matching every token of "${client}" is #${rank + 1} of ${opts.length}, not first`, rule: 'the exact client comes first' })
          if (rank < 0) findings.push({ step: `search-${client}`, check: 'search:no-match', claim: 'measured', observed: `no option contains every token of "${client}" (${opts.length} options)`, rule: 'the client is findable by name' })
          const pick = optLoc.nth(Math.max(rank, 0))
          if (!(await pick.count().catch(() => 0))) continue
          step = `client ${client}`
          await pick.click().catch(() => {})
          await settle(page, 3000)
          await checks(page, `client-${client}`)
          // identity panel expands
          await exploreScope(page, '[data-slot="identity-card"]', `identity-${client}`)
          // each tab
          const tabs = page.locator('[data-slot="tab-shell"] .overflow-x-auto button')
          const nTabs = await tabs.count().catch(() => 0)
          for (let i = 0; i < nTabs && timeLeft(); i++) {
            const name = ((await tabs.nth(i).innerText().catch(() => '')) || `tab${i}`).trim().toLowerCase()
            step = `tab ${name}`
            await page.keyboard.press('Escape').catch(() => {})   // no dialog may stand over the tab strip
            await page.waitForTimeout(300)
            if (opt.openRequest && /analysis/.test(name)) requestHops = { t0: Date.now(), rows: [] }
            if (opt.dashboardWindow && /performance/.test(name)) startDashboardRecorder(page)
            await tabs.nth(i).click().catch(() => {})
            await settle(page, 2500)
            await checks(page, `${client}-${name}`)
            if (opt.performanceState && /performance/.test(name)) {
              const got = await waitForPerformanceState(page)
              performanceStates.push({ client_chars: client.length, ceiling_ms: PERFORMANCE_STATE_CEILING_MS, ...got })
              log('PERFORMANCE STATE', JSON.stringify(performanceStates[performanceStates.length - 1]).slice(0, 600))
              await checks(page, `${client}-performance-answered`)
            }
            // Drill FIRST, on the tab's default view: the explore step below changes selects and opens popups.
            if (/holdings/.test(name)) {
              // --account-drill runs on the tab's default view, BEFORE the generic drill below presses a tile itself.
              if (opt.accountDrill) {
                await accountDrill(page, `${client}-holdings`)
                log('ACCOUNT DRILL', JSON.stringify(accountDrills[accountDrills.length - 1]).slice(0, 900))
              }
              const p = await drill(page, '[data-slot="holdings-tab"]', `${client}-holdings`)
              drillPaths.push({ client, paths: p })
              log('DRILL PATHS', JSON.stringify(p).slice(0, 400))
              if (opt.modelScope) {
                await modelScope(page, `${client}-holdings`)
                log('MODEL SCOPE', JSON.stringify(modelScopes[modelScopes.length - 1]).slice(0, 900))
              }
            }
            // --dashboard-window runs on the tab's default view, BEFORE the explore step below changes selects.
            if (opt.dashboardWindow && /performance/.test(name)) {
              await dashboardWindow(page, `${client}-performance`)
              log('DASHBOARD WINDOW', JSON.stringify(dashboardWindows[dashboardWindows.length - 1]).slice(0, 1500))
            }
            // --composer-picker runs on the tab's default view, BEFORE the explore step below changes selects.
            if (opt.composerPicker && /analysis/.test(name)) {
              await composerPicker(page, `${client}-analysis`)
              log('COMPOSER PICKER', JSON.stringify(composerPickers[composerPickers.length - 1]).slice(0, 1200))
            }
            await exploreScope(page, '[data-slot="tabs"]', `${client}-${name}`)
            if (opt.periodsPerAccount && /performance/.test(name)) await periodsPerAccount(page, '[data-slot="tabs"]', `${client}-${name}`)
            if (opt.openRequest && /analysis/.test(name)) {
              await openRequest(page, `${client}-analysis`, opt.openRequest)
              log('OPEN REQUEST', JSON.stringify(openedRequests[openedRequests.length - 1]).slice(0, 900))
            }
            if (opt.deep) {
              const pressed = await pressAll(page, '[data-slot="tabs"]', `${client}-${name}`)
              log('PRESSED', name, JSON.stringify(pressed).slice(0, 300))
            }
          }
        }
        if (!opt.clients.length) log('NOTE: no --client given; only the page load and the empty search were walked')
      }
    } else if (route.startsWith('/security-analysis')) {
      await walkSecurityAnalysis(page, route)
    } else {
      for (const label of opt.presses || []) {
        if (DO_NOT_CLICK.test(label)) { findings.push({ step: `press ${label}`, check: 'walker:press-refused', claim: 'measured', observed: `--press "${label}" names a write word; not pressed` }); continue }
        const pressed = await clickLabel(page, label)
        await page.waitForTimeout(PRESS_SETTLE_MS)
        await settle(page, 2500)
        log('PRESS', label, pressed ? 'pressed' : 'NOT FOUND')
        await checks(page, `${route}-press-${label}`)
      }
      await exploreScope(page, 'body', route)
    }
  }
} catch (e) {
  if (!(e instanceof WalkVoid)) {
    findings.push({ step, check: 'walker:error', claim: 'measured', observed: String(e.message || e).split('\n')[0] })
    log('ERROR', String(e.message || e).split('\n')[0])
  }
} finally {
  if (browser) await browser.close().catch(() => {})
  if (armedHere && !opt.keepArmed) { try { log(py('disarm', {}, holder).trim()) } catch (e) { log('DISARM FAILED -- run: python .claude/skills/ui-walk/ui_walker_account.py disarm <holder> (holder: armedBy in status)', String(e.stderr || e.message).slice(0, 300)) } }
  // outputs: one UNIQUE finding per (check, observed, selector), with every step and screenshot it was seen at
  const byKey = new Map()
  for (const f of findings) {
    const k = [f.check, f.observed, f.selector || ''].join('|')
    const u = byKey.get(k) || { ...f, steps: [], screenshots: [] }
    u.steps.push(f.step); if (f.screenshot) u.screenshots.push(f.screenshot)
    byKey.set(k, u)
  }
  const unique = [...byKey.values()].map((u, i) => { const { step: _s, screenshot: _sh, ...rest } = u; return { id: `UIW-${stamp}-${String(i + 1).padStart(3, '0')}`, ...rest } })
  const counts = {}
  for (const f of unique) counts[f.check] = (counts[f.check] || 0) + 1
  const doc = { schema_version: '1.1', tool: 'ui-walk', stamp, base: opt.base, routes: opt.routes, clients: opt.clients, minutes: +((Date.now() - t0) / 60000).toFixed(1), screenshots: shotN, raw_finding_count: findings.length, finding_count: unique.length, counts, guard_aborts: guard.length, telemetry_stubbed: stubbed, api_issues: apiIssues, console_errors: consoleErrors, drill_paths: drillPaths, findings: unique }
  writeFileSync(path.join(OUT, 'findings.json'), JSON.stringify(doc, null, 1))
  if (loadStates.length) writeFileSync(path.join(OUT, 'load-states.json'), JSON.stringify(loadStates, null, 1))
  if (timelineDays.length) writeFileSync(path.join(OUT, 'timeline-days.json'), JSON.stringify(timelineDays, null, 1))
  if (modelScopes.length) writeFileSync(path.join(OUT, 'model-scope.json'), JSON.stringify(modelScopes, null, 1))
  if (accountDrills.length) writeFileSync(path.join(OUT, 'account-drill.json'), JSON.stringify(accountDrills, null, 1))
  if (composerPickers.length) writeFileSync(path.join(OUT, 'composer-picker.json'), JSON.stringify(composerPickers, null, 1))
  if (dashboardWindows.length) writeFileSync(path.join(OUT, 'dashboard-window.json'), JSON.stringify(dashboardWindows, null, 1))
  if (searchTimings.length) writeFileSync(path.join(OUT, 'search-timings.json'), JSON.stringify(searchTimings, null, 1))
  if (openedRequests.length) writeFileSync(path.join(OUT, 'analysis-request.json'), JSON.stringify(openedRequests, null, 1))
  if (holdingsAggregates.length) writeFileSync(path.join(OUT, 'holdings-aggregates.json'), JSON.stringify(holdingsAggregates, null, 1))
  if (performanceStates.length) writeFileSync(path.join(OUT, 'performance-state.json'), JSON.stringify(performanceStates, null, 1))
  writeFileSync(path.join(OUT, 'lead-lists.json'), JSON.stringify({ schema_version: '1.0', tool: 'ui-walk', stamp, lists: leadLists }, null, 1))
  writeFileSync(path.join(OUT, 'netlog.tsv'), netlog.join('\n') + '\n')
  writeFileSync(path.join(OUT, 'guard.tsv'), guard.join('\n') + '\n')
  const md = [`# ui-walk ${stamp}`, '', `base ${opt.base}; routes ${opt.routes.join(', ')}; clients ${opt.clients.join(' | ') || '(none)'}; ${doc.minutes} min; ${shotN} screenshots`, '',
    `- unique findings: ${unique.length} (from ${findings.length} step observations)`, `- guard aborts (non-admitted writes blocked): ${guard.length}; telemetry answered locally: ${stubbed}`, `- API answers not READY / not ok: ${apiIssues.length}`, `- console errors: ${consoleErrors.length}`, '',
    '| check | unique findings |', '|---|---|', ...Object.entries(counts).sort((a, b) => b[1] - a[1]).map(([k, v]) => `| ${k} | ${v} |`), '',
    '## Unique findings', '', ...unique.map((f) => `- **${f.id}** \`${f.check}\` -- ${String(f.observed).slice(0, 160)} (steps: ${f.steps.length}; first shot ${f.screenshots[0] || 'n/a'})`), '',
    'Screenshots and findings are under this folder (gitignored: they carry client data).'].join('\n')
  writeFileSync(path.join(OUT, 'summary.md'), md + '\n')
  log('OUT', OUT)
  log(`SUMMARY: ${unique.length} unique finding(s) from ${findings.length} observations, ${shotN} screenshot(s), ${guard.length} guard abort(s), ${stubbed} telemetry stubbed, ${apiIssues.length} API issue(s), ${consoleErrors.length} console error(s), walk void: ${walkVoid ? 'yes' : 'no'}`)
  if (walkVoid) process.exitCode = 3
}
