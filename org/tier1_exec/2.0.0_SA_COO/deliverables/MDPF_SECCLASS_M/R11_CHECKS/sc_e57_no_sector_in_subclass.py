#!/usr/bin/env python3
"""sc_e57_no_sector_in_subclass.py -- MDPF_SECCLASS round 9, cell SC-e-57 (row S28; round-8 analysis section 3):
the FWD-10 planner stops writing a GICS sector into `sub_asset_class`; a resolved sector lands only in `gics_sector`.

READ-ONLY, no AWS. Imports infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py and plans three synthetic
canonical_shape records:
  US  -- `AAPL US Equity`, gics_status RESOLVED, gics_sector 'Information Technology';
  NON -- `BHP AU Equity`, gics_status RESOLVED, gics_sector 'Materials' (country AU -> region Developed);
  UNR -- `ZZZZ US Equity`, gics_status UNRESOLVED (no sector).
Expected after the fix:
  - no planned `sub_asset_class` is a GICS sector name (GICS_SECTORS);
  - US and NON carry `gics_sector` equal to their input sector;
  - NON keeps its country region `Developed` as `sub_asset_class` (the non-sector rule still applies);
  - UNR carries no `gics_sector`.
Prints SC-E57 ok=<bool> us_sub=<v> non_sub=<v> us_gics=<v> non_gics=<v> unr_gics=<v>. Run from the repo root.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path("infra") / "aws" / "lambda" / "v2_portal" / "_shared"))
import rivalfunds_classification as rc  # noqa: E402 -- the module under test, from the repo root

ROWS = {
    "us": {"security_bloomberg": "AAPL US Equity", "provider_security_type": "Equity", "gics_status": "RESOLVED",
           "gics_sector": "Information Technology", "security_name": "Apple Inc"},
    "non": {"security_bloomberg": "BHP AU Equity", "provider_security_type": "Equity", "gics_status": "RESOLVED",
            "gics_sector": "Materials", "security_name": "BHP Group"},
    "unr": {"security_bloomberg": "ZZZZ US Equity", "provider_security_type": "Equity", "gics_status": "UNRESOLVED",
            "gics_sector": None, "security_name": "Zzzz Corp"},
}


def main():
    plan = {k: rc.classify_canonical_row(v) or {} for k, v in ROWS.items()}
    subs = {k: p.get("sub_asset_class") for k, p in plan.items()}
    gics = {k: p.get("gics_sector") for k, p in plan.items()}
    ok = (
        not any(s in rc.GICS_SECTORS for s in subs.values() if s)
        and gics["us"] == "Information Technology"
        and gics["non"] == "Materials"
        and subs["non"] == "Developed"
        and gics["unr"] is None
    )
    print(f"SC-E57 ok={ok} us_sub={subs['us']} non_sub={subs['non']} us_gics={gics['us']} non_gics={gics['non']} "
          f"unr_gics={gics['unr']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
