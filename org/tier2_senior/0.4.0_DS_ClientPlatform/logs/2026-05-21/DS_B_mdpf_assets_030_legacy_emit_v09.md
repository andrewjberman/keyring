# DS~B Session Log -- MDPF_ASSETS.030 (legacy-emit v0.9 re-scope)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**Branch:** CLOUD
**TO:** MDPF_ASSETS.030 -- legacy-emit v0.9 re-scope + historical non_model_assets.json backfill (amendment A1)

## Summary

Brought build_legacy_compat_emit.py (the SoT for the live Model Portfolios
page's non_model_assets.json + aum-timeseries.json) to the PRD v0.9 basis, and
backfilled the historical non_model_assets.json series. The live page now
reconciles to-the-cent against the v0.9 platinum series.

## Phases

- **Phase 0** -- found the emitter on the superseded CEO-direct 2026-05-19
  "broader" full-BD-book basis (compute_49f_broader_custody overriding the
  platinum v0.9 1b). Edit plan A-E; live-page delta -$150.18M.
  Brief: docs/briefs/mdpf-assets-030-phase0-legacy-emit-v09-editplan-20260521.md.
- **Phase 1-2** -- v0.9 re-scope; reconciliation surfaced a $614K Inflection-2a
  residual (emitter's independent Eclipse recompute vs the platinum 2a).
  Brief: ...phase2-reconciliation-inflection-gap...
- **AC2 ruling** -- CTO~B + COO~B ruled Option 1: re-source Inflection from the
  platinum partition. derive_inflection_from_platinum() added; the 4
  load_inflection call sites swapped. Re-run: to-the-cent.
- **Phase 3** -- commit 82d3f8113, deploy (md5 MATCH), emit --upload: the live
  publish (the -$150.18M move).
- **Phase 5** -- CUTOVER 2026-01-16 -> 2025-12-23 (commit 60dd8d5a9), re-emit:
  the full .029 v0.9 range backfilled into non_model_assets.json.

## Verification

| check | result |
|-------|--------|
| non_model_assets.json enterprise_total vs .029 platinum headline | $0.00 to-the-cent (2026-01-20, 03-13, 05-19, 05-20) |
| method=v0_9 rows | 93, from 2025-12-23 |
| live-page headline before -> after | $1,898,213,922.32 -> $1,748,030,393.45 (-$150.18M) |
| boundary | continuous v0.9, no v0.8/v0.9 cliff |
| $614K Inflection residual | characterized VINTAGE (same Eclipse file+column, different snapshot) -- no methodology finding |

## Files Modified

| File | Change |
|------|--------|
| data/mdpf/scripts/backfill/build_legacy_compat_emit.py | v0.9 re-scope (broader override removed; Cohort 0 out of headline; Option-1 Inflection re-source via derive_inflection_from_platinum; CUTOVER->2025-12-23; dead code removed; methodology_version=v0_9) |

## Deploy cycle (Rule 13)

| Step | Result |
|------|--------|
| ds-commit-gate | exit 0 (Rule 14/15) every edit |
| Commits | 82d3f8113 (v0.9 re-scope + Option 1), 60dd8d5a9 (Phase-5 CUTOVER) |
| S3 deploy | s3://opal-data-mdpf/code/scripts/backfill/build_legacy_compat_emit.py md5 MATCH (both phases) |
| Emit | --upload x2 (Phase 3 + Phase 5); non_model_assets.json + aum-timeseries.json live on v0.9 |

## Non-destructive

opal-data-portal-v2 versioned; local pre-overwrite backups
(.runtmp/legacy_*_pre_overwrite.20260521T*.json). No object deleted.

## Compiler Tools

| Tool | Result |
|------|--------|
| ds-commit-gate.sh | exit 0 all edits |
| comp-* | data/mdpf off-graph (known gap); verification by direct S3 read -- to-the-cent reconciliation vs the platinum partitions |

## Current State

MDPF_ASSETS.030 COMPLETE. RAVC2 to COO~B CC CTO~B
(docs/briefs/mdpf-assets-030-ravc2-legacy-emit-v09-complete-20260521.md). The
MDPF v0.9 line is fully landed: .028 + .029 + .030.

## Next

| Recipient | Item |
|-----------|------|
| COO~B 2.0.0 | RAVC2 -- .030 complete. ADHC_VALGATE.003 (C-4) now resumable. |
| CTO~B 1.0.0 | CC on RAVC2. |
