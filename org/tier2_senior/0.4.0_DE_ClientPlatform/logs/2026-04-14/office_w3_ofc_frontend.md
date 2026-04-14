# 0.4.0_DE_ClientPlatform — ADVI_OFFICE.W3 OFC Frontend
**Date:** 2026-04-14 (ET)
**Agent:** 0.4.0_DE_ClientPlatform
**Portal DEV commit:** `7dd0a7e` (4 files, +235/-42 lines)
**CLOUD commits:** session log + TO flip

---

## Summary

Implemented OFC (Office) as a third cohort toggle in DistributionTab alongside GEO and ADV.
Artifact verification confirmed 10 office segments live in platinum before starting.
Build clean (0 TypeScript errors). Blast radius unchanged (8 downstream nodes, 4 endpoints).

PROFAU.003 QA check: `capital_gains_ttm` and `cost_basis_by_year` confirmed present in
`platinum/advisors/travis_penfield/summary.json` — PROFAU.006 gate is clear.

---

## Changes Made

### types.ts
- `CumulativeChartViewMode`: added `'ofc'`
- `PartnerAnalyticsBaseView`: added `'ofc'`
- `NnaPeriodView`: added `ofc?: NnaView`
- `PartnerAnalyticsResponse.views`: added `ofc?: PartnerAnalyticsViewWithPeriods | PartnerAnalyticsView`
- `PlatinumCumulativeChartResponse`: added `ofc?: CumulativeChartView` and `nna_ofc?: NNASeriesView`
- `DonutSegment`: added `advisors?: OfficeAdvisorEntry[]`
- New `OfficeAdvisorEntry` interface: `{ key, label, aua, aua_pct, account_count, relationship_count, primary_role }`

### chartColors.ts
- `OFC_PALETTE`: 10 warm/earthy colors (amber400, orange600, red600, rose600, pink600,
  purple600, indigo600, green700, cyan600, amber600) — visually distinct from GEO (cool) and ADV (electric)

### DistributionTab.tsx
- `CohortOption`: added `'ofc'`
- `COHORT_OPTIONS`: added `{ value: 'ofc', label: 'OFC' }`
- `GrainView`: added `'ofc-aua' | 'ofc-nna'`
- `formatOfficeLabel`: new — titleCase with underscore-to-space (same as formatArchitectLabel)
- `formatCohortLabel`: extended for OFC
- `formatSegLabel`: extended for OFC (uses formatOfficeLabel at L0)
- `getCategoryColor`: added OFC_COLORS fallback
- `getCategoryDisplayName`: added formatOfficeLabel for OFC
- `getViewMode`: added `if (cohort === 'ofc') return 'ofc'`
- `selectedOfficeKey` state: tracks selected office for advisor list
- Reset effect: clears `selectedOfficeKey` on cohort/granularity change
- `drillParentKey`: returns `null` for OFC (no continuous drill)
- `handleDrillChange`: OFC is no-op (L1 is terminal list, not continuous drill)
- `categoryColorMap`: OFC branch uses `OFC_COLORS` + `chartData.ofc.categories`
- `SnapshotDistributionViewProps`: added `selectedOfficeKey`/`setSelectedOfficeKey`
- `SnapshotDistributionView`:
  - `viewMode`: 'ofc' for OFC cohort
  - `grainView`: 'ofc-aua'/'ofc-nna'
  - `nnaSnapshot`: reads `periodView.ofc` for NNA
  - `nnaDrillData`: reads `periodView.ofc?.drill`
  - `isDrilledDown`: extended for `cohort === 'ofc' && selectedOfficeKey !== null`
  - `parentSegment`: finds office segment by `canonicalKey` match
  - `donutCenterTotal`: applies firmHeadlineAua override for OFC (same as ADV)
  - `handleSegmentClick`: OFC toggles `selectedOfficeKey` + `selectedSegmentKey`
  - `handleDrillUp`: OFC clears `selectedOfficeKey`
  - Breadcrumb: 'Offices' label for OFC
  - Right partition: `OfcAdvisorListPanel` when OFC; distribution histogram hidden for OFC
