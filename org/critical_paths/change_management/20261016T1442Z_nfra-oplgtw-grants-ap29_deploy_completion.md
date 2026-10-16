# Deploy Completion Record
**Date opened:** 2026-10-16T14:42:21.849172+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T145224Z
**Deploy:** NFRA_OPLGTW TO-OG-ap-29 Phase B: dedicated read-only role gateway-49f-blackdiamond-live-read-role plus one inline policy on opal-data-bd silver/{unrealized,transactions,allocations,fees}/ (2 add, 0 change, 0 destroy), safe-apply targeted, read back and simulated; .tf sha256-16 5604d8577f68a50d, ask 369a8e7a12f7; halves CTO 7877e044d7, COO b6c6de7fbe, CVO 6b7d6ef48d; GO msg 35070
**Authored by:** 0.7.0_AE_CloudOps~ZS
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | apply role and policy then get-role and get-role-policy | role exists, trust is only opal-gateway-role, policy equals the file, instance role still 24 policies | safe-apply targeted at the role and the policy: plan 2 add 0 change 0 destroy, Apply complete 2 added 0 changed 0 destroyed; iam get-role: trust Principal is only opal-gateway-role's ARN, one statement, no Condition; get-role-policy: 6 statements equal to the file (4 Deny, 2 Allow), sha256-16 39a137ba628e6ae0; 1 inline policy, 0 attached; instance role still 24 inline policies and does not hold the new policy; gateway-49f-blackdiamond-read-role policy sha256-16 ceb6ae001918528d unchanged | CLOSED 20261016T145224Z |
| S1 | verify | simulate-principal-policy one resource per call, four prefixes plus four negative controls plus a positive control | GetObject allowed 4 of 4, ListBucket allowed 4 of 4, negative controls not allowed 4 of 4 | simulate-principal-policy as the new role, one resource per call: GetObject on a probe key under each of the 4 silver tables allowed 4 of 4; ListBucket with each table prefix as s3:prefix allowed 4 of 4; negative controls explicitDeny 4 of 4 (GetObject silver/ap29-negative-control/probe, GetObject on an opal-data-assets key, PutObject silver/fees/probe, ListBucket prefix ap29-negative-control/); positive controls with the caller principal on the same PutObject, GetObject and ListBucket each allowed, each its own invocation; existence read of the four prefixes KeyCount 1 each, no object read | CLOSED 20261016T145224Z |
| V1 | verify | targeted re-plan of the role and policy | No changes | terraform plan -lock=false targeted at aws_iam_role.bdlive_read and aws_iam_role_policy.bdlive_read: No changes. Your infrastructure matches the configuration. | CLOSED 20261016T145224Z |

## Log

- 20261016T144221Z OPENED by 0.7.0_AE_CloudOps~ZS with 3 leg(s)
- 20261016T145224Z LEG P1 closed: safe-apply targeted at the role and the policy: plan 2 add 0 change 0 destroy, Apply complete 2 added 0 changed 0 destro
- 20261016T145224Z LEG S1 closed: simulate-principal-policy as the new role, one resource per call: GetObject on a probe key under each of the 4 silver ta
- 20261016T145224Z LEG V1 closed: terraform plan -lock=false targeted at aws_iam_role.bdlive_read and aws_iam_role_policy.bdlive_read: No changes. Your in
- 20261016T145224Z CLOSED -- all 3 legs proven
