# Never-widen half, MDPF_SECCLASS Cottonwood thread -- 19 new canonical seed rows for Cottonwood's largest uncovered tickers

**Author:** `2.0.0_SA_COO~M`, 2026-10-01 16:0xZ (FAST lease `MDPF_SECCLASS`). **For:** `1.0.0_SA_CTO` to sign the second half.
**Authority:** CTO rulings batch 86 item 6 (the rows for the tickers carrying most of the dollars are written first),
batch 90 item 2 ("the 19 seed rows ... go ahead meanwhile, each with its ground, under their own half") and batch 93 item 1
(no cash seed row; withdrawing FCASH and FIGXX stands), `RULINGS.md` @9559ce8891.
**Status of the act: NOT RUN.** The code is on branch `coo-m-cot-seed-rows` @`15a9717715`, NOT on CLOUD; the table is not
written (read 15:2xZ: 2,671 rows; MEAR, EVSM, BRK.A, PSLV, SPYI, MFEIX absent by consistent `get-item`).

## The act, in two steps

1. **Merge** `15a9717715` into CLOUD (`.tools/safe-merge.sh`), after both halves are signed. The commit touches two files:
   the seed source `infra/aws/lambda/v2_portal/_shared/etf_classification.py` (114 lines added, none changed) and one test.
2. **Run** `python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` (no flag) once, by this seat, from
   the laptop at CLOUD, with the seed source at blob `7a0623a7de` and the seed script at blob `d48358a5cc`.

