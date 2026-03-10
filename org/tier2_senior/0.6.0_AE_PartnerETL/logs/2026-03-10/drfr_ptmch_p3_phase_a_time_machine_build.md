# DRFR_PTMCH P3 — bd-time-machine Full Deploy (Phase A + B) — 0.6.0_AE_PartnerETL

**Date:** 2026-03-10
**Start Time:** 19:30
**End Time:** 20:30

## Objective

Build Phase A of the Portal Time Machine BD layer (DRFR_PTMCH.P3): write
`bd-capture-output-versions` and `bd-time-machine` Lambda source, add them to
Terraform, wire the publisher fan-out, and produce the findings doc.  Terraform
apply is gated on CloudOps P1 completing lifecycle rules + IAM gaps.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Review task order + infrastructure | Identified trigger architecture mismatch (S3 constraint); task order updated by Andrew |
| 2 | Write bd-capture-output-versions Lambda | `infra/aws/lambda/bd-pipeline/bd-capture-output-versions/lambda_function.py` |
| 3 | Write bd-time-machine Lambda | `infra/aws/lambda/bd-pipeline/bd-time-machine/lambda_function.py` |
| 4 | Add capture fan-out to bd-portal-publisher | After Step 3 completes (all writes done) — Lambda async, not S3 event |
| 5 | Add `CAPTURE_VERSIONS_FUNCTION` env var to publisher TF module | `lambdas.tf` |
| 6 | Add two new Lambda modules to lambdas.tf | `bd-capture-output-versions` (256MB/120s), `bd-time-machine` (256MB/300s) |
| 7 | Add two new IAM roles to iam.tf | `bd-capture-versions-lambda-role`, `bd-time-machine-lambda-role` |
| 8 | Extend `bd_gold_layer_invoke` policy | Added `bd-capture-output-versions` to Resource list; renamed policy `invoke-publisher-fanout` |
| 9 | Update s3-notifications.tf comment | Documents three-way fan-out chain |
| 10 | Add source-map entries (null sha256/deploy fields) | `lambda-source-map.json` |
| 11 | Run Req 4 CLI (earliest version date) | Earliest: `2026-02-25T22:02:47Z` (gPL4d7HpRQWoJJe2ZsdOH4YFahMGHbAF) |
| 12 | Write findings doc | `deliverables/DRFR_PTMCH.001.bd-pipeline-findings.md` |
| 13 | Commit all Phase A artifacts | `b3207410` feat(bd-pipeline): DRFR_PTMCH P3 Phase A |
| 14 | Check AE5 log (OpalETL P2 complete) | No dependency conflict. Build workaround noted: build-and-upload.sh fails on bun/MSYS2 /tmp/ paths — use PowerShell PS1 temp files |
| 15 | Pull AE5 commits (yang-v2.2.0, data-refresh-v2.1.0) | lambda-source-map.json merged cleanly; bd entries intact |
| 16 | Build bd-capture-output-versions via PowerShell PS1 | SHA256: `xy+x9MfurPBihkv5Y6Wd09Y/s10fxUMy3uEwvmYqKio=` |
| 17 | Build bd-time-machine via PowerShell PS1 | SHA256: `9zdaFi8Jt15R0PWY98IhKUth554ohrIW9mKWzOeUZms=` |
| 18 | Build bd-portal-publisher via PowerShell PS1 | SHA256: `+bk/8HN0o4CX51J5bae0E0oSuU2CGWl5HnkWQWdjnC0=` |
| 19 | Update source map SHA256 | `9fcb0216` ci: upload artifacts [skip ci] |
| 20 | terraform init (new modules) | OK |
| 21 | terraform plan | 12 to add, 1 to change, 1 to destroy (IAM policy rename) |
| 22 | terraform apply | 12 added, 1 changed, 1 destroyed |
| 23 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 24 | Update pipeline_inventory.xml | bd-v2.18.0, two new Lambda entries, publisher env var updated |
| 25 | record-terraform-deploy.sh | `e85702a1` ci: record deploy bd-pipeline @ 9fcb0216 [skip ci] |
| 26 | Commit pipeline_inventory.xml | `3f175089` |
| 27 | Mark task order complete + commit | `69bd6906` |
| 28 | Tag bd-v2.18.0 + push --follow-tags | Pushed to origin/CLOUD |

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Capture fan-out fires AFTER publisher writes (not at start) | Manifest must reflect versions that were just written, not prior versions |
| Lambda-to-Lambda for capture (not S3 notification) | S3 cannot have two notification rules with same prefix+suffix filter — established constraint in s3-notifications.tf |
| Dedicated IAM roles (Option A confirmed) | `bd-capture-versions-lambda-role` + `bd-time-machine-lambda-role`. Shared publisher role (`bd-gold-layer-lambda-role`) only gets lambda:InvokeFunction extension |
| Sentinel excludes pipeline-complete.json from CopyObject loop | Writing sentinel AFTER restoring all other keys fires the S3 event trigger exactly once cleanly |
| CF invalidation non-fatal | Restored data is correct even if invalidation fails; portal serves stale until TTL expiry (s-maxage=3600) |
| Python 3.12 for new Lambdas | Existing BD Lambdas use 3.11; 3.12 matches yang time-machine precedent. No layer dependency — only boto3 (bundled in Lambda runtime) |
| Fallback path uses list_object_versions | For dates before first bd-capture-output-versions run; O(n keys * API calls) but correct. 300s timeout sufficient for ~100 keys |
| ET cutoff = 22:00 UTC conservative (EST) | Avoids restoring partial rebuild that completed after 5 PM ET; slightly conservative on EDT dates (21:00 would be exact) |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/bd-pipeline/bd-capture-output-versions/lambda_function.py` | New Lambda — manifest writer | Yes — see commit below |
| `infra/aws/lambda/bd-pipeline/bd-time-machine/lambda_function.py` | New Lambda — version restore + sentinel + CF invalidation | Yes |
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | Added capture fan-out (22 lines) after Step 3 completes | Yes |
| `infra/aws/terraform/bd-pipeline/lambdas.tf` | Two new modules + CAPTURE_VERSIONS_FUNCTION env var to publisher | Yes |
| `infra/aws/terraform/bd-pipeline/iam.tf` | Two new IAM roles; extended bd_gold_layer_invoke to include capture fn | Yes |
| `infra/aws/terraform/bd-pipeline/s3-notifications.tf` | Updated comment to document three-way fan-out | Yes |
| `infra/aws/lambda/ci/lambda-source-map.json` | Added bd-capture-output-versions + bd-time-machine entries (null sha256) | Yes |
| `org/tier2_senior/0.6.0_AE_PartnerETL/deliverables/DRFR_PTMCH.001.bd-pipeline-findings.md` | New findings doc — versioning confirmed, earliest date, publisher analysis | Yes |

---

## Blockers

BLOCKED on `0.7.0_AE_CloudOps` DRFR_PTMCH.P1 — lifecycle rules on `opal-data-bd`
+ IAM gap closure must be complete before Phase B deploy.
Evidence: DRFR_PTMCH.P1 task order status = pending as of 2026-03-10.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`
**Tag:** `bd-v2.18.0`

