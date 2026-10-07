#!/usr/bin/env python3
"""sc_e53_keeps_multi_asset.py -- MDPF_SECCLASS SC-e-53 re-cut (laptop review 106245, CTO msg 437): portal composition.ts keeps
`multi_asset` in BOTH canonical class lists while a producer still serves it (row S60).

READ-ONLY, text read. In <worktree>/portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts, the `CANONICAL_CLASSES` and
`CANONICAL_CLASSES_WITH_CASH` array literals must each contain 'multi_asset', and a label 'Multi-Asset' must be present. Prints
SC-E53 ok=<bool>. Run from the super-repo worktree root.
"""
import re
import sys
from pathlib import Path

SRC = Path.cwd() / "portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts"


def members(text, name):
    m = re.search(r"\b" + name + r"\s*=\s*\[([^\]]*)\]", text)
    return re.findall(r"'([a-z_]+)'", m.group(1)) if m else None


def main():
    text = SRC.read_text(encoding="utf-8")
    a, b = members(text, "CANONICAL_CLASSES"), members(text, "CANONICAL_CLASSES_WITH_CASH")
    label = "'Multi-Asset'" in text
    ok = a is not None and b is not None and "multi_asset" in a and "multi_asset" in b and label
    print(f"SC-E53 ok={ok} classes_has={a is not None and 'multi_asset' in a} with_cash_has={b is not None and 'multi_asset' in b} label={label}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
