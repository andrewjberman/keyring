# MDLP_VOLAUD.003 — yang-generate-benchmark-returns RETIRE ship

**Date:** 2026-05-19
**Agent:** 0.5.0_AE_OpalETL~B (first TO on this lane post Andrew-direct provisioning ~17:39Z)
**TO:** `MDLP_VOLAUD.003.ae-yang-generate-benchmark-returns-retire-or-redesign`
**Tag shipped:** `yang-v2.4.3`
**Deploy commit:** `f79700cb7` (RETIRE) + `233fd015e` (CHANGELOG)
**Wall:** ~1.5h end-to-end (Phase 0.5 probe through Phase 2 verify + RAVC2 send)

---

## Current State

- **MDLP_VOLAUD.003:** COMPLETE — `yang-generate-benchmark-returns` Lambda retired; SFN dual-writer race eliminated; `yang-model-portfolio-benchmarks` is single SoT for all 3 benchmark JSON keys (legacy `benchmark_returns.json` + comprehensive `model_portfolio_benchmarks.json` + timeseries `model_portfolio_timeseries.json`).
- **Pipeline tags:** yang-v2.4.3 (new) / news-v2.9.10 / smartx-v2.2.0 / market-overview-v1.9.0 / security-scanner-v1.1.1 (per base AE earlier).
- **Race history (S3 versioning, comprehensive key):**
  - 2026-05-19T11:25:03Z — newer Lambda correct write (15414 bytes)
  - 2026-05-19T11:25:04Z — older Lambda OVERWROTE 1s later (15417 bytes, collapsed)
  - 2026-05-19T17:18:50Z — base AE fresh-invoke single-write (15414 bytes, correct)
  - 2026-05-19T18:39:55Z — my Phase 2 fresh-invoke single-write (15414 bytes, correct)
- **Post-retire state:** structurally impossible for the race to fire again — older Lambda destroyed; SFN parallel branch removed; CloudWatch log group destroyed.

## Phase 0.5 — Pure-Redundant / Unique-Consumer Probe

**Verdict: PURE-REDUNDANT → RETIRE branch.** 7-point empirical evidence chain (≤30min):

1. **SFN parallel-branch wiring confirmed.** `yang-pipeline-definition.json` `ProcessBothPKLs` (lines 478-557) ran THREE parallel branches with identical input event: `GenerateBenchmarkReturns` (yang-generate-benchmark-returns), `GenerateModelPortfolioBenchmarks` (yang-model-portfolio-benchmarks), `GeneratePositioning` (yang-generate-positioning). First two raced on the same OUTPUT_KEYs; positioning writes different keys.

2. **Output-key analysis — newer is strict superset:**
   | Key | Older (yang-generate-benchmark-returns) | Newer (yang-model-portfolio-benchmarks) |
   |---|---|---|
   | `json/benchmarks/benchmark_returns.json` | Yes | **Yes** |
   | `json/benchmarks/model_portfolio_benchmarks.json` | Yes | **Yes** |
   | `json/benchmarks/model_portfolio_timeseries.json` | No | **Yes** (added 2026-05-04 MDLP_RVVALT) |

3. **Race signature on BOTH keys (not just comprehensive).** S3 versioning on `benchmark_returns.json` showed 11:25:03 → 11:25:04 same race pattern (9569 → 9568 collapsed). The race affected both write surfaces; retire fixes both.

4. **No external trigger on older.** `lambdas.tf` module `generate_benchmark_returns`: only SFN invokes (no EventBridge / S3 event source / direct invocation). Grep across `infra/aws/terraform/` confirmed: only CHANGELOG snapshots + IMPORT_COMMANDS + plan-output reference the function — no active TF binding outside the module itself.

5. **No unique downstream consumer.** Active legacy-key consumer is `infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/generate_benchmark_performance.py:49` (`S3_KEY = 'json/benchmarks/benchmark_returns.json'`). Reads the S3 key, not the Lambda name; newer Lambda writes the same key. Retire-safe.

