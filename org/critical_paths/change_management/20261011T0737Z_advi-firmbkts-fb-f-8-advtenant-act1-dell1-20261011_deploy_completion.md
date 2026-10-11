# Deploy Completion Record
**Date opened:** 2026-10-11T07:37:50.061008+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-8 phase B: deploy the advTenant build -- shared-advisor-router (v26 to new) + shared-advisor-router-response (v5 to new), 10 associations on EVTSA9VEHNZVH, through safe-apply, under the never-widen pair
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-act reads saved in the entry: live get-distribution-config ETag + 10 associations, router v26 and guard v5 on 5 behaviors each, built artifact SHA-256 and bytes-above-127 count for both | ETag, the 10 ARNs, and 2 SHA/non-ASCII lines printed in the entry |  | OPEN |
| L2 | activation | terraform plan of infra/aws/terraform/portal-auth read as JSON (exactly 2 functions + the distribution's 10 associations, distribution NOT no-op), then safe-apply, distribution Deployed | plan resource summary line + apply result + status Deployed |  | OPEN |
| L3 | verify | post-apply read: 10 associations name the new versions, CodeSha256 of each new version equals its artifact SHA, post-apply plan reads No changes | AC1 AC2 AC3 outputs + the plan line |  | OPEN |
| L4 | verify | CTO oracle read by 1.0.0_SA_CTO~DELL1: both new versions invoked on the 5 event classes against base, one live no-session request 401, associations diffed | the CTO's read, quoted with its message id |  | OPEN |
| L5 | git | proof instance written and TO-FB-f-8 status flipped complete in one commit | commit hash |  | OPEN |
| shared-advisor-router | tf-lambda | aws_lambda_function.shared_advisor_router[0] | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |
| shared-advisor-router-response | tf-lambda | aws_lambda_function.shared_advisor_router_response[0] | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261011T073750Z OPENED by 0.7.0_AE_CloudOps~FB1 with 7 leg(s)