| | value |
|---|---|
| items written | 19 new items, each `classified_by: seed`, `updated_by: seed-script`, with `asset_class`, `sub_asset_class`, `management_style`, `sector`, `name`, `instrument_kind` (table below) |
| every other row | untouched. `--dry-run` against the live table, 15:24Z, from the branch: 158 tickers in the module, 139 already correct and skipped, **19 to write**, 0 CONFLICT lines, 1 preserved field (VNQ `management_style`, the table's value stands) |
| stops before the write | (a) the seed source blob at CLOUD after the merge is not `7a0623a7de` (another seat edited the file): stop, re-read, re-sign; (b) the pre-run `--dry-run` reads anything other than "rows to write: 19 of 158" naming these 19, or any CONFLICT line |
| writers of this table | 5 by the contract's `classified_by` values (`seed`, `scheduled`, `constituents`, `legacy`, `model`); this act is the seed path only |

## The 19 rows, each with its ground

The ground of every row is the same two facts: **the custody name Cottonwood's own feed carries for the ticker**
(`s3://opal-data-cot/gold/canonical/holdings/2026-09-30.parquet`), and **a seed row of the same kind already in the
table** (the peer, read live 15:5xZ, every one `classified_by: seed`). The new row takes the peer's class and sub class;
the test `R7_CHECKS/test_seed_cot_top_tickers.py` (22 passed) reads each peer from the module and fails if a peer moves.
**The claim is INFERRED from the name and the fund's public category. No vendor was called.**

| ticker | ground: Cottonwood's custody name | USD on Cottonwood gold | row | seed peer | Holdings tab today, per firm | effect |
|---|---|---|---|---|---|---|
| MEAR | iShares Short Maturity Municipal Bond Active ETF | 10,581,165.63 | fixed_income / Short Duration | VTES | Cottonwood fixed_income / Municipal (2 nodes, 10,416,554.07 USD); Inflection fixed_income / Municipal (1 node, 0.00 USD) | sub class moves |
| EVSM | Eaton Vance Short Duration Municipal Income ETF | 10,233,194.76 | fixed_income / Short Duration | VTES | Cottonwood equity / none (1 node, 10,216,541.88 USD) | CLASS moves |
| VMLUX | Vanguard Ltd-Term Tx-Ex Adm | 1,382,001.51 | fixed_income / Short Duration | VTES | Cottonwood fixed_income / Municipal (12 nodes, 1,461,619.65 USD) | sub class moves |
| CDSIX | Calvert Short Duration Income I | 1,440,536.68 | fixed_income / Short Duration | VCSH | Cottonwood fixed_income / Short Duration (69 nodes, 1,622,707.92 USD) | no move |
| FPNIX | FPA New Income - Institutional | 1,893,971.98 | fixed_income / Short Duration | VCSH | Cottonwood fixed_income / Investment Grade (71 nodes, 2,110,434.58 USD); Inflection the same (1 node, 0.00 USD) | sub class moves |
| PRTMX | T. Rowe Price Intermediate Muncpl Bd I | 1,742,145.52 | fixed_income / Municipal | MUB | Cottonwood fixed_income / Municipal (13 nodes, 1,874,077.21 USD) | no move |
| PFMIX | PIMCO Municipal Bond Instl | 998,225.70 | fixed_income / Municipal | MUB | Cottonwood fixed_income / Municipal (11 nodes, 1,095,338.04 USD); Inflection the same (1 node, 0.00 USD) | no move |
| EIHYX | Eaton Vance High-Yield Municipal Inc I | 2,141,564.80 | fixed_income / Municipal | MUB | Cottonwood fixed_income / Municipal (19 nodes, 2,183,343.79 USD) | no move |
| PAAA | PGIM AAA CLO ETF | 2,016,824.51 | fixed_income / Structured Credit | JAAA | Cottonwood fixed_income / Structured Credit (15 nodes, 1,814,221.43 USD) | no move |
| EIBIX | Eaton Vance Income Fund of Boston I | 1,039,948.24 | fixed_income / High Yield | HYG | Cottonwood fixed_income / Intermediate (71 nodes, 1,135,690.71 USD); Inflection the same (1 node, 0.00 USD) | sub class moves |
| MFEIX | MFS Growth I | 10,167,835.89 | equity / US Large Cap | IVV | Cottonwood equity / US Large Cap (98 nodes, 10,549,861.95 USD) | no move |
| FSPGX | Fidelity Large Cap Growth Idx | 6,554,697.56 | equity / US Large Cap | IVV | Cottonwood equity / US Large Cap (112 nodes, 7,642,910.52 USD) | no move |
| FLCOX | Fidelity Large Cap Value Index | 6,265,401.10 | equity / US Large Cap | IVV | Cottonwood equity / US Large Cap (112 nodes, 7,722,156.02 USD) | no move |
| FTHSX | FullerThaler Behavioral Sm-Cp Eq Inst | 1,078,652.24 | equity / US Small Cap | IJR | Cottonwood equity / US Small Cap (15 nodes, 335,999.63 USD) | no move |
| FSSZX | Fidelity Advisor Stock Selector Sm Cp Z | 814,324.68 | equity / US Small Cap | IJR | Cottonwood equity / US Small Cap (84 nodes, 1,718,802.83 USD) | no move |
| PSLV | Sprott Physical Silver | 2,512,405.22 | commodities / Metals | SLV | 49 Financial alternatives / Silver (1 node, 68,221.22 USD); Cottonwood alternatives / Silver (9 nodes, 2,440,594.86 USD) | CLASS moves |
| SPYI | NEOS S&P 500 High Income ETF | 2,025,699.74 | structured / Options Income | JEPI | 49 Financial alternatives / Structured Notes (4 nodes, 100,437.52 USD); Cottonwood alternatives / Structured Notes (19 nodes, 2,671,845.64 USD) | CLASS moves |
| BRK.B | Berkshire Hathaway Inc Del Cl B New | 1,217,082.20 | equity / US Large Cap, single_security | WMT | Cottonwood equity / US Large Cap (9 nodes, 1,183,552.14 USD) | no move |
| BRK.A | Berkshire Hathaway Inc Del Cl A | 747,005.00 | equity / US Large Cap, single_security | WMT | Cottonwood equity / US Large Cap (1 node, 753,367.87 USD) | no move |

Total on Cottonwood gold: 64,852,682.96 of the 103,800,390.12 USD in tickers the table lacks (62.5 percent). The "Holdings
tab today" column is three local builds of `holdings_snapshot.py` (2026-10-01 13:4xZ, business date 2026-09-29, actual
positions); the dollars differ from the gold column because the two sources are a day apart and cover different accounts.

**Four choices a reader should not have to find:**

- **Short-duration municipal funds follow VTES (Short Duration), not MUB (Municipal).** MEAR, EVSM and VMLUX are
  municipal by issuer and short by maturity; the table holds both sub classes and its seed row for the nearest fund
  (VTES, a short-term tax-exempt ETF) reads Short Duration. The fallback serves MEAR and VMLUX as Municipal today. If
  the issuer should win, the three rows read Municipal and nothing moves for two of them.
- **FPNIX leaves Investment Grade for Short Duration** (peer VCSH) and **EIBIX leaves Intermediate for High Yield**
  (peer HYG): each follows what the fund is by its own name and category, against what the fallback's table layer says.
- **PSLV and SPYI change CLASS at two firms.** PSLV, a physical silver trust, joins SLV in commodities; SPYI, an options
  income ETF, joins JEPI in structured. Both read alternatives today.
- **BRK.A and BRK.B are single stocks.** Their rows carry `instrument_kind: single_security`, as WMT's does.

## Served effects, all of them

