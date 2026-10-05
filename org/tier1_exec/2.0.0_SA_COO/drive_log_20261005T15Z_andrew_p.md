# Drive log 20261005T15Z -- 2.0.0_SA_COO~P (/canonical-drive IRPT_BCKEND, IRPT_DASHBD workstream B)

## tick 258 -- 2026-10-05T15:00Z -- lease FULL (both)
| project | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| IRPT_BCKEND | release r57 | 56 | 1/1 | NO-OP: the invoke-payload prep is in flight; all 4 before-reads = anchor (r57 ledger open @e860151215) |
| IRPT_DASHBD (B) | run | 16 | 1/1 | BD relaunch 3 at its tail: 2345 landed this run, 37 not requested, 5 FAILED (all transport, within batch 250's sweep class) |

## tick 259 -- 2026-10-05T15:0xZ..15:2xZ -- lease FULL (both)
| project | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| IRPT_BCKEND | L6 | 57 | 0/1 | PARALLELIZE on CTO batch 264 (S335 option a): issued IB-pr-325 (a retry refresh schedule at 09:40 ET + the latest.json never-widen packet) @e0f7126735, worker ~128 spawned. Read: schedule.tf:381-387 puts the runner up 12:52Z-16:41Z via mdpf-feeder-trigger; today's 12:52Z start did not happen (LaunchTime 13:30:36Z), which is noted in the packet as the MDPF lane. r57 deploys wait on the invoke payloads |

## tick 260 -- 2026-10-05T15:2xZ..15:4xZ -- lease FULL (both)
| project | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| IRPT_DASHBD (B) | run E1 | 16 | 1/1 | Relaunch 3 COMPLETE 15:1xZ: 2382 landed, 6 FAILED (all transport), 0 not requested; S3 5242/5252 (10 missing: 6 FAILED + 4 in-flight losses from relaunch 2). Run 4 (fixed runner) over the re-derived complement of 10 launched (batch 258: relaunch until empty); the batch 250 sweep follows only if any FAILED remain |
| IRPT_BCKEND | r57 / L7 | 57 | 0/1 | NO-OP: r57 waits on the invoke payloads (agent in flight); ~128 in flight on IB-pr-325 |

## tick 261 -- 2026-10-05T15:4xZ..16:0xZ -- lease FULL (both)
| project | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| IRPT_DASHBD (B) | E1 DONE | 16 | 1/1 | DRIVE FORWARD: run 4 over the complement of 10 (9 landed, 1 FAILED transport), then the batch 250 sweep (1 landed, residue 0): S3 5252/5252. Ledger P1 closed @54cbe5a477; G1 (E2, the 0.35 pp tie-out) is next and reuses DB-b-3's tie-out tool on the full population |
| IRPT_BCKEND | L7 rule | 57 | 0/1 | ~128: packet committed (latest.json versions 4620/292/258 entries, writer directory_runner.py:902-903); schedule.tf refused by the naming gate (W128-S1) -> amendment 1 @1b30e3b6d6 names it irpt-directory-refresh-retry-daily; ~128 continued. r57 waits on the invoke payloads |
