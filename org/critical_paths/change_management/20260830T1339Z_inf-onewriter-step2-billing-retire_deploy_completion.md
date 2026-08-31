# Deploy Completion Record
**Date opened:** 2026-08-30T13:39:36.103373+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260830T140459Z
**Deploy:** INF-ONEWRITER Step 2: retire the dispatch path's billing leaf from CHAIN_PULL (s3-pull-runtime artifact)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| dispatch-sh | s3-prefix | s3://opal-data-inf/code/gold/orion-gold-dispatch.sh | ETag == the post-edit MD5 c18c2ba22a07bdb34f681541a65a6d1b, read back from s3api after upload | UPLOADED 14:03:13Z to s3://opal-data-inf/code/gold/orion-gold-dispatch.sh (110.7 KiB, 113,320 B). TWO INDEPENDENT ORACLES, not one: (1) HASH -- live ETag reads 46dce6c7f1ce4987bddf9a225efd733a, EQUAL to the md5 of the blob at origin/CLOUD 5850d0f9ee, so the served bytes equal HEAD exactly rather than merely equalling some origin commit; (2) CONTENT -- the object was DOWNLOADED and read: CHAIN_PULL carries 19 INF_ tokens, INF_API_SILVER_BILLING occurs once (catalog row only), 0 CR bytes. CORRECTION TO THIS LEG AS OPENED: the expected ETag recorded at open was c18c2ba22a07bdb34f681541a65a6d1b, which was the md5 of the pre-annotation worktree; the annotation commit 6fc3f50b64 superseded it and the correct expected value was re-derived from the COMMITTED blob before the upload, not carried forward from the stale worktree figure. PRIOR STATE, verified before the write: the old object ETag f82a41505c75faa42d6f6e47a283b013 equalled the md5 of the pre-cut HEAD blob, so deployed == repo with ZERO prior drift and exactly one change landed. Runners served: inf-gold-layer-runner and inf-gold-qa-runner, both s3-pull-runtime on this key. | CLOSED 20260830T140459Z |
| commit | git | data/inf/scripts/gold/orion-gold-dispatch.sh | committed via safe-commit, hash stated, push state measured by ls-remote + is-ancestor | Committed 09ffccc6ef (the cut: INF_API_SILVER_BILLING out of CHAIN_PULL, 20 -> 19 tokens) and 6fc3f50b64 (the ad-hoc hazard annotation CTO 87575 asked for, comment only). BOTH ON ORIGIN, measured by git ls-remote + merge-base --is-ancestor per commit at 14:01:25Z against origin/CLOUD 5850d0f9ee33e7aea62909507f0934b1aab2ae77 -- ancestry, not a tip comparison. The PUSHED blob was read directly, not inferred from the commit subject: INF_API_SILVER_BILLING occurs exactly ONCE in it (the retained catalog row); 2 would have meant the chain token survived. | CLOSED 20260830T140459Z |

## Log

- 20260830T133936Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20260830T140459Z LEG commit closed: Committed 09ffccc6ef (the cut: INF_API_SILVER_BILLING out of CHAIN_PULL, 20 -> 19 tokens) and 6fc3f50b64 (the ad-hoc haz
- 20260830T140459Z LEG dispatch-sh closed: UPLOADED 14:03:13Z to s3://opal-data-inf/code/gold/orion-gold-dispatch.sh (110.7 KiB, 113,320 B). TWO INDEPENDENT ORACLE
- 20260830T140459Z CLOSED -- all 2 legs proven
