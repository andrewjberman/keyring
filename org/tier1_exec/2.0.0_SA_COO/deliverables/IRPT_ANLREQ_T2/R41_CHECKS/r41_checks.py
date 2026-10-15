"""IRPT_ANLREQ round 41, workstream T -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  fg1  R41-FG1  the commentary drafter builds the prompt's figure block from the closed C-COMM-FIG members only, logs the prompt by
                field name, and a planted client name or dollar amount never reaches the prompt (three named tests pass)
  fg2  R41-FG2  entry.abstract_request carries the figures block from the reader's commentary_basis (one named test passes)

Prints R41-<TOKEN>-OK or R41-<TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or a worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TEST_FILE = Path("data/transcripts/scripts/tests/test_commentary_figures.py")
NAMES = {
    "fg1": ["test_figures_whitelist_drops_unknown_members_and_bad_tickers",
            "test_prompt_carries_figures_block_and_no_planted_name_or_dollar",
            "test_provenance_lists_prompt_fields_by_name_only"],
    "fg2": ["test_abstract_request_carries_figures_from_basis"],
}
ANSI = re.compile(r"\x1b\[[0-9;]*m")


def _run(names):
    exprs = " or ".join(names)
    r = subprocess.run([sys.executable, "-m", "pytest", str(TEST_FILE), "-q", "-p", "no:cacheprovider", "-k", exprs],
                       capture_output=True, text=True, timeout=300)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""]
    tail = ANSI.sub("", lines[-1])
    m = re.search(r"(\d+) passed", tail)
    return r.returncode, (int(m.group(1)) if m else 0), tail


def check(key):
    if not TEST_FILE.exists():
        return False, "absent: %s" % TEST_FILE.as_posix()
    text = TEST_FILE.read_text(encoding="utf-8")
    missing = [n for n in NAMES[key] if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    rc, passed, tail = _run(NAMES[key])
    return (rc == 0 and passed >= len(NAMES[key])), tail


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in NAMES:
        print("usage: r41_checks.py {fg1|fg2}")
        sys.exit(2)
    ok, why = check(sys.argv[1])
    print("R41-%s-%s %s" % (sys.argv[1].upper(), "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
