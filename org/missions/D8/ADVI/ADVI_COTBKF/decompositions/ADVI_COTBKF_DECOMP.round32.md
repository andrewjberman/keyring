# ADVI_COTBKF decomposition -- ROUND 32 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~09:4xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 7 @2a140ad0bb (msg 3005).
- D2-S45 is CLOSED on branch A, and FWD-3 is REALIZED except the 4 ABSENT months.
- Round 32 is one read-only cell for W58-S1: which base date and price source the chain uses for SCHB (808524102) and SCHZ (808524839),
  against the Yahoo as-traded series.
- Nothing served moves. A wrong base is repaired under a pair. An adjusted-close base is named, and the methodology is ruled on, not
  patched.

**Rule 24.** Domain: one item, one cell.

## Measured constraints

1. Round 31 evidence: `s3://opal-data-assets/commonwealth/cottonwood/silver/price_evidence/date=2022-10-12/part-00000.parquet`.
   - Yahoo split-adjusted Close: SCHB 13.98, SCHZ 22.465.
   - The chain's close (r26, before split scaling): 13.3302 and 19.7181, which is 0.954 and 0.878 of Yahoo's.
2. The chain's price path is `data/assets/scripts/silver/commonwealth_daily_valuation.py`: `load_price_store` :133, `read_sechist`
   :152 (field names `_SECHIST_PRICE` :147), `resolve_series` :187, `security_day_prices` :207.
3. **Candidate (issuer, INFERRED, untested):** a dividend-adjusted base (Yahoo `Adj Close`, or a total-return series) understates an
   old close by roughly the dividends paid since. That is about 4 years of yield on a bond ETF (SCHZ) vs a broad equity ETF (SCHB),
   which has the shape of 12% vs 5%. The cell tests it; the order states it only as one candidate class.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-af-1` | read-only trace of the chain's base close for SCHB and SCHZ: source, series, field, and the cause of the gap | FWD-3 | WORLD | none | `0.9.0_WK_ADVI_COTBKF~59` |

**Fan-out:** `1 of 1 chains, cap 8`. A repair cell (under a pair) or a methodology ruling follows on the class.
