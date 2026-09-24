/* Peers B04/P1 FAILURE CASE 1, REACTIVE ARM (2.0.0_SA_COO~Z, 2026-09-24): "expired session: edge 401 -> refresh -> retry".
 * The proactive arm (ensureFreshToken) was exercised at 05:03Z and hides the 401 branch on a full reload. To reach
 * the reactive branch this driver: (1) loads the app origin with every script ABORTED so the page cannot refresh,
 * and reads the EXPIRED bearer out of localStorage; (2) loads the app normally (it refreshes proactively, sets its
 * in-memory issued-at marker); (3) swaps the expired bearer back into localStorage WITHOUT reloading, so the marker
 * still reads fresh; (4) navigates CLIENT-SIDE (pushState + popstate) to another security, so the next requests go out
 * with the expired bearer -> the edge answers 401 -> api-client refreshAndRetry -> the retried 200. Records every
 * /api/scoped/amgt status in order, the /auth/refresh call, and the api-client console line. Never prints a token.
 * argv: <userDataDir> <outDir> [base]
 */
const path = require('node:path');
const fs = require('node:fs');
const { chromium } = require(path.join('C:', 'Users', 'Opal Bloomberg', 'Desktop', 'ajb_workspace', 'portal', 'node_modules', 'playwright-core'));

const userDataDir = process.argv[2];
const outDir = process.argv[3];
const base = process.argv[4] || 'https://d2n2nzpeqf34ge.cloudfront.net';
fs.mkdirSync(outDir, { recursive: true });
const trace = { started_at: new Date().toISOString(), base, expired_token: null, proactive: null, reactive: { sequence: [], console: [], first_401: null, refresh_after_401: null, retried_200: null }, rendered: null };
const save = () => fs.writeFileSync(path.join(outDir, 'trace.json'), JSON.stringify(trace, null, 2));
const log = (m) => { const line = new Date().toISOString() + ' ' + m; console.log(line); fs.appendFileSync(path.join(outDir, 'run.log'), line + '\n'); };
const exp = (t) => { try { return JSON.parse(Buffer.from(t.split('.')[1].replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf8')).exp; } catch (e) { return null; } };

(async () => {
  const ctx = await chromium.launchPersistentContext(userDataDir, { channel: 'msedge', headless: false, viewport: { width: 1440, height: 1000 } });
  const page = ctx.pages()[0] || (await ctx.newPage());
  let phase = 'read-expired';
  page.on('response', (r) => {
    const u = r.url();
    if (!(u.includes('/api/scoped/amgt') || u.includes('/auth/'))) return;
    const rec = { at: new Date().toISOString(), phase, url: u.replace(/\?.*$/, ''), status: r.status() };
    if (phase === 'proactive') { trace.proactive = trace.proactive || []; trace.proactive.push(rec); }
    if (phase === 'reactive') {
      trace.reactive.sequence.push(rec);
      if (r.status() === 401 && !trace.reactive.first_401) trace.reactive.first_401 = rec;
      if (u.includes('/auth/refresh') && trace.reactive.first_401 && !trace.reactive.refresh_after_401) trace.reactive.refresh_after_401 = rec;
      if (r.status() === 200 && trace.reactive.first_401 && u.includes('/api/scoped/amgt') && !trace.reactive.retried_200) trace.reactive.retried_200 = rec;
    }
    save();
  });
  page.on('console', (m) => { const t = m.text(); if (t.includes('[api-client]')) { trace.reactive.console.push({ at: new Date().toISOString(), phase, text: t }); save(); } });

  // (1) the expired bearer, read with the app's scripts aborted so nothing can refresh it first
  await page.route('**/*.js', (route) => route.abort());
  await page.route('**/*.mjs', (route) => route.abort());
  await page.goto(base + '/security-analysis/BA_US_Equity', { waitUntil: 'domcontentloaded' }).catch(() => {});
  await page.waitForTimeout(1500);
  const expired = await page.evaluate(() => localStorage.getItem('accessToken')).catch(() => null);
  const now = Math.floor(Date.now() / 1000);
  trace.expired_token = expired ? { present: true, exp: exp(expired), now, expired: exp(expired) !== null && exp(expired) < now } : { present: false };
  log('stored bearer: ' + JSON.stringify(trace.expired_token));
  await page.unroute('**/*.js'); await page.unroute('**/*.mjs');
  if (!expired || !trace.expired_token.expired) { log('PRECONDITION NOT MET: no stored bearer, or it has not expired yet -- rerun after exp'); save(); await ctx.close(); process.exit(2); }

  // (2) normal load: the app refreshes proactively and sets its in-memory issued-at marker
  phase = 'proactive';
  await page.goto(base + '/security-analysis/BA_US_Equity', { waitUntil: 'networkidle', timeout: 60000 });
  const fresh = await page.evaluate(() => localStorage.getItem('accessToken'));
  if (!fresh || page.url().includes('/login')) { log('NO SESSION after the proactive load (refresh cookie gone?) -- ' + page.url()); save(); await ctx.close(); process.exit(2); }
  log('proactive load done; fresh bearer exp ' + exp(fresh) + '; calls ' + JSON.stringify((trace.proactive || []).map((r) => r.status + ' ' + r.url.split('.net')[1])));

  // (3) swap the EXPIRED bearer back in without reloading (marker stays fresh -> ensureFreshToken skips the refresh)
  await page.evaluate((t) => localStorage.setItem('accessToken', t), expired);
  // (4) client-side navigation to another security: new queries go out with the expired bearer
  phase = 'reactive';
  await page.evaluate(() => { window.history.pushState({}, '', '/security-analysis/CAT_US_Equity'); window.dispatchEvent(new PopStateEvent('popstate')); });
  await page.waitForTimeout(1500);
  await page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {});
  const tab = page.locator('[role="tab"]:has-text("Peers"), button:has-text("Peers")').first();
  if (await tab.count()) { await tab.click({ timeout: 15000 }).catch(() => {}); await page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {}); await page.waitForTimeout(1500); }
  trace.rendered = await page.evaluate(() => ({ url: location.href, on_login: location.pathname === '/login', peers_text: (document.querySelector('[data-tab-panel="peers"]') || { innerText: '' }).innerText.slice(0, 600), rows: (() => { const t = document.querySelector('[data-csc-table]'); return t ? t.querySelectorAll('tbody tr').length : null; })() }));
  const after = await page.evaluate(() => localStorage.getItem('accessToken'));
  trace.reactive.bearer_after = { rotated: after !== expired, exp: after ? exp(after) : null };
  await page.screenshot({ path: path.join(outDir, 'reactive_CAT_US_Equity_peers.png'), fullPage: true });
  trace.finished_at = new Date().toISOString(); save();
  log('REACTIVE: first_401=' + JSON.stringify(trace.reactive.first_401) + ' refresh_after_401=' + JSON.stringify(trace.reactive.refresh_after_401) + ' retried_200=' + JSON.stringify(trace.reactive.retried_200) + ' console=' + trace.reactive.console.length + ' rendered=' + JSON.stringify(trace.rendered));
  await ctx.close();
})().catch((e) => { log('FATAL ' + e.stack); save(); process.exit(1); });
