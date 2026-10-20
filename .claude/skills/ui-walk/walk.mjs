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
//        [--firm "<label>"] [--first-client]   (--firm presses the header Firm option by its visible label first)
//        [--open-first "<summary text>"]...    (expand each closed <details> whose summary reads that text FIRST, before the 20-click cap)
//
// By default it ARMS the account, walks, and DISARMS in a finally block (always, even on failure).
import { createRequire } from 'node:module'
import { execFileSync } from 'node:child_process'
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import path from 'node:path'
import { isSignInPage } from './signin_detect.mjs'
import { orderSummaries } from './open_first.mjs'

// UI_WALK_ROOT lets a copy of this file in a linked worktree drive the shared tree's portal/node_modules and tmp/.
const ROOT = process.env.UI_WALK_ROOT || fileURLToPath(new URL('../../../', import.meta.url))
const require = createRequire(path.join(ROOT, 'portal', 'package.json'))
const { chromium } = require('playwright-core')
const ACCOUNT = path.join(ROOT, '.claude', 'skills', 'ui-walk', 'ui_walker_account.py')
const EMAIL = 'opal-ui-walker@opal.test'

// ---- args ---------------------------------------------------------------------------------------------------------
const argv = process.argv.slice(2)
const opt = { base: 'http://localhost:5174', routes: [], clients: [], securities: [], maxMinutes: 40, arm: true, keepArmed: false, headed: false, deep: false, hovers: [], login: true, settleExtraMs: 0, periodsPerAccount: false, days: [], thread: null, expectTexts: [], reloadReopen: false, firm: null, firstClient: false, openFirst: [] }
for (let i = 0; i < argv.length; i++) {
  const a = argv[i]
  if (a === '--base') opt.base = argv[++i]
  else if (a === '--route') {
    // Git Bash (MSYS) rewrites a leading-slash argv into "C:/Program Files/Git/<route>" before node sees it; undo that.
    opt.routes.push(argv[++i].replace(/^[A-Za-z]:[\\/].*?[\\/]Git(?=[\\/])/i, '').replace(/\\/g, '/'))
  }
  else if (a === '--client') opt.clients.push(argv[++i])
  // --firm "<label>": before the client search, press the header's Firm option whose visible label is <label> (FirmDropdown.tsx).
  // --first-client (with --firm, no --client): walk the FIRST client the empty search lists, as --client walks a named one.
  else if (a === '--firm') { opt.firm = argv[++i]; if (!opt.firm || opt.firm.startsWith('--')) throw new Error('--firm wants a label') }
  else if (a === '--first-client') opt.firstClient = true
  // --probe-get <path> (repeatable; 2.0.0_SA_COO~P 105138 via MSTR 105141): after sign-in, GET that same-origin path
  // from inside the page with the Authorization header the page itself sent, and once WITHOUT it (the control);
  // statuses only are printed and written (probe-get.json). GET only: the guard is unchanged.
  else if (a === '--probe-get') (opt.probeGets = opt.probeGets || []).push(argv[++i].replace(/^[A-Za-z]:[\\/].*?[\\/]Git(?=[\\/])/i, '').replace(/\\/g, '/'))
  else if (a === '--hover') opt.hovers.push(argv[++i])
  // --hover-after-press "<css>@<xfrac>" (repeatable, plain routes): AFTER every --press, move the mouse onto the first
  // visible match of <css> at x = xfrac (0..1) of its width, mid-height, and shoot the viewport + run the checks. For a
  // hover-only popup behind page state no URL carries (a chart tooltip on a toggled view). Requested by 2.0.0_SA_COO~D1.
  else if (a === '--hover-after-press') {
    const v = String(argv[++i] || ''); const at = v.lastIndexOf('@'); const frac = Number(v.slice(at + 1))
    if (at < 1 || !Number.isFinite(frac) || frac < 0 || frac > 1) throw new Error(`--hover-after-press wants "<css>@<xfrac 0..1>", got "${v}"`)
    ;(opt.hoverAfterPress = opt.hoverAfterPress || []).push({ css: v.slice(0, at), frac })
  }
  else if (a === '--security') opt.securities.push(argv[++i])
  // --open-first "<summary text>" (repeatable): in every scope, a closed <details> whose summary reads that text (trimmed,
  // case-insensitive) is expanded before the others, so the 20-click cap does not run out first (AMGT_RESAPP round 107).
  else if (a === '--open-first') opt.openFirst.push(String(argv[++i] || ''))
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
  // --security-press <css> (repeatable, /security-analysis): after each --security name's overlay shot, press the first visible
  // match and shoot the after-state (step <sec>-press-<k>). --window-press <css> (repeatable): on the Thesis tab open the
  // Investment-thesis card, press the first visible match inside the dialog, read document.activeElement, shoot, Escape; one
  // record per press in window-press.json. A target whose text matches DO_NOT_CLICK.test is refused (walker:press-refused);
  // a missing target is walker:press-not-found. Read-only: the network guard is unchanged.
  else if (a === '--security-press') (opt.securityPresses = opt.securityPresses || []).push(String(argv[++i] || ''))
  else if (a === '--window-press') (opt.windowPresses = opt.windowPresses || []).push(String(argv[++i] || ''))
  // both presses test DO_NOT_CLICK.test (walker:press-refused) and record walker:press-not-found; see windowPresses() and walkSecurityAnalysis()
  else if (a === '--press') (opt.presses = opt.presses || []).push(String(argv[++i] || ''))
  // --contrast-table (plain routes): every visible interactive control's (ground, ink) pair at rest, on hover and, where
  // the control says so (aria-pressed / aria-selected / aria-current), selected -- graded against SC 1.4.3. Run after the
  // presses, before the explore step. Writes contrast-table.json. DSGN_REBRND round 3 E4 (FWD-13). Also every
  // non-interactive text pair at rest, grouped, state 'text' (row S10).
  else if (a === '--contrast-table') opt.contrastTable = true
  // --tz <IANA zone>: the browser's own time zone (default: this machine's). A page that formats dates must read the
  // same in every zone; DSGN_REBRND 4c's footer hour did not under UTC.
  else if (a === '--tz') opt.tz = String(argv[++i] || '')
  else if (a === '--holdings-aggregates') opt.holdingsAggregates = true
  // --map-tiles (with --client): on the Holdings tab's default view, count the Securities map's drawn tiles against the
  // distinct securities in the served snapshot it shows (CTO batch 178 H-1 proof). Counts only.
  else if (a === '--map-tiles') opt.mapTiles = true
  else if (a === '--performance-state') opt.performanceState = true
  else if (a === '--expect-text') opt.expectTexts.push(String(argv[++i] || ''))
  else if (a === '--reload-reopen') opt.reloadReopen = true
  // --card-census (with --open-request): the opened report's cards read as a reader sees them (title a name or a code,
  // unit words, cards sharing one title and Label, validation and source lines on the face) and the served sections
  // answer's SHAPE (key names and category tokens only, never a value). Writes into analysis-request.json.
  else if (a === '--card-census') opt.cardCensus = true
  else if (a === '--no-login') opt.login = false
  // --forced <rules.json> (AMGT_RESAPP round 126, CTO msg 8584): force ONE named GET answer on the running build, the page code and
  // the backend staying real. The file is a JSON array of rules {label, match (a regex over the request URL), mode, ...}:
  //   mode "status": answer 500 (or `status`) with a small JSON error;  mode "abort": the request fails;
  //   mode "patch":  the REAL answer is fetched, then `set` (dotted paths to values) and `delete` (dotted paths) are applied to its
  //                  JSON body and it is answered (a 200 body the backend did not send): NAMED as forced in forced.json.
  // Only GET requests are touched; every other request still meets the guard. forced.json (beside findings.json) lists each rule
  // and how many requests it answered.
  else if (a === '--forced') opt.forced = String(argv[++i] || '')
  // --forced-press "<label>" (repeatable, with --security): press the header button with that exact label ("Export as a document" or
  // "Print" only), AFTER the forced rules are in place, so the request the press makes is the forced one and no document is made.
  else if (a === '--forced-press') (opt.forcedPresses = opt.forcedPresses || []).push(String(argv[++i] || ''))
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
if (opt.firstClient && (!opt.firm || opt.clients.length)) throw new Error('--first-client wants --firm "<label>" and no --client')
if (!opt.routes.length && !opt.probeGets?.length) opt.routes.push('/investor-reporting')
if ((opt.probeGets || []).some((p) => !/^\/api\//.test(p))) throw new Error('REFUSED: --probe-get takes a same-origin /api/ path')
if (!/^http:\/\/(localhost|127\.0\.0\.1):\d+$/.test(opt.base)) throw new Error('REFUSED: --base must be a localhost dev build (the protected dev channel)')
const deadline = Date.now() + opt.maxMinutes * 60000

const stamp = new Date().toISOString().replace(/[-:]/g, '').replace(/\..+/, 'Z')
const OUT = path.join(ROOT, 'tmp', 'ui-walk', stamp)
mkdirSync(path.join(OUT, 'shots'), { recursive: true })
// --first-client: the walked name is read from the page and never printed; every terminal line is redacted of it (files stay under OUT).
let firstName = null
// AMENDMENT 3 (c): once --first-client has set the name, the name and each whitespace- or comma-separated word of it of 3+ characters
// read `first-client` in every text that leaves the walker: a shot file name (built from the redacted label), a finding's step, a terminal line.
function redactFirst(s) {
  if (!firstName) return String(s)
  const esc = (t) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  const parts = [firstName, ...firstName.split(/[\s,]+/).filter((w) => w.length >= 3)].filter(Boolean).sort((a, b) => b.length - a.length)
  return String(s).replace(new RegExp(parts.map(esc).join('|'), 'gi'), 'first-client')
}
const log = (...m) => console.log(new Date().toISOString().slice(11, 19), ...m.map((x) => (firstName ? redactFirst(x) : x)))

// ---- account ------------------------------------------------------------------------------------------------------
const py = (cmd, extraEnv = {}, ...args) => execFileSync('python', [ACCOUNT, cmd, ...args], { encoding: 'utf8', env: { ...process.env, ...extraEnv }, stdio: ['ignore', 'pipe', 'pipe'] })

// ---- the network guard: the admitted classes ----------------------------------------------------------------------
const ADMITTED_POST = [/\/auth\/login$/, /\/auth\/refresh$/, /\/auth\/logout$/,
  /\/api\/scoped\/investor-reporting\/directory\/resolve$/, /\/api\/scoped\/investor-reporting\/selections$/]
const forcedAnswered = [] // --forced rules and how many requests each answered (written to forced.json)
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

async function shot(page, label0) {
  shotN += 1
  const label = redactFirst(label0)
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
  // HTML text in an SVG foreignObject (treemap tile labels) sits on its sibling <rect>'s fill, not on an ancestor's
  // background; reading the ancestors gave every tile label 1.18:1 against the panel behind the chart.
  const bgOf = (el) => {
    for (let e = el; e; e = e.parentElement) {
      const s = getComputedStyle(e); const l = lum(s.backgroundColor); if (l && l.a > 0.5) return { l, c: s.backgroundColor }
      if (e.tagName === 'foreignObject') { const r = [...(e.parentElement ? e.parentElement.children : [])].find((c) => c.tagName === 'rect'); const fill = r && getComputedStyle(r).fill; const lf = lum(fill); if (lf && lf.a > 0.5) return { l: lf, c: fill } }
    }
    return { l: lum('rgb(244, 246, 250)'), c: 'rgb(244, 246, 250)' }
  }
  const low = []
  for (const el of document.querySelectorAll('body *')) {
    if (!vis(el) || ![...el.childNodes].some((n) => n.nodeType === 3 && n.nodeValue.trim())) continue
    const s = getComputedStyle(el); const f = lum(s.color); if (!f) continue
    const b = bgOf(el); const ratio = (Math.max(f.L, b.l.L) + 0.05) / (Math.min(f.L, b.l.L) + 0.05)
    if (ratio < 3.0) low.push({ text: (el.innerText || '').trim().slice(0, 50), ratio: +ratio.toFixed(2), color: s.color, background: b.c, selector: trail(el) })
  }
  if (low.length) out.push({ check: 'design:contrast', observed: `${low.length} text element(s) under 3:1 contrast`, samples: low.slice(0, 12), rule: 'portal colour law: no light text on light grounds (DESIGN.md C3/C5)' })
  // 5b. text cut off SIDEWAYS by its nearest clipping ancestor, e.g. Satellite 90's "90.14%" past the Positioning
  // Summary's right edge (walk 20261003T095441Z). Not counted: an ancestor that shows a horizontal scrollbar (scrolling
  // is then visible, by design) and an ellipsis (layout:truncated covers it). Vertical clipping is a scroll area's job.
  const cut = []
  // Drawn invisibly (zero opacity up the chain, or a transparent ink): a collapsed sidebar's section titles, by design.
  const faded = (el) => { if (/rgba\([^)]*,\s*0\)$/.test(getComputedStyle(el).color)) return true; for (let e = el; e; e = e.parentElement) if (getComputedStyle(e).opacity === '0') return true; return false }
  for (const el of document.querySelectorAll('body *')) {
    if (!vis(el) || ![...el.childNodes].some((n) => n.nodeType === 3 && n.nodeValue.trim()) || faded(el)) continue
    const r = el.getBoundingClientRect()
    for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) {
      const st = getComputedStyle(a)
      if (st.overflowX === 'visible') continue
      if (st.textOverflow === 'ellipsis' || a.offsetHeight - a.clientHeight - parseFloat(st.borderTopWidth) - parseFloat(st.borderBottomWidth) > 1) break
      const b = a.getBoundingClientRect()
      const over = Math.max(b.left - r.left, r.right - b.right)
      if (over > 1 && r.right > b.left && r.left < b.right) cut.push({ text: (el.innerText || '').trim().slice(0, 30), px: Math.round(over), selector: trail(el) })
      break
    }
  }
  if (cut.length) out.push({ check: 'layout:clipped', observed: `${cut.length} text element(s) cut off sideways by their container`, samples: cut.slice(0, 12), rule: 'every label is drawn whole (no text past its panel edge)' })
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
async function checks(page, label0) {
  const label = redactFirst(label0)
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
  // expand every closed <details>, in the order orderSummaries() gives: an --open-first entry's summary first, then page order
  const closedSel = `${scopeSel} details:not([open]) > summary`
  const nSum = await page.locator(closedSel).count().catch(() => 0)
  const key = (t) => String(t || '').trim().toLowerCase()
  const entries = new Map() // normalised text -> the entry as the operator typed it
  for (const e of opt.openFirst) if (key(e) !== '' && !entries.has(key(e))) entries.set(key(e), e)
  const texts0 = entries.size ? await page.locator(closedSel).allInnerTexts().catch(() => []) : []
  for (const [k, e] of entries) if (!texts0.some((t) => key(t) === k)) log(`OPEN-FIRST "${e}": not found in ${label}`)
  const opened = new Set()
  for (let i = 0; i < Math.min(nSum, 20) && timeLeft(); i++) {
    const texts = await page.locator(closedSel).allInnerTexts().catch(() => [])
    if (!texts.length) break
    const k = orderSummaries(texts, opt.openFirst)[0]
    const txt = (texts[k] || '').trim()
    if (DO_NOT_CLICK.test(txt)) break
    const entry = entries.get(key(txt))
    // the summary is read as a handle before the click, so its <details> can be counted after the page settles
    const handle = entry !== undefined ? await page.locator(closedSel).nth(k).elementHandle().catch(() => null) : null
    await page.locator(closedSel).nth(k).click({ timeout: 3000 }).catch(() => {})
    await settle(page, 500)
    if (entry !== undefined && !opened.has(key(txt))) {
      opened.add(key(txt))
      const rows = handle ? await handle.evaluate((el) => [...(el.parentElement ? el.parentElement.querySelectorAll('tr') : [])].filter((r) => { const b = r.getBoundingClientRect(); return b.width > 0 && b.height > 0 }).length).catch(() => 0) : 0
      log(`OPEN-FIRST "${entry}": opened (${rows} table row(s) visible inside it)`)
    }
  }
  for (const [k, e] of entries) if (texts0.some((t) => key(t) === k) && !opened.has(k)) log(`OPEN-FIRST "${e}": not opened in ${label} (refused or out of time)`)
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

// ---- --firm "<label>": the header's Firm control, pressed by its visible label --------------------------------------------
// FirmDropdown.tsx mounts PageSurfaceControl as="dropdown", which renders a NATIVE <select> with one <option> per firm
// (PageSurfaceControl.tsx). Its aria-label is "Select Firm" for an internal viewer and "Firm" for a firm viewer. The option
// whose text equals the label is selected by its value; the control must then show that label, or the walk stops.
const FIRM_SELECT = 'select[aria-label="Select Firm"], select[aria-label="Firm"]'
async function selectFirm(page, label) {
  step = `firm ${label}`
  const sel = page.locator(FIRM_SELECT).first()
  await sel.waitFor({ state: 'attached', timeout: 15000 }).catch(() => {})
  const shown = (await sel.count().catch(() => 0)) ? await sel.locator('option').evaluateAll((os) => os.map((o) => (o.textContent || '').trim())).catch(() => []) : []
  if (!shown.includes(label)) throw new Error(`FIRM_OPTION_ABSENT: no Firm option reads exactly "${label}"; the Firm control shows ${shown.length ? shown.map((t) => `"${t}"`).join(', ') : 'no options (the page has no Firm control)'}`)
  const value = await sel.locator('option').evaluateAll((os, want) => { const o = os.find((x) => (x.textContent || '').trim() === want); return o ? o.value : null }, label)
  await sel.selectOption(value)
  const shownNow = await page.waitForFunction((want) => { const s = document.querySelector('select[aria-label="Select Firm"], select[aria-label="Firm"]'); const o = s && s.selectedOptions[0]; return !!o && o.textContent.trim() === want }, label, { timeout: 15000 }).then(() => true).catch(() => false)
  if (!shownNow) throw new Error(`FIRM_NOT_SHOWN: the Firm control did not show "${label}" within 15 s`)
  await settle(page, 1500)
  await checks(page, 'firm-selected')
}
// the first option the open client search lists (its own listbox, by aria-controls), polled until the search stops reading "Loading clients"
async function firstListedClient(page, combo) {
  const t0 = Date.now()
  for (;;) {
    const listId = await combo.getAttribute('aria-controls').catch(() => null)
    const got = await page.evaluate((id) => {
      const list = id ? document.getElementById(id) : null
      const first = list ? [...list.querySelectorAll('[role="option"]')].map((x) => (x.textContent || '').replace(/\s+/g, ' ').trim()).find(Boolean) : null
      return { first: first || null, busy: /Loading clients/.test(document.body.innerText || '') }
    }, listId).catch(() => ({ first: null, busy: true }))
    if (got.first && !got.busy) return got.first
    if (Date.now() - t0 >= SEARCH_ANSWER_CEILING_MS) return got.first
    await page.waitForTimeout(250)
  }
}
// --first-client, AMENDMENT 2: when the empty search lists no client, ONE letter is typed at a time, in this order, and the
// first client the first letter that lists one is walked. Only counts and the empty-state words are kept (no client name).
const FIRST_CLIENT_LETTERS = ['a', 'e', 'i', 'o', 'n', 'r', 's', 't']
async function listedOptionState(page, combo) {
  const listId = await combo.getAttribute('aria-controls').catch(() => null)
  return page.evaluate((id) => {
    const list = id ? document.getElementById(id) : null
    const count = list ? list.querySelectorAll('[role="option"]').length : 0
    const words = list ? (list.innerText || '') : ((document.body.innerText || '').match(/\b(?:no|none)\b[^\n.]{0,60}/i) || [''])[0]
    return { count, empty: count === 0 ? String(words).replace(/\s+/g, ' ').trim().slice(0, 160) : null }
  }, listId).catch(() => ({ count: null, empty: null }))
}
async function clearSearchBox(combo) {
  await combo.click().catch(() => {})
  await combo.press('Control+A').catch(() => {})
  await combo.press('Backspace').catch(() => {})
  await combo.fill('').catch(() => {})
}

// ---- FWD-1: one company picked BY ITS NAME, then the thread hop by hop ----------------------------------------------
// The name is found by its price bar's row, on Trending x Price. Never by
// ticker and never through the ticker search box. A name no row prints is a measured finding and the thread stops.
async function walkThread(page, route, name) {
  step = `thread ${name}`
  await page.goto(opt.base + route, { waitUntil: 'domcontentloaded', timeout: 30000 })
  await settle(page, 2500)
  await amgtLeadState(page, 'Price')
  await waitPriceBars(page) // the bars arrive after the face; the lead-list step already waits for them, the thread did not
  const rows = page.locator('[data-price-bar]')
  // The row is an <li> holding the bar on older builds; on the redesigned page the [data-price-bar] element is the row itself (the same
  // fallback readPriceBars uses), so match the <li> first and the bar element second.
  const liRow = page.locator('li:has([data-price-bar])').filter({ hasText: name }).first()
  const lead = (await liRow.count().catch(() => 0)) ? liRow : page.locator('[data-price-bar]').filter({ hasText: name }).first()
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
  // the header's key figures come from /overlay, which can answer after the flat settle; wait for the loaded state as the
  // --security path does, so the header shot shows the figures and not the skeleton
  const threadWait = await waitForLoaded(page)
  loadStates.push({ security: name, step: 'thread-header', state: threadWait.state, waited_ms: threadWait.waited_ms })
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
  // close the day dialog this step opened, so the next press and every later shot are not taken under it
  await page.keyboard.press('Escape').catch(() => {})
  await page.waitForTimeout(400)
  const dlgOpen = await page.locator('[role="dialog"]:visible').count().catch(() => 0)
  if (dlgOpen) {
    await page.locator('[role="dialog"] [aria-label="Close"], [role="dialog"] button:has-text("Close")').first().click({ timeout: 2000, force: true }).catch(() => {})
    await page.waitForTimeout(400)
  }
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
    // close the day dialog this step opened, so the next press and every later shot are not taken under it
    await page.keyboard.press('Escape').catch(() => {})
    await page.waitForTimeout(400)
    const dlgOpen = await page.locator('[role="dialog"]:visible').count().catch(() => 0)
    if (dlgOpen) {
      await page.locator('[role="dialog"] [aria-label="Close"], [role="dialog"] button:has-text("Close")').first().click({ timeout: 2000, force: true }).catch(() => {})
      await page.waitForTimeout(400)
    }
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

const windowPressRecords = []
async function windowPresses(page, sec) {
  step = `amgt ${sec} thesis window`
  const card = page.locator('[data-thesis-card="investment_thesis"]').first()
  if (!(await card.count().catch(() => 0))) { findings.push({ step, check: 'walker:press-not-found', claim: 'measured', observed: 'Investment-thesis card not found' }); return }
  await card.click({ timeout: 4000 }).catch(() => {})
  await settle(page, 1500)
  await checks(page, `${sec}-Thesis-window`)
  let k = 0
  for (const css of opt.windowPresses) {
    k += 1
    const hit = page.locator('[role="dialog"]').locator(css).locator('visible=true').first()
    if (!(await hit.count().catch(() => 0))) { findings.push({ step, check: 'walker:press-not-found', claim: 'measured', observed: `--window-press ${css}: no visible match in the dialog` }); windowPressRecords.push({ security: sec, css, pressed: false, focused: null, focused_in_view: null }); continue }
    const txt = ((await hit.innerText().catch(() => '')) || '').replace(/\s+/g, ' ').trim()
    if (DO_NOT_CLICK.test(txt)) { findings.push({ step, check: 'walker:press-refused', claim: 'measured', observed: `--window-press ${css}: text "${txt.slice(0, 60)}" names a write word; not pressed` }); windowPressRecords.push({ security: sec, css, pressed: false, focused: null, focused_in_view: null }); continue }
    const pressed = await hit.click({ timeout: 4000 }).then(() => true).catch(() => false)
    await page.waitForTimeout(1500)
    const f = await page.evaluate(() => {
      const e = document.activeElement
      if (!e) return { tag: null, id: null, data_thesis_passage: null, in_view: false }
      const r = e.getBoundingClientRect()
      return { tag: e.tagName, id: e.id || null, data_thesis_passage: e.getAttribute('data-thesis-passage'), in_view: r.top >= 0 && r.top < window.innerHeight }
    }).catch(() => ({ tag: null, id: null, data_thesis_passage: null, in_view: false }))
    await checks(page, `${sec}-Thesis-window-press-${k}`)
    await page.keyboard.press('Escape').catch(() => {})
    windowPressRecords.push({ security: sec, css, pressed, focused: { tag: f.tag, id: f.id, data_thesis_passage: f.data_thesis_passage }, focused_in_view: f.in_view })
  }
}

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
    let pk = 0
    for (const css of opt.securityPresses || []) {
      pk += 1
      step = `amgt ${sec} security-press ${pk}`
      const hit = page.locator(css).locator('visible=true').first()
      if (!(await hit.count().catch(() => 0))) { findings.push({ step, check: 'walker:press-not-found', claim: 'measured', observed: `--security-press ${css}: no visible match` }); continue }
      const txt = ((await hit.innerText().catch(() => '')) || '').replace(/\s+/g, ' ').trim()
      if (DO_NOT_CLICK.test(txt)) { findings.push({ step, check: 'walker:press-refused', claim: 'measured', observed: `--security-press ${css}: text "${txt.slice(0, 60)}" names a write word; not pressed` }); continue }
      await hit.click({ timeout: 4000 }).catch(() => {})
      await settle(page, 2500)
      await waitForLoaded(page)
      await checks(page, `${sec}-press-${pk}`)
    }
    // --forced-press: only the two header buttons named here; the forced rules make their request fail, so nothing is generated.
    let fp = 0
    for (const label of opt.forcedPresses || []) {
      fp += 1
      step = `amgt ${sec} forced-press ${fp}`
      if (!['Export as a document', 'Print'].includes(label)) { findings.push({ step, check: 'walker:press-refused', claim: 'measured', observed: `--forced-press "${label}" is not one of the two allowed buttons; not pressed` }); continue }
      if (!opt.forced) { findings.push({ step, check: 'walker:press-refused', claim: 'measured', observed: `--forced-press "${label}" needs --forced (a rule that fails its request); not pressed` }); continue }
      const btn = page.getByRole('button', { name: label, exact: true }).first()
      if (!(await btn.count().catch(() => 0))) { findings.push({ step, check: 'walker:press-not-found', claim: 'measured', observed: `--forced-press "${label}": no button` }); continue }
      await btn.click({ timeout: 4000 }).catch(() => {})
      await settle(page, 4000)
      await checks(page, `${sec}-forced-press-${fp}`)
      // The print preview closes on a backdrop click (Escape does not); a press with no modal open clicks the page corner harmlessly.
      await page.mouse.click(5, 5).catch(() => {})
      await page.waitForTimeout(500)
    }
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
      if (tab === 'Thesis' && (opt.windowPresses || []).length) await windowPresses(page, sec)
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
// ---- --map-tiles: the Securities map's tile count against the served snapshot (DSGN_IRPTV1 item 85, CTO batch 178) ----
// Every holdings answer the walk receives is reduced to its count of distinct map-eligible securities: SECURITY or CASH
// nodes with a served of_total and a non-zero amount, one per security_id (else per node id) -- the page's own map rule
// (treemapLeavesFrom). The step reads the tile rects drawn in [data-slot="treemap-chart"] on the tab's default view and
// compares them with the answer that view shows: the one with the most distinct securities (the all-accounts selection;
// the tab's background one-account reads are subsets). Counts only; no name and no figure of any client is written.
const mapTileAnswers = new Map()
// ---- --contrast-table: interactive (ground, ink) pairs by state (DSGN_REBRND round 3 E4, FWD-13) ---------------------
// The ground is the nearest ancestor background with alpha > 0.5, the same reading as the design:contrast check (a
// translucent layer is skipped, so a page with translucent fills reads its rung under them). The bar is 4.5:1, or 3:1
// for large text (>= 24 px, or >= 18.66 px at weight 700+). Labels are the controls' own words (page copy).
const contrastRows = []
const CONTRAST_CAP = 80
async function contrastTable(page, label) {
  const measure = (el) => {
    // Any CSS colour (rgb, oklab, color-mix ...) is read through a 1x1 canvas, so the parser never decides a pair.
    const cv = document.createElement('canvas'); cv.width = 1; cv.height = 1
    const cx = cv.getContext('2d', { willReadFrequently: true })
    const rgba = (c) => { cx.clearRect(0, 0, 1, 1); cx.fillStyle = 'rgba(0,0,0,0)'; cx.fillStyle = c; cx.fillRect(0, 0, 1, 1); const d = cx.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2], d[3] / 255] }
    const lin = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4) }
    const L = ([r, g, b]) => 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
    const groundOf = (node) => { for (let e = node; e; e = e.parentElement) { const c = rgba(getComputedStyle(e).backgroundColor); if (c[3] > 0.5) return c } return [244, 246, 250, 1] }
    // The pair is the TEXT the control shows: every element inside it (itself included) that holds visible text,
    // its ink composited over its own ground by the ink's alpha. The control reports its weakest text.
    const holders = [el, ...el.querySelectorAll('*')].filter((n) => [...n.childNodes].some((t) => t.nodeType === 3 && t.nodeValue.trim()) && n.getClientRects().length)
    let worst = null
    for (const h of holders.length ? holders : [el]) {
      const s = getComputedStyle(h); const g = groundOf(h); const k = rgba(s.color)
      const ink = [0, 1, 2].map((i) => Math.round(k[3] * k[i] + (1 - k[3]) * g[i]))
      const a = L(ink); const b = L(g)
      const ratio = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05)
      const px = parseFloat(s.fontSize); const large = px >= 24 || (px >= 18.66 && Number(s.fontWeight) >= 700)
      const bar = large ? 3 : 4.5
      if (!worst || ratio / bar < worst.ratio / worst.bar) worst = { ink: `rgb(${ink.join(', ')})`, ground: `rgb(${g.slice(0, 3).join(', ')})`, ratio: +ratio.toFixed(2), bar }
    }
    const selected = ['aria-pressed', 'aria-selected', 'aria-current'].some((x) => { const v = el.getAttribute(x); return v && v !== 'false' })
    return { label: (el.getAttribute('aria-label') || el.innerText || el.value || '').trim().replace(/\s+/g, ' ').slice(0, 40), tag: el.tagName.toLowerCase(), ...worst, selected, disabled: el.disabled === true }
  }
  const controls = page.locator('button:visible, a[href]:visible, [role=tab]:visible, [role=button]:visible, input:not([type=hidden]):visible, select:visible')
  const n = Math.min(await controls.count().catch(() => 0), CONTRAST_CAP)
  for (let i = 0; i < n; i++) {
    const el = controls.nth(i)
    const rest = await el.evaluate(measure).catch(() => null)
    if (!rest || !rest.label) continue
    contrastRows.push({ step: label, state: rest.selected ? 'selected' : 'rest', ...rest, pass: rest.ratio !== null && rest.ratio >= rest.bar })
    if (rest.disabled) continue
    await el.hover({ timeout: 1500 }).catch(() => {})
    await page.waitForTimeout(150)
    const hover = await el.evaluate(measure).catch(() => null)
    if (hover) contrastRows.push({ step: label, state: 'hover', ...hover, pass: hover.ratio !== null && hover.ratio >= hover.bar })
  }
  await page.mouse.move(2, 2).catch(() => {})
  // NON-INTERACTIVE TEXT at rest (DSGN_REBRND row S10: the Positioning Summary's class labels read 4.07:1 and no limb
  // saw them). Every visible element holding its own text outside a control, read as above and grouped by
  // (ink, ground, bar) with a count. The row's label is a hint -- tag, data-* attribute NAMES, the data-slot value --
  // never the text, so no client word or figure is written.
  const textRows = await page.evaluate(() => {
    const cv = document.createElement('canvas'); cv.width = 1; cv.height = 1
    const cx = cv.getContext('2d', { willReadFrequently: true })
    const rgba = (c) => { cx.clearRect(0, 0, 1, 1); cx.fillStyle = 'rgba(0,0,0,0)'; cx.fillStyle = c; cx.fillRect(0, 0, 1, 1); const d = cx.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2], d[3] / 255] }
    const lin = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4) }
    const L = ([r, g, b]) => 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
    // HTML text inside an SVG foreignObject (the treemap's tile labels) sits on the tile's <rect> fill, a sibling, not an
    // ancestor: walking up from the label would read the panel behind the chart (row S12's probe: 46 labels at 1.18:1).
    const groundElOf = (node) => {
      for (let e = node; e; e = e.parentElement) {
        if (rgba(getComputedStyle(e).backgroundColor)[3] > 0.5) return e
        if (e.tagName === 'foreignObject') { const r = [...(e.parentElement ? e.parentElement.children : [])].find((c) => c.tagName === 'rect'); if (r && rgba(getComputedStyle(r).fill)[3] > 0.5) return r }
      }
      return null
    }
    const groundOf = (node) => { const e = groundElOf(node); return e ? rgba(e.tagName === 'rect' ? getComputedStyle(e).fill : getComputedStyle(e).backgroundColor) : [244, 246, 250, 1] }
    const CONTROL = 'button, a[href], [role=tab], [role=button], input, select, textarea, option'
    // Where a group sits, in code vocabulary only: tag plus its first four class names.
    const cls = (e) => (e ? `${e.tagName.toLowerCase()}${typeof e.className === 'string' && e.className.trim() ? `.${e.className.trim().split(/\s+/).slice(0, 4).join('.')}` : ''}` : 'none')
    // Text a person cannot see is not graded: clipped to nothing by an ancestor whose overflow is not visible (a
    // collapsed panel), or drawn at zero opacity anywhere up the chain.
    const unseen = (node) => {
      let r = node.getBoundingClientRect()
      for (let e = node.parentElement; e && e !== document.body; e = e.parentElement) {
        const st = getComputedStyle(e)
        if (Number(st.opacity) === 0) return true
        if (st.overflowX !== 'visible' || st.overflowY !== 'visible') {
          const b = e.getBoundingClientRect()
          r = { left: Math.max(r.left, b.left), right: Math.min(r.right, b.right), top: Math.max(r.top, b.top), bottom: Math.min(r.bottom, b.bottom) }
          if (r.right - r.left < 1 || r.bottom - r.top < 1) return true
        }
      }
      return false
    }
    const groups = new Map()
    let skippedUnseen = 0
    for (const h of document.body.querySelectorAll('*')) {
      if (['SCRIPT', 'STYLE', 'NOSCRIPT', 'TITLE'].includes(h.tagName) || h.closest(CONTROL)) continue
      if (![...h.childNodes].some((t) => t.nodeType === 3 && t.nodeValue.trim()) || !h.getClientRects().length) continue
      const s = getComputedStyle(h)
      if (s.visibility === 'hidden' || Number(s.opacity) === 0) continue
      if (unseen(h)) { skippedUnseen++; continue }
      const g = groundOf(h); const k = rgba(s.color)
      const ink = [0, 1, 2].map((i) => Math.round(k[3] * k[i] + (1 - k[3]) * g[i]))
      const a = L(ink); const b = L(g)
      const ratio = +((Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05)).toFixed(2)
      const px = parseFloat(s.fontSize); const bar = px >= 24 || (px >= 18.66 && Number(s.fontWeight) >= 700) ? 3 : 4.5
      const key = `${ink}|${g.slice(0, 3)}|${bar}`
      const hit = groups.get(key)
      if (hit) { hit.count++; continue }
      const names = [...h.attributes].map((x) => x.name).filter((n) => n.startsWith('data-') && n !== 'data-slot')
      const slot = h.getAttribute('data-slot')
      const hint = `${h.tagName.toLowerCase()}${slot ? `[data-slot=${slot}]` : ''}${names.length ? `[${names.join(',')}]` : ''} ${px}px/${s.fontWeight}`
      groups.set(key, { label: hint, tag: h.tagName.toLowerCase(), ink: `rgb(${ink.join(', ')})`, ground: `rgb(${g.slice(0, 3).join(', ')})`, ratio, bar, count: 1,
        where: `${cls(h.parentElement)} > ${cls(h)}`, ground_from: cls(groundElOf(h)) })
    }
    return { rows: [...groups.values()], skippedUnseen }
  }).catch(() => ({ rows: [], skippedUnseen: null }))
  for (const r of textRows.rows) contrastRows.push({ step: label, state: 'text', ...r, selected: false, disabled: false, pass: r.ratio >= r.bar })
  const failing = contrastRows.filter((r) => r.step === label && !r.pass)
  log('CONTRAST TABLE', label, `${contrastRows.filter((r) => r.step === label).length} pairs (${textRows.rows.length} non-interactive text groups; ${textRows.skippedUnseen} clipped or transparent text elements not graded), ${failing.length} under their bar`)
}
const mapTiles = []
function readMapTileAnswer(p, j) {
  const d = j && j.data
  if (!d || !Array.isArray(d.nodes)) return
  const ids = new Set()
  for (const n of d.nodes) {
    if (n.node_kind !== 'SECURITY' && n.node_kind !== 'CASH') continue
    const pct = n.percentages ? n.percentages.of_total : null
    const amount = n.amount ? n.amount.value : null
    if (pct === null || pct === undefined || amount === 0) continue
    ids.add(n.security_id ? `${n.security_id.namespace}:${n.security_id.value}` : `node:${n.node_id}`)
  }
  mapTileAnswers.set(p, { selection: p.split('/').pop().slice(0, 16), distinct_securities: ids.size })
}
async function mapTilesStep(page, label) {
  await page.locator('[data-slot="treemap-chart"]').first().scrollIntoViewIfNeeded().catch(() => {})
  await page.waitForTimeout(1500)
  const drawn = await page.evaluate(() => {
    const root = document.querySelector('[data-slot="treemap-chart"]')
    const rects = root ? [...root.querySelectorAll('svg g > rect')] : []
    return { tiles: rects.length, small_tiles: rects.filter((r) => r.getAttribute('data-small-tile') === 'true').length,
      grouped_words: /Other Securities|Smaller Holdings/.test(document.body.innerText) }
  })
  const answers = [...mapTileAnswers.values()].sort((a, b) => b.distinct_securities - a.distinct_securities)
  const shown = answers[0] || null
  mapTiles.push({ label, ...drawn, served_distinct_securities: shown ? shown.distinct_securities : null,
    equal: shown ? shown.distinct_securities === drawn.tiles : null, holdings_answers_read: answers.length })
  await shot(page, `${label}-map-tiles`)
}
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
    if (opt.cardCensus) row.served_shape = sectionsShape(json.data)
  }
  requestHops.rows.push(row)
}
// --card-census: the served sections answer's shape. Key names and short category tokens only; a token longer than 40
// characters or not a string is counted under its type, never written.
function sectionsShape(data) {
  const tok = (v) => (typeof v === 'string' && v.length <= 40 ? v : `<${v === null ? 'null' : typeof v}>`)
  const bump = (acc, k) => { acc[k] = (acc[k] || 0) + 1; return acc }
  const sections = Array.isArray(data.sections) ? data.sections : []
  const keySets = sections.map((s) => (s && typeof s === 'object' ? Object.keys(s).sort().join(',') : '<not-object>'))
  const shape = {
    data_keys: Object.keys(data),
    section_keys_first: sections[0] && typeof sections[0] === 'object' ? Object.keys(sections[0]) : null,
    section_key_sets: keySets.reduce(bump, {}),
    section_type: {}, units: {}, units_found_at: {}, nested_value_keys: {}, validation_keys: {},
  }
  for (const s of sections) {
    if (!s || typeof s !== 'object') continue
    if ('section_type' in s) bump(shape.section_type, tok(s.section_type))
    if ('units' in s) { bump(shape.units, tok(s.units)); bump(shape.units_found_at, 'section.units') }
    for (const [k, v] of Object.entries(s)) {
      if (!Array.isArray(v) || !v.length || typeof v[0] !== 'object' || v[0] === null) continue
      bump(shape.nested_value_keys, `${k}: ${Object.keys(v[0]).join(',')}`)
      for (const item of v) if (item && typeof item === 'object' && 'units' in item) { bump(shape.units, tok(item.units)); bump(shape.units_found_at, `section.${k}[].units`) }
    }
  }
  for (const [k, v] of Object.entries(data)) if (/validation/i.test(k) && v && typeof v === 'object') shape.validation_keys[k] = Object.keys(v)
  return shape
}
async function openRequest(page, label, requestId, afterReload = false) {
  const rows = page.locator('[data-row="owned-analysis-request"]')
  for (let w = 0; w < 40 && !(await rows.count().catch(() => 0)); w++) await page.waitForTimeout(500)
  const listed = await page.evaluate(() => [...document.querySelectorAll('[data-row="owned-analysis-request"]')].map((r) => ({
    id: r.getAttribute('data-request-id'), state: (r.querySelector('[data-slot="owned-request-state"]') || {}).textContent || null })))
  let target = listed.find((r) => r.id === requestId)
  const byId = Boolean(target)
  if (!target) target = listed.find((r) => /^Ready\b/.test(r.state || ''))
  // position_in_list: the asked request's 1-based place in the list as the page draws it (null when not listed).
  const position = listed.findIndex((r) => r.id === requestId)
  const rec = { label, asked: requestId, listed: listed.length, listed_ready: listed.filter((r) => /^Ready\b/.test(r.state || '')).length, opened: target ? target.id : null, opened_by_id: byId, position_in_list: position < 0 ? null : position + 1, row_state: target ? target.state : null }
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
  if (opt.cardCensus) {
    rec.card_census = await page.evaluate(() => {
      const d = document.querySelector('[data-slot="owned-request-detail"]')
      if (!d) return null
      const bump = (acc, k) => { acc[k] = (acc[k] || 0) + 1; return acc }
      const inClosed = (el) => { for (let p = el.parentElement; p && p !== d; p = p.parentElement) if (p.tagName === 'DETAILS' && !p.open) return true; return false }
      const CODE = /^S\d{2,3}$/
      const out = { cards: 0, title_name: 0, title_code: 0, codes_still_printed: {}, units: {}, unit_unknown: 0, label_column_shown: 0, title_label_groups: {} }
      for (const card of d.querySelectorAll('[data-row="native-section"]')) {
        out.cards++
        const title = ((card.querySelector('span') || {}).textContent || '').replace(/^\s*\d+\.\s*/, '').trim()
        if (CODE.test(title)) { out.title_code++; bump(out.codes_still_printed, title) } else out.title_name++
        const heads = [...card.querySelectorAll('thead th')].map((th) => th.textContent.trim())
        const li = heads.indexOf('Label'), ui = heads.indexOf('Unit')
        if (li >= 0) out.label_column_shown++
        for (const tr of card.querySelectorAll('[data-row="native-section-value"]')) {
          const tds = tr.querySelectorAll('td')
          const unit = ui >= 0 && tds[ui] ? tds[ui].textContent.trim() : '<no unit column>'
          bump(out.units, unit)
          if (/^unknown$/i.test(unit)) out.unit_unknown++
          const lab = li >= 0 && tds[li] ? (tds[li].textContent.trim() || title) : title
          bump(out.title_label_groups, `${title} | ${lab}`)
        }
      }
      const groups = Object.values(out.title_label_groups)
      out.groups_total = groups.length
      out.groups_shared = groups.filter((n) => n > 1).length
      out.largest_group = groups.length ? Math.max(...groups) : 0
      out.largest_group_key = Object.keys(out.title_label_groups).find((k) => out.title_label_groups[k] === out.largest_group) || null
      // Rows sharing ONE title and ONE Label, so they cannot be told apart. The group keys are the page's own labels.
      const v = d.querySelector('[data-slot="extraction-validation"], [data-slot="computation-validation"]')
      out.validation_line = v ? { present: true, on_face: !inClosed(v) && v.getClientRects().length > 0 } : { present: false, on_face: false }
      const srcEls = [...d.querySelectorAll('*')].filter((el) => el.children.length === 0 && /\bSource\b/.test(el.textContent || ''))
      out.source_line = { elements: srcEls.length, on_face: srcEls.filter((el) => !inClosed(el)).length, inside_closed_details: srcEls.filter(inClosed).length }
      out.closed_details = d.querySelectorAll('details:not([open])').length
      out.validation_inside_closed_details = v ? inClosed(v) : null
      return out
    }).catch((e) => ({ error: String(e).slice(0, 200) }))
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
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, ...(opt.tz ? { timezoneId: opt.tz } : {}) })
  if (opt.tz) log('TIMEZONE', opt.tz)
  const page = await context.newPage()
  let lastAuthorization = null
  let lastScopedHeaders = null
  page.on('console', (m) => { if (m.type() === 'error') consoleErrors.push({ step, text: m.text().slice(0, 300) }) })
  page.on('pageerror', (e) => consoleErrors.push({ step, text: 'PAGE ERROR: ' + String(e).slice(0, 300) }))
  page.on('request', noteHopRequest)
  page.on('request', (req) => {
    const h = req.headers(); const p = pathOnly(req.url())
    if (h.authorization && /\/api\//.test(p)) { lastAuthorization = h.authorization; if (/\/api\/scoped\//.test(p)) lastScopedHeaders = h }
  })
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
      if (opt.mapTiles && /\/investor-reporting\/holdings\//.test(p)) readMapTileAnswer(p, j)
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
  // --forced: registered AFTER the guard so it answers first; GET only, everything else falls back to the guard.
  if (opt.forced) {
    const rules = JSON.parse(readFileSync(opt.forced, 'utf8'))
    const dotted = (o, pathStr, fn) => { const ks = pathStr.split('.'); let cur = o; for (let i = 0; i < ks.length - 1; i += 1) { if (cur == null || typeof cur !== 'object') return false; cur = cur[ks[i]] } if (cur == null || typeof cur !== 'object') return false; fn(cur, ks[ks.length - 1]); return true }
    for (const rule of rules) {
      const rx = new RegExp(rule.match)
      const rec = { label: rule.label, match: rule.match, mode: rule.mode, answered: 0, patched_paths: [], status: rule.status ?? null }
      forcedAnswered.push(rec)
      await page.route(rx, async (route) => {
        if (route.request().method() !== 'GET') return route.fallback()
        rec.answered += 1
        if (rule.mode === 'abort') return route.abort('failed')
        if (rule.mode === 'status') return route.fulfill({ status: rule.status || 500, contentType: 'application/json', body: JSON.stringify({ error: 'forced by the walker' }) })
        if (rule.mode === 'patch') {
          const real = await route.fetch()
          let j
          try { j = await real.json() } catch { return route.fulfill({ response: real }) }
          rec.body_keys = Object.keys(j).slice(0, 40) // key NAMES only, so a rule's paths can be written against the real envelope
          if (j && typeof j.data === 'object' && j.data) rec.data_keys = Object.keys(j.data).slice(0, 40)
          // A path is tried on the body as served, then under `data.` (an enveloped answer); the paths that took are recorded.
          // `$KEY` inside a `set` value is replaced by the answer's own security_key (a cite is "<security_key>/<element>").
          const keyed = (v) => JSON.parse(JSON.stringify(v).split('$KEY').join(String(j.security_key ?? '')))
          for (const [k, v0] of Object.entries(rule.set || {})) {
            const v = keyed(v0)
            if (dotted(j, k, (o, key) => { o[key] = v })) rec.patched_paths.push('set ' + k)
            else if (dotted(j, 'data.' + k, (o, key) => { o[key] = v })) rec.patched_paths.push('set data.' + k)
          }
          for (const k of rule.delete || []) {
            if (dotted(j, k, (o, key) => { delete o[key] })) rec.patched_paths.push('delete ' + k)
            else if (dotted(j, 'data.' + k, (o, key) => { delete o[key] })) rec.patched_paths.push('delete data.' + k)
          }
          return route.fulfill({ response: real, json: j })
        }
        return route.fallback()
      })
    }
  }

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

  if (opt.probeGets?.length) {
    step = 'probe-get'
    // Same-origin paths need the page on the base (a --no-login run is still on about:blank).
    if (!page.url().startsWith(opt.base)) await page.goto(opt.base + '/', { waitUntil: 'domcontentloaded', timeout: 30000 }).catch(() => {})
    // The headers the page itself sends on its scoped reads (Authorization among them), replayed as sent; held in this
    // process only. Only their NAMES are printed and written. A non-2xx answer keeps its first 200 characters (an
    // error text); a 2xx answer keeps only its byte count, never its body.
    const waitAuth = Date.now() + 20000
    while (!(lastScopedHeaders || lastAuthorization) && Date.now() < waitAuth) await page.waitForTimeout(250)
    const SKIP = /^(host|connection|content-length|accept-encoding|cookie|origin|referer|user-agent|sec-|:)/i
    const sent = Object.fromEntries(Object.entries(lastScopedHeaders || (lastAuthorization ? { authorization: lastAuthorization } : {})).filter(([k]) => !SKIP.test(k)))
    const probes = []
    for (const p of opt.probeGets) {
      const answer = (headers) => page.evaluate(async ({ url, headers }) => {
        try {
          const r = await fetch(url, { method: 'GET', headers, cache: 'no-store' }); const t = await r.text()
          return { status: r.status, bytes: t.length, error_text: r.status >= 300 ? t.slice(0, 200) : null }
        } catch (e) { return { status: `fetch failed: ${String(e).slice(0, 80)}`, bytes: null, error_text: null } }
      }, { url: p, headers })
      const withHeaders = await answer(sent)
      const control = await answer({})
      const row = { path: p, status: withHeaders.status, bytes: withHeaders.bytes, error_text: withHeaders.error_text, header_names_sent: Object.keys(sent).sort(),
        control_status_without_headers: control.status, at: new Date().toISOString() }
      probes.push(row)
      log('PROBE GET', p, '->', row.status, `(${row.bytes} bytes; headers sent: ${row.header_names_sent.join(',') || 'none'}; control without them: ${row.control_status_without_headers})${row.error_text ? ' error: ' + row.error_text : ''}`)
    }
    writeFileSync(path.join(OUT, 'probe-get.json'), JSON.stringify({ base: opt.base, probes }, null, 1))
  }

  for (const route of opt.routes) {
    if (!timeLeft()) break
    step = `route ${route}`
    await page.goto(opt.base + route, { waitUntil: 'domcontentloaded', timeout: 30000 })
    await settle(page, 2500)
    await checks(page, `${route}-load`)
    if (route.startsWith('/investor-reporting')) {
      // --firm: the header's Firm option is pressed by its visible label before the client search
      if (opt.firm) await selectFirm(page, opt.firm)
      // the client search: the empty-query state, then each client
      const combo = page.getByRole('combobox', { name: 'Client search' })
      if (await combo.count().catch(() => 0)) {
        step = 'search-empty'
        await combo.click().catch(() => {})
        await page.waitForTimeout(1200)
        await checks(page, 'search-open-empty')
        // --first-client: the first client the empty search lists is walked as a named one; its name stays out of the terminal
        let walkList = opt.clients
        if (opt.firstClient && !opt.clients.length) {
          let first = await firstListedClient(page, combo)
          if (!first) {
            // AMENDMENT 2: the empty search listed no client; type one letter in turn and take the first client a letter lists
            const emptySt = await listedOptionState(page, combo)
            const perLetter = [{ letter: '(empty)', options: emptySt.count, empty_text: emptySt.empty }]
            log(`FIRST-CLIENT empty search: ${perLetter[0].options} option(s) listed`)
            for (const letter of FIRST_CLIENT_LETTERS) {
              if (!timeLeft()) break
              step = `first-client letter ${letter}`
              await clearSearchBox(combo)
              await combo.pressSequentially(letter, { delay: 40 }).catch(() => {})
              first = await firstListedClient(page, combo)
              const st = await listedOptionState(page, combo)
              perLetter.push({ letter, options: st.count, empty_text: first ? null : st.empty })
              log(`FIRST-CLIENT letter "${letter}": ${st.count} option(s) listed`)
              if (first) break
            }
            if (first) { firstName = first; walkList = [first] }
            else findings.push({ step: 'first-client', check: 'walker:first-client-absent', claim: 'measured', observed: `the empty client search listed no client to walk; one letter at a time listed: ${perLetter.map((p) => `${p.letter}=${p.options}`).join(', ')}`, letters: perLetter, rule: '--first-client walks the first listed client' })
          } else { firstName = first; walkList = [first] }
        }
        for (const client of walkList) {
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
              if (opt.mapTiles) {
                await mapTilesStep(page, `${client}-holdings`)
                log('MAP TILES', JSON.stringify(mapTiles[mapTiles.length - 1]).slice(0, 600))
              }
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
        if (!opt.clients.length && !firstName) log('NOTE: no --client given; only the page load and the empty search were walked')
      }
    } else if (route.startsWith('/security-analysis')) {
      await walkSecurityAnalysis(page, route)
    } else {
      // --hover <css>: hover each of the first 3 matches BEFORE any press or the generic explore (which click), a viewport
      // shot + the checks each -- a hover-only popup (role=tooltip, portal-rendered or not) is graded for occlusion
      for (const sel of opt.hovers) {
        const els = page.locator(sel)
        const n = Math.min(await els.count().catch(() => 0), 3)
        if (!n) findings.push({ step, check: 'hover:no-match', claim: 'measured', observed: `no element matches ${sel}` })
        for (let i = 0; i < n && timeLeft(); i++) {
          await els.nth(i).hover({ timeout: 3000 }).catch(() => {})
          await settle(page, 500)
          await page.screenshot({ path: path.join(OUT, `shots/hover-${i + 1}-viewport.png`) }).catch(() => {})
          await checks(page, `${route}-hover-${i + 1}`)
          await page.mouse.move(0, 0).catch(() => {})
          await settle(page, 250)
        }
      }
      for (const label of opt.presses || []) {
        if (DO_NOT_CLICK.test(label)) { findings.push({ step: `press ${label}`, check: 'walker:press-refused', claim: 'measured', observed: `--press "${label}" names a write word; not pressed` }); continue }
        const pressed = await clickLabel(page, label)
        await page.waitForTimeout(PRESS_SETTLE_MS)
        await settle(page, 2500)
        log('PRESS', label, pressed ? 'pressed' : 'NOT FOUND')
        await checks(page, `${route}-press-${label}`)
        if (opt.contrastTable) await contrastTable(page, `${route}-press-${label}`)
      }
      // --hover-after-press: the presses above set the page state; now hover into it (a chart tooltip follows the pointer,
      // so the move is stepped). One viewport shot + checks per spec; a missing target is hover:no-match, never a silent skip.
      for (const [k, h] of (opt.hoverAfterPress || []).entries()) {
        if (!timeLeft()) break
        const el = page.locator(h.css).first()
        if (!(await el.count().catch(() => 0))) { findings.push({ step, check: 'hover:no-match', claim: 'measured', observed: `--hover-after-press: no element matches ${h.css}` }); continue }
        await el.scrollIntoViewIfNeeded({ timeout: 3000 }).catch(() => {})
        const b = await el.boundingBox().catch(() => null)
        if (!b || !b.width || !b.height) { findings.push({ step, check: 'hover:no-match', claim: 'measured', observed: `--hover-after-press: ${h.css} has no visible box` }); continue }
        const x = b.x + b.width * h.frac; const y = b.y + b.height / 2
        await page.mouse.move(x, y, { steps: 8 }).catch(() => {})
        await settle(page, 600)
        const file = `shots/hover-after-press-${k + 1}-viewport.png`
        await page.screenshot({ path: path.join(OUT, file) }).catch(() => {})
        log('HOVER-AFTER-PRESS', h.css, `@${h.frac}`, `(${Math.round(x)},${Math.round(y)})`, '->', file)
        await checks(page, `${route}-hover-after-press-${k + 1}`)
        await page.mouse.move(0, 0).catch(() => {})
        await settle(page, 250)
      }
      if (opt.contrastTable && !(opt.presses || []).length) await contrastTable(page, `${route}-load`)
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
  if (opt.forced) writeFileSync(path.join(OUT, 'forced.json'), JSON.stringify({ rules_file: opt.forced, rules: forcedAnswered, note: 'FORCED reads: the build, the login and the page code are real; the named answers were forced or patched' }, null, 1))
  if (opt.forced) log('FORCED RULES:', forcedAnswered.map((r) => `${r.label}=${r.answered} answered${r.patched_paths.length ? ' (' + r.patched_paths.join(',') + ')' : ''}`).join('; '))
  if (windowPressRecords.length) writeFileSync(path.join(OUT, 'window-press.json'), JSON.stringify(windowPressRecords, null, 1))
  if (loadStates.length) writeFileSync(path.join(OUT, 'load-states.json'), JSON.stringify(loadStates, null, 1))
  if (timelineDays.length) writeFileSync(path.join(OUT, 'timeline-days.json'), JSON.stringify(timelineDays, null, 1))
  if (modelScopes.length) writeFileSync(path.join(OUT, 'model-scope.json'), JSON.stringify(modelScopes, null, 1))
  if (accountDrills.length) writeFileSync(path.join(OUT, 'account-drill.json'), JSON.stringify(accountDrills, null, 1))
  if (composerPickers.length) writeFileSync(path.join(OUT, 'composer-picker.json'), JSON.stringify(composerPickers, null, 1))
  if (dashboardWindows.length) writeFileSync(path.join(OUT, 'dashboard-window.json'), JSON.stringify(dashboardWindows, null, 1))
  if (searchTimings.length) writeFileSync(path.join(OUT, 'search-timings.json'), JSON.stringify(searchTimings, null, 1))
  if (openedRequests.length) writeFileSync(path.join(OUT, 'analysis-request.json'), JSON.stringify(openedRequests, null, 1))
  if (holdingsAggregates.length) writeFileSync(path.join(OUT, 'holdings-aggregates.json'), JSON.stringify(holdingsAggregates, null, 1))
  if (mapTiles.length) writeFileSync(path.join(OUT, 'map-tiles.json'), JSON.stringify(mapTiles, null, 1))
  if (contrastRows.length) writeFileSync(path.join(OUT, 'contrast-table.json'), JSON.stringify(contrastRows, null, 1))
  if (performanceStates.length) writeFileSync(path.join(OUT, 'performance-state.json'), JSON.stringify(performanceStates, null, 1))
  writeFileSync(path.join(OUT, 'lead-lists.json'), JSON.stringify({ schema_version: '1.0', tool: 'ui-walk', stamp, lists: leadLists }, null, 1))
  writeFileSync(path.join(OUT, 'netlog.tsv'), netlog.join('\n') + '\n')
  writeFileSync(path.join(OUT, 'guard.tsv'), guard.join('\n') + '\n')
  const md = [`# ui-walk ${stamp}`, '', `base ${opt.base}; routes ${opt.routes.join(', ')}; clients ${opt.clients.join(' | ') || (firstName ? 'the first listed client' : '(none)')}; ${doc.minutes} min; ${shotN} screenshots`, '',
    `- unique findings: ${unique.length} (from ${findings.length} step observations)`, `- guard aborts (non-admitted writes blocked): ${guard.length}; telemetry answered locally: ${stubbed}`, `- API answers not READY / not ok: ${apiIssues.length}`, `- console errors: ${consoleErrors.length}`, '',
    '| check | unique findings |', '|---|---|', ...Object.entries(counts).sort((a, b) => b[1] - a[1]).map(([k, v]) => `| ${k} | ${v} |`), '',
    '## Unique findings', '', ...unique.map((f) => `- **${f.id}** \`${f.check}\` -- ${String(f.observed).slice(0, 160)} (steps: ${f.steps.length}; first shot ${f.screenshots[0] || 'n/a'})`), '',
    'Screenshots and findings are under this folder (gitignored: they carry client data).'].join('\n')
  writeFileSync(path.join(OUT, 'summary.md'), md + '\n')
  log('OUT', OUT)
  log(`SUMMARY: ${unique.length} unique finding(s) from ${findings.length} observations, ${shotN} screenshot(s), ${guard.length} guard abort(s), ${stubbed} telemetry stubbed, ${apiIssues.length} API issue(s), ${consoleErrors.length} console error(s), walk void: ${walkVoid ? 'yes' : 'no'}`)
  if (walkVoid) process.exitCode = 3
}
