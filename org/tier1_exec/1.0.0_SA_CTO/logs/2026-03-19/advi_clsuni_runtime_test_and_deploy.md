# ADVI_CLSUNI Runtime Test + Full Deploy — 1.0.0_SA_CTO

**Date:** 2026-03-19
**Start Time:** session continuation (ADVI_BKSCMP PRD produced earlier in session)
**End Time:** session end

## Objective

PRD for ADVI_CLSUNI (BD Securities Classification Unification) was written and
handed to COO earlier in this session. This log covers: (1) full ADVI_CLSUNI PRD
research + spec, (2) ka_testing runtime execution test against ADVI_CLSUNI using
the Docker-based multiagent runtime, (3) deployment of all ADVI_CLSUNI deliverables.

---

## Work Completed

### 1. ADVI_CLSUNI PRD

Full PRD written at docs/architecture/ADVI_CLSUNI_PRD.md. Key decisions:

| Decision | Rationale |
|---|---|
| Separate bd-securities table (not extend Yang's etf-classifications) | Keeps Yang taxonomy intact (hedge naming); BD gets correct alternatives naming from day one; decoupled operational cadence |
| Cash = computed residual, not stored | Yang asked not to add cash as a new DynamoDB class; residual approach handles unallocated and unclassifiable positions cleanly |
| OpenAI batch classification for BD universe | ~$0.01 for 10K securities; DynamoDB table seeded from Yang (116), extended via gpt-4o-mini for remainder; confidence scoring flags needs_review |
| ETFClassifier full-table scan at cold start | 116 items is tiny; all classify() calls O(1) after init; safe for both EC2 long-running processes and Lambda cold starts |

### 2. GOLD_LAYER_RESTRUCTURE_PROPOSAL review

DS submitted proposal for S3 path restructuring (silver/intermediate/gold taxonomy).
CTO approved with 4 conditions. Key issue identified: copy target for lib/classification.py
was _shared/etf_classification.py (Yang file -- wrong). Corrected to
opal-partners-data/etf_classifier.py. ADVI_GLDRST registered.
ADVI_BKSCMP PRD paths updated to GLDRST layout.

### 3. ka_testing Runtime Execution Test

Six runs total. Key progression:

| Run | Result | Root Cause |
|---|---|---|
| Run 1 (bare Python, 3 Workers) | 440K tokens on AE_CloudOps, interrupted | Context windowing not applied; per-iter context grew to 40K |
| Run 2 (Docker, 5 Workers) | AE_CloudOps + RD completed; DS, DT, AE_ETL failed | git checkout -B hard-reset wiped CLOUD_test on 2nd Worker |
| Run 3 (Docker + runtime mount) | DS 27K, DT 11K, AE_ETL pre-flight blocked | Branch fix applied; context windowing working |
| Run 4 (rebuilt image) | CORPOREAL_ROOT missing in container | Container needs env var |
| Run 5 (rebuilt image + env) | DS + DT completed; RD, AE_ETL pending | RD committed entire working tree (git add -A bug -- now fixed in image) |
| Run 6 (rebuilt image, fixed git scope) | RD types.ts correct; DT + RD wrote stubs | write_file on existing files wipes content |

### 4. Runtime Quality Assessment (against original PRD)

| Workstream | Runtime Contribution | Manual Intervention |
|---|---|---|
| WS1 AE_CloudOps Terraform | Resource blocks correct (PRD spec) | main.tf rewrite broke HCL; restored baseline + appended correctly |
| WS2 DS ETFClassifier | Class structure, signatures, layer architecture | Full __init__ rewrite (boto3 paginated scan); dead code removal; normalize_name fix |
| WS7 RD types.ts | MixTimeseriesPoint + FirmMixPeriodPoint correct | None -- genuine runtime output |
| WS7 RD ClientsTab.tsx | alternatives in deriveQuarterlyFromTimeseries spec | Restore from submodule + targeted edit_file |
| WS8 DT Lambda wiring | etf_classifier.py copy correct | lambda_function.py wiped twice; targeted edit_file applied |
| WS3 AE_ETL seed script | Pre-flight correctly blocked (no table yet) | Full script written manually |

Effective runtime attribution: ~35-40% of final committed code.
Primary failure mode: Workers used write_file on existing paths, wiping file contents.
Secondary failure mode (fixed in image): git_commit without file scope staged everything.

### 5. Full Deployment

All ADVI_CLSUNI deliverables deployed:

| Step | Result |
|---|---|
| CLOUD ← CLOUD_test (fast-forward merge) | cd448788 |
| Portal DEV push | f0d9d01 |
| Terraform shared-infra (bd-securities table + IAM) | 4 added, 0 destroyed |
| 0-diff verify | No changes |
| Tag shared-infra-v1.5.0 | Pushed |
| Seed bd-securities from etf-classifications | 116 items, 7 hedge->alternatives, 5 Opal aliases |
| build-and-upload partners-api/opal-partners-data | etf_classifier.py + lambda_function.py + etf_classification.py |
| Terraform partners-api apply | 1 changed (opal-partners-data code hash) |
| 0-diff verify | No changes |
| Tag partners-api-v1.6.0 | Pushed |

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Manual patch DS etf_classifier.py rather than re-run | Runtime produced correct structure; boto3 scan was the only missing piece; faster than another 27K-token run |
| Revert 157e8e49 (RD junk commit) rather than cherry-pick | 615 files committed; no valid content to salvage; full revert cleanest |
| Restore lambda_function.py from CLOUD each time DT wrote stub | DT consistently used write_file to create 5-line file; targeted edit_file was always correct approach |
| Write seed_bd_securities.py manually | AE_ETL pre-flighted correctly on every run (table didn't exist); script is 98 lines of boto3, faster to write than to re-run AE |
| .tmp_client_perf.parquet in git history | File was committed in 157e8e49 (RD junk) and deleted in 62c5081c (revert); exists in history only, not working tree; acceptable given no git lfs in this repo |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/aws/terraform/shared-infra/main.tf` | bd-securities table + IAM (AE restored baseline + appended) | Yes — e14fd78f |
| `data/black_diamond/scripts/gold/lib/etf_classifier.py` | Created (DS stub + CTO patch = production quality) | Yes — 65cdc21e |
| `data/black_diamond/scripts/gold/lib/__init__.py` | Created (empty) | Yes — 65cdc21e |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/etf_classifier.py` | Created (DT copy) | Yes — 66003b36 |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` | ETFClassifier import added (CTO edit_file) | Yes — c2c0bab7 |
| `portal/src/pages/AdvisorIntelligence/types.ts` | MixTimeseriesPoint/FirmMixPeriodPoint alternatives (RD, genuine) | Yes — f0d9d01 (portal DEV) |
| `portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | deriveQuarterlyFromTimeseries alternatives (CTO edit_file) | Yes — f0d9d01 (portal DEV) |
| `data/black_diamond/scripts/classification/seed_bd_securities.py` | Created (CTO) | Yes — cd448788 |
| `org/ka_testing/` (full runtime) | Docker infra, alignment.py, tools.py, all runtime modules | Yes — 4c8a0b59 |

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

All ADVI_CLSUNI code on CLOUD. bd-securities table ACTIVE (116 items seeded).
opal-partners-data Lambda deployed with etf_classifier.py at partners-api-v1.6.0.
Portal types updated on portal DEV at f0d9d01. ETFClassifier will do a real
DynamoDB scan on Lambda cold start. classify('CASH_USD', None) returns ''.
classify() maps hedge -> alternatives. All 4 layers functional.

Outstanding items:
- Portal DEV->PROD merge: shared gate with ADVI_MVP318 WS6, ADVI_MVPLVL, ADVI_MIXV2 -- DT owns
- classify_bd_securities.py (bulk OpenAI enrichment beyond 116 Yang items): not yet written
- detect_new_securities.py (gold layer step): not yet written
- 06b classification call update (replace static ETF_CLASSIFICATIONS with ETFClassifier): GLDRST scope
- ADVI_GLDRST DS Condition 2 (lib/classification -> Lambda layer relationship): pending DS response

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform]** Portal DEV->PROD merge (shared gate: wait for ADVI_MVP318 WS6 + ADVI_MVPLVL + ADVI_MIXV2 gates to clear)
2. **[0.4.0_DS_ClientPlatform]** classify_bd_securities.py + detect_new_securities.py -- extend the bd-securities table beyond the 116 Yang items using OpenAI batch classification
3. **[0.4.0_DS_ClientPlatform]** ADVI_GLDRST Condition 2 -- specify lib/classification approach before COO issues GLDRST task orders

**Files to touch next:**
- `data/black_diamond/scripts/classification/classify_bd_securities.py` -- DS writes this
- `data/black_diamond/scripts/gold/detect_new_securities.py` -- DS writes this

**Do NOT:**
- Run 06b gold layer until DS updates classification calls to use ETFClassifier (GLDRST + CLSUNI scope)
- Merge portal DEV->PROD before all project gate conditions are met
