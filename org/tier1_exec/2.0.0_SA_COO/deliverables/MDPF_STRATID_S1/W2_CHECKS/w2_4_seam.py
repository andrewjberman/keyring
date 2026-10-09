"""MDPF_STRATID workstream 2, ST-w-4 criterion AC2 (SEAM, real data): the re-recorded Cottonwood unidentified list (amendment A1)
no longer lists an ordinary Opal Model (`Opal Satellite 50`, `Opal Short-Term`), does not list `Opal_Muni_Income` (A7, a Custom model), still lists the
control `Opal_Muni_Sleeve` (RULE_NOT_COUNTED), and carries SOURCE, DENOMINATOR, RESULT and EXCLUDED-AS-MODEL lines. W24-SEAM-OK, else W24-SEAM-BAD.
Run from the repo (worktree) root."""
from __future__ import annotations

import re
import sys

PATH = "org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~6/UNIDENTIFIED_STRATEGY_CANDIDATES.md"
MODELS = ("Opal Satellite 50", "Opal Short-Term", "Opal_Muni_Income")  # A7: Andrew-direct ~05:3xZ


def main() -> int:
    try:
        with open(PATH, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        print("W24-SEAM-BAD no file %s" % PATH)
        return 1
    for line in ("SOURCE:", "DENOMINATOR:", "RESULT:", "EXCLUDED-AS-MODEL:"):
        if not re.search(r"^" + line, text, re.M):
            print("W24-SEAM-BAD no %s line" % line)
            return 1
    rows = [ln for ln in text.splitlines() if ln.startswith("|")]
    listed = [m for m in MODELS if any("| %s |" % m in r for r in rows)]
    if listed:
        print("W24-SEAM-BAD Opal Model(s) still listed: %s" % listed)
        return 1
    if not any("Opal_Muni_Sleeve" in r and "RULE_NOT_COUNTED" in r for r in rows):
        print("W24-SEAM-BAD control Opal_Muni_Sleeve RULE_NOT_COUNTED not listed")
        return 1
    print(re.search(r"^RESULT:.*$", text, re.M).group(0))
    print(re.search(r"^EXCLUDED-AS-MODEL:.*$", text, re.M).group(0))
    print("W24-SEAM-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
