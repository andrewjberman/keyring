# Deploy Completion Record
**Date opened:** 2026-09-30T13:45:55.234696+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-7 E_18: step 1 IAM additive inline policy E18ScheduledEtfClassificationsPut on bd-exporter-ec2-role (safe-apply, plan 1/0/0); step 2 BD E_18.detect_new_securities.py deploy SHA-verified; acceptance = first ordinary 04:00Z scheduled run (halves COO c4019eacd2 / CTO a7a6d286f2)
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| I1 | verify | terraform plan bd-pipeline before the apply | exactly 1 add, 0 change, 0 destroy | terraform plan -chdir bd-pipeline at 13:4xZ (winget terraform, init clean): Plan: 1 to add, 0 to change, 0 to destroy -- aws_iam_role_policy.bd_exporter_e18_etf_classifications_put will be created; saved plan bd-e18.tfplan | CLOSED 20260930T135028Z |
| I2 | activation | safe-apply bd-pipeline root | apply rc 0 + re-plan 0-diff | safe-apply (HALT_ACK=1, naming plan gate WARN 135 graded after the builder rename) 13:56:26Z: aws_iam_role_policy.bd_exporter_e18_etf_classifications_put Creation complete [id=bd-exporter-ec2-role:mdpf-secclass-scheduled-put-policy]; Apply complete 1 added 0 changed 0 destroyed; re-plan -detailed-exitcode 0 (no changes). First attempt at 13:50Z was REFUSED on the hand-typed name e18-etf-classifications-put (R1.f no vocabulary); name re-taken from lib/opal_naming.py name('mdpf', None, 'secclass-scheduled-put', 'policy') | CLOSED 20260930T140036Z |
| I3 | verify | read-back of the new inline policy | get-role-policy names Sid E18ScheduledEtfClassificationsPut, PutItem on etf-classifications only | get-role-policy bd-exporter-ec2-role mdpf-secclass-scheduled-put-policy at 13:5xZ: one statement, Sid E18ScheduledEtfClassificationsPut, Effect Allow, Action dynamodb:PutItem, Resource arn:aws:dynamodb:us-east-1:313476888478:table/etf-classifications -- nothing else | CLOSED 20260930T140036Z |
| C1 | s3-prefix | opal-data-bd code/gold E_18.detect_new_securities.py | safe-deploy DEPLOYED line + comp-pipescript deployed MATCH (SHA verified) |  | OPEN |
| A1 | verify | first ordinary bd-canonical-prices-daily 04:00Z run of E_18 --upload | no AccessDenied; written, refused, denominator printed; every written row new; no bd-securities call in the logs |  | OPEN |

## Log

- 20260930T134555Z OPENED by 2.0.0_SA_COO~M with 5 leg(s)
- 20260930T135028Z LEG I1 closed: terraform plan -chdir bd-pipeline at 13:4xZ (winget terraform, init clean): Plan: 1 to add, 0 to change, 0 to destroy --
- 20260930T140036Z LEG I2 closed: safe-apply (HALT_ACK=1, naming plan gate WARN 135 graded after the builder rename) 13:56:26Z: aws_iam_role_policy.bd_exp
- 20260930T140036Z LEG I3 closed: get-role-policy bd-exporter-ec2-role mdpf-secclass-scheduled-put-policy at 13:5xZ: one statement, Sid E18ScheduledEtfCla
