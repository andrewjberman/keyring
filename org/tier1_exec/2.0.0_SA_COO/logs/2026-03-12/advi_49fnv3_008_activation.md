# ADVI_49FNV3.008 Activation — 2.0.0_SA_COO

**Date:** 2026-03-12

## Objective

Process CTO's .008 briefing. Assess 0.6.0_AE_PartnerETL bandwidth, correct stale
ground truth documents, and activate the existing .008 task order for gold-silver
AUA validation pipeline.

---

## Work Completed

### 1. Ground Truth Corrections

| Document | Correction | Reason |
|----------|-----------|--------|
| `org/projects/REGISTRY.md` | ADVI_49FNV3 row: .007 CLOSED, .008 pending (was ".007 + .008 pending") | .007 resolved by ADVI_PSCFIX A2+A3 (bd-v2.18.3) |
| `org/tier1_exec/2.0.0_SA_COO/prompt.md` | Pod dashboard: 0.6.0 line updated, ADVI_49FNV3 line updated, PSCFIX entry finalized | Stale references to .007 as pending |

### 2. Bandwidth Assessment

0.6.0_AE_PartnerETL task order queue:
- 9 complete task orders (004, 005, 006, APISCP.001, DRFR_PTMCH.001, P3, P3b, PSCFIX.A1, PSCFIX.A3)
- 1 pending: `ADVI_49FNV3.008.gold-silver-aua-validation.md`
- No DRFR_PTMCH P5 work assigned to this agent (P5 goes to OpalETL + DE TradingOperations)
- AE's own Next Steps (log 2026-03-11) explicitly lists .008 as next work item

**Verdict: bandwidth clear. Activate .008.**

### 3. Spec Validation

The .008 task order (issued by DE 2026-03-11) is well-specified and still valid:
- Requirement 1: Create 05c_validate_aua_vs_silver.py (PASS/WARN/FAIL thresholds)
- Requirement 2: Wire into pipeline (after 05, before 09)
- Requirement 3: Backfill 35 dates (2026-01-16 through 2026-03-09)
- Requirement 4: Investigate 83 missing accounts + document price divergence

PSCFIX provides foundations that reduce scope slightly:
- 05d already loads silver allocations and computes certified_aua
- 6 liability exclusion types already codified in 05d
- 05c can reuse these patterns but adds decomposition + validation output

No spec changes needed.

### Task Order Dispatch

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.6.0_AE_PartnerETL | org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_49FNV3.008.gold-silver-aua-validation.md | ACTIVATED (existing, no changes). Gold-silver AUA validation pipeline: 05c script, pipeline wiring, 35-date backfill, root cause investigation. |

Execution dependencies: none (single agent, no blockers, silver allocations already exist daily)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Activate .008 without spec changes | Spec is well-specified by DE, PSCFIX foundations reduce scope slightly but don't invalidate any requirement |
| No thread needed | Single agent (AE), no interface boundary, no DS/DE/RD dependency |
| Priority: low-medium | Portal displays correct numbers via PSCFIX. This is observability/engineering quality. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/projects/REGISTRY.md` | .007 CLOSED in ADVI_49FNV3 row | No |
| `org/tier1_exec/2.0.0_SA_COO/prompt.md` | Dashboard updated (3 edits) | No |
| This file | Session log | No |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

CTO's .008 briefing processed. Ground truth corrected (.007 closed). AE bandwidth
confirmed clear. The existing .008 task order at `0.6.0_AE_PartnerETL` is activated
with no spec changes needed. When AE is next invoked, .008 is their top pending item.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Execute .008** -- create 05c, wire into pipeline, backfill 35 dates, investigate root causes (83 missing accounts + price divergence)
2. **[0.6.0_AE_PartnerETL] Mark .008 complete** when all 5 acceptance criteria are met

**Do NOT:**
- Modify the .008 spec (it's valid as-is)
- Block on PSCFIX work (PSCFIX is fully complete)
- Assign .008 to any other agent (AE owns the gold pipeline)
