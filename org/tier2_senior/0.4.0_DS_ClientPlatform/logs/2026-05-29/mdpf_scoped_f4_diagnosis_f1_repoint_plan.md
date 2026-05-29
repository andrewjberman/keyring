# MDPF_SCOPED — F4 diagnosis (49F 12/26 reclass) + F1 repoint plan

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE
**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-29
**Project:** MDPF_SCOPED maturation (CVO findings F1/F4/F5)
**PRD:** docs/architecture/MDPF_SCOPED.md

---

## Session context

MSTR-provisioned 18:19Z for MDPF_SCOPED maturation per Andrew sovereign 3-project directive. COO drive GO sequenced: F4 + F5 start now (parallel, not S2-gated); F1 (Inflection AUA spine-reuse) unblocked once repoint plan coherence-checked (NOT S2-gated — `client_performance` spine IS the F1 input per Andrew). F2 already closed (aa8c9de4).

---

## F4 — 49F 12/26/2025 model/non-model reclassification — VERDICT: TAGGING BUG (not a real reclass)

### Observed (49F per-firm timeseries `platinum/mdpf/49financial/aggregate_aua_timeseries.json`)

| Date | model_aua | sma_aua | non_model_aua | custody_total |
|------|-----------|---------|---------------|---------------|
| 2025-12-23 | 1,064.79M | 19.67M | 243.80M | 1,328.26M |
| 2025-12-26 | 1,107.16M | 20.46M | 207.93M | 1,335.55M |
| **Δ** | **+42.37M** | +0.78M | **−35.86M** | +7.29M (smooth) |

Total custody is smooth; only the model/non-model SPLIT jumps. The +$42.37M is **entirely opal_long_term_conservative (LTC)**: $469.29M → $512.45M (+$43.16M); every other model drifted slightly *down*. Matches Andrew's "12/27 aberration" exactly.

### Root cause — period-end-roll snapshot-selection artifact

The historical 49F model_aua (Cohort 1a) is built by `load_1a_daily()` (`data/mdpf/scripts/backfill/build_mdpf_process_backfill.py:232`), which reads SmartX daily export CSVs and **de-dupes by keeping the newest-`LastModified` CSV per (export-date, asset-class)**, summing `EndMarketVal WHERE AllocationStatus='Open'`. PeriodEnd (reporting month) is NOT used in selection.

SmartX re-exports a model's roster on the NEW period-end basis a few days into the next month. On 12/26 the LTC **December** period-end re-export (uploaded 12/29) had the newest LastModified and won the dedup — putting LTC alone on a December roster while the other 4 models stayed on their November rosters. A mixed-period-end day.

### Ground-truth evidence (raw SmartX export CSVs, open-allocation sums)

| LTC CSV on date | PeriodEnd | open rows | sum EndMarketVal |
|---|---|---|---|
| 12/23 | 11/30/2025 | 2242 | $464.94M |
| 12/26 (Nov-period file) | 11/30/2025 | 2242 | $464.94M (identical) |
| **12/26 WINNER (Dec-period file)** | **12/31/2025** | **2368** | **$508.27M** (+126 allocs, +$43.3M) |

