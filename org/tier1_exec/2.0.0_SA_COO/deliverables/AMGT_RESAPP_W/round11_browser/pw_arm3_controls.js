async (page) => {
  // ROUND 11 BROWSER HALF OF rj-3 -- arms 3-5: the CONTROLS, each in its own FRESH context.
  //   ERROR  : the ranked read answers 503 every time (react-query retries) -> the read-failure sentence.
  //   EMPTY  : Movement = Breakout, served the DEPLOYED adapter's genuine EMPTY generation for today.
  //   ABSENT : the trending path served the DEPLOYED adapter's genuine no-pointer read (as_of 2026-09-13).
  // Every arm prints the served body's own ranking_status so the arm is named by the payload, not by intent.
  const ORIGIN = 'http://[::1]:5175';
  const DIR = 'C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.playwright-mcp/round11/';
  const COMMON = {
    '/api/scoped/amgt/watchlist': 'watchlist.deployed.json',
    '/api/scoped/amgt/lead-panel/timeseries/trending/chatter': 'timeseries.trending.chatter.deployed.json',
  };
  const pathOf = (u) => { const m = /^[a-z]+:\/\/[^/]+(\/[^?#]*)(\?[^#]*)?/i.exec(u); return m ? [m[1], m[2] || ''] : [u, '']; };
  const user = { email: 'dev@opalcapital.com', role: 'admin', firmId: 'opal-capital', userType: 'Dev', name: 'Dev Stub' };
  const TREND = '/api/scoped/amgt/lead-panel/rankings/trending/chatter';
  const BREAK = '/api/scoped/amgt/lead-panel/rankings/breakout/chatter';

  const runArm = async (name, mapping, afterLoad) => {
    const log = [];
    const handlerErrors = [];
    const ctx = await page.context().browser().newContext();
    const p = await ctx.newPage();
    p.setDefaultTimeout(10000);
    await ctx.route('**/auth/refresh', async (route) => { await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ accessToken: 'stub.access.token', user }) }); });
    await ctx.route('**/auth/me', async (route) => { await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ user }) }); });
    await ctx.route('**/api/scoped/amgt/**', async (route) => {
      try {
        const [path, query] = pathOf(route.request().url());
        const m = mapping[path] || COMMON[path];
        if (m === 503) {
          log.push({ path, query, status: 503, served: 'stubbed 503' });
          await route.fulfill({ status: 503, contentType: 'application/json', body: '{"message":"Service Unavailable (round-11 error arm)"}' });
          return;
        }
        if (!m) { log.push({ path, query, status: 404, served: 'NONE (not captured)' }); await route.fulfill({ status: 404, contentType: 'application/json', body: '{"error":"not captured"}' }); return; }
        const r = await ctx.request.get(ORIGIN + '/__exercise/' + m);
        const env = JSON.parse(await r.text());
        const body = env.body || '';
        let status = null, state = null, rowCount = null;
        try { const b = JSON.parse(body); status = b.ranking_status || null; state = b.state || null; rowCount = b.row_count; } catch (e) {}
        log.push({ path, query, status: env.statusCode || 200, file: m, ranking_status: status, state, row_count: rowCount });
        await route.fulfill({ status: env.statusCode || 200, contentType: 'application/json', body });
      } catch (e) { handlerErrors.push(String(e).slice(0, 200)); await route.abort().catch(() => {}); }
    });
    await p.goto(ORIGIN + '/security-analysis', { waitUntil: 'networkidle' });
    await p.waitForTimeout(2500);
    if (afterLoad) { await afterLoad(p); await p.waitForTimeout(6000); }
    const panel = await p.evaluate(() => {
      const lines = (document.body.innerText || '').split(String.fromCharCode(10)).map((s) => s.trim()).filter(Boolean);
      const i = lines.findIndex((l) => l === 'LEAD PANEL');
      const j = lines.findIndex((l) => l === 'THESIS');
      return lines.slice(Math.max(0, i), j > i ? j : i + 30);
    });
    const text = panel.join(' | ');
    await p.screenshot({ path: DIR + 'ROUND11_BROWSER_arm-' + name + '.png', fullPage: true });
    await ctx.close();
    return {
      arm: name,
      panel,
      says_read_failure: /read failure/i.test(text),
      says_daily_job: /daily job/i.test(text),
      says_no_ranked_names: /no ranked names/i.test(text),
      says_absent: /absent|no pointer|no generation/i.test(text),
      transport: log,
      handlerErrors,
    };
  };

  // Close contexts a failed earlier run left open (everything but the tool's own context).
  const own = page.context();
  let closedStray = 0;
  for (const c of page.context().browser().contexts()) { if (c !== own) { await c.close().catch(() => {}); closedStray++; } }
  const safe = async (name, mapping, afterLoad) => { try { return await runArm(name, mapping, afterLoad); } catch (e) { return { arm: name, error: String(e).slice(0, 300) }; } };
  const out = { closedStrayContexts: closedStray };
  out.error = await safe('error-503', { [TREND]: 503 }, null);
  out.empty = await safe('empty-breakout', { [TREND]: 'rankings.trending.chatter.response.2026-09-15.json', [BREAK]: 'rankings.breakout.chatter.deployed.json' },
    async (p) => { await p.locator('select').filter({ has: p.locator('option[value="BREAKOUT"]') }).first().selectOption('BREAKOUT'); });
  out.absent = await safe('absent-no-pointer', { [TREND]: 'rankings.trending.chatter.asof20260913.deployed.json' }, null);
  return JSON.stringify(out);
}
