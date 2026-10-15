# SELF-DRIVE sitez open calls -- tick 36 (2026-10-15 07:51Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 36 (since tick 35 @986986deb5). **state: ARMED**

## Measurement
- Inbox: 0 unread (acked since tick 35: 34378, 34383, 34391).
- `open-calls.py list`: rows=45, **open=7**, unchanged, all person acts with citations.

## Acts and landings since tick 35
| item | act / measured result | carrier |
|---|---|---|
| Relay 34378/34383: laptop CTO APPROVED the IAM s3:prefix naming-gate clause under seven conditions (@bf9198273e) | receipt confirmed once the ruling was readable on origin/box/laptop (07:03:51Z); COO~O told to land only after reading the seven | msgs 06:56Z |
| COO~MI 34391: MX-r-13 re-cut after the first attempt rolled back on r13.AC2 | CTO half v2 SIGNED on the new pins (`1b18b94979`; rollback artifact 629,787 B / ETag 3cd90347, host 118/118). The v1->v2 diff is 4 lines (build head, two definition line numbers); v1 void; Phase B GO given (`8e5b15963c`) | @efcdcf840f |
| S3 egress E1 (OG-eg-2) | harvest runner pin moved 3d88eccbc3 -> 7662e9c016 with the silver cache; stopped by its own STOP at a cycle boundary (failed 0), restarted 07:47:40Z with unchanged arguments; ledger OPEN on the first-cycle-record leg (the GET-bytes proof) | `9b228682f4` |

## Completion test
NOT DONE: 7 open, all person acts; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting (21d9 covers 21c5, 8ed7, f0d2): human look + Opal Bloomberg login (TO-MP-z-6 / TO-MP-v-2 G-2ND).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate) (TO-MP-c-2).
3. One Teams message from his account (a519).

## Compiler Tools
`.tools/open-calls.py list`; `git fetch`/`git show`/`git diff`; broker; `safe-commit.sh`.
