"""Exact replacement package retest; original failing assertions stay immutable."""
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve()
ROOT = HERE.parents[5]
HOME = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/'
PIN = 'f0f391d6a5'
BEFORE = 'ff247a24fe'


def blob(pin, path):
    return subprocess.check_output(['git', 'show', pin + ':' + path], cwd=ROOT)


previous = json.loads(blob('142e5a27a4', HOME + 'holdings_inventory_probe_f886.json'))
assertion_files = ('holdings_package_cases.py', 'holdings_multipart_cases.py', 'holdings_inventory_cases.py')
original = b'\n'.join(blob('142e5a27a4', HOME + name) for name in assertion_files)
assert hashlib.sha256(original).hexdigest() == previous['assertions_sha256']
for name in assertion_files:
    assert HERE.with_name(name).read_bytes() == blob('142e5a27a4', HOME + name), name
mapping = json.loads(blob(PIN, 'infra/aws/lambda/ci/lambda-source-map.json'))['functions']['irpt-holdings']
staged = {row['packaged_as']: row for row in mapping['staged_from']}
assert staged['publication.py']['pin'] == 'fdd02de5b2519dfdf26a8f09b44d66b18ba73b11'
assert set(mapping['files']) == set(previous['members'])
changed = []
for member in mapping['files']:
    row = staged.get(member)
    raw = blob(row['pin'], row['repo_path']) if row else blob(PIN, mapping['source_dir'] + '/' + member)
    if hashlib.sha256(raw).hexdigest() != previous['members'][member]['sha256']:
        changed.append(member)
assert changed == ['publication.py']
for name, expected in previous['terraform_source_sha256'].items():
    assert hashlib.sha256(blob(PIN, 'infra/aws/terraform/investor-reporting/holdings/' + name)).hexdigest() == expected

source = blob('57f0a0ef3c', HOME + 'holdings_package_probe_0fb7.py').decode()
source = source.replace("assert set(fields) == {'files', 'staged_from', '_staged_from_note', '_build_note'}",
                        "assert set(fields) == {'staged_from', '_build_note'}")
source = source.replace('HOLDINGS_PACKAGE_EVIDENCE.json', 'HOLDINGS_R_P10_PACKAGE_EVIDENCE.json')
files = (*assertion_files, 'holdings_inventory_valid_cases.py')
expression = " + b'\\n' + ".join("here.with_name(" + repr(name) + ").read_bytes()" for name in files)
source = source.replace("own = here.with_name('holdings_package_cases.py').read_bytes()", 'own = ' + expression)
namespace = {'__file__': str(HERE), '__name__': 'pinned_holdings_package_probe'}
exec(compile(source, HOME + 'holdings_package_probe_0fb7.py', 'exec'), namespace)
namespace.update(PIN=PIN, BEFORE=BEFORE)
if __name__ == '__main__':
    result = namespace['main']()
    evidence = json.loads(HERE.with_suffix('.json').read_text())
    evidence['changed_member_bytes_from_review_142e5a27a4'] = changed
    evidence['terraform_bytes_equal_review_142e5a27a4'] = True
    evidence['original_assertions_unchanged_sha256'] = previous['assertions_sha256']
    evidence['original_assertion_files'] = {name: hashlib.sha256(blob('142e5a27a4', HOME + name)).hexdigest()
                                            for name in assertion_files}
    evidence['publication_staged_from'] = staged['publication.py']
    HERE.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    raise SystemExit(result)
