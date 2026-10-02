# MDPF_SECCLASS BD forward fix -- what r3 plus fix 1 would serve for 49 Financial, measured (2026-10-02 10:3xZ)

By `2.0.0_SA_COO~M`. Read-only. For `1.0.0_SA_CTO` (batch 117 item 4; tick 6, msg 104138). Fix 1 is built on branch
`coo-m-bd-mix-classes` @0ce0ad6efd; fixes 2 and 3 are packets awaiting the CTO half (@f227938dfd).

## Method

`s3://opal-data-bd/gold/canonical/holdings/2026-09-30.parquet` (what C_06 reads; 113,763 rows, 113,579 with a positive market
value, 1,866,381,354.90 USD), classified by CLOUD's r3 `C_06.classify_series` against the live table (2,719 rows), with fix 1's
one rename applied (`other` -> `unclassified`). Every class that results is in fix 1's eight-class list: **no ticker leaves the
mix.** The served 09-30 firm mix today (old library, restored 08:0xZ): equity 76.86 / fixed_income 21.03 / alternatives 2.11 pct.

## Tomorrow's 49 Financial mix (09-30 positions)

| class | USD | pct | positions |
|---|---|---|---|
| equity | 1,108,089,280.05 | 59.37 | 56,088 |
| **unclassified** | **443,791,300.09** | **23.78** | 26,569 |
| fixed_income | 289,244,385.36 | 15.50 | 25,852 |
| structured | 18,879,281.51 | 1.01 | 4,666 |
| cash | 5,609,674.42 | 0.30 | 370 |
| commodities | 697,864.61 | 0.04 | 25 |
| alternatives | 69,568.86 | 0.00 | 9 |

## The unclassified 443.8 M is mostly positions with NO TICKER

- With a ticker: 10,694,121.37 USD in 148 tickers (fix 2's population, after the rows the table now has).
- **With no ticker: 433,097,178.71 USD in 1,956 distinct names** -- and they are ordinary ETFs whose ticker is blank on the
  canonical holdings row: VANGUARD MORNINGSTAR GROWTH ETF 35.78 M (5,096 positions), ISHARES CORE MSCI EAFE ETF 31.52 M, POLEN
  DIVIDEND INCOME ETF 28.94 M, OPAL INTERNATIONAL DIVIDEND INCOME ETF 24.43 M, PATHFINDER DISCIPLINED US EQUITY ETF 24.43 M,
  STATE STREET SPDR PORTFOLIO S&P 500 ETF 19.73 M, ISHARES CORE S&P MID-CAP ETF 13.10 M ... By name shape: 329.1 M plain security
  names, 59.7 M fund/pool/strategy names, 44.3 M bond/CD-like names, 0.0 M cash-like.
- Today's library classes these by NAME through bd-securities' NAME:: aliases (row MDPF_SECCLASS-S7); r3's canonical-only rule
  does not, so they read unclassified.

## What this means for the re-land

Fixes 1-3 meet batch 117 item 4 as written (no ticker leaves the mix; the 290's rows). But a re-land on them serves 49 Financial
a mix about one quarter `unclassified` where today it reads fully classed -- the dollars are ETFs the table already has rows for
(IEFA, SPYM, IJH, VGIT/BIV ...), missing only the ticker on the holdings row. The open question is an IDENTITY one, not a class:
a holdings row whose name identifies a security the table holds, with its ticker blank. Batch 93's "never a name" ruled out a
name as evidence of CLASS; whether a name may resolve a TICKER (an exact match on a name the security's own row carries, the
seed module's `ASSET_NAME_TO_TICKER`, or E_18's resolution table) is not ruled. Measured gap, not decided here.

Not measured: Inflection; the per-advisor split; which share of the 1,956 names an exact-name resolution would cover.

## ADDENDUM 1 (10:5xZ) -- batch 144's identity resolution, measured before it is built

Batch 144: a blank ticker resolves by identity only -- CUSIP first, then an exact normalized name through E_18's resolution table
(`s3://opal-data-bd/gold/dimensions/ticker_resolution.parquet`, 4,424 names, last written 2026-04-07), `ASSET_NAME_TO_TICKER`
second; never bd-securities NAME:: aliases; an ambiguous match resolves nothing; the resolution lives in the classifier's read.
Measured on the same 09-30 positions (normalization `' '.join(name.lower().split())`, as E_18's `_normalize_asset_name`):

| outcome | USD |
|---|---|
| name resolves in the table to ONE ticker that has a canonical row | 324,054,999.20 |
| name resolves to more than one ticker (ambiguous) | 0.00 |
| name resolves only through `ASSET_NAME_TO_TICKER` | 0.00 |
| name resolves to a ticker with no canonical row | 3,797,653.15 |
| no resolution | 110,835,132.38 |

49 Financial's unclassified: **23.78 pct -> 6.42 pct** (443.79 M -> 119.74 M of 1,866.38 M), before the rows written today (fix 2's
67 and fix 3's 3 were written after this file's first measure). CUSIP-first has no input in C_06: Black Diamond's canonical holdings
carry no `cusip` column (D_03 and D_04 read `holdings_lots`, which does). **The 5.0 pct bar is not met by name resolution alone.**
Largest unresolved names: VANGUARD MORNINGSTAR GROWTH ETF 35,784,713; SCHWAB CHARLES FAMILY FUND PRIME ADV ULTRA 10,000,000 (a money
market fund); WALDROP DONOR ADVISED FUND 5,842,785; EXXONMOBIL HOLDINGS CORP COM SHS 3,354,779; JPMORGAN CHASE FINL CO LLC 0%
02/14/2029 3,060,000 (a structured note); VANGUARD MORNINGSTAR TOTAL STOCK MARKET ETF 2,926,219; VANGUARD MORNINGSTAR VALUE ETF
2,691,122; CLIFFWATER CORPORATE LENDING I 2,608,883; VANGUARD MORN TOTAL STK MKT IDX ADMIRAL 2,444,559; 6 YEAR SHIELD 25 S&P 500
INDEX 2,341,992. The resolution table is six months old: the Vanguard Morningstar funds (about 44 M) are newer than it.
