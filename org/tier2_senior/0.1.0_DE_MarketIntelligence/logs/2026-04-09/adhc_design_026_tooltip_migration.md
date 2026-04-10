# ADHC_DESIGN.026 -- Pod 0.1 Tooltip Migration to DataTooltip
**Date:** 2026-04-09
**Agent:** 0.1.0_DE_MarketIntelligence
**Task Order:** ADHC_DESIGN.026.de-tooltip-migration-pod-0.1.md
**Portal DEV commit:** `0e118be`

---

## Objective

Migrate all pod 0.1 inline data tooltips to the shared `<DataTooltip>` component (ADHC_DESIGN.025).

## Work Completed

8 tooltip sites migrated across 6 files. Net -34 LOC.

### Migration details

| File | Site | Variant | Action |
|------|------|---------|--------|
| FearGreedModal.tsx:188 | CompositeChartTooltip | A | Migrated to `<DataTooltip>` |
| FearGreedModal.tsx:223 | ComponentChartTooltip | A | Migrated to `<DataTooltip>` |
| FearGreedModal.tsx:282 | MethodologyTooltip popover | A | Restyled to canonical tokens, kept as div (CTO adjudication: popover interaction model) |
| IndexPerformanceModal.tsx:84 | PriceChartTooltip | A | Migrated to `<DataTooltip>` |
| MarketRegimeModal.tsx:185 | RegimeChartTooltip | A | Migrated to `<DataTooltip>` |
| RSIModal.tsx:194 | RSIChartTooltip | A | Migrated to `<DataTooltip>` |
| ExpectationsTab.tsx:38 | CMA bar chart tooltip | A (indigo bg) | Migrated to `<DataTooltip>` |
| ThemeBubble.tsx:105 | Theme bubble hover | D (slate-900) | Full rewrite to `<DataTooltip>` inside motion wrapper |

### Visual verification

Playwright headless screenshots captured post-login:
- Fear & Greed composite chart: DataTooltip visible (silver bg, 2px indigo border) -- verified
- Fear & Greed component chart: DataTooltip visible -- verified
- Index Performance (Nasdaq): DataTooltip visible ("Price: $21,683.61") -- verified
- RSI modal chart: renders correctly (tooltip not captured at exact hover point)
- Market Regime modal chart: renders correctly
- All pages load without crash

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-tooltip drift | `comp-tooltip drift` | 0 pod 0.1 hits except FearGreedModal:278 (intentional popover, restyled to canonical tokens) |
| comp-tooltip summary | `comp-tooltip summary` | 32 total sites, 11 canonical/migrated (was 11, now includes our 8 but some may still show as inline-silver) |

## Decisions Made

1. FearGreedModal:282 kept as inline div per TO specification -- it's a floating info popover (clickable, not hover), different interaction model from chart tooltips. Restyled `bg-header` + `border-white/20` to `semantic-background-chartTooltipBg` + `border-[hsl(var(--primary))]` to match DataTooltip visuals.
2. ThemeBubble: kept the `<motion.div>` wrapper for animation and positioning, replaced inner content with `<DataTooltip>`. Updated arrow border color from `border-t-slate-900` to `border-t-[hsl(var(--semantic-background-chartTooltipBg))]`.
3. ExpectationsTab: was using `semantic-action-primary` (indigo bg) -- migrated to DataTooltip which uses `chartTooltipBg` token.

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/components/market-performance/FearGreedModal.tsx | 2 chart tooltips -> DataTooltip, 1 popover restyled | Yes - DEV `0e118be` |
| portal/src/components/market-performance/IndexPerformanceModal.tsx | 1 chart tooltip -> DataTooltip | Yes - DEV `0e118be` |
| portal/src/components/market-performance/MarketRegimeModal.tsx | 1 chart tooltip -> DataTooltip | Yes - DEV `0e118be` |
| portal/src/components/market-performance/RSIModal.tsx | 1 chart tooltip -> DataTooltip | Yes - DEV `0e118be` |
| portal/src/pages/CapitalMarketAssumptions/tabs/ExpectationsTab.tsx | 1 chart tooltip -> DataTooltip | Yes - DEV `0e118be` |
| portal/src/pages/CausalityEngine/components/ThemeBubbleGalaxy/ThemeBubble.tsx | 1 Variant D -> DataTooltip | Yes - DEV `0e118be` |

## Blockers

None.

## Current State

- ADHC_DESIGN.026: COMPLETE
- ADHC_DESIGN.029: COMPLETE (prior commit `55bde3c`)

## Next Steps

- [DevOps] Push commits `55bde3c` and `0e118be` from portal DEV
- [0.4.0_DE] Coordinate TO-028 final audit sweep
