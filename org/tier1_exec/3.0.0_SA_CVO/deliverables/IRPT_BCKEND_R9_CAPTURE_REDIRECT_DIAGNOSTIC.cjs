'use strict';
// CVO L9 read-only diagnostic. Runs actual checked-out capture source with every
// browser, network, prompt and write operation stubbed. No credential is used.
const fs = require('node:fs');
const vm = require('node:vm');
const crypto = require('node:crypto');
const sourcePath = 'infra/aws/ec2/investor-reporting-export/capture-session.cjs';
const bytes = fs.readFileSync(sourcePath);
const origin = 'https://opalinvest.dev';
const check = origin + '/investor-reporting/print';
const foreign = 'https://example.invalid/hop';
const cases = [
  {name: 'same-origin positive', first: [origin], check: [check]},
  {name: 'initial foreign hop returns to portal', first: [origin, foreign, origin], check: [check]},
  {name: 'initial final URL foreign control', first: [origin, foreign], check: [check]},
  {name: 'verification foreign hop returns control', first: [origin], check: [check, foreign, check]},
  {name: 'HTTP 500 refusal control', first: [origin], check: [check], status: 500},
  {name: 'marker absent refusal control', first: [origin], check: [check], marker: 0},
];
async function run(test) {
  let finalUrl = 'about:blank';
  const observed = {name: test.name, navigationCalls: 0, initialChainReads: 0,
    verificationChainReads: 0, writes: 0, success: false, exit: null, errors: '',
    initialHops: test.first, verificationHops: test.check};
  let output = '';
  function requestChain(urls) {
    let previous = null;
    for (const url of urls) {
      const parent = previous;
      previous = {url: () => url, redirectedFrom: () => parent};
    }
    return previous;
  }
  const page = {
    goto: async () => {
      const initial = observed.navigationCalls++ === 0;
      const hops = initial ? test.first : test.check;
      finalUrl = hops[hops.length - 1];
      return {status: () => initial ? 200 : (test.status ?? 200), request: () => {
        if (initial) observed.initialChainReads++; else observed.verificationChainReads++;
        return requestChain(hops);
      }};
    },
    url: () => finalUrl,
    locator: selector => ({count: async () => selector === '[data-print-state]' ? (test.marker ?? 1) : 0}),
  };
  const context = {newPage: async () => page,
    storageState: async () => ({cookies: [], origins: [{origin, localStorage: []}]})};
  const mocks = {
    playwright: {chromium: {launch: async () => ({newContext: async () => context, close: async () => {}})}},
    fs: {mkdirSync() {}, writeFileSync() {observed.writes++;}},
    path: require('node:path'),
    readline: {createInterface: () => ({question: (_question, answer) => answer(''), close() {}})},
  };
  await vm.runInNewContext(bytes.toString('utf8'), {
    require: name => {if (!(name in mocks)) throw new Error('Unexpected module: ' + name); return mocks[name];},
    URL, process: {env: {IRPT_CAPTURE_PORTAL_ORIGIN: origin, IRPT_CAPTURE_INSTANCE_ID: 'i-0167fd745ad906a66'},
      stdin: {}, stdout: {write: value => {output += value;}}, stderr: {write: value => {observed.errors += value;}},
      exit: code => {observed.exit = code;}},
  }, {filename: sourcePath, timeout: 5000});
  observed.success = output.includes('OK: session state captured');
  return observed;
}
(async () => {
  const results = [];
  for (const test of cases) results.push(await run(test));
  console.log(JSON.stringify({sourcePath, diskSha256: crypto.createHash('sha256').update(bytes).digest('hex'),
    boundary: 'Stubbed redirect-chain responses; no real browser, network, files written or credential', results}, null, 2));
  if (!(results[0].success && results[1].success && results[1].initialChainReads === 0
    && results.slice(2).every(result => !result.success && result.writes === 0))) process.exitCode = 1;
})().catch(error => {console.error(error); process.exitCode = 2;});
