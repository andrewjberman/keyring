// Lift the actual parser and comparator; mutate input blobs in memory only.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';
import { execFileSync } from 'node:child_process';
import ts from '../../../../portal/node_modules/typescript/lib/typescript.js';
const portal = resolve('portal');
const out = resolve('.runtime/codex-seats/3.0.0_SA_CVO~F/r15-gate');
mkdirSync(out, { recursive: true });
const git = (...args) => execFileSync('git', args, { cwd: portal, encoding: 'utf8' });
const path = 'src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts';
const code = readFileSync(resolve(portal, path), 'utf8');
const parserSource = code.slice(code.indexOf('const parse ='), code.indexOf('function varInit('));
const parserJs = new Bun.Transpiler({ loader: 'ts' }).transformSync(parserSource + '\nreturn routesOf;');
const routesOf = new Function('ts', 'GATE_PROP_NAMES', parserJs)(ts, ['requireAdmin', 'requireInternal', 'requireDev', 'allowRenderClaim']);
const start = code.indexOf('const SANCTIONED_ADDITIONS:');
const end = code.indexOf('    const carried = unrelated.filter', start);
const js = new Bun.Transpiler({ loader: 'ts' }).transformSync(code.slice(start, end) + '\nreturn {identicalByte,sanctionedAdditive};');
const comparator = new Function('headLines', 'gateHunks', 'RENDERING', 'ROUTE', 'headRoutesAll', 'routesOf', js);
const hunks = [];
for (const line of git('show', '--format=', 'c29a8b86', '--', 'src/App.tsx').split('\n')) {
  if (line.startsWith('@@')) hunks.push({ plus: [], minus: [] });
  else if (hunks.length && line.startsWith('+') && !line.startsWith('+++')) hunks.at(-1).plus.push(line.slice(1));
  else if (hunks.length && line.startsWith('-') && !line.startsWith('---')) hunks.at(-1).minus.push(line.slice(1));
}
const gateHunks = hunks.filter(h => h.plus.some(p => p.includes('/investor-reporting')));
const app = git('show', '8e6e2e38:src/App.tsx');
const mutate = change => app.split('\n').map(l => l.includes('path="/investor-reporting/print"') ? change(l) : l).join('\n');
const cases = {
  current: app,
  removeInternal: mutate(l => l.replace(' requireInternal', '')),
  adminFalse: mutate(l => l.replace(' requireAdmin', ' requireAdmin={false}')),
  internalFalse: mutate(l => l.replace(' requireInternal', ' requireInternal={false}')),
  unrelatedProp: mutate(l => l.replace(' allowRenderClaim', ' allowRenderClaim data-extra="x"')),
};
const results = [];
for (const [name, value] of Object.entries(cases)) {
  try {
    const counts = comparator(value.split('\n'), gateHunks, 'c29a8b86', '/investor-reporting', routesOf(value), routesOf);
    results.push({ name, ...counts, accepted: counts.identicalByte === 2 && counts.sanctionedAdditive === 1 });
  } catch (e) { results.push({ name, accepted: false, error: String(e) }); }
}
const before = git('show', '7dd3d067:' + path);
const ac7 = source => source.slice(source.indexOf("test('F49-AC7"), source.indexOf('test("F49-AC8'));
if (!ac7(code)) throw Error('F49-AC7 extraction empty');
const result = { pin: git('rev-parse', 'HEAD').trim(), cases: results, ac7ByteEqual: ac7(before).replaceAll('\r', '') === ac7(code).replaceAll('\r', ''), appNetZero: git('diff', '3e2ab8e6', 'ed258014', '--', 'src/App.tsx') === '' };
writeFileSync(resolve(out, 'result.json'), JSON.stringify(result, null, 2));
console.log(JSON.stringify(result, null, 2));
