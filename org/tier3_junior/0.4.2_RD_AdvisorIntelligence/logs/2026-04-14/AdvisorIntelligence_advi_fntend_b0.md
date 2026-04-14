# Session Log — ADVI_FNTEND.B0 FE-trivial sweep

**Agent:** 0.4.2_RD_AdvisorIntelligence
**Date:** 2026-04-14
**TO:** `ADVI_FNTEND.B0.rd-fe-trivial-sweep`
**Branch:** portal `DEV`
**Commit:** `5ea017c` (portal)
**Status:** Code complete; /frontend-dev Phase 2 pending external trigger.

## Work Shipped

### B2 — ClientsTable Fee pill nowrap
`panels/ClientsTable.tsx` — added `whitespace-nowrap` to both Fee and No-Fee pill spans; header column width `w-16` -> `w-20` so the wider No-Fee label has room without wrapping. Applied to both pills (not just No-Fee) for visual consistency.

### B4 — AdvisorBookClientDetail readonlyAssetClass
`AdvisorBookClientDetail.tsx:252` — added `readonlyAssetClass` prop to `<CanonicalBookView level="l3">`. Propagates into `ConsolidatedOverviewPanel` which already short-circuits the donut `dataPointSelection` event and the legend button wrapping when the prop is true.

### B10 — AdvisorBookAccountDetail readonlyAssetClass
`AdvisorBookAccountDetail.tsx:114` — added `readonlyAssetClass` prop to `<CanonicalBookView level="l4">`. Same propagation path as B4.

### G1 — Top Holdings palette audit (no-op)
Grepped for `top_holdings|topHoldings|Top Holdings` across `portal/src/`. The only render site is `ConsolidatedOverviewPanel.tsx` (lines 437-456). It already resolves colors via `colorFor = mixPieColor` (line 60) at every Top Holdings bar (`backgroundColor: colorFor(item.asset_class)` at 446, 456). `MIX_PIE` in `src/lib/chartColors.ts:395` maps `equity -> blue500`, `fixed_income -> green500`, `alternatives -> orange500` — matches the Assets Overview canonical (blue/green/orange). No code change.

### D5 — Continuous-ADV Client-N pseudonymization
`tabs/DistributionTab.tsx`.

New module-level helper at line ~481:
```ts
function pseudonymizeChildLabel(key, cohort, isDrilled, ordinalMap): string
```
Returns `Client ${ordinalMap[key]}` when `cohort === 'adv' && isDrilled && key !== 'Other'` and the key has a registered ordinal; else falls through to `getCategoryDisplayName`.

**Stable ordinal maps** — one per drill-parent, derived from the server-sorted full child list so ordinals persist through top-9+Other truncation and `selectedChildKey` collapse. Added `childOrdinalMap` useMemo in both views:

- `ContinuousNnaDivergingView` — keyed off `data.nna_adv_drill[drillParent].categories`
- `ContinuousChartView` — keyed off `viewData.categories` (via `adv_drill[drillParent]`)

**Call-site swaps (6):** breadcrumb child (1295, 1308, 2022), legend category (1445, 2180), tooltip row (2249). Stacked bar cells themselves have no text label — the tooltip row covers the bar-level readout.

**Note forced:** `(pseudonymized)` label at both hero captions is no longer gated by `!canSeeCleartext()`; renders whenever `cohort === 'adv' && isDrilled`. Removed now-unused `const { canSeeCleartext } = useAuth()` from both views (SnapshotDistributionView keeps it — unrelated use site).

**Design note:** For the ContinuousNnaDivergingView the `drillChild` path is only populated by GEO (city-level); ADV in that component has no L2 child drill today. The helper is wired per spec and is a safe no-op on GEO (`cohort === 'adv'` gate). If/when ADV NNA gets a true child drill, the ordinal map is already in place.

## Acceptance
1. /frontend-dev No-Fee pill on single line — CODE LANDED (whitespace-nowrap + w-20).
2. Client/Account L1 drills non-clickable Asset Mix — CODE LANDED (readonlyAssetClass prop threaded).
3. Top Holdings palette matches Assets Overview — VERIFIED (mixPieColor at all render sites; MIX_PIE palette matches).
4. Continuous-ADV drilled Client N labels — CODE LANDED (6 call sites swapped, (pseudonymized) note forced).
5. /frontend-dev closed-loop pass — PENDING external trigger (Playwright session not launched this turn).
6. MCP COMPLETE to COO — TO BE SENT after parent commit.

## Compiler Tools

| Tool | Args | Result | Why |
|------|------|--------|-----|
| comp-transform schema-check | CanonicalBookView | OK — all rendered fields match | Phase 1 per TO mandate (B4+B10 propagation) |
| comp-transform schema-check | ConsolidatedOverviewPanel | OK — all rendered fields match | Phase 1 per TO mandate (G1 palette) |
| comp-transform schema-check | DistributionTab | OK — 4 useQuery sources, NOTE (useQuery alias, not missing); 9+13+3+2 unused unrelated | Phase 1 per TO mandate (D5 6 call sites; UNUSED unrelated to pseudonymization) |
| tsc --noEmit | (full portal) | exit 0 | Pre-commit verification |

No findings blocked work. All schema checks clean.

## Files Changed
- `portal/src/pages/AdvisorIntelligence/panels/ClientsTable.tsx` (B2)
- `portal/src/pages/AdvisorIntelligence/AdvisorBookClientDetail.tsx` (B4)
- `portal/src/pages/AdvisorIntelligence/AdvisorBookAccountDetail.tsx` (B10)
- `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` (D5 — helper + 2 ordinal maps + 6 swaps + 2 `canSeeCleartext` destructure removals + 2 note-gate removals)
