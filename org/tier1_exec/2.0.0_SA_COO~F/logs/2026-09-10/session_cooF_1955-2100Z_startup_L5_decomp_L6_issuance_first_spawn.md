# IRPT_FNTEND round 1: seated, decomposed, issued, first worker spawned -- 2.0.0_SA_COO~F

**Date:** 2026-09-10
**Task Order:** IRPT_FNTEND L5 + L6 (COO lane limbs), L7 in flight
**Status:** IN PROGRESS
**archetype:** COORDINATE
**Workspace CLOUD commits (LOCAL):** `8ace3a2596` (L5) -> `3ceb5201cb` (L6)

---

## Objective

Seat this lane on IRPT_FNTEND, cut the L5 decomposition from PRD v0.4, cut the L6 issuance covering every cell, and open L7 with the first worker. All from the version of the PRD that stood at the cut, with the controls measured rather than assumed.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-adversary | `comp-adversary compose org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md` | PASS | 5 complement sources run / 0 deferred / 4 declared-excluded; all pins read-vintage |
| comp-cache | `comp-cache collisions` | PASS | 415 files scanned; 0 keys under `investor-reporting`; key rule bound in every face |
| comp-blast | `comp-blast component:portal/src/App.tsx` (+ PageSurfaceControl, TabNavigation, ModelPortfolios) | PARTIAL | PRESENT_WITH_ZERO_RESULTS, extracted edges only (lower bound); a bare path is AMBIGUOUS-SUBJECT (2 nodes) and refuses -- pass the `component:` id |
| comp-blast | `comp-blast portal/src/components/CategoryViewTree.tsx` | WARN | SUBJECT_ABSENT_FROM_CORPUS while the file exists at portal `5907cbca`; graph blindness recorded in the decomp battery |
| comp-surprise | `comp-surprise --project IRPT_FNTEND` | WARN | 0 items over 56 files; the rollup reads the legacy root; the tree channel opens on the first row |
| comp-find | `comp-find --name '*' org/missions/D9 --limit 60` | PASS | 4 of 4 files at L3; used again for the decomp lint and tree-index tool discovery |
| comp-read | `comp-read <file> --for/--enumerate` on the gate, the dispatch skill, ui-smoke, ModelPortfolios, App.tsx | PASS | enumerate with a printed denominator replaced every grep |
| to-pipeline-gate | `python .tools/to-pipeline-gate.py <11 orders>` with the row staged at DECOMP | PASS | issuance coverage 11 of 11; the only refusal was the EXECUTING flip the issuance commit carries |
| surprise-row-gate | on an EMPTY channel file, staged | FAIL (correct) | "a channel file mints on an item"; the empty file was removed and every face tells the worker to create it with its first row |
| missions-tree-index | `derive --write` then `check` | PASS | INDEX-DRIFT after each row flip, cleared by regeneration; 0 violations at both commits |
| proof-of-spec-check | `CELL_ID_RE` loaded from the module and applied to the decomp and the 11 orders | PASS | 11 distinct cell-shaped tokens in the decomp, 0 phantoms; every order owns one cell, union = 11 |

