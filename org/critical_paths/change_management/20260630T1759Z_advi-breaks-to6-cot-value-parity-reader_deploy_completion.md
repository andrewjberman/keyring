# Deploy-Completion Ledger — ADVI_BREAKS TO-6 detection-4: cot value-parity reader

**Status:** CLOSED (2026-06-30T18:03Z — cot reader LIVE + dry-run verified; cot day-1 value-parity alarm live)
**Opened:** 2026-06-30T17:59Z by 0.7.0_AE_CloudOps (executor)
**Deploy:** apply `infra/aws/terraform/cot-value-parity/` (pre-staged 2665c5b33, anchor now filled). Hourly Lambda `opal-cot-value-parity` reads cot's served header total.aua + sums silver/holdings/{data_as_of}.parquet.market_value, exact-match (no tolerance), publishes opal-critical-surface-alerts on divergence. Firm-isolated (opal-data-cot only, GetObject RO, ZERO cross-firm).
**Gates cleared:** anchor PINNED (base-DS 174913Z, $0.00 delta over 11,336 rows) + CVO-RATIFIED + COO DRIVE GO (175907Z). Reuses 0.8.0~B's anchor-shape-robust value_parity_reader.py (372c87c64).
**Scope:** dedicated compdiff-cot-value-parity/tfstate (0.7.0_AE deploy lane). Single-Lambda safe-apply, HALT-gated.
**Executor:** 0.7.0_AE_CloudOps. **Co-verify:** 0.8.0~B (dry-run) + CVO.

| Leg | Type | Step | Status |
|---|---|---|---|
| L1 | anchor fill | drop VP_ANCHOR_KEY_TPL=silver/holdings/{date}.parquet + VP_ANCHOR_COLUMN=market_value + IAM prefix silver/holdings/*.parquet | DONE |
| L2 | TF apply (safe-apply HALT-gate) | apply the 8 resources (RO role + 3 policies, lambda, event rule + target + permission) | OPEN |
| L3 | verify 0-diff | re-plan -> 0 change | OPEN |
| L4 | dry-run | invoke {dry_run:true} -> reads cot served + silver/holdings, compares; expect FRESH/quiet-or-fired-correctly | OPEN |

**Closure:** all legs closed + RAVC COO + CVO at cot-reader-LIVE. Unclosed at session end = COO alarm.

## Log
- 20260630T1759Z OPENED. Anchor filled (L1 done). cot anchor is a SINGLE date-named .parquet at an exact key -> GetObject-only suffices (no ListBucket, unlike a multi-file prefix). Proceeding L2 safe-apply.
- 20260630T1803Z **ALL LEGS DONE -> CLOSED.** L2 safe-apply (HALT-gate clean) "Apply complete! 8 added, 0 changed, 0 destroyed"; opal-cot-value-parity live. L3 0-diff "No changes". L4 dry-run {dry_run:true} -> {firm:cot, fired:false, exit_code:0, disposition:FRESH} "served 432,464,116.36 matches cot market_value.sum[2026-06-26] to the cent". CORRECT behavior: cot's served VALUE is accurate vs silver/holdings (the cot freeze is the as_of-LAG, caught by the freeze-monitor DATA-AS-OF-FRONTIER-LAG, NOT a value mismatch) -> value-parity correctly quiet. **The cot day-1 no-tolerance value-regression alarm is LIVE** (fires if cot served value ever diverges from silver/holdings.market_value). 2 of 3 firms now carry the day-1 value-parity alarm (inf LIVE + proven two-sided; cot LIVE); 49F stays anchor-gated on 49F-DS's pin. RAVC'd COO+CVO.
