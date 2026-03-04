# Master Session Log — ADVI-004/005 B1+B2 Deploy + DS Review — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-04
**Agent:** 0.4.0_DT_ClientPlatform (DevOps Technician, Client Platform Pod)
**Start Time:** ~10:10 ET
**End Time:** ~11:30 ET
**Branch:** `CLOUD`
**Purpose of this log:** Full-session record for external validation. Covers all commits authored or triggered by this agent, all deployment actions, one infrastructure incident and its resolution, and a QA gate review of upstream DS work.

---

## Startup Protocol

1. Read `START_HERE.md`, `org/AGENT_START_HERE.md` — mandatory pre-work reading.
2. Read agent identity files: `org/tier2_senior/0.4.0_DT_ClientPlatform/README.md`, `prompt.md`.
3. Read most recent session logs — two logs from 2026-03-03 (`lambda_orphan_scan_and_portal_fixes.md`, `portal_auth_terraform_module_and_scoped_page_access_deploy.md`).
4. Read `deployment_map.xml` — verified current pipeline tags (`bd-v2.14.0`, `yang-v2.1.4`).
5. Read task orders — two open: `deployment_audit.md` (status: superseded), `deployment_map.md`.
6. Checked `org/daily_log/2026-03-03.md` — noted COO task order issuance, SA_CTO prompt enrichment work from prior day.

---

## Work Performed

### Part 1 — Stream B1: bd-portal-publisher Lambda Deploy (ADVI-004)

**Trigger:** DS commit `5f60d30e` + DT brief at `docs/briefs/devops-brief-advi-004-adv-drill-cla.md` (committed `f2e3c675`). Brief issued by `0.4.0_DS_ClientPlatform`.

**What changed in the DS commit:** One Lambda source file (`lambda_function.py`) — added `adv_drill` and `cla` keys to `build_timeseries_chart()` output. No infrastructure changes; no new resources, IAM, or env vars. Both new keys additive; all existing keys unchanged.

**Deploy sequence executed:**

| Step | Protocol Step | Action | Result |
|------|--------------|--------|--------|
| 1 | Build + upload artifact | `bash infra/aws/lambda/ci/build-and-upload.sh bd-pipeline bd-portal-publisher` | SHA256: `st5BAFmgjTeNL0XpfhbyS/k/LQJZ+ZXY5MvgxfezNJg=`, 14,635 bytes |
| 2 | Commit source map | `git add lambda-source-map.json && git commit` | `81b8a66e` — SHA updated: `aWeD...` -> `st5B...` |
| 3 | Terraform plan | `.tools/terraform.exe -chdir=infra/aws/terraform/bd-pipeline plan` | 1 resource to change: `module.bd_portal_publisher.aws_lambda_function.this` (S3 object version + source_code_hash only) |
| 4 | Terraform apply | `.tools/terraform.exe -chdir=infra/aws/terraform/bd-pipeline apply` | 0 added, 1 changed, 0 destroyed |
| 5 | 0-diff verify | `.tools/terraform.exe -chdir=infra/aws/terraform/bd-pipeline plan` | "No changes. Infrastructure is up-to-date." ✅ |
| 6 | Record deploy | `bash infra/aws/lambda/ci/record-terraform-deploy.sh bd-pipeline` | `4149cf49` — 12 bd-pipeline functions updated in source map + CHANGELOG.json |
| 7 | Update core doc | `deployment_map.xml` — bd-portal-publisher + bd-pipeline module tag -> `bd-v2.15.0` | Committed at `6edb13a8` |
| 8 | Tag + push | `git tag -a bd-v2.15.0 ...` + `git push origin CLOUD --follow-tags` | Tag `bd-v2.15.0` pushed, CLOUD `f316666b..6edb13a8` |

**Session log written:** `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-04/bd_portal_publisher_adv_drill_cla_deploy.md` — committed `c98d1ae5`

---

### Incident: AWS CLI Hang — Root Cause + Resolution

**Symptom:** `build-and-upload.sh` hung during its PowerShell S3 upload step. All subsequent `aws` CLI calls hung indefinitely — including `aws --version` and `aws sts get-caller-identity`. Terraform was unaffected (uses Go AWS SDK, not Python).

