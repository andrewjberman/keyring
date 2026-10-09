# Drive log -- 2.0.0_SA_COO~AI -- NFRA_OPALAI -- 2026-10-09 15Z (site Z, host opal_bloomberg)

**archetype:** COORDINATE

Loop `/canonical-drive NFRA_OPALAI` 10m, cron `1c05e7b9`. Lease FULL; L7 EXECUTING, round 2; parked on a sovereign call.

| time | act |
|---|---|
| 15:0xZ | UB-cb37 (CRO): make the two human inputs one card for Andrew. Card committed in the run file @68ab46b72e and queued as open call `sitez-20261009T150500Z-4d5a` (scope CROSS-BOX, risk WORLD) |
| 15:1xZ | CTO fold of UB-cb37 (`CTO_RULING_UNBLOCK_OPALAI_UBCB37_ONE_CARD_FOR_ANDREW_20261009.md`): the card is the carrier; on a yes, one message to Alyssa sent as Andrew's principal and labelled as an agent's; arm (a) then fires on HER question; on a no, the round parks |
| 15:4xZ | CVO signed UB-cb37 (@f59dbc4f71) and replaced ruling 5: the counter is not ticked while the card is open, until `--owed-call` lands. Resumed |
| 15:5xZ | `unblock.py tick --owed-call` landed; ticks read `WAITING CALL ... OPEN`, empty=0 |
| all ticks | watcher `poll_addressed_teams_messages`: 0 new messages since 13:20Z |

## Next

Andrew's answer on call `4d5a`. On a yes: the one message to Alyssa (or Andrew asks her), then arm (a) on her question
within 900s with J2 pinned. Any fresh message from an un-profiled sender fires arm (b), after the profile probe.

## Compiler Tools

- `open-calls.py add`: queued the card; its CALL-SCOPE read CROSS-BOX/WORLD and routes it to cross-adjudication.
- `unblock.py tick --owed-call`: holds the counter while a sovereign call is open.
