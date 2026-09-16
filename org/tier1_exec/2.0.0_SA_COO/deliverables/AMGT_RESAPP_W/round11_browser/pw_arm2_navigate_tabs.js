async (page) => {
  // ROUND 11 BROWSER HALF OF rj-3 -- arm 2: NAVIGATION from a ranked row, then the five tabs, in a FRESH context.
  const ORIGIN = 'http://[::1]:5175';
  const DIR = 'C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.playwright-mcp/round11/';
  const ROUTES = {
    '/api/scoped/amgt/lead-panel/rankings/trending/chatter': ['rankings.trending.chatter.response.2026-09-15.json', '698c391592a41a213365b147136194494f08fb4c06eb72e6ed613c9ac651ef5d'],
    '/api/scoped/amgt/security/BA_US_Equity/thesis': ['thesis.BA_US_Equity.response.2026-09-15.json', 'f2e7c040727195a1ba4a2775d19eac0eb551dc3382902eb014ad4b465aed5cad'],
    '/api/scoped/amgt/security/BA_US_Equity/overlay': ['overlay.BA_US_Equity.deployed.json', null],
    '/api/scoped/amgt/security/BA_US_Equity/peers': ['peers.BA_US_Equity.deployed.json', null],
    '/api/scoped/amgt/security/BA_US_Equity/coverage': ['coverage.BA_US_Equity.deployed.json', null],
    '/api/scoped/amgt/watchlist': ['watchlist.deployed.json', null],
    '/api/scoped/amgt/lead-panel/timeseries/trending/chatter': ['timeseries.trending.chatter.deployed.json', null],
  };
  const utf8 = (s) => unescape(encodeURIComponent(s));
  const sha256 = (ascii) => {
    const rrot = (v, n) => (v >>> n) | (v << (32 - n));
    const K = [], H = [], comp = {};
    for (let c = 2, n = 0; n < 64; c++) {
      if (!comp[c]) { for (let i = c * c; i < 313; i += c) comp[i] = 1; H[n] = (Math.pow(c, 0.5) * 4294967296) | 0; K[n++] = (Math.pow(c, 1 / 3) * 4294967296) | 0; }
    }
    const hash = H.slice(0, 8);
    const bitLen = ascii.length * 8;
    ascii += '\x80';
    while ((ascii.length % 64) - 56) ascii += '\x00';
    const words = [];
    for (let i = 0; i < ascii.length; i++) words[i >> 2] |= ascii.charCodeAt(i) << ((3 - i) % 4) * 8;
    words[words.length] = (bitLen / 4294967296) | 0;
    words[words.length] = bitLen | 0;
    for (let j = 0; j < words.length;) {
      const w = words.slice(j, (j += 16));
      const old = hash.slice(0);
      for (let i = 0; i < 64; i++) {
        const w15 = w[i - 15], w2 = w[i - 2], a = hash[0], e = hash[4];
        const t1 = hash[7] + (rrot(e, 6) ^ rrot(e, 11) ^ rrot(e, 25)) + ((e & hash[5]) ^ (~e & hash[6])) + K[i]
          + (w[i] = i < 16 ? w[i] : (w[i - 16] + (rrot(w15, 7) ^ rrot(w15, 18) ^ (w15 >>> 3)) + w[i - 7] + (rrot(w2, 17) ^ rrot(w2, 19) ^ (w2 >>> 10))) | 0);
        const t2 = (rrot(a, 2) ^ rrot(a, 13) ^ rrot(a, 22)) + ((a & hash[1]) ^ (a & hash[2]) ^ (hash[1] & hash[2]));
        hash.unshift((t1 + t2) | 0);
        hash[4] = (hash[4] + t1) | 0;
        hash.length = 8;
      }
      for (let i = 0; i < 8; i++) hash[i] = (hash[i] + old[i]) | 0;
    }
    let out = '';
    for (let i = 0; i < 8; i++) for (let j = 3; j + 1; j--) { const b = (hash[i] >> (j * 8)) & 255; out += (b < 16 ? '0' : '') + b.toString(16); }
    return out;
  };
  if (sha256(utf8('abc')) !== 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad') return JSON.stringify({ error: 'sha256 self-test failed' });
  const pathOf = (u) => { const m = /^[a-z]+:\/\/[^/]+(\/[^?#]*)(\?[^#]*)?/i.exec(u); return m ? [m[1], m[2] || ''] : [u, '']; };

  const log = [];
  const handlerErrors = [];
  const user = { email: 'dev@opalcapital.com', role: 'admin', firmId: 'opal-capital', userType: 'Dev', name: 'Dev Stub' };
  const ctx = await page.context().browser().newContext();
  const p = await ctx.newPage();
  const console401 = [];
  p.on('response', (r) => { if (r.status() === 401) console401.push(r.url().slice(0, 160)); });
  await ctx.route('**/auth/refresh', async (route) => { log.push({ kind: 'auth', path: '/auth/refresh', status: 200 }); await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ accessToken: 'stub.access.token', user }) }); });
  await ctx.route('**/auth/me', async (route) => { log.push({ kind: 'auth', path: '/auth/me', status: 200 }); await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ user }) }); });
  await ctx.route('**/api/scoped/amgt/**', async (route) => {
    try {
      const [path, query] = pathOf(route.request().url());
      const hit = ROUTES[path];
      if (!hit) { log.push({ kind: 'scoped', path, query, status: 404, served: 'NONE (not captured)' }); await route.fulfill({ status: 404, contentType: 'application/json', body: '{"error":"not captured for the round-11 exercise"}' }); return; }
      const r = await ctx.request.get(ORIGIN + '/__exercise/' + hit[0]);
      const text = await r.text();
      const fileSha = sha256(utf8(text));
      const env = JSON.parse(text);
      const body = env.body || '';
      log.push({ kind: 'scoped', path, query, status: env.statusCode || 200, file: hit[0], fileSha, fileShaEqual: hit[1] ? fileSha === hit[1] : 'n/a', servedBodySha: sha256(utf8(body)) });
      await route.fulfill({ status: env.statusCode || 200, contentType: 'application/json', body });
    } catch (e) { handlerErrors.push(String(e).slice(0, 240)); await route.abort().catch(() => {}); }
  });

  await p.goto(ORIGIN + '/security-analysis', { waitUntil: 'networkidle' });
  await p.waitForTimeout(2500);
  const before = log.length;
  // NAVIGATION: click the ranked row whose ticker text is exactly "BA US" (not "BABA US").
  const row = p.getByText('BA US', { exact: true }).first();
  await row.click();
  await p.waitForTimeout(3500);
  const afterClick = await p.evaluate(() => location.href);
  const navRequests = log.slice(before).map((x) => x.path + (x.query || ''));

  const tabText = async (label) => {
    await p.getByRole('button', { name: label, exact: true }).or(p.getByRole('tab', { name: label, exact: true })).first().click();
    await p.waitForTimeout(1500);
    const text = await p.evaluate(() => (document.querySelector('main') || document.body).innerText);
    const lines = text.split(String.fromCharCode(10)).map((s) => s.trim()).filter(Boolean);
    const idx = lines.findIndex((l) => l === 'POSTURE');
    const body = lines.slice(idx + 1);
    const file = DIR + 'ROUND11_BROWSER_arm2-tab-' + label.toLowerCase().replace(/ /g, '-') + '.png';
    await p.screenshot({ path: file, fullPage: true });
    return { lineCount: body.length, head: body.slice(0, 45) };
  };
  const tabs = {};
  for (const label of ['THESIS', 'EXEC MANAGEMENT', 'PEERS', 'MODEL', 'POSTURE']) {
    try { tabs[label] = await tabText(label); } catch (e) { tabs[label] = { error: String(e).slice(0, 200) }; }
  }
  const thesisDom = await p.evaluate(() => ({
    blockquotes: document.querySelectorAll('blockquote').length,
    titleEvidenceAttrs: Array.from(document.querySelectorAll('[title]')).filter((n) => (n.getAttribute('title') || '').startsWith('Evidence')).length,
  }));
  await ctx.close();
  return JSON.stringify({ afterClick, navRequests, tabs, thesisDom, transport: log, handlerErrors, responses401: console401.slice(0, 10) });
}
