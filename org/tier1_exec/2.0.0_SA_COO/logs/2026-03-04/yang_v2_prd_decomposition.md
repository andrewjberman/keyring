# Yang V2 PRD Decomposition — 2.0.0_SA_COO

**Date:** 2026-03-04
**Session:** Yang V2 PRD Task Order Decomposition

---

## Startup Orientation

Read all recent commits and pod 4 logs before acting. State at session start:

| Agent | Work Since Last COO Session | Status |
|-------|----------------------------|--------|
| 0.7.0_AE_CloudOps | J1: opal-partner-49financial DynamoDB table + IAM | COMPLETE (f036f345) |
| 0.4.2_RD | 9 task orders complete: C1, C2, C4, C3, H, I, I2, 4C, nomenclature/window fixes | COMPLETE (ce2cb497) |
| 0.4.0_DT | HOTFIX-drilldown-account-perf-fallback | COMPLETE (4fcff1e2) |
| 2.0.0_SA_COO (prev) | ADVI-006 thread ran 9 turns (partial — DS+RD converged, DE final pending) | Partial (d9686db0+b9b9ca24) |
| 0.4.0_DE | ADVI-006-books_design_brief task order issued (pending) | Pending |
| J2/J3 | DT auth-handler + authorizer (now UNBLOCKED since J1 complete) | Pending DT |
| Portal DEV push | Pending DE review of RD work | Pending |

---

## PRD Read

Read `docs/architecture/ADVISOR_INTELLIGENCE_YANG_FEEDBACK_V2.md` in full.
32 feedback items across 4 sections. 21 new work streams (Y1-Y17 + FE variants).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Y8 interval toggle: per-view scope | GEO and ADV continuous AUA each get their own independent toggle state. No shared tab-level state needed for MVP. Simpler to implement; RD can proceed without DE consultation. |
| Y4 net line: implement + flag for visual confirmation | Formula (inflow + outflow) / 2 is specified in PRD but is unusual. RD implements with a code comment, and confirms with Andrew/Yang on first render. |
| AUA Mode A label: use "Clients" as placeholder | Naming decision pending from Andrew/Yang ("Clients" / "Tenure" / "Client Type"). RD implements toggle mechanism with "Clients" placeholder. Can be changed without code risk. |
| Y17 (AI RAG): NOT issued | Separate mini-PRD required. Do not bundle into ADVI task orders. Flag to CTO. |
| Y16 (ADVI-007 Books thread): deferred | Wait for J3 completion + DE ADVI-006 design brief to land. ADVI.json thread_counter not incremented yet. |
| Phase 3 FE task orders: NOT issued | Each Y-FE stream requires a Pattern 0 thread after DS delivers + DT deploys. COO schedules threads then issues FE task orders. |
| Y12 UI vs Y12 data: split | Y12 RD task order removes the 1Y rolling UI. DS removing rolling_1y data from script 10 is a separate decision — DS must confirm no other consumer before dropping. Rolling_1y key stays in the JSON until COO confirms. |
| Y6c applies at ALL 4 grain levels | Including the new city (Y6b) and relationship (Y6d) levels that don't exist yet — DS applies the fix when writing those extensions. |
| Y11 gates Y13 | DS must confirm advisor field existence before Y13 scope is final. COO must be notified of Y11 result to adjust Y13-FE expectations. |

---

## Task Orders Issued

### 1. ADVI-Y1-Y4-Y6-Y12-phase1-visual.md → 0.4.2_RD_AdvisorIntelligence
  - Y1: AUA stack flip (NMNC on top of NMEC)
  - Y4: NNA diverging bar alignment + net line centering (flag for visual confirmation)
  - Y6: -1k/1k bucket removal + footnote (GEO-NNA and ADV-NNA snapshots)
  - Y12: Drop 1Y rolling UI from Advisors tab (stacked bar is sole view)
  - Unblocked. Start immediately.

### 2. ADVI-Y8-continuous-aua-stacked-bar.md → 0.4.2_RD_AdvisorIntelligence
  - Y8: Continuous AUA AreaChart -> BarChart (stacked) + Interval toggle (Month/Quarter/Year)
  - Toggle state: per-view (COO design decision, no DE consultation needed)
  - Reuse getPeriodInfo() aggregation from PartnerAnalytics.tsx
  - Unblocked. Start after Phase 1 task order.

