# Deploy Completion Record
**Date opened:** 2026-09-03T09:29:56.440870+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260903T093533Z
**Deploy:** NFRA_OPSEC202609.TO-OP-S-8 -- deletion_protection_enabled on opal-users-v2 at its REAL carrier shared-infra/dynamo.tf, SCOPED -target apply (shared-infra carries unrelated pre-existing drift that must not ride)
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | shared-infra/dynamo.tf edit committed under 0.7.0_AE_CloudOps~S | commit hash | commit 946ec2c50d on SITEZ, author 0.7.0_AE_CloudOps~S -- shared-infra/dynamo.tf deletion_protection_enabled on opal_users_v2, row S17, ledger; 3 files / 58 insertions; row gate rc=0 | CLOSED 20260903T093252Z |
| L2 | activation | safe-apply -target=aws_dynamodb_table.opal_users_v2 (1 change, 0 add, 0 destroy, 0 replace) | apply output | safe-apply rc=0 with -target=aws_dynamodb_table.opal_users_v2 (targeting DECLARED, per cloud-ops pre-flight step 2). 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | CLOSED 20260903T093533Z |
| L3 | verify | DeletionProtectionEnabled true + PITR still ENABLED + SSE unchanged + TableId identical before/after | pasted reads | Live AFTER read: DeletionProtectionEnabled False->True; SSEType KMS with KMSMasterKeyArn 86cc6c40... UNCHANGED before/after (the apply did NOT drop encryption despite the resource block declaring no server_side_encryption -- the specific hazard checked); TableId 8e590a34 and CreationDateTime 2026-01-08T12:46:52 IDENTICAL before/after = updated not replaced; PITR still ENABLED, EarliestRestorableDateTime 2026-07-30T05:34:35-04:00. | CLOSED 20260903T093533Z |
| L4 | verify | UNSCOPED re-plan: opal_users_v2 shows 0-diff and the pre-existing global_graph drift is STILL THERE untouched (the scoped-check trap: a -target apply must not be verified by a -target re-plan) | unscoped plan output | UNSCOPED re-plan (never a -target re-plan -- a scoped check cannot see what the scope excluded). Two-sided PASS: HALF 1, aws_dynamodb_table.opal_users_v2 is ABSENT from the plan = 0-diff on this seat's change. HALF 2, '# aws_s3_bucket_lifecycle_configuration.global_graph will be updated in-place / Plan: 0 to add, 1 to change, 0 to destroy' -- the FOREIGN drift is STILL PRESENT and untouched, proving this seat did not silently apply another seat's change. A clean unscoped plan here would have been a FAILURE, not a success. | CLOSED 20260903T093533Z |

## Log

- 20260903T092956Z OPENED by 0.7.0_AE_CloudOps~S with 4 leg(s)
- 20260903T093252Z LEG L1 closed: commit 946ec2c50d on SITEZ, author 0.7.0_AE_CloudOps~S -- shared-infra/dynamo.tf deletion_protection_enabled on opal_use
- 20260903T093533Z LEG L2 closed: safe-apply rc=0 with -target=aws_dynamodb_table.opal_users_v2 (targeting DECLARED, per cloud-ops pre-flight step 2). 'Ap
- 20260903T093533Z LEG L3 closed: Live AFTER read: DeletionProtectionEnabled False->True; SSEType KMS with KMSMasterKeyArn 86cc6c40... UNCHANGED before/af
- 20260903T093533Z LEG L4 closed: UNSCOPED re-plan (never a -target re-plan -- a scoped check cannot see what the scope excluded). Two-sided PASS: HALF 1,
- 20260903T093533Z CLOSED -- all 4 legs proven
