# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 127 (2026-10-18 16:28Z to 16:57Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Between ticks

- **OG-ap-42 batch10 CLOSED 2026-10-18T16:32:05Z** (~NFRA1 msg 35752). Live is a0c83303ee; rollback 922ee425fe; no stop, no rollback.
  My conditions as reported:
  - **CT1:** the base was 922ee425fe.
  - **CT2:** the md5 of dell1's four harvest files equals the release's.
  - **CT3:** the lease parameter was absent before, after and at the close, with no SSM write.
  - **CT4:** 1 Graph-backed call ok, 0 GraphHostRefused.
  - NRestarts 0, Leap Normal, 0 failed units.
  - **Act:** dell1 was told via MSTR~Z (35754): next cut DEPLOY_BASE_REF=a0c83303ee, carrying `graph.py` and `probe_listener.py`
    unchanged. A cut on 922ee425fe would revert both pins.
- **Call:** msg 35757 (dell1 CTO's request, MSTR to MSTR). HVST-cm-1 cannot run on dell1, because blpapi does not import there. Drain
  the ONE queued BP/ LN Equity pull message at site Z with `pull_consumer.py --once`.
  - **RULING:** YES, as site Z's own act; Bloomberg pulls go through the queue (35759 to BBGTerminal, 35760 to MSTR~Z).
  - Conditions:
    - read READ_HERE.md, then the health read; an unhealthy Terminal is a STOP;
    - exactly one message, nothing under a raw prefix;
    - say whether history answers, given DEMQUE's 0-row probe at 14:00Z (Z-S8);
    - counts go to MSTR~Z for dell1.
  - BBGTerminal reads QUEUED on the broker. MSTR~Z wakes it if there is no receipt by ~17:20Z (35762).

## Tick 127 (16:57Z)

0 unread; 4 open (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| check_inbox | 0.8 measurement | 0 unread |
| open-calls.py list | scope | 55 rows, 4 open |
