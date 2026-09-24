"""Reconstruct exact pair and verify actual directory selection refusal locally."""
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

BACKEND = '960f5f2a4501eff2670bcd0b5951926836093447'
PORTAL = 'c09fea54e9f4613d44b874724e93b79c443f8cc8'
PACKAGE = 'infra/aws/lambda/investor-reporting'


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    snapshot = Path(tempfile.mkdtemp(prefix='cvo-p-selection-960f-')).resolve()
    paths = [PACKAGE + '/' + name for name in ('directory', '_scope', '_authz', '_ids', '_keys', '_contracts')]
    paths += ['docs/contracts/investor-reporting/v1', 'data/firm_registry.json']
    for repo, pin, members in ((root, BACKEND, paths), (root / 'portal', PORTAL, ['src', 'package.json'])):
        archive = subprocess.check_output(['git', 'archive', '--format=zip', pin, *members], cwd=repo)
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            for name in bundle.namelist():
                if name.endswith('/'):
                    continue
                target = (snapshot / name).resolve()
                assert target.is_relative_to(snapshot)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(bundle.read(name))
    subprocess.run(['powershell', '-NoProfile', '-Command',
        f"New-Item -ItemType Junction -Path '{snapshot / 'node_modules'}' -Target '{root / 'portal/node_modules'}' | Out-Null"], check=True)
    assertions = {}
    for name, target in [('selection_wire_cases_960f.py', PACKAGE + '/_contracts/tests/test_reviewer_selection.py'),
                         ('selection_wire_cases_960f.test.ts', 'reviewer-selection.test.ts')]:
        raw = here.with_name(name).read_bytes()
        assertions[name] = hashlib.sha256(raw).hexdigest()
        (snapshot / target).write_bytes(raw)
    environment = {k: v for k, v in os.environ.items() if not k.startswith('IRPT_') and k != 'PYTHONPATH'}
    environment.update(PYTEST_DISABLE_PLUGIN_AUTOLOAD='1', AWS_EC2_METADATA_DISABLED='true',
                       IRPT_CONTRACTS_DIR=str(snapshot / 'docs/contracts/investor-reporting/v1'))
    evidence = {'backend': BACKEND, 'portal': PORTAL, 'snapshot': str(snapshot), 'assertions': assertions, 'runs': []}
    commands = [
        ('independent_backend_selection', [sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider',
                                           PACKAGE + '/_contracts/tests/test_reviewer_selection.py']),
        ('supplied_backend_selection', [sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider',
                                        PACKAGE + '/_contracts/tests/test_selection_contract.py',
                                        PACKAGE + '/directory/tests/test_selection_entry.py']),
        ('independent_fresh_selection_parser', ['bun', 'test', 'reviewer-selection.test.ts']),
        ('supplied_portal_selection', ['bun', 'test', 'src/pages/InvestorReporting/__tests__/mvp-selection/selection.test.ts']),
    ]
    for label, command in commands:
        result = subprocess.run(command, cwd=snapshot, env=environment, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=90)
        evidence['runs'].append({'label': label, 'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
    capture = snapshot / 'actual-selection-refusal.json'
    if capture.exists():
        raw = capture.read_bytes()
        here.with_name('selection_actual_refusal_960f.json').write_bytes(raw)
        evidence['capture_sha256'] = hashlib.sha256(raw).hexdigest()
    evidence['limits'] = 'Actual guarded directory Entry with supplied synthetic loaders/store and independent controls. No network, deployed package, real browser, vendor, export or full-product proof.'
    here.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(evidence, indent=2))
    return int(any(row['exit_code'] for row in evidence['runs']) or not capture.exists())


if __name__ == '__main__':
    raise SystemExit(main())
