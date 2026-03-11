# MDLP_WYNCHT Project Registration and PRD — 1.0.0_SA_CTO

**Date:** 2026-03-11

## Objective

Register the MDLP_WYNCHT project and write a technical PRD for a standalone offline HTML facsimile of the Model Portfolios benchmark tab. The facsimile renders Return vs Volatility scatter and Benchmark Heatmap from local pkl-derived data for controlled screenshot capture without modifying the portal or connecting to cloud.

---

## Work Completed

### 1. Data Investigation

Investigated the `yang-generate-benchmark-returns` Lambda to confirm the complete data lineage:

| Finding | Detail |
|---------|--------|
| Sole data source | `data_pkl['return_daily']` — 13 series filtered by `index_name.contains("Term")` |
| Model pkl usage | None. Lambda only opens data pkl. Model pkl referenced only for S3 key derivation. |
| Date basis | Calendar dates (includes weekends), not trading-day-only |
| Return method | Geometric compounding: `product(1 + r_i) - 1` |
| Volatility method | `std(ddof=1) * sqrt(252)`, min 5 points, 1D uses trailing 20 |
| Shared benchmark | LTC and LTA share `"Long Term Benchmark"` and `"Long Term ETF"` |

Extracted and validated a reference CSV from `data_20260226_v1.pkl` (data as of 2026-02-27) at `model_portfolio_return_vol_20260227.csv`. All 5 models x 9 periods x 3 series (model, index, ETF) confirmed correct.

### 2. Architecture Research

Read the full portal implementation:

| Component | File | Key Specs |
|-----------|------|-----------|
| ReturnVolatilityScatter | `portal/src/components/ReturnVolatilityScatter.tsx` | Recharts ScatterChart, 9-period toggle, circle/diamond shapes, split LTC/LTA diamond, clickable legend with granular tooltips |
| BenchmarkHeatmap | `portal/src/components/BenchmarkHeatmap.tsx` | CSS Grid, 3 rows per model (model/benchmark/spread), Index/ETF toggle, Gross/Net toggle (36 bps prorated), green/red spread overlays |
| ModelPortfolios page | `portal/src/pages/ModelPortfolios.tsx` (lines 1440-1548) | Benchmark tab composition, data transform selecting index vs etf fields |
| Model colors | `portal/src/lib/modelPortfolioColors.ts` | 5 canonical colors: Orange, Amber, Green, Blue, Red |
| Data types | `portal/src/api/portal-proxy.ts` (lines 587-615) | `BenchmarkPeriodReturn`, `BenchmarkModelData`, `BenchmarkReturnsResponse` |

### 3. Volatility Window Inconsistency Identified

During investigation, identified that the Lambda uses a 20-day trailing window for 1D volatility but uses the raw period data for all other periods. WTD (5 days) gets fewer observations than 1D (20 days). Documented a fix recommendation: apply a trailing 20-calendar-day floor to all vol calculations. This is a separate concern from the facsimile project — written up as a standalone devops handoff brief.

### 4. Project Registration

- Created `org/projects/MDLP_WYNCHT.json`
- Added row to `org/projects/REGISTRY.md` Active Projects table
- Macro code: `MDLP` (ModelPortfolios, Pod 0.4 ClientPlatform)

### 5. PRD Written

`docs/architecture/MDLP_WYNCHT_PRD.md` covering:
- Data pipeline (pkl -> Python script -> JSON -> HTML)
- Comprehensive JSON data format (matching Lambda output)
- Scatter chart specs (shapes, colors, axes, period toggle, legends)
- Heatmap specs (grid layout, 3 rows per model, color coding, Index/ETF and Gross/Net toggles)
- Net return proration formula (36 bps, trading-day-counted)
- Dark theme color values
- File structure (`tools/wyncht/`)
- 10 acceptance criteria
- COO decomposition guidance (2 parallel deliverables: Python script + HTML facsimile)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Chart.js + plain HTML grid for facsimile | Portal uses Recharts (React). Building a React app for screenshots is overkill. Chart.js handles scatter via CDN; heatmap is just a styled CSS grid table. Minimizes dependencies. |
| Comprehensive JSON format (not CSV) | JSON preserves the nested model -> period -> {model, index, etf} structure that both components need. CSV was useful for validation but is flat. |
| `tools/wyncht/` at repo root | Keeps facsimile tooling separate from portal and infra. Consistent with existing `.tools/` convention. |
| Two independent deliverables | Python script (data) and HTML file (visualization) share only the JSON contract. Can be built in parallel by different agents. |
| Out-of-scope: granular pinned tooltips | Complex SVG positioning logic (`GranularTooltips` component) using Recharts internal hooks. Hover tooltips are sufficient for screenshot purposes. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/projects/MDLP_WYNCHT.json` | New project JSON | No |
| `org/projects/REGISTRY.md` | Added MDLP_WYNCHT row to Active Projects | No |
| `docs/architecture/MDLP_WYNCHT_PRD.md` | New PRD | No |
| `model_portfolio_return_vol_20260227.csv` | Reference validation data (from earlier in session) | No |

---

## Blockers

None. PRD is complete and ready for COO decomposition.

---

## Current State

**Status:** COMPLETE (CTO scope)
**Active branch:** CLOUD

Project MDLP_WYNCHT registered. PRD written with full component specs extracted from portal source code. Reference CSV validated against Lambda logic. Ready for 2.0.0_SA_COO to decompose into task orders for Pod 0.4 agents.

---

## Next Steps

1. **[2.0.0_SA_COO] Decompose PRD into task orders** -- two parallel deliverables: Python extraction script (DS or AE) and HTML facsimile (DE or RD)
2. **[Assigned agent] Build `extract_benchmark_data.py`** -- pkl to JSON, matching Lambda logic exactly
3. **[Assigned agent] Build `facsimile.html`** -- standalone dark-themed HTML with scatter chart + heatmap
4. **[Andrew] Validate screenshots** -- open facsimile with 2-27 data, compare to portal, capture screenshots

**Files to touch next:**
- `tools/wyncht/extract_benchmark_data.py` -- new file
- `tools/wyncht/facsimile.html` -- new file

**Do NOT:**
- Modify any file in `portal/`
- Connect the facsimile to any cloud service or API
- Require npm/bun/build steps for the HTML
