"""TR-x-2 AC1 -- the whole transcripts test suite passes in ONE pytest process (issuer's check; base: FAIL as expected).

Rows S6/S7/S8: every file passed alone while 22-23 failed together. This check runs the directory once and prints
SUITE-GREEN passed=N failed=0, else SUITE-RED passed=N failed=F (or SUITE-ERROR).
"""
import re
import subprocess
import sys


def main():
    r = subprocess.run([sys.executable, "-m", "pytest", "data/transcripts/scripts/tests", "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True)
    tail = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()][-1:] or [""]
    line = re.sub(r"\x1b\[[0-9;]*m", "", tail[0])
    passed = int((re.search(r"(\d+) passed", line) or [0, 0])[1])
    failed = int((re.search(r"(\d+) failed", line) or [0, 0])[1])
    errors = int((re.search(r"(\d+) error", line) or [0, 0])[1])
    if passed == 0 and failed == 0:
        print("SUITE-ERROR no result line: %s" % line)
        return 1
    if failed or errors:
        print("SUITE-RED passed=%d failed=%d errors=%d" % (passed, failed, errors))
        return 1
    print("SUITE-GREEN passed=%d failed=0" % passed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
