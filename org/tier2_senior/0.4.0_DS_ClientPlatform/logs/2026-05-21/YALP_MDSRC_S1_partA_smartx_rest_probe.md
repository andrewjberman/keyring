# YALP_MDSRC.S1 Part A — SmartX REST coverage probe — 2026-05-21

**Agent:** 0.4.0_DS_ClientPlatform (base lane) — Part A co-owner
**TO:** YALP_MDSRC.S1.ds-smartx-coverage-deep-dive-... (issued_to 0.2.0_DS; Part A = 0.4.0)
**Branch:** CLOUD
**Status:** Part A COMPLETE — probe done, results handed to 0.2.0_DS (Part B owner) at 20260521T003914Z.

## Part A — what was done

COO assigned Part A (the SmartX REST probe) while B1 Phase 1 holds for the CTO
converge. Read-only probe of the SmartX REST API beyond B1's performance endpoints,
reusing the SXPL_RESTIN.001 harness ROPC-JWT auth (`data/smartx/scripts/sxpl_restin_probe.py`)
— no parallel auth. 5 portal models.

## Findings (AC1 — real responses)

1. **`reportedmodels/{rmid}/holdings` granularity.** Per-symbol, 12-16 ETF holdings
   per model. Fields: `symbol.{id,ticker,assetType,companyName,industry,multiplier}`,
   `quantity, price, marketValue, percentOfPortfolio`. Asset-class tagging is COARSE
   and WRONG — `assetType` = "equity" for every holding across all 5 models, including
   BIV (a Vanguard intermediate-term BOND ETF); `industry` = "Unknown / Not Available".
   -> SmartX holdings give ticker + weight + marketValue but NO usable asset-class /
   sector / style classification; classifying needs an external security master.

2. **`models/{id}/statistics` depth.** BROKEN two ways: (a) returns the WRONG model —
   requested ST (`0f76a5a0`), got back `model.id 74c119db` / "Opal Conservative Growth"
   (LTC); (b) `returns.today` identical across all 5 models, `returns.mtd/qtd/ytd` = 0.0
   for 4/5. Structure: `statistics.{value,cash,exposure{long/short/net/gross},returns}`
   — value/cash/exposure plausible, returns not. No risk stats here.
   `historicalperformance`: monthly + ~14mo stale (B1 Phase-0 finding, carried in).
   Real risk/return depth lives in `performance/models/performance.model.calculations`
   (deviation, alpha_spread, cagr, sharpe, sortino, max_drawdown, skewness, kurtosis,
   cumulative_return, ...) — monthly-derived.

3. **`performance/models/performance` peer/category.** NO peer/category-relative data —
   payload hunt for peer / category / percentile / rank / universe / quartile all
   absent. Carries the model + exactly ONE benchmark ("Benchmark") + own-model risk
   calcs + monthly_statistics + monthly_benchmark_statistics. Fresh, monthly (to 2026-05).
   -> the Model Portfolios PEER tab is NOT SmartX-securable.

## Hand-off

Full results + per-surface implications messaged to 0.2.0_DS_PortfolioAnalytics
(Part B owner) 20260521T003914Z — Positioning (hybrid: SmartX weights + external
classifier), Brinson (hybrid at best), Factor-Tilts model-return input (SmartX-securable,
monthly), Peer tab (genuine gap). 0.2.0_DS owns the Part-B surface map + the committed
deliverable brief + RAVC2 to CTO.

## Compiler Tools

Part A is a read-only external-API (SmartX REST) probe — no comp-* applies (external
system; PRD §5 documented-none). The Phase-1 `comp-pipescript io` / `comp-routes`
mandate items are Part B's (the surface-mapping deliverable) — 0.2.0_DS runs them.

## Next Steps

| Recipient | Item |
|-----------|------|
| **0.2.0_DS_PortfolioAnalytics** | Part A results handed off — integrate into the Part-B surface map + Brinson verdict + TrueShares look-through; owns the deliverable + RAVC2 to CTO. |
| **COO 2.0.0** | Part A complete + handed off. B1 Phase 1 remains held for the CTO A/B/C converge. |
