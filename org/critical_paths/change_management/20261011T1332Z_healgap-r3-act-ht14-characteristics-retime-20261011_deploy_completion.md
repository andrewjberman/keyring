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
| L1 | verify | rollback state read live: the rule's ScheduleExpression, Description, State, target | values printed from describe-rule and list-targets-by-rule | Read live 2026-10-11T13:3xZ: rule cot-satellites-characteristics-producer-daily ScheduleExpression cron(30 12 * * ? *), State ENABLED, Description 'Daily Cottonwood satellite weighted-characteristics aggregate + the per-ticker block: ... Fires 12:30Z on its own clock, AFTER the 07:00 America/New_York Bloomberg pull in both DST states.'; target CotSatellitesCharacteristicsProducerDaily -> function cot-satellites-characteristics-producer, input null; today's artifact characteristics.json LastModified 12:31:02Z. Rollback = the file at 61d007d22c. | CLOSED 20261011T133318Z |
| L2 | activation | Terraform cot-pipeline safe-apply -target aws_cloudwatch_event_rule.cot_satellites_characteristics_producer_daily, saved plan | plan reads exactly 1 changed in place, only schedule_expression and description; apply result | safe-apply -chdir=infra/aws/terraform/cot-pipeline apply of a saved plan, -target aws_cloudwatch_event_rule.cot_satellites_characteristics_producer_daily. Plan read 'Plan: 0 to add, 1 to change, 0 to destroy', the one resource updated in place with exactly two attributes differing: description and schedule_expression cron(30 12 * * ? *) -> cron(25 13 * * ? *); nothing else. Apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' 2026-10-11T13:3xZ; tagauthz gate PASSED, tombstone gate CLEAN (0 creates vs 7). Bytes: fix fd95aeb659 merged 00cbe27985, CTO half @7422d986d0. | CLOSED 20261011T133421Z |
| L3 | verify | describe-rule reads cron(25 13 * * ? *) ENABLED with the new description; target and permission unchanged | values printed from live reads | Read live 2026-10-11T13:3xZ after the apply: describe-rule cot-satellites-characteristics-producer-daily ScheduleExpression cron(25 13 * * ? *), State ENABLED, Description now 'Fires 13:25Z on its own clock, AFTER the stamp-gated 13:15Z registry fire has finished and after the 07:00 America/New_York Bloomberg pull in both DST states.'; target CotSatellitesCharacteristicsProducerDaily -> cot-satellites-characteristics-producer input null (unchanged); lambda policy EventBridgeCotSatellitesCharacteristicsProducerDaily scoped to the rule ARN (unchanged). Today's 13:25Z passed before the apply, so the first fire on the new clock is 2026-10-12 13:25Z; today's artifact is the 12:31:02Z one. | CLOSED 20261011T133421Z |
| L4 | verify | first 13:25Z fire after the apply: REPORT rc 0, inputs holdings as_of == as_of, characteristics.json LastModified >= 13:25Z | CloudWatch excerpt and head-object |  | OPEN |

## Log

- 20261011T133249Z OPENED by 2.0.0_SA_COO~G1 with 4 leg(s)
- 20261011T133318Z LEG L1 closed: Read live 2026-10-11T13:3xZ: rule cot-satellites-characteristics-producer-daily ScheduleExpression cron(30 12 * * ? *), 
- 20261011T133421Z LEG L2 closed: safe-apply -chdir=infra/aws/terraform/cot-pipeline apply of a saved plan, -target aws_cloudwatch_event_rule.cot_satellit
- 20261011T133421Z LEG L3 closed: Read live 2026-10-11T13:3xZ after the apply: describe-rule cot-satellites-characteristics-producer-daily ScheduleExpress
