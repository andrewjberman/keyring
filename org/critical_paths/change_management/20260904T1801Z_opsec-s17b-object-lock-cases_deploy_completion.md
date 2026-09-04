# Deploy Completion Record
**Date opened:** 2026-09-04T18:01:34.292569+00:00
**Status:** OPEN
**Deploy:** TO-OP-S-17B: enable Object Lock (GOVERNANCE, 365d default retention) on opal-security-evidence in place; FORWARD-ONLY, the 839 existing case objects are NOT re-written
**Authored by:** 0.7.0_AE_CloudOps~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | PRE-ACT at this vintage: versioning Enabled, no existing lock config, cases/ object count re-measured client-side, key->LastModified map captured for the no-rewrite census | live reads with timestamps |  | OPEN |
| L2 | git | SITEZ commit adding aws_s3_bucket_object_lock_configuration + correcting the two comment blocks the change falsifies | commit hash |  | OPEN |
| L3 | activation | safe-apply on the opsec root; plan read first showing 1 to add, 0 to change, 0 to destroy and ZERO forces-replacement on the bucket | plan + apply output |  | OPEN |
| L4 | verify | POST: get-object-lock-configuration read live; get-object-retention on a PRE-EXISTING object (no retention) AND a NEWLY-WRITTEN one (GOVERNANCE); LastModified census unchanged for the pre-act keys; bypass holders enumerated by SIMULATION | live reads pasted |  | OPEN |

## Log

- 20260904T180134Z OPENED by 0.7.0_AE_CloudOps~X with 4 leg(s)
