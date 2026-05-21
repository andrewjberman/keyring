// VALGATE D-2 runner -- visual-rendering structural-assertion runner.
// ADHC_VALGATE.006. The RENDER half of D-2 (the verdict half is
// d2_visual_baseline_gate.py).
//
// Drives a partner-facing portal panel in a real browser (puppeteer-core +
// system Chrome via CDP) per a structural baseline JSON, and emits a raw
// results JSON the D-2 verdict gate consumes.
//
// puppeteer-core + CDP (not Playwright) is deliberate: the portal's existing
// runner (portal/.frontend-dev/runners/sscn_divdef_001_runner.mjs) documents
// that Bun + Playwright's WebSocket client hangs on Windows during the CDP
// upgrade, while puppeteer-core's own ws client works. This runner reuses the
// /frontend-dev constitution VOCABULARY (assert-style checks) but executes
// standalone -- it does not invoke the /frontend-dev plugin's subagents.
//
// Prerequisite: system Chrome running with --remote-debugging-port=<port>,
// and a served portal (dev server or built+previewed).
//
// Usage:
//   bun run .tools/valgate/d2_runner.mjs --baseline <baseline.json> \
//     [--out <results.json>] [--base-url http://localhost:5175] [--cdp-port 9444]
//
// Baseline JSON shape:
//   { "panel": "advisor-book-headline",
//     "base_url": "http://localhost:5175",            (optional; --base-url wins)
//     "login": { "email": "...", "password": "...",   (optional)
//                "select_partner": "inflection" },
//     "route": "/advisor-intelligence",
//     "navigation": [ { "action": "js_eval"|"click"|"wait", ... } ],
//     "data_bearing_nodes": [
//       { "name": "total-aua-hero", "selector": "...",
//         "check": "visible_nonempty"|"chart_nonempty" } ],
//     "scope_checks": [
//       { "name": "advisor-scoped", "selector": "...",
//         "expect_contains": "...", "expect_not_contains": "..." } ] }
//
// Results JSON shape (consumed by d2_visual_baseline_gate.py):
//   { "panel": str, "baseline": str, "checks": [
//       { "type": "data_bearing"|"scope", "name": str,
//         "observed": "non_empty"|"empty"|"missing"|"scope_ok"|"scope_drift"|"error",
//         "detail": str } ] }

import puppeteer from 'puppeteer-core';
import { readFileSync, writeFileSync } from 'node:fs';

function arg(name, def) {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 && i + 1 < process.argv.length ? process.argv[i + 1] : def;
}

const BASELINE_PATH = arg('baseline', null);
const OUT_PATH = arg('out', 'd2-runner-results.json');
const CDP_PORT = parseInt(arg('cdp-port', process.env.D2_CDP_PORT || '9444'), 10);

if (!BASELINE_PATH) {
  console.error('ERROR: --baseline <path> is required');
  process.exit(3);
}

const baseline = JSON.parse(readFileSync(BASELINE_PATH, 'utf-8'));
const BASE = arg('base-url', baseline.base_url || 'http://localhost:5175');

const EMPTY_TEXT = ['', '--', '—', '–', 'n/a', 'na', 'null', 'undefined', '$0', '0'];

