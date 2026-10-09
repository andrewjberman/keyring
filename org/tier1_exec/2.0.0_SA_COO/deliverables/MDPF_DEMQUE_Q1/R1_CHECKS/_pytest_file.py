"""Shared helper for the MDPF_DEMQUE round 1 checks: run one pytest file from the demand-queue folder (its siblings
import the modules bare) and require each named test PASSED by name. A missing file reads as BAD, never as an error.

  python _pytest_file.py <test_file> <OK_TOKEN> <BAD_TOKEN> <test_name> [<test_name> ...]
"""
from __future__ import annotations

import os
import subprocess
import sys

HOME = os.path.join("data", "mdpf", "scripts", "demque")


def run(test_file: str, ok_token: str, bad_token: str, required: list[str]) -> int:
    if not os.path.isfile(os.path.join(HOME, test_file)):
        print("%s no file %s" % (bad_token, os.path.join(HOME, test_file)))
        return 1
    env = dict(os.environ)
    env.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    r = subprocess.run([sys.executable, "-m", "pytest", "-v", "-p", "no:cacheprovider", test_file],
                       capture_output=True, text=True, timeout=110, check=False, cwd=HOME, env=env)
    out = r.stdout + r.stderr
    print(out[-3000:])
    missing = [t for t in required if not any(t in ln and "PASSED" in ln for ln in out.splitlines())]
    if missing:
        print("%s not-passed=%s rc=%d" % (bad_token, ",".join(missing), r.returncode))
        return 1
    print(ok_token)
    return 0


def run_cli(args: list[str], timeout: int = 110) -> tuple[int, str]:
    """Run one module CLI from the repo root; return (rc, combined output). A missing module reads as rc 127."""
    if not os.path.isfile(args[0]):
        return 127, "no file " + args[0]
    r = subprocess.run([sys.executable] + args, capture_output=True, text=True, timeout=timeout, check=False)
    return r.returncode, r.stdout + r.stderr


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 4:
        print("USAGE: _pytest_file.py <test_file> <OK> <BAD> <test_name>...")
        sys.exit(2)
    sys.exit(run(a[0], a[1], a[2], a[3:]))
