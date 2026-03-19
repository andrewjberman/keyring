# Assets Overview Mix View — Architecture Investigation — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-17
**Start Time:** N/A (investigation session)

## Objective

Andrew flagged two concerns with the Mix toggle in Assets Overview:
1. **Mathematical**: frontend logic slicing a monolithic JSON to track "new assets vs just the split" is incorrect
2. **Data engineering**: using a Lambda + monolithic JSON + frontend period aggregation is out-of-pattern; needs pre-computed portal views

---

## Work Completed

### 1. Full Data Flow Trace

**Current mix flow (Assets Overview, `auaSubMode === 'mix'`):**

```
06b_build_client_mix_timeseries.py (EC2)
  → gold/client_timeseries/{relationship_id}.json  (per-relationship, daily)
  → gold/client_timeseries/0.json  (firm-level aggregate — status unclear, see below)

opal-partners-data Lambda:
  GET /api/scoped/partners/books/relationship/0/mix-timeseries
  → serve_s3_json(bucket, 'gold/client_timeseries/0.json')
  → returns raw {mix: [{date, equity, fixed_income, structured_notes, cash, other}, ...]}

PartnerAnalytics.tsx:
  - getFirmMixTimeseries('bd') → 2000+ daily MixTimeseriesPoint[]
  - firmMixData useMemo → picks LAST point per period (monthly/quarterly/annually)
  - renders 100% stacked bar chart (percentages only, no dollar amounts)
```

### 2. Problem 1 — Dollar Amounts Missing from Raw Data

The `MixTimeseriesPoint` type only contains percentage values (0-1):
```typescript
interface MixTimeseriesPoint {
  date: string
  equity: number        // 0-1 pct
  fixed_income: number  // 0-1 pct
  structured_notes: number
  cash: number
  other: number
}
```

The `06b` gold script computes `market_value` per asset class internally (line 492:
`mix[ac] = round(float(mix_agg.get(ac, 0.0)) / total_mv, 6)`) but ONLY stores pct — the
dollar amounts are discarded at write time.

Result: the chart can only show 100% stacked bars. You cannot display "Equities: $1.02B (62%)" —
only "Equities: 62%". The split is visible but the dollar scale is invisible.

**Andrew's concern about "new assets vs just the split"** resolves to this: a percentage
mix chart (always sums to 100%) doesn't show absolute growth. When equity goes from 60% to
65%, it's impossible to tell if that's:
  a. New clients investing heavily in equity
  b. Market appreciation of existing equity positions
  c. Net rebalancing by existing clients

Without dollar amounts, the chart only shows composition drift, not absolute AUA movement.

### 3. Problem 2 — Firm-Level '0' Aggregate Does Not Appear to Be Explicitly Built

`06b` groups the positions_cube by `relationship_id` (from accounts_dimension). There is no
account with relationship_id='0' in the data — '0' is a synthetic key meaning "firm-level
aggregate." The script does NOT contain any explicit firm-level aggregation step.

Consequence: `gold/client_timeseries/0.json` either:
  a. Does not exist → Lambda returns 404 / empty → Mix tab shows "mix data unavailable"
  b. Was added manually or by a separate step not in 06b

Either way, the firm-level aggregate is not computed with the correct methodology:
correct firm-level mix requires summing market_value by asset_class across ALL relationships
for each date, then computing firm-level pcts. Averaging per-relationship pcts would be wrong
(equal-weighting $50M accounts with $5M accounts).

### 4. Problem 3 — Frontend Period Aggregation Is Out-of-Pattern

`firmMixData` useMemo (PartnerAnalytics.tsx lines 397-416):
- Downloads 2000+ daily data points (the full firm history)
- Groups by granularity-dependent period key (monthly/quarterly/annually)
- Takes the LAST daily point in each period as the end-of-period snapshot
- This is the entire period aggregation logic running in the browser

This violates the "DS logic always goes cloud-side" rule. Compare to the AUA data
(timeseries_chart.json `aua.quarterly/monthly/annually`): pre-aggregated by
`bd-portal-publisher` to three granularities, served directly. The frontend just picks
the right sub-key.

Additional performance issue: the full daily JSON for 2000+ dates is downloaded on every
Mix tab activation. For a firm with 5+ years of history this is a non-trivial payload
(~150KB per call). The frontend then discards all but N period end-dates (12-50 points).

### 5. The "New Assets vs Split" Clarification

Andrew's phrasing "which shouldn't change all that much period over period" is correct for
the **percentage mix** — a firm's asset class mix tends to be stable (62% equity, 24% FI is
unlikely to swing to 50%/40% in one quarter unless there's a large client event). The
frontend is currently doing complex aggregation to produce... a slowly-changing 100% bar.

The **dollar amount** version is far more informative: equity went from $980M to $1.02B this
quarter (+$40M). Of that, how much was market appreciation vs new equity inflows? That's
the GRO view's job. But the Mix view in dollar terms at least grounds the firm's total
exposure correctly.

---

## Diagnosis Summary

| Problem | Root Cause | Severity |
|---------|-----------|----------|
| No dollar amounts | `06b` writes pct only, discards market_value | High — missing required display info |
| Firm '0' aggregate may not exist | `06b` has no explicit firm aggregation logic | High — may be showing stale/empty data |
| Frontend period aggregation | `firmMixData` useMemo slices daily data client-side | Medium — out-of-pattern, fragile, wasteful |
| Percentage-only chart | 100% stacked bars can't show absolute scale | High — misses "both pct and dollar" requirement |

---

## Recommended Architecture

### Gold Layer Change (DS owns)

Extend `06b_build_client_mix_timeseries.py` to add a firm-level aggregation step:

After processing each date partition, maintain a `firm_daily_mix` dict:
  `{date_str: {equity: $, fixed_income: $, ..., total: $}}`

