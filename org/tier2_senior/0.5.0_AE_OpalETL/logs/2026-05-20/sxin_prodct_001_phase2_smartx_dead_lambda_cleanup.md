# SXIN_PRODCT.001 Phase 2 — smartx-pipeline dead-Lambda cleanup

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL~B/task_orders/SXIN_PRODCT.001.ae-opt-c-productionize-emit-cleanup-cross-validation.md`
**Tag shipped:** `smartx-pipeline-v1.0.2`
**Deploy commit:** `ccf3a79c2` (cleanup) + `92f20a167` (record-deploy) + `f2cb89623` (CHANGELOG agent/note fixup)

---

## Current State

- **SXIN_PRODCT.001 Phase 2: COMPLETE.** The dead `append_non_model_today` surface on
  `opal-smartx-ingestion-pipeline` is fully retired. STEPs 1-5 of the ingestion pipeline
  unchanged. Deployed `smartx-pipeline-v1.0.2`, terraform 0-diff verified.
- **Scope history:** TO authored as 3-phase (productionize emit + cleanup + cross-validation).
  Cross-validation gate moved to MDPF_ASSETS.019 (scope reduction 2026-05-19). Then CTO~B
  ruled the Phase 1 architecture fork **Option A (in-chain emit step)** 2026-05-20 and split
  Phase 1 out to **SXIN_PRODCT.002** (0.7.0_AE_CloudOps~B lane — it edits `mdpf-daily-dispatch.sh`,
  the same chain script MDPF_ASSETS.023 edits). SXIN_PRODCT.001 is therefore **Phase-2-only**,
  shipped here.
- **append_non_model_today** was already a v1.0.1 no-op (`append_today_row()` retired in the
  CEO-direct methodology pivot). This TO removed the dead code + dead IAM entirely.

## Phase 0 Probe Findings

- Phase 1 substrate already exists: `infra/aws/terraform/mdpf-pipeline/legacy-emit-ssm.tf`
  (MDPF_ASSETS.021) — the `mdpf-legacy-emit-on-demand` SSM doc + unattached `MDPFLegacyEmitInvoker`
  policy. Architecture blocker surfaced for the naive EventBridge->SSM design: `mdpf-daily-runner`
  EC2 is stopped between runs. RAVC1 raised the A/B fork; CTO~B ruled Option A, Phase 1 -> .002.
- Phase 2 (this ship): `lambda_function.py` STEP 6 still imported + called `append_non_model_today`;
  the function file + 2 IAM statements (`opal-data-bd` aua_certification+allocations read;
  `opal-data-mdpf/cache/*` read) on `smartx-ingestion-lambda-role` served only the dead function.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Edit `lambda_function.py` — remove STEP 6 block + `append_non_model_today` import | -38 lines |
| 2 | `git rm append_non_model_today.py` | -307 lines |
| 3 | Edit `smartx-pipeline/iam.tf` — drop 2 dead IAM statements on `ingestion_s3` policy | -25 lines |
| 4 | Edit `lambda-source-map.json` — drop `append_non_model_today.py` from `files[]` | -1 line |
| 5 | `py_compile` + `.tools/ds-commit-gate.sh lambda_function.py` | py_compile OK; gate "All checks passed" |
| 6 | `build-and-upload.sh smartx-pipeline` | ingestion SHA256 `2jPobc/Pn8cggcFzDjpxeRT3wtCHAnlV7/ybAvCvU5U=`; uploaded |
| 7 | `safe-commit.sh` cleanup diff | `ccf3a79c2` (4 files, 3 ins / 373 del) |
| 8 | `git push origin CLOUD` | `4b14c8e1a..ccf3a79c2` |
| 9 | `terraform apply` | Apply complete: 0 added, 5 changed, 0 destroyed |
| 10 | 0-diff replan | "No changes. Your infrastructure matches the configuration." |
| 11 | `record-terraform-deploy.sh smartx-pipeline --version smartx-pipeline-v1.0.2 --author ...` | `92f20a167`; advanced ingestion only, preserved 3 siblings |
| 12 | CHANGELOG fixup — correct `agent`, add `_deploy_note` for no-op siblings | `f2cb89623` |
| 13 | `git tag -a smartx-pipeline-v1.0.2` + `git push --follow-tags` | `[new tag] smartx-pipeline-v1.0.2` |
| 14 | Update `pipeline_inventory.xml` (core doc) | current_tag + ingestion last_deployed_commit + note |

## Build-unit side-effect (documented per COO~B directive)

`build-and-upload.sh smartx-pipeline` rebuilds the whole pipeline — it re-zipped + re-uploaded
all 4 smartx functions, so `terraform apply` modified 5 resources: `aws_iam_role_policy.ingestion_s3`
+ `aws_lambda_function.{ingestion_pipeline,ec2_autostart,jwt_refresher,rest_pull}`. Only
`ingestion_pipeline` + the IAM policy are real TO-scope changes. `ec2_autostart` / `jwt_refresher`
/ `rest_pull` were **no-op redeploys** — `jwt_refresher` + `rest_pull` byte-identical (unchanged
`source_code_hash`), `ec2_autostart` re-zipped with no functional change. RAVC1'd to COO~B; ruled
**Option A — apply all 4** (in-pattern pipeline-unit deploy; Option B was an S3 object-version
deletion, rejected as racy under ~B-only comms). `record-terraform-deploy.sh` auto-preserved the
3 siblings' `last_deployed_commit` (detected unchanged content); CHANGELOG `_deploy_note` documents
the no-op redeploys explicitly.

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| smartx-pipeline | smartx-pipeline-v1.0.2 | ccf3a79c2 |

## Acceptance Criteria

| AC | Description | Status | Evidence |
|---|---|---|---|
| AC1 | (Phase 1 — scheduled emit) | **N/A** | Split to SXIN_PRODCT.002 per CTO~B Option-A ruling. |
| AC2 | Dead-Lambda cleanup verified: STEP 6 / function / IAM removed; comp-iam gaps no orphan; comp-blast empty | **PASS** | STEP 6 + import + file + 2 IAM statements + source-map entry removed; `comp-iam gaps` shows ZERO gaps on `smartx-ingestion-lambda-role` (the removed IAM was truly dead); `comp-blast append_non_model_today` empty (not a graph node). |
| AC4 | Terraform-only deploy per Rule 1 | **PASS** | commit `ccf3a79c2` -> push -> plan -> apply (0/5/0) -> 0-diff -> tag `smartx-pipeline-v1.0.2` -> push --follow-tags -> record-terraform-deploy. No console shortcuts. |
| AC5 | No emoji in my changes; ds-commit-gate exit 0; session log | **PASS** | My diff is ASCII-only (removed STEP 6 which contained an em-dash; pre-existing emoji elsewhere in `lambda_function.py` untouched — out of scope). `ds-commit-gate.sh` "All checks passed". This log = AC5 deliverable. |
| AC6 | Compiler-tools | **PASS** | See Compiler Tools section. |
| AC7 | RAVC2 to 2.0.0_SA_COO~B (CC CTO~B) | sending after this log commits |

## Verification

```text
# terraform apply
Apply complete! Resources: 0 added, 5 changed, 0 destroyed.

# 0-diff replan
No changes. Your infrastructure matches the configuration.

# ingestion artifact
s3://opal-313476888478-lambda-artifacts/smartx-pipeline/opal-smartx-ingestion-pipeline.zip
SHA256: 2jPobc/Pn8cggcFzDjpxeRT3wtCHAnlV7/ybAvCvU5U=  (was a2EM0JyzUXxQkRKnsQ6LePJS1B0b5lUkZQI9CJU1vLo=)

# comp-iam gaps -- smartx-ingestion-lambda-role: ZERO gaps (removed IAM had no remaining caller)
```

## Compiler Tools

| Tool | Result | What worked / failed |
|------|--------|----------------------|
| `.tools/ds-commit-gate.sh lambda_function.py` | "All checks passed" | py_compile + AST scan + ruff clean on the edited Lambda source |
| `comp-iam gaps` | 2 gaps found, both in `mdpf-daily-trigger` (NOT my scope) | ZERO gaps on `smartx-ingestion-lambda-role` — confirms the 2 IAM statements I removed had no remaining code caller. The 2 reported gaps are pre-existing in a different pipeline (mdpf-pipeline) and look like false positives (`aws s3 cp` is text inside an SSM runShellScript body executed by the EC2 role, not the Lambda role). Flagged, not in scope. |
| `comp-blast append_non_model_today` | "No nodes matching" | Lambda-internal modules are not graph nodes; expected-empty pre + post removal. |
| `comp-iam service opal-smartx-ingestion-pipeline` | "No AWS operations detected" | comp-iam does not trace into the Lambda's imported step modules; no new boto3 surface added by this TO (pure removal) so no IAM gap possible. |
| `comp-pipescript deployed smartx-pipeline` | "No scripts matched filter" | comp-pipescript deployed covers DS gold/silver scripts only, not Lambda pipelines. Lambda-deploy parity is verified by the terraform 0-diff replan instead (AC4). |

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 validation AC2/AC4/AC5/AC6 + this log. On accept: SXIN_PRODCT.json
  status -> complete; REGISTRY 3-step atomic. SXIN_PRODCT.001 TO self-flip to complete.
- `[0.7.0_AE_CloudOps~B]` SXIN_PRODCT.002 (Phase 1 in-chain emit step in `mdpf-daily-dispatch.sh`)
  is the remaining productionization half — separate lane, separate TO.
- `[follow-up, non-blocking]` smartx tag namespace is split (`smartx-v*` vs `smartx-pipeline-v*`);
  pipeline_inventory.xml `current_tag` set to `smartx-pipeline-v1.0.2` (the deployed module tag).
  Reconciling the dual convention is out of this TO's scope — noted for a future cleanup.
