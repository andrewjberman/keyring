# Session Log — 0.7.0_AE_CloudOps~A — YALP_MDSRC.B2 — 2026-05-21

## Summary

YALP_MDSRC.B2 reassigned to ~A by COO (stimulus-scan — the OpalETL lane is
offline). B2 = the AE commit + Lambda deploy of DS 0.4.0's two pre-built/
verified B1 artifacts (the SmartX model-monthly pull + the yang dual-input
producer modification). This session: completed the review + Phase-1/Phase-2
compiler mandate + the deployment-architecture grounding. The two deploy
cycles are the next phase.

## Artifacts (both DS 0.4.0-built + verified — B2 commits + deploys, no re-author)

| Artifact | File | Lane | State |
|----------|------|------|-------|
| 1 — SmartX model-monthly pull | `data/smartx/scripts/pull_smartx_model_monthly_performance.py` (NEW, untracked, 317 lines) | SHARED_OPAL_ETL | reviewed — clean |
| 2 — yang dual-input producer | `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` (MODIFIED) | CLOUD_OPS_OR_ETL | reviewed — clean diff |

### Review findings
- **Artifact 1**: pure stdlib + boto3 (urllib for HTTP — no `requests`) → **no Lambda layer needed**. SmartX OIDC ROPC auth; `smartx/credentials/username|password` from Secrets Manager. `lambda_handler` entrypoint builds + uploads the sidecar `s3://opal-data-portal-v2/json/benchmarks/_smartx_model_monthly.json`. ASCII-only, `from __future__ import annotations`. Lane conventions OK — no adjustment needed.
- **Artifact 2**: clean 6-edit diff exactly per the handoff brief — `SMARTX_SIDECAR_KEY`/`SMARTX_PERIODS` constants, `load_smartx_sidecar()`, sidecar load in `lambda_handler`, the per-period override branch, `model_source_note` + legacy-label. Graceful all-yang fallback. No output column removed (adds `model_source`). 

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io yang-model-portfolio-benchmarks` | "Unknown script" — not a comp-graph node; fell back to a direct diff review per the TO `<if_mismatch>`. No COLUMN GAPS (the change adds fields, removes none). |
| `comp-iam service yang-model-portfolio-benchmarks` | 4 ops, ALL GRANTED — incl. the new `load_smartx_sidecar` `s3:GetObject` (line 383). **Confirms DS's claim: Artifact 2 needs NO new IAM.** |
| `ds-commit-gate.sh` — Artifact 1 | All checks passed (py_compile + ds-precommit-check + ruff py39). |
| `ds-commit-gate.sh` — Artifact 2 | All checks passed. |

(Phase-3 `comp-pipescript deployed` + 0-diff plans will be added post-deploy.)

## Architecture call — Artifact 1 deployment

**Decision: standalone scheduled Lambda in the `smartx-pipeline` Terraform**,
mirroring the existing `smartx-rest-pull` (SXPL_RESTIN.002) pattern
(`rest-pull.tf` / `rest-pull-iam.tf` / `rest-pull-schedule.tf`). Rationale:
- Decoupled from the yang Step Function — no SFN modification, lower-risk deploy.
- The yang producer's graceful all-yang fallback absorbs any timing gap.
- Reuses the established smartx-pipeline `aws_scheduler_schedule` (timezone-aware) pattern.
- Does NOT touch SXPL_RESTIN architecture → no CTO coordination required.

New TF (planned `model-perf-pull.tf` in `smartx-pipeline/`): `aws_lambda_function`
(python3.11, handler `lambda_function.lambda_handler`, S3-backed artifact, no
layer, ~128-256MB / 120s), a CloudWatch log group, a least-privilege IAM role
(`AWSLambdaBasicExecutionRole` + inline: `secretsmanager:GetSecretValue` on
`smartx/credentials/username-*`+`password-*`, `s3:PutObject` on
`opal-data-portal-v2/json/benchmarks/*`), and an `aws_scheduler_schedule`
(daily, America/New_York — keeps the partial-MTD month fresh).

## Build-mechanism decision (Artifact 1)

The TO mandates Artifact 1's file at its canonical `data/smartx/scripts/`
location (SHARED_OPAL_ETL lane). The `smartx-rest-pull` precedent has Lambda
source under `infra/aws/lambda/smartx_rest_pull/`. To avoid a duplicated copy:
the `lambda-source-map.json` entry for the new Lambda uses
`source_dir: "data/smartx/scripts"`, `files: ["pull_smartx_model_monthly_performance.py"]`
— single source of truth at the TO-mandated path. Lambda `handler` =
`pull_smartx_model_monthly_performance.lambda_handler` (module.function form;
no rename to `lambda_function.py`). Verify `build-and-upload.sh` accepts a
non-`infra/aws/lambda/` `source_dir` at build time; if it does not, the
fallback is a thin `infra/aws/lambda/smartx_model_monthly_pull/lambda_function.py`
shim that imports from the committed `data/` module — decided at build step.

Smartx-pipeline TF facts: `local.account_id="313476888478"`, `local.region="us-east-1"`,
state key `smartx-pipeline/tfstate`, artifact pattern `data.aws_s3_object` +
`source_code_hash = ...metadata["content-sha256"]`, S3-backed
`opal-313476888478-lambda-artifacts/smartx-pipeline/{fn}.zip`.

## Deploy plan (next phase)

Deploy order: **Artifact 1 first** (+ run once so the sidecar exists before the
yang producer's first post-deploy run — avoids the transient all-yang window;
the brief's preferred order).
1. Artifact 1: write `model-perf-pull.tf` → source-map entry → safe-commit the
   `.py` + TF → build-and-upload → terraform plan → safe-apply (HALTGT) →
   0-diff → tag → push --follow-tags → record-deploy → invoke once (sidecar).
2. Artifact 2: safe-commit the lambda diff → build-and-upload yang-pipeline
   (single function `yang-generate-...`/`yang-model-portfolio-benchmarks`) →
   plan → safe-apply → 0-diff → source-map → tag → push → record-deploy.
3. Confirm the sidecar at `s3://opal-data-portal-v2/json/benchmarks/_smartx_model_monthly.json`.
4. RAVC2 to COO + CC CTO + CC 0.4.0_DS (so B1 e2e verification can run).

## Owned-paths note

Artifact 1 is `data/smartx/scripts/` (SHARED_OPAL_ETL lane). If the owned-paths
pre-commit hook blocks ~A's serial on that path-class, STOP and MCP COO for the
one-line `.owned-paths.yaml` `permitted_agents` add — do NOT `--force` (per the
TO + `memory/feedback_tilde_lane_owned_paths_gap_route_to_coo`).

## Deploy progress — BLOCKED on owned-paths (COO action required)

Deploy execution started; both artifacts hit the owned-paths pre-commit hook
(block mode) — the `~A` serial is in neither lane's `permitted_agents`:

| Artifact | File | Lane | Hook result |
|----------|------|------|-------------|
| 1 | `data/smartx/scripts/pull_smartx_model_monthly_performance.py` | `SHARED_OPAL_ETL` | VIOLATION — `0.7.0_AE_CloudOps~A` not in permitted_agents |
| 2 | `yang-model-portfolio-benchmarks/lambda_function.py` | `CLOUD_OPS_OR_ETL` | VIOLATION — `~A` not in permitted_agents (lane is "Any AE agent" but the `~A` suffix is not enumerated) |

Per the TO + `feedback_tilde_lane_owned_paths_gap_route_to_coo`: STOPPED, did
NOT `--force`. Surfaced to COO — msgs 16:07Z (SHARED_OPAL_ETL), 16:11Z
(follow-up: CLOUD_OPS_OR_ETL too), 17:07Z (NUDGE — ~45min, no COO action;
COO confirmed LIVE). Request: add `0.7.0_AE_CloudOps~A` to `permitted_agents`
for BOTH path-classes in `.owned-paths.yaml`.

Staged-aside while blocked (so a concurrent `smartx-pipeline` plan can't break
on the not-yet-built artifact): `model-perf-pull.tf` moved to
`org/tier2_senior/0.7.0_AE_CloudOps/drafts/model-perf-pull.tf` — placed into
`smartx-pipeline/` only after Artifact 1's `.py` commits + the zip builds. The
`lambda-source-map.json` `smartx-model-monthly-pull` entry is added (uncommitted,
inert). Both artifacts remain `ds-commit-gate`-clean.

**RESOLVED:** COO committed `789a2f21c` adding `0.7.0_AE_CloudOps~A` to
`permitted_agents` for both `SHARED_OPAL_ETL` + `CLOUD_OPS_OR_ETL` (~50min
after the first request). Deploy executed straight through after.

## Deployment Sequence — COMPLETE

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit Artifact 1 code | `1d2e312c4` — `data/smartx/scripts/pull_smartx_model_monthly_performance.py` |
| 2 | build-and-upload (Artifact 1, `BAU_PARITY_SKIP=1`) | SHA256 `UBqf5FXt...`; `smartx-pipeline/smartx-model-monthly-pull.zip` |
| 3 | Commit Artifact 1 infra | `48c651f1d` — `model-perf-pull.tf` + source-map entry |
| 4 | `terraform plan` smartx-pipeline | 8 to add, 0 change, 0 destroy |
| 5 | `safe-apply` (HALTGT passed, empty inbox) | Apply complete — 8 added, 0 changed, 0 destroyed |
| 6 | 0-diff plan | "No changes. Your infrastructure matches the configuration." |
| 7 | record-deploy + commit | `ad19e1eaa` — CHANGELOG `smartx-pipeline-v1.1.0` + source-map |
| 8 | tag + push | `smartx-pipeline-v1.1.0` pushed |
| 9 | Invoke Artifact 1 once (sidecar) | StatusCode 200 — 5 models, as_of_month 2026-05; sidecar `s3://opal-data-portal-v2/json/benchmarks/_smartx_model_monthly.json` (5098 B) |
| 10 | Commit Artifact 2 | `84128c245` — yang-model-portfolio-benchmarks dual-input |
| 11 | build-and-upload (Artifact 2) | SHA256 `vEotYTEz...`; `yang-pipeline/yang-model-portfolio-benchmarks.zip` |
| 12 | `terraform plan` + `safe-apply` yang-pipeline | 0 add, 1 change, 0 destroy → Apply complete (1 changed) |
| 13 | 0-diff plan | "No changes." |
| 14 | record-deploy + commit | `0cfe2e311` — CHANGELOG `yang-v2.4.7` + source-map |
| 15 | tag + push | `yang-v2.4.7` pushed |

**Deploy Tags:** `smartx-pipeline-v1.1.0` (Artifact 1) · `yang-v2.4.7` (Artifact 2).

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| 1 | `comp-iam service yang-model-portfolio-benchmarks` | 4 ops all GRANTED — Artifact 2 needs NO new IAM (incl. the new sidecar `s3:GetObject`). Artifact 1 IAM scoped minimally in `model-perf-pull.tf` (SecretsManager + s3:PutObject the sidecar prefix). |
| 1 | `comp-pipescript io yang-model-portfolio-benchmarks` | Not a comp-graph node — fell back to a direct diff review per the TO `<if_mismatch>`. |
| 2 | `ds-commit-gate.sh` × both files | All checks passed (py_compile + ds-precommit-check + ruff py39). |
| 3 | `terraform plan` 0-diff × both | Both "No changes" — deployed state matches config. |
| 3 | `aws lambda get-function` × both | `smartx-model-monthly-pull`: Active/Successful, LastModified 18:12Z. `yang-model-portfolio-benchmarks`: Active/Successful, LastModified 18:19Z. |
| 3 | `comp-pipescript deployed` × both | "No scripts matched" — Lambdas are not comp-graph gold scripts; the 0-diff plan is the equivalent verification per the TO `<if_mismatch>`. |

## Process notes

- `BAU_PARITY_SKIP=1` for Artifact 1's build — `data/smartx/scripts/` is a
  shared multi-script directory (22 files); `pull_smartx_model_monthly_performance.py`
  is a self-contained single-file Lambda (stdlib + boto3, no local imports), so
  `files[]` correctly lists the one file. Justified in commit `48c651f1d`.
- `record-terraform-deploy.sh`'s own commit defaults to the git user
  ("Andrew Berman"), which is not in `permitted_agents` → the owned-paths
  author check blocked it both times. Worked around by committing its file
  updates manually under the `~A` agent author (`ad19e1eaa` / `0cfe2e311`).
  Flagged to CTO as a `record-terraform-deploy.sh` gap (it should pass an
  agent `--author`).
- Owned-paths: both lanes needed the `~A` add — tilde-lane gap, COO `789a2f21c`.

## Current State

| Item | Status |
|------|--------|
| Artifact 1 (smartx-model-monthly-pull) | DEPLOYED — `smartx-pipeline-v1.1.0`; invoked, sidecar live |
| Artifact 2 (yang-model-portfolio-benchmarks) | DEPLOYED — `yang-v2.4.7`; 0-diff verified |
| Both Lambdas | Active / LastUpdateStatus Successful |
| RAVC2 | SENT — COO + CC CTO + CC 0.4.0_DS |
| B2 | **COMPLETE** |

## Post-B2 fill-in fixes (COO-dispatched, YCharts-freeze window)

The `record-terraform-deploy.sh` author gap this log flagged was taken as a
fill-in and fixed — both commits RAVC2'd to + accepted by COO:

- `24642756b` — `record-terraform-deploy.sh`: when `--author` is omitted it now
  derives the acting agent's serial from `.comp-graph/.agent_context` instead of
  falling through to the git human identity (which clears no owned-paths lane).
  Best-effort (`.agent_context` is shared/last-writer-wins — surfaced to COO);
  explicit `--author` remains the reliable path. awk-only (Rule 16).
- `3d579f601` — `build-and-upload.sh`: the printed "Next steps" + header
  deploy-sequence comment now show the `record-terraform-deploy.sh` line WITH
  `--author "{serial} <{serial}@opal.agent>"` + a note it is required — makes
  the reliable path the documented default.

## Current State (final)

| Item | Status |
|------|--------|
| B2 | COMPLETE — RAVC2-ACCEPTED by COO (both Lambdas deployed, producer activated) |
| B2 deploy-activation | DONE — yang producer run fired; model_portfolio_benchmarks.json regenerated with the live dual-input (Path A split confirmed) |
| record-terraform-deploy author fix | SHIPPED `24642756b` — RAVC2-accepted |
| build-and-upload guidance fix | SHIPPED `3d579f601` — RAVC2 sent |

## Next Steps

1. [0.4.0_DS] B1 end-to-end `model_portfolio_benchmarks.json` verification — both Lambdas deployed, the sidecar is live, the producer has run (pinged).
2. [~A] Standby for the B3 AE-deploy half (COO dispatches when 0.4.0_DS's B3 Phase 1 code is committed + verified). YCharts capture work (A4 36-recapture + 9-symbol search) stays RUN-frozen until Andrew lifts the freeze.
