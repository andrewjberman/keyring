"""Shared helper for the MDPF_DEMQUE round 2 checks: run one pytest file from its own folder and require each named test PASSED
by name. A missing file reads as BAD, never as an error.
"""
from __future__ import annotations

import os
import subprocess
import sys


def run(home: str, test_file: str, ok_token: str, bad_token: str, required: list[str]) -> int:
    if not os.path.isfile(os.path.join(home, test_file)):
        print("%s no file %s" % (bad_token, os.path.join(home, test_file)))
        return 1
    env = dict(os.environ)
    env.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    r = subprocess.run([sys.executable, "-m", "pytest", "-v", "-p", "no:cacheprovider", test_file],
                       capture_output=True, text=True, timeout=110, check=False, cwd=home, env=env)
    out = r.stdout + r.stderr
    print(out[-3000:])
    missing = [t for t in required if not any(t in ln and "PASSED" in ln for ln in out.splitlines())]
    if missing:
        print("%s not-passed=%s rc=%d" % (bad_token, ",".join(missing), r.returncode))
        return 1
    print(ok_token)
    return 0
