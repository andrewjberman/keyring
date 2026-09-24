"""Exact-pin offline package reconstruction and bounded source-IAM evidence."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

PIN = '0fb7e56629'
BEFORE = '5a85252603'
MAP = 'infra/aws/lambda/ci/lambda-source-map.json'
OWNER = 'org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/'


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]

    def blob(pin, path):
        return subprocess.check_output(['git', 'show', pin + ':' + path], cwd=root)

    pin = subprocess.check_output(['git', 'rev-parse', PIN], cwd=root, text=True).strip()
    before = json.loads(blob(BEFORE, MAP))
    after = json.loads(blob(pin, MAP))
    assert set(before['functions']) == set(after['functions'])
    changed = [key for key in before['functions'] if before['functions'][key] != after['functions'][key]]
    assert changed == ['irpt-holdings']
    assert {k: v for k, v in before.items() if k != 'functions'} == {k: v for k, v in after.items() if k != 'functions'}
    old, item = before['functions']['irpt-holdings'], after['functions']['irpt-holdings']
    fields = [key for key in set(old) | set(item) if old.get(key) != item.get(key)]
    assert set(fields) == {'files', 'staged_from', '_staged_from_note', '_build_note'}
    staged = {row['packaged_as']: row for row in item['staged_from']}
    assert len(staged) == len(item['staged_from']) and set(staged) <= set(item['files'])
    assert len(item['files']) == len(set(item['files'])) == 31
    producer = json.loads(blob(pin, OWNER + 'HOLDINGS_PACKAGE_EVIDENCE.json'))
    runner = blob(pin, OWNER + 'verify_holdings_package.py')
    assignments = ast.parse(runner).body
    supplied = next(ast.literal_eval(node.value) for node in assignments if isinstance(node, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id == 'PROBE' for t in node.targets))
    own = here.with_name('holdings_package_cases.py').read_bytes()
    evidence = {'pin': pin, 'before': BEFORE, 'function_count': len(after['functions']),
                'changed_functions': changed, 'unchanged_functions': len(after['functions']) - 1,
                'changed_fields': sorted(fields), 'members': {}, 'runs': [],
                'assertions_sha256': hashlib.sha256(own).hexdigest(),
                'supplied_runner_sha256': hashlib.sha256(runner).hexdigest()}
    with tempfile.TemporaryDirectory(prefix='cvo-p-holdings-0fb7-') as scratch:
        base = Path(scratch)
        flat = base / 'flat'
        flat.mkdir()
        for member in item['files']:
            row = staged.get(member)
            data = blob(row['pin'], row['repo_path']) if row else blob(pin, item['source_dir'] + '/' + member)
            sha = hashlib.sha256(data).hexdigest()
            if row:
                assert sha == row['sha256']
            else:
                assert data == blob(BEFORE, item['source_dir'] + '/' + member)
            assert sha == producer['members'][member]
            target = (flat / member).resolve()
            assert target.is_relative_to(flat.resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            evidence['members'][member] = {'sha256': sha, 'staged': row is not None}
        fixture = base / 'fixture.json'
        fixture.write_bytes(blob(pin, OWNER + 'holdings_package_fixture.json'))
        closure = base / 'closure.py'
        closure.write_bytes(blob(pin, 'infra/aws/lambda/ci/import-closure-check.py'))
        environment = {k: v for k, v in os.environ.items() if not k.startswith('IRPT_') and k != 'PYTHONPATH'}
        environment['AWS_EC2_METADATA_DISABLED'] = 'true'
        commands = [
            ('supplied_import_closure', [sys.executable, str(closure), str(flat), *item['files']]),
            ('additional_boundary_controls', [sys.executable, '-I', '-c', supplied.split("registry=flat/")[0] + '\n' + own.decode(), str(flat), str(fixture)]),
            ('supplied_guarded_entry_controls', [sys.executable, '-I', '-c', supplied, str(flat), str(fixture)]),
        ]
        for label, command in commands:
            result = subprocess.run(command, cwd=flat, env=environment, capture_output=True,
                                    text=True, encoding='utf-8', errors='replace', timeout=60)
            evidence['runs'].append({'label': label, 'exit_code': result.returncode,
                                     'stdout': result.stdout, 'stderr': result.stderr})
    tf = 'infra/aws/terraform/investor-reporting/holdings/'
    sources = {name: blob(pin, tf + name).decode() for name in ('main.tf', 'iam.tf', 'lambda.tf')}
    evidence['terraform_source_sha256'] = {name: hashlib.sha256(text.encode()).hexdigest() for name, text in sources.items()}
    actions = sorted(set(re.findall(r'"((?:s3|dynamodb|kms):[^"\s]+)"', sources['iam.tf'])))
    assert actions == ['dynamodb:GetItem', 'dynamodb:LeadingKeys', 'kms:Decrypt',
                       'kms:EncryptionContext:aws:dynamodb:tableName', 'kms:ViaService', 's3:GetObject', 's3:GetObjectVersion']
    assert 'basename(dirname(abspath(path.module)))' in sources['main.tf']
    assert 'IRPT_REQUESTS_TABLE' in sources['lambda.tf']
    evidence['iam_source_tokens'] = actions
    evidence['limits'] = 'Offline source declarations and synthetic storage; local resource-pattern checks are not an IAM simulator. No deployed policies, remote state, Terraform plan/apply, layers, cloud/server clock, actual publisher or live transport proof. Additional controls reuse supplied guarded-entry setup.'
    here.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(evidence, indent=2))
    return int(any(run['exit_code'] for run in evidence['runs']))


if __name__ == '__main__':
    raise SystemExit(main())
