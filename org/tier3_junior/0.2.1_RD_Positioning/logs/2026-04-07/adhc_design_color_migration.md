# ADHC_DESIGN-002 Color Migration -- 0.2.1_RD_Positioning

**Date:** 2026-04-07
**Task Order:** ADHC_DESIGN-002
**Scope:** portal/src/pages/Positioning/

## Objective

Migrate all hardcoded hex colors in Positioning page to imports from `@/lib/chartColors.ts`. Run Design QA checklist and fix failures.

---

## Work Completed

### 1. HoldingsTab.tsx -- Hex Migration (~50 instances)

| Category | Before | After |
|----------|--------|-------|
| PORTFOLIOS colors (6 entries) | Hardcoded hex per portfolio | `PALETTE.opalIndigo`, `.orange500`, `.amber500`, `.green500`, `.blue500`, `.red500` |
| ASSET_CLASS_COLORS (3 entries) | Hardcoded `#10b981`, `#3b82f6`, `#f59e0b` | `ASSET_CLASS.fixedIncome`, `.equity`, `.cash` |
| SUB_ASSET_CLASS_COLORS (24 entries) | Full local duplicate of green+blue gradient | `SUB_ASSET_COLORS` imported directly from chartColors |
| getTextColorForBg function | Local 20-line function with hardcoded hex array | Replaced with imported `getSubAssetTextColor` |
| getReturnTextColor (3 hex) | `#34d399`, `#f87171`, `#9ca3af` | `PERF.positive`, `.negative`, `.neutral` |
| Treemap fallback colors (2 hex) | `#3b82f6`, `#6b7280` | `PALETTE.blue500`, `PALETTE.gray500` |
| Inline `#fff` (6 instances) | `color: '#fff'` | `color: PALETTE.white` |
| Portfolio selector `#fff` (1 instance) | `isActive ? '#fff' : ...` | `isActive ? PALETTE.white : ...` |

### 2. PositioningSummary.tsx -- Hex Migration (4 instances)

| Category | Before | After |
|----------|--------|-------|
| COLORS object (2 entries) | `#10b981`, `#3b82f6` | `ASSET_CLASS.fixedIncome`, `ASSET_CLASS.equity` |
| getRowColor (2 entries) | `#10b981`, `#3b82f6` | `ASSET_CLASS.fixedIncome`, `ASSET_CLASS.equity` |

### 3. README.md -- Documentation Update

Updated code example showing ASSET_CLASS_COLORS to reflect import pattern instead of hardcoded hex.

### 4. Design QA Checklist

| Check | Result |
|-------|--------|
| Control labels canonical | PASS -- both View: labels use `text-xs text-white/50 tracking-wider` |
| No hardcoded hex | PASS -- zero hex in TS/TSX files |
| Tabular figures | PASS -- numeric columns use `font-mono` |
| Panel primitives | PASS -- both files use Panel/PanelHeader/PanelContent |
| Build clean | PASS -- zero Positioning errors (pre-existing errors in Attribution + Macroeconomics are outside scope) |

---

## Notes

- `SUB_ASSET_COLORS` in chartColors.ts maps 'International' to `blue700` (#1d4ed8). The local HoldingsTab had it as `blue600` (#2563eb). Standardized to chartColors.ts canonical value. Minor visual difference (one blue shade darker).
- Tailwind utility classes (`bg-green-500/10`, `bg-blue-500/5`, etc.) in table headers/cells are design-system references, not hardcoded hex. Left as-is.
- rgba() values for return heatmap backgrounds (emerald-500/red-500 at various opacities) are not hex and were not in scope per the grep pattern. Left as-is.

---

## Files Modified

| File | Change |
|------|--------|
| tabs/HoldingsTab.tsx | Import chartColors; replace all hex with PALETTE/ASSET_CLASS/SUB_ASSET_COLORS/PERF refs; remove getTextColorForBg |
| panels/PositioningSummary.tsx | Import ASSET_CLASS; replace COLORS and getRowColor hex |
| README.md | Update code example |
| page_inventory.xml | Update color system note |

---

## Status

**COMPLETE** -- all acceptance criteria met.
