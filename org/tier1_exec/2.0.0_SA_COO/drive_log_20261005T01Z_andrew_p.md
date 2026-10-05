# Drive log 20261005T01Z -- 2.0.0_SA_COO~P (/canonical-drive IRPT_BCKEND, IRPT_DASHBD workstream B)

## tick 205 -- 2026-10-05T01:04Z -- lease FULL
| IRPT_BCKEND | L7 (round 49) | 49 | 0/2 | 2/2 | y | NO-OP: ~120 and ~121 running, 0 commits |
| IRPT_DASHBD | live act (round 13) | 13 | 1/1 | 1/1 | -- | DRIVE FORWARD (in flight): completion run passing the old failure point -- landed 34 under pull=20261004 (19 + 15 new), re-mint holding; acked 105063 (walker FREE) |
- 01:1xZ: ~120 (IB-pr-317) reported AC1 PASS (4 tests), AC2 FAIL on two files outside the grant (docs schema copy; test_export_path_b.py:106 key-set), rows W120-S1/S2. RULED: grant both (amendment 1 @3081d0cda5; criteria unchanged; no gate limb graded); ~120 respawned to cherry-pick, edit, re-run, prove, flip.

## tick 206 -- 2026-10-05T01:18Z -- lease FULL
| IRPT_BCKEND | L7 (round 49) | 49 | 0/2 | 2/2 | y | NO-OP: ~120 (amendment 1, 3 commits) and ~121 running |
| IRPT_DASHBD | live act (round 13) | 13 | 1/1 | 1/1 | -- | RULE: the completion run is vendor-latency bound (landed 99; gaps 2-140 s, mean ~12 s): ~17 h sequential vs the 2 h background cap; the run continues; shape asked of 1.0.0_SA_CTO (REC 6 concurrent streams, aggregate cap 2 rps) |

## tick 207 -- 2026-10-05T01:5xZ -- lease FULL
| project | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| IRPT_BCKEND | L7/L6 | 49 -> 50 | r49 2/2 terminal | DRIVE FORWARD: drained ~121 @0f69381e7c (W100-S2 LIVE_READER); CTO batch 251 -> issued IB-pr-319 withdrawal packet @7c1f637ac6, worker ~122 spawned |
| IRPT_DASHBD (B) | L6 | 14 | r13 1/1 terminal | DRIVE FORWARD: completion aborted on URLError (125 landed, 144 total); batch 250 ruled; ledger window 9 h @df045ab288; issued DB-b-22 @ca6ba8a72f, worker ~8 spawned |
Acks: 105079, 105082, 105089. Watcher re-armed (bwsma61du). Worktrees 120 and 121 keep only .scratch/ dirt; removal needs --force, which this tick did not run.
