# Deploy Completion Record
**Date opened:** 2026-10-14T15:38:53.430528+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R30b: release 29b ADDENDUM 1 -- ONE further statement IrptRequestsDecryptViaDynamoOnly (kms:Decrypt only, Resource the irpt-requests table's own KMS key ARN, StringEquals kms:ViaService dynamodb.us-east-1.amazonaws.com and kms:EncryptionContext:aws:dynamodb:tableName irpt-requests) added to the ticket role policy opal_ticket_api_ddb through the scoped plan; the second widening of 29b; NO code rollback (CTO half @6dc939b104, COO addendum blob 827d0857e0); the 29b sitting ledger irpt-r30-ticket-sitting-20261014 stays OPEN; no ticket request is submitted
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G2 | verify | hashes read; markers 0 live open entries naming the ticket role; table key ARN and the four earlier statements read; worktree edit of main.tf adds exactly the signed statement, git diff printed and hashed; scoped plan -target=aws_iam_role_policy.opal_ticket_api_ddb shows ONE in-place update adding only that statement with the resolved Resource equal to the table's KMSMasterKeyArn | plan summary and diff |  | OPEN |
| A | activation | .tools/safe-apply.sh on the saved plan; re-plan No changes; get-role-policy reads FIVE statements, the new one exactly once equal to the signed text, the earlier four equal | apply line and read-back |  | OPEN |
| S | verify | the statement shape read back: Action [kms:Decrypt] only, Resource the key ARN not the alias, the two StringEquals conditions exactly | printed shape |  | OPEN |
| T5 | verify | simulator kms:Decrypt on the key, one resource per call: a) ViaService+tableName context allowed, b) without ViaService DENIED, c) other table context DENIED, d) kms:GenerateDataKey DENIED | printed decisions |  | OPEN |

## Log

- 20261014T153853Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
