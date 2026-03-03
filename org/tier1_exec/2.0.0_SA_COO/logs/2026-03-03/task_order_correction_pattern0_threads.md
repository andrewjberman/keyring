# Task Order Correction: Pattern 0 Threads Before Task Orders — 2.0.0_SA_COO

**Date:** 2026-03-03
**Start Time:** Second session block
**End Time:** Session end

## Objective

Correct the premature task orders issued in the first session block.
The prior task orders for DS (A1/A2/A3), RD (C2/C4/4C), and DE (A2-gate)
pre-specified interface shapes (JSON schemas, TypeScript interface names, field
encodings) that should only come from Pattern 0 alignment threads. Per the updated
COO prompt (commit 28c98a78, M8 mandate in THREAD_KNOWLEDGE.md): Pattern 0 threads
run BEFORE task orders for any stream where DS output feeds DE wiring feeds RD layout.
Also: update staging scripts to use gpt-5.3-codex per CTO model selection commit c18966d7.

---

## Work Completed

### 1. Root Cause of Prior Error

The first session task orders were structurally premature for 7 streams:
- A1 (adv_drill): COO pre-specified `Record<architect_key, CumulativeChartView>` — this
  is not something the COO should invent. The DS describes what the gold layer CAN produce,
  the DE specifies what interface the portal NEEDS, the RD identifies chart constraints.
  The agreed shape emerges from that conversation.
- A2 (cla_timeseries): Same issue. COO pre-specified a nested structure including
  `geo_drill: Record<state, CumulativeChartView>` before DS had confirmed whether
  NMNC/NMEC classification data even exists at that grain.
- A3 (stacked_bar/rolling_1y): COO pre-specified exact field names including
  `AdvisorBarEntry = { name, inflows, outflows, nna_net }` and sign conventions.
  The sign convention for outflows (negative number? separate field?) is exactly what
  RD needs to settle based on the chart library they're using — not something COO invents.
- C2, C4, 4C (RD): These were fully specified with chart behavior before DS had agreed
  to produce any particular shape.
- DE A2-gate: Specified a bilateral DE-DS written acknowledgment for NMNC/NMEC logic.
  That conversation IS the Pattern 0 thread — it should not happen out-of-band.

### 2. Corrections Made

