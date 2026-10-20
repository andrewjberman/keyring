# Deploy Completion Record
**Date opened:** 2026-10-20T20:15:54.466234+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T202342Z
**Deploy:** NFRA_MCPORTAL MP-pd-7: the grant-writer Lambda's code package deployed from source through Terraform (one in-place update; set_person_access and the WIDENING confirm); both never-widen halves signed at ask f0098d2b67ab; pre-act record: org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~NFRA1/MP-pd-7_PRE_ACT_RECORD.md; order org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pd-7.person-access-release.md
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| package-build | activation | the package built from the Lambda directory at f3774ac1df8 and the live release 13917ef993 | proof: W/MP-pd-7_MEASURE.json and the saved plan | package built from the Lambda directory at f3774ac1df8 and live release 13917ef993: 65 members; the Terraform archive equals the measure-time build per member (W/MP-pd-7_MEASURE.json) | CLOSED 20261020T202341Z |
| apply | activation | one safe-apply of the saved targeted plan, 0 to add 1 to change 0 to destroy | proof: W/MP-pd-7_APPLY.json | one safe-apply of the saved targeted plan: Plan 0 to add 1 to change 0 to destroy on aws_lambda_function.mcportal_grant_writer; Apply complete 0 added 1 changed 0 destroyed; 237.4 s (W/MP-pd-7_APPLY.json) | CLOSED 20261020T202341Z |
| deployed-bytes-read | verify | CodeSha256, both no-header invokes REFUSED NO-OWNER-HEADER, the served zip holds WIDEN-NO-CONFIRM and widening_signoff and equals the package built | proof: W/MP-pd-7_AFTER.json | CodeSha256 RUGwtI9t8UKV8VpyCeArffZFwHeuUm4QhOIJU+nAJjg=; both no-header invokes REFUSED NO-OWNER-HEADER; the served zip holds WIDEN-NO-CONFIRM and widening_signoff and its 65 member md5s equal the package built (W/MP-pd-7_AFTER.json) | CLOSED 20261020T202342Z |

## Log

- 20261020T201554Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261020T202341Z LEG package-build closed: package built from the Lambda directory at f3774ac1df8 and live release 13917ef993: 65 members; the Terraform archive eq
- 20261020T202341Z LEG apply closed: one safe-apply of the saved targeted plan: Plan 0 to add 1 to change 0 to destroy on aws_lambda_function.mcportal_grant_
- 20261020T202342Z LEG deployed-bytes-read closed: CodeSha256 RUGwtI9t8UKV8VpyCeArffZFwHeuUm4QhOIJU+nAJjg=; both no-header invokes REFUSED NO-OWNER-HEADER; the served zip 
- 20261020T202342Z CLOSED -- all 3 legs proven
