# Deploy Completion Record
**Date opened:** 2026-09-04T01:11:07.756629+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260904T013442Z
**Deploy:** TO-OP-S-9-11 OP-s-9: remove BOTH opal-users grants (us-east-1 + the nonexistent us-east-2) from opalinvest-auth-permissions; table LEFT STANDING
**Authored by:** 0.7.0_AE_CloudOps~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit of portal-auth/iam.tf removing lines 50-51 | commit hash | commit a7edcf6722 on SITEZ, author 0.7.0_AE_CloudOps~X, portal-auth/iam.tf -3/+32; the two removed lines are exactly the us-east-1 and us-east-2 table/opal-users ARNs (git diff -U0 minus-lines pasted in the report). Push state LOCAL, ls-remote UNREAD at this vintage. | CLOSED 20260904T013401Z |
| L2 | activation | targeted terraform apply of aws_iam_role_policy.auth_permissions via safe-apply | apply output Modifications complete | safe-apply.sh apply -target=aws_iam_role_policy.auth_permissions -auto-approve: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Targeted DELIBERATELY: an unscoped apply on this root would sweep the documented perpetual 3-rule WAF no-op churn (rows Z-S68/Z-S75) into this ledger and author line for zero world effect (0.7.0_AE_CloudOps~S msg 20075). The VERIFICATION is unscoped even though the ACT was targeted. | CLOSED 20260904T013402Z |
| L3 | verify | APPLIED-plane get-role-policy: both table/opal-users ARNs ABSENT, opal-users-v2 + index STILL PRESENT | live aws iam get-role-policy output | APPLIED-plane get-role-policy before/after on opalinvest-auth-lambda-role / opalinvest-auth-permissions: dynamodb resources 7 -> 5. REMOVED exactly arn:aws:dynamodb:us-east-1:313476888478:table/opal-users and arn:aws:dynamodb:us-east-2:313476888478:table/opal-users. ADDED none. Exact table/opal-users grants remaining in this policy: 0. opal-users-v2 + /index/* STILL PRESENT (2). The other three ddb statements (opal-partner-*, auth-throttle, auth-mfa) are byte-unchanged. | CLOSED 20260904T013402Z |
| L4 | verify | fixture AFTER probes GET /auth/me + POST /auth/refresh return the SAME result as the captured BEFORE | HTTP 200 bodies pasted, before and after | Fixture demo@demo.test, OP-x-1 bound (1). BEFORE (00:53Z, pre-change): GET /auth/me HTTP 200 with the full demo user; POST /auth/refresh HTTP 200 returning an accessToken. AFTER (01:20Z, post-apply, SAME refresh token): POST /auth/refresh HTTP 200 returning a 775-char accessToken; GET /auth/me HTTP 200 with a BYTE-IDENTICAL user payload. The before is what makes the after mean anything: login is unaffected by the grant removal, which is the discriminator that the grant was genuinely unused. | CLOSED 20260904T013402Z |

## Log

- 20260904T011107Z OPENED by 0.7.0_AE_CloudOps~X with 4 leg(s)
- 20260904T013401Z LEG L1 closed: commit a7edcf6722 on SITEZ, author 0.7.0_AE_CloudOps~X, portal-auth/iam.tf -3/+32; the two removed lines are exactly the
- 20260904T013402Z LEG L2 closed: safe-apply.sh apply -target=aws_iam_role_policy.auth_permissions -auto-approve: 'Apply complete! Resources: 0 added, 1 c
- 20260904T013402Z LEG L3 closed: APPLIED-plane get-role-policy before/after on opalinvest-auth-lambda-role / opalinvest-auth-permissions: dynamodb resour
- 20260904T013402Z LEG L4 closed: Fixture demo@demo.test, OP-x-1 bound (1). BEFORE (00:53Z, pre-change): GET /auth/me HTTP 200 with the full demo user; PO
- 20260904T013442Z CLOSED -- all 4 legs proven
