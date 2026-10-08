"""NFRA_TRNSPT round 8, cell TR-s-8 -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  s8-all    TR8-s8-AC1  research_fold.build over research_transcripts/structured/*.json parses 29 of 29 with 0 failures, every row
                        carries exactly the teams silver COLUMNS, and per-file row counts sum to the row total
  s8-wipe   TR8-s8-AC2  the research-fold test file passes and holds the planted-token wipe test by name

Each prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root). Counts only.
"""
import glob
import importlib
import re
import subprocess
import sys
from pathlib import Path

TEST = Path("data/transcripts/scripts/tests/test_research_fold.py")


def s8_all():
    sys.path.insert(0, str(Path.cwd()))
    try:
        mod = importlib.import_module("data.transcripts.scripts.teams.research_fold")
        cols = importlib.import_module("data.transcripts.scripts.teams.parse_silver").COLUMNS
    except Exception as exc:  # the module is the build; its absence is the base state
        return False, "import: %s" % type(exc).__name__
    paths = sorted(glob.glob("research_transcripts/structured/*.json"))
    if len(paths) != 29:
        return False, "expected 29 structured files, found %d" % len(paths)
    res = mod.build(paths)
    rows, per_file, failures = res["rows"], res["per_file"], res["failures"]
    if failures:
        return False, "failures=%d first=%s" % (len(failures), failures[0].get("file"))
    if len(per_file) != 29:
        return False, "per_file covers %d of 29" % len(per_file)
    if sum(per_file.values()) != len(rows):
        return False, "per-file sum %d != rows %d" % (sum(per_file.values()), len(rows))
    bad = [i for i, r in enumerate(rows) if list(r.keys()) != list(cols)]
    if bad:
        return False, "%d rows not exactly the silver COLUMNS (first %d)" % (len(bad), bad[0])
    return True, "files=29 rows=%d failures=0" % len(rows)


def s8_wipe():
    if not TEST.exists():
        return False, "absent: %s" % TEST.as_posix()
    if "def test_planted_tokens_wiped_speaker_kept(" not in TEST.read_text(encoding="utf-8"):
        return False, "missing test_planted_tokens_wiped_speaker_kept"
    r = subprocess.run([sys.executable, "-m", "pytest", str(TEST), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed > 0), tail


CHECKS = {"s8-all": ("R8-S8-ALL", s8_all), "s8-wipe": ("R8-S8-WIPE", s8_wipe)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r8s_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
