# ADVI_MVP318 PRD + Ground Truth Corrections — 1.0.0_SA_CTO

**Date:** 2026-03-18
**Start Time:** session start
**End Time:** ongoing

## Objective

Incorporate DS/RD investigative deliverables (D1-D5 + RD books tab brief) into a
consolidated PRD for the final ADVI MVP sprint. Correct stale org documents from prior sessions.

---

## Work Completed

### 1. Ground Truth Corrections (6 documents)

| Document | Correction |
|---|---|
| `ADVI_MIXV2.004.lambda-deploy.md` (DT task order) | `pending` -> `complete` (git: 1fa08590, partners-api-v1.3.0) |
| `ADVI_MIXV2.003.ec2-06b-deploy.md` (AE task order) | DS dependency statuses `pending` -> `complete` (commits a7617a08, a885f625, 2384a9f6) |
| `ADVI_MIXV2.json` | Phase/blocking updated: DT 004 complete, thread 001 complete |
| `ADVI_ADVTV2.json` | Phase updated: DS committed (8ef1da9b), EC2 deployed (72c03d2a), DT verification unknown |
| `REGISTRY.md` | ADVI_MIXV2 and ADVI_ADVTV2 phase rows updated to current state |
| `prompt.md` dashboard | Updated to 2026-03-18 session 5, pipeline tags current |

### 2. PRD: ADVI_MVP318

File: `docs/architecture/ADVI_MVP318_PRD.md`

Six workstreams identified:
- WS1: Segment analytics variance — diagnostic first, then conditional fix
- WS2: Architect consolidation Lambda deploy (D4 code ready, uncommitted)
- WS3: New advisor-level AUA timeseries + mix timeseries endpoints (new gold artifacts + routes)
- WS4: ConsolidatedOverviewPanel frontend (RD in-flight, N1+L3 unblocked, L2 waits for WS3)
- WS5: MTD/QTD/YTD leaderboard windows (gold layer run, one coordinated FULL run covers ADVI_ADVTV2 + ADVI_MIXV2.003 + WS5)
- WS6: Final portal DEV->PROD merge (gates on all portal DEV commits)

Key architectural decision: new advisor timeseries artifacts (`gold/advisors/{id}/timeseries.json`
and `gold/advisors/{id}/mix_timeseries.json`) are pre-computed in `bd-portal-advisor-publisher`
during pipeline runs and served statically by `opal-partners-data`. Consistent with existing
Books tab architecture.

Key coordination note: WS5 gold layer run (AE) should be the LAST infrastructure operation.
It triggers the publisher Lambdas. DT must deploy WS2+WS3b (advisor-publisher) and WS1 (publisher,
if needed) BEFORE the gold layer completes, so the new Lambda code is active when the pipeline
artifacts are generated.

### 3. Project Registration

- `org/projects/ADVI_MVP318.json` created
- `REGISTRY.md` row added

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Pre-compute advisor timeseries in bd-portal-advisor-publisher, serve static JSON | Consistent with existing architecture; keeps opal-partners-data as a thin routing layer; allows complex aggregation (mix timeseries) during pipeline run without real-time latency |
| WS2 + WS3a committed together, deployed as one artifact | DS is already in the file (D4). Adding WS3a in the same commit saves one DT build cycle. |
| Final gold layer run covers ADVI_ADVTV2 + ADVI_MIXV2.003 + WS5 simultaneously | All three script changes are deployed to EC2. One FULL run clears three project blockers. Sequencing requirement: DT must deploy Lambda updates first. |
| bd-v2.19.0 recommended for next BD tag | New gold artifact types + Lambda behavior change (architect override, advisor TS) = minor version bump |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_MIXV2.004.lambda-deploy.md` | status pending->complete | No — local |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_MIXV2.003.ec2-06b-deploy.md` | dependency statuses updated | No — local |
| `org/projects/ADVI_MIXV2.json` | phase/blocking + thread status | No — local |
| `org/projects/ADVI_ADVTV2.json` | phase/blocking updated | No — local |
| `org/projects/REGISTRY.md` | ADVI_MIXV2 + ADVI_ADVTV2 rows + ADVI_MVP318 row | No — local |
| `org/tier1_exec/1.0.0_SA_CTO/prompt.md` | dashboard updated to 2026-03-18 session 5 | No — local |
| `docs/architecture/ADVI_MVP318_PRD.md` | Created | No — local |
| `org/projects/ADVI_MVP318.json` | Created | No — local |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

PRD for ADVI_MVP318 written and registered. Project JSON and REGISTRY.md updated.
Six workstreams documented with agent assignments, data contracts, deployment sequencing,
and gate conditions. Six stale documents corrected. Ready for COO handoff.

The critical path is: DS commits (D4 + WS3a + WS3c + WS1 publisher fix + script 10)
→ DT deploys Lambdas → AE runs FULL gold layer → DT merges portal DEV->PROD.
The RD ConsolidatedOverviewPanel L2 completion and DE endpoint wiring run in parallel
with the Lambda deploys.

---

## Next Steps

1. **[2.0.0_SA_COO] Receive PRD briefing** and decompose into task orders for all agents
2. **[0.4.0_DS_ClientPlatform] Priority commits** — D4 (advisor-publisher architect fix),
   WS3a (advisor timeseries logic), WS3c (opal-partners-data route handlers), WS1 (confirm
   if bd-portal-publisher fix is staged correctly)
3. **[0.4.0_DT_ClientPlatform] WS1-A diagnostic** — run `.tmp_segment_analytics_diag.py`
   to determine segment analytics root cause before DS commits publisher fix
4. **[0.6.0_AE_PartnerETL] Wait for DT Lambda deploys** then run FULL gold layer (covers
   ADVI_ADVTV2 + ADVI_MIXV2.003 + WS5 simultaneously)
5. **[0.4.2_RD_AdvisorIntelligence] ConsolidatedOverviewPanel** — complete N1 + L3 views now;
   L2 view unblocked after DT deploys WS3d (opal-partners-data v1.4.0)

**Files to touch next:**
- `docs/architecture/ADVI_MVP318_PRD.md` — COO reads as source for decomposition
- `org/projects/ADVI_MVP318.json` — COO updates phase as task orders are issued

**Do NOT:**
- Run gold layer BEFORE DT deploys WS2 (bd-portal-advisor-publisher with D4 + WS3a)
- Deploy bd-portal-advisor-publisher until DS commits both D4 + WS3a in one commit
- Merge portal DEV->PROD until ALL portal commits are present (WS4 L2, WS5 frontend, WS1-C conditional)
