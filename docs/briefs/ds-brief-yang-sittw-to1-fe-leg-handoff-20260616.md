# YANG_SITTW.TO-1 — FE-leg (b) handoff brief (DS → DE 0.4.0 / RD 0.4.1)

**From:** 0.4.0_DS_ClientPlatform (~A) · **Date:** 2026-06-16 · **TO:** YANG_SITTW.TO-1 leg (b)
**Gating:** This leg wires against the **DEPLOYED** producer shape. DS leg (a) deploys FIRST
(producer commit `935d3ba79`, held local pending CTO+COO never-widen co-sign + COO DEPLOY-GO).
**Do NOT start until the producer is deployed + DS confirms** (no shape ambiguity — wire against live).
**Scope ceiling: Global aggregate view ONLY. Per-firm views UNCHANGED.**

## 1. The deployed shape change (what the producer now serves)
`build_aggregate_aua_timeseries.py` collapsed the 1c/SMA carve-out into the 1b plug:
- **`sma_aua` field REMOVED** from the aggregate + per-firm slices (`json/mdpf/global/...`,
  `json/mdpf/{firm}/...`).
- **`non_model_aua` is now `1b'` = Schwab_total − 1a** (SMA folded in; `= old non_model_aua + old sma_aua`).
- `opal_aggregate_aua`, `model_aua`, `partner_custody_total`, `by_model` UNCHANGED (verified $0 movement, 413 dates).
- REAL SMA detail still lives in `by_model` entries with `cohort_class:'sma'` (`opal_div_sma`,
  `opal_growth_sma`) — honestly null pre-launch, real post-~2026-05-20. Keep filtering them out of the model stack (unchanged).

**This change is FE-backward-compatible** — the live FE already folds `non_model_aua + sma_aua` with
`?? 0` / `lastNonNull(undefined)→0`, so the chart renders identically even before this leg lands. This
leg is (i) cosmetic type/code cleanup + (ii) the actual SI feature (x-axis extend + demarcation).

## 2. FE touch-points

### (i) Type + redundant-fold cleanup (backward-compat; do with the deploy)
- `portal/src/api/portal-proxy.ts`: `sma_aua` is declared **required** in `MdpfPartnerSeries` (L402),
  `MdpfPerFirmTimeSeries` (L432), `MdpfAggregateAUATimeSeries.aggregate` (L453). The deployed JSON no
  longer carries it → make `sma_aua?:` optional or REMOVE (TS type now lies vs runtime; `?? 0` keeps it
  safe, but reconcile the type).
- `portal/src/pages/ModelPortfolios.tsx`: the `+ sma_aua` folds are now **redundant** (`non_model_aua`
  already includes SMA). Simplify:
  - L831 `lastNonNull(perFirmMdpfData!.non_model_aua) + lastNonNull(perFirmMdpfData!.sma_aua)` → drop the `+ lastNonNull(...sma_aua)`.
  - L893 `(perFirmMdpfData.non_model_aua?.[i] ?? 0) + (perFirmMdpfData.sma_aua?.[i] ?? 0)` → drop the `+ (...sma_aua...)`.
  - The `cohort_class === 'sma'` filters (L497/578/605/640) STAY — by_model sma sleeves still exist.

### (ii) X-axis extension to 2024-11-01 — the SI feature (Global view)
- The Global trend ("growth" tab) is hard-capped to a **rolling 1-year window**:
  `ModelPortfolios.tsx` L1405-1413 (`oneYearAgo = latestTransactionDate − 1y`, filter `period >= oneYearAgoStr`)
  + L1419 (by_model). Title L1434 "…Trend Analysis" + helptip L1436 "Rolling 1-year … growth".
- **Extend the Global view back to 2024-11-01** (the full data floor; served `as_of_first` = `2024-11-01`,
  413 daily pts). Update the window logic + the "Rolling 1-year" copy to a since-inception framing.
- Keep per-firm behavior unchanged (gate the extension on `effectiveFirmId === 'global'`).

### (iii) Demarcate the estimate-basis deep tail (Option A — Andrew-direct)
- **2024-11-01 → 2026-01-15** = estimate-basis (the `.031` 2024depth Schwab-canonical rederive; model 1a
  is REAL, 1b is real-Schwab-derived but uncalibrated). Render with a **shaded band / "estimated history"
  marker** so estimate is NEVER presented as measured.
- Provenance boundaries (from the served artifact): per-date **MEASURED from 2026-01-16**
  (`cohort_provenance[]` non-null); **live-real from 2026-05-18**. So: demarcate `< 2026-01-16` as estimate.

## 3. Acceptance (leg b)
- Global view renders from the **2024-11-01 floor**; deep tail 2024-11-01→2026-01-15 visibly DEMARCATED;
  `sma_aua` gone (no runtime-undefined); per-firm views unchanged.
- `comp-transform schema-check` clean on the touched component(s) (NB: ModelPortfolios.tsx has no
  co-located `types.ts` — types are in `portal-proxy.ts`; the schema-check tool WARNs on resolution, so
  reconcile the `MdpfPerFirmTimeSeries` type manually as in §2(i)).

## 4. Verification artifacts (DS-produced, for your reference)
- Never-widen before/after: TOTAL + model + combined non-model band = $0 movement, all 413 dates, all 3
  slices. `by_model` identical. Reproduced in the DS session log.
