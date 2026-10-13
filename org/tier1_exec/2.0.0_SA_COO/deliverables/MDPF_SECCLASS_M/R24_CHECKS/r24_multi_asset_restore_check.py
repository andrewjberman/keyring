#!/usr/bin/env python3
"""r24_multi_asset_restore_check.py -- MDPF_SECCLASS round 24 cell SC-e-100 (CTO round-23 analysis ADDENDUM 2, msg 4622): the frozen v1
HoldingsSnapshot schema admits `multi_asset` again, in all five asset-class enums of each of its three copies, and nothing else changed.
Run from the repo root being graded.  READ-ONLY (git show, file reads).

Usage:  python r24_multi_asset_restore_check.py

For each copy (docs/contracts/investor-reporting/v1/, infra/aws/lambda/investor-reporting/_contracts/,
infra/aws/lambda/investor-reporting/holdings/contracts/ -- `HoldingsSnapshot.schema.json`):
  - the file parses as JSON;
  - removing every line that is exactly the enum member `"multi_asset",` (any indentation) yields the file at the pinned BASE commit,
    byte for byte (LF-normalised): nothing but those lines was added;
  - exactly 5 such lines were removed, and each sits between `"commodities",` and `"cash",` (the position the port took it from);
  - the pre-port file (01e843ce2e^) had the same 5 members at the same positions in the same shape (the control that says what
    "restored" means).
Prints  MULTI-ASSET-RESTORE ok=<bool> copies=<n of 3> members=<total> base_equal=<bool> positions=<bool> control=<bool>
"""
import json
import re
import subprocess
import sys
from pathlib import Path

BASE = "6b6c2c51bd55"          # trunk at the cut; the restored file minus the member lines must equal this file
PORT_PARENT = "01e843ce2e^"    # the commit before the TO-SC-e62 release port removed the members
COPIES = [
    "docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json",
    "infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json",
    "infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json",
]
MEMBER = re.compile(r'^[ \t]*"multi_asset",[ \t]*$')


def git_show(ref, path):
    out = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True)
    if out.returncode != 0:
        return None
    return out.stdout.decode("utf-8").replace("\r\n", "\n")


def strip_members(text):
    kept, n = [], 0
    for line in text.split("\n"):
        if MEMBER.match(line):
            n += 1
        else:
            kept.append(line)
    return "\n".join(kept), n


def positions_ok(text):
    """every `"multi_asset",` line has `"commodities",` directly above and `"cash",` directly below."""
    lines = text.split("\n")
    found = 0
    for i, line in enumerate(lines):
        if MEMBER.match(line):
            found += 1
            if not (i > 0 and lines[i - 1].strip() == '"commodities",' and i + 1 < len(lines) and lines[i + 1].strip() == '"cash",'):
                return False, found
    return True, found


def main():
    root = Path.cwd()
    copies_ok = members = 0
    base_equal = positions = control = True
    for rel in COPIES:
        p = root / rel
        if not p.is_file():
            base_equal = positions = control = False
            continue
        text = p.read_bytes().decode("utf-8").replace("\r\n", "\n")
        try:
            json.loads(text)
            parses = True
        except ValueError:
            parses = False
        stripped, n = strip_members(text)
        base = git_show(BASE, rel)
        eq = base is not None and stripped == base
        pos_ok, npos = positions_ok(text)
        parent = git_show(PORT_PARENT, rel)
        c_ok = False
        if parent is not None:
            pstrip, pn = strip_members(parent)
            c_ok = pn == 5 and positions_ok(parent) == (True, 5)
        members += n
        base_equal = base_equal and eq
        positions = positions and pos_ok and npos == 5 and n == 5
        control = control and c_ok
        if parses and eq and pos_ok and n == 5 and c_ok:
            copies_ok += 1
    ok = copies_ok == 3 and members == 15 and base_equal and positions and control
    print(f"MULTI-ASSET-RESTORE ok={ok} copies={copies_ok} of 3 members={members} base_equal={base_equal} "
          f"positions={positions} control={control}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
