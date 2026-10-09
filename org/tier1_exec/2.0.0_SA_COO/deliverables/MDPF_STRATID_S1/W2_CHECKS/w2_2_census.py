"""MDPF_STRATID workstream 2, W2-2 criterion AC3: the census of every hard-coded copy that decides Opal strategy identity exists,
with a DENOMINATOR line and one row per copy whose disposition is REPLACED or KEPT (with a reason). W22-CENSUS-OK, else
W22-CENSUS-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import re
import sys

PATH = "org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~5/IDENTITY_COPY_CENSUS.md"


def main() -> int:
    try:
        with open(PATH, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        print("W22-CENSUS-BAD no file %s" % PATH)
        return 1
    m = re.search(r"^DENOMINATOR:\s*(\d+)", text, re.M)
    rows = re.findall(r"^\|[^|\n]+\|[^|\n]+\|\s*(REPLACED|KEPT)\s*\|", text, re.M)
    if not m:
        print("W22-CENSUS-BAD no DENOMINATOR line")
        return 1
    if int(m.group(1)) != len(rows):
        print("W22-CENSUS-BAD DENOMINATOR %s but %d disposition row(s)" % (m.group(1), len(rows)))
        return 1
    print("DENOMINATOR %s; REPLACED %d, KEPT %d" % (m.group(1), rows.count("REPLACED"), rows.count("KEPT")))
    print("W22-CENSUS-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
