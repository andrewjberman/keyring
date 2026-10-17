# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 71 (2026-10-17 ~12:56Z to 13:26Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| ~NFRA1 35483: OG-ap-36 Phase A addendum (CT1). Everything else PASSES: health longest 0.082 s over 98 probes; partition_rows and fence_excluded equal on 6/6. **STOP:** under a 0.5 s gate wait the refused second call answers empty with `absent_reason` null, because `client_core._answer` overwrites it (row Z-S372); ~NFRA1 recommended accepting | **Ruled: cut now, not later.** This release makes the line reachable, and an empty refusal reads as "no transactions", a failed retrieval returning a value. Proportionate re-run: the diff, the ten window files and CT1; no memory gate. The halves re-sign | msgs 35484-35486 |
| ~NFRA1 35488: the release tree takes trunk bytes whole, so the fix must be a trunk cell | Agreed: COO~O cuts the trunk cell and sends a re-run GO with the new trunk_sha | msgs 35489/35490 |
| CVO~Z 35491, row Z-S373: the overwrite is wider and LIVE. `_absent` never sets `_absent_reason`, so all five `no_partition_at_as_of` refusals are nulled on 9d5b712557 today | Adopted: the mapping keeps the adapter's absent_reason whenever meta's is None, and the test asserts both window_read_busy and no_partition_at_as_of. It rides OG-ap-36 | msg to COO~O |

## Scope state

4 open on site Z (55 rows), all `act`: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35. Inbox: 0 unread. OG-ap-36: nothing deployed; live
is 9d5b712557; the dell1 hold stands until batch6 closes.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| send_message / ack_messages | the Z-S372/373 rulings | DELIVERED / READ |
