# ADVI_GLDRST.018: Wire market_growth + synthetic_correction -- 0.4.0_DE_ClientPlatform

**Date:** 2026-04-06
**Task Order:** ADVI_GLDRST.018.de-portal-nna-growth-wiring.md
**Project:** ADVI_GLDRST

**Portal DEV commit:** `478badb`
**Workspace CLOUD:** Lambda change uncommitted (DT deploy responsibility)

---

## Objective

Wire the new `market_growth` and `synthetic_correction` fields from
`client_performance.parquet` into the portal. Display the AUA decomposition
(NNA vs Market Growth vs AUA Reconciliation) at the L3 relationship drill level.

---

## Work Completed

### 1. Lambda Column Addition -- COMPLETE (needs DT deploy)

Modified `handle_books_timeseries()` in `opal-partners-data/lambda_function.py`:
- Added `market_growth`, `synthetic_correction` to the relationship column selection
- Added both to the optional output loop (NaN -> null handling)

File: `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`
This change is in the workspace repo (not portal submodule). DT must commit + deploy.

### 2. TypeScript Interface Update -- COMPLETE

Added to `BooksTimeseriesPoint` in `types.ts`:
- `market_growth: number | null`
- `synthetic_correction: number | null`

### 3. AUA Decomposition Panel -- COMPLETE

New component `AuaDecompositionPanel` renders at L3 (relationship) level:
- Fetches trailing 90d from `getBooksRelationshipTimeseries`
- Sums `nna`, `market_growth`, `synthetic_correction` over the window
- Displays 4 cards: Net New Assets, Market Growth, AUA Reconciliation, Total AUA Change
- **Hidden when fields are null** (pre-.017 data, graceful degradation)
- "AUA Reconciliation" label per Andrew's approved naming

### 4. Type Safety -- VERIFIED

`bunx tsc -b` passes with zero errors.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/AdvisorIntelligence/types.ts | Added market_growth, synthetic_correction to BooksTimeseriesPoint | Yes - DEV `478badb` |
| portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx | AuaDecompositionPanel + L3 decomposition fetch | Yes - DEV `478badb` |
| infra/aws/.../opal-partners-data/lambda_function.py | Added columns to handle_books_timeseries | NOT COMMITTED (workspace repo, DT responsibility) |

---

## Decisions Made

| Decision | Rationale |
|---|---|
| L3 only (not N1/L2) for initial decomposition | N1/L2 data comes from static gold JSON artifacts that don't yet include these fields. L3 timeseries is the only Lambda-served surface with access to client_performance.parquet columns. |
| Trailing 90d window | Matches QTD reporting cadence. Long enough to show meaningful trends, short enough to be responsive to recent changes. |
| Hidden when null | Graceful degradation for data produced before .017 ran. |

---

## Blockers

**Lambda deploy needed.** The `handle_books_timeseries` change is in the workspace repo at
`infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`.
Until DT commits this and deploys (`partners-api` pipeline), the portal will fetch
timeseries without the new columns -- the decomposition panel will remain hidden
(null handling works correctly).

---

## Next Steps

1. **[DevOps] Commit Lambda change + deploy partners-api** -- the portal commit is ready, Lambda change is staged locally
2. **[DevOps] Push portal DEV + merge to PROD** for portal commit `478badb`
3. **[Data Scientist] Extend decomposition to static gold JSON** -- add market_growth/synthetic_correction to advisor book.json and clients_tab.json for N1/L2 coverage (future TO)
