"""RB-s-7 contract checker -- ISSUER artifact (2.0.0_SA_COO~D), READ-ONLY to the worker.

Usage:  python rb7-contract-check.py canon     [path]   -> VERDICT: CANON-CLAUSE-ORDERED | CANON-CLAUSE-MISSING
        python rb7-contract-check.py inversion [path]   -> VERDICT: INVERSION-CARRIED   | INVERSION-MISSING
        path defaults to portal/DESIGN.md (run from the workspace worktree root).

A file rather than an inline one-liner because this round lost two criteria to shell-escaping defects.
Every arm prints its denominator; an absent or empty file can only read MISSING, so an empty sweep
cannot score as a clean pass.
"""
import io
import os
import re
import sys

ARM = sys.argv[1] if len(sys.argv) > 1 else ""
PATH = sys.argv[2] if len(sys.argv) > 2 else "portal/DESIGN.md"
TEXT = io.open(PATH, encoding="utf-8", errors="replace").read() if os.path.exists(PATH) else ""
print("FILE:", PATH, "EXISTS:", os.path.exists(PATH), "BYTES:", len(TEXT.encode("utf-8")))

# Andrew-direct 2026-09-11: value AND order locked -- UST ST INT LT ULT along the reading axis.
LADDER = [("UST", "F97316"), ("ST", "F59E0B"), ("INT", "10B981"), ("LT", "3B82F6"), ("ULT", "EF4444")]


def num(token):
    """A ratio token matched as a whole number: 4.8 must not match 4.85 or 14.8."""
    return re.compile(r"(?<![0-9.])" + re.escape(token) + r"(?![0-9])")


if ARM == "canon":
    up = TEXT.upper()
    present = {rung: ("#" + hx) in up for rung, hx in LADDER}
    print("CANON-HEXES:", sum(present.values()), "of", len(LADDER), present)
    # One ordered block: the five hexes in duration order, each within 600 chars of the previous.
    block = re.search(r"[\s\S]{0,600}?".join("#" + hx for _, hx in LADDER), up)
    print("ORDERED-BLOCK:", bool(block), ("offset %d span %d" % (block.start(), block.end() - block.start())) if block else "")
    ok = bool(TEXT) and all(present.values()) and bool(block)
    print("VERDICT:", "CANON-CLAUSE-ORDERED" if ok else "CANON-CLAUSE-MISSING")
elif ARM == "inversion":
    low = TEXT.lower()
    need = {
        "rule sentence": re.compile(re.escape("preserve the contrast ratio and the role")),
        "opacity 1.0": re.compile(r"opacity[^\n]{0,80}(?<![0-9.])1\.0(?![0-9])"),
        "positive 4.8": num("4.8"),
        "negative 6.4": num("6.4"),
        "warning 4.6": num("4.6"),
        "info 5.4": num("5.4"),
        "boundary floor 1.35": num("1.35"),
        "source cited": re.compile(re.escape("inversion-rule.json")),
    }
    miss = [k for k, rx in need.items() if not rx.search(low)]
    print("REQUIRED:", len(need), "MISSING:", len(miss), miss)
    ok = bool(TEXT) and not miss
    print("VERDICT:", "INVERSION-CARRIED" if ok else "INVERSION-MISSING")
else:
    print("usage: rb7-contract-check.py canon|inversion [path]")
    print("VERDICT: USAGE-ERROR")
    sys.exit(2)
