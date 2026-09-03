# Deploy Completion Record
**Date opened:** 2026-09-03T23:43:40.162924+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-8R2B -- opal-users-v2 SSE from the AWS-managed key 86cc6c40 to the project CMK 64f25291 (alias/opal-security), at its REAL carrier shared-infra/dynamo.tf, SCOPED -target apply. ROLLBACK: arn:aws:kms:us-east-1:313476888478:key/86cc6c40-2387-4446-b7e1-de79392e06b3 (the AWS-managed key ARN captured BEFORE the first flip). UNSCOPED baseline BEFORE any edit: 'No changes. Your infrastructure matches the configuration.' -- so nothing foreign was pending and nothing else can ride
**Authored by:** 0.7.0_AE_CloudOps~W
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | shared-infra/dynamo.tf server_side_encryption block committed under 0.7.0_AE_CloudOps~W | commit hash |  | OPEN |
| L2 | activation | safe-apply -target=aws_dynamodb_table.opal_users_v2 -- MUST read 0 to add, 0 to destroy, 0 forces-replacement | apply output |  | OPEN |
| L3 | verify | live AFTER read: KMSMasterKeyArn 64f25291 (not 86cc6c40); TableId 8e590a34 and CreationDateTime IDENTICAL before/after = updated not replaced; DeletionProtectionEnabled still true; PITR still ENABLED | pasted reads |  | OPEN |
| L4 | verify | UNSCOPED re-plan 0-diff (never a -target re-plan -- a scoped check cannot see what the scope excluded) | unscoped plan output |  | OPEN |
| L5 | verify | S8B-AC3 DATA-PLANE exercise: fixture item put + get-item read back on the NEW key, then delete + read the deletion back. Control-plane key ARN is NOT this leg | data-plane call output |  | OPEN |

## Log

- 20260903T234340Z OPENED by 0.7.0_AE_CloudOps~W with 5 leg(s)