- `OfcAdvisorListPanel` (new component):
  - Shows advisor list from `parentSegment.advisors` (embedded in donut segment)
  - enforceTop9Other applied
  - Renders: advisor name (colored dot), AUA, account count
  - Null-safe: shows placeholder when no office selected, "no data" when advisors empty
- `ContinuousChartView`:
  - `drillViewData`: returns null for OFC (no drill)
  - `viewData`: reads `data['ofc']` via `data[viewMode as 'geo' | 'adv' | 'ofc']`
  - drillParentKey resolution: empty candidates for OFC
- `ContinuousNnaDivergingView`:
  - `nnaSeriesView`: reads `data.nna_ofc` for OFC
  - `hasCanonicalBreakout`: always false for OFC (no by_ofc canonical path)
  - drillParentKey resolution: empty candidates for OFC
- `NnaQuarterlyStrip.getNna`: reads `v.ofc` for OFC NNA strip

### AUATrendChart.tsx
- `VIEW_CONFIG`: narrowed to `AuaTrendViewMode = Exclude<CumulativeChartViewMode, 'ofc'>`
  (legacy CumulativeChartResponse type doesn't have ofc — OFC is platinum-only)

---

## Compiler Tools

| Phase | Tool | Command | Result | Note |
|-------|------|---------|--------|------|
| 1 | comp-transform schema-check | schema-check DistributionTab | PASS | Alias pattern confirmed (chartData/analyticsData); all existing rendered fields match |
| 1 | comp-cache collisions | comp-cache collisions | PASS | 3 shared keys, all intentional; no new conflicts (OFC additive to same endpoints) |
| 1 | S3 spot-check | platinum/firm/partner_analytics_quarterly | PASS | views.ofc present, 10 offices (Austin, Dallas, LA, Jacksonville, Arkansas, Atlanta, Minnesota, KC, + 2) |
| 1 | S3 spot-check | platinum/firm/timeseries_chart.json | PASS | ofc + nna_ofc top-level keys present, 2291 data rows |
| 2 | comp-transform fields | fields DistributionTab | PASS | 17 fields; analyticsData.views.ofc accessed; OFC fields traced |
| 3 | comp-blast | comp-blast DistributionTab | PASS | 8 downstream nodes, 4 endpoints — UNCHANGED from baseline |
| 3 | bun build | bun run build | PASS | 0 TypeScript errors |

Compiler tools appended to org/compiler-tools-log.md.

---

## Acceptance Criteria Status

1. Three toggle buttons [GEO] [ADV] [OFC]: PASS (COHORT_OPTIONS extended)
2. OFC donut renders with office labels: PASS (reads views.ofc, formatOfficeLabel)
3. Clicking office → advisor list (AUA + account count): PASS (OfcAdvisorListPanel)
4. NNA mode + OFC → diverging bar chart: PASS (nna_ofc in ContinuousNnaDivergingView)
5. Continuous AUA + OFC → stacked area chart: PASS (data.ofc in ContinuousChartView)
6. TypeScript build clean: PASS (0 errors)
7. Zero new lint warnings: PASS (pre-existing warnings unchanged)
8. /frontend-dev visual test: PENDING — requires DT push to DEV + browser session
9. OFC donut center uses firm headline AUA: PASS (firmHeadlineAua override for OFC)

---

## PROFAU.003 QA Note

`capital_gains_ttm` and `cost_basis_by_year` confirmed in platinum/advisors/travis_penfield/summary.json
(D_02 commit b2e4e668). PROFAU.006 gate is CLEAR. DS may now issue PROFAU.006 GO when ready.

---

## Next Steps

- **[DT 0.4.0]** Deploy W6-004 + W3 + PROFAU .004 + .005 batch to portal PROD/DEV
- **[DE]** Run /frontend-dev visual test after DT deploy
- **PROFAU.006** (TaxCostBasisPanel L2): PROFAU.003 QA now confirmed clear — awaiting DS signal
- **PROFAU.007** (is_fee_paying): awaiting DS Q2 TO
