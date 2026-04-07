# ADHC_DESIGN-018 Overflow Containment -- 0.4.1_RD_ModelPortfolios
**Date:** 2026-04-07
**Task Order:** ADHC_DESIGN.018.rd-overflow-containment.md
**Status:** Complete

## Audit Findings + Fixes

### ModelPortfolios.tsx

| # | Location | Issue | Fix |
|---|----------|-------|-----|
| 1 | Line 524 | Two-column flex layout: children lack min-w-0, won't shrink below content width at narrow viewports | Added `overflow-hidden` to parent flex container |
| 2 | Line 526 | Left partition (donut + metrics) flex child | Added `min-w-0` to allow flex shrink |
| 3 | Line 776 | Right partition (distribution) flex child | Added `min-w-0` to allow flex shrink |
| 4 | Line 541 | Donut chart container: ApexCharts fixed-size SVG can bleed past container bounds | Added `overflow-hidden` |
| 5 | Line 997 | Period End Summary BarChart wrapper: no overflow containment on chart div | Added `overflow-hidden` |
| 6 | Line 1193 | Daily AUA Analysis AreaChart wrapper: no overflow containment on chart div | Added `overflow-hidden` |

### PeersTab.tsx

| # | Location | Issue | Fix |
|---|----------|-------|-----|
| 7 | Line 462 | Legend row: multiple items with gap-8 overflow at narrow viewports | Added `flex-wrap` |
| 8 | Line 494 | Quartile charts row: multiple 160px SVGs crowd at 1024px | Added `overflow-x-auto` |

### Already Correct (no fix needed)

- ResponsiveContainer width="100%" on both BarChart and AreaChart -- properly constrained
- Distribution chart containers already have `min-w-0`
- Panel components provide outer containment via their own overflow behavior
- Tooltip `wrapperStyle={{ zIndex: 40 }}` is standard Recharts pattern
- PeersTab SVG `overflow-visible` is intentional for arrow markers; clipped by parent panel

## Verification

- `bun run build`: PASS (12.73s, no errors)
- All dynamic-content containers now have explicit overflow handling
