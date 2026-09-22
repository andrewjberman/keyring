// Independent real subprocess controls; run with Bun from the workspace root.
import { mkdirSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { spawnSync } from 'node:child_process';
const portal = resolve('portal');
const scratch = resolve('.runtime/codex-seats/3.0.0_SA_CVO~F/r15-checker');
mkdirSync(scratch, { recursive: true });
const bun = 'C:/Users/AndrewBerman/.bun/bin/bun';
const fixture = (name, content) => {
  const path = resolve(scratch, name).replaceAll('\\', '/');
  writeFileSync(path, content);
  return path;
};
const allowed = fixture('allowed.test.ts', "import {test,expect} from 'bun:test'; test('CVO-KNOWN',()=>expect(1).toBe(2));\n");
const broken = fixture('broken.test.ts', "throw new Error('CVO unhandled module-load error');\n");
const crash = fixture('crash.mjs', 'process.exit(7);\n');
const empty = fixture('empty.mjs', 'process.exit(0);\n');
const names = ['passing', 'unexpected-failure', 'allowed-failure', 'slow'];
const base = './src/pages/InvestorReporting/__tests__/fe-s-90/fixtures/';
const cases = names.map(name => ({ name, args: [...(name === 'slow' ? ['timeout', '3'] : []), bun, 'test', base + name + '.fixture.ts', ...(name === 'allowed-failure' ? ['--allow', 'fe-s-90-known-allowed-failure'] : [])] }));
cases.push({ name: 'crash-no-summary', args: [bun, crash] });
cases.push({ name: 'empty-success', args: [bun, empty] });
cases.push({ name: 'allowed-plus-unhandled-module-error', args: [bun, 'test', allowed, broken, '--allow', 'CVO-KNOWN'] });
const results = [];
for (const entry of cases) {
  const r = spawnSync(bun, ['scripts/suite-complete-check.mjs', ...entry.args], { cwd: portal, encoding: 'utf8', timeout: 60000 });
  const row = { name: entry.name, args: entry.args, status: r.status, error: String(r.error ?? ''), stdout: r.stdout, stderr: r.stderr };
  results.push(row);
  console.log(JSON.stringify(row));
}
const direct = spawnSync(bun, ['test', allowed, broken], { cwd: portal, encoding: 'utf8', timeout: 30000 });
results.push({ name: 'direct-allowed-plus-unhandled-module-error', status: direct.status, stdout: direct.stdout, stderr: direct.stderr });
writeFileSync(resolve(scratch, 'result.json'), JSON.stringify(results, null, 2));
