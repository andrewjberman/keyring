# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 128 (2026-10-18 16:57Z to 17:27Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Between ticks

- **The BP drain at site Z LANDED** (BBGTerminal msg 35764).
  - One message, exit 0; queue 1/0 -> 0/0.
  - 8 requests (4 reference, 4 historical; 159 security x field).
  - 5 objects (bronze refdata/histdata/bestdata, model_block 559,911 B, status.json); BP status LANDED at 17:06:20Z; no raw prefix.
  - **Finding for DEMQUE Z-S8:** the health read pulled real data on both channels, so HISTORY ANSWERS. The 14:00Z probe's 0 rows
    were security-specific (a muni with no PX_LAST), not a channel outage. That supports t76's inconclusive-probe design.
  - Relayed to dell1 W1 and Q1 via MSTR~Z (35765).
- **NFRA1's correction** (msg 35767), with commit 966c4d6865 LOCAL:
  - **CT4** is 272 Graph-backed calls, all ok, with 0 GraphHostRefused, not 1. Its classifier missed helper-routed tools. No verdict
    changes.
  - **Row Z-S395 is a regression from OG-ap-40, which I signed.** `probe_listener`'s `Config(access_log=False)` empties the GLOBAL
    `uvicorn.access` logger. The service's POST /mcp journal lines fell from 157-171 per window to 0 at the OG-ap-40 deploy, while
    traffic continued (audit lake 291-300 per window). So the "0 /mcp requests" readings since 10:31Z measured the silenced logger,
    not the traffic.
  - **RULING (35769 to COO~O):** a repair cell this round.
    - The listener must not touch `uvicorn.access`.
    - Criteria: the journal shows POST /mcp under traffic, counted against the audit lake over the same window, and listener lines
      are distinguishable.
    - It ships in a batched release under its own never-widen, ahead of OG-ev-7.
  - **Lesson for my own halves:** a count read from a log the release itself configures is not evidence of traffic. The next half
    asks for an independent second source, such as the audit lake.

## Tick 128 (17:27Z)

0 unread; 4 open (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| check_inbox | 0.8 measurement | 0 unread |
| open-calls.py list | scope | 55 rows, 4 open |
