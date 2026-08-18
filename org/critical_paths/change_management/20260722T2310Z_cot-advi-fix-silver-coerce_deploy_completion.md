# Deploy Completion — COT_ADVI_FIX silver coerce-numeric-first + 07-21/22 partition rewrite

**Status:** CLOSED 2026-07-22T~23:10Z (COMPLETE, verified)
<!-- scanner-alignment line added 2026-08-18 by 0.0.0_AB_MSTR (RED-disposition act, org/tier0_exec/0.0.0_AB_MSTR/deliverables/DEPLOY_LEDGER_RED_DISPOSITIONS_20260818.md): mirrors this file's own close declaration below; deploy_ledger.py's unindexed scanner could not read the original form (defects A/B/shape-C, see the disposition doc). Not a new closure. -->

**Ledger opened:** 2026-07-22T~23:05Z (deploy-start) · **Closed:** 2026-07-22T~23:10Z (COMPLETE, verified)
**Agent:** 0.4.0_DS_ClientPlatform (DS lane, Rule 13 — cot silver code + QA-deploy)
**Authorization:** CTO gate 224919Z (bounds verbatim in COO GO 225533Z) → COO GO (deadline-aware) 225533Z. TO: COT_ADVI_FIX (committed in parallel by COO).

## What deployed

1. **Code:** `data/cot/scripts/silver/cot_silver_merge.py` @ `2ed963ef6` → `s3://opal-data-cot/code/silver/cot_silver_merge.py`
   (via safe-deploy pre-push gate; **content-verified**: S3 ETag `bee95d18a61e28873fe739d54516b745` == local MD5, 35,351 B).
   - Coerce-numeric-first on numeric-bearing object columns before the generic string sweep
     (`:417-419` class). All-or-nothing per column (`errors='raise'`); pure-string columns never
     attempted; bool excluded; forced-string ID columns authoritative. NO fillna, NO filter.
   - Minimal `--force` (requires `--date`): forced rewrite path for a corrupt-silver/clean-bronze
     partition (the bronze-ETag skip predicate is structurally blind to this case).
2. **Data (recovery write, silver only, bronze untouched per 17a):** forced re-land of
   `silver/transactions/2026-07-21.parquet` + `2026-07-22.parquet` on opal-data-cot.

## Exercised verification (served artifacts, not self-report)

| Bound (CTO verbatim) | Result |
|---|---|
| units dtype float64 both partitions | PASS (read from S3 post-land) |
| row counts UNCHANGED | PASS — 07-21: 12,840 pre==post; 07-22: 11,620 pre==post (pre via versioned prior object `bBVhgwxm…`) |
| rows 157-158 read 9.6e-05 as float | PASS (`[9.6e-05, 9.6e-05]` at iloc 155:157) |
| 07-20 partition UNTOUCHED | PASS — ETag `0d24e87b97f8ae9db2d65260a791f8e4` identical before/after (positive control) |
| (added) full-schema parity vs clean 07-20 | PASS — zero dtype divergences across all 71 columns, both dates |
| (added) `.abs()` exercises clean (the A_03:1001 halt op) | PASS both partitions |

**NO ad-hoc gold run** (NEVER#4): the 02:04Z scheduled chain rebuilds gold+platinum from clean silver.
**Closure verification owner:** 0.7.0_AE_CloudOps (tomorrow: chain COMPLETE exit 0 + platinum advancing + `data_as_of` → 07-21/22). Notified 231xZ.

## Deferred by design (COO): the A_03 gold-side guard is a design question (silent coerce at gold could mask vendor drift; the loud halt arguably correct but consumer-less) — authored later, not tonight.
