# SELF-DRIVE sitez open calls -- tick 34 (2026-10-15 05:50Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 34 (since tick 33 @cc5946947d). **state: ARMED**

## Measurement
- Inbox: 0 unread (acked since tick 33: 34342; two OPEN-CALLS-SCAN notices read).
- `open-calls.py list`: rows=45, **open=7**, unchanged, all person acts with citations.

## Calls ruled since tick 33
| call | ruling | carrier |
|---|---|---|
| XA-20261015T050145Z-7f22 (dell2 CTO, IRPT_ANLREQ): delete ~20 GB of throwaway worker/release folders | (b) apply the d503 class ruling: merged clean worktrees removed by MSTR~DELL2 on the standing word; the dirty wk-irpt-anlreq-74 stays with COO~Y2; plain folders are ONE act for Andrew | @aae79d7aa8 |
| XA-20261015T054033Z-cdc4 (dell2 CTO, IRPT_DASHBD): who pins the filled-report export object | (a) the server pins at submit per the signed IB-pr-551 packet; the page sends the client id only; the build conforms; test that a forged client pin is ignored | @00632d9586 |
| CloudOps~Z 34342 / row Z-S139: an IAM policy applied during OG-ap-20 Phase A (unsigned, ~4 min), rolled back under a ledger | rollback accepted (86499b9237); Phase A never invokes apply, and negative checks are plan-only with kept output; a ledger-aware safe-apply refusal PROPOSED to CVO, not built | msgs 05:28Z; issuer amendment A2 `679683cc41` |

## Completion test
NOT DONE: 7 open, all person acts; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting (21d9 covers 21c5, 8ed7, f0d2): human look + Opal Bloomberg login (TO-MP-z-6 / TO-MP-v-2 G-2ND).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate) (TO-MP-c-2).
3. One Teams message from his account (a519).
Plus, from XA-7f22 (dell2's queue): the plain-folder deletion on dell2 (recursive deletion is his act).

## Compiler Tools
`.tools/open-calls.py list`; `.tools/xadj.py show|rule`; `git log`; broker; `safe-commit.sh`.
