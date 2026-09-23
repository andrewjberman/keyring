"""Offline declared package proof; never upload or call AWS."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--repo", required=True)
parser.add_argument("--out", required=True)
args = parser.parse_args()
root = Path(args.repo).resolve()
pin = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
manifest_path = root / 'infra/aws/lambda/ci/lambda-source-map.json'
manifest_bytes = manifest_path.read_bytes()
manifest = json.loads(manifest_bytes)
out = []
for name, row in manifest['functions'].items():
    if not name.startswith('irpt-') or 'served.py' not in row['files']:
        continue
    package = Path(tempfile.mkdtemp(prefix='irpt-p-opal-' + name + '-')).resolve()
    staged = {dep['packaged_as']: dep for dep in row['staged_from']}
    assert len(staged) == len(row['staged_from'])
    members = []
    for member in row['files']:
        target = (package / member).resolve()
        assert target.is_relative_to(package)
        dep = staged.get(member)
        path = dep['repo_path'] if dep else row['source_dir'] + '/' + member
        source_pin = dep['pin'] if dep else pin
        content = subprocess.check_output(['git', 'show', source_pin + ':' + path], cwd=root)
        digest = hashlib.sha256(content).hexdigest()
        if dep:
            assert digest == dep['sha256'], member
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        members.append(dict(member=member, repo_path=path, pin=source_pin, sha256=digest))
    closure = subprocess.run([sys.executable, str(root / 'infra/aws/lambda/ci/import-closure-check.py'),
                              str(package), *row['files']], capture_output=True, text=True)
    env = {k: v for k, v in os.environ.items() if not k.startswith('IRPT_') and k != 'PYTHONPATH'}
    env.update(IRPT_CONTRACTS_DIR=str(package / 'contracts'), IRPT_FIRM_REGISTRY=str(package / 'firm_registry.json'),
               AWS_EC2_METADATA_DISABLED='true')
    code = "import sys;sys.path.insert(0,sys.argv[1]);import entry;assert callable(entry.lambda_handler);import custody,owner_reads;print('COLD_IMPORT_OK')"
    cold = subprocess.run([sys.executable, '-I', '-c', code, str(package)], cwd=package,
                          env=env, capture_output=True, text=True)
    record = dict(function=name, package=str(package), members=members,
                  closure=dict(rc=closure.returncode, output=closure.stdout + closure.stderr),
                  cold_import=dict(rc=cold.returncode, output=cold.stdout + cold.stderr))
    out.append(record)
    print(name, 'closure', closure.returncode, 'cold', cold.returncode)
    if closure.returncode:
        print(closure.stdout + closure.stderr)
    if cold.returncode:
        print(cold.stdout + cold.stderr)
receipt = dict(source_pin=pin, manifest_sha256=hashlib.sha256(manifest_bytes).hexdigest(), packages=out,
               limits='Offline immutable Git blobs and flat imports. No installed-factory, AWS invocation, upload or live pass.')
Path(args.out).write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
sys.exit(any(row['closure']['rc'] or row['cold_import']['rc'] for row in out))
