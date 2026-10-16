# Deploy Completion Record
**Date opened:** 2026-10-16T06:31:57.928025+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T064018Z
**Deploy:** NFRA_OPLGTW TO-OG-ap-26 Phase B: move the etf-classifications dynamodb:GetItem grant from opal-gateway-role to gateway-global-internal-reader-role (1 add, 0 change, 1 destroy, one replacement), safe-apply targeted, both ends read back; .tf sha256-16 867087958bac89b9, ask 69466be19798; halves CTO 4d0a8d3c0d, COO 90b589c58f, CVO f2cf55e41e; GO msg 34769
**Authored by:** 0.7.0_AE_CloudOps~ZS
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | replace the policy then get-role-policy on the internal reader and list-role-policies on the instance role | present on the internal reader (one statement GetItem, table ARN) and absent from opal-gateway-role | safe-apply targeted: plan 1 add 0 change 1 destroy, Apply complete 1 added 0 changed 1 destroyed (old id opal-gateway-role:<policy> destroyed, new id gateway-global-internal-reader-role:<policy> created); get-role-policy on the internal reader: 1 statement, Allow, dynamodb:GetItem only, Resource equals the describe-table ARN, sha256-16 609426e6a083440b (equal to the prior document); list-role-policies: internal reader 6 -> 7 holds it, opal-gateway-role 25 -> 24 does not | CLOSED 20261016T064017Z |
| S1 | verify | simulate-principal-policy one resource per call with controls, describe-table | internal reader GetItem allowed, Scan not allowed, instance role GetItem not allowed | simulate-principal-policy on the table ARN, one call each: internal reader GetItem allowed, internal reader Scan implicitDeny, opal-gateway-role GetItem implicitDeny; positive control in a separate invocation (caller principal, Scan on the same ARN) allowed; describe-table ACTIVE, hash key ticker | CLOSED 20261016T064017Z |
| V1 | verify | targeted re-plan of the one policy | No changes | terraform plan -lock=false targeted at aws_iam_role_policy.gw_etf_classification_read: No changes. Your infrastructure matches the configuration. | CLOSED 20261016T064017Z |

## Log

- 20261016T063157Z OPENED by 0.7.0_AE_CloudOps~ZS with 3 leg(s)
- 20261016T064017Z LEG P1 closed: safe-apply targeted: plan 1 add 0 change 1 destroy, Apply complete 1 added 0 changed 1 destroyed (old id opal-gateway-ro
- 20261016T064017Z LEG S1 closed: simulate-principal-policy on the table ARN, one call each: internal reader GetItem allowed, internal reader Scan implici
- 20261016T064017Z LEG V1 closed: terraform plan -lock=false targeted at aws_iam_role_policy.gw_etf_classification_read: No changes. Your infrastructure m
- 20261016T064018Z CLOSED -- all 3 legs proven
