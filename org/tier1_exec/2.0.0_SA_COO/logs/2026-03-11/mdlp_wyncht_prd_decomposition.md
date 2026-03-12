# MDLP_WYNCHT PRD Decomposition — 2.0.0_SA_COO

**Date:** 2026-03-11

## Objective

Decompose the CTO's MDLP_WYNCHT PRD into a task order. The PRD defines a standalone offline
HTML clone of the Model Portfolios benchmark tab for screenshot capture.

---

## Work Completed

### 1. PRD Review

Read `docs/architecture/MDLP_WYNCHT_PRD.md`. Verified reference files exist:
- Lambda source, portal components (ReturnVolatilityScatter.tsx, BenchmarkHeatmap.tsx),
  reference CSV (model_portfolio_return_vol_20260227.csv), pkl file.

### 2. Decomposition Decision

**Single task order to DE. No DS task order. No thread.**

The PRD over-specifies this as a dynamic tool. Andrew's direction: duplicate the existing
page, hardcode the numbers from the reference CSV, keep it excessively simple.

- No Python extraction script needed — numbers already in CSV, hardcode them
- No JSON loading, no file picker — static data baked into HTML
- Chart.js for scatter chart (toggles need to work), CSS grid for heatmap
- Index/ETF and Gross/Net toggles work by switching between hardcoded data sets
- Period toggle on scatter works by switching hardcoded period data
- One HTML file, one agent, done

### 3. Task Order Issued

### Task Order Dispatch

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.4.0_DE_ClientPlatform | org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/MDLP_WYNCHT.001.facsimile-html.md | Clone the portal benchmark tab as standalone HTML. Hardcode all data from reference CSV. Chart.js scatter + CSS grid heatmap. Working toggles. Dark theme. |

Execution dependencies: none (single agent, no blockers)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| No DS task order | Data is already in CSV. Hardcode it. No extraction script needed. |
| No thread | One agent, one file, no interface boundary. |
| DE not RD | DE knows the portal components. This is engineering (Chart.js + CSS grid), not design. tools/ is outside RD scope. |
| Chart.js kept | Toggles need to work — period selector, Index/ETF, Gross/Net. Chart.js handles the scatter chart interactivity. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/MDLP_WYNCHT.001.facsimile-html.md` | DE task order | No |
| `org/projects/MDLP_WYNCHT.json` | Phase updated | No |
| `org/projects/REGISTRY.md` | Phase updated | No |
| This file | Session log | No |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE (COO decomposition done)
**Active branch:** CLOUD

Single task order issued to DE. Clone the page, hardcode the numbers, working toggles,
dark theme, done.

---

## Next Steps

1. **[0.4.0_DE_ClientPlatform] Build facsimile.html** -- read the portal components,
   duplicate the visual output, hardcode values from reference CSV, Chart.js scatter,
   CSS grid heatmap, working toggles.

2. **[Andrew] Validate screenshots** -- open in browser, compare to portal, capture.

**Do NOT:**
- Build a Python extraction script (not needed)
- Build a dynamic JSON-loading tool (hardcode the data)
- Modify any file in portal/
