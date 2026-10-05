# Drive log 20261005T11Z -- 2.0.0_SA_COO~P (/canonical-drive IRPT_BCKEND, IRPT_DASHBD workstream B)

## tick 245 -- 2026-10-05T11:0xZ..11:3xZ -- lease FULL (both)
| project | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| IRPT_DASHBD (B) | L7 direct act | 16 | 1/1 | DB-b-25 taken as a DIRECT ACT (disk 1.6 GB, no worktree): mint retry once -> MintFailed abort; worker crash -> STOPPED + abort; complete only when the queue is empty. 4 new tests, 18/18; DB16-1-AC1/AC2 PASS. Runner @98d439936a under the audited GIT_COMMIT_AUTHOR_OVERRIDE=TREE_DELIVERABLES (the ~8 folder lane), amendment @91a4d48e89. Relaunch 3 (pid 43456) runs the old loaded copy; the fixed runner serves the next relaunch. Logs 06Z-10Z committed @9e297a0fd7 |

## tick 246 -- 2026-10-05T11:3xZ -- lease FULL (both)
| project | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| IRPT_BCKEND | release r54 | 54 | 1/1 | DRIVE FORWARD: the 11:30Z 49F fire on the new code landed 2026-10-02 (7577 rows); V2 undated dry_run = TARGET_ALREADY_LANDED, nothing computed; leg V2 closed @72d5f68aee. S297 / W123-S1 proven live. Only A2 (INF, after 14:00Z) remains |
| IRPT_DASHBD (B) | run | 16 | 1/1 | BD relaunch 3: 348 landed this run (~3208/5252), 2 FAILED, 2037 not requested; pace up to ~0.12/s. Disk 1.8 GB |

## tick 247 -- 2026-10-05T11:50Z -- lease FULL (both)
| project | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| IRPT_BCKEND | release | 54-55 | - | NO-OP: A2 (INF) waits on the 14:00Z fire. The r55 re-pin cell edits lambda-source-map.json pins, so it must run in a worker worktree and not as a shared-tree direct act (a pin edit in the shared tree would change any other seat's next build of those functions); disk 4.6 GB leaves a ~2 GB margin after a checkout, so it is held for the worktree removal Andrew is asked about |
| IRPT_DASHBD (B) | run | 16 | 1/1 | BD relaunch 3: 446 landed this run (~3306/5252), 4 FAILED, 1937 not requested |

## tick 248 -- 2026-10-05T11:58Z -- lease FULL (both)
| project | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| IRPT_BCKEND | release | 54-55 | - | NO-OP: A2 waits on the 14:00Z INF fire; the re-pin cell is held for disk (4.6 GB) |
| IRPT_DASHBD (B) | run | 16 | 1/1 | BD relaunch 3: 545 landed this run (~3405/5252), 5 FAILED, 1837 not requested |
