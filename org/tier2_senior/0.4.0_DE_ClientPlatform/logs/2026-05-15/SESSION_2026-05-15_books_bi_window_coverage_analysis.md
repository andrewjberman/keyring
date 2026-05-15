# Session — Books-tab "Business Intelligence" window coverage analysis (49F + Inflection)

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-15
**Source:** Andrew direct — /Books tab windowed metrics (NNA/GRO/New Clients/Rank) don't
respond to the "Business Intelligence" window selector across all windows.
**Deliverable:** analysis brief, distributed to COO for decomposition.

---

## Task

Andrew: in /Books tab (both 49F + Inflection), NNA/GRO/New Clients/Rank should re-compute on
the window picked in "Business Intelligence". 49F works for QTD/YTD, defaults to QTD for
1Y/3Y/Max. Inflection not connected at all. Analyze both partners (FE + BE incl. data needs),
write a brief, route to COO.

## Investigation path

1. Located the Books tab: `BooksTab` exported from `ClientsTab.tsx`; "Business Intelligence"
   panel = `FeeEfficiencyPanel` (49F) / `InflectionInsightsPanel` (Inflection, via `revenueOpsSlot`).
2. Traced the window binding: BooksTab `feePeriod` → `periodAdvisors` (L343-369) →
   `PERIOD_TO_LB_WINDOW` map → `employeeLbData.windows[key]` → `AdvisorSummaryTable`.
3. Confirmed `employeeLbData` = `platinum/firm/leaderboard.json` via `getPlatinumFirmDashboard`.
4. Pulled both leaderboard.json files from S3 — `available_windows: [QTD,YTD,MAX]` on both.
5. Read the gold producers `data/orion/scripts/gold/{D_00c,INF_D_00c}.portal_leaderboard.py` —
   both hardcode the 3-window set in `_window_date_range` + build loop + `available_windows`.

## Findings (three distinct defects)

1. **Data:** `leaderboard.json` (both firms) emits only QTD/YTD/MAX. No 1Y/3Y.
2. **FE map bug** `ClientsTab.tsx:346`: `PERIOD_TO_LB_WINDOW` maps `max → '3Y'` (should be
   `'MAX'`). MAX data exists — Max window is broken by a pure FE typo, zero-backend fix.
   `trailing_1y→'1Y'` / `trailing_3y→'3Y'` resolve to windows the data lacks → silent QTD fallback.
3. **FE Inflection gap:** Inflection renders `InflectionInsightsPanel` (own internal window
   state) instead of `FeeEfficiencyPanel`, so BooksTab `feePeriod` is frozen at default →
   the selector never drives the metric table.

## Deliverable

`docs/briefs/books-bi-window-coverage-20260515.md` — committed CLOUD `4bb9e2012`. Covers FE
(FE-1..5) + BE (BE-1..6) implementation, sequencing, effort, 3 open product questions, and a
coordination flag: BE work touches `INF_D_00c` — same file as the open INFGRO
`firm_return_pct_twr` defect (log `b1fd04b30`) — recommend folding both into one chain cycle.

Distributed to COO via MCP 18:53Z for decomposition.

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-routes trace getFirmLeaderboard` | Confirmed CF behavior `/api/scoped/advisor-intelligence/*.json`, S3 key `platinum/firm/leaderboard.json`, firm-routed origin. |
| `comp-cache collisions` | `firm-leaderboard` key shared across index/AdvisorsTab/ClientsTab — all `PlatinumLeaderboardResponse`, intentional dedup, no collision. |

Implementation TOs (per brief) must run `comp-transform schema-check` on BooksTab/
FeeEfficiencyPanel/InflectionInsightsPanel + `comp-pipescript io` on D_00c/INF_D_00c.

## Current State

| Item | Status |
|------|--------|
| BI-window brief | Shipped — `4bb9e2012`; distributed to COO |
| INFGRO.005 | Held on upstream return-% defect (separate) |
| INFGRO.006 | Dispatch-held |
| Watcher | LIVE |

## Next Steps

- [COO] Decompose the brief into FE + BE + DS TOs. FE-1 (`max:'MAX'`) + FE-2 (Inflection
  lift) are backend-independent — recommend a fast GO ahead of the BE 1Y/3Y work.
- [DE] On GO: execute the DE-lane FE TOs (FE-1, FE-2, FE-4).
- [DS/CTO] BE-1..4 (1Y/3Y window emit) — fold into the INF_D_00c return-% fix chain run.
