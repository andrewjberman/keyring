# work 0534Z — AE 0.7~A: GO fired → combined-apply landed → deploy-mismatch CAUGHT (blocked Stage 2)

**Serial:** 0.7.0_AE_CloudOps~A
**Commit:** cb07bb8a8 (env-fix, prior) + tag imo-pipeline-v0.7.0
**Status:** combined-apply DONE; Stage 2 BLOCKED on deploy-mismatch

## RATIFY-GREEN received (COO 0518Z)
All W1-axis gates cleared: v0.7.3 PRD 8d08c7564 + DS~B 0e53822a4 dual-bar PASS + DS~A .035 discrimination_pass (fp 0.0/precision 1.0) + CVO re-verify 9bfcf1a2a. COO: FIRE.

## Executed (clean)
1. `.tools/safe-apply.sh apply` — 3-Lambda combined apply, 0 add/3 change/0 destroy, HALT-gate passed
2. Deployed env VERIFIED: score-web FIND_INSURE_TAXONOMY_VERSION=v3 + SCORING_WEIGHTS_VERSION=v0.3 (cb07bb8a8 pin-fix confirmed live)
3. 0-diff verified
4. tag imo-pipeline-v0.7.0 pushed (latest was v0.6.3; COO's v0.4.1 was stale)
5. Stage-1 10-IMO silver+gold re-fire (SKIP_BRONZE — re-score validated bronze; fixed my wrapper's absolute-path file:// bug → relative paths, 10/10 silver + 10/10 gold StatusCode 202)

## DEPLOY-MISMATCH CAUGHT (§6 trigger — refire validation)
Deployed scores (fresh 05:31Z, taxonomy_version=v3) but:
- am_prominence=None, wm_classification=None (v0.7.3 PRIMARY fields ABSENT)
- american-equity rollup_score=91 (the v0.7.1 FP-regression value; v0.7.3 should drop it via am_prominence≈0.03→absent)

Deployed score-web runs OLD scoring logic despite taxonomy_version=v3 (env loads v3 taxonomy, but code is pre-am_prominence).

## Root cause
All 3 imo Lambda zips (`s3://opal-...-lambda-artifacts/imo-pipeline/`) are **2026-05-27 21:25-26Z** — pre-v0.7.3/v0.3.1/.026. yang-lambda `artifact_key` = pre-built S3 zip; terraform apply only re-points, does NOT build from source. The zip-build from 0e53822a4 → S3 was NEVER run this cascade. On-disk source IS v0.7.3 (38 am_prominence refs); deployed artifact is not.

Canonical `build-and-upload.sh` has NO imo-pipeline support (pipeline list excludes it; builds from infra/aws/lambda/v2_portal/, not data/find/imo/scripts/). source-map has no find-insure top-level entries. imo packaging is bespoke — unknown to me.

## BLOCKED-ASK fired
- COO `053821Z` [BLOCKED-ASK] — operational: need canonical imo zip-build path + ownership
- AE 0.7~B `053840Z` [PEER-ASK] — they deploy imo Lambdas; asked for the build command they used for the 21:26Z zips
- Holding dispatch_stage2 (no 99-IMO burn on stale code)

## The gate worked
The refire-before-Stage-2 step (COO §2 step-5 + §6) caught a deploy-vs-committed mismatch BEFORE the universe burn. 0 IMOs wasted. This is precisely why the two-stage discipline + the deployed-score re-validation exist.

## On unblock (zip-build path received)
rebuild 3 zips from v0.7.3 source → re-apply (re-point at fresh zips) → re-fire silver+gold → re-grade (expect am_prominence present + dual-bar holds on DEPLOYED scores) → ratify-report → dispatch_stage2 99-IMO. ~5min once zips rebuilt.

## Memory banked
feedback_lambda_env_version_pin_overrides_code_default (env-pin trap). Candidate v2: artifact_key pre-built-zip model means terraform apply ≠ code deploy — verify the ARTIFACT was rebuilt from committed source, not just that TF re-points (this mismatch). Will bank if pattern recurs.

## Files touched
- infra/aws/terraform/imo-pipeline/phase1-score-web-lambda.tf (env fix, committed cb07bb8a8 prior)
- .runtmp/find-insure-stage1/refire_and_regrade_stage1.sh (SKIP_BRONZE guard added)
- this log
