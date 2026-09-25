# Deploy Completion Record
**Date opened:** 2026-08-25T09:39:57.086315+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260825T095533Z
**Deploy:** WSE_COTMDL.TO-R1-AE cot-rebalancer-runner MODEL_DETAIL_SCOPE opal_closure -> all (one TF env line, forward-only)
**Authored by:** 0.7.0_AE_CloudOps~H
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | cot_rebalancer_runner.tf:154 = "all" committed on CLOUD | commit hash in HEAD | cot_rebalancer_runner.tf:154 = "all" committed @27a3a98cdc on CLOUD by 0.7.0_AE_CloudOps~H via safe-commit.sh -F (msg-verify MATCH len=2367); one file, 1 insertion 1 deletion. Push state re-measured at close time, not assumed. | CLOSED 20260825T094100Z |
| L2 | activation | safe-apply opal-assets (env-var in-place update on cot-rebalancer-runner) | apply RC0 + N changed | safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply -target=module.cot_rebalancer_runner.aws_lambda_function.this -auto-approve, RC0. TARGETED per COO spec amendment @12caf0a92f (a blanket apply would have shipped 3 other lanes' committed-but-unapplied changes incl. an MDPF producer prefix cutover). HALTGT: identity fail-closed first (session .serial written, NOT overridden), then 7 routine pending msgs reviewed -- none STOP-class, none touching WSE_COTMDL -- HALT_ACK=1. | CLOSED 20260825T095304Z |
| L3 | verify | re-plan 0-diff AND Rule-22a APPLIED read | get-function-configuration MODEL_DETAIL_SCOPE=all on the live function (DESIRED 0-diff is NOT this) | APPLIED (Rule 22a, the layer that matters): aws lambda get-function-configuration cot-rebalancer-runner -> MODEL_DETAIL_SCOPE=all, LastModified 2026-08-25T09:50:45.000+0000; CodeSha256 eeeXhavS5IDFrBRh72TXH2RXPARsN4ZVtOx7Uzqhdmo= UNCHANGED across the apply (env-only, no code change, as intended). DESIRED re-plan per amended spec @12caf0a92f: 'Plan: 0 to add, 3 to change, 0 to destroy' -- 0-diff ON THE TARGETED RESOURCE; the 3 remaining are NAMED AND COUNTED and are NOT mine (aws_iam_role_policy.bd49f_reporting_io, aws_iam_role_policy.emitter, module.emitter.aws_lambda_function.this). Predicate audited: 14 raw cot_rebalancer_runner hits in the re-plan are ALL 'Refreshing state...' refresh-phase lines; change-bearing lines for my resource = ZERO. | CLOSED 20260825T095532Z |

## Log

- 20260825T093957Z OPENED by 0.7.0_AE_CloudOps~H with 3 leg(s)
- 20260825T094100Z LEG L1 closed: cot_rebalancer_runner.tf:154 = "all" committed @27a3a98cdc on CLOUD by 0.7.0_AE_CloudOps~H via safe-commit.sh -F (msg-ve
- 20260825T095304Z LEG L2 closed: safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply -target=module.cot_rebalancer_runner.aws_lambda_function.this
- 20260825T095532Z LEG L3 closed: APPLIED (Rule 22a, the layer that matters): aws lambda get-function-configuration cot-rebalancer-runner -> MODEL_DETAIL_
- 20260825T095533Z CLOSED -- all 3 legs proven
