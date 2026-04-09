# Session Log: keyword-intelligence-generator model upgrade deploy

**Agent:** 0.1.0_DT_MarketIntelligence
**Date:** 2026-04-07
**GO from:** 1.0.0_SA_CTO
**Project:** news-pipeline

## Summary

Deployed keyword-intelligence-generator Lambda with model upgrade from gpt-4o-mini
to gpt-5.4 for both the main analysis call and synthesis call. Query gen + web
search calls remain on gpt-4o-mini as directed by CTO GO message.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit code change | `14b1e8d0` keyword-intelligence-generator model upgrade gpt-4o-mini -> gpt-5.4 |
| 2 | Build zip from lambda_deployment.zip | Extracted existing 8MB vendored zip, replaced lambda_function.py, re-zipped |
| 3 | Upload to S3 (first attempt) | Missing content-sha256 metadata -- terraform plan failed with Invalid index |
| 4 | Re-upload with metadata | SHA256: `TOkFOGIp7B//t5ximkpN4BnFzkr7ufVFayuZ8GPEo8c=` |
| 5 | Commit source map | `4d4552e6` ci: upload keyword-intelligence-generator artifact |
| 6 | terraform plan | 1 change (keyword_intelligence_generator source_code_hash update) |
| 7 | terraform apply | 0 added, 1 changed, 0 destroyed |
| 8 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 9 | record-terraform-deploy.sh | `650b7302` ci: record deploy news-pipeline @ 571d22d3 |
| 10 | Tag + push | `news-v2.7.6` pushed to CLOUD |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| news-pipeline | `news-v2.7.6` | `650b7302` |

## Verification

1. **CloudWatch:** Most recent pre-deploy invocation at 9:42 AM ET (pre-compute chain running).
2. **Manual invoke (post-deploy):** 200 OK, 244ms, 20/20 keywords skipped as existing (cached from 9:42 AM run).
3. **DynamoDB:** 177 items total, 20 for today (full paginated scan). Initial scan returned only 2 due to DynamoDB 1MB scan page limit -- paginated scan confirms all 20 written by morning run.
4. **No regressions:** No import errors, no runtime crashes. Clean deployment.

## Lessons Learned

1. **S3 metadata required for terraform.** The news-pipeline Terraform config uses
   `data.aws_s3_object.keyword_intelligence_artifact.metadata["content-sha256"]`
   for `source_code_hash`. Plain `aws s3 cp` without `--metadata` produces an empty
   metadata map, causing terraform plan to fail with "Invalid index". Must upload with
   `--metadata "content-sha256=<base64sha256>"`.

2. **lambda_deployment.zip is the canonical build artifact.** The `_build_tmp/` directory
   referenced in the source map note does not exist locally. The 8MB `lambda_deployment.zip`
   in the source dir IS the vendored package. Extract, swap lambda_function.py, re-zip.

## Current State

- keyword-intelligence-generator deployed with gpt-5.4 model
- Pre-compute chain operational (2x daily via EventBridge)
- gpt-5.4 calls will fire on next run with uncached keywords (tomorrow's fresh TopicCloud)
- Portal modal test pending (CTO to verify latency drop)

## Next Steps

- [CTO] Verify portal modal latency after next fresh keyword run
- [CTO] Confirm gpt-5.4 OPENAI_USAGE lines in CloudWatch after next run
- Monitor for any cost/quality changes from model upgrade