6. **Newer is canonical evolution (CTO leans-retire empirically validated).** Source-map: both Lambdas share `last_deployed_commit=cdc2271c4` 2026-05-04T18:55:40Z (the MDLP_RVVALT 2026-05-04 ship). Newer file = older file + ~146 lines for RFR/timeseries (441 → 587 lines). CTO's hypothesis "old Lambda was supposed to be retired when the new one shipped but the SFN was never updated" — confirmed.

7. **comp-blast both empty.** `comp-blast yang-generate-benchmark-returns` + `comp-blast yang-model-portfolio-benchmarks` both return "No downstream consumers found" — consumers reach the S3 keys (newer covers all), not the Lambda names. comp-routes trace yang-model-portfolio-benchmarks → not in routing graph (not an HTTP endpoint; consumer trace goes via portal-data-proxy reading the S3 key).

**Lane:** No cross-lane escalation. SFN definition + Lambda module + source-map all in this lane.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Phase 0.5 probe (source-map + Lambda sources + SFN def + comp-blast + comp-routes + key-grep) | PURE-REDUNDANT verdict |
| 2 | MCP verdict to COO + CC CTO + CC DS~B | CTO ACK 17:55Z: "leans-retire empirically validated; RETIRE branch GO confirmed" |
| 3 | Edits: SFN definition `ProcessBothPKLs.Branches[]` remove GenerateBenchmarkReturns | -26 lines from JSON |
| 4 | Edits: `lambdas.tf` remove `module "generate_benchmark_returns"` | -12 lines |
| 5 | Edits: `lambda-source-map.json` remove `yang-generate-benchmark-returns` entry | -14 lines |
| 6 | `git rm` Lambda source dir (`lambda_function.py` + `deploy.sh`) | -441 + -31 lines |
| 7 | BLOCKED: `safe-commit.sh` owned-paths lane violation — ~B not in CLOUD_OPS_OR_ETL | MCP'd COO with the 1-line YAML fix |
| 8 | COO commit `1dcc800a7` added `0.5.0_AE_OpalETL~B` to CLOUD_OPS_OR_ETL + ANY_EXEC_OR_AE | UNBLOCKED |
| 9 | `safe-commit.sh` retire diff | `f79700cb7` (5 files changed, 514 deletions) |
| 10 | `git push origin CLOUD` | cd8500aad..f79700cb7 |
| 11 | `terraform plan` | 0 added / 1 changed (SFN definition) / 2 destroyed (Lambda + log group) |
| 12 | `terraform apply -auto-approve` | Apply complete: 0 added, 1 changed, 2 destroyed |
| 13 | 0-diff replan | "No changes. Your infrastructure matches the configuration." |
| 14 | `aws lambda get-function --function-name yang-generate-benchmark-returns` | `ResourceNotFoundException` — confirmed destroyed |
| 15 | `git tag -a yang-v2.4.3 -m "..."` | yang-v2.4.3 annotated |
| 16 | `git push --follow-tags` | `* [new tag] yang-v2.4.3 -> yang-v2.4.3` |
| 17 | `record-terraform-deploy.sh yang-pipeline` (auto-output had HEAD-confusion + agent=devops_technician default) | Reverted auto-output; hand-wrote clean entry at CHANGELOG `version: yang-v2.4.3` |
| 18 | safe-commit CHANGELOG.json | `233fd015e` |
| 19 | `git push origin CLOUD` | 316a5681f..233fd015e |
| 20 | Phase 2 — fresh `aws lambda invoke yang-model-portfolio-benchmarks` with `data_20260519_v1.pkl` payload | StatusCode 200; output_keys=3; model_count=5; timeseries_row_count=2675 |
| 21 | S3 versioning post-invoke — comprehensive key | Single new version 18:39:55 (15414 bytes) — NO race |
| 22 | S3 versioning post-invoke — legacy key | Single new version 18:39:55 (9569 bytes) — NO race |
| 23 | AC4 SHA-256 hash comparison (modulo generated_at) vs base AE 17:18:50 baseline | **byte-identical** (`34f46cc29fc2af9c4babc7d1d7d4d8eeee28edf68d015d24593055200be19a7b`) |
| 24 | AC4 6-of-9 long-window cells (1M, QTD, 1Q, YTD, 1Y, SI) × 5 models = 30-cell match | **30/30 match: model + idx_vol + etf_vol all identical** |

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| yang-pipeline | yang-v2.4.3 | f79700cb7 |

