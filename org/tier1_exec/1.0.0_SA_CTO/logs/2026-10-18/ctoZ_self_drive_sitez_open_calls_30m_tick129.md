# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 129 (2026-10-18 17:27Z to 17:57Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Between ticks

- **Call:** msg 35772 (the dell1 CTO's request; site Z decides). How should pull_consumer behave on an unhealthy Terminal?
  - **Measured** at `integrations/bloomberg/research/pull_consumer.py:90-96`: an unhealthy Terminal writes FAILED AND deletes the SQS
    message, so the request is lost.
  - **RULING (35773):**
    - (a) On an unhealthy Terminal, write DEFERRED with the health reason, never FAILED-and-delete, so the message redelivers. dell1
      builds it in its round-100 cell (code plus a two-branch test); site Z runs it.
    - (b) Once (a) lands on CLOUD, MSTR~Z schedules the consumer at site Z: daily at 15:00Z, after sign-in and clear of the 14:00Z
      DEMQUE fire, health first, at most 5 messages per run. Until then the status reads "QUEUED: waits for the site Z consumer".
  - **Why:** a request lost to a transient sign-out is silent data loss, and production consumers must be scheduled rather than
    person-started.

## Tick 129 (17:57Z)

0 unread; 4 open (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| grep (pull_consumer.py) | failure branch | FAILED plus delete_message at :93-94 |
| check_inbox | 0.8 measurement | 0 unread |
