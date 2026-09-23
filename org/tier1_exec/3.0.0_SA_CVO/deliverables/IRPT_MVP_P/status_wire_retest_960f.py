"""Preserve original R-P11 assertions while retesting the exact repaired pair."""
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve()
ROOT = HERE.parents[5]
HOME = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/'
PIN = 'a050df00e5'


def blob(path):
    return subprocess.check_output(['git', 'show', PIN + ':' + HOME + path], cwd=ROOT)


previous = json.loads(blob('status_date_pair_probe_7915.json'))
for name, expected in previous['assertions'].items():
    raw = blob(name)
    assert hashlib.sha256(raw).hexdigest() == expected
    assert HERE.with_name(name).read_bytes() == raw, name
source = blob('status_date_pair_probe_7915.py').decode()
needle = '(snapshot / destination).write_bytes(here.with_name(name).read_bytes())'
assert source.count(needle) == 1
source = source.replace(needle,
    "(snapshot / destination).write_bytes(here.with_name(name).read_bytes() + b'\\n' + here.with_name('status_wire_extra_cases.py' if name.endswith('.py') else 'status_wire_extra_cases.test.ts').read_bytes())")
source = source.replace("'_7915.json'", "'_retest_960f.json'")
namespace = {'__file__': str(HERE), '__name__': 'pinned_original_pair_probe'}
exec(compile(source, HOME + 'status_date_pair_probe_7915.py', 'exec'), namespace)
namespace['BACKEND'] = subprocess.check_output(['git', 'rev-parse', '960f5f2a45'], cwd=ROOT, text=True).strip()
namespace['PORTAL'] = 'c09fea54e9f4613d44b874724e93b79c443f8cc8'
served_path = 'infra/aws/lambda/investor-reporting/_authz/served.py'
served_bytes = subprocess.check_output(['git', 'show', namespace['BACKEND'] + ':' + served_path], cwd=ROOT)
assert served_bytes == subprocess.check_output(['git', 'show', '483a2fee0a:' + served_path], cwd=ROOT)
if __name__ == '__main__':
    result = namespace['main']()
    evidence = json.loads(HERE.with_suffix('.json').read_text())
    evidence['original_review'] = PIN
    evidence['original_assertions_unchanged'] = previous['assertions']
    evidence['additional_assertions_sha256'] = {name: hashlib.sha256(HERE.with_name(name).read_bytes()).hexdigest()
        for name in ('status_wire_extra_cases.py', 'status_wire_extra_cases.test.ts')}
    evidence['served_source_equals_owner_483a2fee0a'] = True
    evidence['served_source_sha256'] = hashlib.sha256(served_bytes).hexdigest()
    HERE.with_suffix('.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    raise SystemExit(result)
