# /self-drive SITEZ fabric (relaunch) -- tick 42, 2026-10-09 ~00:3xZ to ~01:4xZ -- `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 41's log @3322f72915 to 01:4xZ. Cron `812ad509`.
**state: ARMED**. Three of the five have left the scope for DELL1 on Andrew's order (record @b7361ceb2a). The loop ends
STOPPED-BY-OPERATOR when the last two leave.

## The DELL1 move, measured (01:38Z)

| project | site-Z tree | origin box/dell1 | state |
|---|---|---|---|
| DSGN_AMGTV1 | `fabric: dell1` | dell1, `2.0.0_SA_COO~D1` | MOVED; site-Z `2.0.0_SA_COO~D` stood down and deregistered |
| AMGT_HARVST | dell1 | dell1, `~W1` | MOVED |
| AMGT_RESAPP | dell1 | dell1, `~R1` @7dde3e8491 | MOVED; analysis and hand-over @c249be336b |
| AMGT_CORPUS | site-z | site-z | round 40 closes on the 2026-10-09 13:00Z fire; **LANE-DARK** |
| ETFS_RIVALS | site-z | site-z | round 28 closes on the 2026-10-09 11:00Z acts; **LANE-DARK** |

**LANE-DARK cause:** `2.0.0_SA_COO~X`, `~RV`, `~H` and `3.0.0_SA_CVO~RV` have had no process since ~01:04Z, and the spawn audit has
no KILL line for them (`0.0.0_AB_MSTR~Z` msg 32239). This seat read MCP pids 25892 and 25044 as gone. **Asked** `0.0.0_AB_MSTR~Z` to
respawn `~RV`, `~X` and `3.0.0_SA_CVO~RV` (open rounds, signed acts, and CORPUS's OPEN ledger `amgt-corpus-r40-ap10b`), not `~H`, and
to record the cause if a read finds it. HARVST's Seeking Alpha leg is down at checkpoint (133 done) until Andrew names the site-Z
producer owner.

## Calls ruled in the window

| call | ruling | carrier |
|---|---|---|
| AMGT_RESAPP round 79 slug (`3.0.0_SA_CVO~Z` 32207) | analysis R1-R5: ASML NA FWD-18 is a producer fault; percentage-heading parse; FWD-1/FWD-7 graded by a walk on DEV 84e13d0f; no new walker lease; Z-S374 placed on the next scoped-api deploy | `AMGT_RESAPP/ledger/ROUND_ANALYSIS.round79.md` @c249be336b |
| Bloomberg seat `--strict-mcp-config` (Andrew: "adjudicated by the CTO internally") | YES, exactly opal-gateway-bbg, bloomberg and opal-agent-comms; AMENDMENT 1 takes `0.0.0_AB_MSTR~Z`'s spec fix and corrects read 4; `1.0.0_SA_CTO~O` withdrew its sequenced ruling | `deliverables/CTO_RULING_BG_SEAT_STRICT_MCP_CONFIG_20261009.md` @e46928ecc8, @6abc00a2d5 |
| Two RESAPP Bloomberg asks (ABNB model block; ICT identity read) | route both through dell1's backfill queue under Andrew's ~22:4xZ words; no ad hoc call. They were already HELD for Andrew before the laptop CTO's relay, the tool has no un-hold, so his word closes them | `deliverables/CTO_RULING_RESAPP_TWO_BBG_ASKS_TO_BACKFILL_QUEUE_20261009.md` @10e525c7de |

## Acts only Andrew can do (cited)

- Close the two RESAPP Bloomberg calls with his word (CLAUDE.md vendor rule; they are HELD on site Z's list).
- Name the site-Z producer owner (this seat recommends `0.7.0_AE_CloudOps~Z`); the HARVST collector stays on Z unless he redoes the
  publisher sign-ins on DELL1 (his login).

## Compiler Tools

- `sequence-check.py --project` for the two remaining projects: LANE-DARK on both, cause read from liveness and process ids.
- `git show origin/box/dell1:<project.json>` x5: 3 of 5 at `fabric: dell1`.
- `open-calls.py hold`, `close` (REFUSED: CROSS-BOX without CLOSED-BOTH), `xadj.py open` (REFUSED: already escalated). Both
  refusals are the tools working as built.
