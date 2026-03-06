# NNAVAR Timing Shift Diagnostic EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 20:35
**End Time:** 20:42

---

## Objective

Execute both suites of `diag_nnavar_timing_shift.py` (Phase 3b) on EC2
`i-01003b035d2988dfb`. Determine whether the BD→Schwab TOA timing mismatch is a
FIXED day offset (correctable by a date rule) or VARIABLE (event-driven, requires
Schwab TOA data feed).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | git pull CLOUD | Already up-to-date at `3d0b6a82` |
| 2 | Upload script | `s3://opal-data-bd/scripts/diagnostics/diag_nnavar_timing_shift.py` (24.1 KB) |
| 3 | Suite: monthly_lag (first attempt) | CMD `cb3f793d` — FAIL: `ValueError: Unknown format code 'd' for object of type 'float'` at line 329 — all 9 lags computed before crash |
| 4 | Fix lag_months format | `1094bb17` — `int(df.iloc[0]['lag_months'])` cast |
| 5 | Re-upload fixed script | `s3://opal-data-bd/scripts/diagnostics/diag_nnavar_timing_shift.py` |
| 6 | Suite: monthly_lag (fixed) | CMD `796a647d` — SUCCESS, <1s |
| 7 | Suite: day_shift | CMD `76241274` — SUCCESS, 9s |
| 8 | Push fix commit | `1094bb17` pushed to CLOUD |

---

## Suite 1: monthly_lag Results

| lag | direction | pearson_r | sign_agr | total_gap |
|-----|-----------|-----------|----------|-----------|
| -4 | behind | 0.054 | 13/13 | -$78.1M |
| **-3** | **behind** | **0.418** | **12/13** | **-$96.9M** |
| -2 | behind | -0.138 | 12/13 | -$87.6M |
| -1 | behind | 0.293 | 11/13 | -$114.9M |
| +0 | neutral *(prod)* | 0.175 | 10/13 | -$119.8M |
| +1 | ahead | -0.058 | 9/13 | -$144.1M |
| +2 | ahead | 0.203 | 8/13 | -$175.3M |
| +3 | ahead | 0.284 | 8/13 | -$168.0M |
| +4 | ahead | -0.582 | 8/13 | -$123.8M |

**Best lag: -3 months (pearson=0.418).** Our NNA leads Schwab by approximately 3 months.
Peak is NOT at L=0 → coarse offset confirmed. Day sweep required (and completed).

S3: `s3://opal-data-bd/diagnostics/nnavar_timing/20260306/monthly_lag/`

---

## Suite 2: day_shift Results

**Best transfer_only shift:** N=-22d, pearson=0.360, gap=-$121.2M
**Best all_flows shift:**     N=-6d,  pearson=0.302, gap=-$115.6M

### Per-month optimal offset matrix

| month | optimal_N_days | gap_at_N0 | gap_at_optimal |
|-------|----------------|-----------|----------------|
| 2024-05 | -24 | -$22.2M | +$10.4M |
| 2024-06 | -11 | -$11.8M | +$0.1M |
| 2024-07 | -2 | +$0.6M | +$0.1M |
| 2024-08 | +23 | -$23.1M | -$13.9M |
| 2024-09 | -4 | -$18.9M | -$18.0M |
| 2024-10 | +27 | -$20.9M | -$11.0M |
| 2024-11 | -20 | -$3.9M | -$0.04M |
| 2024-12 | -29 | -$33.4M | -$4.1M |
| 2025-01 | +19 | +$40.8M | +$7.9M |
| 2025-02 | -24 | +$12.8M | +$0.6M |
| 2025-03 | +20 | -$10.8M | +$0.2M |
| 2025-04 | +29 | -$41.1M | -$33.4M |
| 2025-05 | +30 | +$12.2M | +$4.7M |

### Offset Consistency Verdict

```json
{
  "mean_optimal_offset_days": 2.6,
  "median_optimal_offset_days": -2.0,
  "std_optimal_offset_days": 21.8,
  "min_optimal_offset_days": -29,
  "max_optimal_offset_days": 30,
  "interpretation": "VARIABLE TIMING -- high variance, not correctable by a fixed offset rule"
}
```

**std=21.8d >> 5d threshold → VARIABLE TIMING.**

S3: `s3://opal-data-bd/diagnostics/nnavar_timing/20260306/day_shift/`

---

## Script Bug Fixed (DT-authorized)

| Commit | File | Bug | Fix |
|--------|------|-----|-----|
| `1094bb17` | `diag_nnavar_timing_shift.py:329` | `{df.iloc[0]['lag_months']:+d}` — float formatting fails | `{int(df.iloc[0]['lag_months']):+d}` |

---

## Key Findings

1. **VARIABLE TIMING confirmed.** std=21.8d across 13 months (range: -29d to +30d).
   The DS decision framework is clear: a fixed date-offset rule on Transfer In/Out
   transactions would NOT solve the NNA gap. The timing is event-driven.

2. **Coarse offset is ~3 months.** monthly_lag peaks at L=-3 (pearson=0.418).
   Our Transfer flows are recorded ~3 months before Schwab recognizes them —
   consistent with complex ACAT settlement timing varying by transfer type/custodian.

3. **Within ±30 days, best achievable is pearson=0.360** (transfer_only, N=-22d).
   No sub-monthly fixed rule gets close to the PRD target (0.50).

4. **Production fix path requires Schwab TOA event dates.** Without the actual
   Schwab record dates for TOA transactions, there is no implementable code fix.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Fix format bug and re-run rather than extract from stdout | summary.csv needed for DS; data was correct but not uploaded |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_nnavar_timing_shift.py` | Fix float format code at line 329 | Yes — `1094bb17` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Both timing suites complete. Definitive verdict: VARIABLE TIMING (std=21.8d). No
production code fix available via date offset. Schwab TOA event dates required for
any further fix. DS/COO to determine Phase 4 scope.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Interpret VARIABLE TIMING verdict** — std=21.8d means
   ACAT settlement timing varies too widely by event to apply a fixed offset.
   The 3-month coarse lag means BD posts TOA flows months before Schwab reconciles them.

2. **[COO/DS] Go/no-go on Schwab TOA data feed request** — The only production path
   to improve pearson is obtaining Schwab's actual TOA recognition dates.

3. **[COO] PRD target reassessment** — Across all phases, ceiling without Schwab data
   is pearson=0.418 (monthly lag shift) or 0.386 (no Transfers). PRD target of 0.50
   is not reachable with available data.

**Do NOT:**
- Implement any date offset rule on Transfer In/Out in production
- Pursue further diagnostic suites without DS/COO direction