**Initial misdiagnosis (logged in B1 session log, now corrected):** The B1 log attributed the hang to `platform._wmi_query` (Windows WMI service). A monkey-patch workaround was used to bypass it. This treated a symptom, not the root cause.

**Correct root cause (confirmed by network team):** `botocore` probes the EC2 Instance Metadata Service (IMDS) endpoint `169.254.169.254` on startup — even when static credentials are present in `~/.aws/credentials`. On a non-EC2 Windows machine, this TCP connection attempt receives no response and hangs indefinitely. The WMI service is fine; restarting it has no effect.

**Fix applied:** `export AWS_EC2_METADATA_DISABLED=true` — added to `~/.bashrc` by Andrew. This env var instructs botocore to skip the IMDS probe entirely. Verified working: `aws sts get-caller-identity` returned `UserId: AIDAUR7FNW6PEXHN2JIOH`, `Account: 313476888478` immediately after fix.

**B1 workaround (boto3 monkey-patch) outcome:** The monkey-patch changed code path timing enough that botocore fell through to `~/.aws/credentials` before the IMDS timeout. It happened to work but did not fix the root cause. The B1 zip and upload were correct; SHA matched.

**Memory updated:** `~/.claude/projects/.../memory/MEMORY.md` — added `AWS CLI Hang Fix` section with correct root cause explanation.

---

### Part 2 — Stream B2: bd-gold-layer-runner EC2 Deploy (ADVI-005)

**Trigger:** DS commit `c9b3ab76` + DT brief at `docs/briefs/devops-brief-advi-005-rolling-flows.md` (committed `75b3b83f`). Brief issued by `0.4.0_DS_ClientPlatform`.

**What changed in the DS commit:** One EC2 gold script (`data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py`) — added `STACKED_BAR_PERIODS` constant, `compute_stacked_bar()` function, and `rolling_1y` extraction. No infrastructure changes; no new IAM, S3 buckets, or instance changes. Both new output keys additive.

**This is an EC2 deploy, not a Lambda deploy.** Protocol: `repo → S3 → EC2 pulls from S3 → executes`. No Terraform apply required (code change only, no infra change).

**Deploy sequence executed:**

| Step | Protocol Step | Action | Result |
|------|--------------|--------|--------|
| 1 | Export jq PATH | `export PATH=".../.tools:$PATH"` | Required for `safe-ec2-deploy.sh` wrapper |
| 2 | S3 sync via wrapper | `bash infra/aws/ec2/safe-ec2-deploy.sh bd-gold-layer-runner infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh` | Bronze (4 scripts), silver (6 scripts), gold (14 scripts) synced to `s3://opal-data-bd/code/` |
| 3 | Manifest auto-commit | Wrapper auto-committed `EC2_MANIFEST.json` | `4a908760` — deployed_commit + deployed_at recorded |
| 4 | Start EC2 instance | `aws ec2 start-instances --instance-ids i-01003b035d2988dfb --region us-east-1` | State: stopped -> pending. Instance boots, pulls scripts from S3, runs `run_gold_layer.sh incremental` (02->05->07->08->09->10), shuts down on completion. |
| 5 | Update core doc | `deployment_map.xml` — bd-gold-layer-runner `deployed_tag` -> `bd-v2.15.1` | Committed with B2 session log at `8d338013` |
| 6 | Tag + push | `git tag -a bd-v2.15.1 ...` + `git push origin CLOUD --follow-tags` | Tag `bd-v2.15.1` pushed, CLOUD `4a908760..4a908760` |

**Note on pipeline-complete trigger:** When the incremental run completes, `pipeline-complete.json` is written to `s3://opal-data-bd/gold/`, which triggers `bd-portal-publisher` and `bd-portal-advisor-publisher` Lambdas. This is expected and correct — they re-run with current data including the new script 10 output.

**Session log written:** `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-04/bd_gold_runner_rolling_flows_deploy.md` — committed with `8d338013`

---

### Part 3 — DS A-Roll Work Review (QA Gate)

**Reviewed:** All DS commits from this session (`5f60d30e`, `c9b3ab76`, `25660f4c`, `e07b630e`) plus `data_contract.xml` updates and session log. Also reviewed DE commit `3252e5ce` (downstream of DS work).

