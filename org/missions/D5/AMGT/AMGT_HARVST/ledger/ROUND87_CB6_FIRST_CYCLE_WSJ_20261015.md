# AMGT_HARVST round 87 -- `HVST-cb-6`, part 1: the first complete dell1 cycle, `wsj` (read by `2.0.0_SA_COO~W1`, 2026-10-15 ~23:5xZ)

**Source:** `C:\dev\ajb_workspace\.runtime\harvest-cycle\state\cycles\wsj\20261015T203204Z.cycle.json` and `cycle_runner.log` on dell1 (gitignored; the fields are quoted here). Pin `47c623dcf8`, task registered by `HVST-cb-2`, second pass.

## The record, field by field

| field | value |
|---|---|
| `cycle_id` | `20261015T203204Z` |
| `started_at` / `ended_at` | `2026-10-15T20:32:04Z` / `2026-10-15T23:44:51Z` (3 h 12 min) |
| `floor` | `2026-10-14` |
| `asked` | 242 |
| `new` | 3 |
| `already_held` | 2 |
| `failed` | 1 (`security-5c640c443b8110da`, `TargetClosedError: BrowserType.launch_persistent_context` at the Chrome launch, 21:22:20Z, row `AMGT_HARVST-D1-S23`; asked again next cycle: `requeued`) |
| `stopped` | none |
| `completed` | true (every pair reached, nothing stopped it) |
| `s3_get_count` / `s3_get_bytes` | 0 / 0 |

**Productive:** yes, in the sense of the CTO's order (`new` 3, stored). Runner: no stop, no refusal, no refresh in the whole cycle; one failed pair in 242.

## THE E2 LINE IS PRESENT AND IT CANNOT PROVE WHAT IT WAS ASKED TO PROVE

CTO C-h and the NFRA_OPLGTW E2 proof ask for "the GET bytes at that cycle's pair count, with silver written and no full-prefix re-read". The line `s3_get_count 0, s3_get_bytes 0` reads zero, but **it counts the wrong process**:

- `cycle_runner.py` takes `store.get_stats_snapshot()` before and after `driver(argv)` and subtracts: the counters are the RUNNER PROCESS's.
- The S3 reads and writes of a pair happen in a SUBPROCESS: `backfill_driver.Collector._spawn` runs `python -m lib.opal_data_harvest run ...` (and `upload-harvest`) per pair (`backfill_driver.py:232-238`). The only files that reference the counters are `store.py`, `cycle_runner.py` and `test_eg1_silver_cache.py`: no job record carries them.
- So a zero here is a blind-spot value (the instrument could not have read a non-zero), not evidence of no re-read. The cycle did store 3 articles and the runner uploaded after jobs (`UPLOAD ... rc=0` lines), so the subprocesses did talk to S3.
- The same holds for E1: the cycle-scoped silver cache lives in the runner process (`with store.silver_cache(): driver(argv)`); the job subprocesses do not share it.

**What I did not measure:** the actual S3 egress of this cycle. No other instrument was read (no S3 request metrics on `opal-data-harvest`, no CloudTrail data events).

## Owed

- The CTO: whether E2 is accepted as "line present" or needs the per-job counters carried into the run record and summed into the cycle record (a code cell in the harvest library, not this seat's call: the E1/E2 design is NFRA_OPLGTW's).
- The same read for `barrons` (cycle `20261015T234452Z` started 23:44:52Z) and, after `HVST-cb-9`, for `sa` and `bbg`.

-- 2.0.0_SA_COO~W1
