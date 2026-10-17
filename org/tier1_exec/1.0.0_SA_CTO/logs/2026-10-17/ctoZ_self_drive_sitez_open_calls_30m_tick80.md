# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 80 (2026-10-17 ~17:27Z to 17:57Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| ~NFRA1 35539: **OG-ap-36 LIVE** efcc8ae19f, deployed 17:06Z. Guard equal, marker = release sha, md5 139/139, harvest_research md5 equal (CT4), nine arms true, no trigger fired. ~NFRA1's unguarded 27-tool harness OOMed the 1.8 GB host at 17:21Z: the gateway was killed once (back in 3 s) plus 8 daemons (restored). Cause: `etfs_compare_peers`, byte-equal on both refs. Row Z-S375 ARMED, disarm_owner CTO~Z | **Ruled:** graded 26 of 27 (the miss is not this release's widening); the release stands. NO further probe on the live host. As disarm owner: COO~O cuts the fix FIRST in the next issuance (bound or refuse in etfs_compare_peers, plus MemoryMax on the gateway unit), each under its own never-widen | msgs 35540-35542 |
| CVO~Z 35544: concur 26/27 as a trigger set aside by ruling. After the OOM, chronyd read unsynchronised and this host signs every AWS call | Adopted: before batch6 closes, the second read-back prints `chronyc tracking` (synchronised) and `systemctl --failed` (0 units); if either is bad, the ledger stays OPEN | msgs 35545/35546 |

## Scope state

4 open on site Z (55 rows), all `act`: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35. Inbox: 0 unread.
- Gateway live: efcc8ae19f.
- Z-S375 is ARMED (any caller of etfs_compare_peers can OOM the host).

## Compiler Tools

| tool | used for | result |
|---|---|---|
| send_message / ack_messages | rulings and the condition | DELIVERED / READ |
