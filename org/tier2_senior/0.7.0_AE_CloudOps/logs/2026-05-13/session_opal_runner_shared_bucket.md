# AE 0.7.0 Session Log — opal-runner-shared bucket creation + cross-pipeline telemetry consolidation
**Date:** 2026-05-13
**Agent:** 0.7.0_AE_CloudOps
**Trigger:** Andrew direct — "you were working on some telemetry streaming analytics for our runners, please make sure that is in some shared cloud location that all EC2s draw against"
**Scope:** BD prod + BD qa + INF prod gold-layer runners (3 EC2s)

---

## TL;DR

Created new `opal-runner-shared` S3 bucket as single canonical location for cross-pipeline EC2 runner code. Seeded with `gold_prof.py` (yesterday's telemetry profiler work) + the existing `opal-telemetry.sh` suite (April 2026 vintage). Granted least-privilege read on both pipeline gold-runner roles. Updated runtime runner scripts (BD `run-gold-layer.sh` + INF `orion-gold-dispatch.sh`) to pull `gold_prof.py` from the new bucket on every boot. Legacy per-pipeline copies retained as fallback for safe-deploy backout.

---

## Problem Statement

Before this session, gold_prof.py existed as duplicate copies:
- `s3://opal-data-bd/code/gold/gold_prof.py` (7499 B, 2026-05-12 14:44Z) — pulled by BD prod + qa via `aws s3 sync code/gold/`
- `s3://opal-data-inf/code/gold/gold_prof.py` (7499 B, 2026-05-12 14:44Z) — pulled by INF dispatcher's `sync_scripts()`

Both copies were identical at deploy time but could drift independently if either pipeline's deploy flow ran without the other being kept in sync. Andrew's directive was to eliminate the duplicate-copy pattern.

Additionally `opal-telemetry.sh` + supporting files were at `s3://opal-data-bd/code/shared/` (April 2026 deploy) and only BD runners pulled them. INF runner had no telemetry-harness suite installed at all.

---

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| New dedicated bucket (`opal-runner-shared`) vs reuse `opal-data-bd` | Andrew picked option B (new dedicated). Clean semantic separation between pipeline DATA buckets and shared CODE bucket. Per-bucket IAM stays cleanly scoped. |
| Layout: preserve existing `code/gold/` + `code/shared/` prefixes | Compatibility — runner scripts that previously did `aws s3 cp .../code/shared/opal-telemetry.sh` keep the same key suffix; only the bucket name changes. Minimizes script-edit surface. |
| Override-pattern in runtime scripts (legacy-fallback safe) | Runtime scripts ADD an `aws s3 cp s3://opal-runner-shared/...` AFTER the legacy per-pipeline sync. If the shared pull succeeds, it overwrites the legacy copy with the canonical version. If the shared pull fails (transient outage, IAM propagation lag, etc.), the legacy copy from the per-pipeline sync remains in place — runner continues with the older but functional binary. After ~1 day of confirmed production pulls, follow-up commit will remove the legacy copies. |
| Read-only IAM (no PUT from runners) | Only humans (deploy scripts) push to `opal-runner-shared`. Eliminates accidental cross-pipeline write contamination. |
| Skip `record-terraform-deploy.sh` on bd-pipeline + inf-pipeline | These IAM-only deploys don't touch Lambda code. Running record-deploy would invoke the `ADHC_DRIFTD.001` sweep-bug — it would overwrite today's stabilized `last_deployed_commit` values across ALL Lambdas in each pipeline (~50+ Lambdas combined), requiring per-Lambda manual restoration. Defer record-deploy invocation until DRIFTD.001 ships. |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read shared-infra TF + identify gold-runner IAM roles in bd-pipeline + inf-pipeline | bd-pipeline uses `aws_iam_role.bd_exporter` (`bd-exporter-ec2-role`); inf-pipeline uses `aws_iam_role.inf_gold_layer` (`inf-gold-layer-ec2-role`). BD prod + qa share the same role (per `iam.tf` comment line 345-348). |
| 2 | Edit `infra/aws/terraform/shared-infra/main.tf` | Added 4-resource block for `aws_s3_bucket.runner_shared` (bucket + versioning + AES256 + public-access-block) |
| 3 | `terraform plan` shared-infra | Plan: 4 to add, 0 to change, 0 to destroy |
| 4 | safe-commit.sh | `534c30885` — `infra(shared-infra): add opal-runner-shared S3 bucket...` |
| 5 | `terraform apply` shared-infra | `Apply complete! Resources: 4 added, 0 changed, 0 destroyed.` |
| 6 | `terraform plan` post-apply | 0-diff confirmed |
| 7 | Seed bucket with telemetry suite + gold_prof.py | 6 files uploaded: `code/gold/gold_prof.py` (from local repo source) + 5 telemetry-suite files (copied from `s3://opal-data-bd/code/shared/`) |
| 8 | Edit `infra/aws/terraform/bd-pipeline/iam.tf` | Added `aws_iam_role_policy.bd_exporter_runner_shared` (s3:GetObject + ListBucket on opal-runner-shared) |
| 9 | Edit `infra/aws/terraform/inf-pipeline/iam.tf` | Added `aws_iam_role_policy.inf_gold_layer_runner_shared` (same pattern) |
| 10 | safe-commit.sh (both files) | `edbfab618` — `infra(bd-pipeline + inf-pipeline): IAM grant — opal-runner-shared read for gold-runner roles` |
| 11 | `terraform apply -target` bd-pipeline | 1 added, post-apply 0-diff |
| 12 | `terraform apply -target` inf-pipeline | 1 added, post-apply 0-diff |
| 13 | Verify via `aws iam list-role-policies` + `get-role-policy` | Both `runner-shared-read` policies present on AWS with correct least-privilege statement |
| 14 | Edit `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh` | Added `aws s3 cp s3://opal-runner-shared/code/gold/gold_prof.py "$SCRIPTS_DIR/gold_prof.py"` after legacy sync. Affects BOTH BD prod + BD qa (qa pulls same run-gold-layer.sh from `s3://opal-data-bd/code/runner/`). |
| 15 | Edit `data/orion/scripts/gold/orion-gold-dispatch.sh` | Same override pattern inside `sync_scripts()`. Affects INF prod. |
| 16 | safe-commit.sh | `4c2afbe32` — `runner(BD prod+qa + INF prod): pull gold_prof.py from canonical opal-runner-shared` |
| 17 | Push to origin/CLOUD | `252c6c608..4c2afbe32 CLOUD -> CLOUD` |
| 18 | Deploy updated scripts to S3 source locations | `s3://opal-data-bd/code/runner/run-gold-layer.sh` (6834 B, 5x `opal-runner-shared` strings) + `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` (41005 B, 4x `opal-runner-shared` strings) |
| 19 | Tag all 3 pipelines | `shared-infra-v1.10.0` + `bd-v2.24.8` + `inf-pipeline-v1.7.55` |
| 20 | `git push --follow-tags` | All 3 tags pushed |

---

## Verification

### Bucket state

```
$ aws s3 ls s3://opal-runner-shared/code/ --recursive
2026-05-13 16:03:14       7499 code/gold/gold_prof.py
2026-05-13 16:03:16      10886 code/shared/opal-telemetry.sh
2026-05-13 16:03:18      10090 code/shared/opal_telemetry.py
2026-05-13 16:03:22        162 code/shared/telemetry-sync.service
2026-05-13 16:03:20       1690 code/shared/telemetry-sync.sh
2026-05-13 16:03:24        163 code/shared/telemetry-sync.timer
```

### IAM

```
$ aws iam list-role-policies --role-name bd-exporter-ec2-role
  ... runner-shared-read ...  <- new
$ aws iam list-role-policies --role-name inf-gold-layer-ec2-role
  ... runner-shared-read ...  <- new
```

Both policies authorize `s3:GetObject` + `s3:ListBucket` on `arn:aws:s3:::opal-runner-shared` + `arn:aws:s3:::opal-runner-shared/*`. Least-privilege.

### Terraform 0-diff post-apply

| Module | Plan post-apply |
|--------|-----------------|
| shared-infra | No changes. Your infrastructure matches the configuration. |
| bd-pipeline (targeted) | No changes. |
| inf-pipeline (targeted) | No changes. |

### Runtime scripts deployed to S3

```
$ aws s3api head-object --bucket opal-data-bd --key code/runner/run-gold-layer.sh
2026-05-13T20:08:54Z 6834 bytes
$ aws s3 cp s3://opal-data-bd/code/runner/run-gold-layer.sh - | grep -c opal-runner-shared
5
$ aws s3api head-object --bucket opal-data-inf --key code/gold/orion-gold-dispatch.sh
2026-05-13T20:08:56Z 41005 bytes
$ aws s3 cp s3://opal-data-inf/code/gold/orion-gold-dispatch.sh - | grep -c opal-runner-shared
4
```

Each runner's self-update mechanism (BD prod via the systemd-fired boot script, BD qa same, INF via run-gold-layer.sh line 50) will pull the updated script on next boot and execute it.

---

## Tags Deployed

| Pipeline | Tag | Commit |
|----------|-----|--------|
| shared-infra | `shared-infra-v1.10.0` | `534c30885` |
| bd-pipeline | `bd-v2.24.8` | `edbfab618` |
| inf-pipeline | `inf-pipeline-v1.7.55` | `edbfab618` |

---

## Open Items Post-Session

| Item | Status |
|------|--------|
| Empirical verification on next runner boot | Pending — first boot after this commit will pull `gold_prof.py` from new bucket and log "gold_prof.py pulled from opal-runner-shared OK" to the runner log. Will know in tomorrow's EventBridge fire (~9 AM ET for BD prod, on-demand for QA). |
| Legacy copy removal | DEFERRED — `s3://opal-data-bd/code/gold/gold_prof.py` and `s3://opal-data-inf/code/gold/gold_prof.py` remain as fallback. Remove after empirical confirmation that opal-runner-shared pulls succeed in production (~1 day window). Surface as follow-up TO if Andrew wants explicit cleanup. |
| setup-instance.sh on BD prod + qa (telemetry suite pull from `${S3_BUCKET}/code/shared/`) | NOT changed in this session. Currently runs only on first launch; affects future fresh AMIs/launches, not running instances. Existing instances have the suite installed from their original setup. Leaving for future migration scope (e.g., next AMI bake or instance-pool refresh). |
| record-terraform-deploy.sh invocation for the 3 pipelines | DEFERRED — skipping until ADHC_DRIFTD.001 (sweep-commit fix) ships. Running record-deploy now would trample today's stabilized `last_deployed_commit` values across the entire bd-pipeline + inf-pipeline Lambda sets, requiring manual restoration per Lambda. CHANGELOG.json entries for shared-infra-v1.10.0 + bd-v2.24.8 + inf-pipeline-v1.7.55 will be backfilled in the same DRIFTD remediation wave. |
| QA runner same-script confirmation | BD qa pulls run-gold-layer.sh from same S3 source as BD prod (`s3://opal-data-bd/code/runner/run-gold-layer.sh` — confirmed in setup-instance.sh:41). Single source-of-truth means my edit reaches both BD instances via one S3 push. |

---

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| `comp-iam service smartx-ingestion-lambda` (legacy from prior TO-3) | Reference for pattern | PASS |
| Manual `aws iam list-role-policies` + `get-role-policy` | Post-apply verification on both pipelines | Both `runner-shared-read` policies confirmed on AWS, statement content matches TF |
| `terraform plan` post-apply | All 3 modules | 0-diff confirmed |

---

## RAVC Trail

| RAVC | Direction | Time (approx) | Content |
|------|-----------|----------------|---------|
| Andrew direct (UI) | Andrew → AE 0.7 | ~19:30Z | "make sure that is in some shared cloud location that all EC2s draw against" |
| AskUserQuestion | AE 0.7 → Andrew | ~19:35Z | 3 options for bucket choice |
| Andrew direct (UI) | Andrew → AE 0.7 | ~19:36Z | Option B selected (new dedicated bucket) |
| Scope clarification | Andrew direct | ~19:38Z | "for now just having the bd gold runners (prod and qa) and the inf gold runner is enough" — INF qa runner excluded |
| Session log (this) | AE 0.7 → repo | ~20:15Z | Detailed deliverable trail |

---

## Commit Trail

```
4c2afbe32 runner(BD prod+qa + INF prod): pull gold_prof.py from canonical opal-runner-shared
edbfab618 infra(bd-pipeline + inf-pipeline): IAM grant — opal-runner-shared read for gold-runner roles
534c30885 infra(shared-infra): add opal-runner-shared S3 bucket for cross-pipeline EC2 runner code
```

Tags: `shared-infra-v1.10.0`, `bd-v2.24.8`, `inf-pipeline-v1.7.55`.

## Session Status: COMPLETE — opal-runner-shared bucket LIVE, both pipeline IAM roles granted, BD prod+qa + INF prod runtime scripts updated + deployed to S3 source locations; next-boot empirical verification pending
