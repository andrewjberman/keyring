"""NFRA_TRNSPT round 13 -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  g13   TR13-g13-AC1  the seam test file passes and holds, by name: the drafter's output carries generated_at (ISO-8601 UTC), and the
                      drafter's real output written through ticket_client against ~V2's section-5 stub returns ok/done (row D2-S6 fixed)

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TEST = Path("data/transcripts/scripts/tests/test_commentary_seam.py")
NAMES = ["test_draft_carries_generated_at", "test_drafter_output_writes_ticket_via_stub"]


def g13():
    if not TEST.exists():
        return False, "absent: %s" % TEST.as_posix()
    text = TEST.read_text(encoding="utf-8")
    missing = [n for n in NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(TEST), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= 2), tail


CHECKS = {"g13": ("R13-G13", g13)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r13_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
