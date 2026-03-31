# ADVI_MVPLVL.010 Session Log -- L2 Composition, Mix Toggle, Projections, Quarterly Bar
**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-03-26
**Task Order:** ADVI_MVPLVL.010.de-l2-composition-rendering.md

---

## Commits (portal DEV)

| Commit | Summary |
|--------|---------|
| `865ab7d` | L2 composition error handling + Mix chart other-class merge |
| `5e921e6` | Wire Mix chart to Interval + Window toggles |
| `593c57d` | Add SHOW_PROJECTIONS flag to disable AUA/NNA projections |
| `a4f44a1` | L2 composition renders immediately from advisor book data |
| `a56fcf1` | Route L2 composition through CloudFront, not API Gateway |
| `decd651` | Exclude current quarter from quarterly metrics bar |

---

## WS1: L2 Advisor Composition (Asset Mix + Top Holdings)

### Root Cause

Two compounding failures prevented the advisor-level composition from rendering:

1. **API Gateway routing failure**: `getBooksAdvisorComposition` routed through API Gateway (`/api/scoped/partners/books/advisor/{id}/composition?firmId=...`) which failed silently -- likely an authorizer mismatch between API Gateway and CloudFront. The firm composition worked because its fallback used `clients_tab.json` portfolio data (populated). The advisor fallback used `book.json` asset_allocation data (empty `[]`).

2. **Empty synthesis fallback**: `book.json` has `portfolio_composition.asset_allocation: []` for all advisors. The synthesis fallback produced empty mix, rendering "No allocation data". Meanwhile, `composition.json` (from script 12) has rich data: 5 asset classes, 9 top holdings, $144M total market value for josh_henson.

### Fix

Rerouted `getBooksAdvisorComposition` through CloudFront (`/api/scoped/advisor-intelligence/advisors/{id}/composition.json?firm=bd`) -- the same behavior that already serves `book.json` reliably. The `composition.json` is a static S3 artifact in the same directory.

### Verification

- Confirmed via `aws s3 cp`: `josh_henson/composition.json` has `mix: [equity, other, fixed_income, alternatives, cash]`, `top_holdings: 9`, `total_market_value: $144,167,098.04`
- Confirmed via `aws s3 cp`: `josh_henson/book.json` has `portfolio_composition.asset_allocation: []`

---

## WS2: PartnerAnalytics Mix Toggle

### Issues Found

1. **Missing other-class data**: `firmMixChartData` mapped `pt.cash.value` alone to display `other`, dropping the actual `other` field from `firm_mix_views.json`. Script 06b outputs both `cash` and `other` as separate `{value, pct}` fields. Fixed by merging: `otherValue = pt.cash.value + (pt.other?.value ?? 0)`.

2. **Missing type field**: `FirmMixPeriodPoint` lacked `other?: FirmMixClassValue`. Added to match script 06b output.

