# ADVI_FIRMBKTS -- the Door 6 retirement, decision text (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~18:5xZ)

**Answers:** `2.0.0_SA_COO~B1`, census `deliverables/0.9.0_WK_ADVI_FIRMBKTS~85/DOOR6_CENSUS.json` @e9b49c930c (FB-p-1, read 18:14Z).
**His decision stands:** Andrew-direct 2026-10-13 (`ANDREW_DIRECT_20261013_200xZ_NINE_OPEN_CALLS_ANSWERED_FIRMBKTS_DEMQUE_BRIEF_HARVEST.md` row 1)
retires the Inflection done-marker `opal-data-inf/gold/meta/pipeline-complete.json` and its watcher `mdpf-feeder-accelerator`, in "the same
flow as the comparable 49 Financial/Cottonwood job". This text orders the steps. It does not change his decision.

## What the census changes (read by this seat in the code)

1. **The marker is also the gold chain's "already done today" record.** `inf-gold-trigger/lambda_function.py:30-43` reads the key's
   `snapshot_date` and skips the dispatch when it equals today's. If the write stops, the key keeps an old date, the check returns False,
   and a second trigger on the same day re-runs the gold chain. A missing key is also treated as not done.
2. **The backstop does not yet replace the watcher.** `mdpf-feeder-backstop-daily` fires `mdpf-feeder-trigger` at `cron(52 12 * * ? *)`,
   while today's marker landed at 12:56:43Z. The backstop fired before gold completed. If the accelerator goes, the feeder would read the
   previous day's gold on such a day, unless the feeder checks readiness itself. That is not yet read.

## Decision: the order, each step with its rollback

1. **First, `inf-gold-trigger`'s idempotency gets its own record.** It reads a key the gold chain writes for that purpose, under the chain's
   own name (builder output, rule 30), or it reads the chain's run manifest. It no longer reads the marker. Test: a planted same-day record
   skips, and a planted previous-day record dispatches. Rollback: redeploy the prior function version.
2. **Second, the feeder is triggered the 49 Financial way,** read live and never assumed. B1 reads how the 49 Financial feeder is
   triggered, plus two facts:
   - the gold chain's completion time against 12:52Z over the last 10 trading days, with the denominator;
   - whether `mdpf-feeder-trigger` checks that gold is ready before it reads.
   If the feeder lacks a readiness check, it gets one (the data-frontier pattern of `inf-portal-publisher`, FB-m-1), or the backstop moves
   after the measured completion time. **Only then is `mdpf-feeder-accelerator` disabled,** and the record says what replaced it: the
   backstop schedule with the readiness check. Rollback: re-enable the rule.
3. **Last, the marker write stops** (`orion-gold-dispatch.sh:1906`). The record names its replacements: the idempotency record (step 1)
   and the feeder trigger (step 2). Nothing else reads it: the census found `inf-gold-freshness-guard` and `mdpf-daily-trigger` absent live.
   Rollback: restore the line.
4. **Out of the retirement, left as they are:** the fence Deny `DenyInfGoldSentinelAbsolutely`, which guards a key nobody will write and
   costs nothing; `FIRMSEP-s3-direct-access-bypass`; and `opal-globgrph-cloudtrail-mgmt`.

**FB-p-2 un-parks now** and carries steps 1-3 in this order, each its own criterion.
- Step 2's reads are its first criterion, and they go to this seat before any rule is disabled.
- The census's NOT-READ line (the deployed runner copies in `s3://opal-data-inf/code/runner/`) is read before step 3: the live writer is
  the deployed copy, not the repo copy.

-- 1.0.0_SA_CTO~DELL1
