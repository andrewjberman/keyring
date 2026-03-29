# AUA Gap Investigation + Phantom Resolution -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-28 to 2026-03-29
**Start Time:** 5:00 PM ET (03-28)
**End Time:** 4:20 AM ET (03-29)
**Project:** ADVI_PRICES (gap investigation + ticker resolution + phantom closure)

---

## Objective

Investigate the gold-vs-silver AUA gap ($37.3M net, $150M gross over / $138M gross under).
Identify root causes, implement fixes, and build the infrastructure to close the gap permanently.

---

## Work Completed

### 1. Yahoo Ticker Expansion (754 YF_OVERRIDES)

Discovered `build_canonical_prices_v2.py` wasn't reading `ASSET_NAME_TO_TICKER` from
`etf_classification.py`. Created single `YF_OVERRIDES` table in `lib/ticker_overrides.py`.

Rebuilt from BD's Unrealized Gain/Loss report (definitive ticker assignments):
- 754 total entries (was 6 in OPAL_ETF_OVERRIDES)
- All 243 unique tickers validated against Yahoo Finance locally via yfinance
- 498 new tickers backfilled to historical_prices.parquet (240K rows, 4.97M total)
- 16 wrong-ticker corrections from 05r audit ($24.9M mispricing)
- Non-ASCII characters stripped for EC2 compatibility

### 2. Scoped Overrides for Shield Products

Back-solved NAVs for 26 Shield/buffer/AQR products from silver allocations:
- Shield products: $1.07-$1.19 (was $1.00 par from BD transactions)
- AQR Delphi: $0.95 (was $1.00)
- Methodology: shield_mv = silver_mv - sum(yahoo_priced_holdings) for 113 clean accounts
- Consistent results: std 0.03-0.18 across accounts

### 3. Pipeline Bug Fix: --upload Flag

Found `run_gold_layer.sh` called `inject_scoped_overrides.py` without `--upload`,
so ALL scoped overrides (existing 7 + new 26) silently ran in dry-run mode and
never wrote to S3. Fixed.

### 4. Root Cause Discovery: Opal Onboarding Rotation

BD Unrealized + Realized Gain/Loss reports revealed the root cause:
- Opal came on as partner ~4/30/2024. 32,632 trades on that single date.
- Pre-Opal model (VTV, IQLT, QUAL, BIL, COWZ, JEPI) rotated into Opal model
  (PFDE, PFOE, DIVZ, IDVZ, IEFA, CLIP)
- The SELL side of the rotation was never delivered to our transaction feed
- Result: ~41K phantom positions (old model) coexisting with real positions (new model)
- Net gap near zero because rotation was dollar-neutral, but holdings decomposition wrong

### 5. Lot-Level Three-Way Reconciliation

Matched at lot level: (AccountID, CUSIP, Open Date, Unit Cost) across our holdings_lots,
BD unrealized, and BD realized:
- 188,972 lots confirmed open ($681M)
- 39,155 lots confirmed phantom-sold via 15mo realized ($104M)
- With DIVZ name fix + 33 months realized: 91.6% phantoms confirmed, 3,390 unexplained (8.4%)
- Full history (2022-2026): 88.9% confirmed, 4,614 hard floor (non-sale closures)

### 6. Realized Sell Injection (the fix)

Implemented synthetic sell injection in `02_build_positions_cube.py`:
- New Step 2a after computing unit events from transactions
- Loads `silver/realized/` (892K lots) + `silver/unrealized/` (402K lots)
- Identifies (account, asset) pairs in realized but NOT in unrealized = confirmed closed
- Injects synthetic sell of -current_units on the realized trade_date
- Cumsum naturally closes the position on the correct date
- 51,317 synthetic sell events targeting the phantom positions

Ghost suppression (Option 3b) removed -- the realized sell injection replaces it
with a precise, data-driven approach instead of a blunt silver threshold.

### 7. Silver Realized Layer

