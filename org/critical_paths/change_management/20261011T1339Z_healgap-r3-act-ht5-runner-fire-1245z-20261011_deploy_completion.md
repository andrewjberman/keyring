# Deploy Completion Record
**Date opened:** 2026-10-11T13:39:31.055613+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP R3 HG-t-5: cot-rebalancer-runner-daily schedule_expression cron(0 6) -> cron(45 12), in place, via safe-apply -target. CTO half SIGNED @0c9f67d92d (ADDENDUM 5, msg 3898) with two named effects: (1) the cot-bronze-complete sentinel invocation (~11:32Z) becomes the day's first pull, the 12:45Z fire is the SKIP-IDEMPOTENT backstop; (2) the 07:00Z cot-satellites-registry-producer-daily rule fails loudly every day, EXPECTED COUNT 3 failed attempts per day (~07:00-07:03Z) until its own retirement pair, cut the day the first 12:45Z fire is read and applied within one trading day. Rollback: terraform apply -target the same rule with cron(0 6 * * ? *) from 98d6e00ba5~1.
**Authored by:** 2.0.0_SA_COO~G1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 48.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | rollback state read live: the runner rule's ScheduleExpression/State/targets and the cot-bronze-complete rule's runner target | values printed from describe-rule and list-targets-by-rule | Read live 2026-10-11T13:4xZ: rule cot-rebalancer-runner-daily ScheduleExpression cron(0 6 * * ? *) ENABLED, one target cot-rebalancer-runner-daily input {mode:pull}; rule cot-bronze-complete targets CotSilverOnBronzeComplete (cot-bd-session-trigger, {mode:silver-run}) and cot-rebalancer-runner-reattempt (cot-rebalancer-runner, {mode:pull}). Today's sentinel bronze/2026-10-11/_BRONZE_COMPLETE.json LastModified 11:31:48Z invoked the runner 11:31:49Z -> SKIP-IDEMPOTENT. Rollback = cron(0 6 * * ? *) from 98d6e00ba5~1. | CLOSED 20261011T134052Z |
| L2 | activation | Terraform opal-assets safe-apply -target aws_cloudwatch_event_rule.cot_rebalancer_runner_daily, saved plan | plan reads exactly 1 changed in place, only schedule_expression; apply result | safe-apply -chdir=infra/aws/terraform/opal-assets apply of a saved plan, -target aws_cloudwatch_event_rule.cot_rebalancer_runner_daily. Plan read 'Plan: 0 to add, 1 to change, 0 to destroy', the one rule updated in place, schedule_expression cron(0 6 * * ? *) -> cron(45 12 * * ? *), nothing else. Apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' 2026-10-11T13:41Z; tombstone gate CLEAN (0 creates vs 7); tag-authz gate SKIPPED (no default_tags block in the root). seat-gates in mode WARN printed APPLY-WHO verdict=REFUSED ('a COO does not apply') and CROSSBOX-DEPLOY verdict=STOP (open deploy adhoc-partner-roster-t1, CloudOps~DELL1, names the root): WARN mode proceeded; both are filed as a surprise row. Bytes: merged 98d6e00ba5 via 672800c42a, CTO half @0c9f67d92d. | CLOSED 20261011T134200Z |
| L3 | verify | describe-rule cot-rebalancer-runner-daily reads cron(45 12 * * ? *) ENABLED; targets, permissions and the sentinel target unchanged | values printed from live reads | Read live 2026-10-11T13:41Z after the apply: describe-rule cot-rebalancer-runner-daily ScheduleExpression cron(45 12 * * ? *) ENABLED, one target cot-rebalancer-runner-daily input {mode:pull} (unchanged); rule cot-bronze-complete targets CotSilverOnBronzeComplete {mode:silver-run} and cot-rebalancer-runner-reattempt {mode:pull} (unchanged). Today (2026-10-11) is already stamped (06:01:00Z), so the first exercised day is 2026-10-12. EXPECTED, named in the CTO half: the 07:00Z cot-satellites-registry-producer-daily rule fails 3 attempts per day (~07:00-07:03Z) from 2026-10-12 until its retirement pair. | CLOSED 20261011T134200Z |
| L4 | verify | first exercised UTC day (2026-10-12): no runner invocation at 06:00Z; the sentinel invocation ~11:32Z pulls (REPORT, not SKIP-IDEMPOTENT) and the stamp lands; silver REPORT within 5 min; result COMPLETE; 12:45Z fire SKIP-IDEMPOTENT; 07:00Z rule 3 failed attempts (expected); 13:15Z serves registry as_of the date; 13:25Z holdings_as_of == as_of | CloudWatch excerpts, head-object, S3 versions |  | OPEN |

## Log

- 20261011T133931Z OPENED by 2.0.0_SA_COO~G1 with 4 leg(s)
- 20261011T134052Z LEG L1 closed: Read live 2026-10-11T13:4xZ: rule cot-rebalancer-runner-daily ScheduleExpression cron(0 6 * * ? *) ENABLED, one target c
- 20261011T134200Z LEG L2 closed: safe-apply -chdir=infra/aws/terraform/opal-assets apply of a saved plan, -target aws_cloudwatch_event_rule.cot_rebalance
- 20261011T134200Z LEG L3 closed: Read live 2026-10-11T13:41Z after the apply: describe-rule cot-rebalancer-runner-daily ScheduleExpression cron(45 12 * *
