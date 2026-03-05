# COO Handoff: Trade Engine Visual Polish

**From:** 1.0.0_SA_CTO
**To:** 2.0.0_SA_COO
**Date:** 2026-03-04
**Priority:** Normal — Yang feedback, no production blockers

---

## PRD

`docs/architecture/TRADE_ENGINE_VISUAL_POLISH.md`

13 frontend-only items for the PortfolioManagement page. All visual/UX — no Lambda, no
Terraform, no infrastructure. Originated from Yang's direct feedback on the trade engine UI.

Stale data bug (Yang's item 1) excluded — already fixed via cache-busting push.

---

## Pod Assignment

**Pod 3 (TradingOperations)** — DE `0.3.0_DE_TradingOperations`

Single pod, single page. No cross-pod interfaces. No threads required.

---

## O3 Check Paths

Before issuing task orders, verify agent readiness:

| Path | What to check |
|------|---------------|
| `org/tier2_senior/0.3.0_DE_TradingOperations/logs/` | Latest session — current workload |
| `org/tier2_senior/0.3.0_DT_TradingOperations/logs/` | No deploy needed but confirm no conflicts |
| `org/tier3_junior/` | Check if Pod 3 RD agents exist; if not, DE handles directly |

---

## Suggested Task Order Decomposition

All 13 items are independent — no blocking dependencies. COO may regroup as needed.

### TO-1: Threshold Highlighting (Items 2, 3, 4, 5)

**Scope:** Risk Decomposition panel + Alpha tab + Sector tab
**Pattern:** Threshold-based color functions (same as existing `getTradeColor`)

| Location | Column | Green | Red |
|----------|--------|-------|-----|
| Risk Decomp — Exposure | Initial, Optimized | > 0.1 | < -0.1 |
| Risk Decomp — Exposure | Trade | > 0.05 | < -0.05 |
| Risk Decomp — Contribution | Initial, Optimized | -- | > 5 |
| Risk Decomp — Contribution | Delta | < -2 | > 2 |
| Alpha | Initial Bet, Optimized Bet, Trade | > 0.1 | < -0.1 |
| Alpha (By Group) | Same columns | > 0.1 | < -0.1 |
| Sector | Initial Bet, Optimized Bet | > 2 | < -2 |
| Sector | Trade | > 0.5 | < -0.5 |

**Files:**
- `portal/src/pages/PortfolioManagement/components/OptimizationSummaryHeader.tsx`
- `portal/src/pages/PortfolioManagement/tabs/AlphaTab.tsx`
- `portal/src/pages/PortfolioManagement/tabs/SectorTab.tsx`

---

### TO-2: Gradient Color Scales (Items 6, 8, 9)

**Scope:** Model tab + Trade tab
**Pattern:** Continuous gradient using `getGradientBackground` from PortfolioGrid.tsx

| Location | Columns | Scale |
|----------|---------|-------|
| Model tab | Coefficient, Weight | white-to-green (higher = green) |
| Trade tab | totalRisk, specRisk | green-to-red (higher = red, inverted) |
| Trade tab | initialBet | Same gradient as optimizedBet (already has it) |
| Trade tab | **NEW** finalBet = finalWeight - benchmarkWeight | Same gradient |

`finalBet` is a derived field computed in the browser. Same pattern as `finalTrade`.

**Files:**
- `portal/src/pages/PortfolioManagement/tabs/ModelTab.tsx`
- `portal/src/pages/PortfolioManagement/components/PortfolioGrid.tsx`

---

### TO-3: Trade Tab Formatting (Items 7, 10)

**Scope:** PortfolioGrid AG Grid column defs

| Change | Detail |
|--------|--------|
| Zero weights to dash | initialWeight, optimizedWeight, finalWeight, benchmarkWeight: display `--` when value === 0 |
| Size column coloring | L = green bg, M = yellow bg, O = red bg (muted/translucent for dark theme) |

**Files:**
- `portal/src/pages/PortfolioManagement/components/PortfolioGrid.tsx`

---

### TO-4: Capitalize + Canonical Group Ordering (Items 1, 11, 13)

**Scope:** AlphaTab, ModelTab, SecurityDetailModal
**Key deliverable:** Extract shared constant `CANONICAL_GROUP_ORDER` to `utils/factorOrder.ts`

```
size, efficiency, growth, management, profitability, quality, value,
analyst, governance, crowding, insider, short, beta, momentum, technical
```

| Change | Location |
|--------|----------|
| Capitalize group names in By Factor view | AlphaTab.tsx line 421 — add `capitalize` CSS class |
| Capitalize group names | ModelTab.tsx — group column cells |
| Capitalize group names + sort by canonical order | SecurityDetailModal.tsx — factor list |
| Replace alphabetical sort with canonical order | AlphaTab.tsx line 74 — replace `localeCompare` |
| Same canonical order in By Group view | ModelTab.tsx |

**Source of truth:** `factorDescriptions.ts` comment order = signal DataFrame row order in Yang's alpha PKL.
Lambda already preserves this order (`lambda_function.py` line 651-654). Frontend "By Factor" default
view is correct. Only "By Group" aggregated view has the alphabetical sort bug.

**Files:**
- `portal/src/pages/PortfolioManagement/utils/factorOrder.ts` (NEW — shared constant)
- `portal/src/pages/PortfolioManagement/tabs/AlphaTab.tsx`
- `portal/src/pages/PortfolioManagement/tabs/ModelTab.tsx`
- `portal/src/pages/PortfolioManagement/components/SecurityDetailModal.tsx`

---

### TO-5: Reset Zero Button (Item 12)

**Scope:** TradeTab + PortfolioManagement parent

| What | Detail |
|------|--------|
| Button location | Between "Reset All" and "Export" in TradeTab button group |
| Behavior | Sets `finalTrade = 0` for ALL securities (hold everything, no trades) |
| Implementation | `finalWeight = initialWeight` for every security |
| Distinct from | "Reset All" which restores `finalWeight = optimizedWeight` (optimizer suggestions) |

**Files:**
- `portal/src/pages/PortfolioManagement/tabs/TradeTab.tsx` — button (line ~368)
- `portal/src/pages/PortfolioManagement/PortfolioManagement.tsx` — `onResetZero` handler

---

## Key Reference Files

| File | Purpose |
|------|---------|
| `docs/architecture/TRADE_ENGINE_VISUAL_POLISH.md` | Full PRD with line numbers and current state |
| `portal/src/pages/PortfolioManagement/utils/factorDescriptions.ts` | Canonical group order source (33 factors, 15 groups) |
| `portal/src/pages/PortfolioManagement/utils/riskFactorFilter.ts` | YANG_STYLE_FACTORS (12 risk factors, separate from alpha factors) |
| `portal/src/pages/PortfolioManagement/components/PortfolioGrid.tsx` | `getGradientBackground` utility (lines 466-516) |
| `portal/src/pages/PortfolioManagement/tabs/TradeTab.tsx` | ECONOMY_ORDER pattern (line 249) — reference for canonical sort implementation |

---

## No Threads Required

Single-pod, single-page, no cross-pod interfaces. Direct task orders from COO to Pod 3 DE.

---

## Post-Completion

No deployment needed. Portal DEV commits from DE/RD, then DT push through standard QA gate.
No Lambda, Terraform, or infrastructure changes.
