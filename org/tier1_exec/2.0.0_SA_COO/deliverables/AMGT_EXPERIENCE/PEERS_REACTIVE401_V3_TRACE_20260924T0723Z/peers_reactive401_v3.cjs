/* Peers B04/P1 FAILURE CASE 1, REACTIVE ARM, v3 (2.0.0_SA_COO~Z, 2026-09-24): the DIFFERENT-SECURITY case driven through
 * the app's own navigation. In Security mode the ranked list is not rendered, so: (1) read the EXPIRED bearer with scripts
 * aborted; (2) load BA normally (proactive refresh, marker fresh); (3) click "Back to universe" (client-side; the ranked
 * list renders with the FRESH bearer); (4) swap the EXPIRED bearer back into localStorage; (5) click a ranked-list row
 * for a security other than BA -- its bundles fire with the expired bearer -> edge 401 -> /auth/refresh -> retried 200;
 * (6) record the sequence, the URL after the click, and the Peers panel's identity line, which must name the NEW name.
 * Never prints a token. argv: <userDataDir> <outDir> [base]
 */
const path = require('node:path');
const fs = require('node:fs');
const { chromium } = require(path.join('C:', 'Users', 'Opal Bloomberg', 'Desktop', 'ajb_workspace', 'portal', 'node_modules', 'playwright-core'));

const userDataDir = process.argv[2];
const outDir = process.argv[3];
const base = process.argv[4] || 'https://d2n2nzpeqf34ge.cloudfront.net';
fs.mkdirSync(outDir, { recursive: true });
const trace = { started_at: new Date().toISOString(), base, expired_token: null, proactive: [], universe_rows: [], reactive: { sequence: [], console: [], first_401: null, refresh_after_401: null, retried_200: null, clicked_row_text: null }, rendered: null };
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
    if (phase === 'proactive' || phase === 'universe') trace.proactive.push(rec);
    if (phase === 'reactive') {
      trace.reactive.sequence.push(rec);
      if (r.status() === 401 && !trace.reactive.first_401) trace.reactive.first_401 = rec;
      if (u.includes('/auth/refresh') && trace.reactive.first_401 && !trace.reactive.refresh_after_401) trace.reactive.refresh_after_401 = rec;
      if (r.status() === 200 && trace.reactive.first_401 && u.includes('/api/scoped/amgt') && !trace.reactive.retried_200) trace.reactive.retried_200 = rec;
    }
    save();
  });
  page.on('console', (m) => { const t = m.text(); if (t.includes('[api-client]')) { trace.reactive.console.push({ at: new Date().toISOString(), phase, text: t }); save(); } });

  await page.route('**/*.js', (route) => route.abort());
  await page.route('**/*.mjs', (route) => route.abort());
  await page.goto(base + '/security-analysis/BA_US_Equity', { waitUntil: 'domcontentloaded' }).catch(() => {});
  await page.waitForTimeout(1500);
  const expired = await page.evaluate(() => localStorage.getItem('accessToken')).catch(() => null);
  const now = Math.floor(Date.now() / 1000);
  trace.expired_token = expired ? { present: true, exp: exp(expired), now, expired: exp(expired) !== null && exp(expired) < now } : { present: false };
  log('stored bearer: ' + JSON.stringify(trace.expired_token));
  await page.unroute('**/*.js'); await page.unroute('**/*.mjs');
  if (!expired || !trace.expired_token.expired) { log('PRECONDITION NOT MET: no stored bearer, or it has not expired yet'); save(); await ctx.close(); process.exit(2); }

  phase = 'proactive';
  await page.goto(base + '/security-analysis/BA_US_Equity', { waitUntil: 'networkidle', timeout: 60000 });
  const fresh = await page.evaluate(() => localStorage.getItem('accessToken'));
  if (!fresh || page.url().includes('/login')) { log('NO SESSION after the proactive load -- ' + page.url()); save(); await ctx.close(); process.exit(2); }
  log('proactive load done; fresh bearer exp ' + exp(fresh));

  phase = 'universe';
  await page.getByRole('button', { name: 'Back to universe', exact: true }).first().click({ timeout: 15000 });
  await page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {});
  await page.waitForTimeout(2000);
  trace.universe_rows = await page.evaluate(() => Array.from(document.querySelectorAll('li')).map((e) => ({ attrs: Array.from(e.attributes).filter((a) => a.name.startsWith('data-')).map((a) => a.name + '=' + a.value).join(' '), text: (e.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 100) })).filter((r) => r.text && !r.attrs.includes('data-feed-item')));
  log('universe url ' + page.url() + '; li rows ' + trace.universe_rows.length + ': ' + JSON.stringify(trace.universe_rows.slice(0, 8)));
  save();

  await page.evaluate((t) => localStorage.setItem('accessToken', t), expired);
  phase = 'reactive';
  const lis = page.locator('li');
  const n = await lis.count();
  let clicked = null;
  for (let i = 0; i < n; i++) {
    const el = lis.nth(i);
    const attrs = await el.evaluate((e) => Array.from(e.attributes).map((a) => a.name).join(' '));
    if (attrs.includes('data-feed-item')) continue;
    const t = (await el.innerText().catch(() => '')).replace(/\s+/g, ' ').trim();
    if (!t || t.length > 160) continue;
    if (/Boeing|\bBA\b/.test(t)) continue;
    if (!/\d/.test(t)) continue; // a ranked row carries a rank and a score
    try { await el.click({ timeout: 10000 }); clicked = t; break; } catch (e) { /* next */ }
  }
  trace.reactive.clicked_row_text = clicked;
  log('clicked row: ' + JSON.stringify(clicked) + ' of ' + n + ' li');
  await page.waitForTimeout(1500);
  await page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {});
  const tab = page.locator('[role="tab"]:has-text("Peers"), button:has-text("Peers"), button:has-text("PEERS")').first();
  if (await tab.count()) { await tab.click({ timeout: 15000 }).catch(() => {}); await page.waitForLoadState('networkidle', { timeout: 30000 }).catch(() => {}); await page.waitForTimeout(1500); }
  trace.rendered = await page.evaluate(() => ({ url: location.href, on_login: location.pathname === '/login', peers_head: (document.querySelector('[data-tab-panel="peers"]') || { innerText: '' }).innerText.slice(0, 160), rows: (() => { const t = document.querySelector('[data-csc-table]'); return t ? t.querySelectorAll('tbody tr').length : null; })() }));
  const after = await page.evaluate(() => localStorage.getItem('accessToken'));
  trace.reactive.bearer_after = { rotated: after !== expired, exp: after ? exp(after) : null };
  await page.screenshot({ path: path.join(outDir, 'reactive_v3_peers.png'), fullPage: true });
  trace.finished_at = new Date().toISOString(); save();
  log('REACTIVE v3: first_401=' + JSON.stringify(trace.reactive.first_401) + ' refresh=' + JSON.stringify(trace.reactive.refresh_after_401) + ' retried_200=' + JSON.stringify(trace.reactive.retried_200) + ' rendered=' + JSON.stringify(trace.rendered));
  await ctx.close();
})().catch((e) => { log('FATAL ' + e.stack); save(); process.exit(1); });
