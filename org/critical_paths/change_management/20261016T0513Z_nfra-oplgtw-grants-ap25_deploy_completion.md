# Deploy Completion Record
**Date opened:** 2026-10-16T05:13:02.049458+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T052014Z
**Deploy:** NFRA_OPLGTW TO-OG-ap-25 Phase B: gateway role dynamodb:GetItem on etf-classifications (1 policy, 1 add, 0 change, 0 destroy), safe-apply targeted, read back from IAM; .tf sha256-16 c51c268d41b63e8f, ask 01861a288d2b; three halves signed (CTO 9fc726f92a, COO d87f790253, CVO be6d23b7f6); GO msg 34744
**Authored by:** 0.7.0_AE_CloudOps~ZS
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | apply gw_etf_classification_read then get-role-policy | one statement, dynamodb:GetItem only, the table ARN | safe-apply targeted: plan 1 add 0 change 0 destroy, Apply complete 1 added 0 changed 0 destroyed; get-role-policy opal-gateway-role/gateway-global-etf-classification-read-policy: 1 statement, Allow, dynamodb:GetItem only, Resource equals the describe-table ARN; policy sha256-16 609426e6a083440b; role inline policies 24 -> 25 | CLOSED 20261016T052013Z |
| S1 | verify | simulate-principal-policy GetItem and Scan, one resource per call, with controls and describe-table | GetItem allowed, Scan not allowed, table exists | simulate-principal-policy on the table ARN, one call each: GetItem allowed, Scan implicitDeny, Query implicitDeny, PutItem implicitDeny; positive control in a separate invocation (caller principal, Scan on the same ARN) allowed; describe-table ACTIVE, hash key ticker | CLOSED 20261016T052014Z |
| V1 | verify | targeted re-plan of the one policy | No changes | terraform plan -lock=false targeted at aws_iam_role_policy.gw_etf_classification_read: No changes. Your infrastructure matches the configuration. | CLOSED 20261016T052014Z |

## Log

- 20261016T051302Z OPENED by 0.7.0_AE_CloudOps~ZS with 3 leg(s)
- 20261016T052013Z LEG P1 closed: safe-apply targeted: plan 1 add 0 change 0 destroy, Apply complete 1 added 0 changed 0 destroyed; get-role-policy opal-g
- 20261016T052014Z LEG S1 closed: simulate-principal-policy on the table ARN, one call each: GetItem allowed, Scan implicitDeny, Query implicitDeny, PutIt
- 20261016T052014Z LEG V1 closed: terraform plan -lock=false targeted at aws_iam_role_policy.gw_etf_classification_read: No changes. Your infrastructure m
- 20261016T052014Z CLOSED -- all 3 legs proven
