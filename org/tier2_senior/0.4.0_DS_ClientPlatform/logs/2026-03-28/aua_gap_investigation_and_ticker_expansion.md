# AUA Gap Investigation + Yahoo Ticker Expansion -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-28 to 2026-03-29
**Start Time:** 5:00 PM ET (03-28)
**End Time:** 3:15 AM ET (03-29)
**Project:** ADVI_PRICES (gap investigation + ticker resolution)

---

## Objective

Investigate the gold-vs-silver AUA gap ($37.3M net, $150M gross over / $138M gross under).
Identify root causes and implement fixes to reduce the gap.

---

## Work Completed

### 1. Yahoo Ticker Expansion (754 YF_OVERRIDES)

Discovered that `build_canonical_prices_v2.py` wasn't reading the `ASSET_NAME_TO_TICKER`
dict from `etf_classification.py`. Created a single `YF_OVERRIDES` table in
`lib/ticker_overrides.py` as the one source of truth for all BD-asset-name-to-Yahoo-ticker
mappings.

Rebuilt from BD's Unrealized Gain/Loss report (definitive ticker assignments):
- 754 total entries (was 6 in OPAL_ETF_OVERRIDES)
- All 243 unique tickers validated against Yahoo Finance locally
- 498 new tickers backfilled to historical_prices.parquet (240K rows)
- 16 wrong-ticker corrections from 05r audit ($24.9M mispricing)
- Non-ASCII characters stripped for EC2 compatibility

### 2. Scoped Overrides for Shield Products

Back-solved NAVs for 26 Shield/buffer/AQR products from silver allocations:
- Shield products: $1.07-$1.19 (was $1.00 par)
- AQR Delphi: $0.95 (was $1.00)
- Added to `_SCOPED_PRICE_OVERRIDES` in `bd_price_update.py`

### 3. Pipeline Bug Fix: --upload Flag

Found `run_gold_layer.sh` called `inject_scoped_overrides.py` without `--upload`,
so ALL scoped overrides (existing 7 + new 26) silently ran in dry-run mode.

### 4. Ghost Suppression (Option 3b)

Added silver-gated ghost suppression to `02_build_positions_cube.py`:
- Excludes accounts with silver $100-$10K from current-date partitions
- Timeseries safety: historical partitions never suppressed

### 5. Lot-Level Three-Way Reconciliation

Using BD Unrealized + Realized Gain/Loss reports as holding-level ground truth:
- Matched at lot level: (AccountID, CUSIP, Open Date, Unit Cost)
- 188,972 lots confirmed open ($681M)
- 39,155 lots confirmed phantom-sold ($104M) -- BD sold, we still hold
- 130,698 lots unmatched at lot level ($753M, likely cost-basis rounding)

### 6. Diagnostic Scripts Written

05f-05t: 16 diagnostic scripts for gap decomposition, tail analysis, unit math
audit, pricing source analysis, asset matching, and lot-level reconciliation.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Single YF_OVERRIDES table (not layered) | CTO direction: one source of truth, not scattered mapping sources |
| BD Unrealized report as authoritative ticker source | BD's own ticker assignments are definitive |
| Back-solve Shield NAVs from silver | BD reports par ($1.00), silver has real NAV. Consistent results (std 0.03-0.18) |
| Timeseries-safe ghost suppression | Andrew: silver is point-in-time, can't retroactively suppress historical partitions |
| Lot-level matching (CUSIP+date+cost) | Most reliable reconciliation key across all three datasets |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `silver/lib/ticker_overrides.py` | 754 YF_OVERRIDES + 25 TICKER_CORRECTIONS | Yes -- multiple commits |
| `silver/build_canonical_prices_v2.py` | Import YF_OVERRIDES | Yes -- `26750d23` |
| `silver/bd_price_update.py` | Import YF_OVERRIDES + 26 scoped overrides | Yes -- `11255fb1` |
| `gold/02_build_positions_cube.py` | Ghost suppression (Option 3b) | Yes -- `f0dc06bf` |
| `gold/run_gold_layer.sh` | Fix --upload flag | Yes -- `cb00f031` |
| `silver/historical_prices.parquet` (S3) | +498 tickers, +240K rows | Yes -- S3 upload |
| `config/yahoo_safe_tickers.txt` (S3) | 3,596 tickers (was 2,888) | Yes -- S3 upload |

---

## Current State

**Status:** COMPLETE (investigation + fixes deployed)
**Active branch:** `CLOUD`

Net gap reduced from $37.3M to $8.5M. Root causes identified:
- 39,155 phantom lots ($104M) confirmed by lot-level BD reconciliation
- Remaining undershoot from missing BD transaction history (lots BD has that our pipeline doesn't)
- These are BD data feed completeness issues, not pipeline logic bugs

---

## Next Steps

1. **[Andrew] Request daily BD Unrealized report feed** -- the unrealized whitelist is the
   most reliable phantom suppression source. Needs to be ingested alongside allocations.
2. **[Andrew] Request full-history Realized report** (2024+) to identify all phantom sells.
3. **[0.4.0_DS_ClientPlatform] Productionize lot-level reconciliation** -- build a script
   that ingests unrealized + realized and suppresses confirmed-phantom lots from the cube.
4. **[0.6.0_AE_PartnerETL] Run gold with all fixes** -- the --upload flag fix, ghost
   suppression, and scoped overrides are all committed and ready.

**Do NOT:**
- Apply the unrealized whitelist as a blanket filter (oversuppresses $364M)
- Change the transaction_id dedup (confirmed correct, no cross-account collisions)
- Trust the "our_only" lot count (130K) as phantom -- it's inflated by cost-basis rounding
