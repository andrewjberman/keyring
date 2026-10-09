# Never-widen COO half (NFRA_TRNSPT) -- ONE bounded 365-day backfill of the analysis-commentary mail pull

Signer `2.0.0_SA_COO~T2` (NFRA_TRNSPT, dell2), 2026-10-09 ~02:4xZ. Ordered by `1.0.0_SA_CTO~DELL2` msg 2205: "Backfill: YES, one bounded backfill of
365 days through the existing pull, same filters and wipe, under its own never-widen pair. The pair names the window override as a new reachable
state on the manual path (CLAUDE.md NEVER-1), its write set and its rollback. Print listed, admitted and gold rows."

**Paired with:** the CTO half (owed by `1.0.0_SA_CTO~DELL2`; this half is not effective until that half is committed).

## The act -- exactly this, nothing wider

ONE run, by the laptop identity that holds encrypt on the transcripts key (`0.7.0_AE_CloudOps`; dell2's grant is Decrypt-only), from a pinned
commit of this repository:

1. `python data/transcripts/scripts/outlook/pull.py --gateway --days 365 --apply` -- the EXISTING pull's manual path (`pull.py:201` `--days`,
   `:217` floor 1, no ceiling), admitted-only (the gateway path's default), the same sender table (`criterion.load_tables()`), the same
   criterion (`criterion.classify`), the same skip of messages already in bronze (`sidecar_in_bronze`).
2. For each bronze date that run newly landed: `silver.build(<date>, apply=True)` (`silver.py:246`), the same wipe.
3. For each of those dates: `gold.build(<date>, apply=True)` (`gold.py:285`).
4. Print: `listed`, `admitted`, `landed`, `skipped_known`, `list_refusals`, silver rows and held_out, gold rows -- counts only, no content.

## The new reachable state (NEVER-1: an override that lets a scheduled producer run off its own clock)

The scheduled producer `outlook-global-transcripts-pull-lambda` runs at 23:30Z with `WINDOW_DAYS=7` and refuses a window over 120
(`mail_handler.py:35`). This act reaches a state the schedule cannot: a 365-day window, by the manual `pull.py --days 365` path. It is a ONE-TIME
run; the Lambda's env and schedule are NOT changed (`WINDOW_DAYS` stays 7; the rule stays `cron(30 23 * * ? *)`).

## Writers of the named properties (N per property, read from each writer's own rule)

| property (keys under `s3://opal-data-transcripts/`) | writers | N | rule read |
|---|---|---|---|
| `outlook/transcripts/bronze/analysis_commentary/date=<d>/...` | `pull.run` -> `land_bronze.land` (the Lambda and this manual run share the code) | 1 code path | admitted-only; a message already in bronze is skipped (`sidecar_in_bronze`), so existing keys are not rewritten |
| `outlook/transcripts/silver/analysis_commentary/date=<d>/...` | `silver.build` | 1 | rebuilds the date's one parquet from that date's bronze |
| `outlook/transcripts/gold/analysis_commentary/date=<d>/...` | `gold.build` | 1 | builds from that date's silver; gold holds 0 objects today |
| `outlook/transcripts/state/pull_runs/run=<id>/run.json` | `pull.run` | 1 | one new key per run id |

## Both branches (read from the producer's rule, not predicted)

- **Admitted >= 1:** new bronze keys on the newly landed dates; silver for exactly those dates (a date that already had silver is rebuilt from
  bronze that now holds more messages -- the one served-output change, on this project's own prefix, which no consumer reads beyond this project);
  gold for those dates (new keys). The run record is written.
- **Admitted = 0:** nothing lands; no silver or gold build runs; only the run record is written. The output is unchanged.

## Write set and rollback, per key

The write set is: new bronze keys (admitted messages only), the silver parquet of each newly landed date, the gold parquet of each such date, one
run record. Versioning is ENABLED on the bucket (measured by the laptop, msg 1705). Rollback per key: a silver key that existed before is restored
by copying back its prior VersionId (recorded before the run); a key that did not exist before is deleted -- a deletion is a human-confirmed act,
asked of Andrew, never taken by this seat.

## Bounds

365 days exactly; the existing filters; no change to the Lambda, the schedule, the sender table, the criterion or the wipe; no vendor call; no
content printed. A second backfill, or any other window, needs a new pair.
