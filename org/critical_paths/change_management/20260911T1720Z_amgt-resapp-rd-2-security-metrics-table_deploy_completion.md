# Deploy Completion Record
**Date opened:** 2026-09-11T17:20:58.227421+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T172431Z
**Deploy:** AMGT_RESAPP rd-2: create opal-amgt-security-metrics DynamoDB table (pre-computed ranking store)
**Authored by:** 0.9.0_WK_AMGT_RESAPP~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform apply infra/aws/terraform/amgt-resapp (aws_dynamodb_table.security_metrics) | safe-apply output: 1 added, 0 changed, 0 destroyed | safe-apply terraform apply -auto-approve in infra/aws/terraform/amgt-resapp: Apply complete! Resources: 1 added, 0 changed, 0 destroyed. Outputs: security_metrics_table_arn=arn:aws:dynamodb:us-east-1:313476888478:table/opal-amgt-security-metrics | CLOSED 20260911T172418Z |
| L2 | verify | opal-amgt-security-metrics live describe-table | aws dynamodb describe-table TableStatus ACTIVE + BillingMode PAY_PER_REQUEST | aws dynamodb describe-table --table-name opal-amgt-security-metrics --query Table.[TableName,TableStatus,BillingModeSummary.BillingMode] --output text => opal-amgt-security-metrics ACTIVE PAY_PER_REQUEST (measured post-apply) | CLOSED 20260911T172418Z |

## Log

- 20260911T172058Z OPENED by 0.9.0_WK_AMGT_RESAPP~2 with 2 leg(s)
- 20260911T172418Z LEG L1 closed: safe-apply terraform apply -auto-approve in infra/aws/terraform/amgt-resapp: Apply complete! Resources: 1 added, 0 chang
- 20260911T172418Z LEG L2 closed: aws dynamodb describe-table --table-name opal-amgt-security-metrics --query Table.[TableName,TableStatus,BillingModeSumm
- 20260911T172431Z CLOSED -- all 2 legs proven
