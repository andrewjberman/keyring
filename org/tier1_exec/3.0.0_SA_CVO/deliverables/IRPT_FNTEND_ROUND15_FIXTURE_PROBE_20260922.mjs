// Read-only strict-key census and consumer binding checks at the pinned portal vintage.
import { readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { execFileSync } from 'node:child_process';
const portal = resolve('portal');
const out = resolve('.runtime/codex-seats/3.0.0_SA_CVO~F/r15-fixture');
mkdirSync(out, { recursive: true });
const git = (...args) => execFileSync('git', args, { cwd: portal, encoding: 'utf8', maxBuffer: 20 * 1024 * 1024 });
const src = git('show', '8e6e2e38:scripts/ui-smoke.mjs');
const from = src.indexOf('const routeKeyCandidates = routeKeys => {');
const to = src.indexOf('// --fail <url-substring>', from);
if (from < 0 || to < 0) throw Error('Classifier boundary missing');
const fn = new Function('readFileSync', src.slice(from, to) + '\nreturn checkKeyValidity;')(p => readFileSync(resolve(portal, p), 'utf8'));
const files = git('ls-tree', '-r', '--name-only', '8e6e2e38', '--', 'src/pages/InvestorReporting').trim().split('\n').filter(p => p.endsWith('.json'));
const maps = [];
for (const file of files) {
  const data = JSON.parse(git('show', '8e6e2e38:' + file));
  const keys = Object.keys(data).filter(k => k.startsWith('/api/'));
  if (!keys.length) continue;
  const result = fn(keys, file);
  maps.push({ file, ...result, invalid: keys.filter(key => fn([key], file).valid === 0) });
}
const names = ['fixtures/smoke/reporting-answer-bearing.json', '__tests__/fe-s-84/fixtures/reporting-qualified.json'];
const bindings = names.map(name => {
  const file = 'src/pages/InvestorReporting/' + name;
  const map = JSON.parse(git('show', '8e6e2e38:' + file));
  const resolution = Object.entries(map).find(([key]) => key.endsWith('/directory/resolve'))[1];
  const fp = resolution.data.permitted_account_set_fingerprint;
  return { file, fingerprint: fp, performanceKeyMatches: Object.keys(map).some(k => k.endsWith('/performance/' + fp)), holdingsKeyMatches: Object.keys(map).some(k => k.endsWith('/holdings/' + fp)) };
});
const result = { pin: '8e6e2e38cc299c4415d42b0fe627edc50ec35e1b', maps, bindings, strictClassifierUnchanged: git('diff', '7dd3d067', '8e6e2e38', '--', 'scripts/ui-smoke.mjs') === '', defaultUnchanged: git('diff', '7dd3d067', '8e6e2e38', '--', 'src/pages/InvestorReporting/fixtures/smoke/default.json') === '' };
writeFileSync(resolve(out, 'result.json'), JSON.stringify(result, null, 2));
console.log(JSON.stringify({ maps: maps.length, mapsWithInvalidKeys: maps.filter(x => x.invalid.length).length, invalidKeys: maps.reduce((n, x) => n + x.invalid.length, 0), bindings, strictClassifierUnchanged: result.strictClassifierUnchanged, defaultUnchanged: result.defaultUnchanged }, null, 2));