At the end of the build, compute period-level views (quarterly/monthly/annually) using the
LAST daily snapshot per period (consistent with the AUA timeseries pattern). Write to:
  `s3://opal-data-bd/gold/firm_mix_views.json`

**Output shape:**
```json
{
  "generated_at": "...",
  "data_as_of": "YYYY-MM-DD",
  "firm_id": "49financial",
  "views": {
    "quarterly": [
      {
        "period": "2024-Q4",
        "label": "Q4 '24",
        "end_date": "2024-12-31",
        "total_aua": 1620000000.0,
        "equity": {"value": 1004400000.0, "pct": 0.62},
        "fixed_income": {"value": 388800000.0, "pct": 0.24},
        "structured_notes": {"value": 97200000.0, "pct": 0.06},
        "cash": {"value": 81000000.0, "pct": 0.05},
        "other": {"value": 48600000.0, "pct": 0.03}
      },
      ...
    ],
    "monthly": [...],
    "annually": [...]
  }
}
```

This is the same pattern as `timeseries_chart.json aua.quarterly/monthly/annually` — pre-aggregated,
period-labeled, three granularities in one file.

### Lambda Change (DS writes, DT deploys)

Add a new endpoint to `opal-partners-data`:
  `GET /api/scoped/partners/books/firm/mix-views?firmId=xxx`
  → serve_s3_json(bucket, 'gold/firm_mix_views.json')

Pure passthrough. Zero computation in Lambda.

The existing `mix-timeseries` endpoint (daily per-relationship) stays for the Books tab
`MixTimeseriesPanel` (per-client view). The new `firm/mix-views` endpoint serves the
Assets Overview chart only.

### Frontend Change (DE/RD own)

Replace in `PartnerAnalytics.tsx`:
- Remove `getFirmMixTimeseries` call and `firmMixData` useMemo
- Add call to new `getFirmMixViews()` endpoint
- Read `data.views[granularity]` directly — no period aggregation logic in frontend
- Update tooltip to show dollar amount + percentage (not just percentage)
- Chart renders `value` (dollar) as bar height with `pct` in tooltip — OR keep 100% stacked
  but label tooltip with both "$1.02B (62%)"

Decision on chart type is a DE/RD call — either:
  a. Keep 100% stacked bars, enrich tooltip with dollar amounts
  b. Switch to absolute stacked bars (height = dollar amount, same colors)
  Option (b) is more informative for "what did the firm hold" but loses the clean pct-sum-to-100 visual.
  Option (a) is lower-risk and satisfies the "both pct and dollar" requirement.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Extend 06b for firm-level aggregate (not a separate script) | 06b already has all market_value data per date in memory. Adding firm aggregation is a natural extension of the same loop — no second pass needed. |
| Write period views from gold layer, not Lambda | Lambda should not aggregate. Gold runner is the correct place for period slicing. Consistent with bd-portal-publisher pattern. |
| New endpoint (firm/mix-views) separate from relationship/mix-timeseries | Different data shapes, different consumers. Keep per-relationship daily data separate from firm-level pre-aggregated views. |
| Include dollar amounts in gold output | Fixes "both pct and dollar" requirement. Market value is computed anyway inside 06b — no additional data joins needed. |

---

## Files to Touch

| File | Change | Owner |
|------|--------|-------|
| `data/black_diamond/scripts/gold/06b_build_client_mix_timeseries.py` | Add firm-level daily aggregation + period view computation + write to `gold/firm_mix_views.json` | DS |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` | Add `GET /api/scoped/partners/books/firm/mix-views` passthrough | DS |
| `portal/src/api/endpoints/advisor-intelligence.ts` | Add `getFirmMixViews()` function | DE/RD |
| `portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` | Replace firmMixRaw + firmMixData useMemo with getFirmMixViews call | DE/RD |
| `portal/src/pages/AdvisorIntelligence/types.ts` | Add `FirmMixViewsResponse` type | DE/RD |

---

## Blockers

None for DS scope (06b extension + Lambda endpoint). DE/RD frontend changes are unblocked
once the endpoint and gold output shape are confirmed.

---

## Current State

**Status:** COMPLETE (investigation only — no code written yet)
**Active branch:** `CLOUD`

Investigation complete. Three compounding problems identified:
  1. Dollar amounts stripped from gold output
  2. Firm-level '0' aggregate not explicitly built
  3. Frontend period aggregation is out-of-pattern

Recommended fix is an extension to `06b` + new Lambda passthrough endpoint + frontend
replacement of the `firmMixData` useMemo. Andrew needs to confirm the chart type direction
(100% stacked + rich tooltip vs absolute dollar stacked) before DE/RD can finalize the
frontend changes.

---

## Next Steps

1. **[Andrew] Confirm** chart type direction: (a) 100% stacked bars with dollar+pct tooltip, or (b) absolute dollar stacked bars showing total AUA scale
2. **[0.4.0_DS_ClientPlatform] Implement** 06b firm-level aggregation + period view output + Lambda endpoint
3. **[0.4.0_DT_ClientPlatform] Deploy** updated 06b to EC2, run gold layer, deploy Lambda
4. **[0.4.0_DE_ClientPlatform] / [0.4.2_RD_AdvisorIntelligence] Replace** firmMixData useMemo with getFirmMixViews call, update tooltip

**Do NOT:**
- Average per-relationship percentages to get firm-level mix (wrong: equal-weights all relationships regardless of size)
- Continue expanding the frontend useMemo to add dollar amounts (wrong direction: computation belongs cloud-side)
- Use the existing `mix-timeseries` endpoint for the firm-level Assets Overview chart (different shape/purpose from per-client MixTimeseriesPanel)