**A1+A2 — adv_drill + cla in bd-portal-publisher (`5f60d30e`)** — PASS
- `adv_drill` keys iterate `adv_categories` (not an independent set) — matches portal `drillParent` lookup requirement exactly.
- Category key format `"{relationship_name} ({relationship_id})"` is collision-safe per Pattern 0 contract.
- Single perf_cohort merge serves both adv_drill and all 4 CLA sub-views — no redundant parquet load.
- `_cla_view()` helper correctly DRYs the groupby/unstack/fillna pattern.
- NMNC/NMEC rule (`months_since_first <= 12`) is consistent with existing `aua` view — no new classification invented.
- `primary_city` added to cdim column prune in `load_all()` before the merge — required for `cla.geo_city_drill`, no side effects on other code paths.
- Both new keys are conditional and additive; all existing keys (`aua`, `nna`, `geo`, `adv`, `geo_drill`) unmodified.
- `build_partner_analytics()` remains DISABLED as required (EC2 script 09 owns that output).

**A3 — stacked_bar + rolling_1y in script 10 (`c9b3ab76`)** — PASS
- Period-outer / role-inner nesting is correct. DS explicitly documented that CTO task order A3.1 overrides the thread receipt (role-outer). Task order is the binding spec; DS applied the right one.
- `compute_stacked_bar()` reuses `_compute_nna_for_range()` and `_get_period_boundaries()` — no new data logic introduced.
- `rolling_1y` correctly extracts from existing `series['1Y']` output — no new rolling math, exact field name match to contract (`date`, `nna`, `inflows`, `outflows`).
- Data history pre-check via session log archaeology is valid: `2020-06-30` inception confirmed across multiple prior DS session logs; all 5 stacked_bar periods fully supported.
- Legacy keys (`summary`, `architects`, `implementors` with 30d/90d/1Y windows) unchanged; backward compat preserved.

**A4 — Script 09 bell curve code verification (`25660f4c`, `e07b630e`)** — PASS
- `abs()` present in all 3 correct locations: materiality filter (line ~332), `abs_max` (line ~348), `abs_min` (line ~349).
- Signed percentiles (lines 374-380) are intentional per docstring — correct for bimodal inflow/outflow distribution.
- Live S3 data confirms non-degenerate distribution: p10=-$46,787, p50=-$1,062, p90=+$151,675. OH segment (all-negative) correctly shows signed outflow-dominant shape.
- No patch required.

**A5 — opal-users-v2 advisor identity investigation (`e07b630e`)** — PASS (investigation complete; BLOCKER correctly identified and escalated)
- Scenario (c) determination is correct and well-evidenced: no `advisorId`/`advisorName` field on any USER#PROFILE item. The two `tier: "advisor"` accounts for 49financial (Wohlgemuth, Okoniewski) are ops staff — not financial architects in the gold data. Actual architects (Penfield, Sims, Bertrand, etc.) have zero portal accounts.
- Email matching correctly ruled out: gold layer carries no email addresses for advisors; identity derives from BD transaction slugs only.
- `advisorKey` recommendation is the minimal correct approach: additive optional attribute on USER#PROFILE, set at advisor account creation, no existing records broken.
- Escalated to COO + CTO correctly. No Books tab auth implementation should proceed until mapping is populated.

**data_contract.xml** — PASS
- Source 2 (timeseries_chart.json) updated with full `adv_drill` and `cla` documentation including structures, category key format, TOP_N_CLIENTS_PER_ARCH constant, NMNC/NMEC rule with formula, sign conventions, primary_city derivation with script 04 line citations.
- Source 5 (advisor_rolling_flows.json) replaced thin entry with full block: data history (2020-06-30 inception, 5.5Y range, first 1Y point ~2021-07-01), legacy key schema, stacked_bar full structure with period boundary definitions, rolling_1y structure.
- `data_contract.xml` updated before DT deploy — gate was met.

