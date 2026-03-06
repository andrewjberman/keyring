# ADVI_49FNV3-F1: bd-portal-publisher Redeploy -- 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Project:** ADVI_49FNV3
**Fix:** F1 -- GRO mode growth_decomposition data unavailable
**Pipeline:** bd-pipeline
**Lambda:** bd-portal-publisher
**Tag:** bd-v2.16.4

---

## DS Finding (received)

- growth_decomposition code IS present in lambda_function.py (lines 707-732 computation,
  853-856 emission) -- added in Y5.
- Root cause: Lambda was deployed at bd-v2.16.2 but the S3 version that was active
  (IALmY4A6FffxCUKJ8H6RvWWIYTZgIXxr) predated or excluded the Y5 artifact. The
  `terraform apply` at bd-v2.16.2 time did not update the Lambda to the artifact
  containing Y5.
- No code change needed. Pure redeploy.
- DT brief: docs/briefs/devops-brief-49fnv3-f1-gro-publisher-fix.md

## Actions Taken

1. Gate check: `git status --porcelain infra/aws/lambda/bd-pipeline/bd-portal-publisher/`
   -- clean (source committed).

2. Build: `bash infra/aws/lambda/ci/build-and-upload.sh bd-pipeline bd-portal-publisher`
   - SHA256: `2WIGdQxTA+o9D6nluDJRXNDjLUSblRhNYhq4FVx3pVg=` (unchanged -- content correct)
   - New S3 version: `_Y2V0R.K.YRFRLlKzfkdjrm.YiXYJFLE`
   - Replaced stale version: `IALmY4A6FffxCUKJ8H6RvWWIYTZgIXxr`

3. Terraform plan: confirmed 1 change -- `s3_object_version` on `bd-portal-publisher`
   only. No other drift.

4. Terraform apply: `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`

5. 0-diff verified: `No changes. Your infrastructure matches the configuration.`

6. record-terraform-deploy.sh: updated source map + CHANGELOG.json, commit `f1b69995`

7. Tagged: `bd-v2.16.4` -- skipped bd-v2.16.3+1 -> .4 because .0-.3 were already
   taken. No bd-v2.16.3 existed for this deploy; kept within .16.x patch series since
   the code was already tagged at bd-v2.16.2 (just stale deploy).

8. Pushed CLOUD with --follow-tags.

9. Pipeline trigger: `aws lambda invoke --function-name bd-portal-publisher
   --invocation-type Event` -> 202 Accepted.

## Outcome

- Lambda is now on the artifact containing Y5 growth_decomposition.
- Lambda invoked; will write fresh timeseries_chart.json with `growth_decomposition.data`.
- Portal should show 3-line GRO chart (market/violet, NNA/blue, total/amber) after Lambda
  completes.

## Verification Required

After Lambda execution completes (~1-2 min):
1. Check S3: `gold/timeseries_chart.json` should contain `growth_decomposition.data`
   with at least 12 monthly entries.
2. Check portal: AdvisorIntelligence > Assets Overview > GRO toggle should show chart.

## Notes

- F2 (projected bars) was blocked on F1 per PRD -- F1 is now unblocked. RD can proceed
  with F2 ghost bar implementation.
- bd-v2.16.3 tag does not exist (was skipped in prior sequencing). Next version after
  this will be bd-v2.17.0 for any new feature work.
