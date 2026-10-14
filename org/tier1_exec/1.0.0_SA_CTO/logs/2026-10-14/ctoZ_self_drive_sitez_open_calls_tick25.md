# SELF-DRIVE sitez open calls -- tick 25 (2026-10-14 20:50Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 25 (since tick 24 @ffbd41134b). **state: ARMED**

## Measurement
- Inbox: 0 unread (read and acked since tick 24: 34211, 34214).
- `open-calls.py list`: rows=45, **open=7**, unchanged, all person acts with citations.

## Calls ruled since tick 24
| call | ruling | carrier |
|---|---|---|
| COO~MP 34211: NFRA_MCPORTAL PC round 2, close or hold? (6 of 8 cells drained; F2 release waits on OPLGTW OG-cp-1) | HOLD as recommended; un-park condition OG-cp-1 RELEASED, then Andrew's People sitting; FWD-21/22 NOT_REALIZED; OG-cp-1 sequenced after the Friday set (told COO~O) | msgs 20:20-20:21Z |
| Relay 34214 (laptop CTO + CTO~DELL1): Security Analysis G6, site Z cycle runner without `sa` | the 10-13T23:53Z stop was HVST-bz-10 under a task order, not Andrew; his standing word keeps Seeking Alpha (09-29); NFRA_OPLGTW cuts it as a WORLD defect cell: read SA access first (Z-W37-S4, 402), re-register with sa, place the trading-day trigger for the four SA tables | PRD v3.8 @3bb7fb022e; msgs to COO~O and MSTR~Z 20:34Z |

## Surfaced to Andrew
- This box's Claude login: weekly limit 84 percent used at 20:09Z (first live `rate_limits` reading, MP-pd-5/6). Told in-session; he decides reset timing or a cut-back.
- If the SA access read fails, the renewal he named on 09-29 is his act.

## Completion test
NOT DONE: 7 open, all person acts; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting (21d9 covers 21c5, 8ed7, f0d2): human look + Opal Bloomberg login (TO-MP-z-6 / TO-MP-v-2 G-2ND).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate) (TO-MP-c-2).
3. One Teams message from his account (a519).

## Compiler Tools
`.tools/open-calls.py list`; `Get-ScheduledTask`; `git fetch`/`git show`; broker; `safe-commit.sh`.
