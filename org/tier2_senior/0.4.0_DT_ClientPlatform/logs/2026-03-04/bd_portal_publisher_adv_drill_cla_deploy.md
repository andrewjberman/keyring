# bd-portal-publisher adv_drill + cla Deploy (ADVI-004 B1) — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-04
**Start Time:** ~10:10 ET
**End Time:** ~10:45 ET

---

## Objective

Deploy `bd-portal-publisher` Lambda code change from DS commit `5f60d30e` — adds `adv_drill` and `cla` keys to `gold/timeseries_chart.json`. Stream B1 of ADVI-004.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | build-and-upload.sh bd-pipeline bd-portal-publisher | SHA256: `st5BAFmgjTeNL0XpfhbyS/k/LQJZ+ZXY5MvgxfezNJg=`, 14635 bytes |
| 2 | Upload to S3 (boto3 workaround) | `s3://opal-313476888478-lambda-artifacts/bd-pipeline/bd-portal-publisher.zip` |
| 3 | Commit source map | `81b8a66e` ci: upload bd-portal-publisher artifact [skip ci] |
| 4 | terraform plan | 1 resource changed (SHA update only, no IAM/infra) |
| 5 | terraform apply | 1 changed, 0 added, 0 destroyed |
| 6 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 7 | Update deployment_map.xml | bd-portal-publisher + bd-pipeline module -> bd-v2.15.0 |
| 8 | record-terraform-deploy.sh | `4149cf49` ci: record deploy bd-pipeline @ 81b8a66e [skip ci] |
| 9 | Commit deployment_map.xml | `6edb13a8` 0.4.0_DT_ClientPlatform: update deployment_map.xml |
| 10 | Tag + push | `bd-v2.15.0`, pushed CLOUD `f316666b..6edb13a8` |

---

## Incident: AWS CLI Hang — botocore IMDS Probe

**Root cause (corrected):** `botocore` probes the EC2 Instance Metadata Service (IMDS) at `http://169.254.169.254/` on startup — even when static credentials are present in `~/.aws/credentials`. On a non-EC2 Windows machine this TCP connection attempt receives no response and hangs indefinitely. The WMI service is unrelated and fine; restarting it has no effect.

**Initial misdiagnosis:** This session attributed the hang to `platform._wmi_query` (WMI). The monkey-patch workaround happened to work because it changed botocore's startup code path timing enough to fall through to file-based credentials. It was a symptom bypass, not a fix.

**Workaround used this session:**
- Zip built successfully by `build-and-upload.sh` before the hang (zip creation uses PowerShell directly, not botocore)
- S3 upload performed manually via Python with `platform._wmi_query` monkey-patched before botocore import
- SHA verified via `head-object` after upload — artifact is correct

**Terraform itself was unaffected** — Terraform uses the Go AWS SDK, not Python.

**Fix applied (same session, post-B1):** `export AWS_EC2_METADATA_DISABLED=true` added to `~/.bashrc`. This instructs botocore to skip the IMDS probe entirely and go straight to `~/.aws/credentials`. All `aws` CLI calls now work instantly. **Status: RESOLVED.**

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Use boto3 with `platform._wmi_query` monkey-patch instead of aws CLI | IMDS hang blocked all botocore/aws CLI paths this session; monkey-patch changed startup timing enough to fall through to file credentials. Correct fix (`AWS_EC2_METADATA_DISABLED=true`) applied post-B1. |
| Build zip manually via PowerShell script file | MSYS variable substitution mangles `$` signs when passing multi-line PS code inline via Git Bash |
| Record CLOUD temp files (build-zip.ps1, bd-portal-publisher.zip) as transient | Created in workspace root for build workaround, deleted before push |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/ci/lambda-source-map.json` | SHA updated for bd-portal-publisher: old `aWeD...` -> `st5B...` | Yes — `81b8a66e` |
| `infra/aws/lambda/ci/lambda-source-map.json` | last_deployed_commit + last_deployed_at for 12 bd-pipeline functions | Yes — `4149cf49` |
| `infra/aws/terraform/bd-pipeline/CHANGELOG.json` | Deploy record entry | Yes — `4149cf49` |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/deployment_map.xml` | bd-portal-publisher + bd-pipeline module tag -> bd-v2.15.0 | Yes — `6edb13a8` |

---

## Verification

- S3 head-object confirmed: `ContentLength: 14635`, `Metadata: content-sha256: st5BAFmgjTeNL0XpfhbyS/k/LQJZ+ZXY5MvgxfezNJg=`
- Terraform 0-diff confirmed: "No changes. Infrastructure is up-to-date."
- Tag `bd-v2.15.0` pushed to remote

**Next verification (requires Lambda invocation):** Trigger `bd-portal-publisher` manually or wait for next BD gold pipeline run. Confirm in CloudWatch `/aws/lambda/bd-portal-publisher`:
```
adv_drill: N architects with client drill-down
cla: N state drill, N arch drill, N state city-drill
timeseries_chart: NNN days, N architects, N states, N arch client-drills, cla(N geo/N adv/N citygeo)
```

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| bd-pipeline | `bd-v2.15.0` | `6edb13a8` |

---

## Blockers

None. The AWS CLI hang encountered during this deploy was caused by botocore probing the EC2 IMDS endpoint (`169.254.169.254`) on non-EC2 Windows hardware. Fixed by adding `export AWS_EC2_METADATA_DISABLED=true` to `~/.bashrc` — all new sessions inherit this. `build-and-upload.sh` works normally.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

`bd-portal-publisher` deployed at `bd-v2.15.0` with `adv_drill` and `cla` keys in `build_timeseries_chart()` output. Lambda code is live. CloudWatch verification pending next pipeline run. The AWS CLI hang (botocore IMDS probe) was resolved post-B1 by `AWS_EC2_METADATA_DISABLED=true` in `~/.bashrc`.

---

## Next Steps

1. **Verify CloudWatch logs** after next BD pipeline run — confirm `adv_drill` and `cla` log lines appear
2. **[RD 0.4.2_RD_AdvisorIntelligence] Implement CLA continuous view** — `cla` key is now live in `gold/timeseries_chart.json`; RD can begin portal rendering (per ADVI-004 task order)

**Files to touch next:**
- None for DT — deploy complete

**Do NOT:**
- Re-enable `build_partner_analytics()` call in `lambda_handler` (marked DISABLED — EC2 script 09 owns that output)
