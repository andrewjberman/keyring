# Deploy Completion Record
**Date opened:** 2026-09-28T11:28:34.940969+00:00
**Status:** OPEN
**Deploy:** bd-exporter-ec2-role gains GetSecretValue on the 49F session secret by EXTENDING the existing AdditionalPermissions statement, so the ported asset-dim REST producer can authenticate (MX-s-10 A5, rows Z-S44/Z-S45)
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: one Resource element added to aws_iam_role_policy.bd_exporter_additional in infra/aws/terraform/bd-pipeline/iam.tf | commit hash |  | OPEN |
| L2 | activation | terraform apply via .tools/safe-apply.sh on infra/aws/terraform/bd-pipeline | plan names 0 to add, 1 to change, 0 to destroy; apply succeeds |  | OPEN |
| L3 | verify | post-apply 0-diff | terraform plan -detailed-exitcode returns 0 |  | OPEN |
| L4 | verify | the grant works from the instance, which is what Z-S44 closes on | an ssm run of the edited command list gets PAST load_bd_cookie with no AccessDeniedException |  | OPEN |

## Log

- 20260928T112834Z OPENED by 0.7.0_AE_CloudOps~I with 4 leg(s)
