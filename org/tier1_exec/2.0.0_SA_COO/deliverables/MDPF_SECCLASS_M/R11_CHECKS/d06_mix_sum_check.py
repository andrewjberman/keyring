#!/usr/bin/env python3
"""d06_mix_sum_check.py -- MDPF_SECCLASS round 9, cell SC-e-55 (remediation C-S13; round-8 analysis section 3):
49 Financial's firm mix serves its residual as its own "unclassified" line, so the top-level mix sums to 1.0.

READ-ONLY. Reads the newest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/D06_MIX_DRY_RUN_<yyyymmdd>.json: the payload the
D_06 emitter (data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py) wrote with `--out` from a LOCAL run against the live
canonical inputs, never uploaded. Checks:
  - the top-level `mix` keys are exactly {equity, fixed_income, alternatives, unclassified};
  - sum(mix[*].pct) is within 0.00001 of 1.0;
  - sum(mix[*].market_value) equals mix_periods[0].total_aua within 0.01;
  - CONTROL: mix.unclassified.market_value equals composition.unclassified.market_value (the residual the emitter already
    carries), so the new line is that residual, not a plug.
Prints D06-MIX-SUM ok=<bool> keys=<..> pct_sum=<..> mv_sum=<..> total=<..> control=<MATCH|DIFF|ABSENT>. Run from the repo root.
"""
import glob
import json
import os
import sys

HOME = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
WANT = {"equity", "fixed_income", "alternatives", "unclassified"}


def main():
    hits = sorted(glob.glob(os.path.join(HOME, "D06_MIX_DRY_RUN_*.json")))
    if not hits:
        print("D06-MIX-SUM ok=False reason=no D06_MIX_DRY_RUN_*.json")
        return 1
    with open(hits[-1], encoding="utf-8") as fh:
        p = json.load(fh)
    mix = p.get("mix", {})
    keys = set(mix)
    pct = sum(float(v.get("pct", 0)) for v in mix.values())
    mv = sum(float(v.get("market_value", 0)) for v in mix.values())
    total = float(p["mix_periods"][0]["total_aua"])
    comp_u = p.get("composition", {}).get("unclassified", {}).get("market_value")
    mix_u = mix.get("unclassified", {}).get("market_value")
    if comp_u is None or mix_u is None:
        control = "ABSENT"
    else:
        control = "MATCH" if abs(float(comp_u) - float(mix_u)) <= 0.01 else "DIFF"
    ok = keys == WANT and abs(pct - 1.0) <= 0.00001 and abs(mv - total) <= 0.01 and control == "MATCH"
    print(f"D06-MIX-SUM ok={ok} keys={sorted(keys)} pct_sum={pct:.6f} mv_sum={mv:,.2f} total={total:,.2f} control={control} "
          f"file={os.path.basename(hits[-1])}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
