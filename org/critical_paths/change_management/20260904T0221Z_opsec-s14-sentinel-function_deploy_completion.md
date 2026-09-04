# Deploy Completion Record
**Date opened:** 2026-09-04T02:21:56.923380+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609 TO-OP-S-14-21 deliverables 1-5: deploy opal-sentinel ARMED WATCH-ONLY -- function, both WAF subscription filters, and the daily digest FILE schedule. Deployed AFTER the TO-OP-S-22 verdict (02:05Z), which is what S1421-AC5 grades.
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | artifact opsec/opal-sentinel.zip on opal-313476888478-lambda-artifacts | head-object ContentLength + VersionId + content-sha256 metadata |  | OPEN |
| L2 | git | CLOUD commit of the function source and sentinel.tf | commit hash |  | OPEN |
| L3 | activation | terraform apply on the opsec root -- 9 to add, 0 change, 0 destroy | apply output |  | OPEN |
| L4 | verify | UNSCOPED re-plan 0-diff on the opsec root | terraform plan -detailed-exitcode rc |  | OPEN |
| L5 | verify | APPLIED-plane read: reserved concurrency 1 (C-7), both subscription filters present, digest rule armed | aws lambda/logs/events output |  | OPEN |
| L6 | verify | S14-AC1/AC2/AC3 fixture exercise and its cleanup read back | invocation result plus a BLOCK census with its denominator |  | OPEN |

## Log

- 20260904T022156Z OPENED by 0.7.0_AE_CloudOps~S with 6 leg(s)