### 3. ADVI-Y-phase2-ds-data-batch.md → 0.4.0_DS_ClientPlatform
  - Streams: Y2, Y3, Y5, Y6b, Y6c, Y6d, Y7, Y9, Y10, Y11, Y13
  - Priority 1 (bugs): Y7 (binning), Y10 (QTD/YTD), Y6c (quartile inversion)
  - Priority 2 (investigations): Y2 (NMNC/NMEC definition), Y11 (advisor field)
  - Priority 3 (data extensions): Y3, Y5, Y6b, Y6d, Y9, Y13
  - Delivery batched: 4 batches, each triggering DT deploy notification
  - Y13 gates on Y11 result
  - Unblocked. Run parallel with RD Phase 1.

---

## Task Orders NOT Issued

| Stream | Reason Not Issued |
|--------|------------------|
| Y3-FE, Y5-FE, Y6b-FE, Y6d-FE, Y9-FE, Y13-FE (RD) | Require Pattern 0 threads after DS deliver + DT deploy |
| Y14 (Books access gating) | Blocked on J3 (DT auth-handler + authorizer deployment) |
| Y15 (Books implementation) | Blocked on ADVI-006 design brief (DE pending) + J3 |
| Y16 (ADVI-007 Books design thread) | Deferred: J3 + DE design brief required |
| Y17 (AI Executive Summary RAG) | Separate mini-PRD recommended. Do not bundle. |

---

## Existing Task Orders — No Changes Needed

ADVI-004 and ADVI-005 are both `complete`. No status changes needed.
The Y8/Y9 scope expansions are handled via new task orders, not amendments.
ADVI-006-books_design_brief.md (DE) is `pending` — untouched, DE owns it.

---

## Open Items Updated

| Item | Owner | Status |
|------|-------|--------|
| J2: auth-handler partner identity injection | 0.4.0_DT_ClientPlatform | UNBLOCKED (J1 complete) — start now |
| J3: portal-authorizer passthrough | 0.4.0_DT_ClientPlatform | BLOCKED on J2 |
| ADVI-006 design brief | 0.4.0_DE_ClientPlatform | Pending (task order issued 2026-03-04) |
| Portal DEV push | 0.4.0_DT_ClientPlatform | Pending DE review |
| RD Phase 1 (Y1+Y4+Y6+Y12) | 0.4.2_RD | Start now |
| RD Y8 (continuous AUA stacked bar) | 0.4.2_RD | Start after Phase 1 |
| DS Phase 2 data batch (Y2+Y3+Y5+Y6b+Y6c+Y6d+Y7+Y9+Y10+Y11+Y13) | 0.4.0_DS | Start now (parallel) |
| Y11 result notification to COO | 0.4.0_DS | Required before Y13 scope final |
| Phase 3 FE task orders (Y3-FE etc.) | 2.0.0_SA_COO | Issue after DS delivers + Pattern 0 threads |
| Y17 AI RAG mini-PRD | 2.0.0_SA_COO | Flag to CTO — separate track |
| ADVI-007 Books design thread | 2.0.0_SA_COO | Schedule after J3 + ADVI-006 brief land |

---

## Files Created

| File | Change |
|------|--------|
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI-Y1-Y4-Y6-Y12-phase1-visual.md` | New task order |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI-Y8-continuous-aua-stacked-bar.md` | New task order |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI-Y-phase2-ds-data-batch.md` | New task order |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-04/yang_v2_prd_decomposition.md` | This session log |
| `org/daily_log/2026-03-04.md` | Updated with Yang V2 COO session |

---

## Current State

**Status:** COMPLETE (task order decomposition)
**Active branch:** CLOUD

Critical path:
  RD Phase 1 (Y1+Y4+Y6+Y12) and DS Phase 2 data batch — run now in parallel
  RD Y8 — start after Phase 1 (same portal DEV branch, avoids conflicts)
  DT J2 — start now (J1 complete, unblocked)
  DT J3 — after J2 verified
  DE ADVI-006 brief — pending (unblocked, task order already issued)
  Phase 3 FE — gated on DS data batch delivery + DT deployment + Pattern 0 threads

Next COO action: schedule Pattern 0 alignment threads when DS signals batch delivery.
