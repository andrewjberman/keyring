# SELF-DRIVE sitez open calls -- tick 29 (2026-10-15 00:51Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 29 (since tick 28 @3ee3e4b29a). **state: ARMED**

## Measurement
- Inbox: 0 unread at tick time; 34295 arrived and was acked in-tick.
- `open-calls.py list`: rows=45, **open=7**, unchanged, all person acts with citations.

## Landed since tick 28 (measured from commits)
- OG-yr-1 LIVE at `bf7ffb62f4`: AC1 and AC2 PASS (`bc07407d54`).
- NFRA_MCPINDEX: runtime catalog landed `0f40810fa2` (MX-c-14 complete, `feffbb3cf5`); naming-gate catalog branch in;
  round 16 issued `9068de2873` (MX-c-16, under the CVO's READ-OK conditions).
- NFRA_OPLGTW: OG-pt-5 cut (`mdpf_get_category_views` by catalog row, `cd23ff4f60`).

## Calls ruled since tick 28
| call | ruling | carrier |
|---|---|---|
| CloudOps~Z 34295 / row Z-S133: OG-ap-18 v3 would move /yearinreview's served md5 0d828b51 -> 3bbd5ab2 (eol=lf; same content) | ROUTE (a): adopt the LF form (reproducible from any clean checkout); amend yr-1's A3 oracle; CTO half covers (a) only | @b0a59f65f3 |
| OG-ap-18 v3 never-widen | CTO half SIGNED at 047f11aa99 on bf7ffb62f4; condition: reconcile the live registry 46 vs v1's 65 on one instrument before Phase B | @b0a59f65f3; msg 00:56Z |

## Completion test
NOT DONE: 7 open, all person acts; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting (21d9 covers 21c5, 8ed7, f0d2): human look + Opal Bloomberg login (TO-MP-z-6 / TO-MP-v-2 G-2ND).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate) (TO-MP-c-2).
3. One Teams message from his account (a519).

## Compiler Tools
`.tools/open-calls.py list`; `git log`/`git diff --stat`; broker; `safe-commit.sh`.
