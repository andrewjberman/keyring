# Andrew-direct 2026-10-13 ~16:5xZ at the 2.0.0_SA_COO~C terminal -- the Dell agent users get Andrew_Berman's access pattern (the admin group), keeping three denies

**Recorded by:** `2.0.0_SA_COO~C` (laptop), same turn. **Supersedes** the grant-by-grant shape of the CTO ruling `CTO_RULING_DELL_IDENTITIES_GET_THEIR_OWN_PERMISSIONS_THREE_GRANTS_NO_CROSSBOX_CLOUDOPS_20261013.md` (@1161dc05fc) and its grant (d) (msg 108771): the purpose there ("the Dell Boxes need the necessary permissions so this cross-box behavior is not necessary") is served whole by this.

## 1. Andrew's words, VERBATIM

Question: *"The DELL boxes cannot be perpetually held up on grants, i thought we already rectified this that they should just be using the same access pattern/ability as Andrew_Berman? Otherwise we are always going to be holding them up in one way or another."*

The card put to him: *"Give both Dell users your access: (a) exact parity -- join AdministratorAccessOpalCapital and drop every Dell deny; or (b) join the admin group but keep three denies: no CloudTrail writes, no production S3 deletes, no table/database deletes?"* REC (b).

Answer: *"Sure let's do rec b"*

## 2. What was measured before the card (live IAM read, laptop identity, ~16:4xZ)

- `Andrew_Berman`: group `AdministratorAccessOpalCapital`; attached `OpalSecretsReader`, `ycharts-credentials-read`, `inf-andrew-otp-write`, `IAMUserChangePassword`; inline `opal-data-cottonwood`, `opal-data-inflection`; no Deny.
- `cloudops-dell1-agent-user`, `cloudops-dell2-agent-user`: group `cloudops-dell-agents-group` (root `infra/aws/terraform/nfra-ctlpln-identity/`, nine managed policies of curated Allows) plus per-user bus and SSM policies. Deny statements found so far: in `dell_deploy_policy.json` `DenyCloudTrailWrites`, `DenyS3DeletesOnProductionData`, `DenyTableAndDatabaseDeletes`, `DenyApiKeyReads`, `DenyCutoverParameterWrites`, `DenyProtectedFunctions`; in `dell_create_policy.json` `DenyAuditTrailBucketWrites`; in `dell_iam_roles_policy.json` a narrow Deny on user, group, access-key, login-profile, MFA and account-setting IAM writes.

## 3. The ruling, as it binds

1. Both Dell agent users become members of `AdministratorAccessOpalCapital` (Andrew_Berman's group), by Terraform in `infra/aws/terraform/nfra-ctlpln-identity/`.
2. Every Deny that reaches either Dell user is REMOVED except three classes: CloudTrail and audit-trail writes (`DenyCloudTrailWrites`, `DenyAuditTrailBucketWrites`), production S3 object deletes (`DenyS3DeletesOnProductionData`), table and database deletes (`DenyTableAndDatabaseDeletes`).
3. One change, applied by `safe-apply` under one signed never-widen pair (COO half `2.0.0_SA_COO~C`, CTO half `1.0.0_SA_CTO`), never a console edit. It is the FIRST cell of NFRA_CTLPLN round 12 and replaces the three/four-grant cell.
4. Read-back by the Dell seats: dell2 decrypts one object under the IRPT key; dell1 runs one policy simulation; one Dell deploys-or-describes a formerly protected function; one Dell's delete of a production S3 object is still refused (the kept Deny). Codes and names only.
