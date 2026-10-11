# Deploy Completion Record
**Date opened:** 2026-10-11T12:03:52.496834+00:00
**Status:** OPEN
**Deploy:** NFRA_IAMROLES202609.TO-IAM-x-4: RETIRE row 7 lambda-test-role -- detach the managed policy, delete the role, read back NoSuchEntity
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ROLLBACK | git | the site-Z recreation record | THIS LEG IS THE ROLLBACK ITSELF AND IT IS CLOSED BEFORE ANYTHING IS DELETED: round7/retire_row7/RECREATE_lambda-test-role.md is committed at a3994c4cb7 and carries the complete restore as exactly two commands -- aws iam create-role --role-name lambda-test-role --path / --description 'Scoped Lambda role - created 2026-02-19 IAM audit' --max-session-duration 3600 --assume-role-policy-document with the verbatim live trust document, then aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole. The role has 0 inline policies, 0 tags and no permissions boundary, so nothing else is owed. It is SITE-Z's OWN record because the laptop's is not in this clone, and a rollback that depends on a file this device cannot read is not a rollback. |  | OPEN |
| DETACH | activation | lambda-test-role | aws iam detach-role-policy returns rc=0 and list-attached-role-policies then reads EXACTLY [] -- the count moving 1 -> 0, not merely 'no error'. delete-role refuses while any policy is attached, so this leg is also the precondition for the next. |  | OPEN |
| DELETE | activation | lambda-test-role | aws iam delete-role returns rc=0. Preceded by step 0's five live re-reads, all matching the cell: RoleLastUsed empty (never assumed since 2026-02-19), trust lambda.amazonaws.com only with no Condition, 1 managed attachment, 0 inline policies, and nothing naming the role -- the served graph returning 1 hit across 2892 nodes (the role itself) plus a repo census of 4 hits across 7922 files that are ALL inventories listing it rather than policy documents granting on it. Step 0's STOP did not fire. |  | OPEN |
| READBACK | verify | lambda-test-role | get-role on the deleted role returns NoSuchEntity, BESIDE A POSITIVE CONTROL: the same call shape on an existing role (opal-smartx-lambda-role) returns the role. Without the control a NoSuchEntity is indistinguishable from a call that cannot reach IAM at all -- a failed retrieval returns a value. Both outputs recorded verbatim in round7/retire_row7/RETIRE_READBACK.md. |  | OPEN |

## Log

- 20261011T120352Z OPENED by 0.7.0_AE_CloudOps~IR with 4 leg(s)
