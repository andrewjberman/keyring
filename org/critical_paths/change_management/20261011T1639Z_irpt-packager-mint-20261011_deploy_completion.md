# Deploy Completion Record
**Date opened:** 2026-10-11T16:39:29.376842+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T164509Z
**Deploy:** IRPT_ANLREQ packager mint: one GetSecretValue grant on irpt-ycharts-runner-role, one secret opal/ticketing/svc-irpt-packager (XB-20261011T163203Z-3fc2)
**Authored by:** 0.7.0_AE_CloudOps~ANL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| before | verify | three simulates secretsmanager:GetSecretValue on the secret ARN pattern, expect implicitDeny x3 | simulate answers | 3 simulates on arn:...:secret:opal/ticketing/svc-irpt-packager-*: irpt-ycharts-runner-role implicitDeny; outlook-global-commentary-draft-role implicitDeny; agentbus-alyssa01-fleet-andrew-role implicitDeny (control: user/Andrew_Berman allowed, separate call) | CLOSED 20261011T164508Z |
| grant | activation | one statement on irpt-ycharts-runner-role via safe-apply in infra/aws/terraform/investor-reporting/ycharts | plan 1 statement added, 0 destroyed, then 0-diff plan | safe-apply on ycharts root, plan 0 add 1 change 0 destroy (one statement ReadThePackagerServiceToken added); commit b7c67d3ac8; post-apply plan No changes; live get-role-policy shows the statement | CLOSED 20261011T164508Z |
| mint | activation | one RS256 service token svc-irpt-packager, no firm claim, 90 days, in memory only | claim names and expiry only | mint_packager.py: claim names aud exp iat iss name sub tier userType; sub svc-irpt-packager userType service; no firm claim; iat 2026-10-11T16:43:55Z exp 2027-01-09T16:43:55Z 90d; token in memory only | CLOSED 20261011T164509Z |
| secret | activation | opal/ticketing/svc-irpt-packager created with JSON token member and description | describe-secret name arn dates | describe-secret: opal/ticketing/svc-irpt-packager arn ...:secret:opal/ticketing/svc-irpt-packager-JEkpSP created 2026-10-11T12:43:56-04:00 | CLOSED 20261011T164509Z |
| after | verify | three simulates after the grant, expect allowed only on irpt-ycharts-runner-role | simulate answers | 3 simulates on the real ARN: irpt-ycharts-runner-role allowed; outlook-global-commentary-draft-role implicitDeny; agentbus-alyssa01-fleet-andrew-role implicitDeny | CLOSED 20261011T164509Z |

## Log

- 20261011T163929Z OPENED by 0.7.0_AE_CloudOps~ANL with 5 leg(s)
- 20261011T164508Z LEG before closed: 3 simulates on arn:...:secret:opal/ticketing/svc-irpt-packager-*: irpt-ycharts-runner-role implicitDeny; outlook-global-
- 20261011T164508Z LEG grant closed: safe-apply on ycharts root, plan 0 add 1 change 0 destroy (one statement ReadThePackagerServiceToken added); commit b7c6
- 20261011T164509Z LEG mint closed: mint_packager.py: claim names aud exp iat iss name sub tier userType; sub svc-irpt-packager userType service; no firm cl
- 20261011T164509Z LEG secret closed: describe-secret: opal/ticketing/svc-irpt-packager arn ...:secret:opal/ticketing/svc-irpt-packager-JEkpSP created 2026-10
- 20261011T164509Z LEG after closed: 3 simulates on the real ARN: irpt-ycharts-runner-role allowed; outlook-global-commentary-draft-role implicitDeny; agentb
- 20261011T164509Z CLOSED -- all 5 legs proven