1. **Investor Reporting, Holdings tab** -- from the next `irpt-holdings-snapshot` publication after the write:

   | | 49 Financial | Cottonwood | Inflection |
   |---|---|---|---|
   | CLASS moves | PSLV and SPYI, 5 nodes, 168,658.74 USD (alternatives to commodities, structured) | EVSM 10,216,541.88 USD (equity to fixed_income: a guess corrected); PSLV 2,440,594.86 USD; SPYI 2,671,845.64 USD -- 15,328,982.38 USD | none |
   | SUB CLASS moves | none | MEAR, VMLUX, FPNIX, EIBIX, 15,124,299.01 USD | 4 nodes with no value |
   | answered the same, from the canonical table instead of the fallback | none | twelve tickers, 38,496,339.35 USD | none |

   `custody_totals` do not move, so the route's tie (class lines plus remainder equal the total) holds.
2. **Black Diamond gold (49 Financial advisor pages: C_06, D_03, D_04)** -- from the next gold fire after the write: SPYI,
   PSLV and FPNIX, 18 open lots, 164,063.07 USD (`gold/holdings_lots`, measured 13:4xZ), move from `other` to the row's
   class. **This couples to tonight's 23:00Z fire:** those three have no row, so the scheduled detector (`E_18`, served
   since 08:41Z) will try to write a `scheduled` row for each. If this act runs first, `E_18` finds the rows and skips
   them. If `E_18` runs first, the pre-run dry run of this act shows it: a row with the same class is merged; a row with
   a different class prints CONFLICT and that ticker stops and comes back to `1.0.0_SA_CTO` (stop (b)).
3. **Investor Reporting, the comparison list** (`infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py`):
   it serves every NAMED row not written by a model and does not read `instrument_kind` (0 matches in the file), so it
   gains 19 entries at every firm, two of them single stocks (Berkshire Hathaway Class A and Class B). WMT is already
   there by the same rule. Whether the series provider returns a series for each when an adviser picks it is NOT measured.
4. **Cottonwood gold**: nothing today. Its host cannot read the table (0 DynamoDB statements on the role) and the
   re-point is serve-held (batch 90 item 2). These rows are what that re-point reads when it ships.
5. **The Black Diamond runner's shipped copy** of the seed source goes 19 more rows behind the repo. Inert there: the
   table, not the module, answers on the runner. The next Black Diamond gold deploy by any seat ships it.
6. **Every other reader of the table** (36 censused, `R7_MODEL_READER_CENSUS_20261001_1100Z.json`): a point lookup, or a
   scan that gains 19 ordinary seed rows of a shape 139 rows already have.

**Not part of this act:** FCASH and FIGXX (cash is the caller's rule, batch 93 item 1); the two Lambda copies of the seed
source; `--force-overwrite` and `--accept-module-truth`.

## Both branches

- **The run writes 19 rows** (expected): effects 1-6 above.
- **The run refuses** (rc 2: the pre-read failed; rc 3: a CONFLICT line): nothing is written, the script's own rule.

## Rollback per key

A row's class is corrected by a new seed run from a corrected seed source (seed always wins); that is the only rollback
this half carries, per ticker. Removing a row is a `delete-item`, which needs Andrew's word; two seat signatures are not
that. The merge is reverted by a revert commit on CLOUD, which does not un-write the table.

## Acceptance

1. Right after the run: `get-item` returns each of the 19 with `classified_by: seed`; the table counts 2,690 (or 2,690
   minus the rows `E_18` wrote first); a second `--dry-run` reads "rows to write: 0 of 158".
2. The one real run: the Holdings producer's own classifier (`holdings_snapshot.classify_security`) called on the 19
   symbols against the live table reads each row's class with basis TABLE.
3. Served: at the first `irpt-holdings-snapshot` publication after the write (2026-10-02 14:15Z if the write is today),
   the three firms' publications read EVSM fixed_income / Short Duration, PSLV commodities / Metals and SPYI structured /
   Options Income, and one walked Cottonwood selection's class lines tie. This is the acceptance; 1 and 2 are the test.
4. Served: the first Black Diamond gold fire after the write reads SPYI, PSLV and FPNIX with the rows' classes.

**Ledger:** one new entry, `secclass-cot-seed-rows-m-20261001`, opened before the merge; legs M (the merge and the blob
read), W (the write and its readback), R (the classifier read), S (the publication) and G (the gold fire).

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-01 16:0xZ)

Signed on the blast radius above: 19 new items; on the Holdings tab a class on 15,497,641.12 USD and a sub class on
15,124,299.01 USD across two firms; 18 Black Diamond lots; 19 more entries in the comparison list; the disclosed stale
shipped copy; a rollback that is a corrected seed row. Read at signing: the 19 tickers' absence (`get-item`, 15:2xZ), the
dry run (15:24Z, 19 of 158, 0 conflicts), the ten peers' live rows (15:5xZ), the three local builds, the lots, the
comparison reader's code. I merge and run only after the second signature, and I stop on any deviation this file does
not name.

## CTO half -- NOT SIGNED
