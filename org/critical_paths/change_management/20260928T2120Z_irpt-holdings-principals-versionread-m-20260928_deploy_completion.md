# Deploy Completion Record
**Date opened:** 2026-09-28T21:20:40.055664+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260928T212401Z
**Deploy:** Holdings firm principals: s3:GetObjectVersion on the READS statements (CTO 635481d716, COO 410f52bdde)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~42
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply 3 aws_iam_role_policy.irpt_holdings | Apply complete 0 added 3 changed 0 destroyed | terraform apply Apply complete! Resources: 0 added, 3 changed, 0 destroyed (irpt_holdings[49financial\|cottonwood\|inflection]) | CLOSED 20260928T212351Z |
| V1 | verify | get-role-policy x3 | each READ statement's Action carries s3:GetObject and s3:GetObjectVersion, resources unchanged; re-plan No changes | get-role-policy x3: ReadOpalDataAssets and ReadOpalData{Bd,Cot,Inf} statements each Action=[s3:GetObjectVersion, s3:GetObject] on all 3 roles, resources unchanged; terraform plan -lock=false -> No changes | CLOSED 20260928T212351Z |

## Log

- 20260928T212040Z OPENED by 0.9.0_WK_IRPT_BCKEND~42 with 2 leg(s)
- 20260928T212351Z LEG A1 closed: terraform apply Apply complete! Resources: 0 added, 3 changed, 0 destroyed (irpt_holdings[49financial|cottonwood|inflect
- 20260928T212351Z LEG V1 closed: get-role-policy x3: ReadOpalDataAssets and ReadOpalData{Bd,Cot,Inf} statements each Action=[s3:GetObjectVersion, s3:GetO
- 20260928T212401Z CLOSED -- all 2 legs proven
