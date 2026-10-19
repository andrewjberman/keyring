# 1.0.0_SA_CTO~Z -- landing the rc 50 / UNVERIFIED landing-leg fix in scheduled_daily_pull.cmd (Z-S17)

**archetype:** VALIDATE
**date:** 2026-10-19 ~13:1xZ | **row:** ETFS_POSITIONING Z-S17 (shape ruled by Z-S20) | **ask:** 0.0.3_BG_BBGTerminal msg 35958
**file:** `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`
[file:///C:/Users/Opal%20Bloomberg/Desktop/ajb_workspace/integrations/bloomberg/pipeline/scheduled_daily_pull.cmd](file:///C:/Users/Opal%20Bloomberg/Desktop/ajb_workspace/integrations/bloomberg/pipeline/scheduled_daily_pull.cmd)

## Who commits

The edit's author is 0.0.3_BG_BBGTerminal, whose prompt bars git work. This seat commits it: this seat ordered it (Z-S20),
and this seat's lane has committed this file before (`2e38c030f4`, 2026-09-24). It is not routed to 0.0.0_AB_MSTR~Z.

## The read Andrew's binding clause requires

`ANDREW_DIRECT_20261014_090xZ_NO_HOLD_ON_BLOOMBERG_SIGN_IN_REPAIRS.md`: "do not accidentally overwrite Positioning pipeline
or ETFS view operations. Any change that touches those runs carries a read showing it does not."

1. **Models chain (Positioning): untouched.** The two changed executable lines sit on the rc 50 path (`:precond_down`) and
   on the pull-failed / DAPI-UNVERIFIED path. Both reached `:prune` before and reach `:etf_leg` now. On both paths the models
   pull did not run or did not succeed, so it has nothing to publish. `RC` stays 50, so the 07:15 backstop still reads
   `LastTaskResult`. The dry run measured exit 50 on both arms. On the success path the only change is the
   `PY_AWS` definition, moved above the precondition with the same value.
2. **ETFS view legs on a genuinely-down Bloomberg: nothing written.**
   - `etf_daily_pull.py`: the Bloomberg pull's `except` returns 62 at :684. The first `put_object` is at :858.
   - `etf_constituents_pull.py`: when leg 1a fails with no tables, it returns 71 at :275. That is before leg 2 and before
     any `put_object` (:316).
   - `put()` refuses to write an empty frame.
   - Every key is under the run's own as-of folder, so no prior day's object is touched.
3. **Price leg:** the leg's own branch returns 82 with "NOTHING committed; the prior pointer is UNTOUCHED". It is
   `integrations/bloomberg/research/`, which the 10-06 record puts outside the order.

## Evidence from the author (dry run)

- With a forced cma failure, pre-fix HEAD ran **0 of 3** landing legs and the fixed bytes ran **3 of 3**.
- cmd exit was 50 on both arms.
- The harness is the real bytes with 4 value lines substituted. The two arms differ by exactly 2 executable lines.
- Source: `org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/SCHEDULED_DAILY_PULL_LINE115_DRYRUN_20261019.md`. It is
  UNTRACKED at this commit and is not in this seat's lane.

## Not in this commit

`integrations/bloomberg/auth/dapi_check.py` (also modified on disk) is the separate IMPORT-BLOCKED naming change. Z-S20
ruled that change 0.0.3_BG_BBGTerminal's. It is not graded or landed here.

## Disarm

Z-S17 disarms when this commit is on `box/sitez` before the 2026-10-20 11:00Z run, which reads disk. The run's log is the
first organic read.
