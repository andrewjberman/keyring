#!/usr/bin/env python3
"""r8_multi_asset_reader_census.py -- MDPF_SECCLASS (CTO batch 164): which readers of etf-classifications admit `multi_asset`.

Runs R6_CHECKS/r6_model_reader_census.py (every reader through its REAL function on an in-memory table double, no AWS call)
with its synthetic rows replaced by `multi_asset` rows -- seven allocation funds the table holds today and three the acts withheld,
one per batch-164 sub class (Target Date, Fixed Mix, Flexible), classified_by seed. A reader that CRASHES, REFUSES or
FAILS-CONTRACT on them is one the readers packet must change before any row is written.

Run from the repo root: python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R8_CHECKS/r8_multi_asset_reader_census.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
R6 = HERE.parent / "R6_CHECKS" / "r6_model_reader_census.py"

ROWS = '''
_MULTI_ASSET_ROWS = [
    {"ticker": t, "name": n, "asset_class": "multi_asset", "sub_asset_class": s, "classified_by": "seed",
     "updated_by": "seed-script", "management_style": m,
     "low_confidence": False}  # the r6 summary line reads this key; False = not a model hedge
    for t, n, s, m in [
        ("AOR", "iShares Core Growth Allocation ETF", "Fixed Mix", "passive"),
        ("VSMGX", "Vanguard LifeStrategy Moderate Growth Fund", "Fixed Mix", "passive"),
        ("VTHRX", "Vanguard Target Retirement 2030 Fund", "Target Date", "passive"),
        ("VTIVX", "Vanguard Target Retirement 2045 Fund", "Target Date", "passive"),
        ("VWELX", "Vanguard Wellington Fund Investor", "Fixed Mix", "active"),
        ("ABALX", "American Funds American Balanced Fund Class A", "Fixed Mix", "active"),
        ("AAETX", "American Funds 2030 Target Date Retirement Fund Class A", "Target Date", "active"),
        ("MDLOX", "BlackRock Global Allocation Fund Investor A", "Flexible", "active"),
        ("KAGIX", "Kensington Dynamic Allocation Fund Institutional", "Flexible", "active"),
    ]
]


def build_model_rows() -> list:
    return [dict(r) for r in _MULTI_ASSET_ROWS]


'''


def main() -> int:
    src = R6.read_text(encoding="utf-8")
    anchor = "\nCONTROL_ROWS = ["
    assert src.count(anchor) == 1, "anchor moved in r6_model_reader_census.py"
    src = src.replace(anchor, "\n" + ROWS + anchor.lstrip("\n"), 1)
    src = src.replace("MODEL-READER-CENSUS", "MULTI-ASSET-READER-CENSUS").replace("MODEL-READER-TOLERATED", "MULTI-ASSET-READER-TOLERATED")
    code = compile(src, str(R6), "exec")
    g = {"__name__": "__main__", "__file__": str(R6)}
    exec(code, g)  # noqa: S102 -- runs the census module itself, with only its synthetic rows replaced
    return 0


if __name__ == "__main__":
    sys.exit(main())