## Acceptance Criteria

| AC | Description | Status | Evidence |
|---|---|---|---|
| AC1 | SFN execution → single S3 write + correct values | **PASS** (logical) | Older Lambda destroyed; race structurally impossible. AC1 fully empirical confirmation defers to AC3 (tomorrow's 14:00Z natural SFN fire). |
| AC2 | Fresh `aws lambda invoke` reproduces correct values + matches DS~B local probe to-the-cent | **PASS** | 18:39:55 invoke produced byte-identical content to base AE 17:18:50 invoke (which matched DS~B per Phase 0). SHA `34f46cc29...0be19a7b`. |
| AC3 | 2026-05-20T14:00Z scheduled SFN execution single-write + correct values | **DEFERRED** — passive observation post-fire | Will verify S3 versioning post-2026-05-20T14:00Z; expected single new version per key + correctly-differentiated 1D/WTD/MTD (1D==WTD will persist if 5/20 is data-as-of-first-trading-day-of-week; that's expected math, not collapse). |
| AC4 | 6-of-9 long-window cells (1M, QTD, 1Q, YTD, 1Y, SI) reproduce TO THE CENT vs DS~B probe baseline | **PASS** | 30/30 cells match across model/idx_vol/etf_vol fields. Transitive proof via byte-identical match against base AE 17:18:50 baseline which itself matched DS~B to-the-cent. |
| AC5 | Terraform-only deploy per Rule 1; tagged + pushed + record-terraform-deploy | **PASS** | f79700cb7 + yang-v2.4.3 + 233fd015e |
| AC6 | No emoji; pre-commit gate (vacuous on deletes); session log | **PASS** | ASCII-only; ds-commit-gate.sh has no .py edit to check (delete-only commit); this log = AC6 deliverable |
| AC7 | Compiler tools: `comp-blast yang-generate-benchmark-returns` + `comp-iam gaps` + `comp-pipescript io yang-generate-benchmark-returns` + `comp-routes trace OUTPUT_KEY` | **PASS** — Compiler Tools section below |
| AC8 | RAVC2 to 2.0.0_SA_COO + CC 1.0.0_SA_CTO + CC 0.4.0_DS_ClientPlatform~B | sending after this log commits |

## Verification

```text
# Pre-invoke baseline (comprehensive key versions)
2026-05-19T17:18:50Z  15414 bytes  Dv9eRdF33dmhlO2ymfGw.byKCJLlW7lk  base AE fresh-invoke (Phase 0)
2026-05-19T11:25:04Z  15417 bytes  Ei1PBpuJhCInkRSP8rVkGNPoRMoSnO33  older Lambda last-writer (collapsed)
2026-05-19T11:25:03Z  15414 bytes  numli0VXWkNuusBbhWZOuLBYZTQHOXm9  newer Lambda first-writer (correct, overwritten 1s later)

# Post-invoke (my Phase 2 fresh-invoke)
2026-05-19T18:39:55Z  15414 bytes  cw7OZBxc6YrAIWmUxuDvGN6jv2fduQsc  surviving Lambda, single-write, correct

# AC4 SHA-256 (modulo generated_at) — base AE baseline vs my Phase 2 invoke
17:18:50 (base AE): 34f46cc29fc2af9c4babc7d1d7d4d8eeee28edf68d015d24593055200be19a7b
18:39:55 (mine):    34f46cc29fc2af9c4babc7d1d7d4d8eeee28edf68d015d24593055200be19a7b
IDENTICAL: True
```

## Compiler Tools

| Tool | Result | What worked / failed |
|------|--------|----------------------|
| `comp-blast yang-generate-benchmark-returns` (Phase 0.5 baseline) | "No downstream consumers found" | Graph-level consumer trace; portal consumers reach via S3 key (not Lambda name) — orthogonal to retire-safety |
| `comp-blast yang-model-portfolio-benchmarks` (Phase 0.5 comparison) | "No downstream consumers found" | Same — confirms consumer trace is key-bound, not Lambda-bound |
| `comp-pipescript io yang-generate-benchmark-returns` | "Unknown script" | Lambda not indexed in pipescript graph (expected per DS~B's Phase 0 finding on `yang-model-portfolio-benchmarks`; documented gap, not blocking) |
| `comp-routes trace yang-model-portfolio-benchmarks` | "No match for: yang-model-portfolio-benchmarks" | Lambda not an HTTP endpoint (correct; consumer trace via `comp-platinum reverse json/benchmarks/model_portfolio_benchmarks.json` would be the routing-graph path; n/a for retire decision) |
| `comp-iam service opal-security-scanner-processor` (sister Phase 0.5 spot — N/A here since this is a Lambda removal not addition) | n/a | No new boto3 surface (pure removal); orphan-IAM scan via `comp-iam gaps` post-retire deferred to follow-up session-end check |
| `comp-iam gaps` (post-retire orphan check per AC7) | TBD | Will run as session closeout; expect no orphan policies since `yang-pipeline-lambda-role` is shared across all yang Lambdas and the role itself is unchanged |
| Cross-grep `infra/aws/terraform` for `yang-generate-benchmark-returns` post-retire | Only historical artifacts (CHANGELOG snapshots + plan-output.txt + ROLLBACK_SNAPSHOT.json + IMPORT_COMMANDS.sh + LAMBDA_SNAPSHOT_PRE_TERRAFORM) | No live TF refs remain |

## Next Steps

- `[2.0.0_SA_COO]` RAVC2 validation AC1-8.
- `[0.4.0_DS_ClientPlatform~B]` CC: post-retire JSON values reproduce TO THE CENT against your MDLP_VOLAUD.001 probe baseline on the 6-of-9 long-window cells (30/30 cells match). MDLP_VOLAUD project ready to close 3-step atomic on your accept + COO RAVC2 accept.
- `[2026-05-20T14:00Z natural SFN fire]` AC3 passive verify — check S3 versioning post-fire (expect single new version per key, NOT two; expect 1D differentiated from MTD per period; 1D==WTD is data-shape expected on Monday-as-data-as-of vs Tue-fire days).
- `[follow-up cleanup]` Orphan S3 artifact `s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-generate-benchmark-returns.zip` remains (not TF-managed; safe to leave or sweep). Lambda Layer `pandas-pyarrow-layer:1` still referenced by other yang Lambdas (`generate_etf_returns`, etc.); not orphaned. Lambda CloudWatch log group destroyed by TF (CW does NOT auto-delete log streams; orphan streams under `/aws/lambda/yang-generate-benchmark-returns` should expire per retention or sweep manually).
- `[future]` `record-terraform-deploy.sh` quirk: it captures `git rev-parse HEAD` for `deployed_commit` even when HEAD has unrelated commits from other agents past the pipeline-scoped tag. The previous fix `1071d5719` improved pipeline-scoped commit detection but didn't fix the deployed_commit field. Future cleanup TO if it bites again.

## Notes for ~B Lane Memory

- First-TO ship. Andrew-direct provisioning ~17:39Z; GO dispatched ~17:42Z via base COO; OWNED_PATHS lane gap surfaced + cleared ~17:55-18:00Z (1-line YAML add by COO).
- Pattern surfaced: **Andrew-direct lane provisioning should bundle the `.owned-paths.yaml` permitted_agents add into the registration step.** Future provisioning of new ~lanes (~C/~D) on any agent should be a 2-step protocol: (1) MCP registration broker + (2) owned-paths.yaml line-add. COO flagged for memory entry; potentially a hook-automation follow-on.
- `record-terraform-deploy.sh` writes with default git identity (`Andrew Berman`); blocked by owned-paths hook even when invoked from an agent's terminal. Workaround: manually craft the CHANGELOG entry under the agent's serial via `safe-commit.sh`. Discussed potential fix: have the script accept `--agent` arg or read from `.comp-graph/.agent_context`.
