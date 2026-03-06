# COO Session Log -- ADVI_49FNV3 Project Launch
**Agent:** 2.0.0_SA_COO
**Date:** 2026-03-06
**Start Time:** 20:35
**End Time:** 21:15

---

## Objective

Initiate ADVI_49FNV3 (49Financial V3) from CTO PRD handoff. Decompose 7 fixes (F1-F7)
and Books tab new features (N1-N3) into task orders. Run Pattern 0 threads for
interface-dependent streams before writing task orders for those streams.

---

## Session Context

- ADVI_YANGV2 and ADVI_V1VERS confirmed closed by CTO.
- ADVI_AUAVAR: COMPLETE (both task orders done, BKF fix deployed, 98.9% accuracy).
- ADVI_NNAVAR: IN PROGRESS (Phase 3 structural diagnostics just run by DT; DS analyzing).
- CTO registered ADVI_49FNV3, corrected $1.236B error across 8 files.

---

## Work Completed

### 1. Thread Pre-Flight + Downstream Check

- DE (0.4.0): fresh log today (Benchmark scatter -> portal-v2.1.9 deployed to PROD).
- DS (0.4.0): 6 logs today covering all AUAVAR phases + NNAVAR Phase 2-3 scripts.
- RD (0.4.2): last log 2026-03-04 (YANGV2 Phase 3 work). Pre-flight note: slightly stale
  but acceptable -- RD's YANGV2 work is complete, no active blockers.
- DT (0.4.0): 10 logs today, all AUAVAR execution + NNAVAR structural. Active.

### 2. PRD Analysis -- Work Stream Classification

| Stream | Classification | Rationale |
|--------|---------------|-----------|
| F1: GRO data | Direct task order to DS | Investigation, root cause unknown |
| F2: Projected bars | Direct task order to RD | Frontend-only, fully spec'd |
| F3: Segment drilldowns | Direct task order to DE | Wiring investigation; data likely exists |
| F4: Stacked advisor bar | Pattern 0 thread | DS must confirm inflow/outflow shape |
| F5: QTD/YTD bug | Parallel task orders DS + DE | Joint investigation, no interface design needed |
| F6: Unassigned sorting | Direct task order to RD | Pure frontend, trivial |
| F7: Zebra striping | Direct task order to RD | Pure frontend, trivial |
| N1+N2: Books tab Phase 1 | Pattern 0 thread | DS confirm data, DE arch, RD layout |
| N3+Y14: Layer 3 + gating | Deferred (Phase 2a) | Not tasked |

### 3. Direct Task Orders Issued (7)

| Task Order | Agent | File |
|------------|-------|------|
| F1: GRO investigation | DS | ADVI_49FNV3.F1.gro-data-investigation.md |
| F2: Projected bars | RD | ADVI_49FNV3.F2.projected-bars.md |
| F3: Segment drilldown wiring | DE | ADVI_49FNV3.F3.segment-drilldown-wiring.md |
| F5-DS: QTD/YTD Lambda | DS | ADVI_49FNV3.F5-DS.qtd-ytd-lambda-investigation.md |
| F5-DE: QTD/YTD frontend | DE | ADVI_49FNV3.F5-DE.qtd-ytd-frontend-investigation.md |
| F6: Unassigned sorting | RD | ADVI_49FNV3.F6.unassigned-sorting.md |
| F7: Zebra striping | RD | ADVI_49FNV3.F7.zebra-striping.md |

### 4. Thread ADVI_49FNV3-001 -- F4 Stacked Bar Data Contract

Script: `org/threads/staging/run-ADVI_49FNV3-001-stacked-bar-data-contract.sh`
Thread: `ADVI_49FNV3-001-pattern-0-stacked-bar-advisor-inflow-out`
Participants: DS -> DE -> RD (round_robin, 3 turns, gpt-5.2, tools ON)
Result: CONVERGE at turn 8 (RD final turn).

**Key findings:**
- Inflows and outflows ARE separate in the source data (script 10 has separate cum_inflows/cum_outflows).
- `stacked_bar` data already exists in advisor_rolling_flows.json with separate fields.
- `AdvisorBarEntry` interface already exists in types.ts.
- F4 is **frontend-only**. No backend changes required.

**Locked contract:**
- Entry shape: `{ advisor_name, advisor_id, inflows (positive), outflows (positive), nna_net (signed) }`
- Period keys: qtd, ytd, 1y, 3y, max | Role keys: architects, implementors
- Outflows render: `outflowsNeg = -outflows`, Recharts `stackOffset="sign"` + `ReferenceLine y=0`
- Gold NNA dash: Scatter/ReferenceDot at y=nna_net
- Top 10 sort: nna_net descending

### 5. Thread ADVI_49FNV3-002 -- Books Tab Design Brief (N1/N2)

