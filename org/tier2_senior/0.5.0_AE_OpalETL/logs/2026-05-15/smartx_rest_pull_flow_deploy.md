# 0.5.0_AE_OpalETL Session Log -- 2026-05-15

**Agent:** 0.5.0_AE_OpalETL
**Date:** 2026-05-15
**Branch:** CLOUD
**Headline:** SXPL_RESTIN.002 (SmartX REST pull flow) deployed end-to-end as `smartx-v2.2.0` -- live-verified. ADHC_OWNPTH.010 Phase-1 premise correction surfaced + CTO-ruled (Phase 2 pending TO rewrite).

---

## SXPL_RESTIN.002 -- SmartX REST Pull Flow (P1)

Headless SmartX REST integration replacing the browser-automation exporter's login+scrape, on the Orion parked-JWT pattern. Code DS-authored (0.4.0_DS_ClientPlatform~B, brief section-5); AE-owned wrapper + infra + deploy.

### Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit owned-paths lane change | `d208afc52` data/smartx/** POD3 -> SHARED_OPAL_ETL (Andrew direct ruling) |
| 2 | Commit source + TF | `14a620d01` 9 files: 3 TF + 2 Lambda code + source-map entries |
| 3 | Relocate rest-pull bundle to dedicated dir | `d5f68eade` (build-and-upload parity check needs a dedicated source_dir) |
| 4 | build-and-upload smartx-jwt-refresher | SHA256 `MCsLEpIgbLtNDTbSDke9CnlBCmxEhN5slexYv2FIjSc=` |
| 5 | build-and-upload smartx-rest-pull | SHA256 `SnPiO8B8AxABQOxJ2wfoPDFaCxaVeGmcDsVPv0JrzaE=` |
| 6 | Commit source-map artifact SHAs | `1e824dd99` |
| 7 | terraform plan | 15 to add, 0 to change, 0 to destroy |
| 8 | terraform apply | 15 added, 0 changed, 0 destroyed |
| 9 | 0-diff plan | No changes. Infrastructure matches configuration. |
| 10 | Update pipeline_inventory.xml | `d71d55115` current_tag -> smartx-v2.2.0; +2 Lambdas +2 schedules |
| 11 | record-terraform-deploy + commit | `e45feb846` CHANGELOG smartx-v2.2.0 + source-map last_deployed |
| 12 | Tag + push | `smartx-v2.2.0`, pushed CLOUD --follow-tags |

### Resources Deployed (15)

`infra/aws/terraform/smartx-pipeline/` -- 3 new files (`rest-pull.tf`, `rest-pull-iam.tf`, `rest-pull-schedule.tf`) + `outputs.tf`:
- `aws_secretsmanager_secret.smartx_jwt` -- `smartx/jwt/current`
- `aws_lambda_function.jwt_refresher` -- `smartx-jwt-refresher` (py3.11, 128MB/120s, stdlib-only)
- `aws_lambda_function.rest_pull` -- `smartx-rest-pull` (py3.11, 512MB/300s, AWSSDKPandas-Python311 layer)
- 2 CloudWatch log groups
- 2 IAM execution roles + 2 basic-exec attachments + 2 inline policies (least-privilege per brief section-5/11)
- 1 EventBridge Scheduler IAM role + 1 inline policy
- 2 `aws_scheduler_schedule` -- `smartx-jwt-refresher-daily` (09:00 ET) + `smartx-rest-pull-daily` (09:15 ET)

`aws_scheduler_schedule` (not classic `aws_cloudwatch_event_rule`) chosen deliberately: `schedule_expression_timezone = "America/New_York"` keeps 9 AM ET correct across DST; the classic rule is UTC-only.

### Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| smartx-pipeline | `smartx-v2.2.0` | `e45feb846` |

(Next tag was v2.2.0 -- `git tag -l` showed actual latest was v2.1.0, not the v2.0.0 in stale inventory.)

### Verification (live)

`smartx-jwt-refresher` invoked: `{"status": "ok", "expires_at": "2026-05-15T21:42:40+00:00"}`. SM `smartx/jwt/current` populated (RS256 JWT); `s3://opal-data-bd/smartx/jwt/current.json` written (1418 B). DS~B-flagged untested SM/S3 writes -- now verified.

`smartx-rest-pull` invoked: `{"status": "ok", "pull_date": "2026-05-15", "models_ok": 7, "models_failed": 0, "errors": [], "aum_rows": 3531, "holdings_rows": 118}`. Raw landed `smartx/raw/{models,enterprises_aum,holdings}/2026-05-15/{modelId}.json`; bronze landed `smartx/bronze/model_aum/2026-05-15.parquet` (48708 B) + `model_holdings/2026-05-15.parquet` (14685 B). Row counts match DS~B's pre-deploy dry-run exactly.

terraform 0-diff: confirmed (step 9).

### Acceptance Criteria

