"""NFRA_TRNSPT round 6 -- the issuer's mechanical checks (2.0.0_SA_COO~T2), one subcommand per criterion.

  f6-build   TR6-f6-AC1  the completeness builder, run on the shipped fixture, gives every occurrence exactly one cause from
                         the five, every cause appears at least once, and the per-series counts sum to the occurrence count
  f6-test    TR6-f6-AC2  the completeness test file passes and holds the two refusal tests by name

Each prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import importlib
import json
import re
import subprocess
import sys
from pathlib import Path

TESTS = Path("data/transcripts/scripts/tests")
FIXTURE = TESTS / "fixtures" / "completeness" / "inputs.json"
CAUSES = {"here", "never_recorded", "expired", "refused", "not_allowlisted"}


def _pytest(path):
    if not path.exists():
        return False, "absent: %s" % path.as_posix()
    cmd = [sys.executable, "-m", "pytest", str(path), "-q", "-p", "no:cacheprovider"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=110)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()]
    tail = re.sub(r"\x1b\[[0-9;]*m", "", lines[-1] if lines else "")
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    if r.returncode != 0 or passed == 0:
        return False, "rc=%d %s" % (r.returncode, tail)
    return True, "passed=%d" % passed


def f6_build():
    if not FIXTURE.exists():
        return False, "absent: %s" % FIXTURE.as_posix()
    sys.path.insert(0, str(Path.cwd()))
    try:
        mod = importlib.import_module("data.transcripts.scripts.teams.completeness")
    except Exception as exc:  # the module is the build; its absence is the base state
        return False, "import: %s" % type(exc).__name__
    rec = mod.build(json.loads(FIXTURE.read_text(encoding="utf-8")))
    rows = rec.get("rows") if isinstance(rec, dict) else None
    if not rows:
        return False, "no rows"
    seen = set()
    for i, row in enumerate(rows):
        cause = row.get("cause")
        if cause not in CAUSES:
            return False, "row %d cause %r not one of the five" % (i, cause)
        seen.add(cause)
    if seen != CAUSES:
        return False, "causes missing from the fixture run: %s" % sorted(CAUSES - seen)
    counts = rec.get("counts") or {}
    total = sum(sum(c.values()) for c in counts.values()) if counts else -1
    if total != len(rows):
        return False, "per-series counts sum %d != rows %d" % (total, len(rows))
    return True, "rows=%d causes=5 series=%d" % (len(rows), len(counts))


def f6_test():
    path = TESTS / "test_completeness.py"
    if not path.exists():
        return False, "absent: %s" % path.as_posix()
    text = path.read_text(encoding="utf-8")
    for need in ("def test_refuse_row_without_cause", "def test_refuse_row_with_two_causes"):
        if need not in text:
            return False, "missing %s" % need
    return _pytest(path)


CHECKS = {"f6-build": ("R6-F6-BUILD", f6_build), "f6-test": ("R6-F6-TEST", f6_test)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r6_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
