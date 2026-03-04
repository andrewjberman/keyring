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

## Incident: WMI Hang in Python/botocore

**Root cause:** `botocore.session.get_session()` hangs on startup in Python 3.12 because `platform.win32_ver()` calls `platform._wmi_query()`, which makes a WMI (Windows Management Instrumentation) query that hangs. This breaks ALL `aws` CLI invocations and `build-and-upload.sh`'s PowerShell S3 upload path.

**Workaround applied:**
- Zip was built successfully by `build-and-upload.sh` before the hang (zip creation uses PowerShell directly, not botocore)
- S3 upload performed manually via Python with `platform._wmi_query` monkey-patched before botocore import:
  ```python
  import platform
  platform._wmi_query = lambda *a, **kw: ('10.0.26100', 0, 'Multiprocessor Free', 0, 0)
  import boto3
  ```
- `build-and-upload.sh` source map update was blocked by the hang, but the source map had already been pre-updated (the working tree diff showed the correct new SHA before the commit)

**Terraform itself was unaffected** — Terraform uses the Go AWS SDK, not Python, and connected to AWS without issue.

**Action needed:** WMI service on this machine is unresponsive. Either a Windows reboot clears it, or the WMI service needs to be restarted (`net stop winmgmt && net start winmgmt` as admin). This will affect ALL Python AWS CLI calls until resolved.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Use boto3 with WMI monkey-patch instead of aws CLI | WMI hang blocked all aws CLI paths; boto3 with the patch works fine |
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

**WMI hang (active):** Python botocore hangs on startup due to `platform._wmi_query` WMI query. The `aws` CLI (Python-based) is completely unusable. `build-and-upload.sh` S3 upload step will hang on every run until resolved. Workaround documented above works but is manual. A machine reboot or WMI service restart should fix this.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

`bd-portal-publisher` deployed at `bd-v2.15.0` with `adv_drill` and `cla` keys in `build_timeseries_chart()` output. Lambda code is live. CloudWatch verification pending next pipeline run. The WMI issue is a machine-level problem unrelated to this deploy.

---

## Next Steps

1. **Verify CloudWatch logs** after next BD pipeline run — confirm `adv_drill` and `cla` log lines appear
2. **Fix WMI / restart machine** — `platform._wmi_query` hang blocks all future Python aws CLI use; reboot or `net stop winmgmt && net start winmgmt` (admin)
3. **[RD 0.4.2_RD_AdvisorIntelligence] Implement CLA continuous view** — `cla` key is now live in `gold/timeseries_chart.json`; RD can begin portal rendering (per ADVI-004 task order)

**Files to touch next:**
- None for DT — deploy complete

**Do NOT:**
- Use `aws` CLI directly until WMI is fixed — it will hang
- Re-enable `build_partner_analytics()` call in `lambda_handler` (marked DISABLED — EC2 script 09 owns that output)