| AC | Result |
|----|--------|
| AC1 smartx-jwt-refresher deployed, 09:00-ET schedule, parks JWT to SM + S3 | PASS -- live-verified |
| AC2 IAM scoped per brief section-5; opal-data-bd/smartx/jwt/* locked refresher(put)+pull(get) | PASS -- comp-iam gaps clean; least-privilege roles |
| AC3 daily pull lands model value + holdings (7 models) raw+bronze; JWT via reader; modelId->reportedModelId chained; rate limit respected | PASS -- 7/7 models, 3.6s throttle |
| AC4 credentials Secrets-Manager-only; no emoji | PASS -- ASCII-only logs, SM-only creds |
| AC5 terraform apply 0-diff; source-map updated; tagged; pushed --follow-tags; silver/gold NOT in scope | PASS -- raw+bronze only |

### Compiler Tools

| Tool | Result |
|------|--------|
| `comp-iam gaps` | No permission gaps detected (123 services, 64 roles) -- run after iam.tf authored |
| `comp-iam service smartx-jwt-refresher` | s3:PutObject GRANTED. (SM calls under-detected by static analysis -- IAM grants them per brief; empirically confirmed by the successful live invoke.) |
| `comp-iam service smartx-rest-pull` | No ops detected in handler (boto3 calls are in the bundled pull module, not scanned). IAM empirically confirmed -- live invoke succeeded with the actual role. |
| `terraform validate` | Success -- config valid (run twice during authoring) |
| `ds-commit-gate.sh` | Clean on all 4 .py files (py_compile + precommit-check + ruff py39) |

### Notes / Follow-up

- `data/smartx/**` lane: Andrew ruled directly ("smartx backend is a 0.5.0_AE lane") -- applied POD3 -> SHARED_OPAL_ETL (`d208afc52`). Superseded the pending CTO lane ruling.
- `record-terraform-deploy.sh` internal commit defaulted to author "Andrew Berman" -> owned-paths hook (block mode) rejected it; committed the leftovers (`e45feb846`) with the correct `--author`. Possible tooling gap: the script does not pass an agent `--author`.
- TO-1 probe harness `data/smartx/scripts/sxpl_restin_probe.py` remains untracked (DS~B TO-1 deliverable, not TO-2 scope) -- left for DS~B / a separate commit.
- smartx-exporter EC2 untouched. Per Andrew direct 2026-05-15, the exporter decommission is DEFERRED INDEFINITELY (not TO-3) -- the REST pull runs as an additive parallel-soak path while the EC2 exporter stays the proven canonical source, revisited weeks-to-months out depending on API performance. Soak isolation confirmed (CTO query): REST pull writes `opal-data-bd/smartx/{raw,bronze}/`; the exporter writes a different bucket (`opal-data-smartx-v2`). No dual-writer; isolation IAM-enforced (smartx-rest-pull-role PutObject scoped to opal-data-bd/smartx/* only).

---

## ADHC_OWNPTH.010 -- Pre-reset Destruction Guard (held)

Phase 1: empirically proved the TO's core mechanism wrong -- git has no `pre-reset` hook (any version; synthetic-repo probe). `reference-transaction` is the only structural hook firing on `git reset`, aborts cleanly at state=prepared, but is command-blind (`GIT_REFLOG_ACTION` unset) -> topology (`merge-base --is-ancestor`) is the only discriminator and necessarily also catches rebase + amend.

Surfaced to COO; CTO ruled **Option (a) ACCEPT** -- reframe as a unified destructive-HEAD-move guard (reset+rebase+amend are the same risk class; AC10's "rebase out-of-scope" was written under the wrong-premise surgical-hook assumption). COO rewrites scope-step-1 + AC10; Phase 2 build pending that rewrite. Audit token to be `FORCE-HEADMOVE` (was FORCE-RESET).

---

## Current State

- **SXPL_RESTIN.002:** COMPLETE -- deployed `smartx-v2.2.0`, live-verified, pushed. RAVC2 to COO (CC CTO + DS~B).
- **ADHC_OWNPTH.010:** Phase 1 done; Phase 2 held pending COO's TO scope-step-1 + AC10 rewrite (CTO Option-a ruling received).
- **Pipeline tags:** smartx-v2.2.0 (new) / yang-v2.4.0 / news-v2.9.6 / market-overview-v1.9.0.

## Next Steps

- `[2.0.0_SA_COO]` RAVC2 receipt on SXPL_RESTIN.002 AC1-5. Rewrite ADHC_OWNPTH.010 scope-step-1 + AC10 per CTO Option-(a) ruling.
- `[0.5.0_AE]` Execute ADHC_OWNPTH.010 Phase 2 (unified destructive-HEAD-move guard via reference-transaction hook) once COO's TO rewrite lands.
- `[0.4.0_DS_ClientPlatform~B]` Confirm SmartX bronze (model_aum / model_holdings) after the first 09:15-ET scheduled run; commit/route the TO-1 probe harness if it should be tracked.
- `[automated]` 2026-05-16 09:00/09:15 ET: first scheduled refresher + pull runs.