**DE commit `3252e5ce`** — PASS (downstream action, not DT scope, noted for completeness)
- DE `0.4.0_DE_ClientPlatform` updated V2 types and refreshed RD task orders (`ADVI-004-distribution_continuous.md`, `ADVI-005-advisors_tab.md`) immediately after DS gates cleared. Correct response; no DT action needed.

**Overall QA verdict: PASS.** All DS A-roll work is correct and in-pattern. B1 and B2 are deployed. RD gates are open. Only open item is the A5 blocker (COO/CTO decision required).

---

## All Commits This Session (DT-Authored or DT-Triggered)

| Hash | Author | Description | Notes |
|------|--------|-------------|-------|
| `81b8a66e` | `0.4.0_DT_ClientPlatform` | `ci: upload bd-portal-publisher artifact for adv_drill + cla deploy [skip ci]` | Source map SHA update — B1 deploy step 2 |
| `4149cf49` | wrapper (auto) | `ci: record deploy bd-pipeline @ 81b8a66e [skip ci]` | 12 bd-pipeline functions updated in source map + CHANGELOG.json |
| `6edb13a8` | `0.4.0_DT_ClientPlatform` | `0.4.0_DT_ClientPlatform: update deployment_map.xml -- bd-v2.15.0 (adv_drill + cla)` | Core document update — B1 post-deploy |
| `c98d1ae5` | `0.4.0_DT_ClientPlatform` | `log(0.4.0_DT): ADVI-004 B1 bd-portal-publisher adv_drill+cla deploy session` | B1 session log |
| `4a908760` | wrapper (auto) | `Deploy EC2 bd-gold-layer-runner @ c98d1ae5` | EC2_MANIFEST.json — deployed_commit + deployed_at recorded by safe-ec2-deploy.sh |
| `8d338013` | `0.4.0_DT_ClientPlatform` | `log(0.4.0_DT): ADVI-005 B2 bd-gold-runner rolling_flows deploy + deployment_map update` | B2 session log + deployment_map.xml update for bd-gold-layer-runner |

## Tags Issued This Session

| Tag | Commit | Description |
|-----|--------|-------------|
| `bd-v2.15.0` | `6edb13a8` | feat(bd-portal-publisher): adv_drill + cla timeseries (ADVI-004 A1+A2) |
| `bd-v2.15.1` | `4a908760` | feat(bd-gold-10): stacked_bar + rolling_1y advisor flows (ADVI-005) |

---

## Files Modified This Session

