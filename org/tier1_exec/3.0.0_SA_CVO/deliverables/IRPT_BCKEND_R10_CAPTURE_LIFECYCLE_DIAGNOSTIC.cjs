'use strict';
// CVO~B: diagnostic, not a repair. No browser, network, credential, or real write.
// Default reads the worktree source. Optional argv[2] reads a git blob (negative control).
// Exit 0 means BOTH residual defects reproduced with the other controls as specified;
// it NEVER means that capture is safe or R101-AC3 passes.
const fs = require('node:fs');
const vm = require('node:vm');
const { EventEmitter } = require('node:events');
const { execFileSync } = require('node:child_process');
const { createHash } = require('node:crypto');
const sourcePath = 'infra/aws/ec2/investor-reporting-export/capture-session.cjs';
const bytes = process.argv[2]
  ? execFileSync('git', ['cat-file', 'blob', process.argv[2]])
  : fs.readFileSync(sourcePath);
const origin = 'https://opalinvest.dev';
const check = origin + '/investor-reporting/print';
const foreign = 'https://example.invalid/hop';

async function run(name, cfg) {
  const out = { name, writes: 0, success: false, prompts: 0, gotoCalls: 0,
    intervalNavigations: 0, intervalChainReads: 0, intervalListeners: 0,
    responseEvents: 0, verificationCalls: 0, verificationChainReads: 0,
    exitCode: null, output: '', errors: '' };
  const page = new EventEmitter();
  const context = new EventEmitter();
  let current = 'about:blank';
  const frame = { url: () => current, parentFrame: () => null };
  page.mainFrame = () => frame;
  page.url = () => current;
  function navigation(hops, phase, status = 200) {
    let previous = null;
    let finalResponse;
    for (let i = 0; i < hops.length; i++) {
      const before = previous;
      const req = { url: () => hops[i], redirectedFrom: () => before,
        isNavigationRequest: () => true, frame: () => frame };
      previous = req;
      const resp = { status: () => i === hops.length - 1 ? status : 302,
        url: () => hops[i], frame: () => frame, request: () => {
          if (phase === 'interval') out.intervalChainReads++;
          if (phase === 'verification') out.verificationChainReads++;
          return req;
        } };
      current = hops[i];
      page.emit('request', req); context.emit('request', req);
      page.emit('response', resp); context.emit('response', resp);
      out.responseEvents++;
      finalResponse = resp;
    }
    page.emit('framenavigated', frame);
    return finalResponse;
  }
  page.goto = async () => {
    out.gotoCalls++;
    if (out.gotoCalls === 1) return navigation(cfg.initial || [origin], 'initial');
    out.verificationCalls++;
    const hops = cfg.verification === 'always-foreign' ||
      (cfg.verification === 'first-foreign' && out.verificationCalls === 1)
      ? [check, foreign, check] : [check];
    return navigation(hops, 'verification', cfg.status || 200);
  };
  page.locator = (selector) => ({ count: async () =>
    String(selector).includes('data-print-state') ? 1 : 0 });
  context.newPage = async () => page;
  context.storageState = async () => ({ cookies: [], origins: [] });
  const mocks = {
    playwright: { chromium: { launch: async () => ({ newContext: async () => context, close: async () => {} }) } },
    fs: { mkdirSync() {}, writeFileSync() { out.writes++; } },
    path: require('node:path'),
    readline: { createInterface: () => ({ close() {}, question: (_q, cb) => {
      out.prompts++;
      if (out.prompts > 6) throw new Error('DIAGNOSTIC: runaway prompts');
      // Model the documented human-controlled SAME tab during ask(), BEFORE ENTER.
      // Only the middle hop varies in the single-difference good/bad interval pair.
      if (out.prompts === 1 && cfg.interval) {
        out.intervalListeners = page.eventNames().reduce((n, e) => n + page.listenerCount(e), 0)
          + context.eventNames().reduce((n, e) => n + context.listenerCount(e), 0);
        out.intervalNavigations++;
        navigation(cfg.interval, 'interval');
      }
      cb('');
    } }) },
  };
  await vm.runInNewContext(bytes.toString('utf8'), {
    require: (name) => { if (!(name in mocks)) throw new Error('Unexpected module: ' + name); return mocks[name]; },
    URL, console: { log() {} },
    process: { env: { IRPT_CAPTURE_PORTAL_ORIGIN: origin, IRPT_CAPTURE_INSTANCE_ID: 'i-0167fd745ad906a66' },
      stdin: {}, stdout: { write: (s) => { out.output += s; } },
      stderr: { write: (s) => { out.errors += s; } }, exit: (c) => { out.exitCode = c; } },
  }, { filename: sourcePath });
  out.success = out.output.includes('OK: session state captured');
  return out;
}

(async () => {
  const cases = [
    ['same-origin interval positive', { interval: [origin, origin, origin] }],
    ['interactive foreign hop returns to portal', { interval: [origin, foreign, origin] }],
    ['initial foreign hop control', { initial: [origin, foreign, origin] }],
    ['verification foreign every attempt control', { verification: 'always-foreign' }],
    ['verification foreign first attempt then clean', { verification: 'first-foreign' }],
    ['HTTP 500 control', { status: 500 }],
  ];
  const results = [];
  for (const [name, cfg] of cases) results.push(await run(name, cfg));
  const accepted = (r) => r.writes === 1 && r.success;
  const refused = (r) => r.writes === 0 && !r.success;
  const reproduced = accepted(results[0]) && accepted(results[1]) &&
    results[1].intervalNavigations === 1 && results[1].intervalChainReads === 0 &&
    refused(results[2]) && refused(results[3]) && accepted(results[4]) &&
    results[4].verificationCalls === 2 && refused(results[5]);
  process.stdout.write(JSON.stringify({ source: process.argv[2] || sourcePath,
    sourceSha256: createHash('sha256').update(bytes).digest('hex'),
    exitZeroMeans: 'residual defects reproduced, NOT repair acceptance', reproduced, results }, null, 2) + '\n');
  process.exitCode = reproduced ? 0 : 1;
})().catch((error) => { console.error(error); process.exitCode = 2; });
