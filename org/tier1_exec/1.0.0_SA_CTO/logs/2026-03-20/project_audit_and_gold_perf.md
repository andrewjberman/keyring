# Project Registry Audit, Gold Layer Performance, Classifier Fix — 1.0.0_SA_CTO

**Date:** 2026-03-20
**Session:** 7

## Objective

Full registry audit to close deprecated/complete projects, fix hanging
classify_bd_securities.py, and increase gold layer concurrency across all scripts.

---

## Work Completed

### 1. Ground Truth Corrections (startup)

- Created `org/projects/ADVI_GLDPRE.json` (lost during COO stash operations, never committed)
- Added GLDPRE row to REGISTRY.md Active Projects
- GLDPRE.002 DS task order: `pending` -> `complete` (WS2 committed at `61f76c8b`)
- GLDPRE.006 DT dependency on DS .002: `pending` -> `complete`
- Prompt.md dashboard updated to session 7 (partners-api v1.3.0->v1.8.0, shared-infra v1.4.0->v1.5.0)
- BKSCMP registry phase: added RD WS3 completion (portal DEV `6266d17`)
- MEMORY.md pipeline tags updated (partners-api v1.8.0, shared-infra v1.5.0)

### 2. Project Registry Audit — 5 Projects Closed

Bottom-up audit of all 9 active projects. Found 5 were either complete or deprecated:

| Project | Reason for Closure |
|---|---|
| `ADVI_MVP318` | WS1-WS5 all done. bd-v2.19.0-v2.19.2, partners-api-v1.4.0. Gold rerun subsumed by GLDPRE. |
| `ADVI_MVPLVL` | All task orders complete (.007 via MVP318.001, .008 at 14b3be3d). 5 threads complete. |
| `ADVI_ADVTV2` | DS committed, EC2 deployed. Gold rerun subsumed by GLDPRE Phase 4. |
| `ADVI_MIXV2` | All DS/DE/DT done. AE 003 gold rerun subsumed by GLDPRE. |
| `DRFR_PTMCH` | P1-P5 deployed. P6a deployed. P6b-d deprecated per Andrew. |

Also corrected BKSCMP state (3/4 task orders already complete, not 1/4 as registry showed):
- DS .001 COMPLETE, RD .002 COMPLETE (task order status fixed), DT .003 COMPLETE (partners-api-v1.5.0)
- AE .004 (script 12 S3 upload) folded into GLDPRE.005 Phase 2 scope

### 3. CLSPT2 Task Orders Issued

Discovered classify_bd_securities.py was represented as complete but:
- WS2 (classify script) was a stub in the registry — DS actually delivered real implementation
- Script 12 uses static ETF_CLASSIFICATIONS dict, NOT ETFClassifier (DynamoDB-backed)

Three task orders created:
- `ADVI_CLSPT2.001.ds-finish-classify-script.md` — DS finishes OpenAI implementation (DONE — DS already delivered, task order is pre-completed reference)
- `ADVI_CLSPT2.002.ae-run-classifier-ec2.md` — AE runs classifier on EC2
- `ADVI_CLSPT2.003.ds-script12-etfclassifier-migration.md` — DS migrates script 12 from static dict to ETFClassifier

### 4. Classifier Hang Fix

classify_bd_securities.py was hanging on EC2. Root cause: 3 bugs.

| Bug | Issue | Fix |
|---|---|---|
| boto3 clients at module level, no region_name | IMDS resolution hangs without metadata service | Moved clients inside function, added `region_name='us-east-1'` |
| dry-run didn't return | Continued to Secrets Manager + OpenAI after logging | Added `return` after dry-run output |
| Module-level init | Hang on import before main() | Clients now function-scoped |

Committed at `7de19390`.

### 5. Gold Layer Concurrency Increase

All gold scripts increased from 64 (or lower) to 128 workers. All are I/O-bound
(S3 GETs). Peak memory at 128 concurrent partitions is ~3.4GB on 32GB r6i.xlarge.

| Script | Was | Now |
|---|---|---|
| 00_build_accounts_dimension.py | 64 | 128 |
| 02_build_positions_cube.py | 64 | 128 |
| 03_build_holdings_lots.py | 64 | 128 |
| 05_build_client_performance.py | 64 | 128 |
| 05b_build_account_performance.py | 64 (hardcoded 16 in pool) | 128 (fixed) |
| 06b_build_client_mix_timeseries.py | 32/64 | 128/128 |

