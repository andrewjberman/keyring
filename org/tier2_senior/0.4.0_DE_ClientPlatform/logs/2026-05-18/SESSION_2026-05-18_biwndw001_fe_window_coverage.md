# Session — ADVI_BIWNDW.001 FE-1/FE-2/FE-4: Books BI window coverage

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-18
**TO:** ADVI_BIWNDW.001 (from 2.0.0_SA_COO) — GO 2026-05-15, backend-independent
**Portal DEV commit:** `fe881e2b`
**Workspace CLOUD commit:** (this log) pending

---

## Task

ADVI_BIWNDW.001 — the /Books tab "Business Intelligence" window selector must drive
the advisor-summary metric table. Three FE changes from the brief I authored
(`docs/briefs/books-bi-window-coverage-20260515.md`, `4bb9e2012`): FE-1 (Max-window
typo), FE-2 (Inflection window lift), FE-4 (defensive unavailable state). FE-3 is a
no-op; FE-5 is deferred (product Q1).

## Work Completed

### FE-1 — PERIOD_TO_LB_WINDOW `max` typo
`ClientsTab.tsx` mapped `max -> '3Y'` — a window the data does not carry — so the Max
toggle silently fell back to QTD. Changed to `max -> 'MAX'` (MAX exists in both firms'
`leaderboard.json`). Hoisted `PERIOD_TO_LB_WINDOW` to module scope so the new
availability memo shares it.

### FE-2 — Inflection BI window lift
Inflection renders `InflectionInsightsPanel` as the `revenueOpsSlot` instead of
`FeeEfficiencyPanel`, so its window selection never reached `BooksTab.feePeriod` and the
advisor-summary table was frozen. Added `onPeriodChange?: (period: FeeEfficiencyWindow)`
to `InflectionInsightsPanelProps`; `BooksTab` injects it via the existing `cloneElement`
mechanism (same path as `onHouseholdClick`). The panel's local `Window` vocabulary
(`qtd/ytd/1y/max`) is mapped to `FeeEfficiencyWindow` via `WINDOW_TO_FEE_PERIOD` inside a
`handleWindowChange` callback that updates local state AND emits upward.

### FE-4 — explicit window-unavailable state
Removed the silent `windows[available_windows[0]]` (== QTD) fallback in `periodAdvisors`.
Added a `periodWindowAvailable` memo; when the selected window is absent from
`leaderboard.json`, the render path shows an explicit "{window} advisor metrics aren't
available for this firm yet" panel instead of QTD numbers under the wrong label.
Data-driven and self-correcting — 1Y/3Y light up automatically once ADVI_BIWNDW.002
materializes those windows.

**Interim-state note:** `feePeriod` defaults to `trailing_1y` for both firms, and
neither `leaderboard.json` carries 1Y yet (pre-chain-run). So on first load the Books-tab
advisor-summary table now shows the explicit "1Y unavailable" message rather than the
old silent-QTD render. This is the *intended* honest behavior of FE-4 and resolves to a
populated table the moment the BIWNDW.002 1Y/3Y emit (already committed `a2010a2b3`)
materializes in the co-landing INF/D_04 chain run. Flagged in RAVC2 to COO.

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx | FE-1 map fix + module-scope hoist; FE-2 cloneElement onPeriodChange inject; FE-4 periodWindowAvailable + explicit unavailable render | Yes — DEV `fe881e2b` |
| portal/src/pages/AdvisorIntelligence/_partners/inflection/InflectionInsightsPanel.tsx | FE-2 onPeriodChange prop + WINDOW_TO_FEE_PERIOD map + handleWindowChange | Yes — DEV `fe881e2b` |

Contract change: `InflectionInsightsPanelProps` gains `onPeriodChange` (optional,
cloneElement-injected). Minor prop addition on an existing panel — not a new
panel/endpoint/tab, so pod_inventory.xml unchanged.

## Compiler Tools

| Tool | Phase | Result |
|------|-------|--------|
| `comp-transform schema-check BooksTab` | before | Component not found (BooksTab is exported from ClientsTab) |
| `comp-transform schema-check ClientsTab` | before/after | Clean — all rendered fields match response types; UNUSED fields pre-existing, unrelated |
| `comp-transform schema-check FeeEfficiencyPanel` | before | Clean |
| `comp-transform schema-check InflectionInsightsPanel` | before/after | Clean — `FirmConcentrationsArtifact: type not found` is pre-existing (type lives in api endpoints file, not types.ts), not introduced |
| `comp-cache collisions` | before/after | `firm-leaderboard` shared key — pre-existing intentional dedup (all `PlatinumLeaderboardResponse`). No fetch/queryKey touched; no new collision. |
| `bun run typecheck` (tsc -b --noEmit) | before commit | PASS |
| `bun run build` | before commit | PASS — `built in 17.06s`; only pre-existing chunk-size advisory |

## Acceptance Criteria

| AC | Status |
|----|--------|
| AC1 FE-1 max->'MAX' | Implemented + static-verified. Visual confirmation pending. |
| AC2 FE-2 Inflection window drives table | Implemented + typecheck-verified wiring. Visual confirmation pending. |
| AC3 FE-4 explicit unavailable state | Implemented. Visual confirmation pending. |
| AC4 schema-check clean / cache / no emoji / build clean | DONE |
| AC5 shipped to DEV; FE-5 not done | DONE — DEV `fe881e2b`; submodule pointer = DT |

## Postmortem: visual smoke not run

### Root Cause
The TO Phase-3 mandate is `/frontend-dev` or a browser smoke. The `/frontend-dev`
plugin skill launched but its coordinator delegates to subagents
(`frontend-dev:frontend-tester`, `frontend-dev:dev-server-manager`) that are not
registered in this session's agent registry — `Agent` rejects them. No
browser/Playwright tool is available to run a headless smoke directly.

### Resolution
- Implementation complete and statically verified (typecheck + build + schema-check
  + cache all clean). — DONE
- Visual confirmation of AC1/AC2/AC3 — BLOCKED on an interactive `/frontend-dev`
  run or Andrew's browser. Handed to COO/Andrew in RAVC2.

## Current State

| Item | Status |
|------|--------|
| Inbox | 1 msg acted on — DS CC RAVC2 INFGRO.007 (window-TWR fix); ACK sent |
| ADVI_BIWNDW.001 | FE-1/FE-2/FE-4 shipped DEV `fe881e2b`; visual smoke pending |
| ADVI_INFGRO.005 | HELD — criterion (a) fix-shipped not-yet-materialized; (b) Finding B / INF_C_02 separate TO pending |
| ADVI_INFGRO.006 | pending — gated on .005 + DS~A MAX coverage proof |
| Portal DEV HEAD | `fe881e2b` |
| Watcher | LIVE (`bdd9x231j` relaunched) |

## Next Steps

- [COO] RAVC2 received — implementation done + statically verified. Visual smoke is the
  one open acceptance item; needs an interactive `/frontend-dev` run.
- [DT 0.4] Review portal DEV `fe881e2b`, push, handle submodule pointer per standard QA gate.
- [Andrew / DE-interactive] Optional: cross-firm Books-tab visual confirmation —
  Max toggle differs from QTD for both firms; Inflection BI selector drives the table;
  1Y/3Y show the explicit unavailable message pre-backfill.
- [DE] On DS post-chain-run materialized `leaderboard.json` verification: re-pull, confirm
  plausible window TWRs, advance INFGRO.005 toward close (still also gated on criterion b).
