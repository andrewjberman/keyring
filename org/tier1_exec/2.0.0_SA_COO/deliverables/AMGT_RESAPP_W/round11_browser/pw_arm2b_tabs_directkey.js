async (page) => {
  // ROUND 11 BROWSER HALF OF rj-3 -- arm 2b: the DIRECT-KEY control and the FIVE TABS, fresh context.
  //   (a) /security-analysis/BA_US_Equity loaded directly: which security requests fire (compare with arm 2's click).
  //   (b) each tab opened by a case-insensitive text locator; its rendered text, its requests, a screenshot.
  const ORIGIN = 'http://[::1]:5175';
  const DIR = 'C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.playwright-mcp/round11/';
  const ROUTES = {
    '/api/scoped/amgt/lead-panel/rankings/trending/chatter': 'rankings.trending.chatter.response.2026-09-15.json',
    '/api/scoped/amgt/security/BA_US_Equity/thesis': 'thesis.BA_US_Equity.response.2026-09-15.json',
    '/api/scoped/amgt/security/BA_US_Equity/overlay': 'overlay.BA_US_Equity.deployed.json',
    '/api/scoped/amgt/security/BA_US_Equity/peers': 'peers.BA_US_Equity.deployed.json',
    '/api/scoped/amgt/security/BA_US_Equity/coverage': 'coverage.BA_US_Equity.deployed.json',
    '/api/scoped/amgt/watchlist': 'watchlist.deployed.json',
    '/api/scoped/amgt/lead-panel/timeseries/trending/chatter': 'timeseries.trending.chatter.deployed.json',
  };
  const pathOf = (u) => { const m = /^[a-z]+:\/\/[^/]+(\/[^?#]*)(\?[^#]*)?/i.exec(u); return m ? [m[1], m[2] || ''] : [u, '']; };
  const user = { email: 'dev@opalcapital.com', role: 'admin', firmId: 'opal-capital', userType: 'Dev', name: 'Dev Stub' };
  const log = [];
  const handlerErrors = [];
  const ctx = await page.context().browser().newContext();
  const p = await ctx.newPage();
  p.setDefaultTimeout(8000);
  await ctx.route('**/auth/refresh', async (route) => { await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ accessToken: 'stub.access.token', user }) }); });
  await ctx.route('**/auth/me', async (route) => { await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ user }) }); });
  await ctx.route('**/api/scoped/amgt/**', async (route) => {
    try {
      const [path, query] = pathOf(route.request().url());
      const f = ROUTES[path];
      if (!f) { log.push({ path, query, status: 404, served: 'NONE (not captured)' }); await route.fulfill({ status: 404, contentType: 'application/json', body: '{"error":"not captured"}' }); return; }
      const r = await ctx.request.get(ORIGIN + '/__exercise/' + f);
      const env = JSON.parse(await r.text());
      log.push({ path, query, status: env.statusCode || 200, file: f });
      await route.fulfill({ status: env.statusCode || 200, contentType: 'application/json', body: env.body || '' });
    } catch (e) { handlerErrors.push(String(e).slice(0, 200)); await route.abort().catch(() => {}); }
  });

  // (a) direct key
  await p.goto(ORIGIN + '/security-analysis/BA_US_Equity', { waitUntil: 'networkidle' });
  await p.waitForTimeout(3500);
  const directRequests = log.map((x) => x.path);

  // (b) the tabs
  const readMain = async () => p.evaluate(() => {
    const lines = ((document.querySelector('main') || document.body).innerText || '').split(String.fromCharCode(10)).map((s) => s.trim()).filter(Boolean);
    let k = -1;
    for (let i = lines.length - 1; i >= 0; i--) { if (/^posture$/i.test(lines[i])) { k = i; break; } }
    return lines.slice(k + 1, k + 1 + 60);
  });
  const tabs = {};
  for (const label of ['Thesis', 'Exec Management', 'Peers', 'Model', 'Posture']) {
    const before = log.length;
    try {
      const re = new RegExp('^\\s*' + label + '\\s*$', 'i');
      await p.locator('button, [role="tab"]').filter({ hasText: re }).first().click();
      await p.waitForTimeout(2500);
      const head = await readMain();
      await p.screenshot({ path: DIR + 'ROUND11_BROWSER_arm2b-tab-' + label.toLowerCase().replace(/ /g, '-') + '.png', fullPage: true });
      tabs[label] = { requests: log.slice(before).map((x) => x.path + ' ' + x.status), head };
    } catch (e) {
      tabs[label] = { error: String(e).slice(0, 200) };
    }
  }
  const dom = await p.evaluate(() => ({
    blockquotes: document.querySelectorAll('blockquote').length,
    titleEvidenceAttrs: Array.from(document.querySelectorAll('[title]')).filter((n) => (n.getAttribute('title') || '').startsWith('Evidence')).length,
    tradeButtons: Array.from(document.querySelectorAll('button')).filter((b) => /\b(buy|sell|order)\b/i.test(b.innerText || '')).length,
    url: location.href,
  }));
  await ctx.close();
  return JSON.stringify({ directRequests, tabs, dom, transport: log, handlerErrors });
}
