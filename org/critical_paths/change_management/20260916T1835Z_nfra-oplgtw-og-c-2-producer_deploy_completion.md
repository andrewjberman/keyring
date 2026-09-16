# Deploy Completion Record
**Date opened:** 2026-09-16T18:35:51.935034+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260916T185151Z
**Deploy:** NFRA_OPLGTW OG-c-2: opal-assets-silver-schwab producer deploy (build 1f03a3f209) -- DEPLOY leg only; replay HELD, opens its own entry when released
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | opal-assets-silver-schwab CodeSha256 + OPAL_BUILD_COMMIT + post-apply plan | live CodeSha256 == built zip SHA256, env 1f03a3f209, 0-diff plan | live CodeSha256 v2BztqbuhHD3gH95eMqCQzkjPEotvSoeIezEOfsxu90= == built zip SHA256 (deploy/build.log); OPAL_BUILD_COMMIT 1f03a3f209; State Active/Successful; post-apply plan 'No changes.' rc=0 (deploy/plan_post_apply.log) | CLOSED 20260916T185151Z |
| opal-assets-silver-schwab | tf-lambda | module.silver_converter["schwab"].aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply rc=0 2026-09-16T18:49:35Z 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' (deploy/apply.log); live LastModified 2026-09-16T18:49:30Z, s3_object_version 7Db1UfM3EU_Z6q4cLQiV4wM3bYaAaFMF | CLOSED 20260916T185151Z |

## Log

- 20260916T183551Z OPENED by 0.9.0_WK_NFRA_OPLGTW~4 with 2 leg(s)
- 20260916T185151Z LEG opal-assets-silver-schwab closed: safe-apply rc=0 2026-09-16T18:49:35Z 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' (deploy/apply.log); l
- 20260916T185151Z LEG V1 closed: live CodeSha256 v2BztqbuhHD3gH95eMqCQzkjPEotvSoeIezEOfsxu90= == built zip SHA256 (deploy/build.log); OPAL_BUILD_COMMIT 1
- 20260916T185151Z CLOSED -- all 2 legs proven
