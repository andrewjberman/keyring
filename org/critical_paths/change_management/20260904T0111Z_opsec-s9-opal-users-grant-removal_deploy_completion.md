# Deploy Completion Record
**Date opened:** 2026-09-04T01:11:07.756629+00:00
**Status:** OPEN
**Deploy:** TO-OP-S-9-11 OP-s-9: remove BOTH opal-users grants (us-east-1 + the nonexistent us-east-2) from opalinvest-auth-permissions; table LEFT STANDING
**Authored by:** 0.7.0_AE_CloudOps~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit of portal-auth/iam.tf removing lines 50-51 | commit hash |  | OPEN |
| L2 | activation | targeted terraform apply of aws_iam_role_policy.auth_permissions via safe-apply | apply output Modifications complete |  | OPEN |
| L3 | verify | APPLIED-plane get-role-policy: both table/opal-users ARNs ABSENT, opal-users-v2 + index STILL PRESENT | live aws iam get-role-policy output |  | OPEN |
| L4 | verify | fixture AFTER probes GET /auth/me + POST /auth/refresh return the SAME result as the captured BEFORE | HTTP 200 bodies pasted, before and after |  | OPEN |

## Log

- 20260904T011107Z OPENED by 0.7.0_AE_CloudOps~X with 4 leg(s)
