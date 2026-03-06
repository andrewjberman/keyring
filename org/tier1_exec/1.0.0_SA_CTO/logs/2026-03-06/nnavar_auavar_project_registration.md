# NNAVAR + AUAVAR Project Registration & YANGV2 Closure -- 1.0.0_SA_CTO

**Date:** 2026-03-06

---

## Objective

Register two new ADVI projects for BD gold layer data quality analysis (NNA correlation
optimization and AUA variance decomposition), close ADVI_YANGV2, and hand off to COO
for task order decomposition.

---

## Work Completed

### 1. ADVI_NNAVAR -- NNA Variance Optimization

**PRD authored** at `docs/architecture/NNA_VARIANCE_OPTIMIZATION_PRD.md`.

Key framing: ACAT parameter grid (v2, executed 2026-03-05) showed Pearson r plateau at
0.175 -- ACAT adjustment adds $12-22M but doesn't move correlation. The $120M gap is
driven by factors outside ACAT (JNL exclusion calibration, velocity caps, dedup
aggressiveness, account coverage, timing). Project scope extends beyond parameter
tuning to full gap decomposition by filter category.

Significant prior art exists:
- DS Phase 3 analysis (ACAT production design complete)
- v2 param grid results on S3 (analysis pending)
- Correlation summary script written but not yet run

### 2. ADVI_AUAVAR -- AUA Variance Analysis

**PRD authored** at `docs/architecture/AUA_VARIANCE_ANALYSIS_PRD.md`.

Key framing: ~$55M gap between our $1.545B non-cash AUA and BD's $1.60B. 49Financial
leadership relies on BD. Prior DS investigation (5-phase reconciliation) found fundamental
data source difference. This project refocuses: segment-level decomposition to identify
which account/asset/pricing segments explain the gap. Outcome is explanation + addressable
vs explainable classification per segment.

Note: DS prior investigation erroneously reported our model at $1.236B (prior agent
conflated NNA and AUA metrics). Our actual non-cash AUA is ~$1.545B. Correction notes
added to DS log, PRD, task orders, COO log, and thread receipts on 2026-03-06.

### 3. ADVI_YANGV2 Closure

Marked complete. Y14 (Books access gating) deferred to upcoming ADVI_49FNV3 project.
All other task orders were delivered per DE audit (c1c50e3a). DT portal push and SSCN
wave pushes completed.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| NNAVAR scope extends beyond ACAT parameters | v2 grid proved ACAT alone doesn't move correlation. Gap decomposition by filter category is the real work. |
| AUAVAR framed as "explain the gap from BD" not "fix our model" | 49 leadership uses BD. The question is what we're missing, not whether our methodology is wrong. |
| Close YANGV2 with Y14 deferred to 49FNV3 | Y14 (Books access gating) is part of the broader Books tab completion that 49 data team flagged. Better scoped under 49FNV3. |
| Both projects to Pod 4 (ClientPlatform) | DS, DT, and AE resources are all Pod 4 / PartnerETL. BD pipeline is the data source. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `docs/architecture/NNA_VARIANCE_OPTIMIZATION_PRD.md` | Created -- full PRD | No -- local |
| `docs/architecture/AUA_VARIANCE_ANALYSIS_PRD.md` | Created -- full PRD | No -- local |
| `org/projects/ADVI_NNAVAR.json` | Created -- project JSON | No -- local |
| `org/projects/ADVI_AUAVAR.json` | Created -- project JSON | No -- local |
| `org/projects/ADVI_YANGV2.json` | status->complete, phase updated, closed date added | No -- local |
| `org/projects/REGISTRY.md` | YANGV2 moved to completed; NNAVAR + AUAVAR added to active | No -- local |
| This session log | Created | No -- local |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

Two new projects registered (NNAVAR, AUAVAR). YANGV2 closed. All files local only --
pending DT commit and push. COO handoff below.

---

## Next Steps

1. **[2.0.0_SA_COO] Read both PRDs and decompose into task orders** -- primary agents are
   0.4.0_DS_ClientPlatform (analysis) and 0.4.0_DT_ClientPlatform (EC2 execution).
   AE (0.6.0_AE_PartnerETL) consulted if BD data enrichment needed.
2. **[0.4.0_DT_ClientPlatform] Commit and push CLOUD** -- carries PRDs, project JSONs,
   REGISTRY update, YANGV2 closure, and this session log.
3. **[Andrew] Discuss ADVI_49FNV3 scope** -- Books tab completion + 49Financial data team
   feedback from yesterday.
