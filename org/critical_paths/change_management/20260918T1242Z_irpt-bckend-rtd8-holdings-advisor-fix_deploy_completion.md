# Deploy Completion Record
**Date opened:** 2026-09-18T12:42:29.561419+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtd-8: the firm check restored on holdings/enforce.py -- row W1-S16 fix (re-staged enforce.py member only)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L2 | verify | live route proof (M of M guarded routes, other-firm advisor refused / own-firm admitted) | the round-1 harness (real signed post-authorizer requests) output |  | OPEN |
| irpt-holdings | tf-lambda | module.irpt_holdings.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260918T124229Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 2 leg(s)
