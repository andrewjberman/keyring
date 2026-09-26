#!/usr/bin/env python3
"""Coverage check for a UI review register (default: the 2026-09-26 Investor Reporting review).

Reads a register JSON (`findings[].id`) and reports, for each id, whether it appears in the given file (default: the
DSGN_IRPTV1 PRD). Read-only; prints a count with its denominator and every missing id. Exit 0 when all ids are
present, 1 otherwise.

Usage:
  python docs/briefs/irpt-ui-review-coverage-check.py [--register REGISTER.json] [FILE-THAT-MUST-CITE-EVERY-ID]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                           text=True, check=True).stdout.strip())
DEFAULT_REGISTER = ROOT / "docs/briefs/irpt-ui-review-findings-20260926.json"
DEFAULT_TARGET = ROOT / "org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md"


def main() -> int:
    args = sys.argv[1:]
    register = DEFAULT_REGISTER
    if len(args) >= 2 and args[0] == "--register":
        register = Path(args[1])
        args = args[2:]
    target = Path(args[0]) if args else DEFAULT_TARGET
    ids = [f["id"] for f in json.loads(register.read_text(encoding="utf-8"))["findings"]]
    prefixes = sorted({re.sub(r"\d+$", "", i) for i in ids})
    text = target.read_text(encoding="utf-8")
    present = set()
    for p in prefixes:
        present |= {m.group(0) for m in re.finditer(re.escape(p) + r"\d+", text)}
    missing = [i for i in ids if i not in present]
    print("OK:" if not missing else "WARN:", len(ids) - len(missing), "of", len(ids),
          "ids from", register.name, "present in", target)
    if missing:
        print("missing:", ", ".join(missing))
    return 0 if not missing else 1


if __name__ == "__main__":
    sys.exit(main())
