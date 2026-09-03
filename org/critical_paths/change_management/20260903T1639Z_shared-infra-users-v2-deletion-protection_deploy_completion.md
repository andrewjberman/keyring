# Deploy Completion Record
**Date opened:** 2026-09-03T16:39:02.033731+00:00
**Status:** OPEN
**Deploy:** Declare deletion_protection_enabled=true on aws_dynamodb_table.opal_users_v2 so desired matches applied; no-op scoped apply
**Authored by:** 0.8.0_AE_CloudComp~K
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | infra/aws/terraform/shared-infra/dynamo.tf one-line deletion_protection_enabled=true declaration | exact declaration commit hash under 0.8.0_AE_CloudComp~K |  | OPEN |
| L2 | verify | NEW saved plan infra/aws/terraform/shared-infra/users-v2-deletion-protection-targeted.tfplan target aws_dynamodb_table.opal_users_v2 | org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-USERS-DELPROT.scoped-plan.txt reads No changes / 0 add 0 change 0 destroy on the exact target |  | OPEN |
| L3 | verify | safe-apply saved scoped no-op plan | org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-USERS-DELPROT.safe-apply-output.txt reads no changes / 0 added 0 changed 0 destroyed |  | OPEN |
| L4 | verify | unscoped shared-infra control plus live opal-users-v2 post-read | unscoped output lists exactly nine untouched API-route auth drifts, users-table line gone and none applied; live DeletionProtectionEnabled=true |  | OPEN |

## Log

- 20260903T163902Z OPENED by 0.8.0_AE_CloudComp~K with 4 leg(s)
