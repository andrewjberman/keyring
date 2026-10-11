# Deploy Completion Record
**Date opened:** 2026-10-11T16:39:29.376842+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ packager mint: one GetSecretValue grant on irpt-ycharts-runner-role, one secret opal/ticketing/svc-irpt-packager (XB-20261011T163203Z-3fc2)
**Authored by:** 0.7.0_AE_CloudOps~ANL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| before | verify | three simulates secretsmanager:GetSecretValue on the secret ARN pattern, expect implicitDeny x3 | simulate answers |  | OPEN |
| grant | activation | one statement on irpt-ycharts-runner-role via safe-apply in infra/aws/terraform/investor-reporting/ycharts | plan 1 statement added, 0 destroyed, then 0-diff plan |  | OPEN |
| mint | activation | one RS256 service token svc-irpt-packager, no firm claim, 90 days, in memory only | claim names and expiry only |  | OPEN |
| secret | activation | opal/ticketing/svc-irpt-packager created with JSON token member and description | describe-secret name arn dates |  | OPEN |
| after | verify | three simulates after the grant, expect allowed only on irpt-ycharts-runner-role | simulate answers |  | OPEN |

## Log

- 20261011T163929Z OPENED by 0.7.0_AE_CloudOps~ANL with 5 leg(s)
