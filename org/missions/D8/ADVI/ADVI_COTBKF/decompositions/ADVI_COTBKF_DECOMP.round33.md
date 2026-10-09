# ADVI_COTBKF decomposition -- ROUND 33 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~10:0xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 8 @bff4e48547 (msg 3060), the price-basis ruling.
- Valuation is at the AS-TRADED close: unadjusted for dividends, adjusted for splits only.
- Dividends and distributions enter ONLY as cash.

Round 33's enrichment list:
1. A read-only census of the price store: adjusted vs as-traded per ticker, with vintage and denominator.
2. A rebuild on the as-traded basis of any served table built on adjusted prices, under a never-widen pair. Until it lands, the affected
   rows carry `price_basis: dividend_adjusted (known wrong; rebuild owed)`.
3. Re-read SCHB after the rebuild.

**Rule 24.** Domain: three items.
- Item 1 is cell `CB-ag-1`, cut now.
- Items 2 and 3 depend on item 1's per-ticker classes and its count of served rows that rest on adjusted prices. They are cut on its
  result as `CB-ag-2` (the price-basis input and chain change) and `CB-ag-3` (the marking, then the rebuild, under a pair, on
  `0.7.0_AE_CloudOps~CB2`). SCHB is re-read inside `CB-ag-3`'s real run.

## Measured constraints (issuer reads ~09:5xZ-10:0xZ)

1. The chain's one price store is `s3://opal-data-cot/silver/prices/canonical_prices.parquet`
   (`commonwealth_price_census` STORES[0], read by `commonwealth_daily_valuation`). It holds:
   - 11,291,021 rows and 4,003 tickers, dated 2006-01-02 to 2026-06-09;
   - columns `date, asset_name, ticker, price, source`.
2. Source labels, rows (tickers):

   | label | rows | tickers |
   |---|---|---|
   | `linear_interpolation` | 7,831,140 | 3,994 |
   | `yahoo_finance` | 3,396,067 | 3,580 |
   | `transaction_observed` | 50,143 | 567 |
   | `scoped_override` | 12,042 | 6 |
   | `bd_txn_price` | 1,623 | 3 |
   | `transaction_observed_capped` | 6 | 0 |

   69% of rows are interpolated between source points, so an adjusted basis at the points carries into the interpolated days.
3. Row D2-S48: `bd_txn_price` provenance is unread (cross-firm law). It is folded into `CB-ag-1`.
4. The served FWD-3 tables (@476f970245; 0 readers): `daily_returns` 1,691,729 rows, `account_day_value` 21,102,041 rows, and
   `month_grades` 82,593 rows, all priced from this store.
5. Yahoo is the source of record. yfinance 1.2.0 works on dell2. Andrew's gentleness word (2026-10-08, ~C2 record @489e1cd24c)
   applies: batched downloads, paced, one pass, with the call count printed.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ag-1` | read-only census of the store's price basis per ticker, vintage, denominator; the served rows resting on adjusted prices; `bd_txn_price` provenance | FWD-3 | WORLD | none | `0.9.0_WK_ADVI_COTBKF~60` |

**Fan-out:** `1 of 1 chains, cap 8`.
