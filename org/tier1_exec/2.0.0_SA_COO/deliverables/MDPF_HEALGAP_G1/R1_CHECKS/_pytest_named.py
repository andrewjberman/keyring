"""Shared helper for the MDPF_HEALGAP round 1 checks: run one pytest file from the runner's folder (its
siblings import `lambda_function` bare) and require each named test PASSED by name.
"""
from __future__ import annotations

import os
import subprocess
import sys

RUNNER = os.path.join("infra", "aws", "lambda", "cot-pipeline", "cot-rebalancer-runner")
TEST_FILE = "test_healgap_guard.py"


def run(required: list[str], ok_token: str, bad_token: str) -> int:
    env = dict(os.environ)
    env.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    r = subprocess.run([sys.executable, "-m", "pytest", "-v", "-p", "no:cacheprovider", TEST_FILE],
                       capture_output=True, text=True, timeout=110, check=False, cwd=RUNNER, env=env)
    out = r.stdout + r.stderr
    print(out[-3000:])
    missing = [t for t in required if not any(t in ln and "PASSED" in ln for ln in out.splitlines())]
    if missing:
        print(bad_token + " not-passed=" + ",".join(missing) + " rc=" + str(r.returncode))
        return 1
    print(ok_token)
    return 0
