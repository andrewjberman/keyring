# ka_testing Runtime Evaluation — ADVI_CLSUNI + ADVI_CLSPT2 — 1.0.0_SA_CTO

**Date:** 2026-03-19
**Session type:** Architecture, runtime test, deployment

---

## Objective

Evaluate the ka_testing Docker execution runtime against two real projects
(ADVI_CLSUNI and ADVI_CLSPT2) to establish a baseline performance benchmark
and identify specific gaps before graduating the runtime to more complex work.

---

## Work Completed

### 1. Architecture Work (pre-runtime)

- ADVI_CLSUNI PRD written (docs/architecture/ADVI_CLSUNI_PRD.md)
- ADVI_BKSCMP PRD updated to GLDRST paths
- ADVI_GLDRST CTO review completed (4 conditions met by DS; correction applied re: copy target)
- ADVI_CLSPT2 PRD written (docs/architecture/ADVI_CLSPT2_PRD.md)
- ADVI_CLSPT2 registered (org/projects/ADVI_CLSPT2.json)

### 2. ADVI_CLSUNI Runtime Execution

**6 runs total. Results at: org/ka_testing/advi_clsuni/results/ and .runtime/results/**

| Run | Config | Outcome | Root cause |
|---|---|---|---|
| 1 — alignment only (3 Workers) | bare Python | 440K tokens on AE_CloudOps, interrupted | Context windowing absent; 40K/iter context growth |
| 2 — alignment only (5 Workers) | Docker | Clean alignment pass | DS→RD interface correctly `missing`; AE_PartnerETL in deps |
| 3 — execution (DS+DT+AE) | Docker + runtime mount | DS 27K, DT 11K; AE pre-flight blocked | Branch checkout -B reset wiped prior commits |
| 4 — execution retry | Docker (rebuilt image) | CORPOREAL_ROOT missing | Container env var not set |
| 5 — execution retry | Docker + env | DS + DT completed; RD junk commit (615 files) | git_commit staged entire working tree (fixed in rebuild) |
| 6 — execution retry (final) | Docker + runtime mount + rebuilt image | RD types.ts correct; DT lambda wipe + ClientsTab wipe | write_file on existing files; Workers not using edit_file |

**Runtime Worker performance (CLSUNI):**

| Worker | Files written correctly | Files requiring manual restore/patch | Tokens |
|---|---|---|---|
| AE_CloudOps | DynamoDB table + IAM resource blocks (content correct) | main.tf structure rewrote; HCL broken; manual fix | ~15K |
| DS | Class structure, signatures, return patterns | __init__ was mocked (3 hardcoded items); full rewrite required | 27K |
| RD (run 1) | None — 615-file junk commit | Full revert required | ~25K |
| RD (run 2) | types.ts 100% correct | ClientsTab.tsx prepended; restore + manual edit | ~90K |
| DT | etf_classifier.py copy (correct) | lambda_function.py wiped to stub twice | 11K + 50K |
| AE_ETL | Pre-flight blocked correctly (table not active) | seed_bd_securities.py written manually | 0 |

**CLSUNI attribution: ~36% of final committed code unedited from runtime.**

### 3. ADVI_CLSPT2 Runtime Execution

**2 runs. Results at: .runtime/results/run_20260319T211632.json (DS) and run_20260319T212244.json (DT)**

Telemetry log covering both projects: `.runtime/results/runtime-telemetry.log` (events 001-040)

| Run | Workers | Outcome |
|---|---|---|
| 1 — DS (3 files) | DS.CP.1 | 128K tokens, 19 iter. 3 files produced. Syntax errors in 2 (dkef typo, orphaned stubs). lambda_function.py duplicate body + prepend. |
| 2 — DT (deploy) | DT.CP.1 | 40K tokens, 12 iter. Deploy sequence correct (build, plan, apply, 0-diff). source-map.json wiped to stub. |

**Runtime Worker performance (CLSPT2):**

| Worker | Files written correctly | Defects | Tokens |
|---|---|---|---|
| DS | classify_bd_securities.py (97%) | dkef typo + empty stub in classify; duplicate body in lambda | 128K |
| DS | detect_new_securities.py (100% — third attempt) | Written 3x; first 2 structurally broken | — |
| DS | lambda_function.py ETFClassifier wiring (20 lines correct) | Old body left as some_other_function(); prepend garbage | — |
| DT | terraform apply sequence (correct) | lambda-source-map.json wiped to stub | 40K |

**CLSPT2 attribution: ~67% of final committed code unedited from runtime.**

### 4. Performance Benchmark (side-by-side)

| Vector | CLSUNI | CLSPT2 | Delta |
|---|---|---|---|
| Unedited production code | ~36% | ~67% | +31pp |
| Stub implementations | 1 (boto3 mocked) | 0 | Eliminated |
| File destruction events | 3 | 1 (source map only) | -2 |
| Git scope violations | 1 (615 files) | 0 | Eliminated |
| Pre-flight gate accuracy | N/A (not active in early runs) | 2/2 correct | — |
| Tokens per correct output line | 540 | 478 | -12% |
| Semantic correctness pre-syntax | Low (stub) | High (real boto3) | Major |
| Remaining failure modes | write_file, stub implem, git scope | write_file on source map, duplicate bodies, no git_commit | Narrowed |

### 5. Deployments Completed This Session

| Action | Tag | Notes |
|---|---|---|
| bd-securities DynamoDB table + IAM | shared-infra-v1.5.0 | Terraform apply; 116 items seeded |
| opal-partners-data (ETFClassifier copy) | partners-api-v1.6.0 | etf_classifier.py added to Lambda package |
| opal-partners-data (ETFClassifier wired) | partners-api-v1.7.0 | _classify_holding() now delegates to _clf; production-live |

### 6. Runtime Attribution Rule Established

Any project, task order, or deliverable where the ka_testing Docker runtime
produced code must be marked `[*runtime]` in REGISTRY.md and carry an asterisk
in the project phase description. See rule in org/AGENT_START_HERE.md §Runtime
Attribution and memory/feedback_runtime_attribution.md.

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `docs/architecture/ADVI_CLSUNI_PRD.md` | Created | Yes |
| `docs/architecture/ADVI_CLSPT2_PRD.md` | Created | Yes |
| `org/projects/ADVI_CLSUNI.json` | Created | Yes |
| `org/projects/ADVI_CLSPT2.json` | Created | Yes |
| `org/projects/REGISTRY.md` | Multiple updates this session | Yes |
| `data/black_diamond/scripts/gold/lib/etf_classifier.py` | Created (DS runtime + manual patch) [*runtime] | Yes |
| `data/black_diamond/scripts/classification/seed_bd_securities.py` | Created (manual) | Yes |
| `data/black_diamond/scripts/classification/classify_bd_securities.py` | Created (DS runtime + minor fixes) [*runtime] | Yes |
| `data/black_diamond/scripts/gold/detect_new_securities.py` | Created (DS runtime + structure fix) [*runtime] | Yes |
| `infra/aws/terraform/shared-infra/main.tf` | bd-securities + IAM added (AE runtime content + manual HCL fix) [*runtime] | Yes |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/etf_classifier.py` | Created (DT runtime) [*runtime] | Yes |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` | ETFClassifier wired (DS runtime core + manual cleanup) [*runtime] | Yes |
| `portal/src/pages/AdvisorIntelligence/types.ts` | Taxonomy update (RD runtime — 100% correct) [*runtime] | Yes (portal DEV f0d9d01) |
| `portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | deriveQuarterlyFromTimeseries (RD runtime content + manual apply) [*runtime] | Yes (portal DEV f0d9d01) |
| `org/ka_testing/` (full runtime) | Docker infra, all runtime modules, alignment fixes | Yes |

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

ADVI_CLSUNI and ADVI_CLSPT2 both deployed. ETFClassifier is live in
opal-partners-data at partners-api-v1.7.0. bd-securities has 116 seeded items.
classify_bd_securities.py and detect_new_securities.py committed and ready for
AE to run on EC2.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL]** Run classify_bd_securities.py on EC2 — enriches
   bd-securities beyond 116 Yang items using OpenAI batch classification
2. **[2.0.0_SA_COO]** Issue GLDRST task orders to DS (DS must resolve Condition 2:
   lib/classification approach first, then COO issues)
3. **[0.4.0_DT_ClientPlatform]** Portal DEV->PROD merge (shared gate: MVP318 WS6
   + MVPLVL + MIXV2 gates must also clear)
4. **[runtime]** Next runtime test: fix write_file guard on existing files, enforce
   git_commit as first Ad stage action, use apply_patch task orders for multi-step
   file edits

**Do NOT:**
- Run 06b gold layer until GLDRST DS session updates classification calls
- Treat runtime-attributed deliverables as fully human-reviewed — always verify
