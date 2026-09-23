"""Rerun the original R-P09 probe/assertions with only the portal pin replaced."""
import hashlib
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve()
ROOT = HERE.parents[5]
ORIGINAL = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/upload_contract_probe_cb62.py'
ASSERTIONS = HERE.with_name('upload_receipt_cases.test.ts')
assert hashlib.sha256(ASSERTIONS.read_bytes()).hexdigest() == '13ef33af34b8d20e806c0d8c25194a5158055d44a74f6ca20f2355bea543f5ea'
source = subprocess.check_output(['git', 'show', 'fb0f801529:' + ORIGINAL], cwd=ROOT).decode()
# Keep the first review's captured bytes/evidence intact; assertions and producer unchanged.
source = source.replace('upload_actual_5add.json', 'upload_actual_retest_c86a.json')
namespace = {'__file__': str(HERE), '__name__': 'pinned_original_upload_probe'}
exec(compile(source, ORIGINAL, 'exec'), namespace)
namespace['PORTAL'] = 'c86a5eb53df6e48906def496df2d4dcdc0f47404'
if __name__ == '__main__':
    raise SystemExit(namespace['main']())
