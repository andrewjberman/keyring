# Deploy Completion Record
**Date opened:** 2026-10-14T12:41:38.291328+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-l-4 (round 8, FWD-9(b)): the first real retirement -- DISABLED EventBridge rule inf-gold-full-on-bronze-complete (C3) in infra/aws/terraform/inf-pipeline/. ONE scoped safe-apply on exactly four addresses: DESTROY aws_cloudwatch_event_rule.inf_gold_full_on_bronze_complete, aws_cloudwatch_event_target.inf_gold_full_on_bronze_complete_target, aws_lambda_permission.allow_eventbridge_inf_gold_full_on_bronze_complete; CHANGE aws_sqs_queue_policy.inf_gold_trigger_dlq (rule ARN removed from the aws:SourceArn list). Plan must read 0 to add, 1 to change, 3 to destroy. Pair: COO half cc781f974a, CTO half 28ae3ff0b4 (condition C1: alarms.tf stays byte-unchanged). Prior state saved at deliverables/0.7.0_AE_CloudOps~FB1/PRIOR_STATE_C3.json (rule DISABLED, one target to inf-gold-trigger with DLQ inf-gold-trigger-dlq, 3 lambda statements, DLQ policy with 3 SourceArns). Consumers: re-census 2026-10-14T12:35Z, 1 AWS hit (the rule itself) across 2929 nodes, 0 consumers. Rollback: git revert of the removal commit plus the same scoped safe-apply re-creates the rule DISABLED; enabling is not covered. inf-gold-trigger (code NBbjVPCW..., config, INF_GOLD_DISPATCH_HOLD) and the other two rules read byte-unchanged before and after.
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pair halves at HEAD and unchanged (cc781f974a, 28ae3ff0b4), FB-l-3 merged and PASS, target not Door 6, re-census 0 consumers over a printed denominator, prior state saved | the commits, the denominator, PRIOR_STATE_C3.json |  | OPEN |
| L2 | git | the removal commit: three resource blocks and the one DLQ-policy SourceArn line (and its comment) in eventbridge.tf, alarms.tf untouched | commit hash |  | OPEN |
| L3 | activation | scoped safe-apply -target the four addresses: plan 0 to add 1 to change 3 to destroy, apply on the saved plan | plan summary and apply line |  | OPEN |
| L4 | verify | describe-rule ResourceNotFoundException; lambda policy 2 statements; DLQ policy 2 SourceArns; inf-gold-trigger and the other two rules byte-unchanged; same census 0; plan after apply | the reads and hashes |  | OPEN |
| L5 | git | RETIRE_RECORD.json committed first; rows, instance and status flip second | commit hash |  | OPEN |

## Log

- 20261014T124138Z OPENED by 0.7.0_AE_CloudOps~FB1 with 5 leg(s)
