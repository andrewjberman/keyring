# BMKAUD WS-4 — Two TF Plans (author + analysis; APPLIES HELD for COO+CTO GO)

**Lane:** 0.7.0_AE_CloudOps · **Audit:** `docs/briefs/benchmark-yang-truth-audit-20260601.md` · **Status:** PLANS AUTHORED, NOT APPLIED.
Both legs follow author→`terraform plan`→RAVC2→(GO)→`safe-apply`+HALTGT. Nothing committed to live `.tf` until GO (avoids an ungated apply by another workspace run). Full technical analysis on both sides below.

═══════════════════════════════════════════════════════════════════════
## LEG 1 — `smartx-model-monthly-pull` FULL RETIREMENT (a destroy)
═══════════════════════════════════════════════════════════════════════

### 1.1 Current state (what exists today)
`infra/aws/terraform/smartx-pipeline/model-perf-pull.tf` defines a standalone scheduled SmartX pull (YALP_MDSRC.B2). Resources in TF state:
| resource | id | purpose |
|---|---|---|
| `aws_lambda_function.model_monthly_pull` | smartx-model-monthly-pull | pulls SmartX model perf → writes `_smartx_model_monthly.json` |
| `aws_cloudwatch_log_group.model_monthly_pull` | /aws/lambda/smartx-model-monthly-pull | logs |
| `aws_iam_role.model_monthly_pull` (+ `_basic` attach + `aws_iam_role_policy.model_monthly_pull`) | exec role | SM read + `s3:PutObject json/benchmarks/*` |
| `aws_iam_role.model_monthly_scheduler` (+ `aws_iam_role_policy.model_monthly_scheduler`) | scheduler role | invoke the lambda |
| `aws_scheduler_schedule.model_monthly_pull` | default/smartx-model-monthly-pull-daily | `cron(35 9 * * ? *)` ET — **currently DISABLED** (WS-0 freeze, f38353b0f) |
| `data.aws_s3_object.model_monthly_pull_artifact` | (data source) | reads the zip from artifact bucket |
Plus: source-map entry `smartx-model-monthly-pull` (lines ~2205-2217) + script `data/smartx/scripts/pull_smartx_model_monthly_performance.py` (DS-CP lane).

### 1.2 Why retire (orphan justification — both sides)
- **FOR retirement:** Post-revert (`80224d674`) the benchmark producer is pure-yang and reads NEITHER sidecar. Repo-wide grep for `_smartx_model_monthly`/`_smartx_model_daily` → ZERO live consumers (only docs/logs/source-map/the producer itself). The lambda fires daily, calls the SmartX API, and writes 2 unread files → dead infra + an ongoing external API pull + a standing write path into the audited S3 surface (a latent re-clobber vector). Andrew's governing principle: Benchmark data is Yang-PKL-only; a live SmartX writer to `json/benchmarks/` contradicts that even when unread.
- **AGAINST / risk of retiring:** (a) If a hidden consumer exists that grep missed (e.g., a runtime-constructed key, an external/portal fetch by literal URL) it would 404 post-destroy. Mitigation: grep was exhaustive (repo + the FE benchmarks.ts reads only `benchmark_returns/model_portfolio_benchmarks/model_portfolio_timeseries`, not the sidecars); CVO WS-5 to independently confirm. (b) Loss of the SmartX-realized series if a future "model vs realized" feature wants it — but that's explicitly out-of-scope per Andrew's Yang-truth ruling; can be re-introduced from git if ever needed. (c) The 2 stale sidecars remain in S3 after destroy (destroy removes the WRITER, not the objects) — recommend a separate explicit `aws s3 rm` of the 2 sidecars OR leave as frozen evidence.

### 1.2-bis DAILY-ORPHAN CONFIRMED (CTO review item 2 — RESOLVED)
There is NO separate "B3 daily" producer. `pull_smartx_model_monthly_performance.py` (the smartx-model-monthly-pull lambda) writes BOTH sidecars in one run: `_smartx_model_monthly.json` (`OUT_KEY`) AND `_smartx_model_daily.json` (`OUT_KEY_DAILY`, L98; both emitted at L422/462; `output_keys=[OUT_KEY,OUT_KEY_DAILY]` L466). So LEG 1's retirement of smartx-model-monthly-pull **retires BOTH sidecar producers** — no LEG 1b needed. (Census doc `bmkaud_benchmarks_writer_census.md` row B.)

### 1.3 Proposed change
1. Remove `infra/aws/terraform/smartx-pipeline/model-perf-pull.tf` (entire file — it contains ONLY these resources). Retires the monthly+daily sidecar producer in one destroy.
2. Remove the `smartx-model-monthly-pull` source-map entry (AE lane).
3. Route script removal (`data/smartx/scripts/pull_smartx_model_monthly_performance.py`) to DS-CP (Rule 13 data-script lane) — coordinate, not my commit.
4. (Optional, separate) `aws s3 rm` the 2 stale sidecars after CVO sign-off.

