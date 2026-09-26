#!/usr/bin/env python3
"""Coverage check for the 2026-09-26 Investor Reporting UI review register.

Reads docs/briefs/irpt-ui-review-findings-20260926.json and reports, for each UIR id, whether it
appears in the given file (default: the DSGN_IRPTV1 PRD). Read-only; prints a count with its
denominator and every missing id. Exit 0 when all ids are present, 1 otherwise.

Usage: python docs/briefs/irpt-ui-review-coverage-check.py [path-to-file-that-must-cite-every-id]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                           text=True, check=True).stdout.strip())
REGISTER = ROOT / "docs/briefs/irpt-ui-review-findings-20260926.json"
DEFAULT_TARGET = ROOT / "org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md"


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_TARGET
    ids = [f["id"] for f in json.loads(REGISTER.read_text(encoding="utf-8"))["findings"]]
    text = target.read_text(encoding="utf-8")
    present = {m.group(0) for m in re.finditer(r"UIR-\d{2}", text)}
    missing = [i for i in ids if i not in present]
    print("OK:" if not missing else "WARN:", len(ids) - len(missing), "of", len(ids),
          "UIR ids present in", target)
    if missing:
        print("missing:", ", ".join(missing))
    return 0 if not missing else 1


if __name__ == "__main__":
    sys.exit(main())
