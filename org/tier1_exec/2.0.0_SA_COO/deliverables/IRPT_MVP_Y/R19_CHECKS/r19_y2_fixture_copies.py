"""R19 ~Y cell IB-yr-2 check: the pinned lookup captures live in the test tree, byte-identical to the CRO capture.

Run from the repo root:  python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R19_CHECKS/r19_y2_fixture_copies.py
Prints COPIES-IDENTICAL 3/3 and exits 0, or names each missing or differing file and exits 1.
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
SOURCE = ROOT / "org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_YCHARTS_LOOKUP_CAPTURE_20260923"
TARGET = ROOT / "infra/aws/lambda/investor-reporting/intake/tests/fixtures/lookup_capture"
NAMES = ("02_securities_info.json", "03_suggest_ALPPL.json", "04_suggest_BREIT.json")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


bad = []
for name in NAMES:
    target = TARGET / name
    if not target.is_file():
        bad.append("MISSING %s" % target.relative_to(ROOT).as_posix())
    elif sha(target) != sha(SOURCE / name):
        bad.append("DIFFERS %s" % name)
if bad:
    print("\n".join(bad))
    sys.exit(1)
print("COPIES-IDENTICAL %d/%d" % (len(NAMES), len(NAMES)))