### 1.4 `terraform plan` (captured, file-removed)
```
Plan: 0 to add, 0 to change, 8 to destroy.
  - aws_lambda_function.model_monthly_pull
  - aws_cloudwatch_log_group.model_monthly_pull
  - aws_iam_role.model_monthly_pull
  - aws_iam_role_policy.model_monthly_pull
  - aws_iam_role_policy_attachment.model_monthly_pull_basic
  - aws_iam_role.model_monthly_scheduler
  - aws_iam_role_policy.model_monthly_scheduler
  - aws_scheduler_schedule.model_monthly_pull
```
No `~`/`+`. Pure destroy of the 8 orphan resources. No other smartx-pipeline resource touched (verified: the refreshed jwt_refresher/rest_pull schedules are untouched).

### 1.5 Blast radius / rollback
- **Blast radius:** ZERO live consumers (proven). Destroying does not touch the yang producer, the yang pipeline, the smartx-rest-pull/jwt-refresher family, or any read path. The artifact zip remains in `opal-313476888478-lambda-artifacts` (so the lambda is re-creatable).
- **Rollback:** `git revert` the removal commit + `terraform apply` re-creates all 8 (idempotent; zip still in S3). Fully reversible.
- **Pre-apply gate:** zero-consumer confirmation (done; CVO WS-5 to corroborate) → RAVC2 GO → `safe-apply` (HALTGT). Destroy is irreversible-at-the-AWS-layer for the moment but re-creatable from code.

═══════════════════════════════════════════════════════════════════════
## LEG 2 — `opal-data-portal-v2` POLICY IMPORT + ANTI-CLOBBER DENY
═══════════════════════════════════════════════════════════════════════

### 2.1 Current state (the deploy-ops gap)
`opal-data-portal-v2` is the CloudFront origin for portal JSON. Its bucket policy is **UNMANAGED by Terraform** — no `aws_s3_bucket`/`aws_s3_bucket_policy` resource exists anywhere in the repo (only IAM grants + the CF origin config in `portal-auth/`). The LIVE policy (captured verbatim):
```json
{ "Version":"2012-10-17","Statement":[
  {"Sid":"AllowCloudFrontOAI","Effect":"Allow",
   "Principal":{"AWS":"arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity EU39UXW7CMSI5"},
   "Action":"s3:GetObject","Resource":"arn:aws:s3:::opal-data-portal-v2/*"},
  {"Sid":"AllowCloudFrontOACPublicData","Effect":"Allow",
   "Principal":{"Service":"cloudfront.amazonaws.com"},"Action":"s3:GetObject",
   "Resource":["arn:aws:s3:::opal-data-portal-v2/json/*","arn:aws:s3:::opal-data-portal-v2/json-tiered/*"],
   "Condition":{"StringEquals":{"AWS:SourceArn":"arn:aws:cloudfront::313476888478:distribution/EVTSA9VEHNZVH"}}}
]}
```
Both statements are `s3:GetObject` (reads). Bringing this under TF + adding a write-only Deny is the durable MDPF anti-clobber control (IAM-A) AND closes the BMKAUD deploy-ops-rigor gap.

### 2.2 Proposed change (2-phase, in a managed-import pass)
**Phase A — import + exact replication (0-diff proof):** add to `shared-infra/s3.tf`:
```hcl
resource "aws_s3_bucket_policy" "opal_data_portal_v2" {
  bucket = "opal-data-portal-v2"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      { Sid = "AllowCloudFrontOAI", Effect = "Allow",
        Principal = { AWS = "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity EU39UXW7CMSI5" },
        Action = "s3:GetObject", Resource = "arn:aws:s3:::opal-data-portal-v2/*" },
      { Sid = "AllowCloudFrontOACPublicData", Effect = "Allow",
        Principal = { Service = "cloudfront.amazonaws.com" }, Action = "s3:GetObject",
        Resource = ["arn:aws:s3:::opal-data-portal-v2/json/*","arn:aws:s3:::opal-data-portal-v2/json-tiered/*"],
        Condition = { StringEquals = { "AWS:SourceArn" = "arn:aws:cloudfront::313476888478:distribution/EVTSA9VEHNZVH" } } },
    ]
  })
}
```
Then `terraform import aws_s3_bucket_policy.opal_data_portal_v2 opal-data-portal-v2` → `terraform plan` MUST show **No changes** (proves byte-exact OAC replication; CTO review gate).

