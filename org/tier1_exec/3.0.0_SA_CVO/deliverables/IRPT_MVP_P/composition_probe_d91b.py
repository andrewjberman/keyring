"""Rebuild exact source-02 pair for independent schema/storage/client review."""
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

BACKEND = 'd91b2bdd10fe05a0e241ccbfb8f6d7f1b35a872c'
PORTAL = '7411ada3'
PACKAGE = 'infra/aws/lambda/investor-reporting'


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    snapshot = Path(tempfile.mkdtemp(prefix='cvo-p-composition-d91b-')).resolve()
    portal_pin = subprocess.check_output(['git', 'rev-parse', PORTAL], cwd=root / 'portal', text=True).strip()
    paths = [PACKAGE + '/' + name for name in ('ops', 'intake', 'reports', 'ycharts/generate', '_scope', '_authz', '_ids', '_keys', '_contracts')]
    paths += ['docs/contracts/investor-reporting/v1', 'data/firm_registry.json']
    hashes = {}
    for repo, pin, members in ((root, BACKEND, paths), (root / 'portal', portal_pin, ['src', 'package.json', 'tsconfig.app.json', 'tsconfig.json', 'tsconfig.node.json'])):
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
    for name, target in [('composition_cases_d91b.py', PACKAGE + '/_contracts/test_reviewer_composition.py'),
                         ('composition_cases_d91b.test.ts', 'reviewer-composition.test.ts')]:
        raw = here.with_name(name).read_bytes()
        assertions[name] = hashlib.sha256(raw).hexdigest()
        (snapshot / target).write_bytes(raw)
    environment = {k: v for k, v in os.environ.items() if not k.startswith('IRPT_') and k != 'PYTHONPATH'}
    environment.update(PYTEST_DISABLE_PLUGIN_AUTOLOAD='1', AWS_EC2_METADATA_DISABLED='true',
                       IRPT_CONTRACTS_DIR=str(snapshot / 'docs/contracts/investor-reporting/v1'),
                       IRPT_WRITE_COMPOSITION_EXAMPLE=str(snapshot / 'actual-composition.json'))
    evidence = {'backend': BACKEND, 'portal': portal_pin, 'snapshot': str(snapshot), 'assertions': assertions, 'runs': []}

    def run(label, command):
        result = subprocess.run(command, cwd=snapshot, env=environment, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=120)
        evidence['runs'].append({'label': label, 'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})

    run('supplied_backend', [sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider', PACKAGE + '/_contracts/test_request_composition.py'])
    run('independent_backend', [sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider', PACKAGE + '/_contracts/test_reviewer_composition.py'])
    run('supplied_portal', ['bun', 'test', 'src/pages/InvestorReporting/__tests__/submission-request.test.ts'])
    capture = snapshot / 'actual-composition.json'
    if capture.exists():
        run('independent_portal', ['bun', 'test', 'reviewer-composition.test.ts'])
        raw = capture.read_bytes()
        here.with_name('composition_actual_d91b.json').write_bytes(raw)
        evidence['capture_sha256'] = hashlib.sha256(raw).hexdigest()
        evidence['capture_equals_committed_example'] = json.loads(raw) == json.loads((snapshot / 'docs/contracts/investor-reporting/v1/examples/RequestComposition.synthetic.json').read_bytes())
    wire = snapshot / 'src/pages/InvestorReporting/contracts/wire'
    before = {p.name: p.read_bytes().replace(b'\r\n', b'\n') for p in wire.glob('*.ts')}
    (snapshot / 'regenerate-wire.ts').write_text(
        "import { generate } from './src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire'; console.log(JSON.stringify(generate()));\n", encoding='utf-8')
    run('generator_reproduction', ['bun', 'run', 'regenerate-wire.ts'])
    run('portal_app_typescript', ['bun', 'x', '--no-install', 'tsc', '-p', 'tsconfig.app.json', '--noEmit'])
    after = {p.name: p.read_bytes().replace(b'\r\n', b'\n') for p in wire.glob('*.ts')}
    evidence['generated_wire_differences'] = [name for name in sorted(set(before) | set(after)) if before.get(name) != after.get(name)]
    evidence['source_sha256'] = {name: sha for name, sha in hashes.items() if name.endswith(('request_composition.py', 'RequestComposition.schema.json', 'AnalysisSubmissionRequest.schema.json', 'submission-request.ts'))}
    evidence['limits'] = 'Local actual repository with synthetic source descriptors, storage/time/auth doubles and modeled client transport. No maintained authority, actual worker acceptance/UI, deployed package, live provider, vendor text limit, rendering or full-product proof.'
    here.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(evidence, indent=2))
    return int(any(row['exit_code'] for row in evidence['runs']) or bool(evidence['generated_wire_differences']) or not capture.exists())


if __name__ == '__main__':
    raise SystemExit(main())
