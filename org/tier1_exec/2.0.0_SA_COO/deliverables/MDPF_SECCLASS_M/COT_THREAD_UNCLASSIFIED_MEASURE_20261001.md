# MDPF_SECCLASS, the Cottonwood thread -- what turns unclassified, in dollars (CTO rulings batch 86 item 6)

By `2.0.0_SA_COO~M`, 2026-10-01 13:0xZ. Read-only. Input: `s3://opal-data-cot/gold/canonical/holdings/2026-09-30.parquet`
(the newest of 127 partitions, written 2026-10-01 11:35Z; the prefix Cottonwood's `C_06` reads), positions with a
positive market value: 13,063 rows, **554,618,741.24 USD**. The canonical table: 2,671 rows (scan, 13:0xZ).
Script: scratch (`cot_unclassified_measure.py`); the numbers below are firm-level, and the names are security names.

## The served mix today is a guess

The Cottonwood gold host role cannot read either classification table (0 DynamoDB statements on
`cot-exporter-ec2-role`, re-read 12:4xZ), so the old library runs on empty maps: a name pattern, else "equity".

| class | served today (the guess) | canonical table only |
|---|---|---|
| equity | 477,064,587.23 (86.0%) | 191,742,563.24 (34.6%) |
| fixed_income | 75,183,089.19 (13.6%) | 136,321,046.93 (24.6%) |
| alternatives | 2,371,064.82 (0.4%) | 102,984.87 (0.0%) |
| commodities | -- | 17,690,668.26 (3.2%) |
| structured | -- | 3,681,352.72 (0.7%) |
| unclassified | -- | **205,080,125.21 (37.0%)** |

## The 205.1 million, in two parts

**1. No ticker at all: 101,279,735.09 USD, 318 names.** A ticker-keyed table cannot answer these. The largest: Voya
(25,973,104.32), "Investor Manual Asset - Home" (8,378,664.00), four "CCA ... Opportunity LP Capital Values" lines
(20,178,309.87 together), "Investor Manual Asset - Limited Liability Company" (4,125,000.00), "Investor Manual Asset -
Trust Accounts" (3,173,684.09). These are held-away, manual and private holdings. Cottonwood's mix already has a class
for them, `other` ("personal and held-away assets", `C_06` `MIX_ASSET_CLASSES`); which of them the callers' rule sends
there, and which stay unclassified, is the callers' cell and is stated in the half.

**2. A ticker the table lacks: 103,800,390.12 USD, 271 tickers.** It is concentrated: the top 10 carry 67.4%
(69,960,103.40), the top 25 carry 84.3% (87,499,630.96), the top 50 carry 91.3%, the top 100 carry 96.5%.

| # | ticker | USD | custody name |
|---|---|---|---|
| 1 | FCASH | 16,707,383.22 | FCASH (Fidelity cash) |
| 2 | MEAR | 10,581,165.63 | iShares Short Maturity Municipal Bond Active ETF |
| 3 | EVSM | 10,233,194.76 | Eaton Vance Short Duration Municipal Income ETF |
| 4 | MFEIX | 10,167,835.89 | MFS Growth I |
| 5 | FSPGX | 6,554,697.56 | Fidelity Large Cap Growth Idx |
| 6 | FLCOX | 6,265,401.10 | Fidelity Large Cap Value Index |
| 7 | FIGXX | 2,770,755.48 | Fidelity Colchester Str Tr Mny Mrkt Fds I |
| 8 | PSLV | 2,512,405.22 | Sprott Physical Silver |
| 9 | EIHYX | 2,141,564.80 | Eaton Vance High-Yield Municipal Inc I |
| 10 | SPYI | 2,025,699.74 | NEOS S&P 500 High Income ETF |
| 11 | PAAA | 2,016,824.51 | PGIM AAA CLO ETF |
| 12 | FPNIX | 1,893,971.98 | FPA New Income - Institutional |
| 13 | PRTMX | 1,742,145.52 | T. Rowe Price Intermediate Muncpl Bd I |
| 14 | CDSIX | 1,440,536.68 | Calvert Short Duration Income I |
| 15 | VMLUX | 1,382,001.51 | Vanguard Ltd-Term Tx-Ex Adm |
| 16 | BRK.B | 1,217,082.20 | Berkshire Hathaway Inc Del Cl B New |
| 17 | SBR | 1,100,383.95 | Sabine Rty Tr Unit Ben Int |
| 18 | FTHSX | 1,078,652.24 | FullerThaler Behavioral Sm-Cp Eq Inst |
| 19 | EIBIX | 1,039,948.24 | Eaton Vance Income Fund of Boston I |
| 20 | PFMIX | 998,225.70 | PIMCO Municipal Bond Instl |
| 21 | JBALX | 962,189.34 | Janus Henderson Balanced I |
| 22 | FSSZX | 814,324.68 | Fidelity Advisor Stock Selector Sm Cp Z |
| 23 | BRK.A | 747,005.00 | Berkshire Hathaway Inc Del Cl A |
| 24 | LMCSP5 | 633,810.74 | LMCSP5 (not a public symbol) |
| 25 | LMCMBI | 472,425.27 | LMCMBI (not a public symbol) |

## What the ruling asks next (item 6)

The rows for the tickers carrying most of those dollars are written FIRST, under today's rules: a seed row with its
ground named (the CEMIX form), or a model row with a seed peer. From the table: 23 of the top 25 are public funds or
stocks whose custody name states what they are; two (LMCSP5, LMCMBI) are not public symbols and stay unclassified. The
half for the re-point then names the residue it accepts.

Not measured here: the same tickers at 49 Financial and Inflection (a canonical row is cross-firm, so each row's own
half states its move on the Holdings tab and on Black Diamond gold); Cottonwood's `D_03` and `D_04`, which classify the
same holdings through the same library.

## ADDED 13:5xZ -- the no-ticker 101.3 million by name shape, and what was done about the ticker part

**The no-ticker part is not one thing** (491 rows; the shape is read from the custody name by this record only, to
size the residue -- it is NOT a rule any code applies):

| name shape | supervision | rows | USD | how gold serves it today |
|---|---|---|---|---|
| other names (the largest: Voya) | Supervised | 12 | 28,721,603.18 | equity (the "else equity" guess) |
| an individual bond or note (coupon, maturity) | Supervised | 280 | 25,503,844.13 | fixed_income (the name pattern) |
| private fund or partnership wording | Supervised | 82 | 21,201,663.80 | equity (the guess) |
| "Investor Manual Asset - ..." | Unsupervised | 51 | 20,020,398.35 | equity (the guess) |
| other names | Unsupervised | 54 | 5,433,995.39 | equity (the guess) |
| an individual bond or note | Unsupervised | 11 | 398,205.38 | fixed_income |
| cash wording | Unsupervised | 1 | 24.86 | fixed_income |

Three facts the half for the re-point must carry:

1. **A ticker-keyed table cannot answer any of this.** Cottonwood's gold positions carry no CUSIP column, so the 348
   CUSIP-keyed rows of the canonical table are unreachable from here too.
2. **About 25.9 million of it is served RIGHT today** (individual bonds as fixed_income, by the name pattern the ruling
   retires). Under shape (a) those bonds read unclassified. That is a served class that gets worse, and it is the one
   place where "no name pattern" costs accuracy rather than a guess.
3. **The knowledge for the rest was already written once, to the wrong table for this purpose.** The 941 rows of
   `bd-securities-cot-new-p1-m-20260926` class Cottonwood names (held-away and manual assets as `other`, cash as `cash`)
   in `bd-securities`, which Cottonwood's host never could read and which shape (a) never reads. `other` and `cash` are
   classes of Cottonwood's mix (`C_06` `MIX_ASSET_CLASSES`) and are not classes of the canonical table (its five:
   equity, fixed_income, structured, commodities, alternatives; cash is fixed_income / Cash).

