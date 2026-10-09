"""NFRA_TRNSPT round 18 -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  g18   TR18-g18-AC1  R18_COVERAGE.md holds a JSON block with exactly one row per ungraded FWD (1-6, 8, 9), each naming an act + invocation +
                      read, or a missing hop
  p18   TR18-p18-AC1  the second-reader test passes by name: the transcripts root declares the second named reader's principal from a
                      name() builder record and adds it to the key's named readers, nothing else widened

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

COVERAGE = Path("org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R18_COVERAGE.md")
FWDS = ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-8", "FWD-9"]
P18_TEST = Path("data/transcripts/scripts/tests/test_transcripts_second_reader.py")
P18_NAMES = ["test_second_reader_from_builder", "test_second_reader_in_named_readers", "test_no_other_reader_widened"]


def g18():
    if not COVERAGE.exists():
        return False, "absent: %s" % COVERAGE.as_posix()
    m = re.search(r"```json\s*(\[.*?\])\s*```", COVERAGE.read_text(encoding="utf-8"), re.S)
    if not m:
        return False, "no json block"
    rows = json.loads(m.group(1))
    ids = [r.get("fwd") for r in rows]
    if sorted(ids) != sorted(FWDS):
        return False, "fwd set %s != %s" % (ids, FWDS)
    bad = [r["fwd"] for r in rows if not ((r.get("act") and r.get("invocation") and r.get("read")) or r.get("missing_hop"))]
    if bad:
        return False, "incomplete rows %s" % ", ".join(bad)
    return True, "%d rows" % len(rows)


def p18():
    if not P18_TEST.exists():
        return False, "absent: %s" % P18_TEST.as_posix()
    text = P18_TEST.read_text(encoding="utf-8")
    missing = [n for n in P18_NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(P18_TEST), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= len(P18_NAMES)), tail


CHECKS = {"g18": ("R18-G18", g18), "p18": ("R18-P18", p18)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r18_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
