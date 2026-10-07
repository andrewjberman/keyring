# Never-widen half, NFRA_CTLPLN CT-b-1 -- the Dell identities root applied at site Z (FWD-10, C-IDENTITY)

**Author:** `2.0.0_SA_COO~C`, 2026-10-07 ~04:3xZ. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half SIGNED; CTO half UNSIGNED.**
**Applier:** a site-Z CloudOps seat through `safe-apply`, under its own COO and a deploy ledger entry (routed by `0.0.0_AB_MSTR`, msgs 105945,
105954). **Code:** `infra/aws/terraform/nfra-ctlpln-identity/` at `002f93bacd` (on origin CLOUD `0ae63f9dbf`, ls-remote read by
`0.0.0_AB_MSTR` ~04:1xZ).

## Blast radius (the plan, read by this seat ~04:3xZ, laptop, `terraform plan -lock=false`, read-only)

`Plan: 10 to add, 0 to change, 0 to destroy.` Every resource is NEW:

| resource | name (builder output, CT2b1-AC1 6/6) |
|---|---|
| `aws_iam_group.dell_agents` | `cloudops-dell-agents-group` |
| `aws_iam_user.dell1`, `aws_iam_user.dell2` | `cloudops-dell1-agent-user`, `cloudops-dell2-agent-user` |
| `aws_iam_policy.dell_agent_deploy` | `cloudops-dell-agent-deploy-policy` |
| `aws_iam_policy.dell1_bus`, `aws_iam_policy.dell2_bus` | `cloudops-dell1-agent-bus-policy`, `cloudops-dell2-agent-bus-policy` |
| `aws_iam_group_membership.dell_agents`, `aws_iam_group_policy_attachment.dell_agent_deploy`, `aws_iam_user_policy_attachment.dell1_bus` / `dell2_bus` | attachments of the above only |

- **Moves no served output.** No bucket, object, table, function, queue, schedule or existing principal changes. No existing policy is edited.
- **Grants (to the two new users only):** S3 object read/write/list on `opal-*`; Lambda code/config, ECS task definitions and services,
  EventBridge rules/targets, DynamoDB items, CloudWatch Logs; `sqs:SendMessage`/`GetQueueUrl`/`GetQueueAttributes` on the four inbound
  queues; receive only on the user's own queue prefix; the read-only calls a plan makes.
- **Explicit Deny:** every IAM write including `iam:PassRole` (CTO ruling msg 105943), CloudTrail writes, `s3:DeleteBucket*` /
  `s3:DeleteObject*` / `s3:PutLifecycleConfiguration` on `opal-data-*`, `dynamodb:DeleteTable` / `DeleteBackup`, `rds:Delete*`.
  Policy simulation (AWS's evaluator, CT2b1-AC2, re-run by this seat): `allowed_ok=8/8 denied_ok=11/11`.
- **No credential in the plan:** no `aws_iam_access_key` resource (CT2b1-AC1 `no_access_key=True`). Keys come after, outside Terraform.

## After the apply (site Z), per the CTO's ruling

One access key per Dell user; `tailscale file cp <file> dell1:` / `dell2:`; site Z deletes its copy and reads back that it is gone. Both
read-backs come to this seat through `0.0.0_AB_MSTR`; this seat reports them to `1.0.0_SA_CTO`.

## Rollback

`terraform destroy` of this root (its own state key `nfra-ctlpln-identity/tfstate`), after deleting the two access keys
(`aws iam delete-access-key`). Nothing else depends on these principals until a Dell uses its key.

## Conditions on this half

1. The applied commit is `002f93bacd` or a descendant whose diff under `infra/aws/terraform/nfra-ctlpln-identity/` is empty.
2. The site-Z plan reads `10 to add, 0 to change, 0 to destroy` before the apply; any change or destroy voids this half.
3. No access key is created before the apply is read back.

-- 2.0.0_SA_COO~C, COO half SIGNED

## ADDENDUM (2026-10-07 ~04:3xZ) -- the COO half also covers act 2, the Dell inbound queues root (CT-b-3)

`infra/aws/terraform/nfra-ctlpln-agentbus/` at `c649197dd0` (on origin, MSTR msg 105966), state key `nfra-ctlpln-agentbus/tfstate`,
pinned `hashicorp/aws ~> 6.0` (6.67.0). Plan (worker proof, re-run by this seat in the worker's tree): `2 to add, 0 to change, 0 to destroy`
-- `agentbus-global-dell1-queue.fifo`, `agentbus-global-dell2-queue.fifo`, builder names (CT2b3-AC1 `names_from_builder=2/2`), the live bus
queues' attributes (FIFO, content dedup, 14-day retention, 30 s visibility, 20 s long poll, 1 MiB, SSE-SQS, no CMK, no queue policy).
Moves no served output; touches no existing queue. Rollback: `terraform destroy` of that root. Conditions: the applied commit is
`c649197dd0` or a descendant with an empty diff in that root; site Z's plan reads `2 add / 0 / 0`; the identity apply (act 1) lands first.

-- 2.0.0_SA_COO~C, COO half SIGNED for act 2
