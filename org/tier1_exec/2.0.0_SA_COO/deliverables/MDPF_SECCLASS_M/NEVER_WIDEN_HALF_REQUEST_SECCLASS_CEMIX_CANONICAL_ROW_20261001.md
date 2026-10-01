# Never-widen half, MDPF_SECCLASS item 6 -- one new canonical row: CEMIX (Causeway Emerging Markets Fund, Institutional class)

**Author:** `2.0.0_SA_COO~M`, 2026-10-01 08:5xZ (FAST lease `MDPF_SECCLASS`). **For:** `1.0.0_SA_CTO` to sign the second half.
**Authority:** the CTO's round-6 order ("the CEMIX canonical row (a served class moves: both halves)",
`CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_6_20261001.md` @453c6430ec) and rulings batch 68 items 6-7 @85931f56b7 (the seed
source granted, code only). **Status of the act: NOT RUN.** The code is on CLOUD @9a45cad3af; the table is not written.

## The act: ONE new item in `etf-classifications`

`python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` (no flag), run once by this seat from the
laptop at CLOUD, with the seed source at blob `c280a8b152` (commit `32acc85d2e`) and the seed script at blob `d48358a5cc`.

| | value |
|---|---|
| item written | `ticker: CEMIX`, `asset_class: equity`, `sub_asset_class: EM`, `management_style: active`, `sector: Emerging Markets`, `name: Causeway Emerging Markets Fund Institutional Class`, `instrument_kind: fund`, `classified_by: seed`, `updated_by: seed-script`, `last_updated` |
| every other row | untouched. `--dry-run` against the live table, 08:32Z: 139 tickers in the module, 138 already correct and skipped, **1 to write (CEMIX)**, 0 conflicts, 1 preserved field (VNQ `management_style`, the table's value stands) |
| stop before the write | the real run is preceded by one more `--dry-run`; anything other than "rows to write: 1 of 139" naming CEMIX, or any CONFLICT line, stops the act |
| writers of this table | 5 by the contract's `classified_by` values (`seed`, `scheduled`, `constituents`, `legacy`, `model`; `org/standards/MDPF_SECCLASS_CONTRACT.json`); this act is the seed path only. E_18 (scheduled) writes only a ticker with no row, so it cannot touch CEMIX after this |

**The claim behind the class is INFERRED, not measured from a vendor feed.** Cottonwood's custody description for the
symbol reads "CAUSEWAY EMERGING MARKETS INSTL" (97 of 97 nodes); the fund is an emerging-markets EQUITY fund by its name
and its public prospectus category. No vendor was called. The row sits where IEMG, VWO and EEM sit (equity / EM).

## What the table serves today, and what moves

Today neither table holds the ticker (`get-item` 08:28Z: no `CEMIX` and no `CUSIP:149498107` in `etf-classifications`; no
`CEMIX` in `bd-securities`). The Holdings producer therefore falls to the bd-securities fallback, which answers through a
NAME ALIAS. Measured on a local Cottonwood build (`holdings_snapshot.py`, 2026-10-01 00:51Z), nodes whose
`display.symbol` is CEMIX -- the key the canonical lookup uses (`classify_security`, `holdings_snapshot.py:938`):

| nodes | basis | served today | after the row | USD |
|---|---|---|---|---|
| 67 | ASSIGNED | fixed_income / International (NAME_ALIAS) | equity / EM (TABLE) | 2,039,120.10 |
| 26 | OBSERVED | fixed_income / International (NAME_ALIAS) | equity / EM (TABLE) | 836,730.89 |
| 4 | ASSIGNED | equity / no sub class (TICKER_SHAPE) | equity / EM (TABLE) | 200,276.77 |

97 of 97 nodes move or gain a sub class. 49 Financial: 0 nodes with the symbol. Inflection: 0 (its 529 Causeway nodes are
CIVIX, a different fund, already equity / International from the table).

**Served effects, all of them:**

1. **Investor Reporting, Holdings tab, Cottonwood** -- from the next `irpt-holdings-snapshot` publication (14:15Z):
   on every selection holding the fund, the fixed-income total falls and the equity total rises by that selection's CEMIX
   amount; `custody_totals` do not move, so the route's tie (class totals plus remainder equal the total) holds.
2. **Investor Reporting, the comparison list** (`ycharts/generate/comparison_catalogue.py`): the list serves every NAMED
   non-model row, so it gains one entry, "Causeway Emerging Markets Fund Institutional Class", at every firm (that module's own note counts 317
   named rows on 2026-10-01; not re-counted here). A mutual fund is already in that list (MRSIX). Whether the series provider
   returns a series for it when an adviser picks it is NOT measured here.
3. **The Black Diamond runner's shipped copy** `s3://opal-data-bd/code/gold/lib/_shared/etf_classification.py` (ETag
   `58bfdb97...e18d`) is now one row behind the repo (md5 `c7f8d17c...2fb`). This act does not put it. The deploy tool
   ships that file with the next Black Diamond gold deploy by any seat (`safe_deploy_core.py` `shipped_artifacts_for`);
   it is inert there: Black Diamond holds no CEMIX and the table, not the module, answers on the runner.
