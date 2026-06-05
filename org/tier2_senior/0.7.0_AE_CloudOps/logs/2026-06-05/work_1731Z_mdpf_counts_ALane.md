# MDPF_COUNTS — AE~A producer/pipeline confirm + validated solution incl backfill

**archetype:** DIAGNOSE
**Agent:** 0.7.0_AE_CloudOps~A · **Date:** 2026-06-05 · **Project:** MDPF_COUNTS (investigation-first, read-only)
**Doc-of-record:** docs/briefs/mdpf-counts-producer-confirm-stale-rollup-deploy-20260605.md (commit 5418ad8c0)

## Task
COO DRIVE TO (~A dedicated lane): confirm at producer/pipeline whether MDPF Account-Count time-series loss is (b) backend stopped emitting count vs (c) aggregate count never built. Discriminate before any fix. C1: no manufactured/ad-hoc gold runs. Andrew-direct mid-investigation: "find the solution too, not just the source" + "include how we backfill this."

## Findings (all ground-truth, read-only)
- **(b) ROOT CAUSE = STALE-DEPLOYED ROLLUP.** Nightly Stage-4 (mdpf-daily-dispatch.sh ROLLUP step, EC2 i-02448edb) syncs `build_aggregate_aua_timeseries.py` from `s3://opal-data-mdpf/code/scripts/backfill/` — that S3 copy is **2026-06-01 14:20, 0 `account_count` refs**, predating the W2D commit `6de57eddc` (2026-06-02, committed copy = 8 refs). Live partitions DO carry real `account_count` both firms (6/05 49F=[3038,1580,1420,676,171..], inflection=[177,143,70..]); served by_model has NO `account_count` key → FE `?? 0` = empty everywhere.
- **(c) Global structurally count-less.** `slice_per_firm()` global slice spreads only aggregate $-metrics; no by_model/account_count. Even a fresh deploy won't populate Global. Plus the live Global view currently reads a LEGACY `portfolios/aum-timeseries.json` (getAUMTimeSeries) produced by the smartx-exporter pipeline — an MDLP_DISTFIX R5 decommission candidate (EC2 stopped Jun 1).
- **Backfill SOURCE FOUND + VALIDATED.** Pre-5/18 partitions have NULL counts (backfill grain never carried it), so a redeploy leaves history null. 49F holdings = all SmartX (Andrew-confirmed). `s3://opal-data-smartx-v2/consolidated/smartx_allocations.parquet` = 8,950 account-level AllocationId, ModelName (5 core), AllocationStatus, monthly Period back to 202409. `account_count = nunique(AllocationId WHERE Open) per ModelName per PeriodEnd` → step-carry to daily. **Validated:** 202605-derived {ConsGrowth 3008, Int 1576, LTA 1419, ST 668, UST 169} reproduce live 5/18 partition [2952,1560,1421,656,169] within month-vs-daily drift (UST exact 169). pre-5/18 Global==49F so same series backfills Global. SMA cohorts + Inflection (Eclipse, ~3 days) legitimately null pre-5/18.

## Solution (3 parts, NOT executed — fix-phase plan, awaiting COO GO)
1. Redeploy committed rollup to S3 → next scheduled nightly emits 49F+Inflection live counts (no code/backfill, C1-safe).
2. Author aggregate `account_count` in Global slice (cross-firm per-model sum) + FE re-point Global off legacy → MDPF 'global' slice (DE~A).
3. SmartX-allocations backfill for pre-5/18 49F+Global history (monthly→step-carry).

## Corroboration
DE~A (artifact↔producer boundary, 86d77d8f5) + base-AE (peer-handoff) independently pinned the same stale-deploy root cause. CTO ACCEPTED (172928Z): (b)+(c) confirmed, FE (a) ruled out; elevated my governance note → structural comp-tool fix (comp-pipescript deployed only checks opal-data-bd, blind to opal-data-mdpf + backfill/ paths — same class as today's yield-curve stranded-deploy).

## Compiler Tools
- `comp-pipescript deployed build_aggregate_aua_timeseries.py` / `mdpf_aggregate_aua.py` → both NO MATCH (filter only covers `s3://opal-data-bd/code/{gold,silver}/`; MDPF lives in opal-data-mdpf + backfill/ path). **Gap surfaced + routed to CTO/COO as a structural widen.** Direct `aws s3 ls`/`cp` of the deployed S3 copy was the substitute that produced the decisive stale-deploy evidence.

## RAVC
RAVC2 → COO (172810Z) + addendum (173119Z Global) ; CC CTO (172818Z, accepted 172928Z); peer-ack → DE~A (173107Z). Next: await COO fix-phase GO.
