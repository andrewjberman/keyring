# Deploy Completion Record
**Date opened:** 2026-10-11T11:21:12.412840+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-ss-6: ONE batch over the 243 MEASURED subjects writing 243 NEW peers/v1/<key>/2026-10-11T1125Z.json objects, no subject listing its own company (risk WORLD; GO 2.0.0_SA_COO~R1 msg 3798). BOTH NEVER-WIDEN HALVES READ WHOLE: COO half NEVER_WIDEN_ROUND93_PEERS_REBUILD_COO_HALF.md (msg 3783), CTO half signed on both classes (msg 3786): 12 member lists change, 231 equal, member count unchanged for 243. Run from a detached checkout at f40dd163cc (engine.py 15a70af793ec, peers_rebuild.py 4af49bd385f8; ss-3 and qq-2 ancestors) with python -m lib.research.api.peers_rebuild (NOT lib.research.peers.engine), the universe read from the pool date=2026-10-02 (ss-5). A subject outside the 12, a moved count or an unlisted member field is a STOP; rollback is a NEWER partition built from the prior engine code, never a delete. The prior partition 2026-10-11T0707Z stays whole.
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | PRE-ACT STATE read by this seat: the pin, the two blobs, ss-3 and qq-2 ancestry, the cache override unset; the prior partition's object count and VersionIds; the new partition string free; the open-deploy sweep for peers/v1 | ancestry and blob reads, the counts, the VersionIds file, the sweep denominators |  | OPEN |
| L2 | verify | BASELINE and DRY BATCH: r93_self_peer_census.py --write-baseline compared with the issuer's PEERS_BASELINE; the dry batch (no --write-pool) compared with the half's table member by member; the ten single-subject dry runs | 243 subjects, 231 equal, 12 differing with removed and added members equal to the table, counts unmoved |  | OPEN |
| L3 | activation | the ONE batch: python -m lib.research.api.peers_rebuild --as-of 2026-10-11 --write-as-of 2026-10-11T1125Z --write-pool, cache override unset, the universe from the pool | UPLOADED 243 of 243 with read-back 243 of 243, SHARED-DEFECT 0 violations |  | OPEN |
| L4 | verify | the new partition read back: 243 objects at the new partition, the prior partition's 243 objects still in place at the L1 VersionIds, no other key written | the counts and the VersionId compare |  | OPEN |
| L5 | verify | the member-by-member compare of all 243 subjects' live /peers against the baseline: exactly the table's 12, every other member and field equal | the compare with each changed member before and after |  | OPEN |
| L6 | verify | AC1 r93_self_peer_census.py --baseline YES (S1-S4); AC2 the no-regression arm YES with the function CodeSha256 unchanged; AC3 r92_minor_unit_census YES | the verdict lines |  | OPEN |

## Log

- 20261011T112112Z OPENED by 0.7.0_AE_CloudOps~RA1 with 6 leg(s)
