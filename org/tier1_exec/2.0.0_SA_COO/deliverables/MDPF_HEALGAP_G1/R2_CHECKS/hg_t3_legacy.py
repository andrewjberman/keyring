"""MDPF_HEALGAP round 2, HG-t-3 criterion AC2: the runner's existing tests still pass (round 1's guard and induce tests
and the original suite). LEGACY-OK when both files run with rc=0 and at least one test each; else LEGACY-BAD.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

RUNNER = os.path.join("infra", "aws", "lambda", "cot-pipeline", "cot-rebalancer-runner")
FILES = ["test_healgap_guard.py", "test_lambda_function.py"]


def main() -> int:
    env = dict(os.environ)
    env.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    bad = []
    for f in FILES:
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", f],
                           capture_output=True, text=True, timeout=170, check=False, cwd=RUNNER, env=env)
        out = r.stdout + r.stderr
        m = re.search(r"(\d+) passed", out)
        n = int(m.group(1)) if m else 0
        print("%s rc=%d passed=%d" % (f, r.returncode, n))
        if r.returncode != 0 or n == 0:
            print(out[-1500:])
            bad.append(f)
    if bad:
        print("LEGACY-BAD " + ",".join(bad))
        return 1
    print("LEGACY-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
