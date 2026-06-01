# MDPF_SCOPED P1 — Model Portfolios FE↔BE Linkage Matrix (MERGED)

- **Deliverable for:** COO [DRIVE] dispatches 20260601T130151Z + T131156Z — Andrew-direct FIRST priority: prove FE + BE are categorically linked for the Model Portfolios page across all three firm segments (GLOBAL / 49 / INFLECTION).
- **Authors:** FE rows — 0.4.2_RD_AdvisorIntelligence~B; BE columns — 0.4.0_DE_ClientPlatform (`31f3b09ed`).
- **Date:** 2026-06-01
- **Sources joined:** `mdpf-fe-be-linkage-matrix-fe-rows-20260601.md` (RD) + `mdpf-fe-be-linkage-matrix-be-columns-20260601.md` (DE).
- **Join key:** React Query `queryKey`.
- **Page:** `portal/src/pages/ModelPortfolios.tsx` (portal/DEV, Rule 19 verified).

---

## Merged matrix (FE row ⋈ BE column on queryKey)

| # | Panel | queryKey (join) | FE re-scope on firm selector | BE serving artifact (GLOBAL / 49 / INF) | BE per-segment fit | Verdict |
|---|-------|-----------------|------------------------------|------------------------------------------|--------------------|---------|
| 1 | Daily AUA Trend (bar/area, value+count) | `aum-timeseries` / `mdpf-per-firm-timeseries` | **RE-SCOPES** (value) ✓; count + extra-models = flags F4/F5 | `json/portfolios/aum-timeseries.json` / `json/mdpf/49financial/aggregate-aua-timeseries.json` / `json/mdpf/inflection/aggregate-aua-timeseries.json` | FIT ✓ (402 dates, schema-identical) | **LINKED** (value); F4/F5 open |
| 2 | AUA-by-Model donut | `aum-metrics` / `mdpf-per-firm-timeseries`.by_model | **RE-SCOPES** ✓ | `json/portfolios/aum-metrics.json` / per-firm aggregate `.by_model` (×2) | FIT ✓ (by_model key-sets differ data-driven; render Object.values) | **LINKED** ✓ |
| 3 | AUA Growth Metrics (quarterly cards) | `aum-metrics` / per-firm derived | **RE-SCOPES** ✓ | `json/portfolios/aum-metrics.json` / per-firm aggregate (derived) | FIT ✓ | **LINKED** ✓ |
| 4 | Account Distribution bell curve | `account-distribution` / `mdpf-per-firm-distribution` | **RE-SCOPES** ✓ | `json/portfolios/account-distribution.json` / `json/mdpf/49financial/account-distribution.json` / `json/mdpf/inflection/account-distribution.json` | FIT ✓ (per-firm = superset shape) | **LINKED** ✓ |
| 5 | Non-Model band (in trend stack) | `non-model-assets` / per-firm `.non_model_aua` | **RE-SCOPES** ✓ (value mode) | `json/portfolios/non_model_assets.json` / per-firm aggregate `.non_model_aua` | FIT ✓ (393 dates per-firm) | **LINKED** ✓ |
| 6 | Benchmark heatmap + Return/Vol scatter | `model-portfolio-benchmarks` | GLOBAL-ONLY (by design — firm-invariant) | `json/benchmarks/model_portfolio_benchmarks.json` (all segments same) | firm-invariant | **LINKED + LABELED** (F1→b) ✓ |
| 7 | ETF benchmark returns | `etf-benchmark-returns` | GLOBAL-ONLY (by design — firm-invariant) | `json/benchmarks/etf_returns.json` (all segments same) | firm-invariant | **LINKED + LABELED** (F1→b) ✓ |
| 8 | Peers — Morningstar quartile | `peer-performance` | GLOBAL-ONLY (by design — firm-invariant) | `json/peers/peer_performance.json` (all segments same) | firm-invariant | **LINKED + LABELED** (F1→b) ✓ |

**FE-only structural elements (no BE join):** firm selector dropdown (`:583`, internal-only); custom donut legend (`:773`, re-scopes ✓); Data Source note (`:1611`, F2 fixed below).

---

## Categorical linkage conclusion

**All 8 panels are linked across GLOBAL / 49 / INFLECTION.**
- Panels #1–5 (Growth tab): FE re-scopes on the firm selector AND BE has a verified-present per-firm artifact for each of the 3 segments. The D1 "empty firm view" reopen defect does **not** recur.
- Panels #6–8 (Performance + Peers): firm-invariant by design (model-level returns don't vary by firm). Now **labeled** under firm scope (COO ruling b) so identical-across-firms data no longer reads as a stale firm-view bug.

---

## Changes landed this session (portal/DEV)

1. **F1 → COO ruling (b): firm-invariant label.** Added a `firmInvariantNotice` (`ModelPortfolios.tsx`, after `activeDistribution`) rendered at the top of the Performance and Peers tabs when `selectedFirmId !== 'global'`: *"Model-level data — identical across firms. Benchmark and peer returns are a property of each model portfolio, not of {firmName}, so this view is not firm-scoped."* Global view shows nothing.
2. **F2 fix (bundled): hardcoded "49Financial:" label.** The Data Source note (`:1624`) hardcoded "49Financial:" regardless of selected firm — wrong under Inflection. Now resolves to the selected firm's display name (or "Non-Model" under Global). One-line, same firm-scope-correctness theme as F1.

**Verification:** `bun run typecheck` (`tsc -b --noEmit`) PASS clean. **Visual smoke: env-blocked** — headless Chrome in this agent env times out at 180s on localhost nav (same blocker that stalled INFDEMO.001's CTO visual-confirm; GCM QUOTA_EXCEEDED). Requesting Andrew or a browser-capable lane (`/frontend-dev`) for the visual gate per portal-closure discipline.

---

## Open items (for COO / DE adjudication)

- **F4 — Count-mode trend = all-zeros in firm views.** Per-firm aggregate artifact carries no per-model `account_count`; the Count toggle reads `account_count` → zeros for 49/INF. **Adjudication:** (a) per-firm artifact emits per-model account_count over time (BE — DE/DS), or (b) FE hides/disables the Count toggle under firm scope. *Not yet implemented — awaiting call.*
- **F5 — Per-firm extra models dropped from trend chart + legend.** Donut renders `Object.values(by_model)` (all per-firm models incl 49 SMA sleeves / INF blends); the trend stacked chart + legend iterate the fixed global `MODEL_ORDER` (5), so the extra per-firm models are absent from the trend in firm view. **RD fix available:** drive trend model iteration from the per-firm key-set when `isPerFirm`. *Not yet implemented — flagged to avoid silent scope creep; RD can land on next DEV cycle on COO GO.*
- **DE note (AE):** two possibly-orphan S3 artifacts (`json/mdpf/aggregate-aua-timeseries.json`, `json/mdpf/global/aggregate-aua-timeseries.json`) are not referenced by current page imports — AE to confirm publish schedule / live consumers.
