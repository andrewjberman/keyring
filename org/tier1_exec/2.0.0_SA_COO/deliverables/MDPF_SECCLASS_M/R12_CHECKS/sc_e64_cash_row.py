#!/usr/bin/env python3
"""sc_e64_cash_row.py -- MDPF_SECCLASS round 10 SC-e-64 (PRD v0.14, ruling 2.4): Cash is a sub-class of cash only.

READ-ONLY, no AWS. ok when (a) the constituents seeder's build_row("CASH", "Cash & Cash Equivalents", "Fixed Income",
"Ultra Short Duration", ts) returns asset_class "cash" and sub_asset_class "Cash"; (b) the contract's values_by_class lists
"Cash" under cash and not under fixed_income; (c) a money-market fund row (SALXX) does not become cash/Cash (the control:
only the CASH residual line moves). Prints SC-E64 ok=<bool>.
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path.cwd()  # the repo root the worker runs from (its own worktree), never this file's tree
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
SEEDER = ROOT / "infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py"
CONTRACT = ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json"
TS = "2026-10-07T00:00:00Z"


def main():
    for p in (str(SHARED), str(SEEDER.parent)):
        if p not in sys.path:
            sys.path.insert(0, p)
    spec = importlib.util.spec_from_file_location("seed_constituents_e64", SEEDER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    cash = mod.build_row("CASH", "Cash & Cash Equivalents", "Fixed Income", "Ultra Short Duration", TS)
    mmf = mod.build_row("SALXX", "x", "Fixed Income", "Ultra Short Duration", TS)
    vbc = json.loads(CONTRACT.read_text(encoding="utf-8"))["fields"]["sub_asset_class"]["values_by_class"]
    a = cash.get("asset_class") == "cash" and cash.get("sub_asset_class") == "Cash"
    b = "Cash" in vbc.get("cash", []) and "Cash" not in vbc.get("fixed_income", [])
    c = not (mmf.get("asset_class") == "cash" and mmf.get("sub_asset_class") == "Cash")
    ok = a and b and c
    print(f"SC-E64 ok={ok} cash_row={cash.get('asset_class')}/{cash.get('sub_asset_class')} "
          f"contract_cash_in_fixed_income={'Cash' in vbc.get('fixed_income', [])} "
          f"salxx={mmf.get('asset_class')}/{mmf.get('sub_asset_class')}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