4. **Every other reader of the table** (35 censused, `R7_MODEL_READER_CENSUS_20261001_0730Z.json`): a point lookup of a
   ticker they do not hold, or a scan that gains one ordinary seed row of a shape 138 rows already have.

**Not edited:** the two Lambda copies of the seed source (ruling item 7). Measured: they differ from it on 295 lines
(`opal-partners-data`) and 682 lines (`yang-generate-etf-returns`); neither one's reader classifies a Cottonwood mutual fund.

## Both branches

- **The run writes 1 row** (expected): effects 1-4 above.
- **The run refuses** (rc 2: the pre-read failed; rc 3: a CONFLICT line): nothing is written, the script's own rule. A
  conflict would mean another writer changed a seed row between the dry run and the run; it is a stop, never
  `--accept-module-truth` under this half.
- `--force-overwrite` and `--accept-module-truth` are NOT part of this act.

## Rollback

The row's class is corrected by a new seed run from a corrected seed source (seed always wins); that is the only rollback
this half carries. Removing the row is a `delete-item`, a destructive act that needs Andrew's word; two seat signatures are
not that. Point-in-time recovery reads ENABLED on the table (08:49Z) and is not used here.

## Acceptance

1. Right after the run: `get-item CEMIX` returns the item above; a second `--dry-run` reads "rows to write: 0 of 139".
2. The one real run: a local Cottonwood build of `holdings_snapshot.py` (no upload) reads 97 of 97 CEMIX nodes as
   equity / EM with basis TABLE, and against the 00:51Z build no node of any other symbol changes class.
3. Served: at the 14:15Z publication, one Cottonwood selection holding the fund reads CEMIX under Equity on the Holdings
   page and the class totals tie. This is the same publication as leg H5 of the held entry
   `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930`; the two reads are separate lines.

**Ledger:** one new entry, `secclass-cemix-canonical-row-m-20261001`, opened before the run; legs W (the write and its
readback), R (the local build) and S (the served page read).

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-01 08:5xZ)

Signed on the blast radius above: one new item, 97 Cottonwood nodes on the Holdings tab, one more entry in the comparison
list, the disclosed stale shipped copy, and a rollback that is a corrected seed row. Read at signing: the two tables'
`get-item` (08:28Z), the dry run (08:32Z, 1 of 139, 0 conflicts), the local build's 97 nodes by basis, the other two firms'
builds (0 nodes), the comparison reader's code, the two copies' diffs. I run the write only after the pre-run dry run reads
1 of 139, and I stop on any deviation this file does not name.

## CTO half -- SIGNED (1.0.0_SA_CTO, 2026-10-01T08:57Z)

Signed on the pre-signature blob `b77f9f7d6e` (@4e64572af9). Write set: ONE new item, `CEMIX`, in `etf-classifications`, by the seed
script with no flag. Both branches and the three acceptance reads stand as written. Rollback is a corrected seed row; no item is
deleted on this half.

Read by this seat, from bytes:

- The seed source at CLOUD HEAD is blob `c280a8b152`, the value this file states; commit 32acc85d2e adds five lines to it, all
  `CEMIX` (asset class, style, sub class, sector, name), and one test file. The seed script at HEAD is blob `d48358a5cc`.
- The live table (`get-item`, 08:56Z): no `CEMIX` item. The peer row `IEMG` reads equity / EM / Emerging Markets, `classified_by`
  seed: the new row sits in an existing class and sub class, so no value outside the contract's vocabulary is introduced.

The class is INFERRED from the fund's name and public category, as this file says; this seat adds no measurement to it.

Named by this half in addition:

1. THE DEFECT BEHIND THE MOVE IS NOT THE MISSING ROW. A name alias classed an emerging-markets equity fund as fixed income on 93
   nodes while a ticker rule classed the same symbol equity on 4. Leg R names the alias rule that fired and counts the other
   symbols it classes today. That count is a row for the round, not a condition of this write.
2. THE COMPARISON LIST gains one entry at every firm whose series was never requested from the provider. It is a public fund's
   name and no client's data. The first comparison request made with it is its test; a refusal there is a row for
   `2.0.0_SA_COO~Y`, and the remedy is the catalogue's eligibility rule, never a second classification table.
3. THE RUNNER'S SHIPPED COPY going one row stale is accepted as inert for the reason stated; the next Black Diamond gold deploy
   by any seat ships it, and that seat's half names it.
4. Acceptance read 3 (14:15Z) is a scheduled publication. It is the acceptance; legs W and R are the test and are not waited on.

Not verified by this seat: the 97-node count and its dollar figures, the dry run's 1 of 139, the two firms' zero counts, the 35
readers' census.
