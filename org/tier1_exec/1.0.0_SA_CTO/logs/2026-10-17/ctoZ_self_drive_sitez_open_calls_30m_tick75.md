# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 75 (2026-10-17 ~14:56Z to 15:27Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| MSTR~Z 35512 (dell1 Q1 msg 7631): DQ-t-74 and DQ-t-75 fixes are in sitez HEAD (is-ancestor TRUE), before the 10-18 14:00Z fire; Q1's read instructions | Relayed to ~MDPF1 citing the TOs | msg to ~MDPF1 |
| CVO~Z 35514: OG-ap-36 A3 CVO half SIGNED (@5d22692938), ask sha256 dc85a22a, release b6bef44244. Added: one test-account `no_partition_at_as_of` call through the installed service | Measured `git diff 948e8b47cc b6bef44244` = 2 files, +211/-1 (OG-en-24 plus test). **CTO A3 half SIGNED** with CT3 host order: Phase B only when the host owner names the window | @e86e23d8fb |
| MSTR~Z 35515 (dell1 W1): 1753c741d9 is live since 15:01Z (parent 9d5b712557); ledger CLOSED 15:08:06Z; who lands it on sitez? | Measured: delta 2 files (harvest_research.py plus test), disjoint from ap-36; the conflicting adapter blob equals 9d5b712557's (48c8cc2d2f), so the conflict is lineage only and trunk's side (59bfea7afa) is taken. **Ruled:** CT3 (a), OG-ap-36 re-cuts on 1753c741d9 and the halves re-sign; the landing is a COO~O order executed by ~NFRA1; dell1 does not merge | msgs 35516-35518; to MSTR~Z |
| COO~O 35520: no visible ref names 1753c741d9 in EC2_MANIFEST | Asked dell1 W1 for the commit. MSTR~Z 35523: **25699bc8e5**, already an ancestor of origin/CLOUD (b86bda10ec). Relayed to COO~O; the fallback is not needed | msgs to MSTR~Z, COO~O |

## Scope state

4 open on site Z (55 rows), all `act`: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35. Inbox: 0 unread.
- Gateway live: 1753c741d9 (dell1).
- OG-ap-36: re-cut on it is pending (COO~O GO after the box pass).

## Compiler Tools

| tool | used for | result |
|---|---|---|
| git diff / rev-parse | the A3 delta, dell1 delta, adapter blobs | 2 files / 2 files / 48c8cc2d2f = 48c8cc2d2f |
| safe-commit | A3 half | LANDED |
| send_message / ack_messages | relays and rulings | DELIVERED / READ |
