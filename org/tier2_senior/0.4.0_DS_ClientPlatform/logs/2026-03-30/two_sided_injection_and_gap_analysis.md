# Two-Sided Injection and AUA Gap Analysis -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-30
**Start Time:** 10:00 AM ET
**Project:** ADVI_PRICES (phantom closure + missing buy injection + gap convergence)

---

## Objective

Implement and validate a two-sided position injection in `02_build_positions_cube.py`:
sell injection closes phantom positions using BD realized data, buy injection restores
missing rotation buys using BD unrealized + residual back-solve. Goal: bring gold AUA
into alignment with silver AUA.

---

## Work Completed

### 1. Realized Parquet Compaction

Previous gold run OOM'd loading 1,198 daily `silver/realized/` parquets (892K rows)
into memory alongside 3.7M-row transaction history on r6i.xlarge (32GB).

Created `compact-realized.py` (one-time backfill tool):
- Compacted 1,198 files into `bd_realized_agg.parquet` (199,853 pre-aggregated pairs, <1MB)
- Also wrote `bd_realized_compact.parquet` (full lot-level, 892K rows) for diagnostics
- Updated `02_build_positions_cube.py` to read single agg file instead of listing/streaming 1,198 keys
- OOM resolved. AE confirmed successful gold run after fix.

Steady-state pipeline: 0.7.0_AE_CloudOps deployed daily realized + unrealized BD runners
(bd-v2.20.0). Weekday automation via EventBridge. Compaction is backfill-only tooling.

### 2. CTO HOLD Resolution

CTO issued HOLD with 4 questions on the sell injection. Answered:
- Q1 (sell quantity without units column): realized report provides WHICH positions closed and WHEN;
  sell quantity comes from our own transaction-derived cumulative units, not from the realized report
- Q2-Q4: Andrew clarified not relevant; ghost suppression stays OFF to get clean injection signal

HOLD cleared. CTO approved the injection logic.

### 3. Sell-Only Gold Run (v2)

05e results: Gold $1,276M vs Silver $1,595M. Net gap: **-$319M (-20.0%)**. Injection correctly
closed 54,634 phantom positions but exposed that we were also missing the replacement buys.
The phantoms had been accidentally compensating for missing buys (Opal onboarding rotation:
old model sold, new model bought, neither transaction delivered).

### 4. Missing Buy Investigation

Identified 4,623 (account, asset) pairs in BD's unrealized report with zero transaction history.
58.2% of these accounts also have phantom sells -- confirmed rotation pattern. Top buy assets:
VUG (602 accts), SPYM (464 accts), DIVZ, IEMG -- all current Opal model ETFs.

BD reports (allocations, realized, unrealized) do not include per-position unit counts.
The only unit source is our transaction feed, which is the incomplete source we're trying to fill.

### 5. Buy Injection Implementation (v3)

Back-solve approach for missing buys:
1. Load unrealized report (position existence authority)
2. Find (account, asset) pairs in unrealized but NOT in unit_events
3. Per-account: residual = silver_mv - gold_mv (estimated from cube units x price)
4. Distribute residual across missing assets weighted by current price
5. units = allocated_mv / price

v3 05e results: Gold $1,484M vs Silver $1,595M. Net gap: **-$111M (-6.97%)**. Recovered $208M
of the $319M sell-only gap. 175 accounts >50% off (was 973). 58.3% within 10% (was 28.7%).

### 6. Top-Decile Analysis and Targeted Fixes

**Overshoot analysis ($70M, 1,460 accounts):**
- Top decile = 87% of overshoot ($61M in 146 accounts)
- Root cause #1: CASH priced at $87.97 via Yahoo instead of $1.00 ($33M)
- Root cause #2: Money market sweep funds (SCHWAB FAMILY FD) not in unrealized or realized ($3-5M)
- Root cause #3: POLEN/OPAL name mismatch -- realized aliased to OPAL, unrealized has POLEN (3,181 pairs)

