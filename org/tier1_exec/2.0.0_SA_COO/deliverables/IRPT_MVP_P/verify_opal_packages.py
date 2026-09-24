"""Offline declared package proof; never upload or call AWS."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

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
    archive = package.with_suffix('.zip')
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as bundle:
        for member in sorted(row['files']):
            info = zipfile.ZipInfo(member, (2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            bundle.writestr(info, (package / member).read_bytes())
    closure = subprocess.run([sys.executable, str(root / 'infra/aws/lambda/ci/import-closure-check.py'),
                              str(package), *row['files']], capture_output=True, text=True)
    enforcing = (package / 'BUILD_MANIFEST.json').is_file()
    negative = None
    if name == 'irpt-ycharts-generate':
        assert enforcing, 'Factory closure requires an enforced BUILD_MANIFEST.json'
        assert 'ADVISORY' not in closure.stdout and 'UNENFORCED' not in closure.stdout
        omitted = [member for member in row['files'] if member != 'custody.py']
        rejected = subprocess.run([sys.executable, str(root / 'infra/aws/lambda/ci/import-closure-check.py'),
                                   str(package), *omitted], capture_output=True, text=True)
        assert rejected.returncode == 1 and 'custody' in rejected.stdout
        negative = dict(omitted_member='custody.py', rc=rejected.returncode,
                        output=rejected.stdout + rejected.stderr)
    env = {k: v for k, v in os.environ.items() if not k.startswith('IRPT_') and k != 'PYTHONPATH'}
    env.update(IRPT_CONTRACTS_DIR=str(package / 'contracts'), IRPT_FIRM_REGISTRY=str(package / 'firm_registry.json'),
               AWS_EC2_METADATA_DISABLED='true')
    code = "import sys;sys.path.insert(0,sys.argv[1]);import entry;assert callable(entry.lambda_handler);import custody,owner_reads;print('COLD_IMPORT_OK')"
    if name == 'irpt-ycharts-generate':
        code += '''
import pathlib
import boto3
from botocore.stub import Stubber
from custody_submission import build_custody_entry
from recipe_snapshot import capture_configuration
root = pathlib.Path(sys.argv[1])
sdk = boto3.client('dynamodb', region_name='us-east-1',
                   aws_access_key_id='offline', aws_secret_access_key='offline')
stub = Stubber(sdk)
stub.activate()
boundary = build_custody_entry(
    dynamodb=sdk, table=object(), s3=object(),
    schema_directory=str(root / 'contracts'),
    reporting_policy=lambda *args: None,
    reporting_destination=lambda *args, **kwargs: None,
    authorize_snapshot=lambda *args: False,
    load_normalized=lambda *args: None,
    send=lambda *args: None, queue_url='offline-no-send',
    ingestion_revision='offline-construction', destination_revision='offline-construction',
    clock=lambda: 0,
    configuration=lambda owner, browser: capture_configuration(owner, browser,
        templates_path=str(root / 'templates.json'), settings_path=str(root / 'settings.json')))
assert boundary is not entry.ENTRY
import custody_submission
assert pathlib.Path(custody_submission.__file__).resolve().parent == root.resolve()
print('EXTRACTED_FACTORY_CONSTRUCTION_OK; synthetic refusing ports; no request or SDK call')
'''
    cold = subprocess.run([sys.executable, '-I', '-c', code, str(package)], cwd=package,
                          env=env, capture_output=True, text=True)
    record = dict(function=name, package=str(package), members=members,
                  local_source_archive=dict(path=str(archive), sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),
                                            bytes=archive.stat().st_size,
                                            kind='offline source-only proof; not a deployable artifact'),
                  closure=dict(rc=closure.returncode, enforced=enforcing,
                               output=closure.stdout + closure.stderr, missing_module_control=negative),
                  cold_import=dict(rc=cold.returncode, output=cold.stdout + cold.stderr))
    out.append(record)
    print(name, 'closure', closure.returncode, 'cold', cold.returncode)
    if closure.returncode:
        print(closure.stdout + closure.stderr)
    if cold.returncode:
        print(cold.stdout + cold.stderr)
receipt = dict(source_pin=pin, manifest_sha256=hashlib.sha256(manifest_bytes).hexdigest(), packages=out,
               limits='Offline immutable Git blobs and flat imports. Generate factory construction uses synthetic refusing ports and host Python third-party dependencies. No packaged-wheel/runtime completeness, request, AWS invocation, upload or live pass.')
Path(args.out).write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
sys.exit(any(row['closure']['rc'] or row['cold_import']['rc'] for row in out))
