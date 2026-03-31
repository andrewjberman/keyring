# Performance Optimization, Gap Analysis, and Account Quality Tiers -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-31
**Start Time:** 9:00 PM ET
**End Time:** 1:00 AM ET
**Project:** ADVI_PRICES (positions cube performance + AUA gap convergence + quality classification)

---

## Objective

Three workstreams in a single session:
1. Parallelize and optimize 02_build_positions_cube.py (was 20 min on 64-vCPU c6i.16xlarge)
2. Analyze and fix the remaining AUA gap between gold and silver
3. Design and implement an account quality tier system for downstream consumers

---

## Work Completed

### 1. Performance Optimization of 02_build_positions_cube.py

AE reported 02 taking 20 min on a 64-vCPU c6i.16xlarge with 128GB RAM, mostly idle cores.
Identified and fixed five sequential bottlenecks:

| Fix | Commit | What was slow | Resolution |
|-----|--------|---------------|------------|
| ProcessPoolExecutor for expand_pairs_to_daily | 395a23b0 | 300K pairs expanded single-threaded | Fork-based parallel, 60 workers |
| ThreadPoolExecutor fallback on Windows | 20bd7138 | Windows fell back to single-threaded | ThreadPool fallback (no single-threaded path) |
| Auto-scale workers to CPU count | dbcaae70 | All scripts hardcoded 32 workers | `max(cpu_count - 4, 4)` across 02, 03, 05, 05b, 06b, run_gold_layer.sh |
| Eliminate batch loop + parallel S3 writes | f41212aa | 500-account batch loop + serial S3 PUTs (designed for 32GB r6i.xlarge) | Single expand call + ThreadPool 64 S3 writes |
| Fix 300M-row strftime bottleneck | 465aac76 | `dt.strftime('%Y-%m-%d')` on 300M rows (element-wise Python) | Group by datetime64 column, strftime on ~1500 unique keys |
| Vectorize sell/buy injection | 5040f359 | `.apply(lambda)` on 200K rows, Python for-loops over accounts | Set operations, vectorized pandas ops, `drop_duplicates` |
| Carry signed_units from compute_unit_events | 597ea654 | Two full groupby().diff() passes to reconstruct signed_units | Return signed_units alongside cum_units, skip diff |

02 timing went from ~20 min to ~12-18 min with the parallel expansion, but the sequential
pre-expansion phases (injection, cumsum recompute) were still dominating. The vectorization
and signed_units carry-through fixes were committed but AE's latest run was 20 min, suggesting
the vectorization fix may not have been in the deployed code for the final run. Next run will confirm.

### 2. AUA Gap Analysis and Fixes

Starting point: v6 canonical prices fix from earlier session, net gap +$14.1M (+0.888%).

| Fix | Commit | Gap Impact | Mechanism |
|-----|--------|------------|-----------|
| Filter blank asset names | 3ba357c9 | -$4.95M | 4 rows with empty asset_name had millions of units at $1.00 |
| Par-valued instrument pricing | 3ba357c9 | ~$0 (confirmation) | Shield/Buffer/Delphi structured products at $1.00 x units = correct |
| Matured bond exclusion | c90de842 | -$4.5M | 50 positions, 45 matured bonds at face value, 29 accounts |

Gap progression:
- v6 start of session: +$14.1M (+0.888%)
- After blank names + par-valued: +$9.4M (+0.594%)
- After matured bonds: +$4.9M (+0.309%)

Remaining +$4.9M is stale positions (departed accounts + partial sells never delivered).
No logic fix available -- needs missing transaction data from BD.

### 3. Account Quality Tier System

Designed and implemented 05f_build_account_quality_tiers.py (commit cb7c38a0).
Classifies every account based on two dimensions:
- Transaction completeness: cube positions vs BD unrealized positions
- AUA accuracy: gold vs silver gap percentage

Tier definitions:
- A (Verified): 100% coverage, gap <= 0.5%
- B (High confidence): 100% coverage, gap <= 2%
- C (Injection-resolved): <=2 missing positions, gap <= 5%
- D (Partial): gap <= 50%
- F (Suspect): gap > 50%

Final distribution (with all fixes):

| Tier | Accounts | % Count | AUA | % AUA | Med Error | Avg Error |
|------|----------|---------|-----|-------|-----------|-----------|
| A | 3,369 | 56% | $819M | 52% | $0 | $105 |
| B | 215 | 4% | $122M | 8% | $1,174 | $5,272 |
| C | 923 | 15% | $267M | 17% | $2,242 | $7,392 |
| D | 1,436 | 24% | $368M | 23% | $6,140 | $22,274 |
| F | 116 | 2% | $11M | <1% | $26,517 | $185,366 |

