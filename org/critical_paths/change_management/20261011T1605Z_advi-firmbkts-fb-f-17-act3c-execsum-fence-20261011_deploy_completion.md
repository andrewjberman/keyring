# Deploy Completion Record
**Date opened:** 2026-10-11T16:05:09.202097+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-17 (act 3c): the exec-summary generator's fence row applied to s3://opal-data-49financial -- ONE bucket policy (aws_s3_bucket_policy.opal_data_49financial, root infra/aws/terraform/shared-infra), 29 to 34 statements (3 Deny + 2 Allow added; fence exemption +1: exec-summary-generator-role, Get/List/Put exempt under advi/49financial/platinum/advisors/ only; Allow side read-only); pair COO half @3d5185f9de + CTO half @6f5335f5c0; rollback = the prior policy put back verbatim; inert until act 4b
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: pair SIGNED at the current bytes, the live policy printed to deliverables/PRIOR_opal-data-49financial_policy_<UTC>.json reading 29 statements, the planned policy checked against the actor's own access | the entry carries the read lines and the prior file path |  | OPEN |
| L2 | activation | scoped plan of shared-infra reads Plan: 0 to add, 1 to change, 0 to destroy, one resource in place, 29 to 34 statements; .tools/safe-apply.sh on the saved plan | plan summary line, the policy diff hunk, apply result line |  | OPEN |
| L3 | verify | AC1 r4_act3b.py --arms live reads 3 of 3 arms (34 statements: 21 Deny, 13 Allow); AC2 the scoped plan reads No changes | the two outputs quoted |  | OPEN |
| L4 | git | proof instance and prior policy file written, status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261011T160509Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
