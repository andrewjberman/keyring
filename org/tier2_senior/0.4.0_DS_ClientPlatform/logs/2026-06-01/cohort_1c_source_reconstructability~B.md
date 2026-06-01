# Cohort 1c (SMA) — source-data reconstructability finding (DS~B, 2026-06-01)
Investigation only (no backfill). Support leg to DE (0.4.0_DE_ClientPlatform, leads pipeline path). CTO Directive 1b / Andrew-direct fast-follow. CVO sole verify-writer.

## What 1c is + the symptom
Cohort taxonomy (mdpf decomposition brief 20260519): 1a=model, **1c=49F SMAs**, 1b=49F non-model residual, 2a/2b=inflection. Symptom: 49F cohort-1c jumps 0→>$20M last week of May, no prior history.

## The "jump" is at 5/18 and is a RECLASSIFICATION, not a real new asset
- Platinum 49F `sma_aua` (1c): null/absent on all pre-5/18 dates; first appears 2026-05-18 = $24.90M; stable ~$25M (24.9→25.5→25.1M) through 5/29. The aggregate_aua series itself goes back to 2024-11-01, but `sma_aua` is populated only from 5/18.
- 5/18 is when the canonical daily aggregator + the `model_aua_positions` feeder started (feeder partitions begin 2026-05-18; 49F 5/18 feeder = 6758 `model` rows + **94 `sma` rows summing $24.90M**, source_pipeline=smartx).
- Before 5/18, platinum was produced by `build_mdpf_process_backfill.py` (49F-only), which EXPLICITLY sets `sma_aua=None` and documents (L24-35): **"Cohort 1b (49F non-model, SMA-INCLUSIVE)… SMA stays INSIDE 1b… no '− sma' subtraction"** and "Cohort 1c… sma_aua is null historically; the SMA dollars [are] inside the 1b residual."
- => The SMA dollars EXISTED historically — lumped into the 1b non-model residual (1b = certified_aua − 1a, SMA-inclusive). The 5/18 "0→$20M" is the canonical aggregator breaking SMA OUT of 1b into its own 1c bucket. Total AUA unaffected; it's a 1b↔1c split surfacing change. NOT a real asset appearing late-May.

## Source availability — (a) vs (b)
- **NOT pure (a) "never captured":** SMA value is implicitly present historically (inside 1b/custody).
- **NOT clean (b) "exists upstream, just reclassify":** the historical SmartX source does NOT carry the SMA accounts separately. The consolidated source `s3://opal-data-smartx-v2/consolidated/smartx_allocations.parquet` covers Period 202409→202606 (monthly, back to Sept 2024) but is **MODEL-ONLY**: distinct ModelName = the 5 Opal models; AssetClass = {INT,LTA,LTC,ST,UST}; **zero non-Opal/SMA allocations**. The 94 SMA accounts the live feeder surfaces are NOT in this historical source.
- The SMA breakdown only became available 5/18 via the live WS-B feeder pulling the SmartX **REST API** (current positions only; the API does not return historical snapshots).

## Reconstructability verdict (source-data leg)
EXACT per-date historical 1c is **NOT reconstructable from existing data** — the historical SmartX source is model-only; SMA accounts aren't separately present pre-feeder. Options:
1. **ESTIMATE (feasible now, no new data):** SMA is structurally slow-moving (24.9–25.5M over 5/18–5/29). Hold-flat-backward (~$25M) or custody-proportional reclassification — moves dollars from the (already-correct) historical 1b into 1c. Does NOT change total AUA; it's a presentation split, explicitly an estimate.
2. **EXACT (needs new source):** a historical SMA allocation feed from SmartX (does SmartX retain historical SMA snapshots via another endpoint / a one-time backfill pull?) — a SmartX data-availability question to scope with AE/DE. Not in current data.

## Hand-off
- DE (leads pipeline): the 1c-surfacing starts at the 5/18 canonical-aggregator/feeder boundary; pre-5/18 platinum is the 49F-only backfiller (sma_aua=None, SMA-in-1b). Combined "what's needed to reconstruct" scope = my source verdict above + your pipeline-path trace.
- COO+CTO: (a)-vs-(b) = "value captured (in 1b) but not separably reconstructable from existing source; estimate-only without a new SmartX historical SMA pull." NO backfill until Andrew sees scope.

## CONSOLIDATED SCOPE (DS~B absorbed lead 2026-06-01 ~1545Z; DE unresponsive ~2.9h, COO routed)

### Pipeline-consumer check — does ANY consumer read Cohort-1c STANDALONE?
**NO standalone 1c-timeseries consumer.** `sma_aua` is TYPED in portal/src/api/portal-proxy.ts (the AUA-timeseries shape) and PRESENT in the served json/mdpf/{firm}/aggregate-aua-timeseries.json, but **no FE component renders the sma_aua timeseries as its own line**. The only consumers:
- ModelPortfolios.tsx AUA trend reads `model_aua` + `non_model_aua` (NOT `sma_aua`); per-firm Non-Model = the artifact `non_model_aua` (L404). RD~B (Directive-1a) is rolling 1b+1c together for this view.
- ModelPortfolios by_model "SMA sleeves" = the DONUT snapshot distribution + snapshot Total cards (current-date, NOT a historical timeseries) — no historical-jump dimension.
=> Nothing surfaces the 1c historical jump as a standalone series.

### Likely current FE presentation of the reclassification (for completeness)
Post-5/18 `non_model_aua` EXCLUDES the broken-out SMA (it moved to `sma_aua`). Since ModelPortfolios renders `non_model_aua` directly and NOT `sma_aua`, the current (pre-RD-fix) per-firm Non-Model line likely DIPS ~$25M at 5/18 (and/or total dips), OR a cohort breakdown shows 1c jumping 0→$25M — depending on the view Andrew looked at. RD's Directive-1a 1b+1c rollup (add SMA back into the displayed non-model) makes it continuous either way.

### THREE OPTIONS + RECOMMENDATION
- **(i) FE rollup resolves it, NO backfill — RECOMMENDED.** RD's Directive-1a rolls 1b+1c together; the combined non-model is continuous across 5/18 (SMA is in the combined total either way). No standalone 1c consumer exists, so nothing else needs the historical split. Backfill is MOOT for the current views.
- (ii) ESTIMATE reclass — only if 1c must be shown SEPARATELY over time later. Hold-flat/custody-proportional (~$25M, SMA slow-moving); presentation-only split within the already-correct total; NOT new data.
- (iii) EXACT historical per-date 1c — needs a NEW SmartX historical-SMA pull (existing source is model-only). Data-availability Q for AE/DE+SmartX. Only path to true per-date.

**DS~B recommendation: (i) — no backfill.** The reclassification leaves total AUA correct; the RD rollup resolves continuity; no consumer reads 1c standalone. Revisit (ii)/(iii) only if a future requirement surfaces a standalone historical-1c view. One verify for RD: confirm the Directive-1a rollup adds SMA into the displayed non-model (so the post-5/18 ~$25M dip doesn't persist).
