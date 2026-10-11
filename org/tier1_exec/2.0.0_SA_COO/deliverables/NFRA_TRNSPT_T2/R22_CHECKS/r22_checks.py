"""NFRA_TRNSPT round 22 -- the issuer's mechanical check (2.0.0_SA_COO~T2).

  c22   TR22-c22-AC1  teams/census.py: the fetchable-on-cutoff set with its denominator, each entry landed or missing with a completeness cause;
                      a --live CLI that only reads; counts only
  rc22  TR22-rc22-AC1 the monday-skip replay: three named tests pass
  rf22  TR22-rf22-AC1 the pull survives a refused content read: three named tests pass and the pull's suites stay green

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

RC_TEST = Path("data/transcripts/scripts/tests/test_monday_skip_replay.py")
RC_NAMES = ["test_replay_skips_exactly_the_four", "test_skip_names_its_code_line", "test_scheduled_path_verdict_stated"]


def rc22():
    if not RC_TEST.exists():
        return False, "absent: %s" % RC_TEST.as_posix()
    text = RC_TEST.read_text(encoding="utf-8")
    missing = [n for n in RC_NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(RC_TEST), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= len(RC_NAMES)), tail


TEST = Path("data/transcripts/scripts/tests/test_census.py")
NAMES = ["test_cutoff_denominator_counts_only_on_or_before", "test_missing_entries_carry_a_completeness_cause",
         "test_live_reads_only_and_prints_no_text"]


def c22():
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
    return (r.returncode == 0 and passed >= len(NAMES)), tail


RF_TEST = Path("data/transcripts/scripts/tests/test_pull_read_refused.py")
RF_NAMES = ["test_refused_read_is_recorded_and_the_loop_continues", "test_run_completes_and_reaches_every_series",
            "test_run_wide_refusal_still_raises"]
RF_SUITE = [RF_TEST, RC_TEST, Path("data/transcripts/scripts/tests/test_teams_pull.py"),
            Path("data/transcripts/scripts/tests/test_pull_handler.py")]


def rf22():
    if not RF_TEST.exists():
        return False, "absent: %s" % RF_TEST.as_posix()
    text = RF_TEST.read_text(encoding="utf-8")
    missing = [n for n in RF_NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest"] + [str(p) for p in RF_SUITE] + ["-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=300)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= len(RF_NAMES)), tail


if __name__ == "__main__":
    fns = {"c22": c22, "rc22": rc22, "rf22": rf22}
    if len(sys.argv) != 2 or sys.argv[1] not in fns:
        print("usage: r22_checks.py {c22|rc22|rf22}")
        sys.exit(2)
    ok, why = fns[sys.argv[1]]()
    print("R22-%s-%s %s" % (sys.argv[1].upper(), "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
