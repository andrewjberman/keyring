# Packet for Andrew's word -- nine stale objects under three gap days of the Inflection holdings gold (PREPARED, NOT RUN)

Author `2.0.0_SA_COO~P`, 2026-10-01 15:1xZ. Ordered by `1.0.0_SA_CTO` rulings batch 92 items 1-4 (@e1acc0265b): the end state is NO
partition for 2026-05-11, 2026-06-30 and 2026-08-10; reaching it is an S3 delete, which CLAUDE.md (Agent Autonomy) reserves to a
human's confirmation. No seat runs this and no half is signed until Andrew says so.

## What is asked, in one sentence

Delete nine objects (three dates, three objects each) from `opal-data-inflection`, in a versioned bucket, so each becomes a delete
marker and stays restorable.

## Why

The Inflection holdings gold was rebuilt today on the measured close basis (1,613 of 1,616 partitions rewritten; ledger
`irpt-holdings-gold-inflection-rebuild-20261001`, closed). Three trading days have no row under the new rule, because the close of
each is in no source partition; their returns are carried by one linked row on the next day (CTO rulings batch 80). The partitions
of those three days still hold the rows of the 2026-09-29 build, which dated every return one day late. A reader chains them
beside the linked row and counts one move twice: measured on account 226, the candidate adapter's year to date reads 0.36 percent
with the three stale rows and 2.40 percent without them. Nothing serves this gold today. The serving packet does not land while
they exist (batch 92 item 4).

## The nine objects (listed 2026-10-01 15:13Z; each has 2 versions, 0 delete markers)

Bucket `opal-data-inflection`. Current version of each, all written 2026-09-29T09:22Z to 09:23Z:

| # | key | current version id | bytes |
|---|---|---|---|
| 1 | `irpt/inflection/gold/holdings_performance_daily/date=2026-05-11/data.parquet` | `HOO_l1FfNuGLZH85hZUnqe09aKKx05vF` | 32,432 |
| 2 | `irpt/inflection/gold/holdings_performance_manifest/date=2026-05-11/data.parquet` | `BV_gGrb2dtzSnrv9Aq5X3D7EWACSjcJm` | 17,619 |
| 3 | `irpt/inflection/gold/holdings_performance_manifest/date=2026-05-11/manifest.json` | `qb89UF2OAF4QagfMhzksT6dY.DHjj2wK` | 3,417 |
| 4 | `irpt/inflection/gold/holdings_performance_daily/date=2026-06-30/data.parquet` | `NxsbZAFvZxKs2I4.O3iTY2BWQT_dSEIE` | 33,068 |
| 5 | `irpt/inflection/gold/holdings_performance_manifest/date=2026-06-30/data.parquet` | `avBIe7gd26LX8XD_pckQQRCEqclXe6sD` | 17,624 |
| 6 | `irpt/inflection/gold/holdings_performance_manifest/date=2026-06-30/manifest.json` | `_E.eAa8qIh42h15LkWSlvwcvpjCtrVvt` | 3,419 |
| 7 | `irpt/inflection/gold/holdings_performance_daily/date=2026-08-10/data.parquet` | `rjBTEV2mKX28Sw.89jMlLUEHFkCJU0iw` | 33,561 |
| 8 | `irpt/inflection/gold/holdings_performance_manifest/date=2026-08-10/data.parquet` | `uUwVBT54p2MicxDKUhJqVSFgBisfecW1` | 17,624 |
| 9 | `irpt/inflection/gold/holdings_performance_manifest/date=2026-08-10/manifest.json` | `JXmzA7Mt49G4c_fFhmfrloTo0zHYKY4_` | 3,419 |

Denominator: the table holds 1,616 daily partitions; 1,613 were written today; these three dates are the whole remainder
(`stale_gap_days_precondition.py`, run 15:14Z: 9 current objects under the three dates; the control date 2026-05-12 holds its three).

## The act, as it would be run (by a human, or by a seat on Andrew's word at a terminal)

For each of the nine keys, ONE call with NO version id, which writes a delete marker and removes nothing:

    .tools/aws s3api delete-object --bucket opal-data-inflection --key <key>

Each call prints the delete marker's own `VersionId`; the nine are recorded in the ledger entry opened for the act. No other key,
no prefix, no recursive form, no version-specific delete.

## Rollback, per key

Remove that key's delete marker, which makes the version in the table above current again:

    .tools/aws s3api delete-object --bucket opal-data-inflection --key <key> --version-id <the delete marker's version id>

## The pre-condition the serving packet reads

`python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/stale_gap_days_precondition.py` must print
`PRE-CONDITION PASS: no partition under the three gap days` with its control line intact. Today it prints FAIL, 9 objects.

## What does not need this

Nothing else waits on it: the rebuild is closed, the three hand reproductions are accepted, and the serving packet's other parts
(the adapter's two members, the read grant on the Inflection gold, the producer function and its re-timed schedule) are being
prepared. If no word is given, batch 92 item 6 has `1.0.0_SA_CTO` reopen the disposition rather than leave the thread parked.
