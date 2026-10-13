# SELF-DRIVE cluster open calls -- tick 28 (2026-10-13 12:14Z, by hand; the 12:00Z cron fire did not arrive) -- state: ARMED

Arming record `ANDREW_DIRECT_20261012_125xZ_SELF_DRIVE_CLUSTER_OPEN_CALLS.md` @4698a8f59d. Ticks covered: 28. Last committed log:
tick 27 @006af9d693 (11:0xZ). Hourly-floor log; quiet tick.

## Measurements

- open rows: 18 (sitez 8, dell1 3, dell2 7, laptop 0), closed 96; fork 1 (sitez 1b36, the grant), act 17. No new row since tick
  26. inbox: 0 unread. No unacked crossbox call to a laptop seat. The opal-assets hold (HG-t-10 induce) runs to ~12:30Z; the
  read-back is dell1's.

## Calls since the last log

- RULED by the driver: 0 new. DESIGN FORKS at CRO research: 0. GOVERNANCE FORKS: 0 open.
- ACTS ONLY ANDREW CAN DO: 22 (tick-24 log), unchanged.

## Completion test

UNMEASURABLE (free-text scope); the loop ends on Andrew's stand-down word.

state: ARMED

## Compiler Tools

`python .tools/open-calls.py list --all --cloud`; `check_inbox`; `python .tools/crossbox-call.py list --open`; `safe-commit.sh`.
