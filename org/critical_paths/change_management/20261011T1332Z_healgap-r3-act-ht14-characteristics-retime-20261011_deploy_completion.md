# Deploy Completion Record
**Date opened:** 2026-10-11T13:32:49.659657+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP R3 HG-t-14: cot-satellites-characteristics-producer-daily schedule_expression cron(30 12) -> cron(25 13) and description, in place, via safe-apply -target. CTO half SIGNED @7422d986d0 (ADDENDUM 4, msg 3893). Rollback: terraform apply -target the same rule from 61d007d22c (cron(30 12 * * ? *) and the prior description).
**Authored by:** 2.0.0_SA_COO~G1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 48.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | rollback state read live: the rule's ScheduleExpression, Description, State, target | values printed from describe-rule and list-targets-by-rule |  | OPEN |
| L2 | activation | Terraform cot-pipeline safe-apply -target aws_cloudwatch_event_rule.cot_satellites_characteristics_producer_daily, saved plan | plan reads exactly 1 changed in place, only schedule_expression and description; apply result |  | OPEN |
| L3 | verify | describe-rule reads cron(25 13 * * ? *) ENABLED with the new description; target and permission unchanged | values printed from live reads |  | OPEN |
| L4 | verify | first 13:25Z fire after the apply: REPORT rc 0, inputs holdings as_of == as_of, characteristics.json LastModified >= 13:25Z | CloudWatch excerpt and head-object |  | OPEN |

## Log

- 20261011T133249Z OPENED by 2.0.0_SA_COO~G1 with 4 leg(s)
