"""Pinned provider refusal, schema generation and declared-package review."""
import ast
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

BACKEND = 'cf11337d2e651a63623336ca29fdb67472983b37'
PACKAGE_PIN = 'f7e0a07c43'
PORTAL = '33e139259d06438674b1d10d48f5a221c26e44f7'
PKG = 'infra/aws/lambda/investor-reporting'
MAP = 'infra/aws/lambda/ci/lambda-source-map.json'
OWNER = 'org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/'


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]

    def blob(ref, path):
        return subprocess.check_output(['git', 'show', ref + ':' + path], cwd=root)

    package_pin = subprocess.check_output(['git', 'rev-parse', PACKAGE_PIN], cwd=root, text=True).strip()
    before, after = [json.loads(blob(ref, MAP)) for ref in (BACKEND, package_pin)]
    assert before['functions'].keys() == after['functions'].keys()
    changed = [k for k in before['functions'] if before['functions'][k] != after['functions'][k]]
    assert changed == ['irpt-performance-adapter']
    assert {k: v for k, v in before.items() if k != 'functions'} == {k: v for k, v in after.items() if k != 'functions'}
    item, old = after['functions'][changed[0]], before['functions'][changed[0]]
    fields = sorted(k for k in set(item) | set(old) if item.get(k) != old.get(k))
    assert set(fields) <= {'files', 'staged_from', '_build_note', 'note', '_staged_from_note'}
    staged = {r['packaged_as']: r for r in item['staged_from']}
    assert len(staged) == len(item['staged_from']) and set(staged) <= set(item['files'])
    assert len(item['files']) == len(set(item['files'])) == 28
    evidence = {'backend': BACKEND, 'package': package_pin, 'portal': PORTAL,
                'functions_total': len(after['functions']), 'unchanged_other_functions': len(after['functions']) - 1,
                'changed_functions': changed, 'changed_fields': fields, 'members': {}, 'runs': []}
    additional = here.with_name('primary_policy_cases.py').read_bytes()
    evidence['assertions_sha256'] = hashlib.sha256(additional).hexdigest()
    runner = blob(package_pin, OWNER + 'verify_selection_packages.py')
    supplied = next(ast.literal_eval(n.value) for n in ast.parse(runner).body if isinstance(n, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id == 'PROBE' for t in n.targets))
    with tempfile.TemporaryDirectory(prefix='cvo-p-primary-cf11-') as scratch:
        base = Path(scratch)
        paths = [PKG + '/' + p for p in ('performance', '_authz', '_scope', '_ids', '_keys', '_contracts')]
        paths += ['docs/contracts/investor-reporting/v1', 'data/firm_registry.json',
                  'infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py']
        for repo, ref, selected in ((root, BACKEND, paths), (root / 'portal', PORTAL, ['src'])):
            raw = subprocess.check_output(['git', 'archive', '--format=zip', ref, *selected], cwd=repo)
            with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                for name in archive.namelist():
                    if name.endswith('/'):
                        continue
                    target = (base / name).resolve()
                    assert target.is_relative_to(base.resolve())
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(archive.read(name))
        flat = base / 'flat'
        flat.mkdir()
        for member in item['files']:
            row = staged.get(member)
            raw = blob(row['pin'], row['repo_path']) if row else blob(package_pin, item['source_dir'] + '/' + member)
            sha = hashlib.sha256(raw).hexdigest()
            if row:
                assert sha == row['sha256']
            else:
                assert raw == blob(BACKEND, item['source_dir'] + '/' + member)
            target = (flat / member).resolve()
            assert target.is_relative_to(flat.resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
            evidence['members'][member] = {'sha256': sha, 'staged': row is not None}
        closure = base / 'closure.py'
        closure.write_bytes(blob(package_pin, 'infra/aws/lambda/ci/import-closure-check.py'))
        environment = {k: v for k, v in os.environ.items() if not k.startswith('IRPT_') and k != 'PYTHONPATH'}
        environment.update(AWS_EC2_METADATA_DISABLED='true', PYTEST_DISABLE_PLUGIN_AUTOLOAD='1')

        def run(label, command, cwd=base):
            result = subprocess.run(command, cwd=cwd, env=environment, capture_output=True,
                                    text=True, encoding='utf-8', errors='replace', timeout=90)
            evidence['runs'].append({'label': label, 'exit_code': result.returncode,
                                     'stdout': result.stdout, 'stderr': result.stderr})

        run('supplied_performance_tests', [sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider', PKG + '/performance/tests'])
        run('canonical_package_closure', [sys.executable, str(closure), str(flat), *item['files']], flat)
        run('supplied_flat_guarded_entry', [sys.executable, '-I', '-c', supplied, str(flat), changed[0]], flat)
        run('additional_flat_controls', [sys.executable, '-I', '-c', supplied.split("if sys.argv[2]")[0] + '\n' + additional.decode(), str(flat)], flat)
        contract = base / 'docs/contracts/investor-reporting/v1/PerformanceReport.schema.json'
        raw_contract = base / PKG / '_contracts/PerformanceReport.schema.json'
        expected = ['SMARTX', 'BLACK_DIAMOND', 'ORION', 'UNKNOWN']
        for path in (contract, raw_contract, flat / 'PerformanceReport.schema.json'):
            assert json.loads(path.read_text())['properties']['lineage']['properties']['provider']['enum'] == expected
        source = """import {readFileSync} from 'node:fs';
import {renderModule} from './src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire';
const schema = readFileSync('./docs/contracts/investor-reporting/v1/PerformanceReport.schema.json','utf8');
const actual = readFileSync('./src/pages/InvestorReporting/contracts/wire/PerformanceReport.ts','utf8');
if(renderModule('PerformanceReport',schema).replace(/\\r\\n/g,'\\n') !== actual.replace(/\\r\\n/g,'\\n')) throw new Error('generated wire drift');
console.log('Pinned SMARTX PerformanceReport wire regenerates exactly');
"""
        (base / 'wire-check.ts').write_text(source, encoding='utf-8')
        run('exact_wire_regeneration', ['bun', 'wire-check.ts'])
        evidence['schema_sha256'] = {str(path.relative_to(base)): hashlib.sha256(path.read_bytes()).hexdigest()
                                      for path in (contract, raw_contract, flat / 'PerformanceReport.schema.json')}
    evidence['limits'] = 'Actual source/flat entry with synthetic scope and storage; source-map reconstruction only. No deployed/layer/IAM or current vendor calculation proof. Additional controls reuse pinned supplied entry setup. No broader readiness.'
    here.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(evidence, indent=2))
    return int(any(r['exit_code'] for r in evidence['runs']))


if __name__ == '__main__':
    raise SystemExit(main())
