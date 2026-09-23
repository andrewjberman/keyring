"""Reuse the pinned independent package review with multipart pins and three controls."""
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve()
ROOT = HERE.parents[5]
HOME = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/'
PIN = 'c9e4529553eb98b17347f81c77f199e0b5bf9868'
BEFORE = 'afb924a74bc4297b12663c3199e13ebbfb9283fb'


def blob(pin, path):
    return subprocess.check_output(['git', 'show', pin + ':' + path], cwd=ROOT)


previous = json.loads(blob('57f0a0ef3c', HOME + 'holdings_package_probe_0fb7.json'))
assert hashlib.sha256(HERE.with_name('holdings_package_cases.py').read_bytes()).hexdigest() == previous['assertions_sha256']
mapping = json.loads(blob(PIN, 'infra/aws/lambda/ci/lambda-source-map.json'))['functions']['irpt-holdings']
staged = {row['packaged_as']: row for row in mapping['staged_from']}
changed = []
for member in mapping['files']:
    row = staged.get(member)
    raw = blob(row['pin'], row['repo_path']) if row else blob(PIN, mapping['source_dir'] + '/' + member)
    if hashlib.sha256(raw).hexdigest() != previous['members'][member]['sha256']:
        changed.append(member)
assert set(changed) == {'entry.py', 'snapshot.py', 'publication.py'}
for name, expected in previous['terraform_source_sha256'].items():
    raw = blob(PIN, 'infra/aws/terraform/investor-reporting/holdings/' + name)
    assert hashlib.sha256(raw).hexdigest() == expected

source = blob('57f0a0ef3c', HOME + 'holdings_package_probe_0fb7.py').decode()
source = source.replace("assert set(fields) == {'files', 'staged_from', '_staged_from_note', '_build_note'}",
                        "assert set(fields) == {'staged_from', '_build_note'}")
source = source.replace('HOLDINGS_PACKAGE_EVIDENCE.json', 'HOLDINGS_MULTIPART_PACKAGE_EVIDENCE.json')
source = source.replace("own = here.with_name('holdings_package_cases.py').read_bytes()",
    "own = here.with_name('holdings_package_cases.py').read_bytes() + b'\\n' + here.with_name('holdings_multipart_cases.py').read_bytes()")
namespace = {'__file__': str(HERE), '__name__': 'pinned_holdings_package_probe'}
exec(compile(source, HOME + 'holdings_package_probe_0fb7.py', 'exec'), namespace)
namespace.update(PIN=PIN, BEFORE=BEFORE)
if __name__ == '__main__':
    result = namespace['main']()
    evidence = json.loads(HERE.with_suffix('.json').read_text())
    evidence['changed_member_bytes_from_review_57f0a0ef3c'] = changed
    evidence['terraform_bytes_equal_review_57f0a0ef3c'] = True
    evidence['prior_assertions_unchanged_sha256'] = previous['assertions_sha256']
    HERE.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    raise SystemExit(result)
