# Never-widen half, MDPF_HEALGAP cell 1 -- the Cottonwood gold catch-up: five existing gold partitions rewritten, five served points restored

**Author:** `2.0.0_SA_COO~M`, 2026-10-01 11:3xZ. **For:** `1.0.0_SA_CTO` to sign the second half.
**Authority:** rulings batch 72 items 1-7 @65417358df (the cause, the remedy, "a served move with both never-widen
halves") and batch 75 items 5-7 @8f06def1e7 (a new module; the call line is `4.0.0_SA_CRO`'s). Trace:
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/COTTONWOOD_ABSENT_POINT_TRACE_BRIEF_20261001.md` @a6645f5d8b.
**Status of the act: NOT RUN.** The module is on CLOUD and wired nowhere; the runs below were dry runs (no write).

## The act

The daily consolidator calls `mdpf_gold_catchup.run(s3, bdmp, slice_mod, upload=True)` after the day's gold build and
before the slice (the call line and the Lambda package row are in `MDPF_HEALGAP_M/HOOKUP_HANDOFF_FOR_4.0.0_SA_CRO.md`;
`4.0.0_SA_CRO` adds them and deploys `mdpf-gold-lambda` under its own ledger entry). **This half covers what the step
then WRITES on its first daily run: five existing objects in `s3://opal-data-assets`, each rewritten by the existing
builder (`build_dim_model_portfolio.main(["--date", A, "--value-date", V, "--upload"])`).**

| key `blackdiamond/cottonwood/gold/dim_model_portfolio/date=<A>/data.parquet` | carries today | after | prior VersionId (rollback target) | Opal dollars it will carry |
|---|---|---|---|---|
| date=2026-08-19 | value date 08-17 | value date 08-18 | `PCk.ZVdhC3KfTH9gK5sDpwT41hacOoCg` | 142,434,495.60 |
| date=2026-08-21 | 08-19 | 08-20 | `jl2bwRAA95xXPXiwwRn3wz1CEPWy1fxG` | 145,708,847.84 |
| date=2026-08-24 | 08-19 | 08-21 | `prrE6yeln3l3SIaGVXZajXh6zVz1erHO` | 146,275,792.27 |
| date=2026-09-24 | 09-22 | 09-23 | `u842OFS3LS4zmmoOVCurbbhX8dH_WXqf` | 197,132,575.38 |
| date=2026-09-25 | 09-22 | 09-24 | `Ie9RJF76OIhzWoMmPhU92fklkHuWLsXI` | 198,026,295.50 |

The five figures are the builder's own `dim_dollar_total_opal`, computed by the ad-hoc QA run (the step with `upload`
off, against live silver): each build returned rc 0 and `RECONCILE PASS`. The bucket's versioning reads `Enabled`; each
object above was last written at 13:30:39Z-13:30:40Z on its own date (`head-object`, 11:2xZ).

**Why existing objects are rewritten.** The partition key is the ASSIGNMENT date; the value date is a column. Valuing
holdings date V means writing partition `date=<the next trading day after V>`, which the daily run already wrote on
that day at an older value date. There is no other key to write (ruling item 3: no second output path).

**Why the older date does not move.** The slice keeps, per value date, the partition with the EARLIEST assignment date
(`build_cottonwood_mdpf_slice.cottonwood_gold_by_date`, the point-in-time rule). The step plans a rewrite only when an
earlier partition already values the older date; the live plan found one for each of 08-17, 08-19 and 09-22 (five of five
builds passed the guard; the trace reads 08-19's as date=08-20 and 09-22's as date=09-23). The rewritten partitions were
the LATER duplicates the slice never chose.

## Served effect

- **Cottonwood's series:** five dates read absent today and read measured after the next daily run: 2026-08-18, 08-20,
  08-21, 09-23, 09-24. No existing point changes value (the three older dates above keep their partition).
