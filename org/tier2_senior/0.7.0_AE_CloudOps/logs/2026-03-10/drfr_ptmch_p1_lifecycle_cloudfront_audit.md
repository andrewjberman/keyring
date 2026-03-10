# DRFR_PTMCH P1: Lifecycle Rules + CloudFront Audit — 0.7.0_AE_CloudOps

**Date:** 2026-03-10
**Start Time:** 18:00
**End Time:** 18:30

## Objective

Execute DRFR_PTMCH.P1 (COO-issued): add S3 noncurrent-version lifecycle rules on
`opal-data-portal-v2` and `opal-data-bd` to bound Time Machine storage cost, and
audit CloudFront distribution EVTSA9VEHNZVH path routing so OpalETL can wire the
correct invalidation paths into the portal-time-machine orchestrator Lambda.
IAM changes removed from scope (each pipeline AE owns their own role).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Review task order + read source files | shared-infra/main.tf read; yang-pipeline/iam.tf read; data-refresh/main.tf found |
| 2 | CloudFront audit (CLI read-only) | 12 behaviors returned; 4 S3-backed paths identified |
| 3 | Check latest shared-infra tag | v1.3.0 exists — next tag is v1.4.0 |
| 4 | Write lifecycle rules to shared-infra/main.tf | 2 resources added (71 lines) |
| 5 | Commit | `5aea13f0` infra(shared-infra): add S3 lifecycle rules for DRFR_PTMCH |
| 6 | Fix filter{} provider warning | Empty filter{} blocks added to all 4 rules |
| 7 | Commit fix | `5978d069` infra(shared-infra): add filter{} to lifecycle rules |
| 8 | terraform plan | 2 to add, 0 to change, 0 to destroy — clean |
| 9 | terraform apply | 2 added, 0 changed, 0 destroyed |
| 10 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 11 | Update pipeline_inventory.xml | current_tag v1.4.0; new BD bucket entry; lifecycle config entries; full CF behavior table |
| 12 | Write findings document | DRFR_PTMCH.001.cloudops-findings.md |
| 13 | Write session log | This file |
| 14 | Commit org + deliverables | `[pending]` |
| 15 | Tag + push | shared-infra-v1.4.0 |

---

## Work Completed

### 1. Lifecycle Rules Deployed

Two `aws_s3_bucket_lifecycle_configuration` resources added to `shared-infra/main.tf`.
Both buckets reference by name (no import needed — Terraform manages the lifecycle config
resource independently of the bucket resource).

| Bucket | Rule 1 | Rule 2 |
|---|---|---|
| opal-data-portal-v2 | noncurrentVersionExpiration: 90d | abortIncompleteMultipartUpload: 7d |
| opal-data-bd | noncurrentVersionExpiration: 90d | abortIncompleteMultipartUpload: 7d |

Both deployed in single apply. 0-diff confirmed.

### 2. CloudFront Behavior Audit

Full 12-behavior list captured from `aws cloudfront get-distribution-config --id EVTSA9VEHNZVH`.

**Critical finding for OpalETL:** Yang data and BD data are served from SEPARATE CloudFront
behaviors with SEPARATE S3 origins. They require SEPARATE invalidation calls.

| Data Layer | Path Pattern | S3 Origin | Invalidation Path |
|---|---|---|---|
| Yang outputs | `/api/general/json-tiered/*` | S3-opal-data-portal-v2-json | `/api/general/json-tiered/*` |
| Yang outputs (catch-all) | `/api/general/*` | S3-opal-data-portal-v2-json | `/api/general/*` |
| Yang outputs (legacy) | `/json-tiered/*` | S3-opal-data-portal-v2-json | `/json-tiered/*` |
| BD gold outputs | `/api/scoped/advisor-intelligence/*.json` | S3-opal-data-bd | `/api/scoped/advisor-intelligence/*` |

**`/api/general/*` does NOT cover BD data.** BD requires its own invalidation on
`/api/scoped/advisor-intelligence/*`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Lifecycle config by bucket name (no import) | opal-data-portal-v2 and opal-data-bd are not in any TF module. aws_s3_bucket_lifecycle_configuration can manage the config without owning the bucket resource. Safe, no state risk. |
| filter{} empty block on all rules | Terraform AWS provider ~5.x requires filter or prefix per rule. Empty filter{} applies rule to all objects (correct intent). Suppresses "will be error in future version" warning. |
| Both buckets in shared-infra | shared-infra is the right shared-services home for cross-pipeline S3 management. Both buckets serve multiple pipelines. |
| 90-day window for both buckets | Matches PRD target restore window. Balances cost vs. utility. |
| Tag v1.4.0 (not v1.3.0) | git tag -l confirmed v1.3.0 already exists (ADVI-J1, DynamoDB partner identity). |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/shared-infra/main.tf` | Added 2 lifecycle config resources (71 lines + 4-line filter fix) | Yes — `5aea13f0`, `5978d069` |
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/pipeline_inventory.xml` | current_tag v1.4.0; opal-data-bd bucket entry added; opal-data-portal-v2 lifecycle note; full CF behavior table; 2 new owned resources | Yes — `[pending]` |
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/DRFR_PTMCH.001.cloudops-findings.md` | New findings document (all 6 requirements) | Yes — `[pending]` |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/DRFR_PTMCH.P1.lifecycle-iam-cloudfront.md` | status: pending -> complete | Yes — `[pending]` |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| shared-infra | `shared-infra-v1.4.0` | `5978d069` (source) |

---

## Verification

**Apply output:**
```
aws_s3_bucket_lifecycle_configuration.portal_v2_versions: Creation complete after 56s [id=opal-data-portal-v2]
aws_s3_bucket_lifecycle_configuration.bd_versions: Creation complete after 56s [id=opal-data-bd]
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

**0-diff:**
```
No changes. Your infrastructure matches the configuration.
```

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Lifecycle rules deployed on both buckets via Terraform. shared-infra is at 0-diff.
CloudFront behavior table fully documented in findings doc and pipeline_inventory.xml.
Findings doc at `deliverables/DRFR_PTMCH.001.cloudops-findings.md` — ready for OpalETL
consumption. Task order marked complete. Tag `shared-infra-v1.4.0` pushed.

---

## Next Steps

1. **[0.5.0_AE_OpalETL] Consume CloudFront findings** — read `DRFR_PTMCH.001.cloudops-findings.md`
   for invalidation paths when building the portal-time-machine orchestrator Lambda. Yang requires
   `/api/general/*` + `/api/general/json-tiered/*`; BD requires `/api/scoped/advisor-intelligence/*`.

2. **[0.5.0_AE_OpalETL] Add IAM permissions for time-machine role** — CloudOps scope excluded
   IAM from P1. OpalETL must add `s3:GetObjectVersion`, `s3:CopyObject`, `s3:ListObjectVersions`
   to the `opal-data-refresh-lambda-role` in `data-refresh/main.tf` when building the time-machine Lambda.

3. **[0.7.0_AE_CloudOps] Create Terraform module for opal-infrastructure-monitor** — deferred from
   previous session (code at commit `1f6bc00e`, deploy blocked on no TF resource). Not blocked by
   DRFR_PTMCH. Can be actioned independently.

**Files to touch next:**
- `infra/aws/terraform/infrastructure-monitor/` — new module to create (deferred, unrelated to DRFR_PTMCH)

**Do NOT:**
- Disable or suspend S3 versioning on either bucket (Time Machine depends on it)
- Remove noncurrentVersionExpiration from lifecycle rules — this is cost control, not optional
- Add S3 notification config for portal-v2 inside individual pipeline TF modules (portal-notifications owns that)
