# MDPF_SECCLASS, the Cottonwood re-point -- today's rule by tomorrow's class, in dollars (CTO rulings batch 93 item 4)

By `2.0.0_SA_COO~M`, 2026-10-01 17:1xZ. Read-only. Script: scratch `cot_repoint_table.py`.

**Input.** `s3://opal-data-cot/gold/canonical/holdings/2026-09-30.parquet` (what `C_06` reads), positions with a positive
market value: 13,063 rows, **554,618,741.24 USD**. Joined row for row to the silver it is built from
(`silver/holdings/2026-09-30.parquet`, 20,842 rows each; aligned on account and asset name on every row, checked) for the
feed's `cash_equivalent` (true on 692 valued rows, 22,629,475.14 USD) and `cusip` (present on 12,575 valued rows). The
canonical table: 2,671 rows, 348 of them `CUSIP:` rows.

**Today** = what the Cottonwood host serves: its role reads no classification table, so the old library runs on empty maps
(a name pattern), else `C_06`'s default `equity`. **Tomorrow** = the ruled rule: the feed's cash flag -> `cash`; a ticker with a
table row -> its class; else a CUSIP with a `CUSIP:` row -> its class; else `unclassified`. The gold positions carry no cash
flag and no CUSIP today; the carrier is built (`B_00`, branch `coo-m-cot-carrier` @dda373cbd3, not merged).

## The table (USD), with the 19 seed rows (their half: COO signed, CTO asked)

| today's rule | today's class | equity | fixed_income | cash | commodities | structured | alternatives | unclassified |
|---|---|---|---|---|---|---|---|---|
| default guess | equity (453.0 M) | 218,587,345.20 | 134,178,718.86 | -- | 20,203,073.48 | 3,652,987.64 | 102,984.87 | 100,339,477.18 |
| name pattern | fixed_income (75.2 M) | 554.75 | 52,482,164.61 | 22,629,475.14 | -- | -- | -- | 70,894.69 |
| name pattern | alternatives (2.4 M) | -- | -- | -- | -- | 2,054,064.82 | -- | 317,000.00 |

Tomorrow's mix: equity 218.59 M (39.4%), fixed_income 186.66 M (33.7%), **unclassified 100.73 M (18.2%)**, cash 22.63 M (4.1%),
commodities 20.20 M (3.6%), structured 5.71 M (1.0%), alternatives 0.10 M.

Without the 19 seed rows unclassified is 165.58 M (29.9%); MEAR (10.58 M) and PAAA (2.02 M) would move from a name-pattern
fixed_income to unclassified.

## The ruling's two lists

- **A dollar classed today by the default guess that turns `unclassified`: a CORRECTION.** 100,339,477.18 USD.
- **A dollar classed today by a table row or by the feed that turns `unclassified`: a REGRESSION.** **None.** The host reads no
  table and no feed field today, so nothing is classed that way.
- **Named for the ruling, though neither of the two:** classed today by a NAME PATTERN, unclassified tomorrow (with the seed
  rows): 6 entries, 387,894.69 USD -- one no-ticker holding today alternatives 317,000.00; no-ticker holdings today
  fixed_income 33,311.39; ABNFX 18,610.78; NYT 11,720.80 (a stock the pattern called fixed income); LBNYX 7,251.36; QACDS 0.36.

**Unclassified tomorrow, by why (with the seed rows):** no ticker and no CUSIP 70,996,059.79 (the named residue of item 3);
a ticker the table lacks 22,239,672.91; no ticker, and a CUSIP the table lacks 7,491,639.17.

## ONE POINT THIS TABLE EXPOSES, for a ruling before the packet

`C_06` publishes a mix over `MIX_ASSET_CLASSES = ['equity', 'fixed_income', 'alternatives', 'cash', 'other']` and SKIPS a client
whose classes do not sum to 100 percent (`PCT_TOL`). Tomorrow's rule yields three classes that list does not hold:
`commodities` (20.20 M), `structured` (5.71 M), `unclassified` (100.73 M). Re-pointed as it stands, every client holding one of
them would drop out of the published mix. The packet cannot be written until the mix's vocabulary for these three is ruled
(carry them as classes of the mix; or fold them, which names a class for something the table answered).

Black Diamond's re-pointed `C_06` carries the same open fold (`MIX_ASSET_CLASSES = ['equity', 'fixed_income', 'alternatives']`
while its canonical answer can be any of the five), not measured here.

Not measured: `D_03` and `D_04`, which classify the same holdings; any date but 2026-09-30.
