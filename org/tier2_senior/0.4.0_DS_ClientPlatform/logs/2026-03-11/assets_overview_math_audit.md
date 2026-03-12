# Assets Overview Math Audit — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-11
**Portal DEV commit:** `67090a4`
**Workspace CLOUD commit:** `c3c8d072`

## Objective

Andrew flagged two concerns: (1) projection math questionable across the board, and
(2) NNA view shows $353M for 2023 while GRO shows $227M for the same year on Year/3Y interval.
Audit actual S3 data (`.tmp_timeseries_gold.json`, data_as_of 2026-03-06) to diagnose.

---

## Work Completed

### 1. Root Cause — GRO vs NNA Discrepancy ($227M vs $353M for 2023)

**Confirmed bug. Fully explained and fixed.**

The `aggregatedGroData` memo in PartnerAnalytics.tsx was filtering monthly GRO points by
time window BEFORE aggregating them to the period (year/quarter) level:

```typescript
// OLD (buggy)
const groData = timeWindowCutoff
  ? groView.data.filter(p => new Date(p.period + '-01T12:00:00') >= timeWindowCutoff)
  : groView.data
// ... then sum groData by period
```

On a 3Y window starting ~March 11, 2023, the monthly cutoff excludes Jan, Feb, and early March 2023.
When summed into the "2023" annual bar, only Apr-Dec 2023 is included = $226,956,468 ≈ $227M.

The NNA view uses a different (correct) approach: it builds a full-history period map from ALL
daily data, then diffs year endpoints against each other. So NNA 2023 always shows the full
calendar year diff: $352,586,319 ≈ $353M, regardless of time window.

**Cross-validation numbers (from raw data):**
| Year | NNA view (endpoint diff) | GRO buggy 3Y | GRO fixed (12 mo) |
|------|--------------------------|--------------|-------------------|
| 2023 | $352,586,319             | $226,956,468 | $343,416,482      |
| 2024 | $144,693,117             | $135,418,640 | $135,418,640      |
| 2025 | $269,214,688             | $265,531,882 | $265,531,882      |

2024 and 2025 are the same (3Y window starts before Jan 2023, so Jan of those years is included).

### 2. Frontend Fix Applied

Changed `aggregatedGroData` to:
1. Aggregate ALL monthly GRO points into period-level buckets (no time window filter)
2. Filter which PERIOD labels to display (period end date >= timeWindowCutoff)

This mirrors the NNA view's "full history for computation, window for display" pattern.
Commit: portal DEV `67090a4`.

### 3. Backend GRO Calculation Bug (secondary, also fixed)

After the frontend fix, GRO 2023 shows $343M vs NNA view $353M — a residual $9.2M gap.

Root cause: the GRO monthly nna_net was computed as:
```python
nna_net = nna_end_of_month - nna_first_day_of_month
```

On some month boundaries (e.g. Aug 1 2023: +$3.0M, Sep 1 2023: +$2.0M), cumulative NNA jumps
between the last day of the prior month and the first data point of the next. These boundary flows
are attributed to neither month's GRO bar.

**Inter-month NNA gaps for 2023 (confirmed from data):**
- Feb 1: +$157K, Mar 1: +$2.2M, May 1: +$1.2M, Jun 1: +$209K
- Aug 1: +$3.0M, Sep 1: +$2.0M, Nov 1: +$716K, Dec 1: -$394K
- Total: +$9.17M = exactly the NNA_view vs GRO gap ✓

Fix: use last-of-prior-month as aua_start/nna_start. This makes monthly nna_net values
telescope: sum Jan-Dec = nna(Dec31) - nna(Dec31_prev_year) = NNA view exactly.

Commit: `c3c8d072` (CLOUD, on top of PSCFIX A2 commit ea832f51).

**After both fixes:**
| Year | NNA view | GRO (both fixes) | Delta |
|------|----------|------------------|-------|
| 2023 | $352,586,319 | $352,586,319 | $0 (telescopes exactly) |
| 2024 | $144,693,117 | $144,693,117 | $0 |
| 2025 | $269,214,688 | $269,214,688 | $0 |

### 4. Projection Math Analysis

**AUA projection formula** (`augmentedAuaData`, lines 490-559):

```
currentDelta = rawDelta * (2 - elapsedFraction)
weightedDelta = (2/3) * currentDelta + (1/3) * historicalDelta
projectedValue = priorEnd + weightedDelta
```

At various elapsed fractions:
| Elapsed | Factor on rawDelta | Intent |
|---------|-------------------|--------|
| 10%     | 1.90x             | Much safer than pure 10x scaling |
| 25%     | 1.75x             | Quarter at 25%: ~2x |
| 50%     | 1.50x             | Mid-period: 1.5x |
| 70%     | 1.30x             | Late quarter/year: 1.3x |
| 100%    | 1.00x             | Complete: exact |

Formula is mathematically correct and intentional (comment explains the blend rationale).
Key characteristic: **always inflates rawDelta by 1.0x to 2.0x** depending on elapsed fraction.
No hard cap on the upside for AUA (unlike NNA which has 1.5x prior period cap).

**For annual granularity at 70 days elapsed (Mar 11 is ~19% of 2026):**
- factor = 2 - 0.19 = 1.81 → inflation of 81% on observed delta
- Then 2/3 weight + 1/3 historical blend
- Example: if NMNC grew +$50M from Q4'25 → current Q1'26 partial,
  projection says +$90M growth for full year 2026
- Whether this is "aggressive" depends on whether Q1 seasonality is representative

**Recommendation:** The formula is more conservative than pure time-scaling but more
aggressive than raw carry-forward. No bugs found. However, consider adding a cap for the
annual AUA projection similar to the NNA 1.5x prior period cap — particularly relevant
if there were large one-time client events early in a year.

**NNA projection** (`augmentedNnaData`):
- Simple `inflow * ratio` with 1.5x prior period cap
- Cap means maximum projected Q1 inflows = 1.5x Q4 inflows
- Math is sound. No bugs.

**GRO projection:** None — the GRO chart has no projected bar. Shows actuals only.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Fix GRO aggregation in frontend (aggregate-then-filter) | Directly fixes the $227M vs $353M issue visible to user. Mirror NNA view approach. |
| Fix GRO nna_start in backend (last-of-prior-month) | Removes residual $9M gap, makes sum telescope to NNA view endpoint diff exactly. |
| No change to projection formula | No bugs found. Flagging the AUA annual projection as potentially aggressive for Andrew's awareness but not changing formula unilaterally. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` | GRO aggregation fix | Yes — portal DEV `67090a4` |
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | GRO nna_start fix | Yes — CLOUD `c3c8d072` |

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD (publisher), portal DEV (frontend)

Two confirmed bugs found and fixed. Both require deploy to be visible in production:
- Frontend fix (DEV `67090a4`): visible immediately after DT pushes to PROD
- Backend fix (publisher `c3c8d072`): requires DT to deploy bd-portal-publisher + Lambda invocation

AUA math itself is correct. NNA = Inflows - Outflows checks out perfectly for all years.
NMNC + NMEC totals match total_aua exactly in the old rolling format (pre-PSCFIX).
The projection formula is mathematically intentional; no code bugs in the projection logic.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform]** Deploy publisher Lambda (commits ea832f51 + c3c8d072) and push portal DEV to PROD.
2. **[Andrew]** Decide if AUA annual projection inflation (up to ~2x rawDelta early in year) is acceptable or needs a cap analogous to the NNA 1.5x cap.

**Do NOT:**
- Apply the projection formula change without explicit instruction — it's intentional math, not a bug