**Undershoot analysis ($84M, 4,031 accounts):**
- Top decile = 73.5% of undershoot ($78M in 403 accounts)
- Root cause: unpriced positions in the buy injection's gold MV estimation
- 2,055 positions had no Yahoo ticker resolution in my analysis (but see Finding #8 below)

Fixes committed:
- CASH + money market sweep funds forced to $1.00 (pattern match on SCHWAB/MONEY/MMKT/SWEEP)
- POLEN/OPAL name alias normalization in sell injection
- 56 new YF_OVERRIDES for BD long-name equities (PG, CVX, NFLX, WFC, JPM, etc.)
- Dot-to-dash ticker conversion (BRK.B -> BRK-B)
- Null guard for None asset_name in unrealized data

### 7. v5 Results -- Overshoot Explosion

05e results: Gold $1,771M vs Silver $1,586M. Net gap: **+$185M (+11.6%)**. Undershoots
collapsed ($84M -> $21M) but overshoots exploded ($70M -> $205M).

Confirmed the 20% silver override in script 05 was NOT masking results (identical with it off).
The overshoot is entirely from the positions cube -- buy injection over-injecting units.

### 8. Root Cause Discovery: Pricing Mismatch in Buy Injection

**Critical finding:** The 2,055 "unpriced" positions were never actually unpriced. Canonical
prices already had Yahoo prices for PROCTER AND GAMBLE CO COM, CHEVRON CORP NEW COM, etc.
via name-based resolution. My analysis incorrectly used Yahoo historical_prices (ticker-keyed)
and treated "no ticker resolution" as "no price." The canonical prices pipeline resolves by
asset name, not ticker.

**The real problem:** Buy injection used Yahoo historical_prices to estimate gold_acct_mv,
but script 05 uses canonical_prices. Massive divergences:
- CASH: canonical $1.00 vs Yahoo $87.97 ($13.5B total difference across 5,908 positions)
- BMC SOFTWARE: canonical $1.00 vs Yahoo $26,500 ($883M on 1 position)
- 4,632 positions have canonical prices but NO Yahoo price ($201M invisible to Yahoo estimator)

Fix committed (v6, b695e7bc): switched buy injection to canonical_prices (same source as
downstream gold scripts). Prices keyed by asset_name -- eliminates ticker resolution entirely.

### 9. Pipeline Architecture Insight

Traced the full pipeline script-by-script:
- PRE-STEP: build_canonical_prices_v2 -> inject_scoped_overrides (builds canonical_prices)
- 02: builds positions_cube (units only, no prices)
- 05: joins cube x canonical_prices -> market_value = units x price -> AUA
- 05 also has silver AUA override (20% threshold) and bond detection (50% threshold)

Key insight: script 02 outputs ONLY units. The buy injection needs prices to SIZE units,
but downstream script 05 VALUES those units with canonical_prices. Any pricing mismatch
between the buy injection's estimator and canonical_prices causes over/under-injection.

Optimization: for testing, only need to rerun the scripts whose inputs changed:
- Canonical prices changes -> rerun canonical_prices only
- Injection logic changes -> rerun 02 only
- Pricing/override settings -> rerun 05 only
Reduced iteration from 57-minute full runs to targeted 5-minute reruns.

### 10. Lot-Level Matching Analysis

Matched BD's unrealized lots against our FIFO-derived holdings_lots (script 03) at
(account_id, asset_name, open_date, unit_cost) level:

| Category | Lots | Meaning |
|----------|------|---------|
| Matched | 199,058 | Confirmed real, correctly tracked |
| Unrealized-only | 191,882 | BD has, we don't -- phantom buys |
| Lots-only | 184,891 | We have, BD doesn't -- phantoms ($1.1B MV) |

(Account, asset) pair breakdown:
- Fully matched: 40,242 pairs (no injection needed)
- Partially matched: 27,496 pairs (some lots match, some don't)
- Fully unmatched: 18,084 pairs (zero lots match)

The lot-level match is precise for identifying WHICH lots are phantom (lots-only has exact
current_units from FIFO). However, for missing buys (unrealized-only), the unrealized report
still has no units column. Lot counts and matched-lot-unit-averages were considered as proxies
but rejected -- no basis for assuming unmatched lots are similar size to matched ones.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Compaction over daily partition reads | 1 file <1MB vs 1,198 S3 GETs. Steady-state pipeline will maintain the agg file. |
| Ghost suppression OFF | Andrew: need clean signal from injection, suppression would mask results |
| Two-sided injection (sell + buy) | Sell-only exposed $319M gap from missing rotation buys |
| Back-solve units from account residual | BD reports lack per-position units. Only method available without new BD data. |
| Switch to canonical_prices in buy injection | Yahoo pricing mismatch caused $135M overshoot explosion in v5 |
| CASH/money market forced to $1.00 | Yahoo returns $87.97 for CASH ticker. $13.5B aggregate mispricing. |
| Rejected lot-count-based unit inference | No basis for assuming unmatched lots match size of matched lots |
| Script-targeted testing over full gold runs | 02+05+05e in ~15 min vs 57 min full pipeline |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `gold/02_build_positions_cube.py` | Compaction fix, sell injection name alias, buy injection, CASH/$1.00 override, canonical prices switch, null guard | Yes -- 22021405, 9971820d, 2c302e9c, 42439b66, 77a7ccfb, b695e7bc |
| `silver/compact-realized.py` | New: one-time backfill compaction tool | Yes -- 6329993d |
| `silver/lib/ticker_overrides.py` | 56 new YF_OVERRIDES + 5 dead tickers | Yes -- 42439b66 |

---

## Current State

**Status:** IN PROGRESS
**Active branch:** `CLOUD`

v6 fix (canonical prices in buy injection) committed but not yet tested on EC2. AE has been
instructed to run 02 + 05 (override off) + 05e only. This tests whether using canonical prices
eliminates the pricing mismatch that caused the v5 overshoot explosion.

The buy injection is fundamentally an estimate -- it trades variance on value for variance on
unit count. For 59.6% of accounts (67.5% of MV), only 1 asset is missing, so
`units = residual / price` is deterministic modulo daily price movement. For multi-asset
accounts (40.4%), units are distributed by price weighting, which is a guess.

Lot-level matching via script 03 can precisely identify phantom SELLS (184,891 lots, $1.1B,
with exact unit counts from FIFO). But for phantom BUYS, the unrealized report lacks units
and no reliable proxy exists in the data.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Run 02 + 05 + 05e** with v6 canonical prices fix -- waiting on results
2. **[0.4.0_DS_ClientPlatform] Evaluate v6 results** -- if overshoot resolves, assess whether remaining gap is acceptable
3. **[0.4.0_DS_ClientPlatform] Consider lot-level sell injection** -- use script 03 lot matching for precise phantom closure instead of (account, asset) level aggregation. 184,891 phantom lots with exact units.
4. **[Andrew] BD holdings report with units** -- if available, this closes the buy-side unit gap entirely. Without it, buy injection remains an estimate.
5. **[0.4.0_DS_ClientPlatform] Investigate 900 silver-only accounts** ($97.9M) -- zero gold positions, separate population from injection targets

**Do NOT:**
- Re-enable ghost suppression (injection replaces it with data-driven approach)
- Use Yahoo historical_prices for gold MV estimation (canonical_prices is the only valid source)
- Assume lot count or matched-lot averages can proxy for unmatched lot units
- Run full gold pipeline for testing (targeted 02 + 05 + 05e is sufficient)
