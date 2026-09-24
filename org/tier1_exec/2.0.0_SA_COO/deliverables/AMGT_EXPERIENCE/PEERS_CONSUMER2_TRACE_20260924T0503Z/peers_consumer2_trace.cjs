/* Peers B04/P1 CONSUMER-2 + FAILURE-CASE runner (2.0.0_SA_COO~Z, 2026-09-24, session e49a705e).
 * Headed Edge from the portal's own playwright-core over a COPY of the profile a human signed in on at
 * 03:12Z. The access token in that profile EXPIRED at 03:35:43Z, so the first request this run makes is
 * mandate FAILURE CASE 1 (expired session: edge 401 -> /auth/refresh -> retry) exercised for real; if the
 * refresh token is also gone the app bounces to /login and this run reports NO-SESSION and exits 2.
 * Then every acceptance selection is walked through BOTH consumers: the Peers tab AND the Posture tab
 * (subject usePeerSet + comparable usePeerSet), recording every /api/scoped/amgt response and every
 * /auth/* status, the rendered Peers panel, the rendered Posture comparable line and the comparable's own
 * identity/peers reads. Never types a credential, never prints a token.
 * argv: <userDataDir> <outDir> [base]
 */
const path = require('node:path');
const fs = require('node:fs');
const { chromium } = require(path.join('C:', 'Users', 'Opal Bloomberg', 'Desktop', 'ajb_workspace', 'portal', 'node_modules', 'playwright-core'));

const userDataDir = process.argv[2];
const outDir = process.argv[3];
const base = process.argv[4] || 'https://d2n2nzpeqf34ge.cloudfront.net';
fs.mkdirSync(outDir, { recursive: true });
const trace = { started_at: new Date().toISOString(), base, session: null, failure_case_1: { auth_calls: [], first_401: null, refresh: null, retried_200: null }, cases: [], api: [] };
const save = () => fs.writeFileSync(path.join(outDir, 'trace.json'), JSON.stringify(trace, null, 2));
const log = (m) => { const line = new Date().toISOString() + ' ' + m; console.log(line); fs.appendFileSync(path.join(outDir, 'run.log'), line + '\n'); };

const CASES = ['BA_US_Equity', '992_HK_Equity', 'ASML_US_Equity', 'CAT_US_Equity', 'NOSUCHKEY_ZZ_Equity', 'BP/_LN_Equity'];

