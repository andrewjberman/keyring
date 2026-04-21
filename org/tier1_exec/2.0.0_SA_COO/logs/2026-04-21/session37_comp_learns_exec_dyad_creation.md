# COO Session 37 — COMP_LEARNS Project-Scoped Exec Dyad Creation

**Date:** 2026-04-21 (Tue, PM ET)
**Agent:** 2.0.0_SA_COO
**Scope:** Andrew directive — spawn project-scoped execs `1.1.0_SA_CTO` + `2.1.0_SA_COO` so base execs stay on the broader Opal portfolio while COMP_LEARNS runs on its own dyad.

---

## Work Completed

### New agent folders (tier1_exec)

| Path | Contents |
|------|---------|
| `org/tier1_exec/1.1.0_SA_CTO/` | README.md (8.2 KB), prompt.md (9.6 KB), empty `deliverables/`, `logs/`, `task_orders/`, `threads/`, `briefs/` seeded with `.gitkeep` |
| `org/tier1_exec/2.1.0_SA_COO/` | README.md (12.4 KB), prompt.md (12.8 KB), empty `deliverables/`, `logs/`, `task_orders/`, `threads/`, `briefs/` seeded with `.gitkeep` |

Mirrored pattern from the 2026-04-20 tier2 reframe commit `788ef8bb` (which spawned `0.{1,2,3,4}.0_DS_CompLearns`). Numeric prefix `1.1.0` / `2.1.0` is an instance index, not a tier tweak. Both agents are siblings-by-name to `1.0.0_SA_CTO` / `2.0.0_SA_COO` with distinct broker serials.

### Scope boundaries encoded in both agent READMEs + prompts

| Authority | Holder |
|-----------|--------|
| COMP_LEARNS PRDs, harness, ratchet, mutation engine | `1.1.0_SA_CTO` |
| COMP_LEARNS TO decomposition + dispatch + operator/validator loop + closure (steps 1+3) | `2.1.0_SA_COO` |
| Workspace REGISTRY row (closure step 2) + MACRO_CODES + shared infra (LibCST layer, anthropic-sdk layer, `.comp-graph/` schema, `org/compiler-tools-log.md` schema) | `1.0.0_SA_CTO` (base) |
| Cross-project arbitration (COMP_LEARNS blocks/gets blocked by ADVI_ROLLUP etc.) | Andrew via MCP escalation |
| Acceptance flex on COMP_LEARNS `<expect>` deviations | `1.1.0_SA_CTO` (5-min redline window per TO_COMPILER_GATE.md Rule 7) |

Scope lock in both prompts: editing outside COMP_LEARNS scope → STOP, MCP base exec for hand-off, do not commit.

### ORG_CHART.md updated

- Added "Project-Scoped Agents (off-hierarchy)" section documenting COMP_LEARNS dyad (2 execs + 4 DS)
- Total agent count refreshed: 38 (was 32 stale; reality was already 36 post-reframe)
- Tier 1 count: 4 (was 2) — 2 workspace + 2 COMP_LEARNS
- Tier 2 count: 19 (was 15)

### COMP_LEARNS.json updated

- Added `"cto_lane": "1.1.0_SA_CTO"` (new field)
- Changed `"coo_lane"` from `"2.0.0_SA_COO~Z"` to `"2.1.0_SA_COO"`
- Added `"exec_dyad_note"` documenting the succession + workspace-infra authority retention by base execs
- Updated `coo_lane_note` to mark ~Z as succeeded 2026-04-21; prior ~Z session logs retained as historical reference

JSON validated via `python -c "import json; json.load(open(...))"`.

---

## Decisions Made

1. **Naming: `1.1.0_SA_CTO` + `2.1.0_SA_COO`** (not bare `1.1.0_SA_CTO`). Matches the tier2 suffix pattern (`_CompLearns`) and disambiguates from workspace-wide execs. Andrew's shorthand ask was "1.1.0_SA_CTO and 2.1.0_SA_COO" — extended with suffix for convention consistency. Flagged in oriented summary in case he wants bare.

2. **Authority split pattern: shared-infra stays with base CTO**. Registry row moves in closure (step 2 of 3-step atomic) are base-CTO commits; project JSON + PRD status line are project-COO commits. Same pattern recommended for MACRO_CODES, `.comp-graph/` schema, `compiler-tools-log.md` schema, and cross-project AE/DT requests.

3. **Reporting structure: dyad is a peer to base execs, not a subordinate.** Both READMEs explicitly state "sibling exec" / "peer" / "no adjudication authority over each other". Escalation on cross-project resource contention goes direct to Andrew.

