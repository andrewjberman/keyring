# ADVI_APISCP.002: Stale IAM Portal-v2 Cleanup — 0.7.0_AE_CloudOps

**Date:** 2026-03-10
**Start Time:** 17:45
**End Time:** 17:55

## Objective

Remove the stale `PortalBucketWrite` IAM statement from `bd-pipeline/iam.tf` — an `s3:PutObject`
permission on `opal-data-portal-v2/*` that was a remnant of the eliminated copy-to-portal
anti-pattern. No active BD pipeline code writes to `opal-data-portal-v2` (confirmed by
`0.6.0_AE_PartnerETL` audit, commit `c3820bb1`). Enforces bucket separation at IAM level.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read task order | Full context established |
| 2 | Verify target lines in iam.tf (lines 371-376) | Confirmed exact match |
| 3 | Remove PortalBucketWrite statement + trailing comma | Edit applied cleanly |
| 4 | git commit | `ab731673` infra(bd-pipeline): remove stale PortalBucketWrite IAM permission |
| 5 | terraform plan | 1 change: `aws_iam_role_policy.bd_exporter_s3` updated in-place. No other resources affected. |
| 6 | terraform apply | 0 added, 1 changed, 0 destroyed. Apply complete. |
| 7 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 8 | Update pipeline_inventory.xml | N/A — IAM-only change, no new resources |
| 9 | git tag + push | `bd-v2.17.3` pushed with `--follow-tags` |

---

## Verification

**Plan output (relevant diff only):**
```
~ aws_iam_role_policy.bd_exporter_s3
  ~ policy = jsonencode(
    ~ Statement = [
        { Sid = "BDDataBucket", ... },   # unchanged
      - { Sid      = "PortalBucketWrite"
      -   Effect   = "Allow"
      -   Action   = "s3:PutObject"
      -   Resource = "arn:aws:s3:::opal-data-portal-v2/*"
      - }
      ]
    )
Plan: 0 to add, 1 to change, 0 to destroy.
```

**0-diff confirmed:** `No changes. Your infrastructure matches the configuration.`

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| No other IAM changes | Task order was precise: only PortalBucketWrite. All other statements untouched. |
| Tag bd-v2.17.3 | Latest tag was bd-v2.17.2; patch increment appropriate for IAM-only cleanup. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/bd-pipeline/iam.tf` | Removed PortalBucketWrite statement (6 lines) from `bd_exporter_s3` policy | Yes — `ab731673` |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_APISCP.002.stale-iam-portal-v2-cleanup.md` | Status: pending → complete | Local only |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| bd-pipeline | `bd-v2.17.3` | `ab731673` |

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

`PortalBucketWrite` removed from `bd-exporter-ec2-role:s3-access` policy in AWS. Terraform
state is 0-diff. Tag `bd-v2.17.3` pushed. Task order marked complete. BD pipeline retains
full access to `opal-data-bd` — no operational impact.

---

## Next Steps

No follow-up required for this task. All acceptance criteria met.

**Do NOT:**
- Re-add any `opal-data-portal-v2` permissions to bd-pipeline IAM roles (bucket separation invariant)
