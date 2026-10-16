# AMGT_HARVST round 87 -- the egress fix, REAL READ: the same `bbg` job, before and after `HVST-cb-10` and `HVST-cb-11` (`2.0.0_SA_COO~W1`, 2026-10-16 ~00:4xZ)

**Merged:** `HVST-cb-10` `62fcc1978e` (per-process S3 GET counters, ledger, cycle sums), `HVST-cb-11` `02d4090763` (design B: a job's backfill bound from a LOCAL watermark, no silver S3 read). Drain checks on the merged head: AC1 files 19 passed, AC2 set `125 passed, 4 subtests passed`, `py_compile` and `ruff` clean on the five touched modules.

## The read: one `run` job, same pair, same bucket, same probe

`deliverables/2.0.0_SA_COO_W1/round87/cb10_job_get_probe.py bbg .runtime/harvest-cycle/state/cycles/wsj/securities/BA.json` (the driver's own per-pair argument list, one process, scratch runtime root, read-only, nothing uploaded):

| | S3 GETs | bytes | status |
|---|---|---|---|
| BEFORE (23:5xZ, code before cb-10/cb-11) | 747 | 212,043,826 | `no_new_articles` |
| AFTER (00:4xZ, merged head `02d4090763`) | **0** | **0** | `no_new_articles` |

After the merge the probe also prints what cb-10 added: `record_get_count=0 record_get_bytes=0 ledger_lines=1`: the run record carries the two keys and the process wrote one ledger line, both agreeing with the in-process count. The instrument is the SAME probe that read 747 before, so the zero is not a blind spot (it was able to read a non-zero value on the old code).

## What this establishes and what it does not

- Establishes: the per-job silver read of the watermark is gone for a backfill job, and the counters now live where the S3 reads happen (run record + ledger + cycle sum).
- Does NOT establish: (1) the UPLOADER's reads (`upload-harvest`, `uploads.py` `silver_append` per source per pass): not run, not measured; `cb-10`'s ledger will show them in the first cycle that uploads. (2) A whole cycle's bytes: one job, one publisher. (3) `wsj`, `barrons`, `sa`: the probe ran `bbg` only (the other publishers' profiles are the production runner's). (4) Behaviour under the new bound on real articles: this job found nothing new, so the local mark was not advanced or exercised on live data.
- Carried: row `AMGT_HARVST-D1-W147-S1`: a pair with no local mark pages back to the cycle floor; a pair whose candidates are all already held never writes a mark. Cost: listing requests bounded by the floor, not silver reads.

-- 2.0.0_SA_COO~W1
