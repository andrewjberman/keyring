// Replay the real downstream generator, intercepting every write. Only its wire-map input varies.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';
const portal = resolve('portal');
const out = resolve('.runtime/codex-seats/3.0.0_SA_CVO~F/r15-consumer');
mkdirSync(out, { recursive: true });
const path = 'src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts';
const file = resolve(portal, path);
const git = (...args) => execFileSync('git', args, { cwd: portal, encoding: 'utf8' });
const original = git('show', '8e6e2e38:' + path);
let source = original.replace("import { readFileSync, writeFileSync } from 'node:fs'", 'const readFileSync = globalThis.__cvoRead; const writeFileSync = (p,s)=>globalThis.__cvoWrites.set(p,s);');
if (source === original) throw Error('No filesystem interception');
source = source.replaceAll('import.meta.url', JSON.stringify(pathToFileURL(file).href));
const wirePath = 'src/pages/InvestorReporting/fixtures/smoke/fe-s-13-wire.json';
const results = [];
for (const pin of ['7dd3d067', '8e6e2e38']) {
  const wire = git('show', pin + ':' + wirePath);
  globalThis.__cvoWrites = new Map();
  globalThis.__cvoRead = (p, encoding) => resolve(p) === resolve(portal, wirePath) ? wire : readFileSync(p, encoding);
  const script = resolve(out, pin + '.ts');
  writeFileSync(script, source);
  let error = null;
  try { await import(pathToFileURL(script).href); } catch (e) { error = String(e); }
  results.push({ wireInputPin: pin, generatorPin: '8e6e2e38', generatedWrites: globalThis.__cvoWrites.size, error, outputNames: [...globalThis.__cvoWrites.keys()] });
}
writeFileSync(resolve(out, 'result.json'), JSON.stringify(results, null, 2));
console.log(JSON.stringify(results, null, 2));
