# Deploy Completion Record
**Date opened:** 2026-10-11T08:14:45.129227+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-8 phase B (laptop, FBL): deploy the advTenant build - shared-advisor-router (v26 to new) + shared-advisor-router-response (v5 to new), 10 associations on EVTSA9VEHNZVH + WAF ACL rider, via safe-apply, under the never-widen pair; rollback = re-associate v26 and v5, WAF pre-act JSON re-apply
**Authored by:** 0.7.0_AE_CloudOps~FBL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-act reads saved in the entry: get-distribution-config ETag + 10 associations (router v26, guard v5, 5 behaviors each), get-web-acl JSON (name, id, LockToken, 6 rules), s3_object_version of the 2 functions in state, built artifact SHA-256 and bytes-above-127 for both | ETag, 10 ARNs, ACL name/id/LockToken, 2 SHA lines with non-ASCII counts | ETag E1OAC26XEP0FDI, Deployed; router v26 x5 + guard v5 x5; ACL opal-cloudfront-protection a09833c0-4043-49fc-a92c-0dcdeaff9abd LockToken 848a6d0b-d69f-40e0-876a-cfc0ce40b6b2 (6 rules, 3 Count); ROUTER_SHA256 cOG/BuFhy9xcL7EF+4u5VexRZGjDdJq3h364PAPkYsw= bytes>127=0 (S3 VersionId rFzCqwaX6lC8KHZH0zPBiBpBXgPxxHLU); GUARD_SHA256 YIgGtFjZwFltdXbviIx5dOQbb6FsOAUtIB96caAI0xs= bytes>127=0 (VersionId H8zfKrvXgbVifrAyEet4RClXGA0OSQFA); state s3_object_version pre-act NWJciPj.../T39sO4P...; files in deliverables/0.7.0_AE_CloudOps~FBL/evidence/ | CLOSED 20261011T082031Z |
| L2 | verify | plan of infra/aws/terraform/portal-auth read as JSON: exactly 2 functions + 10 associations + WAF ACL 3 version attrs, distribution NOT no-op | plan resource summary line | terraform 1.15.8 plan portal-auth: 74 resource_changes, 70 no-op, 4 update = aws_cloudfront_distribution.portal (10 association lambda_arn on behaviors 1,2,3,15,26, nothing else), aws_lambda_function.shared_advisor_router[0], aws_lambda_function.shared_advisor_router_response[0] (s3_object_version only), aws_wafv2_web_acl.opal_cloudfront_protection (3 managed group version attrs); distribution not no-op | CLOSED 20261011T082031Z |
| L3 | activation | safe-apply of the saved plan, distribution Deployed | apply summary + Deployed status |  | OPEN |
| L4 | verify | post-apply: AC1-AC4 outputs, ACL equal rule by rule modulo version and LockToken, post-apply plan No changes | AC1-AC4 outputs + plan line |  | OPEN |
| L5 | verify | CTO oracle read by 1.0.0_SA_CTO~DELL1 at Deployed | the CTO read quoted with message id |  | OPEN |

## Log

- 20261011T081445Z OPENED by 0.7.0_AE_CloudOps~FBL with 5 leg(s)
- 20261011T082031Z LEG L1 closed: ETag E1OAC26XEP0FDI, Deployed; router v26 x5 + guard v5 x5; ACL opal-cloudfront-protection a09833c0-4043-49fc-a92c-0dcde
- 20261011T082031Z LEG L2 closed: terraform 1.15.8 plan portal-auth: 74 resource_changes, 70 no-op, 4 update = aws_cloudfront_distribution.portal (10 asso
