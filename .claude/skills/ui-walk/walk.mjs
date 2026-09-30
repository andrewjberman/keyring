// /ui-walk walker: logs the Opal UI walker service account into the LOCAL dev build (localhost, `bun run dev:live`),
// walks pages like a person (search, tabs, dropdowns, expands, drill rows, account pickers), screenshots every step,
// and runs in-page checks for frontend defects. READ-ONLY by construction: a network guard aborts every request
// outside the admitted classes. Output goes to the gitignored tmp/ui-walk/<stamp>/ because screenshots carry
// client data.
//
// Usage (from any cwd):
//   node .claude/skills/ui-walk/walk.mjs [--base http://localhost:5174] [--route /investor-reporting]
//        [--client "Thiessen, Anna"]... [--max-minutes 40] [--no-arm] [--keep-armed] [--headed] [--no-login]
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
const opt = { base: 'http://localhost:5174', routes: [], clients: [], securities: [], maxMinutes: 40, arm: true, keepArmed: false, headed: false, deep: false, login: true, settleExtraMs: 0, periodsPerAccount: false }
for (let i = 0; i < argv.length; i++) {
  const a = argv[i]
  if (a === '--base') opt.base = argv[++i]
  else if (a === '--route') {
    // Git Bash (MSYS) rewrites a leading-slash argv into "C:/Program Files/Git/<route>" before node sees it; undo that.
    opt.routes.push(argv[++i].replace(/^[A-Za-z]:[\\/].*?[\\/]Git(?=[\\/])/i, '').replace(/\\/g, '/'))
  }
  else if (a === '--client') opt.clients.push(argv[++i])
  else if (a === '--security') opt.securities.push(argv[++i])
  else if (a === '--max-minutes') opt.maxMinutes = Number(argv[++i])
  else if (a === '--no-arm') opt.arm = false
  else if (a === '--keep-armed') opt.keepArmed = true
  else if (a === '--headed') opt.headed = true
  else if (a === '--deep') opt.deep = true
  else if (a === '--no-login') opt.login = false
  // Extra wait after every settle, for a read whose answer lands after networkidle (a retained Performance
  // reopen fires after the account switch, so a 1200 ms settle screenshots "Loading"). Default 0: unchanged.
  else if (a === '--settle-extra-ms') opt.settleExtraMs = Number(argv[++i])
  else if (a === '--periods-per-account') opt.periodsPerAccount = true
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
const py = (cmd, extraEnv = {}) => execFileSync('python', [ACCOUNT, cmd], { encoding: 'utf8', env: { ...process.env, ...extraEnv }, stdio: ['ignore', 'pipe', 'pipe'] })

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
  for (const p of [...document.querySelectorAll('[role=listbox],[role=menu],[role=dialog],[role=tooltip],[data-radix-popper-content-wrapper]')].filter(vis)) {
    const r = p.getBoundingClientRect(); let covered = 0; let by = null
    for (const fx of [0.2, 0.5, 0.8]) for (const fy of [0.1, 0.5, 0.9]) {
      const x = r.left + r.width * fx; const y = r.top + r.height * fy
      if (x < 0 || y < 0 || x >= vw || y >= vh) continue
      const top = document.elementFromPoint(x, y)
      if (top && !p.contains(top)) { covered++; by = by || top }
    }
    if (covered) out.push({ check: 'occluded-popover', observed: `${covered} of 9 sample points of an open ${p.getAttribute('role') || 'popover'} are covered by another element`, selector: trail(p), covered_by: by ? trail(by) : null, covered_by_text: by ? (by.innerText || '').trim().slice(0, 60) : null, rect: box(p), rule: 'an open dropdown renders above every page element (z-order)' })
  }
  // 2. unconnected fields, placeholders, raw codes, sample content
  const pats = [[/\bnot supplied\b/i, 'not-supplied'], [/\bunavailable\b/i, 'unavailable'], [/\bvalue pending\b/i, 'value-pending'], [/^\s*unknown\s*$/i, 'unknown'], [/\bwithheld\b/i, 'withheld'], [/\bn\/a\b/i, 'n-a'], [/illustrative sample/i, 'sample-content'], [/\b(?:[A-Z][A-Z0-9]{2,}_)+[A-Z0-9]{2,}\b/, 'raw-code']]
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
// Movement x Subject x View = 8 lead-panel states (constants.ts MOVEMENT_OPTIONS / SUBJECT_OPTIONS; LeadPanel.tsx view
// toggle). A --security is picked by clicking its row text in the lead panel, else typed into "Search any ticker".
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
async function amgtLeadState(page, movement, subject, view) {
  const okM = await clickLabel(page, movement)
  const okS = await clickLabel(page, subject)
  const v = page.locator(`[aria-label="${view}"]`).first()
  const okV = (await v.count().catch(() => 0)) ? await v.click({ timeout: 4000 }).then(() => true).catch(() => false) : false
  const missing = [!okM && movement, !okS && subject, !okV && view].filter(Boolean)
  if (missing.length) findings.push({ step, check: 'walker:control-missing', claim: 'measured', observed: `control not found or not clickable: ${missing.join(', ')}` })
  await settle(page, 1500)
}
async function walkSecurityAnalysis(page, route) {
  for (const movement of ['Trending', 'Breakout']) {
    for (const subject of ['Chatter', 'Price']) {
      for (const view of ['List view', 'Chart view']) {
        if (!timeLeft()) return
        step = `amgt lead ${movement}-${subject}-${view}`
        await amgtLeadState(page, movement, subject, view)
        await checks(page, `lead-${movement}-${subject}-${view.split(' ')[0]}`)
      }
    }
  }
  for (const sec of opt.securities) {
    if (!timeLeft()) return
    step = `amgt select ${sec}`
    await page.goto(opt.base + route, { waitUntil: 'domcontentloaded', timeout: 30000 })
    await settle(page, 2500)
    await amgtLeadState(page, 'Trending', 'Price', 'List view')
    let picked = false
    const row = page.getByText(sec, { exact: true }).first()
    if (await row.count().catch(() => 0)) picked = await row.click({ timeout: 4000 }).then(() => true).catch(() => false)
    if (!picked) {
      const box = page.getByPlaceholder('Search any ticker')
      await box.fill(sec).catch(() => {})
      await box.press('Enter').catch(() => {})
    }
    await settle(page, 3000)
    await checks(page, `${sec}-overlay`)
    for (const tab of AMGT_TABS) {
      if (!timeLeft()) return
      step = `amgt ${sec} tab ${tab}`
      if (!(await clickLabel(page, tab))) findings.push({ step, check: 'walker:control-missing', claim: 'measured', observed: `tab not found: ${tab}` })
      await settle(page, 2500)
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
let browser
const t0 = Date.now()
try {
  let password = null
  if (opt.login) {
    if (opt.arm) { log(py('arm').trim()); armedHere = true } else log(py('status').trim())
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
  page.on('response', async (res) => {
    const req = res.request(); const p = pathOnly(req.url())
    netlog.push([req.method(), res.status(), p].join('\t'))
    if (!/\/api\//.test(p)) return
    let reason = null; let state = null; let ok = null
    try { const j = await res.json(); ok = j.ok ?? null; state = j.status?.state ?? null; reason = j.status?.public_reason_code ?? null } catch { /* not json */ }
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
          await page.waitForTimeout(2500)
          await checks(page, `search-${client}`)
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
            await tabs.nth(i).click().catch(() => {})
            await settle(page, 2500)
            await checks(page, `${client}-${name}`)
            // Drill FIRST, on the tab's default view: the explore step below changes selects and opens popups.
            if (/holdings/.test(name)) {
              const p = await drill(page, '[data-slot="holdings-tab"]', `${client}-holdings`)
              drillPaths.push({ client, paths: p })
              log('DRILL PATHS', JSON.stringify(p).slice(0, 400))
            }
            await exploreScope(page, '[data-slot="tabs"]', `${client}-${name}`)
            if (opt.periodsPerAccount && /performance/.test(name)) await periodsPerAccount(page, '[data-slot="tabs"]', `${client}-${name}`)
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
  if (armedHere && !opt.keepArmed) { try { log(py('disarm').trim()) } catch (e) { log('DISARM FAILED -- run: python .claude/skills/ui-walk/ui_walker_account.py disarm', String(e.stderr || e.message).slice(0, 300)) } }
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
