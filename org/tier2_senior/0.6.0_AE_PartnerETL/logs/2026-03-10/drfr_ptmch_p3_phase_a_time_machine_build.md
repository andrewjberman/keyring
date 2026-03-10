# DRFR_PTMCH P3 Phase A — bd-time-machine Build — 0.6.0_AE_PartnerETL

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
| 13 | Commit all Phase A artifacts | `feat(bd-pipeline): DRFR_PTMCH P3 Phase A — bd-time-machine source + Terraform` |

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

**Status:** IN PROGRESS (Phase A complete — Phase B gated on CloudOps P1)
**Active branch:** `CLOUD`

All Phase A code is written and committed.  `bd-capture-output-versions` and
`bd-time-machine` Lambda source exists at `infra/aws/lambda/bd-pipeline/`.
Terraform modules, IAM roles, and source-map entries are in place with null
deploy fields (not yet built/uploaded). `bd-portal-publisher` has the capture
fan-out wired and env var added to its Terraform module. Findings doc confirms
earliest restorable BD date is 2026-02-25.  `terraform plan` not yet run —
Phase B (build + upload + plan + apply + tag) is blocked until CloudOps P1
confirms lifecycle rules deployed and findings doc written.

---

## Next Steps

1. **[0.7.0_AE_CloudOps] Complete DRFR_PTMCH.P1** — lifecycle rules on
   `opal-data-bd` + IAM gap analysis + CloudFront path table. This unblocks deploy.

2. **[0.6.0_AE_PartnerETL] Phase B on CloudOps P1 signal** — when P1 is complete:
   - Review CloudOps P1 findings doc (CloudFront path table — confirm
     `/api/scoped/advisor-intelligence/*` is correct scope or update)
   - `build-and-upload.sh` for three functions: `bd-capture-output-versions`,
     `bd-time-machine`, `bd-portal-publisher`
   - Update source-map sha256 fields for all three
   - `terraform plan` (expect: 2 new Lambdas + IAM roles + updated publisher module)
   - `terraform apply` → 0-diff → update `pipeline_inventory.xml` →
     `record-terraform-deploy.sh` → tag `bd-v2.18.0` → push

3. **[0.6.0_AE_PartnerETL] Post-deploy acceptance check:**
   - Trigger a gold pipeline run — verify `bd-capture-output-versions` fires and
     writes a manifest to `s3://opal-data-bd/snapshots/manifests/`
   - Invoke `bd-time-machine` with `target_date=2026-03-06` — verify files
     restored, sentinel written, publisher re-triggered, CF invalidation fires

**Files to touch next:**
- `infra/aws/terraform/bd-pipeline/iam.tf` — review against CloudOps P1 IAM findings
  (may need to adjust permission scope once full table is available)
- All three Lambda source dirs for `build-and-upload.sh` — no changes needed,
  just build and upload

**Do NOT:**
- Run `terraform apply` before CloudOps P1 lifecycle rules are on `opal-data-bd`
- Add a second entry to `aws_s3_bucket_notification.bd_data_bucket` for
  `pipeline-complete.json` — the S3 filter constraint is permanent
- Tag `bd-v2.18.0` until 0-diff is confirmed after apply
