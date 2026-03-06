# Scanner Controls: Category Chip Color + Distribution Bar Tooltip — 0.3.4_RD_SecurityScanner

**Date:** 2026-03-06
**Portal DEV commit:** `8c1ab08`

## Objective

Two visual improvements to the ScannerHeaderPanel controls table and distribution bar:
1. Category cell — render a colored chip badge (light tint + colored text) matching the factor's category HSL color.
2. Distribution bar — replace native `title` attribute with the canonical portal `Tooltip` component (indigo popup), showing factor name and weight on hover.

---

## Work Completed

### 1. Category Cell Chip

Added a `<span>` badge inside the Category `<td>`. Uses `getCategoryColor` (already computed per row as `catColor`) with `hsla(${catColor}, 0.15)` background, `hsl(${catColor})` text, and `hsla(${catColor}, 0.25)` border. Capitalized, `rounded-md`, `text-xs font-medium`. This matches the chip color system used by `FactorChip` (colored dot) while adapting it to a table cell context.

### 2. Distribution Bar Tooltip

Imported `Tooltip` from `@/components/Tooltip`. Wrapped each bar segment `<div>` in a `<Tooltip>` with:
- `content={`${f.name}: ${w}%`}`
- `side="top"`
- `preserveLayout` (renders as `display: contents` so the flex bar layout is unaffected)
- `key` moved to the `<Tooltip>` wrapper

Removed the `title` attribute from the inner div (replaced entirely by Tooltip).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `preserveLayout` on bar Tooltip | The bar is a flex row with `overflow-hidden`; a non-contents wrapper div would break the flex layout or escape the clip boundary |
| `hsla` for chip background/border, `hsl` for text | Low-opacity tint gives the "light chip" feel without washing out the text; full-saturation text reads clearly against the dark table row |
| Tooltip content: `${f.name}: ${w}%` | Directly answers "what percentage this factor occupies" — matches the existing chip label convention |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/SecurityScanner/components/ScannerHeaderPanel.tsx` | Import Tooltip; colored chip in Category td; Tooltip on distribution bar segments | Yes — `8c1ab08` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`

Category cell now renders a light colored chip per factor (HSL tint matching the FactorChip dot color). Distribution bar segments respond to hover with the canonical indigo `Tooltip` popup showing `{factor name}: {weight}%`. Work is local — needs portal DEV commit.

---

## Next Steps

1. ~~Commit portal DEV~~ — done, `8c1ab08`

**Files to touch next:**
- None pending.
