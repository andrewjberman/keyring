# MDPF_SCOPED P1 — FE↔BE Linkage Matrix: BE Columns (DE)

**Author:** 0.4.0_DE_ClientPlatform | **Date:** 2026-06-01 | **Project:** MDPF_SCOPED Phase 1 maturation
**Scope:** Backend-fit mapping for the **Model Portfolios** page (`portal/src/pages/ModelPortfolios.tsx`, portal/DEV) across all three firm segments: **GLOBAL** / **49** (49 Financial, `49financial`) / **INFLECTION** (`inflection`).
**Pod-4 split:** RD~B owns FE panel ROWS; DE owns BE COLUMNS (this doc); AE owns schedule/interval column; DS~B standby for data-shape gaps.
**Join key:** React Query `queryKey` (column 2) — RD joins FE rows to these BE cols by that key.

CF rewrite: `/api/general/*` → `/json/*` via `public-data-router`. All keys below are under `s3://opal-data-portal-v2/`. **All serving artifacts VERIFIED-PRESENT in S3 (listed 2026-06-01; published 2026-05-29 by DS~B).**

## BE Columns

| # | FE panel | queryKey (join key) | GLOBAL serving artifact | 49 serving artifact | INFLECTION serving artifact | Per-segment FIT |
|---|----------|---------------------|-------------------------|---------------------|-----------------------------|-----------------|
| 1 | Daily AUA Analysis (trend chart) | global `aum-timeseries` / per-firm `mdpf-per-firm-timeseries` | `json/portfolios/aum-timeseries.json` (272KB) | `json/mdpf/49financial/aggregate-aua-timeseries.json` (92KB) | `json/mdpf/inflection/aggregate-aua-timeseries.json` (70KB) | **FIT ✓** — per-firm enabled when `selectedFirmId !== 'global'`; both per-firm files 402 dates, identical top-level schema |
| 2 | AUA-by-Model donut (radial) | global derived from `aum-metrics` / per-firm `mdpf-per-firm-timeseries`.`by_model` | `json/portfolios/aum-metrics.json` (4KB) | (same as #1, `.by_model`) | (same as #1, `.by_model`) | **FIT ✓** — by_model is data-driven 7-each; sets DIFFER (49: 5 base + `opal_div_sma`/`opal_growth_sma`; INF: 5 base + `opal_blend_5050_int_ltc`/`opal_blend_5050_st_int`). Identical entry fields {cohort_class, display_name, model_value}. NO canonical-name collision. FE renders `Object.values(by_model)` — divergence is correct, not a break |
| 3 | AUMGrowthMetrics (quarterly cards) | `aum-metrics` / per-firm derived (`by_model` + `partner_custody_total`) | `json/portfolios/aum-metrics.json` | (per-firm aggregate, derived) | (per-firm aggregate, derived) | **FIT ✓** — re-derives from per-firm via useMemo dep `[metricsData, selectedFirmId, perFirmMdpfData]` |
| 4 | AccountDistribution (bell curve) | global `account-distribution` / per-firm `mdpf-per-firm-distribution` | `json/portfolios/account-distribution.json` (5.4KB) | `json/mdpf/49financial/account-distribution.json` (5KB) | `json/mdpf/inflection/account-distribution.json` (6.4KB) | **FIT ✓** — per-firm enabled when firm selected. Per-firm is a SUPERSET shape: core {by_model, period, total} matches global; per-firm adds {firm_id, firm_name, source} (additive, runtime-present) |
| 5 | Non-Model band (within trend stack) | global `non-model-assets` / per-firm `.non_model_aua` | `json/portfolios/non_model_assets.json` (98KB) | (per-firm aggregate `.non_model_aua`) | (per-firm aggregate `.non_model_aua`) | **FIT ✓** — F1 maturation confirmed per-firm non-model SUBSUMED in the aggregate series (Inflection non_model_aua, 393 dates) |
| 6 | Performance tab — BenchmarkHeatmap + ReturnVolatilityScatter | `model-portfolio-benchmarks` | `json/benchmarks/model_portfolio_benchmarks.json` | — same artifact — | — same artifact — | **FLAG (classify):** NOT firm-gated (`enabled: activeTab === 'performance'` only). Shows GLOBAL/model-level for all 3 segments |
| 7 | Performance tab — ETF benchmark returns | `etf-benchmark-returns` | `json/benchmarks/etf_returns.json` | — same artifact — | — same artifact — | **FLAG (classify):** same as #6 |
| 8 | Peers tab — Morningstar quartile chart | `peer-performance` | `json/peers/peer_performance.json` | — same artifact — | — same artifact — | **FLAG (classify):** NOT firm-gated (`enabled: activeTab === 'peers'`). Shows GLOBAL/model-level for all 3 segments |

## Fit-break analysis

**No empty-firm-view / missing-data breaks.** Every Growth-tab panel (#1–5) has a real, verified backend source for all three segments. The D1-class "firm view shows no data" defect from the 2026-05-29 reopen does NOT recur on current artifacts — the per-firm files exist and carry the right shape.

**No cross-segment schema-drift break.** 49 and inflection aggregate-aua files are schema-identical; account-distribution per-firm files are schema-identical to each other and a superset of global. The by_model **key-set** divergence (#2) is intentional data-driven content, not a shape mismatch.

**One classification needed (FLAG, panels #6–8 — Performance + Peers tabs):**
These tabs are gated ONLY by `activeTab`, never by `selectedFirmId`. They render model-level data (a model's benchmark return series / Morningstar peer-universe quartile) that is **firm-invariant by design** — a model's performance doesn't change with which firm custodies it. So showing identical data across all 3 segments is arguably *correct*. BUT the page does not signal this, so a user on "49 Financial" may read Performance/Peers as firm-scoped when it is not.
**Decision needed (RD + COO):** (a) accept as-is (model-level, firm-invariant = correct), (b) add a "model-level / firm-invariant" label on these tabs when a firm is selected, or (c) hide Performance/Peers under firm scope. This is a UX/scope call, not a data gap — DE has no fix pending until adjudicated.

## Notes for AE (schedule/interval column) + DS~B
- **Possible orphans (flag to AE):** `json/mdpf/aggregate-aua-timeseries.json` (300KB) and `json/mdpf/global/aggregate-aua-timeseries.json` (36KB) exist in S3 but are NOT referenced by current `ModelPortfolios.tsx` imports (global trend reads `json/portfolios/aum-timeseries.json`, not these). Possible legacy/other-consumer artifacts — AE to confirm publish schedule + whether still fed.
- All per-firm artifacts last published 2026-05-29 by DS~B. AE owns the refresh-interval column (how often each artifact regenerates).
- No silver/gold data-shape gap surfaced for DS~B — all artifacts well-formed and schema-consistent.
