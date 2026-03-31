# ADVI_PRICES.005 -- Yahoo-First Gold Run, Pipeline Timing Fix -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-27
**Start Time:** 12:00 AM ET
**End Time:** 1:15 AM ET

## Objective

Resume crashed gold run with Yahoo-first canonical prices, evaluate AUA gross over/under impact, and fix the broken historical-prices pipeline that prevented Yahoo data from reaching canonical prices.

---

## Work Completed

- **Session recovery** -- DONE. EC2 (c6i.16xlarge, i-01003b035d2988dfb) was idle. First gold run from previous session had completed successfully (all scripts 00-10, CloudFront invalidated). A second pending-trigger re-run had crashed mid-script-05.
- **Yahoo-first canonical prices rebuild + gold incremental** -- DONE. SSM command `e34c9561`: synced silver scripts (Yahoo-first `build_canonical_prices_v2.py` from commit `2dea3ba1`), rebuilt canonical prices, injected MBS overrides, ran full gold incremental (00-10). Completed ~04:48 UTC.
- **05e gap diagnostic on Yahoo-first gold artifacts** -- DONE. SSM command `4a61546d`: ran 05e against freshly rebuilt gold data.
- **Root cause identified: `historical_prices.parquet` stale since 3/25** -- The Yahoo-first change had zero effect on the latest date (3/25) because `historical_prices.parquet` stopped updating on 3/25. Zero Yahoo rows existed for 3/25 in canonical prices.
- **Root cause of staleness: `fetch_historical_prices_yfinance.py` broken since 3/25** -- DONE. A `from lib.config import S3_BUCKET` import was added to the script, but it runs on ephemeral EC2 as a single-file download (no `lib/` directory). Every run since 3/25 crashed with `ModuleNotFoundError`. Fix: inlined `S3_BUCKET` constant, synced to `s3://opal-data-bd/scripts/`.
- **Structural fix: canonical prices rebuild baked into gold runner** -- DONE. Added pre-step to `run_gold_layer.sh` that syncs silver scripts and runs `build_canonical_prices_v2.py` + `inject_scoped_overrides.py` before gold scripts. Every gold run now rebuilds canonical prices from latest silver data regardless of timing.
- **S3 artifacts synced** -- DONE. `run_gold_layer.sh` synced to both `code/gold/` and `code/runner/`. `fetch_historical_prices_yfinance.py` synced to `scripts/` and `code/silver/`.
- **EC2 stopped** -- DONE. c6i.16xlarge shut down.

---

## 05e Results -- Yahoo-First (2026-03-25 snapshot)

| Metric | Value |
|--------|-------|
| Gold AUA | $1,604,396,169 |
| Silver AUA | $1,611,595,100 |
| Net gap | -$7,198,931 (-0.45%) |
| Gross overvaluation | $150,756,535 (2,081 accounts) |
| Gross undervaluation | -$138,110,630 (3,762 accounts) |
| Gross absolute error | $288,867,165 |

**NOTE:** These numbers are identical to the pre-Yahoo baseline because Yahoo had zero rows for 3/25 (the broken fetcher). The Yahoo-first logic only affected historical dates (through 3/24). Once the fetcher fix takes effect (next 10 AM ET run), canonical prices will have Yahoo data for the current date and the gross error numbers should improve.

### Top Undervalued Assets (gold < silver, transaction_observed pricing)

| Asset | Net Gap | Accounts |
|-------|---------|----------|
| PATHFINDER DISCIPLINED US EQUITY ETF | -$3.9M | 12 |
| PATHFINDER FOCUSED OPPORTUNITIES ETF | -$3.6M | 12 |
| DODGE & COX INCOME I | -$2.2M | 1 |
| iSHARES CORE MSCI EAFE ETF | -$1.3M | 13 |
| STATE STREET SPDR PORTFOLIO S&P 500 ETF | -$1.2M | 10 |
| STATE STREET SPDR PORTFOLIO HIGH YIELD BOND ETF | -$1.1M | 4 |

These are the T1 intraday-vs-NAV divergences that Yahoo-first pricing is designed to fix. Once Yahoo data reaches 3/25, these assets with confirmed tickers will use Yahoo close (end-of-day NAV) instead of T1 (intraday trade price).

### Top Overvalued Assets (gold > silver, linear_interpolation pricing)

| Asset | Net Gap | Accounts |
|-------|---------|----------|
| AQR TA DELPHI PLUS FUND LLC | +$2.7M | 2 |
| NATIONAL BANK OF CANADA | +$1.2M | 1 |
| STATE STREET SPDR 1-3 MONTH T-BILL ETF | +$1.0M | 4 |
| INVESCO BULLETSHARES 2027 CORP BOND ETF | +$1.0M | 3 |
| DIREXION DAILY SEMICONDUCTOR BEAR 3X | +$0.8M | 1 |

These are interpolation errors -- assets where the interpolated price diverges from custodian mark-to-market. Not addressable by Yahoo-first (these lack Yahoo tickers or have structural pricing differences).

