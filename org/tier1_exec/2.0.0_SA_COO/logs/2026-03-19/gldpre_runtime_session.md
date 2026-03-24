# Session Log — ADVI_GLDPRE Runtime Execution — 2.0.0_SA_COO

**Date:** 2026-03-19/20
**Duration:** ~3 hours
**Branch:** CLOUD (parent), DEV (portal submodule)

---

## Summary

Executed GLDPRE workstreams WS1, WS3, WS4, WS5 via the ka_testing Docker runtime.
Ran two evaluation passes (V1 and V2 with eng team fixes). Validated and corrected
all runtime output. All 4 workstreams are code-complete with validator corrections
applied. WS2 (aua_mix) deferred pending CTO decision on target script.

## What Was Done

### 1. PRD Intake and Planning

- Read ADVI_GLDPRE PRD (docs/architecture/ADVI_GLDPRE_PRD.md)
- Read all referenced source files: 06b, 09, lib/etf_classifier.py, lambda_function.py,
  PartnerAnalytics.tsx, types.ts, ClientsTab.tsx
- Identified WS2 target ambiguity: PRD says "script 09" but timeseries_chart.json is
  produced by archived script 08. Deferred WS2 pending CTO confirmation.
- Created execution harness (`org/ka_testing/advi_gldpre/run_execution.py`) and
  `.runtime/config.json` with 4 task orders

### 2. V1 Runtime Execution

- Non-containerized test first (rejected -- user corrected: must use Docker)
- Docker run with `runtime:latest` image, OpenAI provider (gpt-4o)
- 4 workers completed, 100K tokens, 5m15s wall time
- **Result: 10% attribution, 8 Critical defects.** All 4 workers produced broken output.
- Validator (COO) corrected all defects manually.
- Wrote full eval report: `ka_testing_runtime_evaluation_gldpre.md`

### 3. V2 Runtime Execution (A/B test with eng fixes)

- Eng team implemented P0 fixes: replace_function tool, git_commit failure=draft,
  coordinator mandates, index.lock pre-flight
- Rebuilt Docker image
- Stashed V1 corrections, restored all files to pre-edit state for clean A/B
- Re-ran same 4 task orders against rebuilt runtime
- 4 workers completed, 145K tokens, 5m47s wall time
- **Result: ~65% attribution, 2 Critical defects (down from 8).**
  - Chimera functions: eliminated (0, was 4)
  - File destruction: eliminated (0, was 2)
  - New: indentation bug in cash residual, over-deletion in FirmMixPeriodPoint
- Wrote full V2 eval report: `ka_testing_runtime_evaluation_gldpre_v2.md`

### 4. Final Production Code

After both eval runs, applied all corrections from scratch on HEAD:
- Restored 06b, lambda_function.py to HEAD
- Restored portal types.ts from pre-CLSUNI commit (f0d9d01^) — CLSUNI runtime had
  destroyed the 1397-line file, replacing it with a 17-line stub. This was committed
  as portal DEV HEAD f0d9d01 and never caught.
- Applied all WS1/WS3/WS4/WS5 edits manually with full validation

### 5. Org Updates

- COO prompt: added Runtime Execution Protocol section (canonical Docker flow)
- ADVI_GLDPRE.json: phase updated
- Memory: saved feedback_runtime_docker_canonical.md
- MEMORY.md: added runtime Docker feedback link

---

## Current State of Files (Uncommitted)

### Parent Repo (CLOUD branch)

| File | Change | Status |
|---|---|---|
| `data/black_diamond/scripts/gold/06b_build_client_mix_timeseries.py` | ETFClassifier import, classify_holding/classify_series rewritten, _MIX_ASSET_CLASSES 3-class, compute_period_views cash residual, ~230 lines of static dicts/regex removed | Modified, unstaged |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` | Line 1056: mix_timeseries.json -> mix.json | Modified, unstaged |
| `org/ka_testing/runtime/tools.py` | Eng team: replace_function tool added | Modified, unstaged |
| `org/ka_testing/runtime/nodes/worker.py` | Eng team: replace_function wiring | Modified, unstaged |
| `org/ka_testing/runtime/nodes/coordinator.py` | Eng team: coordinator mandates | Modified, unstaged |

### Portal Submodule (DEV branch)

| File | Change | Status |
|---|---|---|
| `src/pages/AdvisorIntelligence/types.ts` | Restored from f0d9d01^ (1397 lines, was 17-line stub). FirmMixPeriodPoint 4-class, MixTimeseriesPoint 4-class, MixAssetClass 4-member. | Modified, unstaged (+1389/-11 because f0d9d01 destroyed the file) |
| `src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` | FIRM_MIX_COLORS 4-class, firmMixChartData alternatives, CLASS_LABELS 4-class, bar keys 4-class, isTop=3 | Modified (from stash pop) |
| `src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | Minor (from stash pop, pre-existing changes) | Modified |

### Git History Notes

- `194f0410` — non-containerized WS3 commit (on CLOUD). Should be reverted or squashed.
- `1b63de96` — revert of above. These two cancel out but add noise.
- Portal `f0d9d01` — CLSUNI runtime commit that destroyed types.ts. The types.ts
  restoration in this session's diff fixes this. The portal commit history will show
  a large +1389/-11 diff — this is correct (restoring the destroyed file).

---

## Blocking / Next Steps

| # | Action | Owner | Depends On |
|---|---|---|---|
| 1 | **Commit GLDPRE WS1+WS3 code** (parent repo) | COO or DT | — |
| 2 | **Commit GLDPRE WS4+WS5 + types.ts restoration** (portal) | DT | — |
| 3 | **CTO decision: WS2 target script** | CTO | Is aua_mix added to script 08 (archived) or script 09? |
| 4 | **WS2 implementation** | DS (runtime or manual) | #3 |
| 5 | **Lambda deploy WS3** as partners-api-v1.8.0 | DT | #1 committed + Terraform apply |
| 6 | **Full gold rerun on EC2** | AE_PartnerETL | #1 + #4 committed, deployed to EC2 |
| 7 | **Portal DEV->PROD merge** | DT | #2 + #6 verified |

---

## Runtime Eng Team Handoff

Two eval reports written for the eng team:
- `ka_testing_runtime_evaluation_gldpre.md` — V1 baseline (pre-fix)
- `ka_testing_runtime_evaluation_gldpre_v2.md` — V2 A/B comparison (post-fix)

**Key findings:**
- replace_function eliminated all chimera-function and file-destruction defects
- Attribution improved from 10% to 65% on pure-edit workload
- Remaining gaps: edit_file indentation (P0), over-deletion on interface edits (P0),
  deletion budget prioritization (P1)
- 2/4 workers produced deployable code unmodified in V2 (was 0/4 in V1)

**Pre-existing issue discovered:** Portal types.ts was destroyed by CLSUNI runtime
commit f0d9d01 (1397 lines -> 17 lines). This was committed to portal DEV and never
caught. Fixed in this session by restoring from f0d9d01^ and applying GLDPRE edits.

---

## Files Created This Session

| File | Purpose |
|---|---|
| `org/ka_testing/advi_gldpre/__init__.py` | Package init |
| `org/ka_testing/advi_gldpre/run_execution.py` | Local test harness (not for production use) |
| `.runtime/config.json` | V2 task order config |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-19/ka_testing_runtime_evaluation_gldpre.md` | V1 eval report |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-19/ka_testing_runtime_evaluation_gldpre_v2.md` | V2 A/B eval report |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-19/gldpre_runtime_session.md` | This file |
| `memory/feedback_runtime_docker_canonical.md` | Runtime must use Docker |