const results = {
  panel: baseline.panel || '<unknown>',
  baseline: BASELINE_PATH,
  started_at: new Date().toISOString(),
  checks: [],
  console_errors: [],
  fatal_error: null,
};

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function main() {
  // ---- connect to CDP Chrome ----
  let wsEndpoint;
  try {
    const v = await (await fetch(`http://127.0.0.1:${CDP_PORT}/json/version`)).json();
    wsEndpoint = v.webSocketDebuggerUrl;
  } catch (e) {
    results.fatal_error = `CDP Chrome not reachable on port ${CDP_PORT}: ${e.message}`;
    return 3;
  }
  const browser = await puppeteer.connect({
    browserWSEndpoint: wsEndpoint,
    defaultViewport: { width: 1600, height: 1000 },
  });
  const pages = await browser.pages();
  const page = pages[0] || (await browser.newPage());
  await page.setViewport({ width: 1600, height: 1000 });
  page.on('console', (m) => { if (m.type() === 'error') results.console_errors.push(m.text()); });
  page.on('pageerror', (e) => results.console_errors.push('pageerror: ' + e.message));

  try {
    // ---- login (optional) ----
    if (baseline.login) {
      await page.goto(`${BASE}/login`, { waitUntil: 'domcontentloaded' });
      await sleep(1200);
      await page.evaluate(() => { try { localStorage.clear(); sessionStorage.clear(); } catch {} });
      await page.goto(`${BASE}/login`, { waitUntil: 'domcontentloaded' });
      await sleep(1200);
      await page.type('input[type="email"], input[name="email"]', baseline.login.email);
      await page.type('input[type="password"], input[name="password"]', baseline.login.password);
      const navP = page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 20000 }).catch(() => {});
      await page.evaluate(() => {
        const b = document.querySelector('button[type="submit"]')
          || Array.from(document.querySelectorAll('button')).find((x) => /log|sign/i.test(x.textContent));
        if (b) b.click();
      });
      await navP;
      await sleep(4000);
    }

    // ---- navigate to the panel ----
    if (baseline.route) {
      await page.evaluate((p) => {
        window.history.pushState({}, '', p);
        window.dispatchEvent(new PopStateEvent('popstate'));
      }, baseline.route);
      await sleep(3000);
    }
    for (const step of baseline.navigation || []) {
      if (step.action === 'wait') await sleep(step.wait_ms || 1000);
      else if (step.action === 'click') {
        await page.evaluate((sel) => { const el = document.querySelector(sel); if (el) el.click(); }, step.selector);
        await sleep(step.wait_ms || 1500);
      } else if (step.action === 'js_eval') {
        await page.evaluate((s) => { /* eslint-disable no-eval */ (0, eval)(s); }, step.script);
        await sleep(step.wait_ms || 1500);
      }
    }

    // select-partner (optional) -- the AdvisorIntelligence firm switch
    if (baseline.login && baseline.login.select_partner) {
      await page.evaluate((partner) => {
        const sel = Array.from(document.querySelectorAll('select')).find((s) =>
          Array.from(s.options).some((o) => o.value === partner));
        if (sel) { sel.value = partner; sel.dispatchEvent(new Event('change', { bubbles: true })); }
      }, baseline.login.select_partner);
      await sleep(5000);
    }

    // ---- readiness wait: poll until the SPA has rendered substantial content,
    // capped, so a cold-start render race does not produce false "missing"
    // observations. A generic settle signal -- not node-specific (a check for a
    // specific node could mask a real structural emptiness).
    {
      const deadline = Date.now() + 25000;
      let ready = false;
      while (Date.now() < deadline) {
        const s = await page.evaluate(() => ({
          complete: document.readyState === 'complete',
          textLen: (document.body && document.body.innerText || '').length,
          svgCount: document.querySelectorAll('svg').length,
        }));
        if (s.complete && s.textLen > 400 && s.svgCount > 0) { ready = true; break; }
        await sleep(800);
      }
      results.readiness = ready ? 'settled' : 'timeout';
      await sleep(2500);
    }

    // ---- data-bearing node checks ----
    for (const node of baseline.data_bearing_nodes || []) {
      try {
        const obs = await page.evaluate((n, emptyText) => {
          const els = Array.from(document.querySelectorAll(n.selector));
          if (els.length === 0) return { observed: 'missing', detail: 'selector matched nothing' };
          if (n.check === 'chart_nonempty') {
            // a rendered chart carries data elements (recharts bars/dots, svg paths)
            const dataEls = els.flatMap((e) => Array.from(
              e.querySelectorAll('svg path, svg rect, svg circle, .recharts-bar-rectangle, .recharts-dot, canvas')));
            return dataEls.length > 0
              ? { observed: 'non_empty', detail: `${dataEls.length} chart data element(s)` }
              : { observed: 'empty', detail: 'chart container has no data elements' };
          }
          // visible_nonempty: visible + non-placeholder text
          const visible = els.find((e) => {
            const r = e.getBoundingClientRect();
            return r.width > 0 && r.height > 0;
          });
          if (!visible) return { observed: 'empty', detail: 'matched but not visible' };
          const txt = (visible.innerText || '').trim();
          return emptyText.includes(txt.toLowerCase())
            ? { observed: 'empty', detail: `placeholder text: ${JSON.stringify(txt)}` }
            : { observed: 'non_empty', detail: `text: ${JSON.stringify(txt.slice(0, 60))}` };
        }, node, EMPTY_TEXT);
        results.checks.push({ type: 'data_bearing', name: node.name, ...obs });
      } catch (e) {
        results.checks.push({ type: 'data_bearing', name: node.name, observed: 'error', detail: e.message });
      }
    }

    // ---- scope checks ----
    for (const sc of baseline.scope_checks || []) {
      try {
        const obs = await page.evaluate((s) => {
          const el = document.querySelector(s.selector);
          if (!el) return { observed: 'missing', detail: 'scope selector matched nothing' };
          const txt = (el.innerText || '');
          if (s.expect_contains && !txt.includes(s.expect_contains))
            return { observed: 'scope_drift', detail: `expected text to contain ${JSON.stringify(s.expect_contains)}` };
          if (s.expect_not_contains && txt.includes(s.expect_not_contains))
            return { observed: 'scope_drift', detail: `unexpected text ${JSON.stringify(s.expect_not_contains)} present (scope drift)` };
          return { observed: 'scope_ok', detail: '' };
        }, sc);
        results.checks.push({ type: 'scope', name: sc.name, ...obs });
      } catch (e) {
        results.checks.push({ type: 'scope', name: sc.name, observed: 'error', detail: e.message });
      }
    }
  } catch (e) {
    results.fatal_error = e.message;
  } finally {
    try { await browser.disconnect(); } catch {}
  }
  return results.fatal_error ? 3 : 0;
}

main().then((code) => {
  results.finished_at = new Date().toISOString();
  writeFileSync(OUT_PATH, JSON.stringify(results, null, 2));
  console.log(`[D2-RUNNER] panel=${results.panel} checks=${results.checks.length} ` +
    `errors=${results.console_errors.length} -> ${OUT_PATH}`);
  if (results.fatal_error) console.error(`[D2-RUNNER] FATAL: ${results.fatal_error}`);
  process.exit(code);
}).catch((e) => {
  console.error('[D2-RUNNER] uncaught:', e);
  process.exit(3);
});