### Canonical Prices Source Distribution (all dates, post-rebuild)

| Source | Rows | % |
|--------|------|---|
| linear_interpolation | 8,568,245 | 81.6% |
| yahoo_finance | 1,823,700 | 17.4% |
| transaction_observed | 104,950 | 1.0% |

Yahoo covers 3,269 assets across 1,439 trading days. On 3/24 (last date with Yahoo): 1,671 assets. On 3/25 (latest date): 0 assets (broken fetcher).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Inlined S3_BUCKET instead of fixing lib/ download | The ephemeral EC2 model downloads a single script file. Adding lib/ download to user-data would work but is fragile. Inlining a single constant is simpler and keeps the single-file model intact. |
| Baked canonical prices rebuild into run_gold_layer.sh | Decouples gold run from external scheduling. Gold always gets freshest prices regardless of when Yahoo fetch ran. Adds ~2 min to gold runtime on c6i.16xlarge. |
| Killed redundant pending-trigger re-run | First Yahoo-first gold pass completed fully. Second pass was triggered by stale pending marker and would produce identical results. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/silver/fetch_historical_prices_yfinance.py` | Replaced `from lib.config import S3_BUCKET` with inlined constant. Fixes `ModuleNotFoundError` on ephemeral EC2. | No |
| `data/black_diamond/scripts/gold/run_gold_layer.sh` | Added pre-step: sync silver scripts, rebuild canonical_prices_v2, inject scoped overrides before gold scripts. | No |

**S3 synced (not git committed):**
- `s3://opal-data-bd/scripts/fetch_historical_prices_yfinance.py` -- fix live for next 10 AM run
- `s3://opal-data-bd/code/gold/run_gold_layer.sh` -- fix live for next gold run
- `s3://opal-data-bd/code/runner/run-gold-layer.sh` -- boot-time self-update copy
- `s3://opal-data-bd/code/silver/*` -- latest silver scripts including Yahoo-first build

---

## Pipeline Timing (corrected chain)

```
10:00 AM ET  historical-prices-daily (EventBridge)
             -> historical-prices-scheduler Lambda
             -> ephemeral EC2: fetch_historical_prices_yfinance.py
             -> writes daily parquets + updates historical_prices.parquet

 5:40 PM ET  bd-transaction-pipeline-trigger (EventBridge)
             -> transaction + allocation downloads

 7:00 PM ET  bd-gold-nightly-fallback (EventBridge)
             -> bd-gold-layer-runner EC2
             -> run_gold_layer.sh:
                PRE-STEP: sync silver scripts
                PRE-STEP: build_canonical_prices_v2.py (reads historical_prices.parquet)
                PRE-STEP: inject_scoped_overrides.py
                GOLD: scripts 00 -> 02 -> 05 -> 05c -> 05d -> 07 -> 08b -> 12 -> 06b -> 08 -> 09 -> 10
                POST: pipeline-complete sentinel, CloudFront invalidation
```

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Two fixes applied and synced to S3 but not yet git committed: (1) `fetch_historical_prices_yfinance.py` inlined S3_BUCKET to fix `ModuleNotFoundError` that broke Yahoo fetcher since 3/25, (2) `run_gold_layer.sh` pre-step added to rebuild canonical prices before every gold run. The 05e diagnostic ran on Yahoo-first gold data but showed no improvement because Yahoo had no 3/25 data (the broken fetcher). The next full pipeline cycle (10 AM Yahoo fetch -> 7 PM gold run on 3/27) will be the first run with the complete fixed chain.

## Next Steps

1. **[0.6.0_AE_PartnerETL] Commit the two fixes to CLOUD** -- `fetch_historical_prices_yfinance.py` and `run_gold_layer.sh`. These are already live on S3 but need git tracking.
2. **[0.6.0_AE_PartnerETL] Verify 10 AM ET run succeeds** -- Check `s3://opal-data-bd/logs/historical-prices/2026-03-27_*.log` after 10:15 AM ET. Confirm `historical_prices.parquet` LastModified updates past 3/25.
3. **[0.6.0_AE_PartnerETL] Verify 7 PM ET gold run** -- Confirm pre-step runs canonical prices rebuild, gold scripts consume Yahoo-priced data for 3/25+, and 05e (if run manually after) shows reduced gross over/under for transaction_observed assets.
4. **[0.4.0_DS_ClientPlatform] Evaluate gross error reduction** -- Once Yahoo data covers 3/25+, re-run 05e and compare gross overvaluation/undervaluation vs the $150M/$138M baseline. The Pathfinder/iShares/SPDR undervaluation ($12M combined) should shrink significantly with Yahoo close prices replacing T1 intraday.

**Do NOT:**
- Assume the current 05e numbers reflect Yahoo-first impact -- they don't (Yahoo had 0 rows for 3/25)
- Re-add `from lib.config import S3_BUCKET` to `fetch_historical_prices_yfinance.py` -- it runs as a single file on ephemeral EC2
- Remove the pre-step from `run_gold_layer.sh` -- it's the only mechanism ensuring canonical prices are current before gold scripts
