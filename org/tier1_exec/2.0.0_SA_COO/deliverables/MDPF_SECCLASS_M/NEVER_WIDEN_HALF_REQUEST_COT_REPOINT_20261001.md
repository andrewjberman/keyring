# Never-widen half, MDPF_SECCLASS -- the Cottonwood re-point: Cottonwood gold classifies from the canonical table by the ruled rule

**Author:** `2.0.0_SA_COO~M`, 2026-10-01 18:3xZ (FAST lease `MDPF_SECCLASS`). **For:** `1.0.0_SA_CTO`, second half.
**Status (2026-10-02 05:2xZ): COO half SIGNED; CTO half asked; the act is NOT RUN. The three preconditions are MET (below); the
values are re-measured on the live table, the writers per key are counted, and the branch's merge trap is fixed.**
**Authority:** CTO rulings batch 86 items 5-8 (canonical only, the residue named), batch 93 items 1-5
(COTTONWOOD-CASH-AND-NO-TICKER-CLASS-RULED-20261001), batch 99 items 1-4 (the mix carries commodities, structured and
unclassified; the reader census), `RULINGS.md` @944faa8793. Row IRPT_BCKEND-S173.

## Preconditions (batch 93 item 4: "Items 1 and 2 and the 19 seed rows land first")

1. **The 19 seed rows -- WRITTEN** 2026-10-02 02:12:11Z under both halves (CTO `CTO_HALF_SECCLASS_COT_SEED_ROWS_20261002.md`),
   ledger `secclass-cot-seed-rows-m-20261001` (legs M, W, R closed).
2. **The CUSIP rows (item 2) -- WRITTEN** 2026-10-02 03:40:18Z: 29 bank-CD `CUSIP:` rows, 3,005,499.29 USD, under both halves
   (`NEVER_WIDEN_HALF_REQUEST_COT_CUSIP_ROWS_20261001.md`; CTO batch 108), ledger `secclass-cot-cusip-rows-m-20261002` (leg R held
   on this act's leg S). Not written, by ruling: 43 Black Diamond vendor identifiers (4.47 M, batch 93 item 3) and two
   mortgage-backed bonds with no peer (16,103.37 USD).
3. **The cash rule (item 1)** -- built into this act (`classify_position`, rule 1); it lands with it.

## The act, by leg

| leg | what | how | code |
|---|---|---|---|
| M | merge branch `coo-m-cot-carrier` @affbc33e2b into CLOUD | `.tools/safe-merge.sh`; stop if the merged tree differs from CLOUD in any file but the ten named here, or B_00 is not blob `922249798b` after it | B_00 carrier; `lib/etf_classifier.classify_position`; C_06, D_03, D_04 on the rule; `lib/mix_views.py`; D_04's firm snapshot; four test files -- 10 files. `data/cot/scripts/gold/tests` 22 passed at affbc33e2b |
| I | the Cottonwood host role reads the canonical table | plan + `safe-apply` of `infra/aws/terraform/cot-pipeline` (statement `CanonicalClassificationsRead` on `cot_exporter_policy`, on CLOUD since @47e510a186), the role's statements printed before and after (CTO condition) | |
| A | the shared classifier client reaches the host | `safe-deploy` of Cottonwood's shipped artifacts (`CODE_TREES["cot"]["shipped_artifacts"]` @47e510a186, to `lib/_shared/`) | |
| G | the gold scripts reach the host | `safe-deploy` of `data/cot/scripts/gold/{B_00,C_06,D_03,D_04}` and `lib/{etf_classifier,mix_views}.py`; remove the `# DEPLOY-SERVE-HELD` line from `lib/etf_classifier.py` in leg M | |
| P | the portal renders every class | portal branch `coo-m-cot-mix-readers` @35cd4be5 (from DEV 2bb367ef) merged forward and pushed to DEV under this lease | six readers of the census + Cottonwood's layout |
| R | the one real run | an ad-hoc Cottonwood gold run (QA) after G, its outputs read | |
| S | served | the next scheduled Cottonwood gold run, and one walked Cottonwood page per view below | |

Order: I, A before G (a host that cannot read the table would class everything unclassified); P before S's walk.

**The merge trap, found and fixed on the branch (2026-10-02 05:1xZ).** The branch forked at dda373cbd3 (the B_00 carrier), and
CLOUD carries that commit AND its revert 1c1d2a02c2 (made on `coo-m-r30`), so a merge in either direction resolved B_00 to
CLOUD's bytes and dropped its test -- silently, with no conflict. CLOUD was merged into the branch (12a364a4fd, tree check 1,761
files, 0 dropped, 0 foreign) and both files restored from dda373cbd3 (affbc33e2b); CLOUD's B_00 equals dda373cbd3's parent, so
nothing is lost. The B_00 test fails on CLOUD's B_00 (negative control) and passes on the branch. A dry merge
(`git merge-tree --write-tree CLOUD coo-m-cot-carrier`) differs from CLOUD in exactly the ten files of leg M, B_00 at
`922249798b`. Leg P's portal branch: 48 commits behind origin/DEV, none touching its 8 files; it is merged forward at leg P.

