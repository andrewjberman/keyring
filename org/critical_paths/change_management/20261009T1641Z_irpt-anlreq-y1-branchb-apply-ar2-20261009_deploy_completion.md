# Deploy Completion Record
**Date opened:** 2026-10-09T16:41:06.648997+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ.TO-APPLY-Y1 BRANCH B legs B2+ (AMENDMENT 5): apply-only rollback of irpt-status from rev 4 VC/r14ka to rev 3 t6OJTCcmOnWGVl8iglcvfGoYb3PbPJqJYqsSgJBpGdI=, live 500 on every call since 15:43:11Z. Applier 0.7.0_AE_CloudOps~AR2 substituted for 0.7.0_AE_CloudOps~DELL2 per CTO standing ruling @5ff94852a6 (CTO msgs 3689/3709, MSTR msg 3688). NO UPLOAD: ~DELL2 leg B1 (msg 3694) already made rev 3 bytes the CURRENT object version 1dX90t6JdYfffHVpKsy7MHlQdfdFvp2V, 356127 bytes, content-sha256 t6OJTCcm, verified by this seat with head-object. CTO asked that B2+ append to Y1 existing ledger; a tool scan of 20 of 20 sentinels found ZERO open irpt-status/Y1/branchb entries (~DELL2 closed its branchb entry SUPERSEDED), so this fresh entry carries B2+ and names that supersession. Rollback: re-promote rev 4 artifact version (recorded in leg B2 proof) through the same Terraform path. One family on the artifact key: irpt-status (a Lambda; no task-definition sweep).
**Authored by:** 0.7.0_AE_CloudOps~AR2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B3 | verify | AMENDMENT 5 after-reads (a)(b)(c) | (a) live CodeSha256 == t6OJTCcmOnWGVl8iglcvfGoYb3PbPJqJYqsSgJBpGdI=; (b) one real GET answers 200 for a non-49F caller; (c) the CloudWatch count of additional_policy_revisions TypeError errors stays flat for 5 minutes after the promote |  | OPEN |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T164106Z OPENED by 0.7.0_AE_CloudOps~AR2 with 2 leg(s)
