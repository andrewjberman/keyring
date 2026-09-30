# Deploy Completion Record
**Date opened:** 2026-09-28T23:14:15.706516+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260928T233027Z
**Deploy:** Holdings firm principals: s3:GetObjectVersion on PublishOwnHoldings (COO 5c2f71f798, CTO ed8b09e0ea)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~42
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply 3 aws_iam_role_policy.irpt_holdings | Apply complete 0 added 3 changed 0 destroyed | Apply complete! Resources: 0 added, 3 changed, 0 destroyed on aws_iam_role_policy.irpt_holdings[49financial\|cottonwood\|inflection] (safe-apply, -target x3, HALT_ACK=1) | CLOSED 20260928T232935Z |
| V1 | verify | get-role-policy x3 | PublishOwnHoldings Action carries s3:GetObject, s3:GetObjectVersion, s3:PutObject, resources unchanged; READS statements still carry GetObjectVersion; re-plan No changes | get-role-policy x3: PublishOwnHoldings Action=[s3:PutObject, s3:GetObjectVersion, s3:GetObject] on irpt-49f-holdings-role, irpt-cot-holdings-role, irpt-inf-holdings-role, resources unchanged; terraform plan -lock=false -> No changes. | CLOSED 20260928T232936Z |

## Log

- 20260928T231415Z OPENED by 0.9.0_WK_IRPT_BCKEND~42 with 2 leg(s)
- 20260928T232935Z LEG A1 closed: Apply complete! Resources: 0 added, 3 changed, 0 destroyed on aws_iam_role_policy.irpt_holdings[49financial|cottonwood|i
- 20260928T232936Z LEG V1 closed: get-role-policy x3: PublishOwnHoldings Action=[s3:PutObject, s3:GetObjectVersion, s3:GetObject] on irpt-49f-holdings-rol
- 20260928T233027Z CLOSED -- all 2 legs proven
