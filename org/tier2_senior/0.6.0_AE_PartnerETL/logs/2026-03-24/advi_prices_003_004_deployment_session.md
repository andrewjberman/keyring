# ADVI_PRICES.003 + .004 -- Deployment Session -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-24
**Task Orders:** ADVI_PRICES.003 (partial), ADVI_PRICES.004 (phases 1-3 in progress)
**Status:** Phase 3 gold rerun IN PROGRESS

---

## Phase 0: .003 Partial Work (Before COO Intervention)

### IYF Ticker Correction (COMPLETE)

**Commit:** `1c7bbb4a`
**Author:** `0.6.0_AE_PartnerETL`

Added 9th ticker correction: `ISHARES U.S. FINANCIALS ETF` XLF -> IYF.
DS flagged -16.5% error but did not include in commit `61b34f77`.

### S3 Code Upload (COMPLETE)

Uploaded both pricing scripts to `s3://opal-data-bd/code/silver/`:
- `bd_price_update.py` (with all 32 corrections from DS .003 + .004)
- `build_canonical_prices_v2.py` (kept in sync)

### ticker_lookup.json Patch (COMPLETE)

Downloaded 10,116-record ticker_lookup.json, patched 9 corrections (7 corrected, 2 removed), re-uploaded. Later DS added 23 more corrections in the code (total 32), but ticker_lookup.json only has the 9 from .003 -- the _TICKER_CORRECTIONS dict in the code handles the rest.

### Premature Canonical Rebuild (SUPERSEDED)

Ran build_canonical_prices_v2.py BEFORE fixing historical_prices. Result:
- 82.3% interpolation, 15.8% yahoo, 1.9% T1
- COO discovered 16 missing + 670 stale tickers in historical_prices.parquet
- This rebuild was superseded by Phase 2 rebuild below

---

## Phase 1: Historical Prices Backfill (COMPLETE)

**Task Order:** ADVI_PRICES.004, requirement 1
**SSM Command:** `b9a548b2-1e20-4584-b6a8-25d9b172889d`

Wrote and deployed `backfill_historical_prices.py` to EC2 via S3:
- Reads yahoo-safe ticker list from S3 (2,880 tickers, DS commit `4f4a7fc1`)
- Categorized: 16 MISSING, 670 STALE (before 2026-03-17), 2,194 CURRENT
- Fetched from yfinance in batches of 50 with 2s sleeps
- Added 143,588 net new rows (2,922,097 -> 3,065,685)

### Coverage After Backfill

| Category | Count | Notes |
|----------|-------|-------|
| OK | 2,234 | Current through 2026-03-21+ |
| Still stale | 646 | Delisted, expired ETFs, or transient yfinance errors |
| Missing | 0 | All 16 formerly missing tickers backfilled |

### Critical Ticker Verification (ALL PASS)

All 18 DS-corrected tickers + 5 spot-check tickers verified current:

| Ticker | Rows | Latest | Close | Note |
|--------|------|--------|-------|------|
| CBLL | 362 | 2026-03-24 | $18.83 | was CRBL ($0.05) |
| SERV | 512 | 2026-03-24 | $9.25 | was SRVR |
| IUSG | 6,451 | 2026-03-24 | $157.14 | was IGRO |
| IWR | 1,564 | 2026-03-24 | $97.62 | was MDY |
| USXF | 1,448 | 2026-03-24 | $55.81 | was ECOZ |
| BAI | 355 | 2026-03-24 | $34.59 | was AIIQ |
| QQQM | 1,555 | 2026-03-24 | $240.81 | was QQQ |
| PSLV | 3,872 | 2026-03-24 | $22.47 | was SIVR |
| FLRN | 3,597 | 2026-03-24 | $30.79 | was FLTN |
| VBTIX | 1,554 | 2026-03-23 | $9.66 | was BND ($73.45) |
| VTIAX | 1,563 | 2026-03-23 | $40.99 | was VXUS |
| VTSNX | 3,851 | 2026-03-23 | $163.92 | was VXUS |
| VTPSX | 3,851 | 2026-03-23 | $163.95 | was VXUS |
| VSMSX | 3,907 | 2026-03-23 | $457.02 | was VIOO |
| VEMIX | 6,475 | 2026-03-23 | $33.76 | was VWO |
| SWAGX | 2,282 | 2026-03-23 | $8.93 | was SCHZ |
| SWTSX | 6,745 | 2026-03-23 | $15.84 | was SCHB |
| SWPPX | 1,554 | 2026-03-23 | $16.91 | was SCHB |
| IYF | 6,494 | 2026-03-24 | $117.78 | was XLF ($49) |
| GLTR | 3,877 | 2026-03-24 | $205.03 | was GLDM ($89) |
| IEFA | 1,561 | 2026-03-23 | $89.41 | spot-check (was $57.43) |
| IEMG | 1,562 | 2026-03-23 | $70.46 | spot-check (was $48.22) |
| IJK | 1,564 | 2026-03-24 | $101.40 | spot-check (was $1.00) |

