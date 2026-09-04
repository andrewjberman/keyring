# Deploy Completion Record
**Date opened:** 2026-09-04T01:44:04.946589+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260904T020212Z
**Deploy:** NFRA_OPSEC202609 TO-OP-S-14-21 deliverable 6: declare and APPLY the sentinel's IAM role (opal-sentinel), hand the APPLIED ARN to TO-OP-S-22 before any function code is deployed. The apply lands the shared opsec root, so TO-OP-S-15-19's four already-committed resources ride it.
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of infra/aws/terraform/opsec/iam_sentinel.tf | commit hash | commit c027eb4f6f, author 0.7.0_AE_CloudOps~S -- iam_sentinel.tf + this ledger + .open_deploys entry, 3 files, 322 insertions. Push state: LOCAL (GATE 5, push is the integrator's). | CLOSED 20260904T015935Z |
| L2 | activation | terraform apply on the opsec root via safe-apply -- 6 to add, 0 change, 0 destroy | apply output with the created-resource count | safe-apply (HALT_ACK=1 on a 13d-old routine message addressed to 0.5.0_AE_OpalETL~Z, reviewed, unrelated to this root) -> 'Apply complete! Resources: 6 added, 0 changed, 0 destroyed.' rc=0. Created: aws_iam_role.sentinel + aws_iam_role_policy.sentinel (this face) and aws_iam_role.ipset_reconciler, aws_iam_role_policy.ipset_reconciler, aws_iam_role.ipblock_cli, aws_iam_role_policy.ipblock_cli (TO-OP-S-15-19, riding the shared root as declared at commit time). | CLOSED 20260904T015935Z |
| L3 | verify | UNSCOPED re-plan 0-diff on the opsec root after apply | terraform plan -detailed-exitcode rc | terraform plan -detailed-exitcode UNSCOPED on the opsec root: rc=0, 'No changes. Your infrastructure matches the configuration.' Unscoped, not -target: a -target re-plan verifying a -target apply is the named blind spot in CLAUDE.md Rule 22. | CLOSED 20260904T015936Z |
| L4 | verify | APPLIED-plane read of opal-sentinel: get-role plus get-role-policy, not the plan | aws iam output | APPLIED plane via the live primitive (not comp-iam, which is DECLARED-view per Rule 22a). get-role: arn:aws:iam::313476888478:role/opal-sentinel, CreateDate 2026-09-04T01:51:56Z. get-role-policy opal-sentinel-table-evidence-and-notify: 8 statements; ProjectKeyThroughDynamoDBAndS3 APPLIED as ['kms:GenerateDataKey','kms:Decrypt'] with DescribeKey absent as intended; SendExactlyOneNotificationPerEvent resource arn:aws:ses:us-east-1:313476888478:identity/opalinvest.dev conditioned StringEquals ses:FromAddress=noreply@opalinvest.dev; DENY SentinelMayNeverWriteAnIpSet on UpdateIPSet/CreateIPSet/DeleteIPSet Resource *. | CLOSED 20260904T015936Z |
| L5 | verify | APPLIED ARN handed to 0.7.0_AE_CloudOps~W for the TO-OP-S-22 verdict, and the apply announced to 0.7.0_AE_CloudOps~T which is holding on it | broker message id | Broker msg 20110 to 0.7.0_AE_CloudOps~W (the TO-OP-S-22 verdict), 20111 to 0.7.0_AE_CloudOps~T (the lane holding on this apply), 20112 to 2.0.0_SA_COO~Z. 3 DELIVERED / 0 QUEUED / 0 REFUSED, denominator 3. Carries all three applied ARNs, the 8-statement applied-plane read, and the correction that this apply CREATED TO-OP-S-15-19's four resources. | CLOSED 20260904T020212Z |

## Log

- 20260904T014404Z OPENED by 0.7.0_AE_CloudOps~S with 5 leg(s)
- 20260904T015935Z LEG L1 closed: commit c027eb4f6f, author 0.7.0_AE_CloudOps~S -- iam_sentinel.tf + this ledger + .open_deploys entry, 3 files, 322 inser
- 20260904T015935Z LEG L2 closed: safe-apply (HALT_ACK=1 on a 13d-old routine message addressed to 0.5.0_AE_OpalETL~Z, reviewed, unrelated to this root) -
- 20260904T015936Z LEG L3 closed: terraform plan -detailed-exitcode UNSCOPED on the opsec root: rc=0, 'No changes. Your infrastructure matches the configu
- 20260904T015936Z LEG L4 closed: APPLIED plane via the live primitive (not comp-iam, which is DECLARED-view per Rule 22a). get-role: arn:aws:iam::3134768
- 20260904T020212Z LEG L5 closed: Broker msg 20110 to 0.7.0_AE_CloudOps~W (the TO-OP-S-22 verdict), 20111 to 0.7.0_AE_CloudOps~T (the lane holding on this
- 20260904T020212Z CLOSED -- all 5 legs proven
