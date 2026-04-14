# Session Log — ADVI_FNTEND.D6 OFC list style parity

**Agent:** 0.4.2_RD_AdvisorIntelligence
**Date:** 2026-04-14
**TO:** `ADVI_FNTEND.D6.rd-ofc-list-style-symmetry`
**Branch:** portal `DEV`
**Commit:** `814ba34`
**Status:** Code complete; /frontend-dev Phase 2 pending external trigger.

## Root Cause
`ContinuousChartView` legend (DistributionTab.tsx ~2183-2240) has three render branches:
1. `canLegendDrill && !isDrilled` → GEO/ADV top-level — `<button>` with `rounded px-1 py-0.5 w-full text-left` + hover/transition.
2. `isDrilled && canLegendDrill` → GEO/ADV drilled children — same `<button>` container.
3. Fallback (everything else, including OFC at L0) → bare `<div className="flex items-center gap-2">` with swatch missing `flex-shrink-0`.

OFC is not in `canLegendDrill` (set at line 2015: geo + non-drilled adv only) because `drillViewData` is always null for OFC in this component. So OFC renders through branch 3 — lacking the container padding and fixed-width swatch of branches 1/2. Visually, that made OFC rows look tighter and slightly shifted vs GEO/ADV.

## Fix
Branch 3: `<div className="flex items-center gap-2 rounded px-1 py-0.5 w-full text-left">` (matches GEO/ADV container metrics without hover/transition since no click), plus `flex-shrink-0` on the color swatch. Text classes unchanged — already `text-xs text-white/50` in all three branches.

## Acceptance
1. Font-size matches — same `text-xs` in all branches.
2. Font-weight matches — no weight specified anywhere (inherits normal) across branches.
3. Color matches — `text-white/50` identical.
4. Spacing matches — container now `rounded px-1 py-0.5 w-full` + swatch `flex-shrink-0`.
5. /frontend-dev pass — PENDING external trigger.
6. MCP COMPLETE — to be sent bundled with B0 COMPLETE after parent commit.

## Compiler Tools

| Tool | Args | Result |
|------|------|--------|
| comp-transform schema-check | DistributionTab | OK (no className/prop drift; run as part of B0 Phase 1 — still applies after D6) |

## Files Changed
- `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` (fallback legend branch container className + swatch flex-shrink-0)
