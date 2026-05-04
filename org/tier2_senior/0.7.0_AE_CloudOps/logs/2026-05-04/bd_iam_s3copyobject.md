# 0.7.0_AE_CloudOps — BD_IAM_S3COPYOBJECT Session Log
**Date:** 2026-05-04
**TO:** BD_IAM_S3COPYOBJECT (ad-hoc operational fix)
**Session type:** IAM gap fix — Terraform + deploy

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | comp-iam service bd-gold-runner (Phase 1 mandate) | s3:CopyObject MISSING on bd-exporter-ec2-role at D_04:2405 confirmed |
| 2 | Read D_04.client_portal_summary.py:2398-2415 | copy_object target: platinum/firm/leaderboard.json → .prior_week.json; resource scope opal-data-bd/platinum/* |
| 3 | Read iam.tf:374-398 (bd_exporter_s3 block) | Resource already arn:aws:s3:::opal-data-bd/*; missing only s3:CopyObject from action list |
| 4 | Edit iam.tf | Added "s3:CopyObject" to bd_exporter_s3 statement |
| 5 | terraform plan (Phase 2 mandate) | 0 to add, 1 to change, 0 to destroy — single IAM policy diff only |
| 6 | git commit via safe-commit.sh | ae29221d5 — author 0.7.0_AE_CloudOps |
| 7 | terraform apply | Apply complete: 0 added, 1 changed, 0 destroyed |
| 8 | terraform plan 0-diff verify (Phase 3 mandate) | No changes. Infrastructure matches configuration. |
| 9 | git tag -l check | Latest was bd-v2.24.4 (memory stale at bd-v2.23.0); tagged bd-v2.24.5 |
| 10 | git push --follow-tags | CLOUD → remote, bd-v2.24.5 tag pushed |
| 11 | comp-iam gaps (Phase 3 mandate) | No permission gaps detected. (1 services scanned, 50 IAM roles parsed) |
| 12 | TO status update | pending → complete |

---

## IAM Change Detail

**Policy:** `aws_iam_role_policy.bd_exporter_s3` (name="s3-access", role=bd-exporter-ec2-role)
**File:** `infra/aws/terraform/bd-pipeline/iam.tf` (lines 384-390)

**Before:**
```hcl
Action = [
  "s3:PutObject",
  "s3:GetObject",
  "s3:ListBucket",
  "s3:HeadObject",
  "s3:DeleteObject"
]
```

**After:**
```hcl
Action = [
  "s3:PutObject",
  "s3:GetObject",
  "s3:ListBucket",
  "s3:HeadObject",
  "s3:DeleteObject",
  "s3:CopyObject"
]
```

**Resource scope:** `arn:aws:s3:::opal-data-bd` + `arn:aws:s3:::opal-data-bd/*` (already present — no change)

**Call site confirmed:** D_04.client_portal_summary.py:2405 — copies `platinum/firm/leaderboard.json` → `platinum/firm/leaderboard.prior_week.json` (prior-week rotation, ADVI_49EXEC.005). Both source and destination are within `opal-data-bd/platinum/firm/` — covered by existing `opal-data-bd/*` resource.

---

## Compiler Tools

| Tool | Phase | Run | Result |
|------|-------|-----|--------|
| comp-iam service bd-gold-runner | Phase 1 (before code) | Pre-edit | s3:CopyObject MISSING at D_04:2405 — confirmed gap |
| terraform plan | Phase 2 (before commit) | Pre-commit | 0 to add, 1 to change, 0 to destroy — single IAM diff |
| terraform plan (0-diff) | Phase 3 (after commit) | Post-apply | No changes. Infrastructure matches configuration. |
| comp-iam gaps | Phase 3 (after commit) | Post-apply | No permission gaps detected. (1 services scanned, 50 IAM roles parsed) |

---

## 0-Diff Plan Output (post-apply)

```
No changes. Your infrastructure matches the configuration.

Terraform has compared your real infrastructure against your configuration
and found no differences, so no changes are needed.
```

---

## comp-iam gaps Output (post-fix)

```
No permission gaps detected.
  (1 services scanned, 50 IAM roles parsed)
```

---

## Commit + Tag

| Item | Value |
|------|-------|
| Commit | ae29221d5 |
| Author | 0.7.0_AE_CloudOps |
| Message | fix(BD_IAM_S3COPYOBJECT): add s3:CopyObject to bd-exporter-ec2-role |
| Tag | bd-v2.24.5 |
| Push | git push origin CLOUD --follow-tags |

---

## Coupling Note

DS~B (ADVI_49FRECN.003) has shipped Track 2 D_04 changes (AQR filter removal + c1_recovered_accounts.json sidecar). The s3.copy_object call pre-dates their changes. With this IAM grant live, the next BD gold run on D_04 will succeed on the copy_object call. No D_04 reprocess needed — IAM-only change, no data semantics affected.
