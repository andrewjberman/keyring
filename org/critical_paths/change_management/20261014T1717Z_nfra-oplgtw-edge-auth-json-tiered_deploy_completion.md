# Deploy Completion Record
**Date opened:** 2026-10-14T17:17:12.953248+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-zs-1: attach auth-validator-edge to CloudFront behavior /json-tiered/* (row Z-S114, CTO ruling 34093; A1 accepts the 2-change plan on three conditions)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the root plan reads 0 to add, 1 or 2 to change, 0 to destroy and the second change is ONLY aws_wafv2_web_acl.opal_cloudfront_protection | the Plan: line plus the per-resource list from W/ZS1_PLAN.txt |  | OPEN |
| L2 | verify | A1 conditions (i) and (ii): the live ACL's rule set is IDENTICAL either side of the apply | W/ZS1_ACL_BEFORE.json and W/ZS1_ACL_AFTER.json with equal rules_sha256 over the whole ordered rule list |  | OPEN |
| L3 | activation | safe-apply lands the one association on behavior 7 and the distribution reaches status Deployed | the apply output, the live LambdaFunctionAssociations read back on that behavior, and the distribution Status |  | OPEN |
| L4 | verify | the hole is closed and nothing else moved: bare path refuses unauthenticated, the twin still serves authenticated, and exactly ONE UpdateWebACL call | W/ZS1_PROOF.json -- bare_unauth_status, twin_authed_status, updatewebacl_calls from CloudTrail with its lag probe |  | OPEN |

## Log

- 20261014T171712Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
