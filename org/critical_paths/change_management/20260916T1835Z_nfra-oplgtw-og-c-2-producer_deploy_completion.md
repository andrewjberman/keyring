# Deploy Completion Record
**Date opened:** 2026-09-16T18:35:51.935034+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-c-2: opal-assets-silver-schwab producer deploy (build 1f03a3f209) -- DEPLOY leg only; replay HELD, opens its own entry when released
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | opal-assets-silver-schwab CodeSha256 + OPAL_BUILD_COMMIT + post-apply plan | live CodeSha256 == built zip SHA256, env 1f03a3f209, 0-diff plan |  | OPEN |
| opal-assets-silver-schwab | tf-lambda | module.silver_converter["schwab"].aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260916T183551Z OPENED by 0.9.0_WK_NFRA_OPLGTW~4 with 2 leg(s)
