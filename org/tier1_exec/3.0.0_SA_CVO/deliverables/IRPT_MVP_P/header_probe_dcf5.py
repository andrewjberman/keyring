"""Exact-source component tests; static assets intercepted without a web server."""
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import zipfile

PORTAL = 'dcf5e177f6513612f5e39ce90c016d098cc41aab'
TEST_HOME = 'src/pages/InvestorReporting/__tests__/m-selection'


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    snapshot = Path(tempfile.mkdtemp(prefix='cvo-p-header-dcf5-')).resolve()
    members = ['src', 'package.json', 'tsconfig.json', 'tsconfig.app.json', 'tsconfig.node.json', 'postcss.config.js']
    archive = subprocess.check_output(['git', 'archive', '--format=zip', PORTAL, *members], cwd=root / 'portal')
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for name in bundle.namelist():
            if name.endswith('/'):
                continue
            target = (snapshot / name).resolve()
            assert target.is_relative_to(snapshot)
            target.parent.mkdir(parents=True, exist_ok=True)
            raw = bundle.read(name)
            target.write_bytes(raw)
            hashes[name] = hashlib.sha256(raw).hexdigest()
    subprocess.run(['powershell', '-NoProfile', '-Command',
        f"New-Item -ItemType Junction -Path '{snapshot / 'node_modules'}' -Target '{root / 'portal/node_modules'}' | Out-Null"], check=True)
    (snapshot / 'reviewer.html').write_bytes(here.with_name('header_cases_dcf5.html').read_bytes())
    (snapshot / 'reviewer.mjs').write_bytes(here.with_name('header_cases_dcf5.mjs').read_bytes())
    (snapshot / 'offline-routes.mjs').write_text("""import fs from 'node:fs/promises';
import path from 'node:path';
export async function installOfflineRoutes(page) {
  await page.route('**/*', async route => {
    const url = new URL(route.request().url());
    if (url.origin !== 'https://irpt-review.invalid') return route.abort('blockedbyclient');
    const base = path.resolve('dist');
    const target = path.resolve(base, '.' + decodeURIComponent(url.pathname));
    if (!target.startsWith(base + path.sep)) return route.abort('blockedbyclient');
    try { const body = await fs.readFile(target);
      const contentType = target.endsWith('.html') ? 'text/html' : target.endsWith('.js') ? 'application/javascript' : target.endsWith('.css') ? 'text/css' : 'application/octet-stream';
      await route.fulfill({status:200,body,contentType});
    } catch { await route.fulfill({status:404,body:'offline fixture missing'}); }
  });
}
""", encoding='utf-8')
    (snapshot / 'build-review.mjs').write_text("""import { build } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'node:path';
await build({configFile:false, envDir:false, root:process.cwd(), plugins:[react()],
  resolve:{alias:{'@':path.resolve('src')}},
  build:{outDir:'dist',emptyOutDir:false,rollupOptions:{input:[
    'reviewer.html',
    'src/pages/InvestorReporting/__tests__/m-selection/header-race.html',
    'src/pages/InvestorReporting/__tests__/m-selection/browse-race.html']}}});
""", encoding='utf-8')
    for name in ('header-race', 'browse-race'):
        script = (snapshot / TEST_HOME / (name + '.mjs')).read_text(encoding='utf-8')
        marker = 'await page.goto('
        assert script.count(marker) == 1
        script = "import { installOfflineRoutes } from './offline-routes.mjs'\n" + script
        script = script.replace(marker, 'await installOfflineRoutes(page)\n  ' + marker)
        (snapshot / (name + '.mjs')).write_text(script, encoding='utf-8')
    environment = {k: v for k, v in os.environ.items() if not k.startswith(('VITE_', 'IRPT_'))}
    environment['IRPT_TEST_ORIGIN'] = 'https://irpt-review.invalid'
    evidence = {'portal': PORTAL, 'snapshot': str(snapshot), 'runs': [],
                'source_sha256': {key: value for key, value in hashes.items()
                    if key.startswith(TEST_HOME) or key.endswith(('header/ClientSearch.tsx', 'header/FirmDropdown.tsx', 'InvestorReporting/index.tsx'))},
                'reviewer_sha256': {name: hashlib.sha256(here.with_name(name).read_bytes()).hexdigest()
                    for name in ('header_cases_dcf5.html', 'header_cases_dcf5.mjs')}}
    for label, script in [('isolated_test_bundle', 'build-review.mjs'),
                          ('supplied_header_race', 'header-race.mjs'),
                          ('supplied_browse_race', 'browse-race.mjs'),
                          ('independent_header_controls', 'reviewer.mjs')]:
        result = subprocess.run(['node', script], cwd=snapshot, env=environment,
                                capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=150)
        evidence['runs'].append({'label': label, 'exit_code': result.returncode,
                                'stdout': result.stdout, 'stderr': result.stderr})
        if label == 'isolated_test_bundle' and result.returncode:
            break
    evidence['limits'] = 'Actual components with controlled scope/API fixtures; browser requests fulfilled only from the isolated static test bundle on an invalid synthetic origin, no HTTP server or live API. Not CloudFront, auth, deployed build, live acceptance or Andrew visual smoke.'
    here.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'portal': PORTAL, 'snapshot': str(snapshot), 'runs': evidence['runs'], 'limits': evidence['limits']}, indent=2))
    return int(any(row['exit_code'] for row in evidence['runs']))


if __name__ == '__main__':
    raise SystemExit(main())
