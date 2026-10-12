# Deploy Completion Record
**Date opened:** 2026-10-11T13:32:49.659657+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T132727Z
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
| L4 | verify | first 13:25Z fire after the apply: REPORT rc 0, inputs holdings as_of == as_of, characteristics.json LastModified >= 13:25Z | CloudWatch excerpt and head-object | First fire on the new clock, 2026-10-12 13:25Z, read 13:26Z: cot-satellites-characteristics-producer START 13:25:14Z (rule cron(25 13)), RUN COMPLETE rc 0, REPORT Duration 47545 ms (of the 120 s timeout), inputs line 'holdings as_of=2026-10-12 sats=9 \| positioning as_of=2026-10-09 \| bbg 2026-10-09 rows=171'; platinum/satellites/characteristics.json LastModified 2026-10-12T13:26:03Z (>= 13:25Z), as_of 2026-10-12, holdings_as_of 2026-10-12 == as_of. The 13:15Z registry fire it follows wrote holdings.json at 13:15:48Z (10 min before, margin as signed). The one-day lag the ruling removes does not appear. Previous version 2026-10-11T12:31:02Z, 68606 B; new 68601 B. | CLOSED 20261012T132726Z |

## Log

- 20261011T133249Z OPENED by 2.0.0_SA_COO~G1 with 4 leg(s)
- 20261011T133318Z LEG L1 closed: Read live 2026-10-11T13:3xZ: rule cot-satellites-characteristics-producer-daily ScheduleExpression cron(30 12 * * ? *), 
- 20261011T133421Z LEG L2 closed: safe-apply -chdir=infra/aws/terraform/cot-pipeline apply of a saved plan, -target aws_cloudwatch_event_rule.cot_satellit
- 20261011T133421Z LEG L3 closed: Read live 2026-10-11T13:3xZ after the apply: describe-rule cot-satellites-characteristics-producer-daily ScheduleExpress
- 20261012T132726Z LEG L4 closed: First fire on the new clock, 2026-10-12 13:25Z, read 13:26Z: cot-satellites-characteristics-producer START 13:25:14Z (ru
- 20261012T132727Z CLOSED -- all 4 legs proven