| File | Change |
|------|--------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/advisor_intelligence_completion.md` | A1/A2/A3 requirements replaced with "implement per Pattern 0 thread receipt" stubs. A4/A5 kept as immediate starts. Thread staging script paths added to references. |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/advisor_intelligence_completion.md` | C2/C4/4C requirements updated to reference thread receipts as binding specs. C1/C3/H/I unchanged (data exists, no interface dependency). Thread staging script refs added. |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/advisor_intelligence_completion.md` | A2-gate bilateral requirement replaced with thread.1 (DE participates in threads 1+2 to specify TypeScript interfaces). References updated. |

### 3. Pattern 0 Staging Scripts Written

Three self-contained run scripts ready to execute from repo root:

| Script | Thread ID | Streams | Model |
|--------|-----------|---------|-------|
| `run-2026-03-03-continuous-nna-cla-alignment.sh` | 2026-03-03-continuous-nna-cla-alignment | A1 + A2 | gpt-5.3-codex |
| `run-2026-03-03-advisors-stacked-bar-alignment.sh` | 2026-03-03-advisors-stacked-bar-alignment | A3 | gpt-5.3-codex |
| `run-2026-03-03-books-tab-design.sh` | 2026-03-03-books-tab-design | Stream D (Books) | gpt-5.3-codex |

Each script:
- M1 compliant: injects actual Lambda/script/portal source files as code context
- M2 compliant: opening message includes pushback instruction for DS
- M4 compliant: inline briefing describes knowledge source/receiver and deliverable
- M5 compliant: max-turns=3
- M8 compliant: runs BEFORE task orders are actioned
- Model: gpt-5.3-codex (code-grounded thread, per c18966d7 model selection update)
- Turn order: round_robin (3-party: DS -> DE -> RD or DS -> RD -> DE)

### 4. Model Selection Update

Per CTO commit c18966d7:
- Pattern 0 (pre-implementation alignment): gpt-5.3-codex — agents read Lambda handlers, TypeScript types, gold scripts
- Pattern 1 (delivery audit): gpt-5.2-pro — reads session logs, task order status, deliverable state
- Pattern 2 (technical investigation): gpt-5.3-codex — same as Pattern 0 (code-grounded)
- Pattern 3 (cross-pod coordination): gpt-5.2-pro — planning/coordination, no source code needed

Updated all three staging scripts from `MODEL="gpt-4o"` to `MODEL="gpt-5.3-codex"` via sed.
COO prompt already updated by CTO (commit 28c98a78) — no changes needed there.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Replace DS A1/A2/A3 requirements wholesale | Original requirements were detailed enough to be misleading — an agent reading them might implement the specified shape instead of waiting for the thread. Clean replacement is safer than addendum. |
| Keep DS A4/A5 as immediate starts | These have no interface dependency. Bell curve verification and opal-users-v2 investigation produce findings, not shapes. |
| Keep RD C1 and C3 mostly unchanged | C1 (GEO continuous) uses existing geo_drill which has known shape. C3 (CLA snapshot) uses existing header_metrics.json. No new data shapes being agreed. |
| Books tab thread: DS -> RD -> DE turn order | DS surfaces data first (gold layer knowledge source), RD proposes layout (visual constraint surfacer), DE closes with wiring and writes the design brief (synthesis role). |
| Pattern 1 audit deferred | DE and DT have no session logs — O3 risk. Pattern 0 threads (bespoke, code-grounded, tools enabled) do not require logs. Pattern 1 exploratory sync waits for first-activation logs. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/threads/staging/run-2026-03-03-continuous-nna-cla-alignment.sh` | New staging script (A1+A2, gpt-5.3-codex) | No — pending commit |
| `org/threads/staging/run-2026-03-03-advisors-stacked-bar-alignment.sh` | New staging script (A3, gpt-5.3-codex) | No — pending commit |
| `org/threads/staging/run-2026-03-03-books-tab-design.sh` | New staging script (Books D, gpt-5.3-codex) | No — pending commit |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/advisor_intelligence_completion.md` | A1/A2/A3 corrected to thread receipt gates | No — pending commit |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/advisor_intelligence_completion.md` | C2/C4/4C corrected to thread receipt gates | No — pending commit |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/advisor_intelligence_completion.md` | A2-gate replaced with thread.1 | No — pending commit |

---

## Blockers

None. Pattern 0 staging scripts are ready to run. Execute them in any order (A1+A2 and A3 are independent; Books can run in parallel). All three can run before agents have session logs — they are bespoke, tool-enabled, code-grounded threads.

---

## Current State

**Status:** COMPLETE (correction + staging scripts)
**Active branch:** `CLOUD`

Three Pattern 0 staging scripts ready at `org/threads/staging/`. Task orders for DS, RD, and DE corrected to properly gate interface-dependent streams on thread receipts. Immediate-start items unchanged: DS A4+A5, RD C1+C3+H+I, DE I2. The COO's next action after committing this session is to run the 3 Pattern 0 threads and await receipts before any implementation begins on A1/A2/A3/C2/C4/4C/G.

---

## Next Steps

1. **Commit this session block** (staging scripts + corrected task orders + this log)
2. **Run the 3 Pattern 0 threads** — execute from repo root in any order:
   ```bash
   bash org/threads/staging/run-2026-03-03-continuous-nna-cla-alignment.sh
   bash org/threads/staging/run-2026-03-03-advisors-stacked-bar-alignment.sh
   bash org/threads/staging/run-2026-03-03-books-tab-design.sh
   ```
3. **After thread receipts land** in DS/DE/RD threads/ folders: activate each agent
   (DS, DE, RD) with their corrected task orders — they now have grounded contracts.
4. **Pattern 1 audit** (run-exploratory.sh, DE + DT, gpt-5.2-pro): run after DE and DT
   each have at least one session log from their first activation.

**Do NOT:**
- Run the Pattern 0 threads before committing this block (thread receipts reference repo state)
- Ask agents to implement A1/A2/A3/C2/C4/4C before thread receipts are in their threads/ folder
- Add shape specifications to task orders — that is the thread's job
