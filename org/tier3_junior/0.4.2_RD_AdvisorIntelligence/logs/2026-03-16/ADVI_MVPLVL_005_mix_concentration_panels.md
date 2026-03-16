# ADVI_MVPLVL-005 Mix + Concentration Panels — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-03-16
**Portal DEV commit:** `458c9dc`
**Task Order:** `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_MVPLVL.005.mix-concentration-charts.md`
**Thread:** `org/threads/ADVI_MVPLVL-005-addendum-a-mix-timeseries-alignment/`

## Objective

Wire MixTimeseriesPanel and ConcentrationPanel into Books Tab L3 (relationship detail view).
100% stacked area charts using Recharts, linked via asset class click filtering, independent
1Y/3Y/Max window toggle. Mock data skeleton until Lambda endpoints are deployed.

---

## Work Completed

### 1. TypeScript Interfaces (types.ts)

Added 6 new types at the end of `portal/src/pages/AdvisorIntelligence/types.ts`:

| Type | Purpose |
|------|---------|
| `MixAssetClass` | Union: `'equity' | 'fixed_income' | 'structured_notes' | 'cash' | 'other'` |
| `MixTimeseriesPoint` | Daily row: `{date, equity, fixed_income, structured_notes, cash, other}` (0-1 pcts) |
| `ConcentrationPoint` | Per-holding row: `{date, asset_name, ticker: string|null, asset_class, market_value, pct}` |
| `ConcentrationResponse` | Wrapper: `{relationship_id, top_n, data: ConcentrationPoint[]}` |
| `MixWindow` | `'1Y' | '3Y' | 'Max'` |

### 2. API Client Functions (advisor-intelligence.ts)

Added two new functions with proper query param construction:

- `getMixTimeseries(relationshipId, firmId, window?)` -> `MixTimeseriesPoint[]`
  - Endpoint: `/api/scoped/partners/books/relationship/${relationshipId}/mix-timeseries`
- `getConcentrationTimeseries(relationshipId, firmId, window?)` -> `ConcentrationResponse`
  - Endpoint: `/api/scoped/partners/books/relationship/${relationshipId}/concentration-timeseries`

Both follow the existing `apiRequest<T>` pattern. Window and firmId passed as query params.
Uses `URLSearchParams` for clean param construction.

### 3. MixTimeseriesPanel.tsx (new)

100% stacked area chart with 5 asset class series. Key implementation details:

| Feature | Implementation |
|---------|---------------|
| Chart type | Recharts `AreaChart` with `stackId="mix"` on all 5 `<Area>` components |
| Color mapping | Semantic tokens: `--primary` (equity), `--success` (fixed_income), `--warning` (structured_notes), `rgba(255,255,255,0.35)` (cash), `--danger` (other) |
| Window toggle | Local state `useState<MixWindow>('1Y')`, button group in PanelHeader actions |
| Click-to-filter | `onClick` on each Area toggles `selectedAssetClass` (same class = deselect) |
| Opacity dimming | Non-selected classes render at `fillOpacity={0.3}`, `strokeOpacity={0.3}` |
| Mock data | 90 daily points with gradual allocation drift for skeleton rendering |
| Data fetching | `useEffect` on `[relationshipId, firmId, window]` triggers `getMixTimeseries()` |

Props: `relationshipId`, `firmId`, `selectedAssetClass`, `onSelectAssetClass` — state is lifted
to L3ClientDetail for linkage with ConcentrationPanel.

### 4. ConcentrationPanel.tsx (new)

Top-N holdings over time, filtered by `selectedAssetClass` when set.

| Feature | Implementation |
|---------|---------------|
| Chart type | Recharts `AreaChart` with `stackId="conc"` per holding |
| Data pivot | Flat `ConcentrationPoint[]` pivoted to `{date, [asset_name]: market_value}` rows |
| Null ticker | `holdingLabel()` returns `name` only when `ticker === null`, `name (ticker)` otherwise |
| Header | `"Top {top_n} Holdings"` — dynamic from response `top_n` field |
| Asset class filter | When `selectedAssetClass` is set, `data.filter(p => p.asset_class === cls)` |
| Empty state | Shows "No holdings for selected filter" when filtered data is empty |
| Mock data | 5 holdings across 30 dates for skeleton rendering |