- **Global's series:** the same five dates stop being carried and become measured (ruling item 5).
- **49 Financial and Inflection:** no input of theirs is touched.
- **Readers of the rewritten partitions, 3:** the slice (every partition, by value date); the pair (lists partition dates
  for the series start and reads TODAY's partition only); the consolidator's QA path (`_dim_anchor_value_date`, newest
  partition only). None reads a historical partition by its assignment date.
- **Writers of this table, 2:** the consolidator's daily build (13:30Z) and the EC2 nightly
  (`infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:554`, `--date <freshest assignment> --upload`). Both write
  only the NEWEST assignment date, so neither rewrites a caught-up partition. The EC2 instance reads `stopped` (11:2xZ)
  and left no write on the five objects after 13:30Z of their date; whether it still fires on a schedule is NOT measured.

## Every branch of the step

| the day's state | what the step does |
|---|---|
| a late holdings date whose next-trading-day partition exists and whose older date has an earlier partition (the five) | one builder call with the explicit value date; the partition is rewritten |
| nothing unvalued that it may build (every day after the first) | zero builder calls; the family's output is what it would have been without the step (test: zero calls) |
| the next trading day has no assignment partition (34 dates live, the seven of ruling item 4 among them) | skipped, `NO-ASSIGNMENT-PARTITION`; the date stays absent |
| rewriting would restate or drop an older date (live: 08-04 and 08-12) | skipped, `WOULD-RESTATE`; the date stays absent |
| the daily run never wrote the next trading day's partition (live: 07-28, 07-29, 07-30) | skipped, `NO-PARTITION-TO-REWRITE`; the step never mints a partition |
| the newest holdings date | skipped, `ASSIGNMENT-NOT-YET-LANDED`; its own daily run values it |
| a read fails while planning, or a build fails or raises | recorded in the report (`plan_error` / `failed`), a WARN line, and the family continues to the slice |

**Two things the live plan showed that the ruling did not have** (QA runs 10:41Z-10:46Z and, after the narrowing,
11:16Z-11:23Z: 53 gold partitions, 78 holdings dates on the axis, 44 valued by no partition; the second run planned
exactly the five builds above, skipped 34 + 3 + 2, and returned the same five figures):

1. The first plan was EIGHT builds, not five: 07-28, 07-29 and 07-30 have holdings and a next-day assignment but no gold
   partition for date=07-29 / 07-30 / 07-31. Building them would MINT partitions in the range the composed backfill
   serves. The step now refuses that shape (`NO-PARTITION-TO-REWRITE`, @5082ed0513). If those three should return, that
   is a separate act with its own half.
2. Two more holdings dates are valued by no partition and stay so: 2026-08-04 and 08-12. Their next-day partitions
   (date=08-05, 08-13) are the EARLIEST that value 08-03 and 08-11, so rewriting them would drop those points. The trace's
   window began 08-17; these two are outside it. How they read on the served series is NOT measured here.

## Rollback

Per key: `copy-object` from the prior VersionId in the table onto the same key (a new version; no delete). The next daily
run then serves the five dates absent again, as today. The step itself is switched off by removing its call line
(`4.0.0_SA_CRO`'s file); with the line gone and the five objects restored the estate is as it is now.

## Acceptance

1. **The test, not waited on:** the ad-hoc QA run above and the fixture (`data/mdpf/tests/test_mdpf_gold_catchup.py`,
   16 passed: the 2026-09-23 to 09-28 landing order replayed ends with no unvalued holdings date it may build; control
   without the step: two dates dropped).
2. **The first daily run after the hookup deploys:** the family report's `catchup` block reads five `built`, 0 `failed`;
   each of the five objects carries the value date and the Opal total in the table (parquet read); the three older
   dates' earliest partitions are byte-unchanged.
3. **Served:** one trace per date to the Cottonwood point reading measured with that total, and the Global point reading
   measured; 49 Financial's and Inflection's series byte-unchanged.
4. **The second daily run:** `catchup` reads 0 planned, 0 built.

**Ledger:** one entry, `healgap-cottonwood-catchup-m-20261001`, opened before the hookup deploys; it records the five prior
VersionIds. The Lambda deploy is `4.0.0_SA_CRO`'s own entry.

## Not covered by this half

- The seven days with no assignment partition (2026-08-31 to 09-04, 09-08, 09-09): absent, by ruling item 4.
- The three late-July dates and the two August dates above.
- The Lambda build and deploy that carry the call line.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-01 11:3xZ)

Signed on the blast radius above: five named objects rewritten by the existing builder at explicit value dates, their
prior versions as the rollback, five served points restored and none restated, and a step that builds nothing on any
later day and lets no error out. Read at signing: the live plan (two QA runs, upload off), the five figures, the five
objects' versions, the bucket's versioning, the readers and writers of the table from source, the EC2 runner's state.

## CTO half -- (unsigned)
