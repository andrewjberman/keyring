# Portal Time Machine Deploy (DRFR_PTMCH P5) -- 0.5.0_AE_OpalETL

**Date:** 2026-03-12

## Objective

Two changes for Phase 5:
1. Patch yang-time-machine to exclude append-only JSON paths from S3 version restore
2. Build portal-time-machine orchestrator Lambda that fans out to yang/bd/news restore layers

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source (yang-time-machine patch, portal-time-machine, data-refresh API, TF) | `c92bf442` feat(time-machine): portal-time-machine orchestrator + append-only exclusion |
| 2 | build-and-upload.sh yang-pipeline yang-time-machine | SHA256: `TIHg/TYwb0R7vTNkhE1n4+sVyNGrG9VSSutiujFEIQw=` |
| 3 | build-and-upload.sh data-refresh portal-time-machine | SHA256: `0R8pqdEvf4qvWYCYMYbuSrmekB6l9+5jd8I11b70jbk=` |
| 4 | build-and-upload.sh data-refresh opal-data-refresh-api | SHA256: `ay+UJHc51v9i4acbBxCJIX6HsK9ay57wBwN6xvDVH1Q=` |
| 5 | Commit source map | `324d9a03` ci: upload artifacts [skip ci] |
| 6 | terraform apply yang-pipeline | 0 added, 1 changed (yang-time-machine code) |
| 7 | terraform init data-refresh | Initialized portal_time_machine module |
| 8 | terraform apply data-refresh | 3 added (Lambda + log group + IAM), 2 changed (API env var + IAM target) |
| 9 | 0-diff plan yang-pipeline | No changes. Infrastructure is up-to-date. |
| 10 | 0-diff plan data-refresh | No changes. Infrastructure is up-to-date. |
| 11 | record-deploy + tag + push | `84273455` / `8b1ccb6d`, tags `yang-v2.3.1` + `data-refresh-v2.2.0` |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| yang-pipeline | `yang-v2.3.1` | `84273455` |
| data-refresh | `data-refresh-v2.2.0` | `8b1ccb6d` |

## Verification

- Terraform 0-diff confirmed on both pipelines
- Lambda `portal-time-machine` created: 128MB, 15s, python3.11, no layers needed
- Lambda `yang-time-machine` updated with append-only exclusion logic
- Lambda `opal-data-refresh-api` updated: TIME_MACHINE_FUNCTION_NAME -> portal-time-machine
- IAM: data-refresh role can invoke portal-time-machine; portal-time-machine can invoke all 3 downstream Lambdas

## Append-Only Path Exclusion

**Paths SKIPPED during yang-time-machine restore:**
- `json/portfolios/*` -- append-only time series (frontend filters by view_as_of date)

**Snapshot exceptions (still restored):**
- `json/portfolios/aum-metrics.json` -- snapshot, not time series
- `json/portfolios/account-distribution.json` -- snapshot, not time series

**Paths NOT skipped (confirmed as snapshot):**
- `json/model_portfolios/views/*` -- fully regenerated each SmartX run (latest.json, summary.json, by_assetclass/*.json, by_period/*.json)

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| json/model_portfolios/views/ is snapshot, DO restore | precompute_views.py fully regenerates all view JSONs from SmartX parquet each run. Not appended. |
| portal-time-machine uses opal-data-refresh-lambda-role | Same role as data-refresh API. Simpler than creating a new role. Role only needs lambda:InvokeFunction on 3 downstream functions + CloudWatch logs (already covered). |
| 128MB / 15s for portal-time-machine | Lightweight orchestrator -- only makes 3 async invoke calls, no data processing. |
| Separate IAM policy for downstream invokes | Clean separation: data_refresh_time_machine_invoke (API -> orchestrator) vs portal_time_machine_invoke_downstream (orchestrator -> yang/bd/news) |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/v2_portal/yang_pipeline/outputs/yang-time-machine/lambda_function.py` | Added _is_append_only(), APPEND_ONLY_PREFIXES, SNAPSHOT_EXCEPTIONS; updated restore_outputs() to skip + track | Yes -- `c92bf442` |
| `infra/aws/lambda/data_refresh/portal_time_machine/lambda_function.py` | New Lambda -- orchestrator fan-out to yang/bd/news | Yes -- `c92bf442` |
| `infra/aws/lambda/data_refresh/lambda_function.py` | TIME_MACHINE_FUNCTION_NAME default -> portal-time-machine | Yes -- `c92bf442` |
| `infra/aws/terraform/data-refresh/main.tf` | Added portal_time_machine module + IAM; updated API env var and invoke target | Yes -- `c92bf442` |
| `infra/aws/lambda/ci/lambda-source-map.json` | Added portal-time-machine entry; updated SHA256s | Yes -- `324d9a03`, `84273455`, `8b1ccb6d` |
| `infra/aws/terraform/yang-pipeline/CHANGELOG.json` | Added yang-v2.3.1 entry | Yes -- `84273455` |
| `infra/aws/terraform/data-refresh/CHANGELOG.json` | Added data-refresh-v2.2.0 entry | Yes -- `8b1ccb6d` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

The portal-time-machine orchestrator is deployed. POST /data-refresh/time-machine now invokes
portal-time-machine (async), which fans out to yang-time-machine, bd-time-machine, and
semantic-trending-topics-portal-publisher in parallel. yang-time-machine skips append-only
json/portfolios/ paths (except aum-metrics.json and account-distribution.json snapshots).

---

## Next Steps

1. **Verify live invocation** -- trigger POST /data-refresh/time-machine from the portal.
   Confirm CloudWatch logs show: portal-time-machine invoked, then yang/bd/news each invoked.
2. **Verify append-only skip** -- after a yang-time-machine restore, confirm response includes
   `files_skipped_append_only` with json/portfolios/ time series keys. Verify
   json/portfolios/aum-metrics.json IS restored (not skipped).
3. **[2.0.0_SA_COO] Mark P5 task order complete** -- all acceptance criteria met except live validation.
