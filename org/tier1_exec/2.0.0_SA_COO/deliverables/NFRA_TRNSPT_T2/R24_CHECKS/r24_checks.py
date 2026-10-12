"""NFRA_TRNSPT round 24 -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  cm24  TR24-cm24-AC1  FWD-4: a listed, allowlisted meeting whose content read was refused classifies `refused` in the
                       completeness table (three named tests pass with the completeness suites)
  cl24  TR24-cl24-AC2  LIVE read-only: the one-meeting completeness query answers `refused` for each of the four Monday
                       meetings and `here` for a landed one

Prints R24-<TOKEN>-OK or R24-<TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or a worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TESTS = Path("data/transcripts/scripts/tests")
CM_SUITE = [TESTS / "test_completeness.py", TESTS / "test_live_readers_exercise.py", TESTS / "test_listing_snapshot_expired.py"]
CM_NAMES = {
    TESTS / "test_completeness.py": ["test_read_refused_listed_meeting_is_refused", "test_listed_without_read_refusal_still_raises"],
    TESTS / "test_live_readers_exercise.py": ["test_completeness_cli_read_refused_from_run_record"],
}
FOUR = ["2026-04-10", "2026-04-13", "2026-05-04", "2026-06-01"]
LANDED_DATE = "2026-10-05"
ANSI = re.compile(r"\x1b\[[0-9;]*m")


def _pytest(paths):
    r = subprocess.run([sys.executable, "-m", "pytest"] + [str(p) for p in paths] + ["-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=300)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""]
    tail = ANSI.sub("", lines[-1])
    m = re.search(r"(\d+) passed", tail)
    return r.returncode, (int(m.group(1)) if m else 0), tail


def cm24():
    missing = []
    for path, names in CM_NAMES.items():
        if not path.exists():
            return False, "absent: %s" % path.as_posix()
        text = path.read_text(encoding="utf-8")
        missing += [n for n in names if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    rc, passed, tail = _pytest(CM_SUITE)
    return (rc == 0 and passed >= 3), tail


def cl24():
    got = {}
    for date in FOUR + [LANDED_DATE]:
        r = subprocess.run([sys.executable, "data/transcripts/scripts/teams/completeness.py", "--live", "--series",
                            "monday_meeting", "--date", date], capture_output=True, text=True, timeout=120)
        last = (r.stdout.strip().splitlines() or [""])[-1]
        got[date] = last.split()[-1] if r.returncode == 0 and last else "ERROR(rc=%d)" % r.returncode
    facts = " ".join("%s=%s" % (d, got[d]) for d in FOUR + [LANDED_DATE])
    if any(got[d] != "refused" for d in FOUR):
        return False, facts
    if got[LANDED_DATE] != "here":
        return False, "positive control failed: " + facts
    return True, facts


if __name__ == "__main__":
    fns = {"cm24": cm24, "cl24": cl24}
    if len(sys.argv) != 2 or sys.argv[1] not in fns:
        print("usage: r24_checks.py {cm24|cl24}")
        sys.exit(2)
    ok, why = fns[sys.argv[1]]()
    print("R24-%s-%s %s" % (sys.argv[1].upper(), "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