Built `merge-capital-gains.py` to ingest BD's Realized Gain/Loss Excel exports:
- 12 quarterly files (2021 Q1 through 2026 Q1) = 892,588 rows
- Partitioned by trade_date into 1,198 daily parquets at `silver/realized/`
- Name alias mapping (POLEN DIVIDEND INCOME ETF -> OPAL DIVIDEND INCOME ETF)
- Uploaded to S3

### 8. Diagnostic Scripts

05f-05t: 16 diagnostic scripts for gap decomposition, tail analysis, unit math
audit, pricing source analysis, asset matching, and lot-level reconciliation.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Single YF_OVERRIDES table | CTO: one source of truth, not scattered mapping sources |
| BD Unrealized as authoritative ticker source | BD's own assignments are definitive |
| Back-solve Shield NAVs from silver | BD reports par ($1.00), silver has real NAV |
| Realized sell injection over ghost suppression | Uses BD's actual sell data, not a threshold heuristic |
| Remove ghost suppression | Redundant with realized injection, risks false positives on small accounts |
| Lot-level matching (CUSIP+date+cost) | Most reliable reconciliation key across all three datasets |
| Timeseries safety on any date-gated filter | Andrew: silver is point-in-time, can't retroactively suppress historical partitions |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `silver/lib/ticker_overrides.py` | 754 YF_OVERRIDES + 25 TICKER_CORRECTIONS | Yes -- multiple commits, final `a8925d3d` |
| `silver/build_canonical_prices_v2.py` | Import YF_OVERRIDES | Yes -- `26750d23` |
| `silver/bd_price_update.py` | Import YF_OVERRIDES + 26 scoped overrides | Yes -- `11255fb1` |
| `gold/02_build_positions_cube.py` | Realized sell injection + ghost suppression removed | Yes -- `65612b84`, `eece84ac` |
| `gold/run_gold_layer.sh` | Fix --upload flag | Yes -- `cb00f031` |
| `silver/merge-capital-gains.py` | New ingestion script for realized G/L | Yes -- `01216c15` |
| `silver/historical_prices.parquet` (S3) | +498 tickers, +240K rows | Yes -- S3 upload |
| `config/yahoo_safe_tickers.txt` (S3) | 3,596 tickers (was 2,888) | Yes -- S3 upload |
| `silver/realized/` (S3) | 1,198 partitions, 892K rows | Yes -- S3 upload |
| `silver/unrealized/` (S3) | BD unrealized report as parquet | Yes -- S3 upload |

---

## Current State

**Status:** COMPLETE -- awaiting gold rebuild to validate
**Active branch:** `CLOUD`

ROOT CAUSE: Opal onboarding rotation ~4/30/2024. 32,632 trades rotated pre-Opal
model holdings into Opal model. Sell side never delivered to transaction feed.
91.6% of 41K phantoms confirmed via lot-level reconciliation against BD realized data.

FIX: Realized sell injection in 02_build_positions_cube.py closes 51K phantom
positions using BD's actual sell dates from silver/realized/. Combined with 754
YF_OVERRIDES, 26 scoped overrides, and the --upload flag fix, the next gold rebuild
should bring gold AUA into close alignment with silver for the first time.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Full gold rebuild** with all fixes -- sync code from CLOUD, run full mode
2. **[0.6.0_AE_PartnerETL] Run 05k** on the new gold data to measure the gap post-fixes
3. **[Andrew] Add BD Unrealized + Realized to bronze daily feed** for ongoing reconciliation
4. **[0.4.0_DS_ClientPlatform] Name normalization pass** on remaining 3,390 unexplained phantoms
5. **[0.4.0_DS_ClientPlatform] Investigate missing positions** -- 182K lots BD has that we don't

**Do NOT:**
- Re-add ghost suppression (realized injection replaces it)
- Change the transaction_id dedup (confirmed correct, no cross-account collisions)
- Trust the "our_only" lot count (130K) as phantom -- inflated by cost-basis rounding
- Use unrealized whitelist as a blanket cube filter (oversuppresses $364M)
