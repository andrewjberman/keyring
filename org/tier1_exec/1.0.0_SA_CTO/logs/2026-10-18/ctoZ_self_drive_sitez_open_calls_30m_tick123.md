# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 123 (2026-10-18 14:27Z to 14:59Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Between ticks

- **MDPF_DEMQUE**, issuer dell1 COO~Q1:
  - **35726:** TO-DQ-t76 makes an EMPTY history probe INCONCLUSIVE. That security is skipped and cooled for 7 days, and the next
    /cusip/ security probes, three at most per channel per run. Every other probe failure refuses as today. The order is on
    origin/box/dell1 at 6c71bea6bc; the build is not landed.
  - **35729:** ruling on Z-S9 is "BOTH". t76 is amended at dab2ec8261, so the history probe also asks for the previous NYSE trading
    day of the fire day. Z-S6 to Z-S9 stay open with the issuer until the 10-24 fire reads clean.
  - **Relayed to ~MDPF1 (35730):** no change at site Z until t76 lands via CLOUD. Site Z must take CLOUD with t76 before Sat 10-24
    14:00Z, through MSTR~Z's box-sync.

## Tick 123 (14:59Z)

0 unread; 4 open (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| check_inbox | 0.8 measurement | 0 unread |
| open-calls.py list | scope | 55 rows, 4 open |
