# /self-drive dell2-box -- tick 103 (2026-10-17 ~14:27Z-14:57Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** the time since the tick 102 log (@9bd0d9f4bf). There is a substantive delta. state: ARMED. Inbox: 0 unread.

## Acts taken

| act | carrier |
|---|---|
| The Cottonwood re-land pair CTO half was SIGNED against sha256 37ce1e48: eight gold days, one republish, with gained following days allowed in Act 4. It was then **SUSPENDED before apply**, because `~D2` measured that the derive sums overlapping 14-day transaction partitions. On 07-24 there are 3,328 rows against 277 distinct IDs, so the served Cottonwood flows are inflated 8 to 13x. | @e5d081d262, @a5f1769c0b |
| dell1's convert of 07-27 and 07-29 is done (897 and 896 accounts). Its retry sweep re-landed those days' bronze with fuller deliveries (3 to 1,553 and 1 to 1,552 rows). dell2 WAIVED the letter of "no bronze change", because the fuller-delivery rule covered it. | msg 10584 |
| dell1 (msg 7612): no re-pull is needed for 08-19, 09-24 and 09-25. Those trades sit in later partitions by trade_date. | relay |
| RULED: ONE reader fix (partitions D to D+14, filter trade_date = D, dedup on transaction_id), folded with `~F2`'s transaction stage as one code release. Then ONE all-days rewrite pair from 07-10 and one republish. A surprise row is owed by `~D2`. A read-only check of the 49F and Inflection derives for the same overlap is due today. | msgs 10587-10592 |

## Served-output note

Served Cottonwood returns for accounts with flows are WRONG today. Only Opal staff in Global view can see them; no Cottonwood advisor has a grant. The fix is sequenced above. Andrew has been told.

## Acts only Andrew can do

- **449e: the Retry on TCK-20261017-5af976ff in PROD Ticket Center.** Citation: ticket_center lambda_function.py:1750-1753.
- 3c22: lift or keep C-V1. Citation: IRPT_YCDGEN PRD :312, "on Andrew's word only".
- c02c is POSTPONED.
