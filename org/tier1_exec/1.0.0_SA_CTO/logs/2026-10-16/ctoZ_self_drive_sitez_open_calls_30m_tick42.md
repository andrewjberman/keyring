# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 41-42 (2026-10-16 ~21:58Z to 22:57Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| tick 41 (22:27Z) | quiet; 0 unread | drive_ticks |
| CVO 35285: **OG-ap-31 LIVE**. Guard MET (e4: owner passes with 0 store reads; every other branch 403); OG-ap-28 AC3 MET; OG-ap-31 AC3 PARTIAL (a 13-month request reads the newest 60 of 334 tx and 60 of 395 fee partitions, ~2 months, flagged); r39 MAY-CLOSE | Round 40 W1 RULED: measure the full read on the host (concurrency 16, p50/p95, bytes); raise the cap to 13 months if inside the request budget, else a continuation cursor. Refused: a monthly source (a new pipeline) and narrowing up front | @0a15d90223 |

## Scope state

5 open on site Z (55 rows), all `act`, all only Andrew can do; 0 forks: f0d2, 8ed7, def4, bd68 and 5b35. Inbox: 0 unread.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| safe-commit.sh | the W1 ruling, this log | OK |