(Artifact's $469→$512M vs raw $465→$508M = the `.029` RPS calibration multiplier ~1.0086.)

### Why non-model drops in lockstep

Non-model is a **residual** at this layer: `non_model_aua = rolled-forward certified_aua book − model_aua(1a)`. The per-date partitions even carry `1b = null:no_same_date_bd_allocations` — the trend's non-model is filled by roll-forward in consolidation. So model_aua(1a) +$43M forces non_model −$43M; net custody stays smooth (book is rolled forward independently). The reclass is a residual artifact of the 1a model jump — no real money moved between cohorts.

### Scope — SYSTEMIC, not isolated to 12/26

A day-over-day scan of the 49F series found **52 single-model >4% jumps**, clustered at month boundaries (12/31→1/1, 2/25→2/26, 3/31→4/1, 4/30→5/1, 5/30→6/2, 7/31→8/1, 8/29→9/1, 9/30→10/1, 11/28→12/1, 12/23→12/26) — the period-end-roll class. Two additional distinct artifacts in the same window:
- **12/27**: entire $1.107B book dumped into Ultra-Short-Term (`1a_coverage = daily_partial:1of5`) — a partial-coverage day (only 1 of 5 model CSVs present); the partial-1a guard should have nulled it but it published.
- **12/23**: the `.031 2024depth → .029 rps_calibrated` cutover seam (LTC −6%, USTI +84.8%).

### Proposed fix (COO scope call needed — surgical vs systemic)

Fix point = `load_1a_daily` CSV selection in `build_mdpf_process_backfill.py` (+ the `.runtmp` history sweeps that reused the logic):
1. **Period-end-coherent selection**: when multiple CSVs exist for a (date, asset-class), select the one whose PeriodEnd agrees with the consensus PeriodEnd across the 5 models on that date (or matches adjacent days), NOT blindly newest-LastModified. Keeps all 5 models on one period basis per day; the December roll then happens uniformly at a clean month boundary.
2. **Partial-coverage suppression**: confirm the `<5 of 5 models` guard nulls the partition (12/27 leaked through).
3. Re-emit affected partitions → reconsolidate `build_aggregate_aua_timeseries.py --upload`.

**Scope question for COO/Andrew:** surgical 12/26 (+12/27) correction vs systemic re-run of the historical model_aua backfill (correct but larger; touches the whole 2024-11 → 2026-01 model-split trend). Recommend systemic since the visible artifact is one of ~10 month-boundary instances; a surgical patch leaves the others visible on the same chart.

---

## F1 — Inflection AUA spine-reuse — REPOINT plan (groundwork, awaiting COO 2-min coherence check)

**Gap source (confirmed):** MDPF Inflection `partner_custody_total` = `build_mdpf_wsc_inflection_feeder.py:build_non_model_aua()` = `sum(portfolios_full.total_value)` (Eclipse-administered book, $203.98M). Assets Overview's canonical spine = `INF_D_00b.portal_timeseries.py:build_daily_firm_aua()` = `client_performance.parquet` (opal-data-inf `gold/timeseries/`, I_C02 output) grouped by date, summed `total_aua` ($205.53M). ~$1.5M gap = two valuations of the same Inflection book.

**Repoint (NOT rearchitecture):**
- Daily feeder `build_mdpf_wsc_inflection_feeder.py`: source `partner_custody_total` from `client_performance.parquet` (filter to as_of date, sum `total_aua`) instead of `portfolios_full.total_value`. `custody_scope` → `client_performance_daily_spine`. Same `opal-data-inf` bucket — one new read.
- `non_model_aua = client_performance_total − model_aua_input − sma_aua_input` (formula unchanged; new minuend). Model decomposition (Eclipse positions) unchanged — only the custody total repoints.
- **History**: drive the Inflection daily series straight off `client_performance` (full daily history already exists) rather than the S2 Orion assets_v2 API backfill (which is a parallel decomposition vs the spine). New/repointed backfill reads client_performance per-date total → emits `non_model_aua/inflection/{date}.parquet` → reconsolidate.
- COO has directed AE~A to treat the running S2 backfill (PID 2190) as STATE-REPORT-ONLY pending this; coherence-flag = S2 API pull may still legitimately feed a distinct S2 model-split-trend feature — confirm before touching that path.

**Sent to COO for the requested 2-min coherence check before touching the emit.**

---

## Compiler Tools

Investigation phase — no gold/silver script edits yet, so the before-write `comp-pipescript io` mandate has not yet fired. It WILL run before any edit to `build_mdpf_wsc_inflection_feeder.py` / `build_mdpf_process_backfill.py` (COLUMN GAPS) and `comp-pipescript deployed` before any re-run, per Rule 14/CLAUDE.md DS minimums. Ground truth this session came from direct S3 artifact + raw SmartX export reads (the decisive evidence layer for a DIAGNOSE archetype).

## Current State

- F4: diagnosis CONCLUSIVE (tagging bug, period-end-roll). RAVC2 → COO (CC CVO) with surgical-vs-systemic scope question.
- F1: repoint plan authored → COO for coherence check; unblocked, ready to implement on COO go.
- F5: next (canonical S4 display_names at by_model emit).

## Next Steps

- [COO] F4 scope decision: surgical 12/26+12/27 vs systemic historical model_aua re-run.
- [COO] F1 repoint-plan 2-min coherence check (S2 feature non-overlap).
- [DS~B] On F1 go: implement repoint (comp-pipescript io first) → re-emit → reconsolidate → verify Inflection latest ties to client_performance spine → RAVC2.
- [DS~B] F5: emit canonical S4 display_names at the by_model source.
