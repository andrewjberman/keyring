# /self-drive EVERY dell2 project (11, 30m) -- tick 1 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_034xZ_SELF_DRIVE_30M_EVERY_DELL2_PROJECT_AND_DISCRETION_ON_THREE_ACTS.md` @35fabf20c8
**Tick:** 1 (04:18Z), plus the work since the re-arm. **state: ARMED** | cron c17cb1c7 (7,37). It replaces b0f6db2a and then e2973ff1.

## Scope (denominator 11)

Measured from `org/missions/D*/*/*/project.json` with `placement: DELL2` (48 scanned, 10 matched), plus IRPT_ANLREQ registered this tick.

| Project | status | dep_stage | Reach |
|---|---|---|---|
| ADVI_BILLING | active | PRD (ADMITTED 10-06) | **UNREACHABLE: no COO seat.** Seat asked of MSTR~DELL2, msg 042037Z |
| ADVI_COTBKF | active | EXECUTING | reachable |
| DSGN_IRPTV1 | active | EXECUTING | reachable |
| IRPT_ANLREQ | active | REGISTERED | reachable. L4 PRD owed by this seat |
| IRPT_BCKEND | active | EXECUTING | reachable |
| IRPT_CUSTDY | active | EXECUTING | reachable |
| IRPT_DASHBD | active | EXECUTING | reachable |
| IRPT_YCDGEN | active | EXECUTING | reachable |
| NFRA_OPSWKF | active | PRD (ADMITTED 10-06) | **UNREACHABLE: no COO seat.** Seat asked of MSTR~DELL2 |
| NFRA_TRNSPT | active | EXECUTING | reachable |
| TCKT_VNEXT | active | EXECUTING | reachable |

## Acts since the re-arm

| Act | Record |
|---|---|
| Andrew's discretion grant executed: S3 delete rows 47b1 and e6a4 closed as ruled by andrew; ~Y2 told to delete exactly the named lists | the record @35fabf20c8 |
| IRPT_ANLREQ: L2 endpoint, then L3 registration (tree row, index, D9 members line) | @670ded26ed, @07d6672dbe |
| IRPT_DASHBD v0.8 FWD-11: fix landed @3eb7dbcf36; CVO signed, ADMITTED (msg 2350). Rule-13 note corrected | @6375cfa208 |
| data_refresh admission hazard (row W6-S2) measured: 45 PROFILE rows lack userType. Fix ruled fail-closed. **Site Z owns and applies it** (msg 2394) | msgs 040619Z, 040623Z |
| Firm-scope narrowing for internal callers: keyed to the PROFILE row; a non-list value fails closed (IB-pr-387 ~P2; ticket handlers ~V2) | msgs 040932Z, 040936Z |
| Svc-commentary composition read: (b) through get(), tenant-bound | msgs 034322Z, 034325Z |
| TV-r-1 seat-arm pair REFUSED (internal = ALL for 2h) | msg 034330Z |
| Portal 44c31b8e (= 35395cf5) verified live on DEV. Portal fd345aef APPROVED for DEV (patch-id equal) | msgs 041152Z, 041945Z |
| **IRPT_DASHBD R35: ROLL BACK ruled.** The dry_run sizing was unmet (lots key refusal), and 4 packaged members were at older pins than the signed list | msg 041948Z |

## Completion test

NOT DONE: 0 of 11 complete. 9 REACHABLE, 2 UNREACHABLE (ADVI_BILLING and NFRA_OPSWKF: no COO seat; the act is MSTR's seating).

## Acts only Andrew can do

None outstanding beyond his discretion grant. Test ticket TCK-20261009-a1052909 stays open for any person to close (no seat holds a human sign-in);
nothing waits on it.

## Compiler Tools

`project.json` placement census; `prd-signoff.py status`; opal-users-v2 scan (counts only); `git patch-id`; `missions-tree-index.py`; safe-commit.sh.