Script: `org/threads/staging/run-ADVI_49FNV3-002-books-tab-design.sh`
Thread: `ADVI_49FNV3-002-pattern-0-books-tab-design-brief-n1-n2`
Participants: DS -> RD -> DE (round_robin, 3 turns, gpt-5.2, tools ON)
Result: RD converged at turn 8 (DE turn 9 not reached due to early convergence).
Design brief exists at: `docs/architecture/advisor_intelligence/books_tab_design_brief.md` (from prior ADVI-006 thread, covers L2/L3/L4).

**Key findings:**
- N1 data confirmed available today -- no backend changes needed:
  - `clients_tab.json`: headline (total_aua, account_count, client_count), tax, engagement
  - `architect_leaderboard.json`: windows['1Y'].entries[] with total_aua, name, client_count
- N2 data confirmed in per-advisor JSONs: advisors/{advisor_id}/book.json
- CRITICAL slug fix required: frontend must replicate `_advisor_id()` regex (not just whitespace replace)
- N1 "AUA by Advisor": Option A (reuse existing table) -- faster, consistent
- Median AUA NOT in clients_tab headline -- do not display
- Phase 1b is fully backend-unblocked

### 6. Post-Thread Task Orders Issued (3)

| Task Order | Agent | File |
|------------|-------|------|
| F4: Stacked bar impl | RD | ADVI_49FNV3.F4.stacked-bar-impl.md |
| N1+N2: Firm dashboard + advisor book wiring | DE | ADVI_49FNV3.N1-N2-DE.firm-dashboard-and-advisor-book-wiring.md |
| N1+N2: Firm dashboard + advisor book UI | RD | ADVI_49FNV3.N1-N2-RD.firm-dashboard-and-advisor-book-ui.md |

RD N1-N2 task order is BLOCKED until DE completes N1-N2-DE (wiring must precede UI).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| F4 sort key: nna_net desc | Thread recommendation; total_aua would require backend change |
| N1 AUA by Advisor: Option A (table reuse) | Fastest for Phase 1b; consistent with existing patterns |
| N1/N2 Phase 1b: no backend changes | All data exists today in published JSONs |
| F5: parallel DS + DE task orders, no thread | It's a bug investigation, not an interface design |
| N3/Y14: deferred | Explicitly Phase 2a; not tasked this session |

---

## Open Items for Andrew

| Item | Priority | Decision Needed |
|------|----------|----------------|
| F4 sort key confirmation | Low | nna_net desc (COO default) or total_aua (requires backend work)? |
| NNA canonical fix go/no-go | P1 | Approve JNL/sweep commits 9bfb289b+b4f2d7a7 for gold rebuild |
| AUAVAR cube rebuild timing | High | BKF fix deployed; trigger rebuild now or wait for scheduled run? |
| AUAVAR cash-only accounts ($34.1M) | Medium | Accept gap or pursue balance feed architecture? |

---

## Files Modified This Session

| File | Action |
|------|--------|
| 7 direct task orders (F1-F7) | Created -- see Work Completed table |
| 3 post-thread task orders (F4, N1-N2 DE, N1-N2 RD) | Created -- see Work Completed table |
| `org/threads/staging/run-ADVI_49FNV3-001-stacked-bar-data-contract.sh` | Created |
| `org/threads/staging/run-ADVI_49FNV3-002-books-tab-design.sh` | Created |
| `org/threads/ADVI_49FNV3-001-*` (full thread + messages) | Created by orchestrator |
| `org/threads/ADVI_49FNV3-002-*` (full thread + messages) | Created by orchestrator |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-06/advi_49fnv3_project_launch.md` | This file |

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

ADVI_49FNV3 project launched. 10 task orders issued across DS, DE, RD.
Two Pattern 0 threads ran and converged. F1-F7 fixes decomposed; N1-N2 Books
tab Phase 1b decomposed. All independent work streams can start immediately.
RD N1-N2 UI is blocked on DE N1-N2 wiring. N3/Y14/Phase 2 not yet tasked.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] NNAVAR Phase 3 analysis** -- structural results just returned from DT.
   Transfer contamination finding (r=0.386 without transfers) is significant. DS must analyze and
   report before next NNAVAR thread/task order.
2. **[0.4.0_DS_ClientPlatform] F1 GRO investigation** -- ADVI_49FNV3.F1 (P0 fix)
3. **[0.4.0_DS_ClientPlatform] F5-DS QTD/YTD Lambda investigation** -- ADVI_49FNV3.F5-DS
4. **[0.4.2_RD_AdvisorIntelligence] F2, F4, F6, F7** -- independent fixes, can start now
5. **[0.4.0_DE_ClientPlatform] F3, F5-DE, N1-N2** -- F3 and F5-DE can start now; N1-N2 after thread receipt absorbed
6. **[Andrew/COO] AUAVAR cube rebuild decision** -- BKF fix is live, needs trigger authorization
7. **[Andrew] NNA canonical fix go/no-go** -- P1, JNL/sweep commits waiting

**Do NOT:**
- Task N3 (Relationship Detail) or Y14 gating until Phase 1b is delivered
- Change F4 sort key to total_aua without confirming Andrew's preference (requires backend work)
- Trigger AUAVAR cube rebuild without explicit Andrew authorization
