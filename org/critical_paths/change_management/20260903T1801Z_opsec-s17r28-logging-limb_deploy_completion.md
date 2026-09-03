# Deploy Completion Record
**Date opened:** 2026-09-03T18:01:39.068462+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-17R-28 logging limb, on THE Z-S49 RULING (shape (a) EXTEND) -- the access-logs target's ArnLike widens to TWO project-owned sources and opal-security-evidence begins delivering under security-evidence/. The incumbent source must keep delivering: that limb is a FAIL, never latency
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | s3_access_logs.tf ArnLike widened to a two-element list + s3_evidence.tf logging block uncommented, committed under 0.7.0_AE_CloudOps~S; baseline quoted | commit hash + baseline |  | OPEN |
| L2 | activation | safe-apply -- 1 to add (aws_s3_bucket_logging.security_evidence), 1 to change (aws_s3_bucket_policy.access_logs, UPDATE IN-PLACE never replace), 0 to destroy, and NO other existing resource -- ROLLBACK: revert the ArnLike to the single data_security value and remove the logging block, an in-place PutBucketPolicy back plus a DeleteBucketLogging on the NEW bucket only; the incumbent's logging configuration is never touched | apply output + enumerated changed-resource list with change types |  | OPEN |
| L3 | verify | S17R-AC1 limb 5 -- get-bucket-logging on opal-security-evidence now reads TargetBucket opal-data-security-access-logs with TargetPrefix security-evidence/ (NOT evidence-store/, which is taken by the incumbent); the criterion reaches 5 of 5 | pasted read |  | OPEN |
| L4 | verify | S17R-AC3 REGRESSION LIMB, which does NOT get an UNCOMPUTABLE branch -- evidence-store/ shows at least one object with LastModified AFTER this apply, proving aws_s3_bucket_logging.data_security still delivers. A silent stop here is a regression THIS task order caused: FAIL plus a row, never latency | list-objects-v2 with the apply timestamp |  | OPEN |
| L5 | verify | S17R-AC3 DELIVERY LIMB for the new source -- a real log object under security-evidence/, key and LastModified pasted, placeholders and test files excluded and named. Best-effort within hours, so an empty prefix inside this 24h window files UNCOMPUTABLE with the window and read time -- and that branch applies to THIS limb only, never to L4 | list-objects-v2 |  | OPEN |
| L6 | verify | UNSCOPED re-plan 0-diff after the apply; push state MEASURED by ls-remote + is-ancestor | plan + ls-remote |  | OPEN |

## Log

- 20260903T180139Z OPENED by 0.7.0_AE_CloudOps~S with 6 leg(s)
