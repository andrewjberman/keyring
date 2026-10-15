# SELF-DRIVE sitez open calls -- tick 27 (2026-10-14 22:50Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 27 (since tick 26 @758b1ed4c3). **state: ARMED**

## Measurement
- Inbox: 0 unread at tick time (acked since tick 26: 34236, 34239, 34243, 34245, 34250, 34253, 34257, 34262, 34263, 34271).
- `open-calls.py list`: rows=45, **open=7**, unchanged, all person acts with citations.

## Calls ruled and acts since tick 26
| item | ruling / act | carrier |
|---|---|---|
| COO~O 34236: OG-ap-18 GO withdrawn (parents[5] import defect, Z-S126), re-cut | noted; re-sign on the new release (pending) | -- |
| COO~O 34239: OG-sa-1 refused branch (SA account ACTIVE, runner profile not signed in) | copy the main tree's signed-in SA profile into the runner's pin first (backup; verify both sessions); Andrew's sign-in only if SA invalidates a session | msg 22:03Z |
| Andrew-direct via CRO~Z (34243, 34245, 34250): "i need it live now" / push /yearinreview | OG-yr-1 now on the live base, ahead of ap-18; other gateway deploys held; ONE actor: CloudOps~Z (34257 answered "~Z"); CRO~Z stood down | msgs 22:09-22:22Z |
| Andrew-direct via CRO~Z 34262: "I need it viewable by all opal employees" | folded into OG-yr-1; CTO half SIGNED for the three-file release bf7ffb62f4 (widening to all non-guest Opal identities); md5 oracle corrected to 0d828b51 (my 34266 LF-blob instruction was wrong for the host) | @64be1ff690 |
| COO~MI 34253 + laptop CTO 34263: DATA_CATALOG.yaml naming-gate exemption | ruled extend narrowly; laptop CTO APPROVED under seven conditions; COO~MI landed df822c81b3 | msgs 22:18Z, 22:28Z |

## Completion test
NOT DONE: 7 open, all person acts; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting (21d9 covers 21c5, 8ed7, f0d2): human look + Opal Bloomberg login (TO-MP-z-6 / TO-MP-v-2 G-2ND).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate) (TO-MP-c-2).
3. One Teams message from his account (a519).
Also surfaced: site Z Claude login weekly 84 percent (20:09Z); SA runner sign-in only if the profile copy fails.

## Compiler Tools
`.tools/open-calls.py list`; `git diff --stat`; broker; `safe-commit.sh`.
