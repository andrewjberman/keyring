/* Peers B04/P1 LIVE THREAD runner (2.0.0_SA_COO~Z, 2026-09-24).
 * Headed Chromium from the portal's own playwright-core. A HUMAN signs in (MFA) in the window;
 * this script only waits for a session, then walks the acceptance cases on the SERVED stack and
 * records every /api/scoped/amgt response, the rendered Peers panel text, the Posture reads and a
 * screenshot per case. It never types a credential and never prints a token.
 * argv: <userDataDir> <outDir> [base]
 */
const path = require('node:path');
const fs = require('node:fs');
const { chromium } = require(path.join('C:', 'Users', 'Opal Bloomberg', 'Desktop', 'ajb_workspace', 'portal', 'node_modules', 'playwright-core'));

const userDataDir = process.argv[2];
const outDir = process.argv[3];
const base = process.argv[4] || 'https://d2n2nzpeqf34ge.cloudfront.net';
fs.mkdirSync(outDir, { recursive: true });
const trace = { started_at: new Date().toISOString(), base, sign_in: null, cases: [], api: [] };
const save = () => fs.writeFileSync(path.join(outDir, 'trace.json'), JSON.stringify(trace, null, 2));
const log = (m) => { const line = new Date().toISOString() + ' ' + m; console.log(line); fs.appendFileSync(path.join(outDir, 'run.log'), line + '\n'); };

const CASES = ['BA_US_Equity', '992_HK_Equity', 'ASML_US_Equity', 'CAT_US_Equity', 'NOSUCHKEY_ZZ_Equity', 'BP/_LN_Equity'];

function decodeClaims(token) {
  try {
    const payload = JSON.parse(Buffer.from(token.split('.')[1].replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf8'));
    const keep = {};
    for (const k of ['role', 'userType', 'custom:userType', 'custom:role', 'cognito:groups', 'exp', 'iss', 'token_use']) if (k in payload) keep[k] = payload[k];
    return keep;
  } catch (e) { return { decode_error: String(e) }; }
}

(async () => {
  const ctx = await chromium.launchPersistentContext(userDataDir, { channel: 'msedge', headless: false, viewport: { width: 1440, height: 1000 } });
  const page = ctx.pages()[0] || (await ctx.newPage());
  page.on('response', async (r) => {
    const u = r.url();
    if (!u.includes('/api/scoped/amgt')) return;
    let body = null;
    try { body = await r.text(); } catch (e) { body = 'UNREADABLE: ' + e; }
    trace.api.push({ at: new Date().toISOString(), url: u, status: r.status(), body });
    save();
  });
  await page.goto(base + '/login', { waitUntil: 'domcontentloaded' });
  log('login page opened; waiting up to 40 minutes for a human sign-in (MFA)');
  const deadline = Date.now() + 40 * 60 * 1000;
  let token = null;
  while (Date.now() < deadline) {
    try {
      token = await page.evaluate(() => localStorage.getItem('accessToken'));
      const idTok = await page.evaluate(() => localStorage.getItem('idToken'));
      const user = await page.evaluate(() => localStorage.getItem('user'));
      if (token && page.url().includes('/login')) { await page.goto(base + '/market', { waitUntil: 'domcontentloaded' }); await page.waitForTimeout(2500); }
      if (token && !page.url().includes('/login')) {
        trace.sign_in = { at: new Date().toISOString(), url_after: page.url(), access_claims: decodeClaims(token), id_claims: idTok ? decodeClaims(idTok) : null, user_record: user ? (() => { try { const u = JSON.parse(user); return { role: u.role, userType: u.userType, isDev: u.isDev, id_present: !!u.id }; } catch (e) { return 'unparsed'; } })() : null };
        break;
      }
    } catch (e) { /* navigating */ }
    await page.waitForTimeout(2000);
  }
  if (!trace.sign_in) { log('NO SIGN-IN within the window; exiting with nothing traced'); save(); await ctx.close(); process.exit(2); }
  log('signed in: ' + JSON.stringify(trace.sign_in));
  save();

  for (const key of CASES) {
    const rec = { security_key: key, requested_url: base + '/security-analysis/' + encodeURIComponent(key) };
    const before = trace.api.length;
    try {
      await page.goto(rec.requested_url, { waitUntil: 'networkidle', timeout: 60000 });
      rec.landed_url = page.url();
      rec.redirected_to_market = rec.landed_url.includes('/market');
      const tab = page.locator('[data-tab="peers"], [data-tab-id="peers"], button:has-text("Peers"), [role="tab"]:has-text("Peers")').first();
      await tab.click({ timeout: 15000 });
      await page.waitForSelector('[data-tab-panel="peers"]', { timeout: 20000 }).catch(() => {});
      await page.waitForTimeout(1500);
      await page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {});
      rec.peers_panel_present = await page.evaluate(() => !!document.querySelector('[data-tab-panel="peers"]'));
      rec.peers_panel_text = await page.evaluate(() => { const p = document.querySelector('[data-tab-panel="peers"]') || document.querySelector('[data-csc-table]')?.closest('section') || document.body; return p.innerText.slice(0, 6000); });
      rec.csc_column_states = await page.evaluate(() => Array.from(document.querySelectorAll('[data-csc-column-state]')).map((e) => e.getAttribute('data-csc-column-state')));
      rec.csc_table_rows = await page.evaluate(() => { const t = document.querySelector('[data-csc-table]'); return t ? t.querySelectorAll('tbody tr').length : null; });
      await page.screenshot({ path: path.join(outDir, key.replace(/[\/*]/g, '_') + '_peers.png'), fullPage: true });
      const posture = page.locator('[data-tab="posture"], [data-tab-id="posture"], button:has-text("Posture"), [role="tab"]:has-text("Posture")').first();
      if (await posture.count()) { await posture.click({ timeout: 15000 }); await page.waitForTimeout(1500); await page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {}); rec.posture_panel_text = await page.evaluate(() => (document.querySelector('[data-tab-panel="posture"]') || document.body).innerText.slice(0, 3000)); await page.screenshot({ path: path.join(outDir, key.replace(/[\/*]/g, '_') + '_posture.png'), fullPage: true }); }
      rec.api_calls = trace.api.slice(before).map((a) => ({ url: a.url, status: a.status, bytes: a.body ? a.body.length : 0 }));
    } catch (e) { rec.error = String(e); }
    trace.cases.push(rec); save(); log('case ' + key + ' -> ' + (rec.error || (rec.redirected_to_market ? 'REDIRECTED /market (FAIL)' : 'landed ' + rec.landed_url)));
  }
  trace.finished_at = new Date().toISOString(); save();
  log('done; browser stays open 3 minutes for a human look');
  await page.waitForTimeout(180000);
  await ctx.close();
})().catch((e) => { log('FATAL ' + e.stack); save(); process.exit(1); });