### 5. Wiring into L3ClientDetail (ClientsTab.tsx)

- Added `clientKey` and `firmId` to `L3ClientDetailProps` interface
- Added `selectedAssetClass` local state (linked between Mix and Concentration)
- Inserted `MixTimeseriesPanel` and `ConcentrationPanel` after Accounts Table, before L4 drill
- Caller passes `selectedClientKey` as `clientKey` and `firmOverride || firmId` as `firmId`
- Imported `MixAssetClass` type and both panel components

### 6. Barrel Export (panels/index.ts)

Added `MixTimeseriesPanel` and `ConcentrationPanel` exports.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Panels in L3ClientDetail (ClientsTab.tsx), not ClientDetailPage.tsx | The active L3 view is inside `BooksTab` — `ClientDetailPage` is a standalone page with different data flow. Thread contract says "Books Tab L3". |
| `selectedAssetClass` state lifted to L3ClientDetail | Required for Mix-to-Concentration linkage — both panels need to share this state |
| ConcentrationPanel receives `window` as prop (not own state) | Thread contract: "independent 1Y/3Y/Max" refers to Mix panel's toggle. Concentration follows Mix's window for coherent UX. |
| Mock data in both panels | Lambda dependency (`ADVI_MVPLVL.005.lambda-deploy`) is pending. Constraint allows skeleton state. |
| `firmOverride || firmId` passed to panels | Follows existing pattern in BooksTab where firmOverride takes precedence for internal users |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/types.ts` | Add MixAssetClass, MixTimeseriesPoint, ConcentrationPoint, ConcentrationResponse, MixWindow types | Yes -- portal DEV `458c9dc` |
| `portal/src/api/endpoints/advisor-intelligence.ts` | Add getMixTimeseries(), getConcentrationTimeseries() + import new types | Yes -- portal DEV `458c9dc` |
| `portal/src/pages/AdvisorIntelligence/ClientDetail/panels/MixTimeseriesPanel.tsx` | New file — 100% stacked area chart with window toggle + click filter | Yes -- portal DEV `458c9dc` |
| `portal/src/pages/AdvisorIntelligence/ClientDetail/panels/ConcentrationPanel.tsx` | New file — top-N holdings chart with asset class filtering | Yes -- portal DEV `458c9dc` |
| `portal/src/pages/AdvisorIntelligence/ClientDetail/panels/index.ts` | Add barrel exports for both new panels | Yes -- portal DEV `458c9dc` |
| `portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | Wire panels into L3ClientDetail, add clientKey/firmId props, add imports | Yes -- portal DEV `458c9dc` |

---

## Blockers

None. Lambda endpoints not yet deployed, but panels render with mock data per constraint.

---

## Current State

**Status:** COMPLETE (pending commit + push)
**Active branch:** portal `DEV`
**TypeScript:** `bunx tsc -b --noEmit` — zero errors

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push portal DEV** — 6 files (2 new, 4 modified) pending commit and push. DT QA gate.
2. **[0.4.0_DT_ClientPlatform] Lambda deploy** — task order `ADVI_MVPLVL.005.lambda-deploy` must complete before live data flows.
3. **[0.6.0_AE_PartnerETL] EC2 gold script deploy** — `06b_build_client_mix_timeseries.py` must be deployed for gold artifacts.
4. **[0.4.2_RD_AdvisorIntelligence] Post-deploy** — remove mock data, verify live endpoint renders, confirm pct sum validation.

**Do NOT:**
- Modify L4 (account detail) views — out of scope per requirement #6
- Introduce ApexCharts — Recharts only per constraint
- Add granularity toggle — daily data rendered directly per thread contract
