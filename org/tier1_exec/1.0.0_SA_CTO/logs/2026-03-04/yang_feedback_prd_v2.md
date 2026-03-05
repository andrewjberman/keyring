# Yang Feedback PRD V2 — 1.0.0_SA_CTO

**Date:** 2026-03-04
**Agent:** 1.0.0_SA_CTO
**Branch:** CLOUD

---

## Objective

Ingest Yang's 4-part feedback on the Advisor Intelligence page, organize into
architectural requirements, and produce a V2 PRD for COO decomposition into
updated task orders.

---

## Work Completed

### 1. Yang Feedback Ingestion (4 parts)

Received and organized 29+ feedback items from Andrew (relaying Yang's review):

| Section | Items | Key Changes |
|---------|-------|-------------|
| Assets Overview (Header) | 1-8 | AUA stack flip, asset mix toggle, NNA bar alignment, new GRO mode |
| Distribution | 9-16 + 2.2b/2.2c/2.3b | Bucket removal, city drill-down, ADV relationship drill-down, outflows quartile fix, area->stacked bar |
| Advisors | 17-21 | QTD/YTD bug, Advisor toggle, drop 1Y rolling, NNA bar format |
| Books | 22-29 | Admin/non-admin architecture, tax-dominant client view, AI exec summary RAG |

### 2. V2 PRD Written

`docs/architecture/ADVISOR_INTELLIGENCE_YANG_FEEDBACK_V2.md`

- 21 new work streams (Y1-Y17 + Y3-FE, Y5-FE, Y6b, Y6c, Y6d)
- 5 execution phases defined
- Full dependency graph
- Relationship to V1 PRD documented (what's unchanged, extended, or replaced)
- Naming decisions flagged for Andrew/Yang

### 3. Late Additions (Andrew follow-up)

- **2.2b:** Snapshot GEO-NNA city-level drill-down (state -> city)
- **2.2c:** Outflows quartile inversion fix scoped to ALL 4 grain levels (state, city, architect, relationship)
- **2.3b:** Snapshot ADV-NNA relationship-level drill-down (architect -> relationship)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| V2 PRD as new document, not in-place edit of V1 | V1 has completed streams with status tracking; overwriting would lose that history |
| GRO data uses accounting identity (AUA_end - AUA_start - NNA) | No new raw data needed if period AUA endpoints and NNA both available |
| AI RAG system recommended as separate mini-PRD | Too large and architecturally distinct to bundle with visual feedback items |
| Outflows quartile fix scoped to all 4 levels | Same logical error applies everywhere NNA outflows are percentile-ranked |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `docs/architecture/ADVISOR_INTELLIGENCE_YANG_FEEDBACK_V2.md` | Created — full V2 PRD | No — local only |
| `org/tier1_exec/1.0.0_SA_CTO/logs/2026-03-04/yang_feedback_prd_v2.md` | Created — this log | No — local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

V2 PRD is written and ready for COO decomposition. No commits pushed yet — DT owns the
push gate. The PRD defines 21 new work streams across all Pod 4 agents plus AE shared
services. Phase 1 (frontend-only visual changes) can start immediately once COO issues
task orders. Phase 2 (DS data work) runs in parallel.

---

## Next Steps

1. **[COO] Read V2 PRD and decompose into task orders** — see handoff briefing
2. **[DT] Push CLOUD** — PRD + session log need to reach remote
3. **[COO] Update existing RD task orders** — C2/C4/4C may need scope adjustments per Yang feedback
4. **[DS] Phase 2 data batch** — after COO issues task orders

**Do NOT:**
- Issue task orders directly to leaf agents from this PRD — COO decomposes
- Start ADVI-006 thread before J3 is live
- Bundle AI RAG system (Y17) into the main task order set — separate mini-PRD needed
