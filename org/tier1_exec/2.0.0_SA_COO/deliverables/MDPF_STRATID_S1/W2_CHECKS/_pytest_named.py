"""Shared helper for the MDPF_STRATID round 1 checks: run one pytest file from the repo root and require each named
test PASSED by name (an empty name list requires rc 0 and at least one PASSED). A missing file reads as BAD, never as
an error.

  python _pytest_named.py <test_file> <OK_TOKEN> <BAD_TOKEN> [<test_name> ...]
"""
from __future__ import annotations

import os
import subprocess
import sys


def run(test_file: str, ok_token: str, bad_token: str, required: list[str]) -> int:
    if not os.path.isfile(test_file):
        print("%s no file %s" % (bad_token, test_file))
        return 1
    env = dict(os.environ)
    env.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    r = subprocess.run([sys.executable, "-m", "pytest", "-v", "-p", "no:cacheprovider", test_file],
                       capture_output=True, text=True, timeout=110, check=False, env=env)
    out = r.stdout + r.stderr
    print(out[-3000:])
    lines = out.splitlines()
    if required:
        missing = [t for t in required if not any(t in ln and "PASSED" in ln for ln in lines)]
    else:
        missing = [] if (r.returncode == 0 and any("PASSED" in ln for ln in lines)) else ["<suite>"]
    if missing:
        print("%s not-passed=%s rc=%d" % (bad_token, ",".join(missing), r.returncode))
        return 1
    print(ok_token)
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 3:
        print("USAGE: _pytest_named.py <test_file> <OK> <BAD> [<test_name>...]")
        sys.exit(2)
    sys.exit(run(a[0], a[1], a[2], a[3:]))
