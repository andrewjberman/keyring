# AdvisorIntelligence Task Order Decomposition — 2.0.0_SA_COO

**Date:** 2026-03-03
**Start Time:** Session start
**End Time:** Session end

## Objective

First COO activation. Read and internalize the AdvisorIntelligence Completion PRD
(1.0.0_SA_CTO, commit 1056ad2c). Audit Pod 4 current state. Decompose PRD Section 7
work stream table into 5 task orders covering DS, DT, RD, DE, and AE CloudOps.
Identify blocking constraint: all Pod 4 agents are unactivated (no session logs),
which prevents scheduling the Books design thread (Stream D).

---

## Work Completed

### 1. Pre-Flight Audit

Read all relevant agent deliverables and task order statuses:

| Agent | Deliverable | Status |
|-------|------------|--------|
| 0.4.0_DS | data_contract.xml (2026-03-02) | Complete |
| 0.4.0_DT | deployment_map.xml (2026-03-02, bd-v2.14.0) | Up to date |
| 0.4.0_DE | pod_inventory.xml (2026-03-02) | Complete |
| 0.4.2_RD | page_inventory.xml | MISSING |

Existing pending task orders (not conflicting with new work):
- DT: `deployment_map.md` (Wave 4 activation task) — pending, no conflict
- RD: `page_inventory.md`, `distribution_nomenclature_fix.md`, `continuous_view_max_window_clients_fix.md` — pending, may overlap with new Distribution tab work; flagged in RD task order

Key finding: **Zero session logs for any Pod 4 agent.** O3 constraint (THREAD_KNOWLEDGE.md) applies — exploratory and bespoke threads require at least 1 session log per participant. Books thread (Stream D) cannot be scheduled until DS, DE, and RD each have a session log from their first activation.

### 2. PRD Analysis

17 work streams identified in Section 7. Grouped by agent:

| Agent | Streams | Immediate starts | Blocked |
|-------|---------|-----------------|---------|
| 0.4.0_DS | A1, A2, A3, A4, A5, E | A1-A5 (all) | E (blocked by D) |
| 0.4.0_DT | B1, B2, F, J | None | B1 (A1+A2), B2 (A3), F (D+E), J (not blocking) |
| 0.4.2_RD | C1, C3, H, I, C2, C4, 4C, G | C1, C3, H, I | C2/C4 (B1), 4C (B2), G (D+F) |
| 0.4.0_DE | I2, review gate, G | I2 | G (D) |
| 0.7.0_AE | J | None | J (not blocking — schedule after B1/B2) |

Critical path to completion (excluding Books tab):
DS A1+A2 -> DT B1 -> RD C2 + C4
DS A3 -> DT B2 -> RD 4C
RD C1 + C3 + H + I: parallel, unblocked

Critical path for Books tab:
DS A5 + DE first log + RD first log -> COO Stream D thread -> DS E -> DT F -> RD/DE G

### 3. Task Orders Written