**Phase B — add the write-only Deny** (append to Statement, after 0-diff proven):
```hcl
{ Sid = "DenyNonRunnerWriteMdpfAggregateAua", Effect = "Deny",
  Principal = "*", Action = ["s3:PutObject","s3:DeleteObject"],
  Resource = "arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/aggregate_aua/*",
  Condition = { ArnNotLike = { "aws:PrincipalArn" = [
    "arn:aws:sts::313476888478:assumed-role/mdpf-daily-runner-ec2-role/*",
    "<NARROW break-glass admin ARN — TBD, confirm NOT a routine dev/agent cred>" ] } } }
```
**Phase B also adds the BENCHMARK Deny (CTO review 154xZ — Andrew's actual lock-down ask; SEPARATE canonical writer = the yang lambda role, NOT mdpf-runner):**
```hcl
{ Sid = "DenyNonYangWriteBenchmarks", Effect = "Deny",
  Principal = "*", Action = ["s3:PutObject","s3:DeleteObject"],
  Resource = "arn:aws:s3:::opal-data-portal-v2/json/benchmarks/*",
  Condition = { ArnNotLike = { "aws:PrincipalArn" = [
    "arn:aws:sts::313476888478:assumed-role/yang-pipeline-lambda-role/*",
    "<NARROW break-glass admin ARN>" ] } } }
```
Canonical writer confirmed (live `get-function-configuration`): yang-model-portfolio-benchmarks runs as **`yang-pipeline-lambda-role`** (shared by all yang-pipeline lambdas — all canonical yang writers; excepting it permits the yang pipeline while structurally DENYING the smartx-monthly/daily sidecar writer [B], the EC2 dual-writer [C], smartx-ingestion [D], news [E], AND any rogue/manual/dev-cred). This is the lock Andrew asked for: after apply, ONLY the yang role (+break-glass) can write `json/benchmarks/*`.

`terraform plan` then shows **+2 Deny statements (benchmarks + mdpf-aggregate), OAC statements unchanged**. Both Denys coexist in the one imported policy.
- **Benchmark Deny (Andrew's directive — ship with this batch):** Resource = `json/benchmarks/*`, except yang-pipeline-lambda-role.
- **MDPF aggregate Deny (CTO-ratified):** Resource = `platinum/mdpf/aggregate_aua/*`, except mdpf-daily-runner-ec2-role.
- **MDPF C-scope (fast-follow):** extend to `platinum/mdpf/aggregate_aua_timeseries.json` + (only after MDPF leg-1a/1b make the runner the legit json/mdpf writer) `json/mdpf/*`.

### 2.3 Technical correctness notes (both sides)
- **Write-only is the safety guarantee:** Action set = `{PutObject,DeleteObject}` ONLY, never `GetObject`. A Deny that excludes GetObject is structurally incapable of affecting CloudFront OAC/OAI reads — the portal cannot break from this Deny by construction (CTO condition 1).
- **`ArnNotLike` + assumed-role session ARN:** EC2 role credentials present as `arn:aws:sts::<acct>:assumed-role/<role>/<session>`, NOT the bare role ARN — hence `ArnNotLike` against `assumed-role/mdpf-daily-runner-ec2-role/*` (wildcard session). Using `NotPrincipal` is error-prone with Deny (AWS docs warn) → use `Condition` (CTO condition 2). Alternative: `aws:userId <role-unique-id>:*`.
- **Not theater:** the 5/29 clobber principal is un-attributable (no CloudTrail data events / no S3 access logging) but the Deny is an allow-LIST (runner + narrow break-glass) → ANY un-named dev/agent cred is OUTSIDE by construction. MUST confirm the break-glass ARN is a rarely-used admin, NOT everyday dev/agent creds (else it re-permits the clobber class).
- **Post-apply proof required:** a live write from the runner role SUCCEEDS + a write from a non-whitelisted dev cred is DENIED (CTO condition 4).

### 2.4 Blast radius / rollback (LEG 2)
- **Blast radius:** HIGH-sensitivity (shared CF origin) but bounded by write-only scope. Risks: (a) byte-imperfect OAC replication on import → an apply could rewrite the live policy and break portal reads — MITIGATED by the Phase-A 0-diff gate (we do NOT proceed to B unless import shows No changes). (b) Leaving the imported resource in shared-infra state means the next `shared-infra apply` by any agent would push pending HCL — so the Deny HCL must NOT be committed until GO, and the apply must be the SAME-pass gated apply. (c) S3 allows ONE bucket policy → this resource OWNS the policy once imported; any out-of-band policy edit would drift.
- **Rollback:** `terraform state rm aws_s3_bucket_policy.opal_data_portal_v2` un-manages it (live policy untouched); or revert the Deny statement + apply to restore OAC-only. The live policy is captured verbatim in this doc + the WS-0 evidence for reconstruction.
- **Pre-apply gate:** CTO architecture sign-off on (i) the import-and-manage-in-shared-infra approach, (ii) the exact break-glass ARN, (iii) the A-vs-C scope. Then import → 0-diff proof → add Deny → plan → RAVC2 the +Deny plan → `safe-apply` (HALTGT) → post-apply allow/deny verification.

### 2.5 Sequencing across both legs + MDPF
- LEG 1 (retirement) is independent — can apply on its own GO.
- LEG 2 Phase A (import + OAC, 0-diff) is a safe no-op bring-under-management — low risk, CTO-gated.
- LEG 2 Phase B (Deny) A-scope ships on CTO GO; C-scope waits on MDPF leg-1a (DS~B rollup redeploy) + leg-1b (DONE, runner json/mdpf grant) so the runner is the legit scheduled json/mdpf writer before any json/mdpf Deny.
