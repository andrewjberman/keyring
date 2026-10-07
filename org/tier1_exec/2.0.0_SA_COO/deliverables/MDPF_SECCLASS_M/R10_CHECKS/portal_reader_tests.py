#!/usr/bin/env python3
"""MDPF_SECCLASS round 8, cell SC-e-23 (criterion SC8-e23-AC2): the two rewritten reader tests assert six classes, and pass.

Runs `bun test` in <portal> (default: <worktree>/portal) on the two reader test files, filtered to test names that
contain `six_class`, with a 110 s bound. Parses bun's own summary counts.

Prints one line:
  PORTAL-READERS ok=<bool> pass=<n> fail=<n> rc=<n>
ok=True only when bun exits 0, fail == 0 and pass >= 1 (a filter that selects nothing is not a pass).
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
FILES = [
    "src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-148.multi-asset-class-readers.test.ts",
    "src/pages/AdvisorIntelligence/__tests__/mdpf-secclass/multi-asset.readers.test.ts",
]


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
    portal = Path(argv[1]).resolve() if len(argv) > 1 else ROOT / "portal"
    exe = bun()
    if exe is None:
        print("PORTAL-READERS ok=False pass=0 fail=0 rc=-1 reason=bun-not-found")
        return 1
    try:
        r = subprocess.run([exe, "test", *FILES, "-t", "six_class"], cwd=str(portal),
                           capture_output=True, text=True, timeout=110, check=False)
    except subprocess.TimeoutExpired:
        print("PORTAL-READERS ok=False pass=0 fail=0 rc=-2 reason=timeout")
        return 1
    text = re.sub(r"\x1b\[[0-9;]*m", "", (r.stdout or "") + (r.stderr or ""))
    p = re.search(r"(\d+) pass", text)
    f = re.search(r"(\d+) fail", text)
    npass = int(p.group(1)) if p else 0
    nfail = int(f.group(1)) if f else 0
    ok = r.returncode == 0 and nfail == 0 and npass >= 1
    if not ok:
        print(text[-2000:])
    print(f"PORTAL-READERS ok={ok} pass={npass} fail={nfail} rc={r.returncode}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