function decodeClaims(token) {
  try {
    const payload = JSON.parse(Buffer.from(token.split('.')[1].replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf8'));
    const keep = {};
    for (const k of ['role', 'userType', 'exp', 'iss', 'token_use']) if (k in payload) keep[k] = payload[k];
    return keep;
  } catch (e) { return { decode_error: String(e) }; }
}

(async () => {
  const ctx = await chromium.launchPersistentContext(userDataDir, { channel: 'msedge', headless: false, viewport: { width: 1440, height: 1000 } });
  const page = ctx.pages()[0] || (await ctx.newPage());
  page.on('response', async (r) => {
    const u = r.url();
    if (u.includes('/auth/')) {
      const rec = { at: new Date().toISOString(), url: u.replace(/\?.*$/, ''), status: r.status() };
      trace.failure_case_1.auth_calls.push(rec);
      if (u.includes('/auth/refresh') && !trace.failure_case_1.refresh) trace.failure_case_1.refresh = rec;
      save();
      return;
    }
    if (!u.includes('/api/')) return;
    let body = null;
    if (u.includes('/api/scoped/amgt')) { try { body = await r.text(); } catch (e) { body = 'UNREADABLE: ' + e; } }
    const rec = { at: new Date().toISOString(), url: u, status: r.status(), body };
    trace.api.push(rec);
    if (r.status() === 401 && !trace.failure_case_1.first_401) trace.failure_case_1.first_401 = { at: rec.at, url: u };
    if (r.status() === 200 && trace.failure_case_1.first_401 && !trace.failure_case_1.retried_200 && u.includes('/api/scoped/amgt')) trace.failure_case_1.retried_200 = { at: rec.at, url: u };
    save();
  });
  page.on('console', (m) => { const t = m.text(); if (t.includes('[api-client]')) { trace.failure_case_1.auth_calls.push({ at: new Date().toISOString(), console: t }); save(); } });

  // Land on a real page first: the api-client refreshes proactively (token > 10 min old) or reactively on 401.
  await page.goto(base + '/security-analysis/BA_US_Equity', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);
  let token = null;
  try { token = await page.evaluate(() => localStorage.getItem('accessToken')); } catch (e) { /* navigating */ }
  const onLogin = page.url().includes('/login');
  trace.session = { at: new Date().toISOString(), url_after: page.url(), token_present: !!token, claims: token ? decodeClaims(token) : null, on_login: onLogin };
  save();
  if (!token || onLogin) {
    log('NO-SESSION: the persisted profile did not yield a live session (refresh failed or bounced to /login). ' + JSON.stringify(trace.session));
    log('waiting up to 20 minutes for a human sign-in (MFA) in the open window');
    const deadline = Date.now() + 20 * 60 * 1000;
    while (Date.now() < deadline) {
      try {
        token = await page.evaluate(() => localStorage.getItem('accessToken'));
        if (token && page.url().includes('/login')) { await page.goto(base + '/market', { waitUntil: 'domcontentloaded' }); await page.waitForTimeout(2500); }
        if (token && !page.url().includes('/login')) { trace.session = { at: new Date().toISOString(), url_after: page.url(), token_present: true, claims: decodeClaims(token), on_login: false, human_signin: true }; break; }
      } catch (e) { /* navigating */ }
      await page.waitForTimeout(2000);
    }
    if (!token || page.url().includes('/login')) { save(); await ctx.close(); process.exit(2); }
  }
  log('session: ' + JSON.stringify(trace.session) + ' | failure_case_1: ' + JSON.stringify(trace.failure_case_1));
  save();

  for (const key of CASES) {
    const rec = { security_key: key, requested_url: base + '/security-analysis/' + encodeURIComponent(key) };
    const before = trace.api.length;
    try {
      await page.goto(rec.requested_url, { waitUntil: 'networkidle', timeout: 60000 });
      rec.landed_url = page.url();
      rec.redirected_to_market = rec.landed_url.includes('/market');
      // CONSUMER 1: Peers tab
      const tab = page.locator('[role="tab"]:has-text("Peers"), button:has-text("Peers")').first();
      await tab.click({ timeout: 15000 });
      await page.waitForSelector('[data-tab-panel="peers"]', { timeout: 20000 }).catch(() => {});
      await page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {});
      await page.waitForTimeout(1200);
      rec.peers = await page.evaluate(() => {
        const p = document.querySelector('[data-tab-panel="peers"]');
        return {
          panel_present: !!p,
          text: p ? p.innerText.slice(0, 4000) : null,
          basis_absent: !!document.querySelector('[data-peers-basis="absent"]'),
          column_states: Array.from(document.querySelectorAll('[data-csc-column-state]')).map((e) => e.getAttribute('data-csc-column-state')),
          table_rows: (() => { const t = document.querySelector('[data-csc-table]'); return t ? t.querySelectorAll('tbody tr').length : null; })(),
        };
      });
      await page.screenshot({ path: path.join(outDir, key.replace(/[\/*]/g, '_') + '_peers.png'), fullPage: true });
      // CONSUMER 2: Posture tab -- subject usePeerSet + comparable usePeerSet (PostureTab.tsx:339-347)
      const posture = page.locator('[role="tab"]:has-text("Posture"), button:has-text("Posture")').first();
      if (await posture.count()) {
        await posture.click({ timeout: 15000 });
        await page.waitForSelector('[data-tab-panel="posture"]', { timeout: 20000 }).catch(() => {});
        await page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {});
        await page.waitForTimeout(1500);
        rec.posture = await page.evaluate(() => {
          const p = document.querySelector('[data-tab-panel="posture"]');
          const comp = document.querySelector('[data-posture-comparable]');
          return {
            panel_present: !!p,
            text: (p || document.body).innerText.slice(0, 4000),
            comparable_key: comp ? comp.getAttribute('data-posture-comparable') : null,
            comparable_line: comp ? comp.innerText : null,
            cites_resolved: document.querySelector('[data-posture-cites-resolved]')?.getAttribute('data-posture-cites-resolved') ?? null,
            cites_total: document.querySelector('[data-posture-cites-total]')?.getAttribute('data-posture-cites-total') ?? null,
            peer_attrs: Array.from(document.querySelectorAll('[data-posture-peers], [data-posture-peers-subject], [data-posture-peers-comparable]')).map((e) => ({ tag: e.tagName, attrs: Array.from(e.attributes).map((a) => a.name + '=' + a.value).join(' '), text: e.innerText.slice(0, 300) })),
          };
        });
        await page.screenshot({ path: path.join(outDir, key.replace(/[\/*]/g, '_') + '_posture.png'), fullPage: true });
      }
      // every /api/scoped/amgt call this case made, with the peers reads summarised
      rec.api_calls = trace.api.slice(before).map((a) => {
        const out = { url: a.url, status: a.status, bytes: a.body ? a.body.length : 0 };
        if (a.url.endsWith('/peers') && a.body && a.status === 200) {
          try { const b = JSON.parse(a.body); out.peers = { identity: b.identity && { status: b.identity.status, security_key: b.identity.security_key }, basis: b.basis, members: (b.members || []).length, peer_read: b.peer_read && b.peer_read.status, reason: b.reason || null }; } catch (e) { out.parse_error = String(e); }
        }
        if (a.status >= 400 && a.body) out.body_head = a.body.slice(0, 200);
        return out;
      });
    } catch (e) { rec.error = String(e); }
    trace.cases.push(rec); save();
    log('case ' + key + ' -> ' + (rec.error || (rec.redirected_to_market ? 'REDIRECTED /market (FAIL)' : 'landed; peers ' + (rec.peers && (rec.peers.basis_absent ? 'ABSENT-basis' : 'rows=' + rec.peers.table_rows)) + '; posture comparable ' + (rec.posture && rec.posture.comparable_key))));
  }
  trace.finished_at = new Date().toISOString(); save();
  log('done');
  await page.waitForTimeout(5000);
  await ctx.close();
})().catch((e) => { log('FATAL ' + e.stack); save(); process.exit(1); });
