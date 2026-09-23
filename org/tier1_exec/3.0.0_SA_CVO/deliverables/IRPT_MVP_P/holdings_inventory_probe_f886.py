"""Reconstruct replacement package and preserve prior independent assertions."""
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve()
ROOT = HERE.parents[5]
HOME = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/'
PIN = 'f8860f9839'
BEFORE = '55fae26e37'


def blob(pin, path):
    return subprocess.check_output(['git', 'show', pin + ':' + path], cwd=ROOT)


previous = json.loads(blob('198d9a29c8', HOME + 'holdings_multipart_probe_c9e4.json'))
old_assertions = (HERE.with_name('holdings_package_cases.py').read_bytes() + b'\n'
                  + HERE.with_name('holdings_multipart_cases.py').read_bytes())
assert hashlib.sha256(old_assertions).hexdigest() == previous['assertions_sha256']
mapping = json.loads(blob(PIN, 'infra/aws/lambda/ci/lambda-source-map.json'))['functions']['irpt-holdings']
staged = {row['packaged_as']: row for row in mapping['staged_from']}
assert staged['publication.py']['pin'] == 'fd4690b4ffca23f2616fe5f19d90737af6fe3a58'
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
source = source.replace('HOLDINGS_PACKAGE_EVIDENCE.json', 'HOLDINGS_INVENTORY_REPAIR_PACKAGE_EVIDENCE.json')
source = source.replace("own = here.with_name('holdings_package_cases.py').read_bytes()",
    "own = here.with_name('holdings_package_cases.py').read_bytes() + b'\\n' + here.with_name('holdings_multipart_cases.py').read_bytes() + b'\\n' + here.with_name('holdings_inventory_cases.py').read_bytes()")
namespace = {'__file__': str(HERE), '__name__': 'pinned_holdings_package_probe'}
exec(compile(source, HOME + 'holdings_package_probe_0fb7.py', 'exec'), namespace)
namespace.update(PIN=PIN, BEFORE=BEFORE)
if __name__ == '__main__':
    result = namespace['main']()
    evidence = json.loads(HERE.with_suffix('.json').read_text())
    evidence['changed_member_bytes_from_review_198d9a29c8'] = changed
    evidence['terraform_bytes_equal_review_198d9a29c8'] = True
    evidence['prior_assertions_unchanged_sha256'] = previous['assertions_sha256']
    evidence['publication_staged_from'] = staged['publication.py']
    HERE.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    raise SystemExit(result)
