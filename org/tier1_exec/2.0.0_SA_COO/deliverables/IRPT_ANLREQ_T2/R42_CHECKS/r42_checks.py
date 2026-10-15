"""IRPT_ANLREQ round 42, workstream T -- the issuer's mechanical check (2.0.0_SA_COO~T2).

  lg1  R42-LG1  the commentary Lambda's module logger emits INFO on its own (no test-side level override), so the COMMENTARY-POST line
                reaches CloudWatch: two named tests pass, one of which asserts the level with NO caplog.at_level

Prints R42-<TOKEN>-OK or R42-<TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or a worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TEST_FILE = Path("data/transcripts/scripts/tests/test_commentary_logging.py")
NAMES = ["test_module_logger_emits_info_without_any_test_side_override",
         "test_post_line_is_emitted_at_the_modules_own_level"]
ANSI = re.compile(r"\x1b\[[0-9;]*m")


def check():
    if not TEST_FILE.exists():
        return False, "absent: %s" % TEST_FILE.as_posix()
    text = TEST_FILE.read_text(encoding="utf-8")
    missing = [n for n in NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(TEST_FILE), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=300)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""]
    tail = ANSI.sub("", lines[-1])
    m = re.search(r"(\d+) passed", tail)
    passed = int(m.group(1)) if m else 0
    return (r.returncode == 0 and passed >= len(NAMES)), tail


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] != "lg1":
        print("usage: r42_checks.py lg1")
        sys.exit(2)
    ok, why = check()
    print("R42-LG1-%s %s" % ("OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
