"""Exact-pair focused consumer/access review; no preview or publication operation."""
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import zipfile

BACKEND = 'cd8d11825424e45fe82f1e78df0396904c0b9ae0'
PORTAL = 'a538217980cdb5d15dc67cdcc98794baeb5e2517'
REMOTE_DEV = 'b3d5f59b4534eb653105f9bedc9e178384111c9f'


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    snapshot = Path(tempfile.mkdtemp(prefix='cvo-p-final-a538-')).resolve()
    backend = snapshot / 'backend'
    portal = snapshot / 'portal'
    # The backend census reads committed blobs through Git; no full checkout needed.
    subprocess.run(['git', 'worktree', 'add', '--detach', '--no-checkout', str(backend), BACKEND], cwd=root, check=True)
    archive = subprocess.check_output(['git', 'archive', '--format=zip', BACKEND,
                                       'docs/contracts/investor-reporting/v1'], cwd=root)
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for name in bundle.namelist():
            if name.endswith('/'):
                continue
            target = (backend / name).resolve()
            assert target.is_relative_to(backend)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(bundle.read(name))
    subprocess.run(['git', 'worktree', 'add', '--detach', str(portal), PORTAL], cwd=root / 'portal', check=True)
    subprocess.run(['powershell', '-NoProfile', '-Command',
        f"New-Item -ItemType Junction -Path '{portal / 'node_modules'}' -Target '{root / 'portal/node_modules'}' | Out-Null"], check=True)
    for repo, pin in ((backend, BACKEND), (portal, PORTAL)):
        assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip() == pin
    environment = {key: value for key, value in os.environ.items() if not key.startswith('IRPT_')}
    environment.update(IRPT_WORKSPACE_ROOT=str(backend),
                       IRPT_CONTRACTS_DIR=str(backend / 'docs/contracts/investor-reporting/v1'))
    evidence = {'backend': BACKEND, 'portal': PORTAL, 'remote_dev_parent': REMOTE_DEV,
                'snapshot': str(snapshot), 'runs': []}
    groups = [
        ('focused_gates_consumers', [
            'src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts',
            'src/pages/InvestorReporting/__tests__/fe-s-88/render-claim-admission.test.ts',
            'src/pages/InvestorReporting/__tests__/mvp-selection',
            'src/pages/InvestorReporting/__tests__/mvp-upload',
            'src/pages/InvestorReporting/__tests__/m-selection/selectionRequest.test.ts',
            'src/pages/InvestorReporting/__tests__/submission-request.test.ts',
            'src/pages/InvestorReporting/__tests__/fe-s-15/composer.test.ts']),
        ('affected_analysis_consumers', ['src/pages/InvestorReporting/tabs/analysis/tests']),
    ]
    for label, paths in groups:
        command = ['bun', 'test', *paths]
        result = subprocess.run(command, cwd=portal, env=environment, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=180)
        evidence['runs'].append({'label': label, 'command': command, 'exit_code': result.returncode,
                                'stdout': result.stdout, 'stderr': result.stderr})
    def blob(pin, path):
        return subprocess.check_output(['git', 'show', pin + ':' + path], cwd=root / 'portal')
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', REMOTE_DEV, '--', 'src'],
                                    cwd=root / 'portal', text=True).splitlines()
    preserved = [name for name in names if 'SecurityAnalysis' in name or 'mfa' in name.lower()
                 or name in ('src/components/ProtectedRoute.tsx', 'src/contexts/AuthContext.tsx',
                             'src/contexts/AuthContext.context.ts', 'src/lib/firmAccess.ts')]
    evidence['remote_dev_preservation'] = []
    for name in preserved:
        before, after = blob(REMOTE_DEV, name), blob(PORTAL, name)
        evidence['remote_dev_preservation'].append({'path': name, 'equal': before == after,
                                                   'sha256': hashlib.sha256(after).hexdigest()})
    evidence['carrier_status_after'] = subprocess.check_output(['git', 'status', '--porcelain', '--',
        'src/hooks/useAuth.ts', 'src/components/LoadingSpinner.tsx', 'src/contexts/AuthContext.context.ts'],
        cwd=portal, text=True)
    evidence['limits'] = 'Committed exact-pair consumer tests and static React/lifted-nav guard evaluation. No preview, actual browser, render/vendor call, publication or approval gate. Source census does not prove live authorization. Prior render delegate is preserved, not newly security-certified. No all14/runtime/full-product acceptance.'
    here.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(evidence, indent=2))
    return int(any(run['exit_code'] for run in evidence['runs']) or bool(evidence['carrier_status_after']))


if __name__ == '__main__':
    raise SystemExit(main())
