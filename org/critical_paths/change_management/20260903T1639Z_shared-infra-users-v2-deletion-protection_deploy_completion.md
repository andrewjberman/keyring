# Deploy Completion Record
**Date opened:** 2026-09-03T16:39:02.033731+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260903T164637Z
**Deploy:** Declare deletion_protection_enabled=true on aws_dynamodb_table.opal_users_v2 so desired matches applied; no-op scoped apply
**Authored by:** 0.8.0_AE_CloudComp~K
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | infra/aws/terraform/shared-infra/dynamo.tf one-line deletion_protection_enabled=true declaration | exact declaration commit hash under 0.8.0_AE_CloudComp~K | Declaration commit 14fbeace00 under 0.8.0_AE_CloudComp~K adds only deletion_protection_enabled = true to aws_dynamodb_table.opal_users_v2; .tools/terraform.exe -chdir=infra/aws/terraform/shared-infra fmt -check dynamo.tf exited 0. Ledger was opened and committed first at 45b99d1f96. Live pre-read at 2026-09-03T16:41:22Z was true. | CLOSED 20260903T164326Z |
| L2 | verify | NEW saved plan infra/aws/terraform/shared-infra/users-v2-deletion-protection-targeted.tfplan target aws_dynamodb_table.opal_users_v2 | org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-USERS-DELPROT.scoped-plan.txt reads No changes / 0 add 0 change 0 destroy on the exact target | NEW saved plan infra/aws/terraform/shared-infra/users-v2-deletion-protection-targeted.tfplan produced with -target=aws_dynamodb_table.opal_users_v2; captured org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-USERS-DELPROT.scoped-plan.txt says No changes. Your infrastructure matches the configuration. Scoped plan exit 0; denominator one refreshed target address, zero planned resource changes. | CLOSED 20260903T164354Z |
| L3 | verify | safe-apply saved scoped no-op plan | org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-USERS-DELPROT.safe-apply-output.txt reads no changes / 0 added 0 changed 0 destroyed | safe-apply consumed infra/aws/terraform/shared-infra/users-v2-deletion-protection-targeted.tfplan; org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-USERS-DELPROT.safe-apply-output.txt ends Apply complete! Resources: 0 added, 0 changed, 0 destroyed. It was the saved scoped no-op plan; never bare and never unscoped. | CLOSED 20260903T164554Z |
| L4 | verify | unscoped shared-infra control plus live opal-users-v2 post-read | unscoped output lists exactly nine untouched API-route auth drifts, users-table line gone and none applied; live DeletionProtectionEnabled=true | Amended acceptance ee688a660b. Unscoped control captured in org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-USERS-DELPROT.unscoped-post-plan.txt: Plan: 0 to add, 9 to change, 0 to destroy. The aws_dynamodb_table.opal_users_v2 deletion_protection line is GONE and aws_s3_bucket_lifecycle_configuration.global_graph is GONE. Whole address list: module.apigateway_portal.aws_apigatewayv2_route.r_as2dsme, r_c0k8rl0, r_gwygx58, r_m8wdq80, r_mxus2bs, r_o2xr1ct, r_ruzaqhq, r_sogv7z9, r_t81twif; each remains authorization_type CUSTOM -> NONE and authorizer_id naqxlm -> null. NONE applied. Live post-read at 2026-09-03T16:46:21Z captured in NFRA_GLOBGRPH.TO-USERS-DELPROT.live-post-read.txt returned DeletionProtectionEnabled=true. | CLOSED 20260903T164637Z |

## Log

- 20260903T163902Z OPENED by 0.8.0_AE_CloudComp~K with 4 leg(s)
- 20260903T164326Z LEG L1 closed: Declaration commit 14fbeace00 under 0.8.0_AE_CloudComp~K adds only deletion_protection_enabled = true to aws_dynamodb_ta
- 20260903T164354Z LEG L2 closed: NEW saved plan infra/aws/terraform/shared-infra/users-v2-deletion-protection-targeted.tfplan produced with -target=aws_d
- 20260903T164554Z LEG L3 closed: safe-apply consumed infra/aws/terraform/shared-infra/users-v2-deletion-protection-targeted.tfplan; org/tier2_senior/0.8.
- 20260903T164637Z LEG L4 closed: Amended acceptance ee688a660b. Unscoped control captured in org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOB
- 20260903T164637Z CLOSED -- all 4 legs proven