3. **Window toggle not wired**: Mix chart showed all periods regardless of the 1Y/3Y/Max Window toggle. Fixed by filtering `pts` through `timeWindowCutoff` (same pattern as the Clients chart's `aggregatedAuaData`).

---

## WS3: AUA/NNA Projections Feature Flag

Added `SHOW_PROJECTIONS = false` flag in PartnerAnalytics (line 461). Gates the projection computation in `augmentedAuaData` and `augmentedNnaData` via early-return. All downstream rendering (tooltip projected values, dashed reference lines, Y-axis domain extension) naturally no-ops when projection fields are absent. Set to `true` to re-enable.

---

## WS4: Quarterly Metrics Bar -- Current Quarter Dedup

The quarterly bar showed the current incomplete quarter (Q1 '26) as the first historical point, duplicating the "Current AUA" card. Fixed by filtering out the current quarter period (`YYYY-Q#`) from the completed quarters list. Result: Current AUA -> Q4 '25 -> Q3 '25 -> Q2 '25. Bumped firm-level slice from `-4` to `-5` to ensure enough completed quarters for QoQ calculation.

---

## GLDRST Input: Quarterly Mix Views Should Be Pre-Computed at All Levels

**To:** 0.4.0_DS_ClientPlatform
**Context:** ADVI_GLDRST (gold layer restructure)

### Current State

The quarterly lookback bar (Current AUA -> Q4 '25 -> Q3 '25 -> Q2 '25) has three different data strategies depending on drill level. Two of three derive quarterly snapshots client-side from daily timeseries — this is fragile, wasteful, and inconsistent.

| Level | Source | Pre-computed? | Artifact |
|-------|--------|---------------|----------|
| N1 Firm | `firm_mix_views.json` | Yes | `gold/firm_mix_views.json` (script 06b) |
| L2 Advisor | `deriveQuarterlyFromTimeseries()` in browser | No | `gold/advisors/{id}/mix.json` EXISTS but is not wired; code tries to derive from `mix_timeseries.json` which doesn't exist (key mismatch) |
| L3 Relationship | `deriveQuarterlyFromTimeseries()` in browser | No | No quarterly artifact exists; derived from ~2000 daily data points (`gold/client_timeseries/{id}.json`) on every page load |

### Problems

1. **Inconsistent methodology.** N1 uses publisher-aggregated quarterly snapshots from positions_cube. L3 derives snapshots from daily mix percentages interpolated to quarter-end dates. These can diverge — the publisher picks exact quarter-end positions, the client-side derivation picks the nearest available daily data point.

2. **Fragile dependencies.** L2 fails entirely because script 06b writes `mix.json` but the Lambda reads `mix_timeseries.json` — a key naming mismatch that went undetected because the quarterly bar silently falls back to null.

3. **Wasteful computation.** L3 downloads the full daily timeseries (~2000 points per relationship) and runs `deriveQuarterlyFromTimeseries()` in the browser just to extract 4 quarter-end snapshots. This is ~50KB of JSON transferred and parsed for 4 numbers.

4. **No L4 (account) quarterly bar.** There is no account-level timeseries artifact at all.

### GLDRST Recommendation

All quarterly mix views should be pre-computed by the same script, from the same source table (positions_cube), using the same methodology, at all four levels:

```
gold/firm_mix_views.json                              # N1 — already exists
gold/advisors/{advisor_id}/mix_views.json             # L2 — needs creation or wire existing mix.json
gold/client_timeseries/{relationship_id}_views.json   # L3 — needs creation
gold/accounts/{account_id}/mix_views.json             # L4 — needs creation (future)
```

Each artifact should have the same schema:
```json
{
  "views": {
    "quarterly": [FirmMixPeriodPoint...],
    "monthly":   [FirmMixPeriodPoint...],
    "annually":  [FirmMixPeriodPoint...]
  }
}
```

This eliminates `deriveQuarterlyFromTimeseries()` entirely from the portal, ensures methodological consistency across drill levels, and reduces payload size by 10-50x for the quarterly bar use case.

### Immediate Fix (pre-GLDRST)

For L2: wire the existing `gold/advisors/{id}/mix.json` (already pre-computed by script 06b, 25KB, correct schema) to the quarterly bar via the advisor mix-views CloudFront endpoint. This is a portal-only change — no gold rerun needed.

For L3: no immediate fix without a new artifact. `deriveQuarterlyFromTimeseries()` continues to work (it's just suboptimal). Flag for GLDRST.

---

## Files Changed

| File | Changes |
|------|---------|
| `src/api/endpoints/advisor-intelligence.ts` | Rerouted getBooksAdvisorComposition to CloudFront path |
| `src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | L2 composition effect, QuarterlyMetricsBar current-Q filter, firm slice -5 |
| `src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` | SHOW_PROJECTIONS flag, Mix chart cash+other merge, Window filter |
| `src/pages/AdvisorIntelligence/types.ts` | Added other? to FirmMixPeriodPoint |
