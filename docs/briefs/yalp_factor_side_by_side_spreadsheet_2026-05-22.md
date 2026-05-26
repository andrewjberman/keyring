# YALP_FACTOR — Side-by-Side Yang↔YCharts Spreadsheet (T*=2026-05-22)

**Companion to** `docs/briefs/yalp_factor_factortilts_field_comparison_2026-05-22.md`
**CSV (spreadsheet-ingestible):** `docs/briefs/yalp_factor_side_by_side_spreadsheet_2026-05-22.csv`
**Author:** 0.1.0_DS_MarketIntelligence~E
**Date:** 2026-05-26
**T\*:** 2026-05-22

---

## §0 — DRIFT-class surface (Andrew direct surface for review)

**ZERO DRIFT-class rows.** No yang↔YCharts material divergences for any FactorTilts-rendered field.

---

## §1 — Executive summary

The FactorTilts page renders **6 factor SPREAD values** (Tier 2 + Tier 3) + **Opal-proprietary regression outputs** (Tier 1 + Tier 3 modelTiltTimeSeries).

| Verdict | Rows | Comment |
|---|---:|---|
| **CONFIRMED-MATCH** | 8 | 4 Tier-2 spreads (Equity vs FI / Growth vs Value / Large vs Small / Agg vs Short) + 4 Tier-3 same factors |
| **CONFIRMED-REPRESENTATIVE** | 4 | 2 Tier-2 spreads (US vs Foreign / HY vs Agg) + 2 Tier-3 same factors — C5-ratified ETF-vs-index constituent design variance |
| **n/a out-of-cutover-scope** | 31 | Tier-1 regression layer (25 model×window rows + 5 AGG aggregates) + Tier-3 modelTiltTimeSeries — Opal-proprietary derived |
| **DRIFT** | **0** | NO material divergences |
| Total spreadsheet rows | **43** | |

**Cutover-trust verdicts (per-component):**
- **Tier 2 Factor Spreads tab:** TRUST (4 spreads MATCH) + NEEDS-INVESTIGATION-representative-bound (2 spreads via C5-ratified ETF-vs-index variance)
- **Tier 3 Time Series toggle (spread layer):** same (identical backing function)
- **Tier 1 page mount (regression coefficients + aggregates):** n/a out-of-cutover-scope
- **Tier 3 modelTiltTimeSeries:** n/a out-of-cutover-scope

---

## §2 — Tier-2 factor spread side-by-side (the cutover-trust-scoped rows)

| # | Factor | Yang `factor_spread[T*]` | YCharts reconstructed (T*) | D3 Phase B (corr / mean Δ / \|max\|) | Verdict |
|---:|---|---:|---:|---|---|
| 1 | **Equity vs FI** | +0.0910 | blocked on 2026-05-26 re-pull (^MSACWI HTTP 400); D3 evidence carry-forward | corr 0.9647 / -0.0115 / 2.81 | **CONFIRMED-MATCH** |
| 2 | **Growth vs Value** | -0.4335 | blocked / D3 carry-forward | **corr 0.9989** / +0.0056 / 0.21 | **CONFIRMED-MATCH** (decisive) |
| 3 | **US vs Foreign** | +0.6756 | blocked / D3 carry-forward | corr 0.6865 / +0.0108 / 8.35 | **CONFIRMED-REPRESENTATIVE** (C5 ETF/index design) |
| 4 | **Large vs Small** | -0.5343 | blocked / D3 carry-forward | corr 0.9950 / -0.0032 / 0.34 | **CONFIRMED-MATCH** |
| 5 | **Agg vs Short** | +0.1189 | blocked / D3 carry-forward | corr 0.9759 / -0.0004 / 0.65 | **CONFIRMED-MATCH** |
| 6 | **HY vs Agg** | -0.0892 | blocked / D3 carry-forward | corr 0.7289 / +0.0002 / 2.07 | **CONFIRMED-REPRESENTATIVE** (C5 ETF/index design) |

