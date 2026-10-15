# SELF-DRIVE sitez open calls -- tick 32 (2026-10-15 03:50Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 32 (since tick 31 @077974f09f). **state: ARMED**

## Measurement
- Inbox: 1 at tick time (34326, read and acked); also acked since tick 31: 34322.
- `open-calls.py list`: rows=45, **open=7**, unchanged, all person acts with citations.

## Calls ruled and acts since tick 31
| item | ruling / act | carrier |
|---|---|---|
| CloudOps~Z 34322 / row Z-S137: `app/typed_scope.py` is outside OG-ap-19's take-list, yet the release cannot start without it | REC route 1 (amend the take-list); the issuer ruled route 1 (A2 @68a7d83f97); cut templates now enumerate imported seams | msg 03:44Z |
| OG-ap-19 never-widen (13 G3/G6 tools, two read grants) | CTO half SIGNED at ee23dd004c; the G6 news read on the INSTANCE role accepted as a recorded exception (PRD v3.9), with a follow-up cell owed to move it to the internal reader | @8c84e01428; msg 03:53Z |
| OG-cp-1 (C-PERSON reader, un-parks MC Portal) | cut by COO~O `a8e22ed56d` | -- |

## Completion test
NOT DONE: 7 open, all person acts; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting (21d9 covers 21c5, 8ed7, f0d2): human look + Opal Bloomberg login (TO-MP-z-6 / TO-MP-v-2 G-2ND).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate) (TO-MP-c-2).
3. One Teams message from his account (a519).

## Compiler Tools
`.tools/open-calls.py list`; `git diff --stat`; `.tools/prd-signoff.py status`; broker; `safe-commit.sh`.
