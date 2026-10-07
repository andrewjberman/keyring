#!/usr/bin/env python3
"""r10_pytest_ok.py -- MDPF_SECCLASS round 8 issuer check: run pytest on the paths given and print ONE verdict token.

Why a file and not `pytest ... -> expect passed`: a run with failures prints "1 failed, 2 passed", which still contains
"passed". This prints PYTEST-OK only when pytest exits 0, collected at least one test and reports no failure or error;
otherwise PYTEST-BAD with the summary line. Usage: python r10_pytest_ok.py <path> [<path> ...]
"""
import subprocess
import sys


def main(argv):
    if not argv:
        print("PYTEST-BAD no paths given")
        return 2
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", *argv],
                       capture_output=True, text=True, timeout=110, check=False)
    out = (r.stdout or "") + (r.stderr or "")
    lines = [ln for ln in out.strip().splitlines() if ln.strip()]
    summary = lines[-1] if lines else "<no output>"
    bad = r.returncode != 0 or " passed" not in summary or "failed" in summary or "error" in summary
    print(f'{"PYTEST-BAD" if bad else "PYTEST-OK"!s} rc={int(r.returncode)} summary={summary!s}')
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
