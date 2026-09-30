"""Round 27 (~M) checks IBM27-271-AC1 and IBM27-272-AC2: a pytest directory passes WHOLE.

Usage: r27_suite_whole.py <tests-dir>. Runs `python -m pytest <tests-dir> -q -p no:cacheprovider` and prints
SUITE-WHOLE <summary line> only when pytest exits 0 with at least one test passed; otherwise SUITE-BROKEN <summary line>.
A literal `passed` would also match '6 failed, 306 passed', so the exit code decides, not the word.

Run from the repo (or worktree) root.
"""
import subprocess
import sys


def main():
    if len(sys.argv) != 2:
        print("SUITE-BROKEN usage: r27_suite_whole.py <tests-dir>")
        return 2
    r = subprocess.run([sys.executable, "-m", "pytest", sys.argv[1], "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True)
    lines = [ln for ln in (r.stdout or "").splitlines() if ln.strip()]
    summary = lines[-1] if lines else "(no output)"
    if r.returncode == 0 and "passed" in summary and "failed" not in summary and "error" not in summary:
        print("SUITE-WHOLE %s" % summary)
        return 0
    print("SUITE-BROKEN rc=%d %s" % (r.returncode, summary))
    return 1


if __name__ == "__main__":
    sys.exit(main())
