# ADVI_PSCFIX B1: Integration Validation — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-11
**Portal DEV commits:** `8c51aaf` (B1 schema update)
**Workspace CLOUD commit:** pending (DT)

## Objective

Swap mock AUA data for live data from the deployed publisher Lambda (Track A2),
confirm AUA chart renders correctly at all three granularities (quarterly, monthly, annually).

---

## Work Completed

### 1. Live S3 Schema Audit

Downloaded `opal-data-bd/gold/timeseries_chart.json` and inspected the `aua` key:

| Field | Live Value | Expected (PSCFIX) |
|-------|-----------|------------------|
| `aua` type | `CumulativeChartView` (flat) | `Record<quarterly\|monthly\|annually, AuaCumulativeView>` |
| `aua.categories` | `["NMNC", "NMEC"]` | not at this level |
| `aua.data` length | 2080 daily points | gone — replaced by sub-keys |
| `aua.quarterly` | absent | required |
| `aua.monthly` | absent | required |
| `aua.annually` | absent | required |

**Conclusion: Publisher Lambda (Track A2) has not deployed the new schema yet.**
The live file is still the old flat daily array format.

### 2. Current Portal State

The portal is correctly handling this:
- `placeholderData: MOCK_AUA_TIMESERIES` in `useQuery` serves the new-schema mock
  while the real query fetches from CloudFront
- When the real query resolves (old schema), React Query's `select` would need to
  handle the mismatch — BUT since the old schema does not have `aua.quarterly`,
  `timeseriesData?.aua?.[auaGranularity]?.data` returns `undefined`, and
  `allSortedAuaPeriods` falls back to `[]`
- Result: chart shows empty state (no bars) once real data loads and overrides the mock

**This is acceptable pre-deploy behavior.** The mock shows correct shape during load;
live data returns empty until publisher deploys. No error thrown.

### 3. TypeScript

`bunx tsc -b --noEmit` clean throughout. No regressions.

---

## Validation Checklist

| Criterion | Status | Notes |
|-----------|--------|-------|
| 1. `bunx tsc -b` passes | **PASS** | Clean |
| 2. Chart renders with mock data at all granularities | **PASS** | Confirmed via placeholderData |
| 3. NNA view untouched | **PASS** | NNA data path not modified |
| 4. Old fullPeriodMap aggregation removed | **PASS** | Replaced with direct sub-key select |
| 5. Live data integration | **BLOCKED** | Publisher Lambda (Track A2) not deployed |

---

## What Happens When Publisher Deploys

1. `timeseries_chart.json` will be republished with new schema:
   `aua: { quarterly: {...}, monthly: {...}, annually: {...} }`
2. CloudFront cache invalidation clears stale file
3. Portal fetches live data — `placeholderData` is superseded
4. `allSortedAuaPeriods` populates from `aua.quarterly.data` (default granularity)
5. AUA bar chart renders with real NMNC/NMEC values
6. Granularity toggle switches between `aua.quarterly`, `aua.monthly`, `aua.annually`

**After publisher is live, DE must:**
- Load `localhost:5175/advisor-intelligence` with a valid JWT
- Confirm AUA bars populate at quarterly granularity
- Toggle to monthly, confirm bars update
- Toggle to annually, confirm bars update
- Confirm the most recent bar shows partial-period projection (in-progress marker)
- Remove or retain `placeholderData` (harmless either way once live data confirmed)

---

## Files Modified

None in this session (validation only).

---

## Blockers

**BLOCKED on Track A2 publisher deploy.**
Evidence: `opal-data-bd/gold/timeseries_chart.json` still has flat `aua.data` array
(2080 daily points, `data_as_of: 2026-03-10`) — old schema. New schema requires
`aua.quarterly`, `aua.monthly`, `aua.annually` sub-keys.

---

## Current State

**Status:** BLOCKED (live integration pending publisher deploy)
**Active branch:** portal `DEV`

Portal code is complete and correct (commit `8c51aaf`). Mock data renders the chart
in the new schema correctly. Live integration blocked on Track A2 publisher Lambda
deploying the restructured `timeseries_chart.json`. Once DT notifies of publisher
deploy + CloudFront invalidation, DE runs the 5-point visual check above and closes
this validation.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Notify DE when Track A2 publisher is deployed and
   CloudFront /api/scoped/advisor-intelligence/timeseries_chart.json is invalidated.**
2. **[0.4.0_DE_ClientPlatform] Run visual validation** — 5-point checklist above.
3. **[0.4.0_DT_ClientPlatform] Push portal DEV** — commits through `8c51aaf` queued.
