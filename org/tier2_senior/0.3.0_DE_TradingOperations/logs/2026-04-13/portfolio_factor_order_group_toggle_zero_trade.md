# Portfolio Management — Factor Order, Group Toggle, Zero Trade Fix

**Agent:** 0.3.0_DE_TradingOperations
**Date:** 2026-04-13
**Portal DEV commit:** `02c46eb`

---

## Objective

Three requests from Yang regarding the Portfolio Management Trade tab:
1. Order individual factors in SecurityDetailModal by canonical PKL order (not alpha-desc within group)
2. Add Factor/Group toggle in SecurityDetailModal with group-level aggregates
3. Fix Final Trade column: entering 0 treated as null; delete should reset to optimizer

---

## Work Completed

### 1. Canonical Factor Order in SecurityDetailModal

**Root cause:** The existing sort was `canonicalGroupIndex(a.group) - canonicalGroupIndex(b.group)` — groups were in canonical order, but within each group, factors preserved their PKL array order, which comes alpha-desc from the model.

**Fix:** Added `CANONICAL_FACTOR_ORDER` (all 33 factors in signal DataFrame row order) and `canonicalFactorIndex()` to `src/utils/factorOrder.ts`. This is a total order covering both group and within-group position — mirrors `factorDescriptions.ts` key order (already the declared source of truth).

Updated `SecurityDetailModal` sort to `canonicalFactorIndex(a.factor) - canonicalFactorIndex(b.factor)`. Single key, full canonical sort, no secondary groupBy needed.

### 2. Factor/Group Toggle in SecurityDetailModal

Added `factorView: 'factor' | 'group'` state and a Factor/Group toggle button pair in the Factor Breakdown section header.

- **Factor view** — unchanged individual rows, now in canonical order
- **Group view** — one row per factor group (canonical group order), showing:
  - Group name
  - Factors (count of individual factors in that group)
  - Avg Zscore (average across factors in the group)
  - Total Alpha (sum of alpha contributions)
  - Contrib % (sum of % contributions)

Computed via `useMemo` with `Map`-based aggregation over `security.factors`. Two `react-hooks/preserve-manual-memoization` suppressions with justification (nullable optional chain prevents compiler optimization).

### 3. Final Trade 0 vs. Null

**Root cause:**
- AG Grid `agNumberCellEditor` returns `null` when user clears/deletes, `0` when user types `0`
- Both paths reached `onFinalTradeUpdate(ticker, newValue)` with no distinction
- `valueFormatter` showed `–` for any `Math.abs(val) < 0.005` — so typing `0` looked identical to clearing

**Fix (three parts):**

**PortfolioGrid.tsx `onCellValueChanged`:** Guard for `newValue === null | undefined` → call `onFinalTradeUpdate(ticker, null)` and redraw; return early before weight validation.

**PortfolioGrid.tsx `valueFormatter`:** When `params.data?.isOverridden && Math.abs(val) < 0.005`, display `0.00%` (user explicitly held). Otherwise unchanged dash for optimizer-hold rows.

**useOptimizationState.ts `updateFinalTrade`:** Accepts `number | null`. On `null` → resets `finalTrade` to `sec.trade ?? 0`, `finalWeight` to `sec.optimizedWeight ?? 0`, `isOverridden = false`. On number → existing logic unchanged. Propagated type through `TradeTab.tsx` interface and `PortfolioGrid.tsx` prop.

---

## Compiler Tools

| Tool | Result |
|------|--------|
| `bun run lint` | Before: 42 warnings. After: 40 warnings, 0 errors. Net -2 (new suppressed warnings offset by pre-existing cleanup). |
| `bun run build` | Pre-existing TS error in `PageSurfaceControl.tsx` (unrelated). My 5 changed files: no new TS errors. |

No comp-trace/comp-blast needed — changes are local to `SecurityDetailModal`, `PortfolioGrid`, `TradeTab`, `useOptimizationState`, and `factorOrder`. No cross-pod shared files or S3 key changes.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `src/utils/factorOrder.ts` | Add `CANONICAL_FACTOR_ORDER` + `canonicalFactorIndex()` | Yes - DEV `02c46eb` |
| `src/pages/PortfolioManagement/components/SecurityDetailModal.tsx` | Canonical sort, Factor/Group toggle + group aggregate view | Yes - DEV `02c46eb` |
| `src/pages/PortfolioManagement/components/PortfolioGrid.tsx` | Null guard in `onCellValueChanged`, `0.00%` formatter, prop type | Yes - DEV `02c46eb` |
| `src/pages/PortfolioManagement/tabs/TradeTab.tsx` | `onUpdateFinalTrade` type: `number | null` | Yes - DEV `02c46eb` |
| `src/pages/PortfolioManagement/hooks/useOptimizationState.ts` | `updateFinalTrade` handles null = reset | Yes - DEV `02c46eb` |

---

## Decisions Made

- **`canonicalFactorIndex` as total order:** Since all 33 factors span 15 groups in the same canonical sequence, a single factor-level sort index covers both requirements (group order + within-group order). No need for a two-key sort.
- **`isOverridden` as the 0.00% sentinel:** `finalTrade === 0` cannot distinguish "optimizer says hold" from "user explicitly overrode to 0" because initialization sets `finalTrade = sec.trade ?? 0`. `isOverridden` is already the correct signal: it's `true` only when the PM overrode, and `false` when reset or unchanged from optimizer.
- **Reset-on-null restores optimizer state cleanly:** Sets `finalTrade = sec.trade`, `finalWeight = sec.optimizedWeight`, `isOverridden = false`. This is indistinguishable from the initial load state for that security.

---

## Current State

All three requests complete. Awaiting DT push.

## Next Steps

- [DevOps 0.3.0_DT] Push portal DEV branch (commit `02c46eb`)
