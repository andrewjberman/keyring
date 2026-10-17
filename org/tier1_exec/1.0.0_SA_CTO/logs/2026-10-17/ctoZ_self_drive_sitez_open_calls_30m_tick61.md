# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 60-61 (2026-10-17 ~07:27Z to 08:26Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| Tick 60 (07:57Z) | Quiet | drive_ticks line |
| CVO~Z 35442: the Z-S336 disarm evidence is verified (base guard equal twice, host md5 139/139), but the row gate refuses the clock: OG-ap-33 and OG-db-2 are not terminal, and exception 21533 covers only ap-33 | Extended 21533 to OG-db-2 for this clock only; relayed to COO~O (incl. Z-S356 needs the issuer's ruling) | msgs to CVO~Z, COO~O |
| CVO~Z 35446: the gate has no NFRA_OPLGTW exception slot, and Z-S356 has no disposition yet. (a) wait for OG-db-2, or (b) the override | **Ruled (a)**; the 35443 extension is withdrawn and no override is authorized. The hazard is already disarmed on measured evidence. COO~O was told the clock is NOT written; Z-S358 (round-tag v39/v40) is the CVO's | msgs 35447/35448 |

## Scope state

4 open on site Z (55 rows), all `act`: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35. Inbox: 0 unread.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| send_message / ack_messages | the Z-S336 rulings | DELIVERED / READ |
