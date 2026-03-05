# Trade Engine Visual Polish PRD — 1.0.0_SA_CTO

**Date:** 2026-03-04
**Agent:** 1.0.0_SA_CTO
**Branch:** CLOUD

---

## Objective

Write a PRD for Yang's 13-item feedback list on the PortfolioManagement page. All items are
frontend-only visual/UX improvements: conditional cell highlighting, gradient color scales,
capitalize group names, canonical group ordering, zero-weight formatting, size column coloring,
new finalBet derived column, and a Reset Zero button.

---

## Work Completed

### 1. Yang Feedback Triage (13 items)

Went through Yang's raw feedback line by line. Resolved 3 ambiguities with Andrew:
- Size column "O" = Other (not a typo for S). L=green, M=yellow, O=red.
- Reset Zero = sets all finalTrade to 0 (hold everything). Confirmed.
- Canonical group order = from Yang's signal DataFrame, not alphabetical.

### 2. Canonical Factor Group Order Discovery

Traced through the data flow:
- Yang's alpha PKL contains a `signal` DataFrame with 33 factors in canonical row order
- `lambda_function.py` line 651-654: merges signal metadata and sorts by `order` column
- `factorDescriptions.ts`: comments organize factors by group in the same canonical sequence
- Alpha tab "By Factor" default view preserves Lambda array order (correct)
- Alpha tab "By Group" view sorts alphabetically (bug — line 74 of AlphaTab.tsx)

Canonical order: size, efficiency, growth, management, profitability, quality, value,
analyst, governance, crowding, insider, short, beta, momentum, technical (15 groups, 33 factors).

### 3. PRD Written

`docs/architecture/TRADE_ENGINE_VISUAL_POLISH.md` — 13 items fully spec'd with:
- Current state per component
- Exact thresholds and color rules
- File paths and line numbers
- Implementation patterns (threshold vs gradient vs CSS)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Pod 3 (TradingOperations) owns all work | PortfolioManagement page is Pod 3, not Pod 2 |
| Extract CANONICAL_GROUP_ORDER to shared util | Needed by AlphaTab, ModelTab, and SecurityDetailModal |
| Reuse getGradientBackground from PortfolioGrid | Already exists for optimizedBet gradient; extend to other columns |
| Stale data bug excluded from PRD | Already addressed via cache-busting fix pushed separately |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `docs/architecture/TRADE_ENGINE_VISUAL_POLISH.md` | New PRD | No -- local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

PRD written and reviewed with Andrew. COO handoff brief delivered in chat. Ready for
2.0.0_SA_COO to decompose into task orders for Pod 3 DE (0.3.0_DE_TradingOperations).
All 13 items are independent with no blocking dependencies.

---

## Next Steps

1. **[COO] Read PRD and decompose into task orders** -- `docs/architecture/TRADE_ENGINE_VISUAL_POLISH.md`
2. **[COO] Issue task orders to 0.3.0_DE_TradingOperations** -- suggested 5 groupings in handoff brief
3. **[DE] Decide RD delegation vs direct implementation** -- all items are portal-only
4. **[DT] Push portal DEV when DE work is committed** -- standard QA gate

**Do NOT:**
- Issue task orders to Pod 2 (PortfolioAnalytics) -- this is Pod 3 work
- Modify any Lambda or backend code -- all items are frontend-only
- Change the Lambda factor order -- the canonical order is already correct in the backend
