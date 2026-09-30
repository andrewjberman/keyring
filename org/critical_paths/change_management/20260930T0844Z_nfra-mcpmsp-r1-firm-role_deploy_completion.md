# Deploy Completion Record
**Date opened:** 2026-09-30T08:44:59.043095+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T100341Z
**Deploy:** NFRA_MCPMSP r1: Inflection firm role + gateway AssumeRole grant
**Authored by:** 0.9.0_WK_NFRA_MCPMSP~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform apply targeted to mcpmsp_firm_roles.tf | apply output line | Apply complete! Resources: 3 added, 0 changed, 0 destroyed. (plan: 3 to add, 0 to change, 0 to destroy; role arn:aws:iam::313476888478:role/gateway-inf-firm-reader-role) | CLOSED 20260930T100340Z |
| L2 | verify | simulate-principal-policy arms | AC2+AC3 lines | a1.AC2: own-prefix=allowed cot-prefix=explicitDeny cot-bucket=explicitDeny RESULT: PASS; a1.AC3: AssumeRole(gateway-inf-firm-reader-role)=allowed opal-data-inf=implicitDeny opal-data-cot=implicitDeny RESULT: PASS | CLOSED 20260930T100340Z |

## Log

- 20260930T084459Z OPENED by 0.9.0_WK_NFRA_MCPMSP~2 with 2 leg(s)
- 20260930T100340Z LEG L1 closed: Apply complete! Resources: 3 added, 0 changed, 0 destroyed. (plan: 3 to add, 0 to change, 0 to destroy; role arn:aws:iam
- 20260930T100340Z LEG L2 closed: a1.AC2: own-prefix=allowed cot-prefix=explicitDeny cot-bucket=explicitDeny RESULT: PASS; a1.AC3: AssumeRole(gateway-inf-
- 20260930T100341Z CLOSED -- all 2 legs proven