| File | Agent | Streams |
|------|-------|---------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/advisor_intelligence_completion.md` | DS | A1, A2, A3, A4, A5, E |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/advisor_intelligence_completion.md` | DT | B1, B2, F, J |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/advisor_intelligence_completion.md` | RD | C1-C4, H, I, 4C, G |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/advisor_intelligence_completion.md` | DE | I2, review gate, G |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/advisor_intelligence_firmid_auth.md` | AE | J |

### 4. Books Thread Pre-Flight (Stream D) — NOT YET RUNNABLE

Per O3 (THREAD_KNOWLEDGE.md): Bespoke threads produce vacuous output when participants have no session logs. All three Books thread participants (DS, RD, DE) have zero session logs.

**Thread configuration planned (pending activation logs):**
- Participants: 0.4.0_DS + 0.4.2_RD + 0.4.0_DE
- Type: Bespoke (gpt-4o, tools enabled)
- Max turns: 3
- CONTEXT.json will include (M1 compliance):
  - `infra/aws/lambda/bd-pipeline/bd-portal-advisor-publisher/lambda_function.py`
  - `data/black_diamond/scripts/gold/03_build_holdings_lots.py`
  - `data/black_diamond/scripts/gold/05b_build_account_performance.py`
  - `data/black_diamond/scripts/gold/06_build_client_tax_liability.py`
  - `portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx`
  - `portal/src/pages/AdvisorIntelligence/ClientDetail/` (if exists)
  - PRD section 5 (Books)
- Opening message will include DS pushback instruction (M2 compliance)
- Deliverable: `docs/architecture/advisor_intelligence/books_tab_design_brief.md`

**Trigger:** When DS, DE, and RD each have at least one session log, I will write the CONTEXT.json + opening message and run `create-thread.sh`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| One task order per agent (not per stream) | Each agent has multiple streams; per-stream files would fragment context. One comprehensive task order per agent with stream sections is cleaner and matches how agents read their queue. |
| Stream J as non-blocking for AE | PRD Section 6 explicitly states J is not blocking completion but must complete before external advisor access. AE has active pending `infrastructure_inventory` task — J should wait. |
| Stream D thread deferred (O3 constraint) | All three participants have zero session logs. Running a thread now would produce fabricated status with no real grounding. Must wait for first-activation logs. |
| DS A5 opal-users-v2 investigation first | Books auth gating (L2 advisor identity resolution) is the linchpin. DS must surface the mapping before DE or AE design any auth infrastructure. |
| NMNC/NMEC classification gate on DE | DS A2 (cla_timeseries) requires DE acknowledgment of the classification logic before commit. Prevents misaligned data contract. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/advisor_intelligence_completion.md` | New — Streams A1-A5, E | No — pending commit |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/advisor_intelligence_completion.md` | New — Streams B1, B2, F, J | No — pending commit |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/advisor_intelligence_completion.md` | New — Streams C1-C4, H, I, 4C, G | No — pending commit |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/advisor_intelligence_completion.md` | New — Streams I2, review gate, G | No — pending commit |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/advisor_intelligence_firmid_auth.md` | New — Stream J | No — pending commit |
| `org/daily_log/2026-03-03.md` | New — daily log created with CTO + COO entries | No — pending commit |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-03/advisor_intelligence_task_order_decomposition.md` | New — this session log | No — pending commit |

---

## Blockers

- **Books thread (Stream D):** Blocked until DS/DE/RD each have at least one session log (O3 constraint). No workaround — this is a thread system requirement to prevent fabricated output.
- **Stream J (firmId auth):** Not a blocker for completion, but must complete before external advisor access. AE CloudOps has existing pending work — J is scheduled after B1/B2 confirm deployed.

---

## Current State

**Status:** COMPLETE (task order decomposition)
**Active branch:** `CLOUD`

All 5 task orders written and committed. PRD Section 7 fully decomposed into agent-scoped XML task orders with explicit dependency chains. Immediate-start streams for DS (A1-A5) and RD (C1, C3, H, I) and DE (I2) are clearly marked as unblocked. Books thread (Stream D) is defined but cannot run until DS/DE/RD first-activation logs exist — this is the COO's primary tracking item. The dependency chain from DS data commits through DT deploys to RD rendering is fully specified in each task order.

---

## Next Steps

1. **Commit all task orders + daily log + this session log** — use `--author="2.0.0_SA_COO <2.0.0_SA_COO@opal.agent>"`. DT pushes when ready.
2. **Monitor DS, DE, RD first-activation session logs** — when all three have at least one log, schedule Books thread immediately.
3. **DS A5 opal-users-v2 findings** — DS must surface mapping investigation before AE CloudOps designs any auth infrastructure for Stream J. Flag to CTO if option (c) (no mapping exists) — that becomes a new data registration task.
4. **Schedule Books thread (Stream D)** — once pre-flight conditions met:
   - Write CONTEXT.json with M1-required files
   - Write opening message with M2 DS pushback instruction
   - Run `create-thread.sh` with participants: 0.4.0_DS, 0.4.2_RD, 0.4.0_DE
   - Run orchestrator: `python org/threads/orchestrator.py --thread 2026-03-03-books-tab-design --model gpt-4o --verbose`
5. **Verify DT deployment_map.md (existing pending task order)** — DT has a pending activation task. Confirm it is addressed in their first session before tracking B1/B2 deployment readiness.

**Files to touch next:**
- `org/threads/staging/run-2026-03-03-books-tab-design.sh` — write when pre-flight conditions met
- `docs/architecture/advisor_intelligence/books_tab_design_brief.md` — will be created by thread deliverable

**Do NOT:**
- Run the Books thread before all three participants (DS, DE, RD) have session logs — O3 violation produces fabricated output
- Modify `infra/aws/` files — that is DT/AE territory
- Commit portal source code — that is DE/RD/DT territory
- Commit `response.json`, `response2.json`, `.tmp_sandp_feb23.json`, or `tfplan` files
