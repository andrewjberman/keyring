"""IRPT_ANLREQ round 2, workstream ~T -- AR-t-21 (I7): the store's commentary_ref is exactly {artifact_id, sha256, version_id} and its canonical
JSON (sorted keys, no spaces) is at most 512 chars. Prints AR2-T21-OK|FAIL and exits 0/1. Run from the repo root."""
import re
import subprocess
import sys
from pathlib import Path

TEST = Path("infra/aws/lambda/investor-reporting/reports/tests/test_commentary_ref_i7.py")
NAMES = ["test_ref_has_exactly_three_fields", "test_canonical_json_under_512", "test_stored_and_returned_ref_are_equal"]
if not TEST.exists():
    print("AR2-T21-FAIL absent: %s" % TEST.as_posix())
    sys.exit(1)
text = TEST.read_text(encoding="utf-8")
missing = [n for n in NAMES if "def %s(" % n not in text]
if missing:
    print("AR2-T21-FAIL missing %s" % ", ".join(missing))
    sys.exit(1)
r = subprocess.run([sys.executable, "-m", "pytest", str(TEST), "-q", "-p", "no:cacheprovider"], capture_output=True, text=True, timeout=110)
tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
ok = r.returncode == 0 and int((re.search(r"(\d+) passed", tail) or [0, 0])[1]) >= len(NAMES)
print("AR2-T21-%s %s" % ("OK" if ok else "FAIL", tail))
sys.exit(0 if ok else 1)
