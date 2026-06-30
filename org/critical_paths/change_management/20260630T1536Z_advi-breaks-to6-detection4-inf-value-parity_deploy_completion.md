# Deploy-Completion Ledger — ADVI_BREAKS TO-6 detection-4: inf value-parity reader

**Status:** OPEN
**Opened:** 2026-06-30T15:36Z by 0.7.0_AE_CloudOps (executor)
**Deploy:** apply `infra/aws/compdiff/deploy/inf_value_parity.tf` (0.8.0~B-authored, committed 19237dc97) in a dedicated standalone TF root (`_root.tf`, state key `compdiff-inf-value-parity/tfstate`). The TO-6 detection-4 served-vs-source value-parity reader: hourly Lambda `opal-inf-value-parity` reads inf's OWN served header total_aua + inf's OWN silver positions_mv current_value sum, exact-match (no tolerance, Andrew-direct), publishes opal-critical-surface-alerts on a divergence. Firm-isolated (CTO option-b): inf-only GetObject, ZERO cross-firm, READ-ONLY (distinct from any enforcer write-role).
**Gates cleared:** CTO co-signed the plan (152820Z, same-measure arch condition grounded) + COO floor GO (153142Z, time-sensitive to capture the two-sided fire-test over the ~16:20Z inf recovery). Within-firm standard inf infra (NOT the cross-firm carve-out).
**Scope:** dedicated compdiff-inf-value-parity TF state (0.7.0_AE deploy lane). Single-Lambda safe-apply, HALT-gated. Lambda code = `infra/aws/compdiff/value_parity_reader.py` (inline archive_file). AWSSDKPandas-Python312:16 layer (validated live, pyarrow for the parquet anchor).
**Executor:** 0.7.0_AE_CloudOps. **Verify co-author:** 0.8.0_AE_CloudComp~B + CVO (the two-sided live fire-test).

| Leg | Type | Step | Status |
|---|---|---|---|
| L1 | source-map (Rule 4) | add `opal-inf-value-parity` entry to lambda-source-map.json | DONE |
| L2 | TF apply (safe-apply HALT-gate) | apply the 8 resources (RO role + 3 policies, lambda, event rule + target + permission) | OPEN |
| L3 | verify 0-diff | re-plan -> 0 change | OPEN |
| L4a | fire-on-stale (live) | invoke now -> reader FIRES on the stale 132B stub ($1.59M: served 202,582,215.84 != positions_mv 200,987,115.59) | OPEN |
| L4b | quiet-on-fresh (CVO co-sign) | post-~16:20Z recovery: served snaps to positions_mv to the cent -> reader EXACT-MATCH/QUIET = the two-sided proof; CVO co-signs -> TO-2 GREEN | OPEN |

**Closure:** all legs closed + RAVC COO + CTO + CVO at (a) reader-live+firing-on-stale, (b) quiet-on-fresh. Unclosed at session end = COO alarm.

## Log
- 20260630T1536Z OPENED. Plan clean (8 add / 0 change / 0 destroy) in the dedicated root. Layer :16 validated live (python3.12, pyarrow). Proceeding L2 (safe-apply) to capture the fire-on-stale half before the ~16:20Z recovery.
