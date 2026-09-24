"""Baseline actual client -> guarded producer -> actual consumer, offline only."""
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

BACKEND = 'cd8d11825424e45fe82f1e78df0396904c0b9ae0'
PORTAL = 'e83ebbfe4f83228f42925b24f77f43e6b6d2a037'
PACKAGE = 'infra/aws/lambda/investor-reporting'


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    snapshot = Path(tempfile.mkdtemp(prefix='cvo-p-bootstrap-cd8-')).resolve()
    paths = [PACKAGE + '/' + name for name in ('directory', '_authz', '_scope', '_ids', '_keys', '_contracts')]
    paths += ['docs/contracts/investor-reporting/v1', 'data/firm_registry.json']
    hashes = {}
    for repo, pin, members in ((root, BACKEND, paths), (root / 'portal', PORTAL, ['src', 'package.json'])):
        archive = subprocess.check_output(['git', 'archive', '--format=zip', pin, *members], cwd=repo)
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
    assertions = {}
    for name, target in [('bootstrap_cases_cd8.py', PACKAGE + '/_contracts/tests/test_reviewer_bootstrap.py'),
                         ('bootstrap_cases_cd8.test.ts', 'reviewer-bootstrap.test.ts')]:
        raw = here.with_name(name).read_bytes()
        assertions[name] = hashlib.sha256(raw).hexdigest()
        (snapshot / target).write_bytes(raw)
    (snapshot / 'capture-bootstrap.ts').write_text("""import { writeFileSync } from 'node:fs';
import { LiveClient } from './src/api/endpoints/investor-reporting';
let capture: unknown;
const api = new LiveClient({ transport: { async request<T>(url: string, init: any): Promise<T> {
 capture = { url, ...init }; throw new Error('offline capture sentinel');
} }, telemetrySink: () => undefined });
await api.resolveScope({ tenant: 'bootstrap', requested: { firmId: null, clientId: null, relationshipId: null, accountIds: [] } }).catch(() => undefined);
if (!capture) throw new Error('bootstrap transport was never called');
writeFileSync('bootstrap-request.json', JSON.stringify(capture, null, 2) + '\\n');
""", encoding='utf-8')
    environment = {k: v for k, v in os.environ.items() if not k.startswith('IRPT_') and k != 'PYTHONPATH'}
    environment.update(PYTEST_DISABLE_PLUGIN_AUTOLOAD='1', AWS_EC2_METADATA_DISABLED='true',
                       IRPT_CONTRACTS_DIR=str(snapshot / 'docs/contracts/investor-reporting/v1'))
    evidence = {'backend': BACKEND, 'portal': PORTAL, 'snapshot': str(snapshot), 'assertions': assertions, 'runs': []}
    for label, command in [
        ('real_client_request_capture', ['bun', 'run', 'capture-bootstrap.ts']),
        ('real_guarded_producer_assertions', [sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider', PACKAGE + '/_contracts/tests/test_reviewer_bootstrap.py']),
        ('real_frontend_consumer_assertions', ['bun', 'test', 'reviewer-bootstrap.test.ts'])]:
        result = subprocess.run(command, cwd=snapshot, env=environment, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=90)
        evidence['runs'].append({'label': label, 'exit_code': result.returncode,
                                'stdout': result.stdout, 'stderr': result.stderr})
    for name in ('bootstrap-request.json', 'bootstrap-actual.json'):
        target = snapshot / name
        if target.exists():
            raw = target.read_bytes()
            here.with_name(name.replace('.json', '_cd8.json')).write_bytes(raw)
            evidence[name + '_sha256'] = hashlib.sha256(raw).hexdigest()
    evidence['source_sha256'] = {name: sha for name, sha in hashes.items() if name.endswith((
        'directory/entry.py', 'directory/handler.py', 'contracts/envelope.ts', 'contracts/adapt.ts',
        'InvestorReporting/index.tsx', 'endpoints/investor-reporting.ts', 'ResolvedScope.schema.json'))}
    evidence['limits'] = 'Actual modules, actual client request, existing verified-principal fixtures; only external directory/ownership/policy dependencies controlled. Backend is prior exact source baseline, not a live deployed-hash assertion. No HTTP network, real UI, provisioning or live-cause closure.'
    here.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(evidence, indent=2))
    return int(any(row['exit_code'] for row in evidence['runs']))


if __name__ == '__main__':
    raise SystemExit(main())
