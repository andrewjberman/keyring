"""Independent immutable backend/portal pairing with regenerated actual fixtures."""
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

BACKEND = '7915bc9b2c3d264d6b2560989b01dc57565f556f'
PORTAL = 'cf77e5db'
PACKAGE = 'infra/aws/lambda/investor-reporting'


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    portal = root / 'portal'
    snapshot = Path(tempfile.mkdtemp(prefix='cvo-p-dates-7915-'))
    portal_pin = subprocess.check_output(['git', 'rev-parse', PORTAL], cwd=portal, text=True).strip()
    paths = [PACKAGE + '/' + name for name in ('ops', 'intake', 'reports', 'ycharts/generate', '_authz', '_scope', '_ids', '_keys', '_contracts')]
    paths += ['docs/contracts/investor-reporting/v1', 'data/firm_registry.json']
    hashes = {}
    for repo, pin, members in ((root, BACKEND, paths), (portal, portal_pin, ['src', 'package.json'])):
        archive = subprocess.check_output(['git', 'archive', '--format=zip', pin, *members], cwd=repo)
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            for name in bundle.namelist():
                if name.endswith('/'):
                    continue
                target = (snapshot / name).resolve()
                assert target.is_relative_to(snapshot.resolve())
                raw = bundle.read(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(raw)
                hashes[name] = hashlib.sha256(raw).hexdigest()
    subprocess.run(['powershell', '-NoProfile', '-Command',
        f"New-Item -ItemType Junction -Path '{snapshot / 'node_modules'}' -Target '{portal / 'node_modules'}' | Out-Null"], check=True)
    old = json.loads(subprocess.check_output(['git', 'show',
        'dea338a397:docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json'], cwd=root))
    old['properties'].pop('internal_correlation_id')
    old['required'].remove('internal_correlation_id')
    (snapshot / 'old-public-status.json').write_text(json.dumps(old), encoding='utf-8')
    for name, destination in (
        ('status_date_pair_cases.py', PACKAGE + '/_contracts/test_reviewer_dates.py'),
        ('status_date_pair_cases.test.tsx', 'reviewer-dates.test.tsx')):
        (snapshot / destination).write_bytes(here.with_name(name).read_bytes())
    environment = {k: v for k, v in os.environ.items() if not k.startswith('IRPT_') and k != 'PYTHONPATH'}
    environment.update(PYTEST_DISABLE_PLUGIN_AUTOLOAD='1', AWS_EC2_METADATA_DISABLED='true',
        IRPT_CONTRACTS_DIR=str(snapshot / 'docs/contracts/investor-reporting/v1'),
        IRPT_WRITE_OWNED_OUTER_FIXTURE=str(snapshot / 'actual-owned-outer.json'),
        IRPT_WRITE_OWNED_DATE_OUTER_FIXTURE=str(snapshot / 'actual-owned-dates.json'))
    evidence = {'backend': BACKEND, 'portal': portal_pin, 'snapshot': str(snapshot), 'runs': [],
        'assertions': {name: hashlib.sha256(here.with_name(name).read_bytes()).hexdigest()
                       for name in ('status_date_pair_cases.py', 'status_date_pair_cases.test.tsx')}}

    def run(label, command):
        result = subprocess.run(command, cwd=snapshot, env=environment, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=90)
        evidence['runs'].append({'label': label, 'exit_code': result.returncode,
                                'stdout': result.stdout, 'stderr': result.stderr})
        return result.returncode

    run('supplied_backend_actual_entry_dates_outer', [sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider',
        PACKAGE + '/_contracts/test_owned_outer_contracts.py', PACKAGE + '/ops/tests/test_owned_entry.py',
        PACKAGE + '/ops/tests/test_prospect_dates.py'])
    run('independent_backend_pairing', [sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider',
        PACKAGE + '/_contracts/test_reviewer_dates.py'])
    evidence['captures'] = {}
    for name, fixture in (('outer', 'producer-owned-outer.json'), ('dates', 'producer-owned-dates.json')):
        target = snapshot / ('actual-owned-' + name + '.json')
        if target.exists():
            raw = target.read_bytes()
            here.with_name('status_date_actual_' + name + '_7915.json').write_bytes(raw)
            committed = snapshot / 'src/pages/InvestorReporting/__tests__/mvp-selection/tests' / fixture
            evidence['captures'][name] = {'sha256': hashlib.sha256(raw).hexdigest(),
                'equal_committed_portal_json': json.loads(raw) == json.loads(committed.read_bytes())}
            if name == 'outer':
                fresh, prior = copy.deepcopy(json.loads(raw)), copy.deepcopy(json.loads(committed.read_bytes()))
                # Diagnose fixture nondeterminism only; separate failing tests judge raw disclosure.
                for value in (fresh, prior):
                    for pair in value['cases'].values():
                        pair['refusal']['status'].pop('internal_correlation_id', None)
                evidence['captures'][name]['equal_except_rotating_refusal_correlation'] = fresh == prior
    run('supplied_portal_pairing', ['bun', 'test',
        'src/pages/InvestorReporting/__tests__/mvp-selection/prospect-dates.test.tsx',
        'src/pages/InvestorReporting/__tests__/mvp-selection/owned-outer.test.ts'])
    if len(evidence['captures']) == 2:
        run('independent_fresh_wire_parser_static', ['bun', 'test', 'reviewer-dates.test.tsx'])
    wire = snapshot / 'src/pages/InvestorReporting/contracts/wire'
    before = {p.name: p.read_bytes().replace(b'\r\n', b'\n') for p in wire.glob('*.ts')}
    (snapshot / 'regenerate-wire.ts').write_text(
        "import { generate } from './src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire'; console.log(JSON.stringify(generate()));\n", encoding='utf-8')
    run('generator_reproduction', ['bun', 'run', 'regenerate-wire.ts'])
    after = {p.name: p.read_bytes().replace(b'\r\n', b'\n') for p in wire.glob('*.ts')}
    evidence['generated_wire_differences'] = [name for name in sorted(set(before) | set(after)) if before.get(name) != after.get(name)]
    evidence['source_sha256'] = {name: sha for name, sha in hashes.items() if name.endswith((
        'StatusEnvelope.schema.json', 'BoundaryRefusal.schema.json', 'status-job.response.schema.json',
        'prospect_dates.py', 'owned_status.py', 'contracts/envelope.ts', 'contracts/prospect-dates.ts'))}
    evidence['limits'] = 'Actual Entry/retained services with supplied synthetic storage and reports; independent mutations and fresh wires. Static markup only. No cloud/runtime route, actual browser/export, vendor certification, full integration or atomicity proof. Legacy schema projection removes server-only CID; not an old-browser execution.'
    here.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(evidence, indent=2))
    return int(any(row['exit_code'] for row in evidence['runs']) or bool(evidence['generated_wire_differences'])
               or len(evidence['captures']) != 2 or not all(row['equal_committed_portal_json']
                    or row.get('equal_except_rotating_refusal_correlation', False) for row in evidence['captures'].values()))


if __name__ == '__main__':
    raise SystemExit(main())
