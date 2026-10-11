"""MDPF_DEMQUE round 8, DQ-t-29 criterion AC2: the whole demque test folder COLLECTS (D1-S7). `pytest --collect-only -q` over
data/mdpf/scripts/demque exits 0, prints no INTERNALERROR and names at least one test of test_demque_land.py. COLLECT-OK n=<tests>;
else COLLECT-BAD <why>. Collection only: no test body runs, no network.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

HOME = os.path.join("data", "mdpf", "scripts", "demque")

if __name__ == "__main__":
    env = dict(os.environ)
    env.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    r = subprocess.run([sys.executable, "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider", HOME],
                       capture_output=True, text=True, timeout=110, check=False, env=env)
    out = r.stdout + r.stderr
    print(out[-1500:])
    land = [ln for ln in out.splitlines() if "test_demque_land.py::" in ln]
    if r.returncode != 0 or "INTERNALERROR" in out or not land:
        print("COLLECT-BAD rc=%d internalerror=%s land_tests=%d" % (r.returncode, "INTERNALERROR" in out, len(land)))
        sys.exit(1)
    m = re.search(r"(\d+) tests? collected", out)
    print("COLLECT-OK n=%s land=%d" % (m.group(1) if m else len([x for x in out.splitlines() if "::" in x]), len(land)))
    sys.exit(0)
