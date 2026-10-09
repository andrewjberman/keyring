"""MDPF_SECHIST round 3: run one pytest file and require each NAMED test to have run and passed.

Usage: python r3_named_tests.py <LABEL> <test file, repo-relative> <test name> [<test name> ...]
A missing file, a missing name, a skip or a failure is BAD; the check never edits anything.

Last line: <LABEL>-TESTS-OK passed=<n>/<n>   or   <LABEL>-TESTS-BAD <reason>.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys


def main(argv: list[str]) -> int:
    if len(argv) < 4:
        print("usage: r3_named_tests.py LABEL TESTFILE NAME [NAME ...]")
        return 2
    label, test_file, names = argv[1], argv[2], argv[3:]
    if not os.path.isfile(test_file):
        print(f"{label}-TESTS-BAD missing-file={test_file}")
        return 1
    run = subprocess.run([sys.executable, "-m", "pytest", "-v", "-p", "no:cacheprovider", test_file],
                         capture_output=True, text=True)
    out = run.stdout + run.stderr
    print(out[-4000:])
    passed, bad = [], []
    for n in names:
        if re.search(r"::" + re.escape(n) + r"(\[[^\]]*\])? PASSED", out):
            passed.append(n)
        else:
            bad.append(n)
    if bad:
        print(f"{label}-TESTS-BAD not-passed={','.join(bad)}")
        return 1
    print(f"{label}-TESTS-OK passed={len(passed)}/{len(names)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
