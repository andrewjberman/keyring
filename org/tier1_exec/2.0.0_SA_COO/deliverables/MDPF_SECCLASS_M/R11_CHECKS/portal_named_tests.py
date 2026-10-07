#!/usr/bin/env python3
"""portal_named_tests.py -- MDPF_SECCLASS round 9 issuer check for the portal cells (SC-e-51, SC-e-52, SC-e-53).

Usage (repo root): python <this file> <portal-relative test file> <test-name filter>
Runs `bun test <file> -t <filter>` in <worktree>/portal with a 110 s bound and parses bun's own summary counts.
Prints PORTAL-TESTS ok=<bool> pass=<n> fail=<n> rc=<n> file=<file> filter=<filter>.
ok=True only when bun exits 0, fail == 0 and pass >= 1 (a filter that selects nothing, or an absent file, is not a pass).
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]


def bun():
    found = shutil.which("bun")
    if found:
        return found
    home = Path(os.path.expanduser("~")) / ".bun" / "bin"
    for name in ("bun.exe", "bun"):
        if (home / name).exists():
            return str(home / name)
    return None


def main(argv):
    if len(argv) != 3:
        print("PORTAL-TESTS ok=False reason=usage: <portal-relative test file> <filter>")
        return 2
    rel, flt = argv[1], argv[2]
    portal = ROOT / "portal"
    if not (portal / rel).exists():
        print(f"PORTAL-TESTS ok=False pass=0 fail=0 rc=-3 file={rel} filter={flt} reason=absent")
        return 1
    exe = bun()
    if exe is None:
        print(f"PORTAL-TESTS ok=False pass=0 fail=0 rc=-1 file={rel} filter={flt} reason=bun-not-found")
        return 1
    try:
        r = subprocess.run([exe, "test", rel, "-t", flt], cwd=str(portal), capture_output=True, text=True, timeout=110, check=False)
    except subprocess.TimeoutExpired:
        print(f"PORTAL-TESTS ok=False pass=0 fail=0 rc=-2 file={rel} filter={flt} reason=timeout")
        return 1
    text = re.sub(r"\x1b\[[0-9;]*m", "", (r.stdout or "") + (r.stderr or ""))
    p = re.search(r"(\d+) pass", text)
    f = re.search(r"(\d+) fail", text)
    npass = int(p.group(1)) if p else 0
    nfail = int(f.group(1)) if f else 0
    ok = r.returncode == 0 and nfail == 0 and npass >= 1
    if not ok:
        print(text[-1500:])
    print(f"PORTAL-TESTS ok={ok} pass={npass} fail={nfail} rc={r.returncode} file={rel} filter={flt}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
