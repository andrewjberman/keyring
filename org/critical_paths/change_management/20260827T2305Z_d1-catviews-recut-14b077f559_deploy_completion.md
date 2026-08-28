# Deploy Completion Record
**Date opened:** 2026-08-27T23:05:44.745312+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / mdpf-scheduled-floor cron(30 13 * * ? *) UTC -> mdpf-gold-lambda: the 2026-08-28 13:30Z fire. TP1AE-AC1 scores on the SCHEDULED fire ONLY -- an ad-hoc run writes a real artifact at the real key and destroys the time-of-day discriminator. RE-READ 2026-08-28T01:2xZ by 0.7.0_AE_CloudOps~Z: gate UNCHANGED and NOT yet fired. Re-formed from --reread-date to --reread-event: the dependency is an EVENT (a cron fire), and a date-gated hold on an event-shaped gate surfaces as PAST-REREAD while nothing has been neglected. (held since 2026-08-27T23:12:15.302967+00:00)
**Deploy:** D1_CATVIEWS.TO-P1-AE: cited-literal re-cut of mdpf-gold-lambda at pin 14b077f559 (emit path + post-20:5xZ SMA_BUCKETS) so the 13:30Z scheduled floor emits category-views
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| artifact-upload | s3-prefix | s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip | new VersionId + content-sha256 metadata == local zip sha256 | VersionId 2hwZEYAHvPRLw3C5y6xBqHPrWqvXWqmv, ContentLength 804455, metadata content-sha256=5fca0b5d24591b55b95818657ba2d283fba7569f66ebfd248daddd50c6c4037c == local zip sha256 (read-back, not rc) | CLOSED 20260827T231154Z |
| deployed-bytes | verify | mdpf-gold-lambda | downloaded members carry _shape_category_views + SMA_BUCKETS; CodeSha256 changed from 57V6D/ZNiAGSKBe2UkJ33aevjHDCLj0HNRphN//+iKg= | re-downloaded deployed zip: CodeSha256 X8oLXSRZG1W5WBhle6LSg/unVp9m6/0kja3dUMbEA3w= (was 57V6D/ZNiAGSKBe2UkJ33aevjHDCLj0HNRphN//+iKg=); registry SMA_BUCKETS+build_category_views PRESENT; consolidator _shape_category_views+category-views+import PRESENT | CLOSED 20260827T231155Z |
| zero-diff | verify | terraform mdpf-pipeline | post-apply replan -detailed-exitcode rc=0 | targeted replan -detailed-exitcode rc=0, No changes | CLOSED 20260827T231155Z |
| scheduled-emit | verify | portal/gold/mdpf/*/category-views/ | AC1: artifact present after the 2026-08-28 13:30Z mdpf-scheduled-floor fire, key+bucket+size+LastModified(s3api UTC) |  | OPEN |
| mdpf-gold-lambda | tf-lambda | aws_lambda_function.mdpf_gold | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply -target=aws_lambda_function.mdpf_gold: Apply complete 0 added 1 changed 0 destroyed, rc=0 | CLOSED 20260827T231155Z |

## Log

- 20260827T230544Z OPENED by 0.7.0_AE_CloudOps~Z with 5 leg(s)
- 20260827T231154Z LEG artifact-upload closed: VersionId 2hwZEYAHvPRLw3C5y6xBqHPrWqvXWqmv, ContentLength 804455, metadata content-sha256=5fca0b5d24591b55b95818657ba2d2
- 20260827T231155Z LEG mdpf-gold-lambda closed: safe-apply -target=aws_lambda_function.mdpf_gold: Apply complete 0 added 1 changed 0 destroyed, rc=0
- 20260827T231155Z LEG deployed-bytes closed: re-downloaded deployed zip: CodeSha256 X8oLXSRZG1W5WBhle6LSg/unVp9m6/0kja3dUMbEA3w= (was 57V6D/ZNiAGSKBe2UkJ33aevjHDCLj0
- 20260827T231155Z LEG zero-diff closed: targeted replan -detailed-exitcode rc=0, No changes
- 20260827T231215Z HELD-SOVEREIGN-GATED gate=external/mdpf-scheduled-floor cron(30 13 * * ? *) UTC -> mdpf-gold-lambda: TP1AE-AC1 scor
- 20260828T012320Z HELD-SOVEREIGN-GATED gate=external/mdpf-scheduled-floor cron(30 13 * * ? *) UTC -> mdpf-gold-lambda: the 2026-08-28