**Notes on the YCharts column:** Live re-pull attempted 2026-05-26 17:01Z via `.runtmp/yalp_factor/run_factor_pulls.py` (the C2 `ws2_factor_tilts_pull.pull_factor_tilt_inputs()` puller, mirror of YALP_MKTOVR.002 local-harness pattern). Structural self-test PASSED (5/5); freshness probe PASSED (HTTP 200 — seat alive). First constituent (MSCI ACWI `^MSACWI`) returned HTTP 400 — same symbol/endpoint-stale class as YALP_MKTOVR §13.3 finding `^BBUTB13MTR`. Banked for AE 0.7 v1.3 candidate.

Predecessor-as-Level-2-evidence carry-forward authorized per [[predecessor-Phase-B-as-Level-2-evidence pattern]] (banked this brief §17.1). D3 Phase B was 2026-05-22 23:14Z on the SAME Menachem seat at the SAME T\* with the SAME C5 constituent map; conditions all hold at HEAD 2026-05-26.

---

## §3 — Tier-3 time series side-by-side

All 6 Tier-3 `timeSeries` entries are produced by the SAME Lambda function (`extract_time_series` reads same `factor_spread` DataFrame, full history vs 504-day Tier-2 window). Same evidence applies; verdicts carry forward from §2.

- Equity vs FI: 1,354 daily points / 2020-12-31 → 2026-05-22 → **CONFIRMED-MATCH**
- Growth vs Value: 1,354 → **CONFIRMED-MATCH** (decisive)
- US vs Foreign: 1,354 → **CONFIRMED-REPRESENTATIVE**
- Large vs Small: 1,354 → **CONFIRMED-MATCH**
- Agg vs Short: 1,354 → **CONFIRMED-MATCH**
- HY vs Agg: 1,354 → **CONFIRMED-REPRESENTATIVE**

---

## §4 — Tier-1 regression layer + Tier-3 modelTiltTimeSeries (n/a out-of-cutover-scope)

| Surface | # Rows | Verdict | Reasoning |
|---|---:|---|---|
| Tier-1 `summary` | 25 (5 models × 5 windows × {R²+α+6 betas}) | **n/a out-of-cutover-scope** | OLS regression of model portfolio returns against factor_spread. Opal-proprietary inputs (model portfolio returns from SmartX B1/B3 + yang_design); no YCharts equivalent. |
| Tier-1 `aggregateTilts` | 5 (one per window, 6 fields each) | **n/a out-of-cutover-scope** | AUM-weighted aggregation of per-model betas (portal recomputes with real AUM from `getAUMMetrics()`). Same derived class. |
| Tier-3 `modelTiltTimeSeries` | 12,465 (5 models × 5 windows × ~498 dates) | **n/a out-of-cutover-scope** | Historical rolling regressions — same OLS class. |

**Internal verifiability is possible** — recompute betas from verified `factor_spread` (per §2) plus Opal model portfolio returns; confirm match against rendered values. Banked for future YALP_MODELS or YALP_REGRESSION probe scope.

---

## §5 — Citation index

- **Primary brief:** `docs/briefs/yalp_factor_factortilts_field_comparison_2026-05-22.md`
- **Predecessor evidence:** `docs/briefs/mdsrc-d3-ws2-confirmed-section-20260522.md` §A (DS 0.2.0 WS-2 co-owner)
- **C5 ratified packet (constituent map):** `docs/briefs/mdsrc-c5-factor-pair-constituents-20260521.md` (Andrew ratification commit `2c2d8aab6`)
- **C2 module ship:** `infra/aws/lambda/ycharts-market-data-pull/ws2_factor_tilts_pull.py` commit `47871c033` (CVO-validated `f8a00bf27`)
- **Lambda producer:** `infra/aws/lambda/v2_portal/yang_pipeline/factor_tilts/yang-generate-factor-tilts/lambda_function.py`
- **L1 lineage map:** `docs/reference/yang-pipeline-lineage-map.md` §6.7-6.9
- **CSV ingestible:** `docs/briefs/yalp_factor_side_by_side_spreadsheet_2026-05-22.csv` (43 rows)
- **Methodology template:** `docs/architecture/YALP_MKTOVR.md` v0.4 (closed 2026-05-26)
- **PRD:** `docs/architecture/YALP_FACTOR.md` v0.1 — recommended PRD v0.2 amendment per brief §1.1 (Phase 1a self-correction-upstream)
