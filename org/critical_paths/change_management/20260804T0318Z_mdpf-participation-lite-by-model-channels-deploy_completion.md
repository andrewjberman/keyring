# Deploy completion — participation-LITE (49F + inflection) + by_model_channels (global)

**Deployer:** 0.2.0_DS_PortfolioAnalytics · **Opened/closed:** 2026-08-04 03:10–03:18Z (single-leg, in-session)
**What:** `s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` → repo HEAD @2180c946e8 (MATCH).
**Authority:** CI-R6R ratified shape word CTO 20260804T030825Z (six binding conditions) ← my position 030649Z ← DE F-flags 030449Z ← v1.1 + participation ruling chain.

## The six conditions, each with its evidence

| # | Condition | Evidence |
|---|---|---|
| 1 | ONE VOCABULARY | Same `channel_participation` meta key + all v1.1 field names; `scope` is new-where-no-v1.1-name-exists; `last_carried_as_of` REUSED on per-firm rows (= last MEASURED as-of, glossed in the law text). DE pre-commit name flag sent 031649Z per their binding note |
| 2 | META-ONLY, DELTA=0 PROVEN | Three-artifact frozen-input parity (replay3 vs replay4): 49financial / inflection / global — **every VALUE field IDENTICAL** (dates, model_aua, non_model, custody, by_model, cohort_provenance, counts, point_class, opal_aggregate) |
| 3 | F-B DEMONSTRATED on real data | Controlled-axis dry-run (real inputs, axis extended to 08-05): tail rows 08-03/08-04 = within-window (`no_measured_value` + `last_carried_as_of 2026-07-31`), **08-05 = the past_window TRANSITION row** — visible, zero writes |
| 4 | by_model_channels measured-at-build | Predicate-not-roster (firm appears IFF its leg carried ≥1 non-None model_value): measured map = core-5 → [49financial, inflection, cottonwood]; growth/div SMA → [49financial]; both blends → [inflection]. partners{} stays dead per the 07-22 ruling |
| 5 | NOTHING on the DC1-held file | All edits in the dim file (deployed family). **Cottonwood-LITE split out** — its builder is the DC1-HELD slice; it rides that family when the hold lifts. CTO's ETag check (44db6559) unaffected |
| 6 | 49F explicit-null-with-reason | `windows_trading_days: {49financial: null}` + `windows_note_49financial` on the per-firm artifact itself |

Observed on the build: 49F LITE 0 exceptions (fully contributed — honest); inflection LITE 6 exceptions (the named eclipse gaps); global unchanged (28 exceptions, participation block intact); all gates PASS.

**Serve path:** staged artifacts gain the meta at the next scheduled 6d cycle → accrual → publisher (no hand-publish). DE pinged with the vintage when served copies carry it.
