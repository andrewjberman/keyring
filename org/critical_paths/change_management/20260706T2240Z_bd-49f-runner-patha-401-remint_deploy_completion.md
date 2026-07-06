# Deploy Completion Record
**Date opened:** 2026-07-06T22:40:57.158537+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260706T231356Z
**Deploy:** Path A (AUTHCHAIN-F3F6): bd-49f-runner re-mint bearer before declaring cookie-death -- fixes the 07-06 token-expiry->cookie-death misclassification (allocations 401 aborted 3/4). Authored 0.6.0 (18c10c853), CTO formal-gate PASS 223559Z, 0.7.0~A TF-deploy. -target-scoped (holds out bd-49f-interim.tf:52 SNS-sub drift).
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD 18c10c853 (code, 0.6.0) + source-map commit + bd-v2.49.0 tag pushed origin/CLOUD | hashes + tag pushed | code 18c10c853(0.6.0) + source-map fc96f6888 + fix 5ac7e39f2-followup + record; annotated tag bd-v2.49.0 pushed origin/CLOUD (@fc96f6888) | CLOSED 20260706T225415Z |
| L2 | activation | safe-apply -target=module.bd_49f_runner.aws_lambda_function.this (HALT-gated) | Apply complete 0 add 1 change 0 destroy | safe-apply HALTGT-passed -target=module.bd_49f_runner.aws_lambda_function.this: Apply complete! 0 added, 1 changed, 0 destroyed | CLOSED 20260706T225417Z |
| L3 | verify | live get-function-configuration source_code_hash == /GIzEjcrEEatKMFa81otWukyZTHHpjAnHTgkFhNDGco= + targeted 0-diff re-plan | live hash match + No changes | live get-function-configuration CodeSha256=/GIzEjcrEEatKMFa81otWukyZTHHpjAnHTgkFhNDGco= (LastModified 22:45:47Z); targeted re-plan 'No changes.' NOTE: apply STRIPPED reserved-concurrency=3 (unmanaged-attr reset) -> re-put=3 restored; codify-in-TF now urgent | CLOSED 20260706T225419Z |
| L4 | verify | exercise-verify (AUTHCHAIN-F3F6 close): ASYNC Event-invoke force=true run self-completes despite the ~85MB sweep + emits bronze sentinel (proves re-mint recovers a bearer lapse, no 3/4 abort) | async run RESULT + _BRONZE_COMPLETE.json emitted | exercise-verify PASS: async Event force=true run (RequestId 8dfc2c1d, SINGLE run, no storm) -- RESULT landed=[all 4], pulled=[all 4], failed=[], auth_dead=False; bronze sentinel refreshed 23:05:31 GMT; self-completed ~9min through the ~85MB sweep. Definitive all-4 fresh-pull + no 3/4-abort regression. | CLOSED 20260706T231324Z |

## Log

- 20260706T224057Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
- 20260706T225415Z LEG L1 closed: code 18c10c853(0.6.0) + source-map fc96f6888 + fix 5ac7e39f2-followup + record; annotated tag bd-v2.49.0 pushed origin/C
- 20260706T225417Z LEG L2 closed: safe-apply HALTGT-passed -target=module.bd_49f_runner.aws_lambda_function.this: Apply complete! 0 added, 1 changed, 0 de
- 20260706T225419Z LEG L3 closed: live get-function-configuration CodeSha256=/GIzEjcrEEatKMFa81otWukyZTHHpjAnHTgkFhNDGco= (LastModified 22:45:47Z); target
- 20260706T231324Z LEG L4 closed: exercise-verify PASS: async Event force=true run (RequestId 8dfc2c1d, SINGLE run, no storm) -- RESULT landed=[all 4], pu
- 20260706T231356Z CLOSED -- all 4 legs proven
