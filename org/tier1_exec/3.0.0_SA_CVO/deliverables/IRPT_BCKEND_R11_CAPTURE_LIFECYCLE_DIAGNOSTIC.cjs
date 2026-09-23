'use strict';
// CVO~B review diagnostic ONLY. VM mocks; no browser/network/credential/real writes.
// Optional argv[2] selects a git blob. Exit 0 means the TWO defects reproduced,
// NOT repair acceptance. All source bytes and mock cases are printed by hash/name.
const fs = require('node:fs');
const vm = require('node:vm');
const { EventEmitter } = require('node:events');
const { execFileSync } = require('node:child_process');
const { createHash } = require('node:crypto');
const sourcePath = 'infra/aws/ec2/investor-reporting-export/capture-session.cjs';
const bytes = process.argv[2] ? execFileSync('git', ['cat-file', 'blob', process.argv[2]]) : fs.readFileSync(sourcePath);
const origin = 'https://opalinvest.dev';
const check = origin + '/investor-reporting/print';
const foreign = 'https://example.invalid/resource';

async function run(name, cfg = {}) {
  const out = { name, writes: 0, success: false, exitCode: null, prompts: 0,
    verificationCalls: 0, storageCalls: 0, eventsDuringStorage: 0,
    nonNavigationResponses: 0, output: '', errors: '' };
  const page = new EventEmitter();
  const context = new EventEmitter();
  let current = 'about:blank';
  const frame = { url: () => current, parentFrame: () => null };
  page.mainFrame = () => frame;
  page.url = () => current;
  function navigation(hops, status = 200) {
    let previous = null;
    let response;
    for (const url of hops) {
      const before = previous;
      const request = { url: () => url, redirectedFrom: () => before,
        isNavigationRequest: () => true, frame: () => frame };
      previous = request;
      response = { url: () => url, status: () => status, frame: () => frame, request: () => request };
      current = url;
      page.emit('request', request); context.emit('request', request);
      page.emit('response', response); context.emit('response', response);
    }
    page.emit('framenavigated', frame);
    return response;
  }
  let gotoCalls = 0;
  page.goto = async () => {
    if (++gotoCalls === 1) return navigation([origin]);
    out.verificationCalls++;
    if (out.verificationCalls === 1 && cfg.firstFailure === 'timeout') throw new Error('Timeout 60000ms exceeded');
    if (out.verificationCalls === 1 && cfg.firstFailure === 'generic') throw new Error('net::ERR_CERT_AUTHORITY_INVALID');
    const status = out.verificationCalls === 1 ? (cfg.firstStatus || 200) : 200;
    return navigation([check], status);
  };
  page.locator = (selector) => ({ count: async () => {
    if (String(selector).includes('data-print-state')) return out.verificationCalls === 1 && cfg.missingMarker ? 0 : 1;
    return out.verificationCalls === 1 && cfg.password ? 1 : 0;
  } });
  context.newPage = async () => page;
  context.storageState = async () => {
    out.storageCalls++;
    // Browser events can run while awaiting the storageState protocol response.
    // The pair changes ONLY the middle origin in this navigation chain.
    await Promise.resolve();
    if (cfg.storageHop) {
      navigation([origin, cfg.storageHop, origin]);
      out.eventsDuringStorage++;
    }
    return { cookies: [], origins: [] };
  };
  const mocks = {
    playwright: { chromium: { launch: async () => ({ newContext: async () => context, close: async () => {} }) } },
    fs: { mkdirSync() {}, writeFileSync() { out.writes++; } },
    path: require('node:path'),
    readline: { createInterface: () => ({ close() {}, question: (_q, cb) => {
      out.prompts++;
      if (out.prompts > 6) throw new Error('DIAGNOSTIC runaway prompts');
      if (out.prompts === 1 && cfg.resourceUrl) {
        // A fetch/image/script belongs to the main frame but is NOT a navigation.
        // Same-origin/foreign resource pair differs ONLY by resource URL origin.
        const request = { url: () => cfg.resourceUrl, frame: () => frame,
          isNavigationRequest: () => false, redirectedFrom: () => null };
        const response = { url: request.url, frame: () => frame, request: () => request, status: () => 200 };
        page.emit('request', request); context.emit('request', request);
        page.emit('response', response); context.emit('response', response);
        out.nonNavigationResponses++;
      }
      if (out.prompts === 1 && cfg.intervalForeign) navigation([origin, foreign, origin]);
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
    ['storage wait same-origin positive', { storageHop: origin }],
    ['storage wait foreign hop then portal', { storageHop: foreign }],
    ['non-navigation same-origin response positive', { resourceUrl: origin + '/resource' }],
    ['non-navigation foreign response', { resourceUrl: foreign }],
    ['interactive foreign navigation refusal control', { intervalForeign: true }],
    ['same-origin HTTP 500 then clean', { firstStatus: 500 }],
    ['same-origin timeout then clean', { firstFailure: 'timeout' }],
    ['same-origin missing marker then clean', { missingMarker: true }],
    ['same-origin HTTP 404 then clean', { firstStatus: 404 }],
    ['same-origin non-timeout navigation error then clean', { firstFailure: 'generic' }],
    ['same-origin password screen then clean', { password: true }],
  ];
  const results = [];
  for (const [name, cfg] of cases) results.push(await run(name, cfg));
  const accepts = (r) => r.writes === 1 && r.success && r.exitCode === null;
  const refuses = (r) => r.writes === 0 && !r.success && r.exitCode === 1;
  const reproduced = accepts(results[0]) && accepts(results[1]) && results[1].eventsDuringStorage === 1 &&
    accepts(results[2]) && refuses(results[3]) && results[3].nonNavigationResponses === 1 && refuses(results[4]);
  process.stdout.write(JSON.stringify({ source: process.argv[2] || sourcePath,
    sourceSha256: createHash('sha256').update(bytes).digest('hex'),
    exitZeroMeans: 'two defects reproduced, NOT repair acceptance', reproduced, results }, null, 2) + '\n');
  process.exitCode = reproduced ? 0 : 1;
})().catch((e) => { console.error(e); process.exitCode = 2; });