**What worked:** `comp-read --enumerate` with its denominator for every "what does this tool read" question; loading the enforcer's own regex instead of eyeballing ids; staging the orders to pre-grade coverage with the row still at DECOMP.
**What failed:** `comp-surprise --limit` is not a flag (rc 2); `comp-blast` on a bare portal path refuses as ambiguous; `to-pipeline-gate` on UNTRACKED files reports "0 newly-added" and grades nothing -- files must be staged for it to see them.
**Gap found:** the workspace tracks `portal/` as a gitlink, so no estate instrument (owned-paths hook, safe-commit's gates, comp-blast on the served graph) sees a portal commit; the `<paths>` grant on portal paths binds by reading only. Recorded in the decomp (s.7 item 7) and every face.

---

## Work Completed

### 1. Startup and preparation
Registered `2.0.0_SA_COO~F` (PID 11064), inbox Monitor `bc5d23hea` armed and confirmed running, session serial file written, PATH 104 of 104 comp-tools. Read in full: the FE brief (215 lines), both endpoints (12 blocks), the BK contract inventory (11 contracts), the CTO's three Andrew-direct records on execution-only PRDs and on the silent watch of this lane. Acked 95543 (COO base preparation), 95559 (L4 landed), 95578 (v0.2), 95588 (v0.3), 95596 (v0.4).

### 2. L5 decomposition -- `8ace3a2596`
`org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md` v0.1: eleven cells `FE-s-1..11` over three write surfaces, cut from PRD v0.4 @`62301f71e0`. Re-cut map 14 of 14 candidates (F1+F2, F3+F7, F12+F14 merged; F9 made the shared renderer). Rule 24 record over three domains (8 outcomes, 14 candidates, 8 manifest rows), 0 uncovered each. Edges: one component, one ready root, waves A..G, max width 3. Battery: comp-schedule and comp-iam declared not applicable with reasons; adversary, cache, blast, surprise, path existence (23 of 23 reuse, 16 of 16 fixtures, 2 of 2 new homes absent) and instrument availability RUN. Row flipped PRD -> DECOMP; flat index regenerated.

### 3. L6 issuance -- `3ceb5201cb`
Eleven task orders at `org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-<n>.<slug>.md`, two faces each. 78 mechanical criteria (one invocation, one expect each) and 9 judgment criteria. Every face carries the two-repo commit path, the `<paths>` grant, the bounds, the surprise-row instruction and the proof-of-spec instance name. `fanout: 1 of 1 chains, cap 8` as data in the commit message; slots ~1 (queue of 7), ~2 (FE-s-4 -> FE-s-8), ~3 (FE-s-6), ~4 (FE-s-7). Row flipped DECOMP -> EXECUTING in the same commit; index regenerated.

### 4. L7 opened
Worktree pair for slot ~1 cut from HEAD `3ceb5201cb`: `/c/tmp/wk-irpt_fntend-1-1-fe-s-1` (workspace, branch `wk-irpt_fntend-1-1-fe-s-1`) with the portal repo checked out INTO its `portal/` gitlink directory on a branch of the same name from DEV `5907cbca`, `node_modules` a junction to the main checkout (measured on a probe: typecheck rc 0 in 17 s). Worker `0.9.0_WK_IRPT_FNTEND~1` spawned on FE-s-1 with the face verbatim plus the identity line. The spawn is the GO.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| FE-s-1 (contracts + typed client + fixture adapter) is the single root | every other cell consumes its types and fixtures; a shared shape copied per cell is the drift the brief forbids |
| The render package owns the performance and Analysis layout components; the Reporting tab mounts them | preview-to-PDF parity becomes structural rather than a comparison after the fact |
| One fresh worktree pair per ORDER, not per slot | a terminal subagent cannot be resumed here, and a re-used worktree leaves later faces and dependencies off its branch |
| The portal worktree lives inside the workspace worktree's `portal/` gitlink directory | workspace-relative `portal/...` paths in `<paths>` resolve exactly as in the main tree |
| Coverage pre-graded with the row at DECOMP, then flipped in the issuance commit | the gate grades coverage only at DECOMP; the spine wants the flip in the issuance commit; staging briefly satisfied both |
| No empty channel file in the issuance | the row gate refuses a zero-row channel; the first worker row opens it |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md` | new, v0.1 | Yes -- `8ace3a2596` |
| `org/missions/D9/IRPT/IRPT_FNTEND/task-orders/*.md` (11) | new | Yes -- `3ceb5201cb` |
| `org/missions/D9/IRPT/IRPT_FNTEND/project.json` | dep_stage PRD -> DECOMP -> EXECUTING; decompositions[] | Yes -- both |
| `org/projects/IRPT_FNTEND.json` | regenerated | Yes -- both |

---

## Blockers

None at this seat. The next act, the drain of FE-s-1, is gated on the worker's report and its proof-of-spec instance, which is the spine's own sequencing.

---

## Current State

IRPT_FNTEND reads `dep_stage EXECUTING` at `3ceb5201cb`. One order (`FE-s-1`) is `pending` with worker `0.9.0_WK_IRPT_FNTEND~1` executing in `/c/tmp/wk-irpt_fntend-1-1-fe-s-1`; ten orders read `blocked` on their named dependency. The portal repo has no Investor Reporting code on DEV yet; the first code lands on the worker's portal branch and is merged into DEV at the drain. All workspace commits are LOCAL on CLOUD; this seat does not push.

---

## Next Steps

1. **Drain FE-s-1** -- read the WORKER REPORT and the instance; `safe-merge.sh` the workspace branch (merged-index row gate); merge the portal branch into DEV; remove both worktrees and branches.
2. **Seat FE-s-2 (slot ~1) and FE-s-4 (slot ~2)** in fresh worktree pairs from the post-drain HEAD; ports 5181 and 5182.
3. **Continue the queues** as dependencies land: FE-s-3, then FE-s-5/6/7 (max width 3), FE-s-8, FE-s-9, FE-s-10, FE-s-11.
4. **L10** -- ONE message to `1.0.0_SA_CTO` after every order is terminal and every row dispositioned, carrying the CVO watermark against the channel row count and any armed row this lane could not seat, plus the workspace `portal` gitlink pointer left at `5907cbca` (its move is a separate act).
