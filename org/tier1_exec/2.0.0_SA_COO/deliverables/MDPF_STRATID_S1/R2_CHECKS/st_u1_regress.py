"""MDPF_STRATID round 2, ST-u-1 criterion AC3: round 1's seven Global-fold tests and the TaxSMA served-fold check still pass.
U1-REGRESS-OK when both pass; else U1-REGRESS-BAD naming the one that failed. Run from the repo (worktree) root."""
from __future__ import annotations

import os
import subprocess
import sys

R1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R1_CHECKS")


def main() -> int:
    for script, ok in (("st_t3_tests.py", "T3-OK"), ("st_t3_regress.py", "T3-REGRESS-OK")):
        r = subprocess.run([sys.executable, os.path.join(R1, script)], capture_output=True, text=True)
        last = (r.stdout.strip().splitlines() or [""])[-1]
        print("%s -> %s" % (script, last))
        if not last.startswith(ok):
            print("U1-REGRESS-BAD %s" % script)
            return 1
    print("U1-REGRESS-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
