"""MDPF_STRATID workstream 2, W2-3 criterion AC2 (SEAM, real data): the recorded unidentified list for Cottonwood on its latest
Rebalancer date exists with SOURCE, DENOMINATOR and RESULT lines, and carries the known control `Opal_Muni_Income` (S07: a rule
with no member until a person verifies it). W23-SEAM-OK, else W23-SEAM-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import re
import sys

PATH = "org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~6/UNIDENTIFIED_STRATEGY_CANDIDATES.md"


def main() -> int:
    try:
        with open(PATH, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        print("W23-SEAM-BAD no file %s" % PATH)
        return 1
    for line in ("SOURCE:", "DENOMINATOR:", "RESULT:"):
        if not re.search(r"^" + line, text, re.M):
            print("W23-SEAM-BAD no %s line" % line)
            return 1
    if "Opal_Muni_Income" not in text:
        print("W23-SEAM-BAD the control Opal_Muni_Income is not listed")
        return 1
    print(re.search(r"^RESULT:.*$", text, re.M).group(0))
    print("W23-SEAM-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
