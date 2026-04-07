# Session Log: ADHC_DESIGN.005 - Color Migration + Design QA

**Agent:** 0.2.5_RD_Macroeconomics
**Date:** 2026-04-07
**Task Order:** ADHC_DESIGN.005

## Summary

Migrated all hardcoded hex colors in Macroeconomics page to `@/lib/chartColors` PALETTE imports. Ran Design QA Pre-Commit Checklist. Build passes (only pre-existing Attribution error remains).

## Files Modified

| File | Changes |
|------|---------|
| `utils/percentileColor.ts` | Added PALETTE import; replaced 7 hex values in `getPercentileSolidColor()` |
| `constants.ts` | Added PALETTE import; replaced 10 hex values in VIX_REGIMES and MOVE_REGIMES |
| `tabs/YieldCurveTab.tsx` | Added PALETTE import; replaced 6 hex values in CURVE_COLORS and getCurveShape() |
| `tabs/VolatilityTab.tsx` | Added PALETTE import; replaced 12 hex values in PERCENTILE_COLORS, DEFAULT_REGIME_COLORS, getRegimeColor fallback, and chart Line stroke/activeDot; added `string` type annotation to fix TS narrow-type inference issue |
| `components/MacroTimeSeriesModal.tsx` | Added PALETTE import; replaced 12 hex values in getPercentileBandColors() line colors and chart Line stroke/activeDot |

## Shared File Edit (outside commit scope)

**`portal/src/lib/chartColors.ts`**: Added `nativeGreen500: '#22c55e'` and `nativeGreen400: '#4ade80'` to PALETTE. This color (Tailwind's actual green-500) was used in 14 files across the portal but was missing from the centralized palette. The existing `green500: '#10b981'` maps to Tailwind's emerald-500.

This edit is outside my commit scope -- needs DE/DT to include in their commit.

## Design QA Checklist Results

- [x] Control bar labels use canonical pattern (Display:, Period:)
- [x] No hardcoded hex colors (0 remaining)
- [x] Panel primitives used throughout
- [x] Chart library = Recharts (consistent)
- [x] `bun run build` succeeds (Macroeconomics scope)

## Notes

- Heatmap cell backgrounds in `getPercentileColor()` still use inline `rgba()` with dynamic opacity -- these are functional (opacity varies per percentile) and cannot be replaced with static PALETTE entries. Not hex.
- MacroTimeSeriesModal band colors in `getPercentileBandColors()` also use `rgba()` for transparent overlays -- same rationale.
- Pre-existing TS error in `Attribution/constants/holdings-shared.tsx:172` unrelated to this work.
