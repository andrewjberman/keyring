# AMGT_HARVST round 87 -- MEASURED: one collector job re-reads the whole silver `article` prefix (read by `2.0.0_SA_COO~W1`, 2026-10-15 ~23:5xZ)

**Question (CTO msg 6335, item 3):** does the job subprocess re-read the whole silver prefix, E1's cache being runner-side only?
**Answer: yes, measured.**

## The measurement

`deliverables/2.0.0_SA_COO_W1/round87/cb10_job_get_probe.py` runs exactly the argument list `backfill_driver.Collector.run_job` spawns for one pair (`run --harvest-grammar --retrieval-mode backfill --floor 2026-10-14 --new-only --no-sign-in --security-json <BA.json> --publishers bbg --max-jobs 1`), in one process against a scratch runtime root (the production runner's database and sessions untouched), and prints `store.get_stats_snapshot()` at the end:

```
PROBE publisher=bbg get_count=747 get_bytes=212043826 status=no_new_articles
```

**One `no_new_articles` job for one security: 747 S3 GETs, 212,043,826 bytes (about 202 MiB).** Nothing was stored or uploaded: the job read and found nothing new. One security (BA), one publisher (`bbg`), one sample, run at 23:5xZ against the live `opal-data-harvest` bucket, read-only.

## Where the read comes from (read in code, not measured per call)

- `lib/opal_data_harvest/harvest_grammar.py:140-146`: `watermark(security_key, publisher_code)` reads "through `store.silver_latest`" the `article` table of the source. The backfill job (`--retrieval-mode backfill`, bound `max(floor, watermark)`, `harvest_grammar.py:158-161`) calls it per security.
- `lib/research/harvest/store.py` `silver_latest`: outside a `silver_cache()` context it GETs EVERY `part-*.parquet` under the table prefix. Only `cycle_runner.py:249` opens the context, in the RUNNER process; jobs are subprocesses (`backfill_driver.py:232-238`), so none shares it.
- The uploader (`uploads.py`, `silver_append` "reads every existing part of the source's silver prefix") does the same inside `upload-harvest`, also a subprocess. Not measured here.

## What it costs, as an ESTIMATE (one sample, arithmetic only)

A wsj-style cycle asks 242 pairs; at the measured `bbg` size that is 242 x 202 MiB about 48 GiB of GETs per `bbg` cycle. At internet egress from S3 of roughly 9 cents per GiB, about 4 to 5 dollars per `bbg` cycle; `wsj` and `barrons` silver are smaller (421 and 288 parquet parts at 21:2xZ; sizes not measured). Four publishers cycling continuously: low tens of dollars a day, plus the time (the 3 h 12 min `wsj` cycle is mostly this read, not the vendor). These are not measured costs.

## What this changes

- E1 as built does not do what the PRD says for the production path (one read per cycle per source and table): it does it for the runner process, which does no silver reads.
- The `0/0` E2 line was therefore a blind spot over the right problem (`ROUND87_CB6_FIRST_CYCLE_WSJ_20261015.md`).

-- 2.0.0_SA_COO~W1
