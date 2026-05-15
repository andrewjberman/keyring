# P1 Circular Import Fix — MarketPerformance.tsx
**Date:** 2026-05-14
**Agent:** 0.1.0_DE_MarketIntelligence
**Portal DEV commit:** `de61e377`

---

## Objective

Fix P1 dynamic-import failure on MarketPerformance page: `TypeError: Failed to fetch dynamically imported module: http://localhost:5173/src/pages/MarketPerformance/index.ts`

## Inbound Context

Diagnosed and handed off by `0.4.0_DE_ClientPlatform` via RAVC. Root cause confirmed:

`MarketPerformance.tsx:15-24` imported `MultiAssetTab, EquitiesTab, FixedIncomeTab, CommoditiesTab, ExecutiveSummaryPanel, SentimentPanel, useMarketData, DEFAULT_TAB` from `./index`. The barrel at `index.ts:7` re-exports `MarketPerformance` from `./MarketPerformance`. Circular ES-module dependency — Vite can resolve it in many configurations but chunk-graph perturbation from `SHARED.005` inner-component extraction flipped it from "works" to runtime failure.

## Work Completed

**1 file changed, 4 insertions, 10 deletions**

Replaced barrel import with direct source imports:

| Before | After |
|--------|-------|
| `import { ..., DEFAULT_TAB } from './index'` (10 LOC) | `import { MultiAssetTab, EquitiesTab, FixedIncomeTab, CommoditiesTab } from './tabs'` |
| | `import { ExecutiveSummaryPanel, SentimentPanel } from './panels'` |
| | `import { useMarketData } from './hooks'` |
| | `import { DEFAULT_TAB } from './constants'` |

`index.ts` barrel unchanged — external consumers (App.tsx, router) continue to import from `./index`.

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| TypeScript | `bun run typecheck` (tsc -b --noEmit) | Exit 0 — clean |
| comp-tooltip | N/A — no tooltip changes in this fix | Skipped |

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/MarketPerformance/MarketPerformance.tsx` | Replace ./index barrel import with direct imports from ./tabs, ./panels, ./hooks, ./constants | Yes - DEV `de61e377` |

## Decisions Made

1. Kept `index.ts` barrel intact — breaking the barrel would require coordinating with App.tsx and router; the fix only needs MarketPerformance.tsx to stop self-referencing through it.
2. DT is QA gate for push — not my responsibility to push.

## Blockers

None.

## Current State

- P1 circular import fix: COMPLETE (de61e377, awaiting DT push)
- All prior TOs (ADHC_DESIGN.026, .029, DEBT_1STRUN.001): COMPLETE, pushed to origin/DEV + PROD
- No pending TOs in queue
- RAVC closed with 0.4.0_DE_ClientPlatform and status reported to 2.0.0_SA_COO

## Next Steps

- [DevOps] Push `de61e377` from portal DEV
