# Zebra Striping Fix — SecurityScanner Grids — 0.3.4_RD_SecurityScanner

**Date:** 2026-03-06
**Portal DEV commit:** pending

## Objective

Apply alternating row backgrounds (zebra striping) to both AG Grid instances on the SecurityScanner page: UniverseDataTab and UniverseScannerTab. Previous session attempted this but crashed before completion.

---

## Work Completed

### 1. Root Cause Analysis

Previous session made three attempts:
1. CSS variable `--ag-odd-row-background-color` — no effect (AG Grid v35 quartz-dark ignores this variable)
2. `getRowStyle` callback — AG Grid's own row background inline styles override inline styles returned from `getRowStyle`
3. Scoped `<style>` tag with `.scanner-grid .ag-row-even` — correct mechanism but session crashed mid-way

State at session start:
- **UniverseDataTab**: had `scanner-grid` class + `<style>` tag but without `!important` (loses to AG Grid's own row CSS at equal specificity)
- **UniverseScannerTab**: had `scanner-grid` class + dangling `getRowStyle={getRowStyle}` prop (callback deleted but prop reference left), missing `<style>` tag entirely

### 2. Canonical Pattern Reference

PortfolioGrid (`portal/src/pages/PortfolioManagement/components/PortfolioGrid.tsx:469-499`) uses a `<style>` tag inside the grid wrapper div with a scoped class name: `.portfolio-grid-custom .ag-row-even { background-color: rgba(0, 0, 0, 0.1); }`. This is the confirmed working pattern.

Key difference: PortfolioGrid works because AG Grid's own `.ag-row` background rule and our `.ag-row-even` rule have equal CSS specificity (2 classes each). When specificity ties, last-loaded wins — PortfolioGrid's inline `<style>` happens to win. For certainty, added `!important` to SecurityScanner rules.

### 3. Fixes Applied

**UniverseDataTab** (`portal/src/pages/SecurityScanner/tabs/UniverseDataTab.tsx`):
- Added `!important` to `.scanner-grid .ag-row-even`
- Added explicit `.scanner-grid .ag-row-odd` rule (belt-and-suspenders contrast)
- Bumped even-row alpha from `0.1` to `0.15` for visibility

**UniverseScannerTab** (`portal/src/pages/SecurityScanner/tabs/UniverseScannerTab.tsx`):
- Removed dangling `getRowStyle={getRowStyle}` prop (callback no longer exists — runtime warning)
- Added `<style>` tag with `.scanner-grid .ag-row-even`, `.ag-row-odd`, `.ag-row:hover` — identical to UniverseDataTab

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Use `!important` on `.ag-row-even` | AG Grid v35 row background rules have equal specificity; `!important` guarantees our rule wins regardless of CSS load order |
| Add explicit `.ag-row-odd` rule | Makes the alternating pattern visible from both directions; odd rows get a very slight lift instead of the default flat color |
| Reuse `scanner-grid` class name across both tabs | Both tabs are never mounted simultaneously in the tab view; same CSS applies cleanly to both |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/SecurityScanner/tabs/UniverseDataTab.tsx` | Added `!important` + `.ag-row-odd` rule to `<style>` tag | No — local only |
| `portal/src/pages/SecurityScanner/tabs/UniverseScannerTab.tsx` | Removed dangling `getRowStyle` prop; added `<style>` tag with zebra CSS | No — local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`

Both SecurityScanner AG Grid tabs now have identical zebra striping: `.scanner-grid .ag-row-even { background-color: rgba(0, 0, 0, 0.15) !important; }` and `.scanner-grid .ag-row-odd { background-color: rgba(255, 255, 255, 0.02) !important; }`. The dangling undefined `getRowStyle` reference in UniverseScannerTab is removed. Work is local only — needs a portal DEV commit with `--author` flag before push.

---

## Next Steps

1. **Commit portal DEV** — `git commit --author="0.3.4_RD_SecurityScanner <0.3.4_RD_SecurityScanner@opal.agent>" -m "0.3.4_RD_SecurityScanner: SecurityScanner -- zebra striping on UniverseDataTab and UniverseScannerTab grids"`
2. **[0.3.0_DE_TradingOperations] Notify** — zebra striping complete; security scanner visual polish done

**Files to touch next:**
- None pending for this page.