A+B+C = 4,507 accounts (74%), $1.208B AUA (76%) -- position-level data trusted.
R-squared = 0.991 all accounts, 0.999 excluding tier F.

### 4. Tier F Root Cause Analysis

126 accounts decomposed into three patterns:

| Pattern | Accounts | Gap | Root Cause |
|---------|----------|-----|------------|
| Matured bonds at par | 44 | +$5.2M | FIXED (c90de842) -- reduced to $0.7M remaining |
| Departed accounts | 3 | +$2.4M | Silver near-zero, exit txns never delivered |
| Yahoo overshoot (stale positions) | 31 | +$16.7M | FIFO has too many units, partial sells missing |

### 5. Yang Model Weight Investigation

AE identified Yang model.pkl files (s3://opal-data-portal-v2/benchmarks/) as potential
buy injection improvement. Model weights provide target allocations per model (UST/ST/INT/LTC/LTA).
Could replace residual-based back-solve for model portfolio accounts (88 accounts in 13-15 position cluster).

Blocker: BD silver allocations have no account-to-model mapping (investment_strategy_name = "No Investment Strategy Defined" for all accounts). Need to infer model from holdings fingerprint.
Flagged for next iteration.

### 6. Coverage Analysis

- 6,059 accounts in gold (have transaction history)
- 408 accounts in silver but not in gold (no transactions)
  - 210 with positive MV totaling $4.2M (0.26% of AUA)
  - 169 with zero MV
  - 29 with negative MV totaling -$4.5M (margin/short/billing)
- Gold covers 100% of positive silver AUA

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Auto-scale workers to cpu_count - 4 | Hardcoded 32 wasted half of 64-vCPU machine. Floor of 4 for dev machines. |
| Eliminate batch loop in 02 | Batch loop was for 32GB r6i.xlarge memory. On 128GB it's pure overhead. |
| Par-valued patterns separate from cash patterns | Structured products carry market risk unlike cash; keeping distinct for auditability |
| Quality tiers not numerical scores | Categorical tiers map to trust decisions (trust positions vs trust totals vs silver-only) |
| No silver MV cap on gold | Caps hide errors from time series. Wrong is better than silently clamped. Tiers flag it. |
| Maturity year regex on asset name | Maturity = return of par capital. Unredeemed bonds are phantom positions. Per-partition exclusion preserves history. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `gold/02_build_positions_cube.py` | Parallelization, batch elimination, strftime fix, vectorized injection, signed_units carry, blank name filter, par-valued patterns, matured bond exclusion | Yes -- 395a23b0, 20bd7138, f41212aa, 465aac76, 5040f359, 597ea654, 3ba357c9, c90de842 |
| `gold/03_build_holdings_lots.py` | Auto-scale workers | Yes -- dbcaae70 |
| `gold/05_build_client_performance.py` | Auto-scale workers | Yes -- dbcaae70 |
| `gold/05b_build_account_performance.py` | Auto-scale workers | Yes -- dbcaae70 |
| `gold/05f_build_account_quality_tiers.py` | New script -- account quality classification | Yes -- cb7c38a0 |
| `gold/06b_build_client_mix_timeseries.py` | Auto-scale workers | Yes -- dbcaae70 |
| `gold/run_gold_layer.sh` | Auto-scale workers, 05f added to both modes, stale r6i.xlarge comment removed | Yes -- dbcaae70, cb7c38a0 |

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Net AUA gap at +$4.9M (+0.309%) after all fixes. 74% of accounts (76% of AUA) classified as
trusted (tiers A+B+C). Quality tier system deployed and producing parquet + JSON outputs on
each gold run.

02 performance optimization code is committed but final timing confirmation pending -- AE's
last run (20 min) may not have included the vectorization + signed_units fixes. Next run
should show improvement.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Confirm 02 timing** with all vectorization fixes deployed -- target < 10 min
2. **[0.4.0_DS_ClientPlatform] Yang model weight buy injection** -- infer account-to-model mapping from holdings fingerprint, use model weights to distribute rotation buys instead of residual back-solve
3. **[0.4.0_DS_ClientPlatform] Investigate tier D promotion** -- 1,436 accounts at 8% avg error. Many have only 1 missing position. Better injection accuracy (Yang weights, capital gains data) could promote to tier C.
4. **[0.4.0_DS_ClientPlatform] Capital gains maturity/called data** -- check if BD's capital gains report contains maturity and called events that could feed the sell injection for bonds
5. **[Andrew] BD holdings report with units** -- if available, closes the buy-side unit gap entirely

**Do NOT:**
- Apply silver MV caps to gold -- time series integrity matters more than hiding errors
- Re-enable ghost suppression -- injection replaces it with data-driven approach
- Use Yahoo historical_prices for gold MV estimation -- canonical_prices is the only valid source
