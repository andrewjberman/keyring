# Opal ETF Ticker Fix — Silver Deploy + canonical_prices Rebuild — 0.6.0_AE_PartnerETL

**Date:** 2026-03-18
**Start Time:** 15:45 UTC
**End Time:** 15:58 UTC

## Objective

Deploy DS's `_OPAL_ETF_OVERRIDES` silver script fix to EC2 and run a full rebuild of
`canonical_prices.parquet` so that Opal/Pathfinder-branded ETFs no longer carry `ticker=NaN`
downstream into `holdings_lots`, `client_tax_liability`, and portal position lists.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Verify DS changes present but uncommitted | Both `build_canonical_prices_v2.py` and `bd_price_update.py` had local modifications |
| 2 | Commit silver scripts to CLOUD with DS author | `b69d1ae6` |
| 3 | `aws s3 cp` both scripts to `s3://opal-data-bd/code/silver/` | Both uploaded successfully |
| 4 | Write run script, upload to `s3://opal-data-bd/code/adhoc/` | `run_canonical_prices_full.sh` |
| 5 | SSM send-command: first attempt failed | `--full-rebuild --upload` flags not valid — script takes no args except `--dry-run` |
| 6 | Fix run script, re-upload, re-send SSM | Command `11a9621a` — Success |
| 7 | Rebuild completed in 114s | 10,406,355 rows, 91.3 MB written to `s3://opal-data-bd/silver/prices/canonical_prices.parquet` |
| 8 | Spot-check canonical_prices.parquet locally | 6/6 Opal ETF name variants now have correct tickers, 0 NaN |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Commit DS changes before uploading to S3 | Standard deployment protocol: code must correspond to a git commit before any AWS operation |
| Run full rebuild (not incremental) | The fix must backfill all historical dates — incremental would only correct today's new rows. `build_canonical_prices_v2.py` always does a full rebuild by design (no incremental mode) |
| Run on bd-gold-layer-runner (already up) | Instance was already running from earlier ADVI_MIXV2.003 work; avoided a cold start |

---

## Rebuild Output

```
Total rows:    10,406,355
Date range:    2020-06-30 -> 2026-03-16
Unique assets: 9,952
Size:          91.3 MB
Elapsed:       114s

By source:
  linear_interpolation   8,561,465  (82.3%)
  yahoo_finance          1,651,217  (15.9%)
  transaction_observed     193,673  ( 1.9%)
```

## Spot-Check

```
                              asset_name  ticker
          OPAL DIVIDEND INCOME ETF         DIVZ
OPAL INTERNATIONAL DIVIDEND INCOME ETF     IDVZ
  PATHFINDER DISCIPLINED US EQUITY ETF     PFDE
  PATHFINDER FOCUSED OPPORTUNITIES ETF     PFOE
             POLEN DIVIDEND INCOME ETF     DIVZ
                 POLEN HIGH INCOME ETF     PCHI

NaN tickers for these assets: 0
```

`PATHFINDER DISCIPLINED US EQUITIES ETF` (BD alternate spelling) not present in parquet for
this date range — not an error, simply no BD transactions observed under that spelling.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/silver/build_canonical_prices_v2.py` | `_OPAL_ETF_OVERRIDES` added, injected in `load_ticker_lookup()` | Yes — `b69d1ae6` |
| `data/black_diamond/scripts/silver/bd_price_update.py` | Same addition | Yes — `b69d1ae6` |

---

## Current State

**Status:** COMPLETE

`canonical_prices.parquet` rebuilt on S3 with correct tickers for all Opal/Pathfinder ETFs.
Both the monthly full-rebuild path and the daily incremental path carry the override — fix
will not regress. No data was removed; for the Opal ETFs, some previously-interpolated price
values may now be real Yahoo Finance closes.

Downstream propagation (`holdings_lots`, `client_tax_liability`, portal blank tickers) will
resolve automatically on the next gold layer incremental run — no further action needed.

---

## Next Steps

1. **[nightly pipeline]** Next gold incremental: `03_build_holdings_lots.py` picks up corrected
   tickers and Yahoo prices from canonical_prices — propagates to `client_tax_liability` and portal.
2. No further AE action required for this fix.

**Do NOT:**
- Re-run the full rebuild unless canonical_prices.parquet drifts — current parquet is correct as of 2026-03-18T15:57 UTC