4. **TO decomposition discipline inherited verbatim from base COO.** The 2.1.0 prompt references the base COO's locked triad format rather than duplicating it — prevents drift if the format evolves. Same for /loop dynamic mode, RAVC, acceptance flex Rule 7, closure discipline, and commit identity rules.

5. **No tier3 project-scoped RDs needed.** COMP_LEARNS is a research project with no portal frontend; the 4 DS agents are sufficient. Tier3 stays pod-scoped.

6. **`.gitkeep` seeding for empty folders.** Git doesn't track empty directories; seeded `.gitkeep` in each subfolder (`deliverables/`, `logs/`, `task_orders/`, `threads/`, `briefs/`) so the broker + tooling finds the expected structure on first use.

---

## Files Modified

Tracked:
- `org/ORG_CHART.md` (edited: added Project-Scoped Agents section + count refresh)
- `org/projects/COMP_LEARNS.json` (edited: +cto_lane, +exec_dyad_note, ~coo_lane, ~coo_lane_note)

Created:
- `org/tier1_exec/1.1.0_SA_CTO/README.md`
- `org/tier1_exec/1.1.0_SA_CTO/prompt.md`
- `org/tier1_exec/1.1.0_SA_CTO/{deliverables,logs,task_orders,threads,briefs}/.gitkeep`
- `org/tier1_exec/2.1.0_SA_COO/README.md`
- `org/tier1_exec/2.1.0_SA_COO/prompt.md`
- `org/tier1_exec/2.1.0_SA_COO/{deliverables,logs,task_orders,threads,briefs}/.gitkeep`

Out of scope (left untouched in working tree):
- `org/compiler-tools-log.md` — had pre-existing uncommitted state from another session; not my lane
- Other `??` files (schwab TRN enrichment brief, top holdings investigation log, etc.) — other agents' work

---

## Blockers

None.

---

## Current State

Two new exec agents structurally ready. They are NOT yet registered on the MCP broker — first session of each will call `register_agent(...)` and announce. Andrew can spawn terminals under these serials whenever he's ready.

Existing project lane reference updated: any new COMP_LEARNS TO authoring / operator runs should attribute to `2.1.0_SA_COO`, and any PRD amendments should attribute to `1.1.0_SA_CTO`. The prior ~Z lane is superseded but session-log history preserved.

---

## Next Steps

1. **[Andrew]** Spawn terminals for `1.1.0_SA_CTO` + `2.1.0_SA_COO` when ready. First session will register on broker + run ground-truth reconciliation scoped to COMP_LEARNS.
2. **[2.1.0_SA_COO first session]** Run `query_project("COMP_LEARNS")` + `operator COMP_LEARNS --dispatch` to pick up where `~Z` left off — 14 staged TOs + 1 pending (.022) + 1 deferred (.005) — and take it through to closure.
3. **[Base COO — me]** Stay out of COMP_LEARNS unless Andrew explicitly overrides. Continue active work on ADVI_ROLLUP + ADHC_DSFLOW + TRSB_TFIMPT.
4. **[Follow-up]** Consider whether `operator.py` + `validator.py` need any serial-recognition patch to route lane-specific directives. Current impl is `{PROJECT_CODE}`-keyed so should work unchanged — verify at first 2.1.0 session.

---

## Compiler Tools

| Tool | Command | Result | Purpose |
|------|---------|--------|---------|
| Read | `org/tier2_senior/0.{1,2,4}.0_DS_CompLearns/{README,prompt}.md` | Pattern captured | Mirror the tier2 reframe structure into tier1 |
| Read | `org/tier1_exec/1.0.0_SA_CTO/README.md` + prompt.md | Exec template captured | Base for CTO-scoped README |
| Read | `org/tier1_exec/2.0.0_SA_COO/README.md` + prompt.md | Exec template captured | Base for COO-scoped README |
| Read | `org/projects/COMP_LEARNS.json` | Current state captured (phase v4.2, 22 TOs, coo_lane ~Z) | Update lane fields |
| Read | `org/ORG_CHART.md` | Agent-count + hierarchy baseline | Where to add project-scoped section |
| git show | `git show --stat 788ef8bb` | Tier2 reframe commit pattern | Confirms `_CompLearns` suffix convention for project-scoped instances |
| python | `python -c "import json; json.load(open('org/projects/COMP_LEARNS.json'))"` | JSON OK | Post-edit validation |
| git status | `git status --porcelain` | 5 tracked edits + 2 new dirs matching my scope | Pre-commit scope check |

No comp-* runs — pure org/doc work. Compiler tools mandate minimum satisfied by tier2-pattern-inheritance + JSON parse validation.

---

— 2.0.0_SA_COO
