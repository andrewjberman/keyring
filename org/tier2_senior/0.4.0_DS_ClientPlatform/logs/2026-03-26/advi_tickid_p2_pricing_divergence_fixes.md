# ADVI_TICKID P2 -- Pricing Divergence Fixes

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-26
**Project:** ADVI_TICKID (reopened for P2)
**PRD:** docs/architecture/ADVI_TICKID_PRICING_DIVERGENCE_ADDENDUM.md

---

## Objective

Implement 3 of 4 fixes from the CTO-authored pricing divergence addendum targeting
$414M gross pricing gap between gold (units x canonical_prices) and silver
(BD-reported account_market_value). Fix 4 (.008) is gated on .007 results.

---

## Work Completed

### 1. ADVI_TICKID.005 -- Feedback Bridge + Method 5 (F1: $257M)

Modified `data/black_diamond/scripts/classification/resolve_tickers.py`:

**sync_to_ticker_lookup():** New function called after resolution parquet is written.
- Loads `config/ticker_lookup.json` from S3
- For each resolved entry with confidence >= 0.85 where asset_name is not already in lookup, appends new entry (append-only, never overwrites existing)
- Validates new tickers against Yahoo Finance (50/batch, 3s delay)
- Appends verified tickers to `config/yahoo_safe_tickers.txt`
- Logs count of new entries and yahoo validation results

**Method 5 (individual_stock_pattern):** No longer a stub.
- Extracts company stems from SEC-style names (e.g., "WALMART INC COM")
- Matches stems against bd-securities DynamoDB items
- For unmatched stems, attempts yfinance ticker search validation (capped at 200)
- Now accepts `db_items` parameter for DynamoDB cross-reference

**Commit:** `76c26f33`

### 2. ADVI_TICKID.006 -- Yahoo Coverage Sweep + Stale Diagnosis (F2+F3: $11.7M)

Modified `data/black_diamond/scripts/silver/fetch_historical_prices_yfinance.py`:

**--sweep-unlisted mode:** Closes the 493-asset coverage gap.
- Loads all tickers from ticker_lookup.json, compares to yahoo_safe_tickers.txt
- Batch-validates unlisted tickers against Yahoo (50/batch, 3s delay)
- Appends verified tickers to safe list on S3
- Logs verified vs failed counts

**--diagnose-stale mode:** Addresses 38 assets with stale Yahoo data.
- Loads historical_prices.parquet, finds tickers with max_date > 7 days old
- Attempts 30-day re-fetch for each stale ticker
- Appends refreshed data to historical_prices.parquet
- Classifies tickers as "refreshed" (Yahoo returned data) or "delisted" (no data)
- Logs per-ticker last-seen dates for delisted securities

**Commit:** `da272777`

### 3. ADVI_TICKID.007 -- Silver AUA Override (F5: $94M)

Modified `data/black_diamond/scripts/gold/05_build_client_performance.py` and
`data/black_diamond/scripts/gold/05b_build_account_performance.py`:

**Account-level silver override logic:**
- For each date partition, loads `silver/allocations/{date}.parquet`
- Computes gold AUA per account (sum of units * price)
- Compares to silver `account_market_value`
- If divergence > 20% (OVERRIDE_THRESHOLD) and silver_aua > $1,000 (MINIMUM_AUA): overrides gold with silver
- Ghost accounts remain excluded before override logic runs

**Script 05 implementation:**
- `_load_silver_allocations(date_str)` helper using main-process s3 client
- Override scales position-level market_value so account total = silver AUA
- Module-level `_override_stats` accumulator for end-of-run summary
- Prints total overrides, dollar impact, largest single override

**Script 05b implementation:**
- `_load_silver_allocations_05b(date_str)` using process-safe `_get_s3()`
- Override at account-aggregate level (post-aggregation replacement, simpler than 05)
- `silver_override` boolean column tracked per partition, aggregated and logged after concat

**Commit:** `0253186a`

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Method 5 uses DynamoDB stem match first, yfinance second | DynamoDB is free and fast; yfinance search is rate-limited. DynamoDB covers most SEC-named stocks that already have an entry. |
| sync_to_ticker_lookup is append-only | TICKER_CORRECTIONS in lib/ticker_overrides.py takes final precedence. Feedback bridge must not overwrite manually-corrected entries. |
| Script 05 scales positions, 05b replaces account total | 05 aggregates to relationship level, so position-level scaling preserves tax_status breakdown. 05b already has account-level aggregation, so direct replacement is cleaner. |
| Override threshold at 20% | Per CTO endorsement. Catches structural mispricing while allowing normal yahoo/carry-forward variance. Money markets (gold = silver at $1.00) never trigger. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/classification/resolve_tickers.py` | sync_to_ticker_lookup() + method 5 | Yes -- `76c26f33` |
| `data/black_diamond/scripts/silver/fetch_historical_prices_yfinance.py` | --sweep-unlisted + --diagnose-stale | Yes -- `da272777` |
| `data/black_diamond/scripts/gold/05_build_client_performance.py` | Silver AUA override | Yes -- `0253186a` |
| `data/black_diamond/scripts/gold/05b_build_account_performance.py` | Silver AUA override | Yes -- `0253186a` |

---

## Current State

**Status:** IN PROGRESS (3/4 TOs complete, .008 gated)
**Active branch:** `CLOUD`

ADVI_TICKID P2 has 3 of 4 task orders complete. All code is committed locally.
The three commits implement the feedback bridge (resolve_tickers -> ticker_lookup -> yahoo_safe),
Yahoo coverage gap closure (sweep-unlisted + diagnose-stale), and account-level silver AUA
override in scripts 05/05b. Task order .008 (bond face-value classifier) remains `pending`,
gated on .007's gold run results -- if script 05c gap drops below 0.5% after the override,
.008 is marked "not needed."

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push commits** -- `76c26f33`, `da272777`, `0253186a` to CLOUD remote
2. **[0.6.0_AE_PartnerETL] Run resolve_tickers.py --upload** on EC2 to populate ticker_lookup.json and yahoo_safe_tickers.txt feedback
3. **[0.6.0_AE_PartnerETL] Run fetch_historical_prices_yfinance.py --sweep-unlisted** on EC2 to validate and add unlisted tickers
4. **[0.6.0_AE_PartnerETL] Run fetch_historical_prices_yfinance.py --diagnose-stale** on EC2 to refresh stale tickers
5. **[0.6.0_AE_PartnerETL] Run fetch_historical_prices_yfinance.py --backfill** on EC2 for newly-added safe tickers
6. **[0.6.0_AE_PartnerETL] Run build_canonical_prices_v2.py** to rebuild canonical_prices with enriched T2
7. **[0.6.0_AE_PartnerETL] Full gold layer run** (subsumes GLDRST .002 scope + TICKID P2 changes)
8. **[0.4.0_DS_ClientPlatform] Check script 05c output** after gold run -- if gap < 0.5%, mark .008 "not needed"

**Do NOT:**
- Run resolve_tickers.py without --upload (feedback bridge only writes to S3 in upload mode)
- Run --sweep-unlisted before resolve_tickers.py --upload (new resolutions must feed ticker_lookup.json first)
- Begin .008 before .007 gold run validation
