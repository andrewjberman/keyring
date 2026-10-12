# Deploy Completion Record
**Date opened:** 2026-10-12T13:41:43.265136+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP R3 HG-t-15: retire the 07:00Z cot-satellites-registry-producer-daily rule, its target and its permission (3 destroys) via safe-apply -target. CTO half SIGNED @44e8559bca (ADDENDUM 6, msg 4366). Rollback: restore the three resource blocks from f3afa83d59 and apply the same targets; the rollback of HG-t-5 (rule back to cron(0 6)) now INCLUDES re-applying this rule from its prior tf.
**Authored by:** 2.0.0_SA_COO~G1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 48.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | rollback state read live: rules on the function, the 07:00Z rule's schedule/target, the lambda policy statements | values printed from list-rule-names-by-target, describe-rule, list-targets-by-rule, get-policy | Read live 2026-10-12T13:4xZ: rules on cot-satellites-registry-producer = [cot-satellites-registry-producer-daily, etfs-cot-satellites-registry-producer-stamp-gated-daily]; the daily rule cron(0 7 * * ? *) ENABLED with target CotSatellitesRegistryProducerDaily input null; lambda policy statements EventBridgeCotSatellitesRegistryProducerDaily and EventBridgeCotSatellitesRegistryProducerStampGated. Rollback = the three resource blocks at f3afa83d59, applied with the same three targets (and with the HG-t-5 rollback). | CLOSED 20261012T134222Z |
| L2 | activation | Terraform cot-pipeline safe-apply -target the rule, target and permission of the daily rule, saved plan | plan reads exactly 0 add 0 change 3 destroy on those three addresses; apply result | safe-apply -chdir=infra/aws/terraform/cot-pipeline apply of a saved plan, -target aws_cloudwatch_event_rule.cot_satellites_registry_producer_daily, aws_cloudwatch_event_target.cot_satellites_registry_producer_daily, aws_lambda_permission.events_cot_satellites_registry_producer. Plan read 'Plan: 0 to add, 0 to change, 3 to destroy', the three addresses only, each 'because ... is not in configuration'. Apply rc=0 'Apply complete! Resources: 0 added, 0 changed, 3 destroyed' 2026-10-12T13:44Z; tagauthz gate PASSED, tombstone gate CLEAN (0 creates vs 7). seat-gates in WARN again printed APPLY-WHO REFUSED (a COO does not apply) and CROSSBOX-DEPLOY STOP (an unreadable foreign worktree C:/dev/wk-firmbkts-35, ls-tree rc=128): row MDPF_HEALGAP-D1-S13 stands, no ruling on it yet. Bytes: fix 0ef23bcaf5 merged c866517296, CTO half @44e8559bca. | CLOSED 20261012T134503Z |
| L3 | verify | list-rule-names-by-target reads the stamp-gated rule only; describe-rule on the daily rule reads ResourceNotFound; lambda policy carries only the StampGated statement | values printed from live reads | Read live 2026-10-12T13:44Z after the apply: list-rule-names-by-target cot-satellites-registry-producer = [etfs-cot-satellites-registry-producer-stamp-gated-daily] only; describe-rule cot-satellites-registry-producer-daily -> ResourceNotFoundException (rule does not exist); the stamp-gated rule cron(15 13 * * ? *) ENABLED, target CotSatellitesRegistryProducerStampGated input {require_stamp:true}; lambda policy carries only EventBridgeCotSatellitesRegistryProducerStampGated. Served keys untouched by the act (written at 13:15Z). | CLOSED 20261012T134503Z |
| L4 | verify | first 07:00Z after the apply (2026-10-13 07:00Z): zero invocations in the log group; the 13:15Z fire unchanged (as_of that date, rc 0) | CloudWatch excerpt and head-object |  | OPEN |

## Log

- 20261012T134143Z OPENED by 2.0.0_SA_COO~G1 with 4 leg(s)
- 20261012T134222Z LEG L1 closed: Read live 2026-10-12T13:4xZ: rules on cot-satellites-registry-producer = [cot-satellites-registry-producer-daily, etfs-c
- 20261012T134503Z LEG L2 closed: safe-apply -chdir=infra/aws/terraform/cot-pipeline apply of a saved plan, -target aws_cloudwatch_event_rule.cot_satellit
- 20261012T134503Z LEG L3 closed: Read live 2026-10-12T13:44Z after the apply: list-rule-names-by-target cot-satellites-registry-producer = [etfs-cot-sate