DRFR_PTMCH.P3 is fully deployed. `bd-capture-output-versions` and `bd-time-machine`
are live in AWS at bd-v2.18.0. `bd-portal-publisher` is updated with the capture
fan-out. All IAM roles created, Terraform 0-diff confirmed, tag pushed to origin.
On the next BD gold pipeline run, `bd-capture-output-versions` will fire automatically
and write the first manifest to `s3://opal-data-bd/snapshots/manifests/`.
`bd-time-machine` can be invoked directly with `{"target_date": "YYYY-MM-DD"}` for any
date on or after 2026-02-25 (earliest available S3 version).

---

## Next Steps

1. **Verify first manifest** — after next nightly gold run (23:00 UTC tonight),
   confirm `bd-capture-output-versions` fired and wrote to `s3://opal-data-bd/snapshots/manifests/`.
   Command: `aws s3 ls s3://opal-data-bd/snapshots/manifests/`
   Verify manifest contains non-null versionIds for all gold/ files.

2. **Acceptance test bd-time-machine** — invoke with a historical date:
   `aws lambda invoke --function-name bd-time-machine --payload '{"target_date":"2026-03-06"}' out.json`
   Verify: `files_restored > 0`, sentinel written, CF invalidation id in response,
   portal shows 2026-03-06 data after publisher re-runs.

**Do NOT:**
- Add a second S3 notification rule on `pipeline-complete.json` — S3 filter constraint is permanent
- Inline Python or shell in SSM commands — EC2 code always goes through S3