**The ticker part:** 21 seed rows were drafted for the largest tickers, each following a seed peer of its own kind
(branch `coo-m-cot-seed-rows` @7612ad62d5, NOT on CLOUD: a seed run from CLOUD would write them; the dry run against the
live table reads 21 to write of 160, 0 conflicts). **Two of the 21 are WITHDRAWN, FCASH and FIGXX**, on what the
Holdings tab serves today (three local builds, 13:4xZ):

- FCASH is served **cash / Money Market** today, by the bd-securities fallback: 133 nodes and 9,198,812.25 USD at
  Cottonwood, 187 nodes and 1,453,523.02 USD at Inflection. The canonical table has no cash class; its one cash row,
  the seed row CASH_USD, reads fixed_income / Cash. A canonical FCASH row in that form would move 10.65 million USD
  from Cash to Fixed Income on a served page, the opposite of what row IRPT_BCKEND-W41-S1 asks. Whether the table
  gains a `cash` class or its readers fold fixed_income / Cash to cash is a contract question for `1.0.0_SA_CTO`.
- The other 19 carry 64,852,682.96 of the 103,800,390.12 USD (62.5%). What they move on the Holdings tab: at
  Cottonwood a CLASS on 15,328,982.38 USD (EVSM equity to fixed_income, 10,216,541.88, a guess corrected; PSLV
  alternatives to commodities, 2,440,594.86; SPYI alternatives to structured, 2,671,845.64) and a SUB CLASS on
  15,124,299.01 USD (MEAR, VMLUX, FPNIX, EIBIX); at 49 Financial a class on 168,658.74 USD (PSLV, SPYI); at
  Inflection nothing with a value. On Black Diamond gold lots: SPYI, PSLV and FPNIX, 18 lots, 164,063.07 USD, from
  `other` to a class. Twelve of the 19 keep class and sub class at Cottonwood (38,496,339.35 USD: the fallback's table
  layer already answers them the same), so only the source of the answer changes.
- FIGXX is served fixed_income / Cash today (6 nodes, 2,737,377.41 USD at Cottonwood) and would not move; it is held
  with FCASH so that cash is ruled once.
