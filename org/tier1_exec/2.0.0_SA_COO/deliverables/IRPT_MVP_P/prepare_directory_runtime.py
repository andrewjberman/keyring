"""Prepare one immutable directory package and offline proof inputs; no cloud writes."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--pin', required=True)
p.add_argument('--out', required=True)
a = p.parse_args()
root = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
out = Path(a.out).resolve()
out.mkdir(parents=True, exist_ok=True)

def blob(path, pin=a.pin):
    return subprocess.check_output(['git', 'show', pin + ':' + path], cwd=root)

map_path = 'infra/aws/lambda/ci/lambda-source-map.json'
map_bytes = blob(map_path)
row = json.loads(map_bytes)['functions']['irpt-directory-search']
staged = {x['packaged_as']: x for x in row['staged_from']}
members = []
for name in row['files']:
    dep = staged.get(name)
    path = dep['repo_path'] if dep else row['source_dir'] + '/' + name
    pin = dep['pin'] if dep else a.pin
    content = blob(path, pin)
    sha = hashlib.sha256(content).hexdigest()
    if dep:
        assert sha == dep['sha256'], name
    dest = out / 'payload' / name
    assert dest.resolve().is_relative_to((out / 'payload').resolve())
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(content)
    members.append(dict(member=name, path=path, pin=pin, sha256=sha,
                        git_blob=subprocess.check_output(['git', 'rev-parse', pin + ':' + path], text=True).strip(), bytes=len(content)))
tests = ['infra/aws/lambda/investor-reporting/directory/tests/' + name for name in
         ['test_selection_entry.py', 'test_bootstrap_browse.py', 'test_opal_context.py']]
tests.append('infra/aws/lambda/investor-reporting/_contracts/tests/test_selection_contract.py')
contracts = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', a.pin,
                                     'docs/contracts/investor-reporting/v1'], text=True).splitlines()
proof = []
for path in tests + [x for x in contracts if x.endswith('.schema.json')]:
    content = blob(path)
    dest = out / 'test-inputs' / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(content)
    proof.append(dict(path=path, pin=a.pin, sha256=hashlib.sha256(content).hexdigest()))
manifest = dict(source_pin=a.pin, source_map_sha256=hashlib.sha256(map_bytes).hexdigest(),
                function='irpt-directory-search', members=members, test_inputs=proof,
                limits='Tests and test dependencies are separate from the runtime ZIP. No upload or apply.')
(out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print('PREPARED', len(members), 'runtime members;', len(proof), 'separate test inputs')
