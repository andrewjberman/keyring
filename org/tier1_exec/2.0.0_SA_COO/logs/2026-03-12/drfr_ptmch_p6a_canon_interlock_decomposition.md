# DRFR_PTMCH Phase 6a Canon Interlock Decomposition — 2.0.0_SA_COO

**Date:** 2026-03-12

## Objective

Decompose the CTO's Canon Interlock PRD (Phase 6) into task orders. The PRD defines a
passive observation layer for the Yang pipeline that validates new data uploads against
established canonical values, flags divergences, and maintains an incremental historical
record with full audit trail and surgery capability.

---

## Work Completed

### 1. PRD Review

Read `docs/architecture/DRFR_PTMCH_CANON_INTERLOCK_PRD.md` (654 lines). Key architectural
decisions already resolved by CTO:
- Canon in same bucket (`opal-data-portal-v2/canon/`), not dedicated bucket
- Single Lambda handles all sources per upload (not one per source)
- Parallel Branch E in Step Functions ProcessFileTypes
- Parquet for canon storage (year-partitioned)
- Float comparison at 2 decimal places
- Always overwrite canon on mismatch (flag is the record)
- Zero friction: never blocks pipeline

### 2. Infrastructure Audit

Verified yang-pipeline Terraform state:
- `lambdas.tf`: 26 Lambdas via yang-lambda module. Pattern clear for adding new module.
- `yang-pipeline-definition.json`: Step Functions with ProcessFileTypes Parallel state
  containing Branches A-D. Branch E addition is straightforward.
- `main.tf`: `local.pandas_layer` includes pyarrow (needed for parquet). Available.
- IAM: `yang-pipeline-lambda-role` already has S3 read/write on `opal-data-portal-v2/*`.
  CloudWatch PutMetricData to verify (likely already present from existing generators).

### 3. Decomposition Decision

**Single task order to 0.5.0_AE_OpalETL. No DS task order. No thread.**

Rationale:
- No interface boundary: purely backend infrastructure. No portal UI changes.
  No data contract that feeds DE/RD. No Pattern 0 thread needed.
- The interlock Lambda is infrastructure code that uses pandas — same pattern as
  every other yang generator Lambda. Not a data science deliverable.
- OpalETL owns the yang pipeline (built P2 yang-time-machine). Consistent routing.
- Backfill script and surgery script are infrastructure tooling, not DS analysis.
- AE has deploy authority (can push to CLOUD, terraform apply, tag).

**Phase 6a only.** Phases 6b-6d deferred to separate task orders after 6a proves the pattern.

**P5 dependency.** P6a depends on P5 completing first — both modify `yang-pipeline-definition.json`
and yang-pipeline Terraform. Same agent (OpalETL), sequential execution.

### Task Order Dispatch

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.5.0_AE_OpalETL | org/tier2_senior/0.5.0_AE_OpalETL/task_orders/DRFR_PTMCH.P6a.yang-canon-interlock.md | Phase 6a: yang-canon-interlock Lambda (data_pkl only), Step Functions Branch E, Terraform module, backfill script, surgery script, CloudWatch metrics. Depends on P5 completion. |

Execution dependencies:
  DRFR_PTMCH.P5 (OpalETL) -> DRFR_PTMCH.P6a (OpalETL) — sequential, same agent

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Single AE task order, no DS/DE/RD | No interface boundary. Infrastructure code using pandas, same as all yang generators. |
| No thread | One agent, no cross-agent interface to align on. |
| Phase 6a only | Prove the pattern on data_pkl. Subsequent phases (6b-6d) get separate task orders. |
| P5 before P6a | Both modify yang-pipeline Terraform. Sequential to avoid conflicts. |
| OpalETL not MarketIntelligence DT | OpalETL owns yang pipeline infrastructure (P2 precedent). |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/DRFR_PTMCH.P6a.yang-canon-interlock.md` | New task order | No |
| `org/projects/DRFR_PTMCH.json` | Added Phase 6 PRD, updated phase and blocking | No |
| `org/projects/REGISTRY.md` | DRFR_PTMCH row updated with P6a status | No |
| `org/tier1_exec/2.0.0_SA_COO/prompt.md` | Dashboard updated (DRFR_PTMCH + OpalETL lines) | No |
| This file | Session log | No |

---

## Blockers

None. P5 is a prerequisite for P6a but both are assigned to the same agent — no cross-agent blocker.

---

## Current State

**Status:** COMPLETE (COO decomposition + post-execution validation done)
**Active branch:** CLOUD

**P5 + P6a both COMPLETE as of 2026-03-12:**

P5 (portal-time-machine orchestrator):
- OpalETL: portal-time-machine Lambda deployed (data-refresh-v2.2.0), yang-time-machine
  append-only exclusion patched (yang-v2.3.1). Commits `c92bf442`, `324d9a03`, `84273455`, `8b1ccb6d`.
- DE TradingOperations: TimeMachineContext + API endpoints + App wrapper committed to portal DEV.
  RD task orders issued to 0.3.3 (HistoryTab) and 0.3.1 (banner+filter). Commits `980be6dc`, `e1bfa41d`.
- All P5 AE + DE task orders marked complete.

P6a (yang-canon-interlock):
- Lambda deployed (yang-v2.3.0 → yang-v2.3.1). Branch E in Step Functions live.
  Backfill: 21 PKLs, 185K flags, canon frontier 2026-03-06. Commit `3242a472` (pushed).

**Remaining DRFR_PTMCH work:**
- RD sub-tasks: 0.3.3_RD_DataRefresh (HistoryTab time machine control) and
  0.3.1_RD_PortfolioManagement (banner + chart date filter) — task orders issued, not started.
- P6b-d: deferred until P6a live validation confirms pattern in production.

**Validation cross-checks performed:**
- Git tags: yang-v2.3.1 and data-refresh-v2.2.0 confirmed, match project JSON deployed_versions.
- Task order statuses: P2 complete, P5 (OpalETL) complete, P5 (DE) complete, P6a complete.
- RD task orders: confirmed in commit `980be6dc` at correct paths.
- ADVI_49FNV3: status=complete in project JSON, moved to Completed in registry.
- Registry, project JSON, COO dashboard all aligned.

---

## Next Steps

1. **[0.3.3_RD_DataRefresh] Build HistoryTab time machine control** -- date picker from
   restorePoints, Travel/Return buttons, loading state, active pill.

2. **[0.3.1_RD_PortfolioManagement] Build banner + chart filter** -- global amber banner
   when time machine active, date-filtered time series charts.

3. **[2.0.0_SA_COO] Issue P6b-P6d** -- after P6a live validation (next Yang upload), issue
   task orders for model_pkl, Excel sources, SmartX interlock, control plane consolidation.

**Do NOT:**
- Issue P6b/P6c/P6d task orders yet (wait for P6a live validation)
- Push the 2 unpushed commits (DT pushes)
