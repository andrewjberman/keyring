# Opal ETF Ticker Fix — canonical_prices Full Rebuild — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-18
**Start Time:** 15:45 UTC
**End Time:** 15:58 UTC

## Objective

Deploy the `_OPAL_ETF_OVERRIDES` ticker fix to both silver price-building scripts and run a full
rebuild of `canonical_prices.parquet` so that Opal/Pathfinder-branded ETFs no longer carry
`ticker=NaN` through the pipeline into portal position lists.

---

## Root Cause

`config/ticker_lookup.json` (built from bulk BD transaction data) never receives a `ticker` field
for Opal/Pathfinder-branded ETFs — Black Diamond stores them only by their long fund names. This
propagated `ticker=NaN` through the entire silver→gold→portal chain:

```
canonical_prices.parquet  (ticker=NaN)
  → holdings_lots.parquet  (ticker=NaN, from latest-price join)
    → client_tax_liability.parquet  (ticker=NaN)
      → portal position lists  (blank ticker shown)
```

Secondary impact: with `ticker=NaN`, the T2 Yahoo Finance price fetch had no symbol to query,
forcing these assets onto T1 transaction-observed prices only — any day without a BD transaction
was filled by interpolation/carry-forward rather than real market closes.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Verify DS changes uncommitted in working tree | Both scripts had local modifications |
| 2 | Commit silver scripts to CLOUD | `b69d1ae6` — authored `0.4.0_DS_ClientPlatform` |
| 3 | Upload to `s3://opal-data-bd/code/silver/` | Both files uploaded |
| 4 | Send SSM: `build_canonical_prices_v2.py` full rebuild | Command `11a9621a` — Success |
| 5 | Spot-check canonical_prices.parquet | 6/6 Opal ETF names now have correct tickers, 0 NaN |

---

## What Was Fixed

`_OPAL_ETF_OVERRIDES` dict added to both scripts and injected via `mapping.update()` after
`ticker_lookup.json` is loaded from S3:

| BD Asset Name | Ticker | Notes |
|---|---|---|
| OPAL DIVIDEND INCOME ETF | DIVZ | Current brand name |
| POLEN DIVIDEND INCOME ETF | DIVZ | Filing/legacy name pre-rebrand |
| OPAL INTERNATIONAL DIVIDEND INCOME ETF | IDVZ | |
| PATHFINDER DISCIPLINED US EQUITY ETF | PFDE | BD standard spelling |
| PATHFINDER DISCIPLINED US EQUITIES ETF | PFDE | BD alternate spelling |
| PATHFINDER FOCUSED OPPORTUNITIES ETF | PFOE | |
| POLEN HIGH INCOME ETF | PCHI | Same pattern, included proactively |

Both the monthly full-rebuild path (`build_canonical_prices_v2.py`) and the daily incremental
path (`bd_price_update.py`) were updated so the fix persists through future runs.

---

## Rebuild Output

```
Total rows:    10,406,355
Date range:    2020-06-30 -> 2026-03-16
Unique assets: 9,952
Size:          91.3 MB -> s3://opal-data-bd/silver/prices/canonical_prices.parquet
Elapsed:       114s

By source:
  linear_interpolation   8,561,465  (82.3%)
  yahoo_finance          1,651,217  (15.9%)
  transaction_observed     193,673  ( 1.9%)
```

## Spot-Check Result

```
                        asset_name  ticker
          OPAL DIVIDEND INCOME ETF    DIVZ
OPAL INTERNATIONAL DIVIDEND INCOME ETF    IDVZ
  PATHFINDER DISCIPLINED US EQUITY ETF    PFDE
  PATHFINDER FOCUSED OPPORTUNITIES ETF    PFOE
         POLEN DIVIDEND INCOME ETF    DIVZ
             POLEN HIGH INCOME ETF    PCHI

NaN tickers for these assets: 0
```

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/silver/build_canonical_prices_v2.py` | Added `_OPAL_ETF_OVERRIDES`, injected in `load_ticker_lookup()` | Yes — `b69d1ae6` |
| `data/black_diamond/scripts/silver/bd_price_update.py` | Same addition | Yes — `b69d1ae6` |

---

## Current State

**Status:** COMPLETE

`canonical_prices.parquet` is rebuilt and on S3 with correct tickers for all 6 observed Opal/Pathfinder
ETF name variants. The next gold layer run (incremental or full) will propagate the corrected tickers
downstream: `03_build_holdings_lots.py` picks the latest canonical_prices row per asset, so
`holdings_lots → client_tax_liability → portal` will be correct after the next pipeline run.

---

## Next Steps

1. **[nightly pipeline]** Next gold layer incremental will propagate ticker fix to `holdings_lots.parquet`
   and `client_tax_liability.parquet` automatically — no further action needed.
2. **[0.4.0_DS_ClientPlatform]** Monitor next portal build to confirm blank ticker is resolved in
   position lists.

**Do NOT:**
- Run `build_canonical_prices_v2.py --dry-run` expecting it to write to S3 — dry-run skips all writes
- Re-run the full rebuild unless canonical_prices.parquet drifts — the current parquet is correct as of 2026-03-18T15:57 UTC
