# Causality Teardown — Staged Plan Set (RAVC1 for CTO+COO review)

**Author:** 0.5.0_AE_OpalETL · **Date:** 2026-06-11 · **Status:** STAGED — apply gated on CTO+COO GO
**Work order:** 1.0.0_SA_CTO [WORK ORDER — LOW-PRI cleanup] 20260611T213234Z (Andrew-authorized full deprecation)
**Gate:** 4-layer destructive-op gate (name-target-list → blast-radius → saved/reviewable plan → post-verify), trade-recon-teardown template.

## 1. Live census (boto3, 2026-06-11 ~21:53Z) — everything is LIVE, this is a real teardown

| Target | State | Notes |
|---|---|---|
| 8 lambdas `causality-*` | ALL LIVE | last modified 2026-02-03, python3.12 |
| 8 roles `lambda-causality-*-role` | ALL LIVE | inline: CausalityEnginePolicy (×7) / S3AccessPolicy+SecretsManagerPolicy (data-enrichment); attached: AWSLambdaBasicExecutionRole only |
| EventBridge `causality-daily-signals-6am-et` | LIVE, **ENABLED** | cron(0 6 * * ? *) → thematic-signals-generator |
| DDB ×3 (thematic-signals, generations, saved-analyses) | ALL LIVE, **all 0 items** | zero data-loss exposure |
| `/causality/*` on opal-portal-api (f61h681z9g, REST) | **11 resources / 9 methods** LIVE | all 9 integrations point ONLY at causality lambdas (boto3-verified per WO — kuzu graph not trusted for apigw) |

## 2. Divergences from the work order (all verified, none change the goal)

1. **"0 invocations/30d" is wrong for one lambda:** `causality-thematic-signals-generator` fired **90×/30d** — the ENABLED daily rule × ~3 (1 fire + 2 async retries), with its output table at 0 items, i.e. **failing daily**. Strengthens the teardown case (removes daily error noise + small real cost). Other 7 lambdas: 0 invocations/30d confirmed.
2. **"Clean `terraform destroy` of the causality root" is impossible:** the root's S3 backend key (`opal-313476888478-terraform-state/causality/tfstate`) holds **no state file** — the root was never applied. Its config also covers **only the 8 lambda modules** (roles passed as ARN strings; rule/thematic-signals-table/apigw resources in no TF config anywhere). The WO's TF-location map is stale on this point.
3. **Route count is 9 methods / 11 resources** (incl. the two path-only parents `/causality`, `/causality/generate`). Deleting parent resource `71k5lh` cascades all 11.

## 3. Mechanism (what replaces "destroy the root")

| Set | Mechanism | Artifact |
|---|---|---|
| 2 TF-managed tables (generations, saved-analyses; shared-infra root) | saved `-target` destroy plan, **0 add / 0 change / 2 destroy**, rest of shared-infra not refreshed | `infra/aws/terraform/shared-infra/causality-tables-destroy.tfplan` (local; `terraform show` verified — names exactly the 2 tables) |
| Everything TF-unmanaged (8 lambdas, 8 roles, rule, thematic-signals table, 11 apigw resources + stage redeploys) | gated boto3 script, dry-run-first; `--execute` requires `GO_CAUSALITY_TEARDOWN=1` env (set only on CTO+COO GO); `--verify` = post-verify | `infra/aws/terraform/causality/teardown/causality_teardown.py` + non-causality route snapshot (38 paths) |

Import-to-destroy was considered and rejected: authoring + importing ~30 resources including method/integration resources **on the live production REST API** is more state-surgery risk than a scoped, reviewable deletion script.

**Order:** rule (targets→rule) → `/causality` resource tree → **immediate create_deployment to BOTH stages `prod` + `production`** → 8 lambdas → 8 roles (inline deleted, AWSLambdaBasicExecutionRole **detached not deleted**, role deleted) → thematic-signals table → shared-infra saved plan apply → post-verify.

## 4. Protect list (structurally absent from both artifacts)

KMS `86cc6c40-2387-4446-b7e1-de79392e06b3` · `s3://opal-data-news-av` · shared secrets · `AWSLambdaBasicExecutionRole` (AWS-managed, detach only). The boto3 script contains **no** S3/KMS/Secrets delete calls; dry-run + post-verify assert all four intact. Dry-run result 2026-06-11: **0 problems**.

## 5. Post-verify (script `--verify`)

All 25 AWS-side targets GONE; `/causality*` resource count 0; opal-portal-api non-causality route set **byte-identical to the 38-path snapshot**; protect-list intact; both saved-plan tables gone + shared-infra plan returns 0-diff.

## 6. Repo cleanup (same window as apply, not before GO)

- `infra/aws/lambda/ci/lambda-source-map.json`: remove 8 causality entries (Rule 4)
- `infra/aws/terraform/causality/`: remove root config (main.tf + lock; teardown/ artifacts retained for audit) — prevents future re-apply of a deleted feature
- `infra/aws/lambda/causality_*` (8 source dirs): propose removal — CTO call at review
- Empty S3 state key `causality/tfstate`: nothing to clean (no object exists)

## 7. Adjacent facts surfaced (no action in this teardown)

- **`market-updates` DDB table (market-overview module)** is fed by causality-market-update-generator (0 invocations/30d → already not being fed). Table stays (market-overview-owned); the market-overview page keeps serving whatever records exist. Flag if the page should drop the section — DE scope.
- **Portal FE dead code** (`causality-endpoints.ts` etc.): flagged to DE per WO, untouched here.
- `lambda-causality-trade-idea-generator-role` dead trade-recon invoke-grant: base-AE strip SKIPPED (role in destroy set — coordinated via COO 2026-06-11).
- Graph: comp-blast on causality lambdas shows no extracted downstream edges (lower-bound only; pre-WAVE-4 graph has no apigw nodes — boto3 census is the authoritative apigw source, per WO).
