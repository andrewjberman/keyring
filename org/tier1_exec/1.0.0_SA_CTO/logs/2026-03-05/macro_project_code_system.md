# Macro/Project Code System — 1.0.0_SA_CTO

**Date:** 2026-03-05
**Agent:** 1.0.0_SA_CTO
**Branch:** CLOUD

---

## Objective

Design and implement a two-level code system to eliminate conflation between
surface area identifiers (pages, pipelines, cloud processes, research) and
specific project initiatives. One macro can host many projects over its lifetime.

---

## Work Completed

### 1. Problem Identified

`ADVI` was serving double duty as both the AdvisorIntelligence page identifier
AND the project code. V1 completion (threads 001-006) and Yang Feedback V2
(21 work streams) were both registered under the same `ADVI.json`, making
thread serials, task orders, and commits ambiguous across different initiatives
on the same surface area.

### 2. Design

Two-level system:

| Level | Format | Example | Purpose |
|-------|--------|---------|---------|
| Macro code | 4 chars | `ADVI` | Surface area — permanent, never a project code |
| Project code | `{MACRO}_{6CHAR}` | `ADVI_V1VERS` | Specific initiative |

Thread serials: `{PROJECT_CODE}-{NNN}` → `ADVI_V1VERS-007`
Task orders: `{PROJECT_CODE}-{NNN}-{slug}.md`
Project JSON: `org/projects/{PROJECT_CODE}.json`
Scripts: unchanged (treat project code as opaque string)

### 3. Core System Files Updated (commit 3d5fc658)

| File | Change |
|------|--------|
| `PAGE_CODES.md` → `MACRO_CODES.md` | Renamed via git mv; language updated throughout |
| `ADVI.json` → `ADVI_V1VERS.json` | V1 completion project; all 6 threads carry `legacy_serial` fields |
| `ADVI_YANGV2.json` | New — Yang Feedback V2 project, thread_counter 0 |
| `PFMG_VISPOL.json` | New — Trade Engine Visual Polish (PFMG macro) |
| `REGISTRY.md` | Restructured with Macro + Project Code columns |
| `AGENT_START_HERE.md` | Task order filename convention updated |
| `1.0.0_SA_CTO/prompt.md` | New project workflow + MACRO_CODES.md reference |
| `2.0.0_SA_COO/prompt.md` | Project file refs + task order format |
| `threads/THREAD_KNOWLEDGE.md` | M8 + M10 updated to PROJECT_CODE format |
| `threads/README.md` | All examples updated |
| `threads/ARCHITECTURE.md` | Schema, file structure, receipt naming |

### 4. Retroactive Cleanup Task Orders Issued

Scope analysis: 16 task order files and 9 thread receipt files across 5 agents,
plus 3 THREAD.json files in thread folders. Session logs and thread internals
(CONTEXT_COMPILED.md, messages/) are left as-is (historical records).

| Task Order | Issued To | File |
|------------|-----------|------|
| COO scope: THREAD.json + AE/DT task orders | 2.0.0_SA_COO | `org/tier1_exec/2.0.0_SA_COO/task_orders/macro_project_code_retroactive_cleanup.md` |
| Pod 4 scope: DE/DS/RD task orders + receipts | 0.4.0_DE_ClientPlatform | `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/macro_project_code_retroactive_cleanup.md` |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| "Macro code" not "page code" | Surface areas include pipelines, cloud processes, research — not just pages |
| `{MACRO}_{6CHAR}` format | Underscore as separator is readable and valid in filenames; 6-char suffix is human-meaningful |
| `ADVI_V1VERS` for all V1 threads (001-006) | Grandfathering under one project is cleaner than splitting; `legacy_serial` field preserves old IDs |
| Thread folder directory names not renamed | Too disruptive; THREAD.json field update is sufficient for correctness |
| Session logs not renamed | Historical records; renaming would destroy context traceability |
| DE handles all pod 4 renames | DE has commit authority across all pod 4 paths; most efficient in one pass |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/projects/MACRO_CODES.md` | Renamed from PAGE_CODES.md + content update | Yes — `3d5fc658` |
| `org/projects/ADVI_V1VERS.json` | Renamed from ADVI.json + schema update | Yes — `3d5fc658` |
| `org/projects/ADVI_YANGV2.json` | Created | Yes — `3d5fc658` |
| `org/projects/PFMG_VISPOL.json` | Created | Yes — `3d5fc658` |
| `org/projects/REGISTRY.md` | Restructured | Yes — `3d5fc658` |
| `org/AGENT_START_HERE.md` | Task order convention | Yes — `3d5fc658` |
| `org/tier1_exec/1.0.0_SA_CTO/prompt.md` | Project lifecycle protocol | Yes — `3d5fc658` |
| `org/tier1_exec/2.0.0_SA_COO/prompt.md` | Project file refs | Yes — `3d5fc658` |
| `org/threads/THREAD_KNOWLEDGE.md` | M8 + M10 | Yes — `3d5fc658` |
| `org/threads/README.md` | Examples | Yes — `3d5fc658` |
| `org/threads/ARCHITECTURE.md` | Schema + structure | Yes — `3d5fc658` |
| `org/tier1_exec/2.0.0_SA_COO/task_orders/macro_project_code_retroactive_cleanup.md` | New task order | No — local |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/macro_project_code_retroactive_cleanup.md` | New task order | No — local |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE (core system), PENDING (retroactive cleanup)
**Active branch:** CLOUD

Core two-level code system is committed at `3d5fc658`. Two task orders issued for
retroactive file renames: COO handles THREAD.json (3 files) and AE/DT task orders
(2 files); DE handles all pod 4 task order renames (10 files) and receipt renames
(8 files). Going forward, next ADVI V1 thread is `ADVI_V1VERS-007`, next YANGV2
thread is `ADVI_YANGV2-001`.

---

## Next Steps

1. **[COO] Execute `macro_project_code_retroactive_cleanup.md`** — THREAD.json updates + AE/DT renames
2. **[DE] Execute `macro_project_code_retroactive_cleanup.md`** — pod 4 task order + receipt renames
3. **[DT] Push CLOUD** — carry both cleanup commits + session log to remote
