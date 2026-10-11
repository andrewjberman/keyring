# Deploy Completion Record
**Date opened:** 2026-10-11T11:10:38.738634+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-ss-5: ONE additive store write -- the candidate universe at its new dated key amgt/harvest/gold/candidate_universe/date=2026-10-02/candidate_universe.json (risk WORLD; GO 2.0.0_SA_COO~R1 msg 3787). BOTH NEVER-WIDEN HALVES READ WHOLE: COO half NEVER_WIDEN_ROUND93_UNIVERSE_KEY_COO_HALF.md (msg 3769), CTO half (msg 3770). Run from a detached checkout at 3336af9669 (universe.py fcd61615156e, qq-2 @9d4236533c an ancestor). Expected object: vintage 2026-10-02, 2856 rows, 3759160 bytes, sha256 8e652b082ef234b057be3ea18cfcc700be249c1bb410828beb8526b2d9042ebb, equal to round 91's PP3 cache after pooling; the dry build's digest is compared BEFORE the put and a difference is a STOP. date=2026-08-06 stays at D.ZdXaKfQXNoHYeZ7.58h0t7peUmVcKB. Rollback: the new key is a new object, its removal is the owner's call and is NOT done by this seat (no delete); the old key is untouched.
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | PRE-ACT STATE read by this seat: the pin, universe.py blob, qq-2 ancestry; the six scanner files' asOf; VersionId of date=2026-08-06 and the new key absent; the open-deploy sweep for candidate_universe | ancestry and blob reads, six asOf values, the VersionIds, the sweep denominators |  | OPEN |
| L2 | verify | the DRY BUILD in memory at the pin: vintage, rows, pooled bytes and sha256 equal to the pair's; the model-block directory's file count and the added rows' keys; equal to the PP3 cache after pooling | the printed digest comparison |  | OPEN |
| L3 | activation | the ONE write: python -m lib.research.peers.universe --refresh with AMGT_PEER_UNIVERSE_CACHE unset; target absent -> put-if-absent with document-sha256 and schema-version metadata | the receipt and the refresh output lines |  | OPEN |
| L4 | verify | read-back of the new object (size, digest, metadata, VersionId) and date=2026-08-06 unchanged (VersionId, one version) | head of both keys |  | OPEN |
| L5 | verify | AC1 r93_universe_pool.py --prior-version-id YES (U1-U4); AC2 the no-regression arm YES with the function CodeSha256 unchanged | the verdict lines |  | OPEN |

## Log

- 20261011T111038Z OPENED by 0.7.0_AE_CloudOps~RA1 with 5 leg(s)