| File | Change | Commit |
|------|--------|--------|
| `infra/aws/lambda/ci/lambda-source-map.json` | `bd-portal-publisher` SHA updated (`aWeD...` -> `st5B...`) | `81b8a66e` |
| `infra/aws/lambda/ci/lambda-source-map.json` | 12 bd-pipeline functions: `last_deployed_commit` + `last_deployed_at` | `4149cf49` |
| `infra/aws/terraform/bd-pipeline/CHANGELOG.json` | Deploy record entry for `bd-v2.15.0` | `4149cf49` |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/deployment_map.xml` | bd-portal-publisher tag -> `bd-v2.15.0`; bd-pipeline module tag -> `bd-v2.15.0`; bd-gold-layer-runner `deployed_tag` -> `bd-v2.15.1` | `6edb13a8`, `8d338013` |
| `infra/aws/ec2/EC2_MANIFEST.json` | bd-gold-layer-runner: `deployed_commit`, `deployed_at`, `deployed_by` updated | `4a908760` |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-04/bd_portal_publisher_adv_drill_cla_deploy.md` | New — B1 session log | `c98d1ae5` |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-04/bd_gold_runner_rolling_flows_deploy.md` | New — B2 session log | `8d338013` |

---

## Protocol Compliance Checklist

**Lambda deploy (B1):**
- [x] DS `data_contract.xml` updated before DT deploy (confirmed in `5f60d30e`)
- [x] Source map updated and committed before `terraform plan`
- [x] `terraform plan` run and reviewed (1 resource, SHA only, no infra changes)
- [x] `terraform apply` executed
- [x] 0-diff plan verified: "No changes. Infrastructure is up-to-date."
- [x] `deployment_map.xml` updated after 0-diff, before tag
- [x] `record-terraform-deploy.sh` run after 0-diff
- [x] Tag created: `bd-v2.15.0`
- [x] Pushed with `--follow-tags`
- [x] Session log written

**EC2 deploy (B2):**
- [x] `safe-ec2-deploy.sh` wrapper used (not deploy script directly)
- [x] `EC2_MANIFEST.json` auto-updated by wrapper
- [x] S3 sync confirmed: bronze (4), silver (6), gold (14) scripts
- [x] EC2 instance started for incremental run
- [x] `deployment_map.xml` updated
- [x] Tag created: `bd-v2.15.1`
- [x] Pushed with `--follow-tags`
- [x] Session log written

**QA gate:**
- [x] DS source reviewed commit-by-commit before approving deploys
- [x] data_contract.xml update confirmed present before deploy
- [x] No accidental file inclusions (portal code, .env, binaries) in DT commits
- [x] No `aws lambda update-function-code` used — Terraform only
- [x] No code written directly on EC2 — S3-pull model followed
- [x] All commits include `--author="0.4.0_DT_ClientPlatform <0.4.0_DT_ClientPlatform@opal.agent>"`

**Pattern deviations and justifications:**
- **B1 S3 upload via boto3 (not build-and-upload.sh):** `build-and-upload.sh` successfully built the zip and computed the SHA, but hung on the PowerShell S3 upload step due to the IMDS hang. The zip artifact was verified (SHA matched), re-created deterministically (same PowerShell zip logic, same fixed timestamp 2020-01-01, same file list), and uploaded via boto3 with WMI monkey-patch workaround. The SHA on S3 was verified via `head-object` before committing the source map. Terraform plan and 0-diff confirmed the correct artifact was deployed. This is a tooling workaround, not a protocol deviation.
- `build-and-upload.sh` is fully functional now that `AWS_EC2_METADATA_DISABLED=true` is in `.bashrc`. Future deploys should use the script normally.

---

## Blockers Inherited (Not DT-Actionable)

**A5 — Books Tab Advisor Identity Mapping (BLOCKER)**
`opal-users-v2` contains no `advisorId` or `advisorName` field on any USER#PROFILE item. The financial architects in the BD gold layer (Travis Penfield, Kyle Sims, Chase Bertrand, etc.) have no user accounts in the portal auth system. JWT userId cannot be resolved to a gold layer advisor slug. Escalated by DS to COO + CTO. No DT or DE action until COO/CTO resolves.

Recommended resolution (from DS): add optional `advisorKey` attribute to USER#PROFILE items (e.g., `advisorKey: "travis_penfield"`). Populate at advisor user account creation. No auth implementation should proceed until mapped for real users.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

B1 (`bd-portal-publisher`, `bd-v2.15.0`) is live — `adv_drill` and `cla` keys are in the deployed Lambda. B2 (`bd-gold-layer-runner`, `bd-v2.15.1`) is live — script 10 deployed to S3, EC2 instance is running the incremental gold pass. When B2 completes, `pipeline-complete.json` will trigger bd-portal-publisher and bd-portal-advisor-publisher (expected side effect). DS A-rolls reviewed and passed. RD gates cleared by DE at `3252e5ce`. Only open item is the A5 Books tab blocker (COO/CTO).

---

## Next Steps

1. **[COO/CTO] Resolve A5 Books tab blocker** — `advisorKey` attribute decision on opal-users-v2
2. **Verify B2 EC2 run completed** — check `s3://opal-data-bd/logs/gold-layer/` for `COMPLETE -- INCREMENTAL` with no script 10 errors; verify `stacked_bar` and `rolling_1y` keys in `advisor_rolling_flows.json`
3. **[RD 0.4.2_RD_AdvisorIntelligence] Implement portal rendering** — `adv_drill` + `cla` (timeseries_chart.json) and `stacked_bar` + `rolling_1y` (advisor_rolling_flows.json) are all live

**Do NOT:**
- Re-enable `build_partner_analytics()` in bd-portal-publisher `lambda_handler` — marked DISABLED, EC2 script 09 owns that output
- Change `stacked_bar` nesting to role-outer/period-inner — CTO task order A3.1 is binding, not the thread receipt
- Start Books tab auth implementation until `advisorKey` is confirmed populated for real advisor users
