"""NFRA_TRNSPT round 20 -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  x20   TR20-x20-AC1  live read-only wiring: S3 readers for the securities question and a completeness CLI for one meeting; reads only

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

T = "data/transcripts/scripts/tests/"
SPEC = {
    "x20": (T + "test_live_readers_exercise.py",
            ["test_s3_readers_read_only", "test_completeness_cli_one_meeting_cause", "test_securities_cli_counts_only"]),
}


def run(key):
    path, names = SPEC[key]
    test = Path(path)
    if not test.exists():
        return False, "absent: %s" % test.as_posix()
    text = test.read_text(encoding="utf-8")
    missing = [n for n in names if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(test), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= len(names)), tail


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in SPEC:
        print("usage: r20_checks.py {%s}" % "|".join(SPEC))
        sys.exit(2)
    ok, why = run(sys.argv[1])
    print("R20-%s-%s %s" % (sys.argv[1].upper(), "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
