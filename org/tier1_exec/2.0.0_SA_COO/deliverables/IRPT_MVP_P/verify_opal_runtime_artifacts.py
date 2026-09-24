"""Hash-check, extract and test the local function/dependency artifact pair."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import zipfile

IMAGE = 'public.ecr.aws/lambda/python@sha256:5f188ce6104ab76d1a9a44b9b53fd0d72ea5ccec94eb4cbccf5c9b0ef485f9f8'


def extract(source, target, expected_sha, members):
    assert hashlib.sha256(source.read_bytes()).hexdigest() == expected_sha
    expected = {row['member']: row['sha256'] for row in members}
    assert len(expected) == len(members)
    with zipfile.ZipFile(source) as archive:
        assert len(archive.namelist()) == len(set(archive.namelist()))
        assert set(archive.namelist()) == set(expected)
        for name in archive.namelist():
            dest = (target / name).resolve()
            assert dest.is_relative_to(target.resolve())
            data = archive.read(name)
            assert hashlib.sha256(data).hexdigest() == expected[name], name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-receipt', required=True)
    parser.add_argument('--dependency-manifest', required=True)
    parser.add_argument('--dependency-zip', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    source = json.loads(Path(args.source_receipt).read_text())
    package = next(row for row in source['packages'] if row['function'] == 'irpt-ycharts-generate')
    dependencies = json.loads(Path(args.dependency_manifest).read_text())
    stage = Path(tempfile.mkdtemp(prefix='irpt-p-linux-proof-'))
    extract(Path(package['local_source_archive']['path']), stage / 'function',
            package['local_source_archive']['sha256'], package['members'])
    extract(Path(args.dependency_zip), stage / 'layer', dependencies['zip_sha256'], dependencies['members'])
    proof = Path(__file__).resolve().parent
    command = ['docker', 'run', '--rm', '--platform', 'linux/amd64', '--network', 'none',
               '--read-only', '--tmpfs', '/tmp', '--cpus', '2', '--memory', '1g',
               '--entrypoint', '/var/lang/bin/python']
    for host, guest in ((stage / 'function', '/var/task'), (stage / 'layer/python', '/opt/python'),
                        (proof, '/proof')):
        command += ['--mount', 'type=bind,source=' + str(host) + ',target=' + guest + ',readonly']
    command += [IMAGE, '-I', '-B', '/proof/verify_opal_linux_runtime.py']
    result = subprocess.run(command, capture_output=True, text=True, timeout=60)
    receipt = dict(source_pin=source['source_pin'], source_manifest_sha256=source['manifest_sha256'],
                   source_archive_sha256=package['local_source_archive']['sha256'],
                   dependency_archive_sha256=dependencies['zip_sha256'], image=IMAGE,
                   command=command, rc=result.returncode, stdout=result.stdout, stderr=result.stderr,
                   checker_sha256=hashlib.sha256((proof / 'verify_opal_linux_runtime.py').read_bytes()).hexdigest(),
                   limits='Local extracted artifact dependency and construction proof; no current producer or live acceptance.')
    Path(args.out).write_text(json.dumps(receipt, indent=2) + '\n')
    print(result.stdout)
    if result.returncode:
        print(result.stderr)
        raise SystemExit(result.returncode)
    assert json.loads(result.stdout)['result'] == 'PASS'


if __name__ == '__main__':
    main()
