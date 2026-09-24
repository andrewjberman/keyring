'use strict';
// CVO read-only diagnostic: execute the actual capture source in a fully stubbed VM.
// No browser, credentials, network, or session file is created.
const fs = require('node:fs');
const vm = require('node:vm');
const crypto = require('node:crypto');
const sourcePath = 'infra/aws/ec2/investor-reporting-export/capture-session.cjs';
const source = fs.readFileSync(sourcePath, 'utf8');
async function probe(label, origin, passwordCount, responseStatus) {
  const calls = { navigations: [], writes: 0, prompts: 0, output: '', errors: '' };
  const page = {
    goto: async url => { calls.navigations.push(url); return { status: () => responseStatus }; },
    locator: () => ({ count: async () => passwordCount }),
  };
  const context = { newPage: async () => page, storageState: async () => { calls.writes++; } };
  const mocks = {
    playwright: { chromium: { launch: async () => ({ newContext: async () => context, close: async () => {} }) } },
    fs: { mkdirSync: () => {} },
    path: require('node:path'),
    readline: { createInterface: () => ({ close: () => {}, question: (_q, cb) => {
      calls.prompts++;
      if (calls.prompts > 1) throw new Error('TEST STOP: still waiting, no capture');
      cb('');
    } }) },
  };
  const sandbox = {
    require: name => { if (!(name in mocks)) throw new Error(`Unexpected module ${name}`); return mocks[name]; },
    URL,
    process: {
      env: { IRPT_CAPTURE_PORTAL_ORIGIN: origin }, stdin: {},
      stdout: { write: text => { calls.output += text; } },
      stderr: { write: text => { calls.errors += text; } },
      exit: code => { calls.exitCode = code; },
    },
  };
  await vm.runInNewContext(source, sandbox, { filename: sourcePath });
  return { label, responseStatus, passwordCount, writes: calls.writes,
    navigations: calls.navigations, literalInstancePlaceholder: calls.output.includes('--target <instance-id>'),
    captureSuccessPrinted: calls.output.includes('OK: session state captured'), errors: calls.errors.trim() };
}
(async () => {
  console.log(JSON.stringify({ sourcePath, sourceSha256: crypto.createHash('sha256').update(source).digest('hex'),
    environment: 'VM mocks only; no network, real browser, host action or filesystem write',
    results: await Promise.all([
      probe('negative: sign-in page', 'https://opalinvest.dev', 1, 200),
      probe('counterexample: HTTP 500 without password input', 'https://opalinvest.dev', 0, 500),
      probe('counterexample: arbitrary non-portal origin accepted', 'https://example.invalid', 0, 200),
    ]) }, null, 2));
})().catch(error => { console.error(error); process.exitCode = 1; });