### Schema Note

historical_prices.parquet has 5 columns: date, ticker, close, fetch_date, source.
Backfilled rows have null fetch_date/source (2,664,170 / 3,065,685 = 87%).
The daily scheduler will populate metadata on future runs. This is non-blocking.

---

## Phase 2: Canonical Prices Rebuild (COMPLETE)

**Task Order:** ADVI_PRICES.004, requirement 2
**SSM Command:** `1b6edd6d-a7db-4718-9df8-65685509be87`

Ran build_canonical_prices_v2.py on EC2 (113s, 10,447,015 rows, 9,972 assets).

### Source Distribution Comparison

| Source | Premature Run | Post-Backfill Run | Delta |
|--------|--------------|-------------------|-------|
| yahoo_finance | 1,650,684 (15.8%) | 1,729,677 (16.6%) | +78,993 |
| linear_interpolation | 8,596,571 (82.3%) | 8,522,912 (81.6%) | -73,659 |
| transaction_observed | 198,952 (1.9%) | 194,426 (1.9%) | -4,526 |

Yahoo coverage increased by +78,993 rows (+4.8% relative increase).

### BNP Canary (PASS)

| Asset | Price | Source | Status |
|-------|-------|--------|--------|
| BNP PARIBAS SA | $1.02 | linear_interpolation | PASS (ticker removed) |
| BNP PARIBAS 0% 05/26/2026 | $1.45 | linear_interpolation | PASS |
| BNP PARIBAS SPONSORED ADR | $95.03 | yahoo_finance | Correct (ADR is real equity) |

### 5 Spot-Checks (ALL PASS)

| Ticker | Price | Source | Expected | Status |
|--------|-------|--------|----------|--------|
| IEFA | $87.60 | transaction_observed | ~$89 | PASS (1.6% diff) |
| IEMG | $68.73 | transaction_observed | ~$70 | PASS (1.8% diff) |
| IJK | $99.69 | transaction_observed | ~$103 | PASS (3.2% diff) |
| VBTIX | $9.63 | transaction_observed | ~$9.66 | PASS (0.3% diff) |
| CBLL | $18.50 | yahoo_finance | ~$19 | PASS (2.6% diff) |

Note: IEFA/IEMG/IJK/VBTIX show T1 on latest date because there were transactions.
Yahoo prices exist for other dates. bd_price_update.py handles the override hierarchy.

---

## Phase 3: Gold Rerun (IN PROGRESS)

**Task Order:** ADVI_PRICES.004, requirement 3
**SSM Command:** `bf949bac-03c1-47e0-bce9-6bbd2ac3283b`

### Issue: Stale run_gold_layer.sh on S3

First attempt failed: the deployed `s3://opal-data-bd/scripts/run_gold_layer.sh`
pointed to `s3://scripts/gold_layer/` (old path with stale 2026-02-23 scripts).
The local version uses `s3://code/gold/` (current scripts).

Fixed by uploading local `run_gold_layer.sh` to S3. Gold rerun v2 is now running.

### Pending: Reconciliation

After gold rerun completes, run:
```
python recon_lots_vs_allocations.py --date {latest_alloc_date}
```
Compare to baselines:
- Pre-fix (2026-03-19): +$296M (+18.6%)
- Post PRICES.001 (phantom fix): -$57.7M (-3.6%)
- Target: < -1.5%

