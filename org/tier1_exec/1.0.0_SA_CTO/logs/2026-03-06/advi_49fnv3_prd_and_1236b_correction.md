# ADVI_49FNV3 PRD + $1.236B Error Correction -- 1.0.0_SA_CTO

**Date:** 2026-03-06

---

## Objective

1. Correct the erroneous $1.236B AUA figure that propagated from a prior DS
   investigation into AUAVAR thread artifacts, task orders, and logs.
2. Author the PRD for ADVI_49FNV3 (49Financial V3): 7 fixes + Books tab
   three-layer drill hierarchy.

---

## Work Completed

### 1. $1.236B Error Correction

The DS Phase 1 reconciliation investigation (2026-03-05) reported our gold layer
model at $1.236B AUA. This was a prior agent error conflating NNA and AUA metrics.
Our actual non-cash AUA is ~$1.545B. The erroneous figure propagated into the
AUAVAR-001 thread (all 6 messages + CONTEXT_COMPILED), both AUAVAR task orders,
the COO session log, thread receipts, the daily log, and the CTO PRD.

Corrected 8 files that future agents will read on startup:

| File | Correction |
|------|-----------|
| DS log `bd_model_schwab_reconciliation_investigation.md` | Prominent correction banner at top |
| PRD `AUA_VARIANCE_ANALYSIS_PRD.md` | Prior art section rewritten, risk table updated |
| DS task order `ADVI_AUAVAR.001-DS` | Background corrected, Step 1 simplified |
| DT task order `ADVI_AUAVAR.002-DT` | Background corrected, scope narrowed |
| COO log `advi_nnavar_auavar_project_launch.md` | Receipt summary corrected |
| DS thread receipt | Correction banner added |
| DT thread receipt | Correction banner added |
| Daily log `2026-03-06.md` | Corrected with note |

Untouched: 11 frozen thread artifacts (messages 000-006, CONTEXT_COMPILED, context
injection copies). These are historical records per protocol. COO briefed to be
aware of contamination if injecting thread content into future contexts.

### 2. ADVI_49FNV3 PRD

PRD authored at `docs/architecture/ADVISOR_INTELLIGENCE_49FN_V3_PRD.md`.

**Fixes (P0):**
- F1: GRO mode no data (frontend wired, Lambda/data investigation needed)
- F2: Projected bars for partial periods (extrapolate with 1.5x cap, frontend-only)
- F3: Missing city/client drilldowns in Snapshot NNA Segment Analytics
- F4: Top ten advisors stacked bar (blue inflows, red outflows, gold NNA dash)
- F5: QTD/YTD timing bug (March 2026: Q1=YTD, should be identical)
- F6: Unassigned implementors pinned to bottom of leaderboard
- F7: Zebra striping on leaderboard rows

**New Features (P1):**
- N1: Books tab firm admin dashboard (tax status, AUA by advisor, distributions, engagement)
- N2: Advisor book drilldown (per-advisor tax, clients, NNA, engagement)
- N3: Relationship detail drilldown (Layer 3, may need publisher extension)
- N4: Y14 access gating (deferred from YANGV2, not Phase 1 priority)

**Phase 2 (noted, not blocking):**
- Firm-level asset allocation (new gold layer script/table needed)
- Fee revenue by advisor (new BD API feed needed -- data exists in BD)

**Key codebase findings:**
- GRO frontend is complete (PartnerAnalytics.tsx lines 372-400, 1272-1326)
- Tax status exists in gold layer (accounts_dimension `tax_status_1`, normalized)
- clients_tab.json already has tax breakdown (taxable/deferred/exempt with AUA)
- Per-advisor JSONs have tax, engagement, clients arrays
- income_fees is zeroed throughout ("not available from BD data")
- asset_allocation is zeroed ("not available from BD data")

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| $1.236B is an error, not a gold-vs-gold discrepancy | Andrew confirmed: prior agent conflated NNA and AUA. Our actual non-cash AUA is ~$1.545B. |
| Projected bar cap at 1.5x prior period | Andrew's direction: simple extrapolation with guardrail to suppress short-timeline noise |
| Fees and asset allocation are Phase 2 | Data doesn't exist in current pipeline. Noted but does not block Books tab launch. |
| Y14 access gating deferred again | Priority is data and interface structure. Auth chain already deployed. |
| Books tab three-layer hierarchy | Firm (admin) -> Advisor (drilldown) -> Relationship (detail). Natural top-down drill pattern. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| 8 files corrected for $1.236B error | See table above | No -- local |
| `docs/architecture/ADVISOR_INTELLIGENCE_49FN_V3_PRD.md` | Created -- full PRD | No -- local |
| `org/projects/ADVI_49FNV3.json` | Created -- project JSON | No -- local |
| `org/projects/REGISTRY.md` | Added ADVI_49FNV3 to active | No -- local |
| This session log | Created | No -- local |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

Three projects registered this session: ADVI_NNAVAR, ADVI_AUAVAR, ADVI_49FNV3.
YANGV2 closed. $1.236B error corrected across 8 files. COO briefed on thread
contamination. All files local only -- pending DT commit and push.

---

## Next Steps

1. **[2.0.0_SA_COO] Read ADVI_49FNV3 PRD and decompose into task orders** -- fixes
   F1-F7 are P0 (address first), Books tab N1-N3 are P1.
2. **[2.0.0_SA_COO] Rectify AUAVAR-001 thread artifacts** -- per CTO briefing,
   frozen thread messages contain $1.236B error. COO is aware.
3. **[0.4.0_DT_ClientPlatform] Commit and push CLOUD** -- carries all three project
   registrations, YANGV2 closure, error corrections, PRDs, and session logs.