Committed at `d031cb7a` (06b) and `25a09998` (rest).

### 6. S3 Upload

All 7 files uploaded to S3 while OpenAI classifier was running (safe — separate
S3 prefixes, classifier already loaded its code from /tmp):

- 6 gold scripts -> s3://opal-data-bd/code/gold/
- 1 classifier -> s3://opal-data-bd/code/classification/

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Close MVP318, MVPLVL, ADVTV2, MIXV2 | All code-complete; pending gold reruns subsumed by GLDPRE |
| Close DRFR_PTMCH, deprecate P6b-d | Core feature live; P6b-d had zero activity for 8 days; Andrew confirmed |
| Fold BKSCMP AE .004 into GLDPRE.005 | Script 12 is in run_gold_layer.sh; GLDPRE full run covers it |
| 128 workers for all gold scripts | I/O-bound work on 32GB instance; peak memory ~3.4GB; 2x throughput |
| Upload during classifier run | Classifier runs from /tmp copy; S3 uploads don't affect it |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `data/black_diamond/scripts/classification/classify_bd_securities.py` | IMDS hang fix + dry-run fix | Yes -- `7de19390` |
| `data/black_diamond/scripts/gold/06b_build_client_mix_timeseries.py` | 128 workers | Yes -- `d031cb7a` |
| `data/black_diamond/scripts/gold/00_build_accounts_dimension.py` | 128 workers | Yes -- `25a09998` |
| `data/black_diamond/scripts/gold/02_build_positions_cube.py` | 128 workers | Yes -- `25a09998` |
| `data/black_diamond/scripts/gold/03_build_holdings_lots.py` | 128 workers | Yes -- `25a09998` |
| `data/black_diamond/scripts/gold/05_build_client_performance.py` | 128 workers | Yes -- `25a09998` |
| `data/black_diamond/scripts/gold/05b_build_account_performance.py` | 128 workers + fixed hardcoded 16 | Yes -- `25a09998` |
| `org/projects/*.json` (7 files) | Project closures + GLDPRE creation | Pending commit |
| `org/projects/REGISTRY.md` | 5 projects moved to Completed, GLDPRE+GLDRST added | Pending commit |
| `org/tier1_exec/1.0.0_SA_CTO/prompt.md` | Dashboard session 7 | Pending commit |
| Task orders (5 files) | GLDPRE.002/.005/.006 status fixes, CLSPT2.001/.002/.003 created | Pending commit |

---

## Current State

**Status:** IN PROGRESS
**Active branch:** CLOUD

OpenAI classifier running on bd-gold-layer-runner. Gold full run paused, will
resume after classifier completes. Updated scripts on S3 will be picked up on
next run_gold_layer.sh sync.

4 active projects remain:
- `ADVI_GLDPRE` — AE gold rerun + DT portal merge
- `ADVI_BKSCMP` — AE script 12 upload folded into GLDPRE.005
- `ADVI_CLSPT2` — DS .003 (script 12 migration) then gold rerun
- `ADVI_GLDRST` — blocked on BKSCMP + CLSPT2 completion

---

## Next Steps

1. **[0.6.0_AE_PartnerETL]** Monitor OpenAI classifier completion. Verify
   bd-securities count > 500 after run.
2. **[0.4.0_DS_ClientPlatform]** CLSPT2.003: Migrate script 12 from static
   ETF_CLASSIFICATIONS to ETFClassifier. Upload to S3 after commit.
3. **[0.6.0_AE_PartnerETL]** Resume gold full run (`run_gold_layer.sh full`).
   128-worker scripts will be synced automatically. Validate GLDPRE + BKSCMP
   acceptance criteria.
4. **[0.4.0_DT_ClientPlatform]** After gold run verified: portal DEV->PROD merge.
5. **[1.0.0_SA_CTO]** Close GLDPRE + BKSCMP. Assess CLSPT2 closure. Unblock GLDRST.

**Do NOT:**
- Resume gold run before OpenAI classifier finishes (both use the same instance)
- Treat script 12 composition output as accurate until CLSPT2.003 (ETFClassifier migration) is done
- Start GLDRST before BKSCMP and CLSPT2 are validated complete
