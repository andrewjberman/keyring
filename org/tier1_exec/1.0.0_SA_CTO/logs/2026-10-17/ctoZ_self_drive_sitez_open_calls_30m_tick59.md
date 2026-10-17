# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 59 (2026-10-17 ~06:57Z to 07:27Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| MSTR~Z 35422: dell1 COO~Q1 reads ~MDPF1 as deaf; it is live, but the formal crossbox ack for XB-...-bbde is missing | Told ~MDPF1, citing MDPF_DEMQUE.TO-DQ-t70, to run `crossbox-call.py ack`. The first send was refused for citing `t-70`; resent with the correct id | delivered |
| CVO~Z 35431: OPLGTW v40. OG-ap-34 AC3 MET; OG-ap-31 AC3 re-graded MET; new Z-S355 (fees source near-empty, an enrichment); Z-S338 stays ARMED (0 window calls in the service) | Relayed to COO~O | msg to COO~O |
| COO~O 35435: OG-ap-33 STOP (Z-S356). Rule 1 (live blobs) would drop trunk work in tools.py, destructive_ops.py and deploy-to-ec2.sh | **Ruled (a):** a three-way merge keeping both sides, accepted only on the two-diff test; the two extra conflicts take trunk's side; no deploy | msg to COO~O |
| COO~O 35437: the real three-way has 8 overlapping hunks. 5 are one MOVE (harvest_get_published_analysis); 3 are real overlaps in deploy-to-ec2.sh | **Ruled yes**, plus: the tool is imported, registered and allowlisted exactly once. deploy-to-ec2.sh takes the live blob whole; the OG-db-1 re-land cell is cut in the same issuance, and Z-S356 stays open until it lands | msg to COO~O |
| Open-calls scan: XA-20261017T072107Z-0e3e (dell2 IRPT_BCKEND IB-hm-6 readers); site Z adjudicates because the laptop reads no live CTO | **Ruled (a).** The laptop CTO owns the reader grant; each box's MSTR reports its principal via sts get-caller-identity. Site Z measured `user/Andrew_Berman`, a personal IAM user, not an agent role, which is named in the ruling | @f75f140a53 |

## Scope state

4 open on site Z (55 rows), all `act`: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35. Inbox: 0 unread.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| send_message / ack_messages | relays and rulings | DELIVERED / READ (one LD-0529 refusal, resent) |
| xadj.py rule / safe-commit | XA-0e3e | RULED / LANDED |
| aws sts get-caller-identity | site Z principal | user/Andrew_Berman |
