"""MDPF_STRATID round 2, ST-u-2 criterion AC3: ST-u-1's tests and seam, round 1's Global-fold tests and the TaxSMA check still pass.
U2-REGRESS-OK when all pass; else U2-REGRESS-BAD naming the one that failed. Run from the repo (worktree) root."""
from __future__ import annotations

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    for script, ok in (("st_u1_tests.py", "U1-OK"), ("st_u1_seam.py", "SEAM-OK"), ("st_u1_regress.py", "U1-REGRESS-OK")):
        r = subprocess.run([sys.executable, os.path.join(HERE, script)], capture_output=True, text=True)
        last = (r.stdout.strip().splitlines() or [""])[-1]
        print("%s -> %s" % (script, last))
        if not last.startswith(ok):
            print("U2-REGRESS-BAD %s" % script)
            return 1
    print("U2-REGRESS-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
