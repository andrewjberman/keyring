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
| L1 | verify | rollback state read live: rules on the function, the 07:00Z rule's schedule/target, the lambda policy statements | values printed from list-rule-names-by-target, describe-rule, list-targets-by-rule, get-policy |  | OPEN |
| L2 | activation | Terraform cot-pipeline safe-apply -target the rule, target and permission of the daily rule, saved plan | plan reads exactly 0 add 0 change 3 destroy on those three addresses; apply result |  | OPEN |
| L3 | verify | list-rule-names-by-target reads the stamp-gated rule only; describe-rule on the daily rule reads ResourceNotFound; lambda policy carries only the StampGated statement | values printed from live reads |  | OPEN |
| L4 | verify | first 07:00Z after the apply (2026-10-13 07:00Z): zero invocations in the log group; the 13:15Z fire unchanged (as_of that date, rc 0) | CloudWatch excerpt and head-object |  | OPEN |

## Log

- 20261012T134143Z OPENED by 2.0.0_SA_COO~G1 with 4 leg(s)
