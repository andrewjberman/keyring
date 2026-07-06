# Deploy Completion Record
**Date opened:** 2026-07-06T22:40:57.158537+00:00
**Status:** OPEN
**Deploy:** Path A (AUTHCHAIN-F3F6): bd-49f-runner re-mint bearer before declaring cookie-death -- fixes the 07-06 token-expiry->cookie-death misclassification (allocations 401 aborted 3/4). Authored 0.6.0 (18c10c853), CTO formal-gate PASS 223559Z, 0.7.0~A TF-deploy. -target-scoped (holds out bd-49f-interim.tf:52 SNS-sub drift).
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD 18c10c853 (code, 0.6.0) + source-map commit + bd-v2.49.0 tag pushed origin/CLOUD | hashes + tag pushed |  | OPEN |
| L2 | activation | safe-apply -target=module.bd_49f_runner.aws_lambda_function.this (HALT-gated) | Apply complete 0 add 1 change 0 destroy |  | OPEN |
| L3 | verify | live get-function-configuration source_code_hash == /GIzEjcrEEatKMFa81otWukyZTHHpjAnHTgkFhNDGco= + targeted 0-diff re-plan | live hash match + No changes |  | OPEN |
| L4 | verify | exercise-verify (AUTHCHAIN-F3F6 close): ASYNC Event-invoke force=true run self-completes despite the ~85MB sweep + emits bronze sentinel (proves re-mint recovers a bearer lapse, no 3/4 abort) | async run RESULT + _BRONZE_COMPLETE.json emitted |  | OPEN |

## Log

- 20260706T224057Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