## Blast radius

**Values -- today's rule by tomorrow's class**, RE-MEASURED 2026-10-02 03:5xZ on the live table (2,719 rows, 377 `CUSIP:`; the
same script as `COT_REPOINT_TODAY_BY_TOMORROW_20261001.md` @e0f8d95bd8; 2026-09-30, 13,063 valued rows, 554,618,741.24 USD):
unclassified tomorrow **97,721,872.62 USD (17.6%)** (100.73 M before the CUSIP rows), of which 97,333,977.93 is classed today
only by the default guess (a correction); regressions in the ruling's terms: none (the host reads no table and no feed field
today); the same six entries classed today by a name pattern turn unclassified (387,894.69 USD, listed there, the ruling's to rule
on). The residue by why: no ticker and no CUSIP 70,996,059.79; a ticker with no row 22,239,672.91; a CUSIP with no row
4,486,139.92 (the vendor identifiers and the two bonds above). Tomorrow's mix: equity 218.59 M (39.4%), fixed_income 189.67 M
(34.2%), unclassified 97.72 M (17.6%), cash 22.63 M (4.1%), commodities 20.20 M (3.6%), structured 5.71 M (1.0%),
alternatives 0.10 M.

**Served keys written by the changed scripts** (graph `comp-pipescript io <script> --pipeline cot-gold`): C_06 writes
`gold/views/mix_daily_summary.json` and `gold/entities/clients/{*}.json`; D_03 writes `gold/artifacts/firm_mix_views.json`,
`firm_mix_views_daily.json`, `gold/entities/advisors/{*}/mix.json`, `mix_daily.json`, `mix_timeseries.json` (and the composition
artifacts); D_04 writes 23 `platinum/...` keys including `platinum/firm/mix_summary.json`, `timeseries_overview.json` and the
advisor, client and account summaries; B_00 adds two columns to `gold/canonical/holdings/{date}.parquet` (values untouched).
**Writers per key: ONE each, counted from the world** (2026-10-02 04:0xZ, `comp-clobber --sweep opal-data-cot <prefix>`, the
live etag-lineage oracle over every key's version history): gold/views/ 5 keys, gold/artifacts/firm_mix 2, platinum/firm/ 12,
gold/entities/advisors/ 2, platinum/advisors/ 3, gold/entities/clients/ 410, platinum/clients/ 437 -- 871 keys, 0 interleaved
lineages (no second producer writes between the gold runs); `mix_daily_summary.json` shows one daily writer at ~11:35Z over its
last 10 versions (one off-cycle write 2026-09-27 18:48Z, a Saturday, not interleaved -- an ad-hoc run of the same chain by its size step). The static scan of `data/cot` names D_04 as the sole
writer of each literal `platinum/firm/*` key. LIMIT: lineage sees only producers that wrote inside the retained versions.
**CORRECTION (2026-10-02 05:4xZ, after both halves):** `platinum/firm/mix_summary.json` has a SECOND DECLARED writer the static
scan missed (it holds the key in a constant, `SERVED_KEY` :35, and writes it through a helper, `fc.emit_and_verify` :211, into
its `--output-root`): `data/cot/scripts/gold/runners_cot/d08_cot_mix_summary.py`, a fleet emitter.
It is not live -- the key's last three versions (2026-09-29 11:58Z, 09-30 11:35Z, 10-01 11:37Z) are one daily lineage at the
chain's time and carry D_04's shape (`composition`, `concentration`, `mix_periods`, `mix`). Its rule, read: it classes from its
own `dim_asset_classification` (A_07) table, imports no classifier library (no file in `runners_cot` names `etf_classifier`),
and raises `CLASS-DOMAIN FAIL` on any class outside {equity, fixed_income, alternatives, UNCLASSIFIED-LOUD} of THAT table. This
act changes neither A_07 nor `runners_cot`, so the d08 branch is unchanged by it: if d08 ever runs, it writes what it would have
written without this act. Declared writers of that key: 2 (D_04 live, d08 dormant); both rules read.

**Shape changes:** the mix carries `commodities`, `structured`, `unclassified` as classes (batch 99); the period views publish
`cash`, `commodities`, `structured`, `other` as themselves where they read `unclassified` before; the firm snapshot keeps every
class. **Readers** (`COT_REPOINT_READER_CENSUS_20261001.md` @a1298b33c9): 18 readers; the 7 that dropped a class change in
leg P; 0 crash; 3 reachabilities not determined. One colour gap: `unclassified` shares grey with `other` in the advisor Mix chart
(`chartColors.ts` is `2.0.0_SA_COO~D`'s).

**Black Diamond and Inflection:** not moved by this act. The portal readers render any class they receive, so a firm that
serves only the old classes renders as before (the reader tests pass on unchanged fixtures). Black Diamond's own `C_06` alignment
is batch 99 item 4, separate.

## Both branches

- **The act lands:** values as above; the host reads the canonical table; every Cottonwood view shows the new classes.
- **Leg I or A fails:** stop before G; nothing classes differently (the old library keeps running on empty maps).
- **Leg R reads a mix that does not sum, or a reader drops a class on the walk:** roll G back (prior code objects by version id)
  and P back (revert commit on DEV); the served keys rewrite on the next run of the old code.

## Rollback per key

Code objects: the prior S3 version of each deployed file (recorded at deploy). Served keys: each is rewritten by the next run of
whichever code is deployed; no key is deleted. The IAM statement: removed by a plan + `safe-apply` of the prior file. Portal: a
revert commit on DEV.

## Acceptance

1. Leg R: the QA run's `mix_daily_summary.json` sums to 100% per client with the new classes present; the firm snapshot carries
   every class; the period views publish `cash` and `commodities` as themselves.
2. Leg S: the scheduled run's served keys read as in 1; one walked Cottonwood page each: the firm Mix chart (structured,
   commodities, unclassified drawn), the Books donut and legend, one advisor's Mix chart.

**Ledger:** `secclass-cot-repoint-m-<date>`, opened before leg I; legs M, I, A, G, P, R, S.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-02 05:2xZ)

Signed on the blast radius above: Cottonwood gold only -- 554.62 M USD reclassed by the ruled rule, 97.72 M of it served
`unclassified` as the named residue (a correction of today's default guess; no regression in the ruling's terms; the six
name-pattern entries, 387,894.69 USD, left for the CTO to rule); 871 served keys, one producer each; the mix gains commodities,
structured and unclassified as classes; seven portal readers change in leg P; Black Diamond and Inflection unmoved; one IAM
read statement on the Cottonwood host role (one table, GetItem and Scan). Read at signing: the re-measure on the live table
(03:5xZ), the writer sweep (04:0xZ), the branch at affbc33e2b (22 tests, the B_00 negative control, the dry merge's ten files),
the portal branch against DEV. NOT read at signing: the Terraform plan of leg I (the root needs a provider install on a disk at
94 percent; leg I prints the role's statements before and after as its first step and stops on any change other than the one
statement); the three reader reachabilities the census left open. I act only after the second signature, leg by leg in the
order above, and stop on any deviation this file does not name.

## CTO half -- NOT SIGNED
