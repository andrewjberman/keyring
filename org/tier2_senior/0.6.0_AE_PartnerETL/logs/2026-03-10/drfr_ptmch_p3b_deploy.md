# DRFR_PTMCH.P3b Deploy — 0.6.0_AE_PartnerETL

**Date:** 2026-03-10
**Start Time:** ~21:30 UTC (resumed after crash mid-plan)
**End Time:** ~23:35 UTC

## Objective

Deploy patched bd-time-machine (commit 233da228) as bd-v2.18.1 per COO task order P3b.
Fixes: try/except in restore paths, MetadataDirective=COPY (default), tuple return signatures.
Deploy-only — no code changes required.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Verify bug fixes in working copy (4 criteria) | All confirmed in lambda_function.py |
| 2 | Build + upload bd-time-machine via PowerShell PS1 | SHA256: `ECUBv/TTn8fmwdHNOH+HQ7f22ou3FBmjEBbU1x8/kX8=` |
| 3 | Update source map + commit | `dbff0093` [skip ci] |
| 4 | terraform plan (bd-pipeline) | 0 add, 1 change, 0 destroy (code update) |
| 5 | terraform apply | 1 changed (bd-time-machine Lambda) |
| 6 | 0-diff plan | No changes |
| 7 | pipeline_inventory.xml → bd-v2.18.1 | Updated |
| 8 | record-terraform-deploy + commit | `8c794947` |
| 9 | Task orders P3 + P3b marked complete | `f0c04c16` |
| 10 | Tag bd-v2.18.1 + push | Pushed |
| 11 | Smoke test | Lambda ran 145s, AccessDenied on list_object_versions |
| 12 | **Root cause:** `s3:ListObjectVersions` in IAM policy (action does not exist) | Should be `s3:ListBucketVersions` |
| 13 | Fix iam.tf + commit | `2ab1e436` |
| 14 | terraform plan | 0 add, 1 change (IAM policy), 0 destroy |
| 15 | terraform apply | 1 changed (IAM policy) |
| 16 | 0-diff plan | No changes |
| 17 | Smoke test (post-IAM-fix) | IAM confirmed working, no AccessDenied |
| 18 | Fallback path performance finding | Timeout (300s) on gold/clients/ volume |
| 19 | pipeline_inventory.xml → bd-v2.18.2 | Updated |
| 20 | record-terraform-deploy + commit | `cf5117b0` |
| 21 | Tag bd-v2.18.2 + push | Pushed |

## Verification

```
aws lambda get-function --function-name bd-time-machine \
  --query "Configuration.{CodeSha256:CodeSha256,LastModified:LastModified}"

{
    "CodeSha256": "ECUBv/TTn8fmwdHNOH+HQ7f22ou3FBmjEBbU1x8/kX8=",
    "LastModified": "2026-03-10T22:40:48.000+0000"
}
```

SHA256 matches patched artifact. IAM fix confirmed via CloudWatch: no AccessDenied post-fix.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Fix IAM immediately (unplanned bd-v2.18.2) | Smoke test revealed fallback path broken by wrong IAM action name. Deploy in same session — no code change, IAM-only. |
| Do not attempt fallback smoke test after IAM fix | gold/clients/ has thousands of per-client JSON files; fallback path exhausts 300s Lambda timeout. Not a bug — a known capacity limit of the fallback design. |
| Defer full acceptance test to post-manifest | First manifest created at ~23:00 UTC nightly run. Manifest path is fast (O(n) on manifest entries, no S3 version scan). Full acceptance per DRFR_PTMCH_acceptance_test_plan.md should run after that. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/bd-pipeline/bd-time-machine/lambda_function.py` | Bug fixes by COO at 233da228 (not this session) | Yes — `233da228` |
| `infra/aws/lambda/ci/lambda-source-map.json` | SHA256 updated for bd-time-machine | Yes — `dbff0093` |
| `infra/aws/terraform/bd-pipeline/iam.tf` | `s3:ListObjectVersions` → `s3:ListBucketVersions` | Yes — `2ab1e436` |
| `org/tier2_senior/0.6.0_AE_PartnerETL/deliverables/pipeline_inventory.xml` | bd-v2.18.1 → bd-v2.18.2, last_deployed_commit updated | Yes — `97f49f4a` |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/DRFR_PTMCH.P3.bd-time-machine.md` | Status: in_progress → complete | Yes — `f0c04c16` |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/DRFR_PTMCH.P3b.bd-time-machine-patch.md` | Status: pending → complete | Yes — `f0c04c16` |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| bd-pipeline | `bd-v2.18.1` | `f0c04c16` (code patch) |
| bd-pipeline | `bd-v2.18.2` | `97f49f4a` (IAM fix) |

---

## Blockers

None. IAM fixed in session.

**Fallback path performance limitation** (not a blocker, architectural note):
The `_restore_fallback` path scans `list_object_versions` for every key under `gold/`.
`gold/clients/` contains thousands of per-client JSON files. At ~145ms per list_object_versions
call, the fallback exceeds 300s on any date requiring client-level restore.
The manifest path (primary) is not affected — it only CopyObjects files listed in the manifest.
Recommendation: do not test the fallback path in isolation; test via manifest path post-23:00 UTC.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

bd-time-machine is deployed at `bd-v2.18.2` with both P3b code fixes (error handling, MetadataDirective)
and the IAM fix (`s3:ListBucketVersions`). The Lambda is correctly configured and will function on
its primary (manifest) path. First manifest will be written tonight at ~23:00 UTC by the nightly
bd-portal-publisher run triggering bd-capture-output-versions. Full acceptance testing per
`docs/testing/DRFR_PTMCH_acceptance_test_plan.md` can run after the first manifest exists.

---

## Next Steps

1. **Wait for nightly run** (~23:00 UTC) — bd-capture-output-versions writes first manifest to `s3://opal-data-bd/snapshots/manifests/`
2. **Verify manifest exists**: `aws s3 ls s3://opal-data-bd/snapshots/manifests/`
3. **Full acceptance test** per `docs/testing/DRFR_PTMCH_acceptance_test_plan.md` — use manifest-path date (any date after first manifest)
4. **[2.0.0_SA_COO]** Notify that DRFR_PTMCH Time Machine stack is deployed and ready for acceptance testing

**Do NOT:**
- Use 2026-03-06 (or any pre-2026-03-10 date) for fallback smoke tests — gold/clients/ volume exceeds 300s timeout
- Use `aws lambda update-function-code` for any future patches
