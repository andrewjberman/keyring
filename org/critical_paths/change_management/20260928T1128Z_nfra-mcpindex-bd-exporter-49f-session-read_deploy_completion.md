# Deploy Completion Record
**Date opened:** 2026-09-28T11:28:34.940969+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260928T115010Z
**Deploy:** bd-exporter-ec2-role gains GetSecretValue on the 49F session secret by EXTENDING the existing AdditionalPermissions statement, so the ported asset-dim REST producer can authenticate (MX-s-10 A5, rows Z-S44/Z-S45)
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: one Resource element added to aws_iam_role_policy.bd_exporter_additional in infra/aws/terraform/bd-pipeline/iam.tf | commit hash | 5d7d1769e3 -- one Resource element added to aws_iam_role_policy.bd_exporter_additional. CORRECTION TO THAT COMMIT MESSAGE, which is wrong and is superseded here: it says the element uses A5's literal ${local.account_id} form 'exactly as A5 specified'. It does NOT. A5's literal was REFUSED by the naming gate as a hand-kept carrier of '49f' ('read it through lookup(49financial)'), so the landed element is the DERIVED aws_secretsmanager_secret.bd_49f["session"].arn -- this module's own idiom for the same secret (bd-49f-interim.tf:95, :223, :407), which the gate PASSED (NAMING-GATE: PASS 0 graded). The file's own comment beside the element states the deviation correctly; only the commit message is stale. The derived form grants strictly LESS than A5's literal would have: the plan resolves it to the exact secret arn:aws:secretsmanager:us-east-1:313476888478:secret:blackdiamond/49f/session-6bwJqe rather than a '-*' prefix pattern. terraform fmt -check exit 0; validate 'Success! The configuration is valid.'; plan 'Plan: 0 to add, 1 to change, 0 to destroy', the one change being bd_exporter_additional updated in-place. | CLOSED 20260928T113552Z |
| L2 | activation | terraform apply via .tools/safe-apply.sh on infra/aws/terraform/bd-pipeline | plan names 0 to add, 1 to change, 0 to destroy; apply succeeds | safe-apply.sh (Rule 18) on infra/aws/terraform/bd-pipeline, with the apply subcommand: 'Plan: 0 to add, 1 to change, 0 to destroy' then 'aws_iam_role_policy.bd_exporter_additional: Modifications complete after 0s [id=bd-exporter-ec2-role:AdditionalPermissions]' and 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' -- A5's stated 0/1/0 acceptance, met. The resolved element is the exact secret arn:aws:secretsmanager:us-east-1:313476888478:secret:blackdiamond/49f/session-6bwJqe, not a '-*' prefix pattern. Note on the invocation: a first call passing only '-auto-approve' was REFUSED by the wrapper ('no apply subcommand in the arguments') -- it gates terraform apply only; nothing ran on that call. | CLOSED 20260928T114351Z |
| L3 | verify | post-apply 0-diff | terraform plan -detailed-exitcode returns 0 | terraform plan -detailed-exitcode returned 0 and printed 'No changes. Your infrastructure matches the configuration.' Read as the EXIT CODE plus the printed sentence, not from a positional slice: 0 means no-changes, 1 error, 2 changes-present, so a bare rc=0 read would have been ambiguous with an error-free plan carrying changes had the flag been absent. | CLOSED 20260928T114351Z |
| L4 | verify | the grant works from the instance, which is what Z-S44 closes on | an ssm run of the edited command list gets PAST load_bd_cookie with no AccessDeniedException | ssm:3b3df28d-e4ba-425d-8b2e-a4ae6e589b85 on i-0e6f6dc014fdcf1cd, 2026-09-28T11:45:39Z. THE GRANT WORKS AND THIS IS THE POSITIVE READ, not an absence of the old error: the run printed 'OK: bearer minted; session expires_in=7199 s' and then 'selection: 3 levels, 11 dimensions'. Minting a bearer REQUIRES reading blackdiamond/49f/session, so load_bd_cookie succeeded where the pre-grant run ssm:103d29fd died on AccessDeniedException at pull_bd_asset_dim_rest.py:172. Same instance, same document, same command list, the only change between them being this grant -- so the discriminator is clean. The as-of also resolved correctly on the instance: 'as-of (last completed trading day): 09/25/2026', matching MX-s-9's value. The run then FAILED further downstream on an unrelated vendor 400 rejecting template.dateRangeType='AsOfDate'; that is a module defect filed as its own row and is NOT an IAM finding. Instance self-stopped 11:48:25Z; SSM recorded Failed, so the honest exit held a fourth time. | CLOSED 20260928T115010Z |

## Log

- 20260928T112834Z OPENED by 0.7.0_AE_CloudOps~I with 4 leg(s)
- 20260928T113552Z LEG L1 closed: 5d7d1769e3 -- one Resource element added to aws_iam_role_policy.bd_exporter_additional. CORRECTION TO THAT COMMIT MESSAG
- 20260928T114351Z LEG L2 closed: safe-apply.sh (Rule 18) on infra/aws/terraform/bd-pipeline, with the apply subcommand: 'Plan: 0 to add, 1 to change, 0 t
- 20260928T114351Z LEG L3 closed: terraform plan -detailed-exitcode returned 0 and printed 'No changes. Your infrastructure matches the configuration.' Re
- 20260928T115010Z LEG L4 closed: ssm:3b3df28d-e4ba-425d-8b2e-a4ae6e589b85 on i-0e6f6dc014fdcf1cd, 2026-09-28T11:45:39Z. THE GRANT WORKS AND THIS IS THE P
- 20260928T115010Z CLOSED -- all 4 legs proven