---

## Phase 4: Scheduler Diagnosis (PARTIAL)

### Root Cause Identified

The historical-prices-scheduler Lambda runs daily (logs confirm through 2026-03-24).
The EC2 spawned by the scheduler runs `fetch_historical_prices_yfinance.py` which:
1. Loads ALL 10,116 tickers from `ticker_lookup.json` on S3
2. Fetches in batches of 100 with NO sleep between batches
3. yfinance rate-limits aggressively: today only 1,581/3,400 fetched

The ~706 Feb 12 dropoff: tickers processed alphabetically. Once rate-limited, remaining
tickers (late alphabet: R-Z) never get fetched. Each day the same tickers fail because
the script doesn't randomize order or retry.

### Fix Required

1. Reduce batch size: 100 -> 50
2. Add 2-3s sleep between batches
3. Filter to yahoo-safe tickers only (2,880 vs 10,116)
4. Randomize ticker order so rate-limit failures don't always hit the same tickers
5. Add retry pass for failed tickers

### Fix NOT YET APPLIED

The scheduler fix is Phase 4 -- can run in parallel with Phase 3 but requires modifying
`fetch_historical_prices_yfinance.py` and deploying to S3.

---

## Files Created/Modified This Session

| File | Action | Purpose |
|------|--------|---------|
| `data/black_diamond/scripts/silver/bd_price_update.py` | Modified | Added IYF to _TICKER_CORRECTIONS (commit 1c7bbb4a) |
| `data/black_diamond/scripts/silver/build_canonical_prices_v2.py` | Modified | Same (kept in sync) |
| `s3://opal-data-bd/code/silver/bd_price_update.py` | Uploaded | Deploy corrected pricing script |
| `s3://opal-data-bd/code/silver/build_canonical_prices_v2.py` | Uploaded | Deploy corrected canonical builder |
| `s3://opal-data-bd/config/ticker_lookup.json` | Patched | 9 ticker corrections applied |
| `s3://opal-data-bd/config/yahoo_safe_tickers.txt` | Uploaded | DS-curated safe ticker list |
| `s3://opal-data-bd/code/diagnostics/backfill_historical_prices.py` | Uploaded | Phase 1 backfill script |
| `s3://opal-data-bd/code/diagnostics/verify_backfill.py` | Uploaded | Phase 1 verification |
| `s3://opal-data-bd/code/diagnostics/verify_phase2.py` | Uploaded | Phase 2 verification |
| `s3://opal-data-bd/scripts/run_gold_layer.sh` | Uploaded | Fixed stale version (was pointing to old script path) |
| `s3://opal-data-bd/silver/historical_prices.parquet` | Updated | Backfill added 143,588 rows |
| `s3://opal-data-bd/silver/prices/canonical_prices.parquet` | Rebuilt | 10.4M rows, 16.6% yahoo |

## EC2 State

- Runner `i-01003b035d2988dfb` (r6i.xlarge, 32GB): RUNNING
- Instance stopped once during session (likely SSM agent timeout during long rebuild)
- Restarted successfully

## SSM Commands (Chronological)

| Command ID | Purpose | Status |
|-----------|---------|--------|
| 60a4c0df | Premature canonical rebuild | Success (superseded) |
| 4017c1cd | BNP canary check | Success |
| 0238dcfd | Fetch GLTR/VTMGX/IYF (failed shell escaping) | Failed |
| b9a548b2 | Phase 1 backfill | Success |
| e1797eef | Get backfill log tail | Success |
| 02ebe4d1 | Verify backfill | Success |
| ed56dea1 | Canonical rebuild (instance died mid-run) | Unknown |
| 1b6edd6d | Canonical rebuild (retry) | Success |
| 7bff683e | Phase 2 verification | Success |
| fe18311e | Gold rerun v1 (CRLF error) | Success (script failed) |
| 9accda59 | Gold rerun v2 (stale run_gold_layer.sh) | Success (positions_cube failed) |
| bf949bac | Gold rerun v3 (correct scripts) | IN PROGRESS |
