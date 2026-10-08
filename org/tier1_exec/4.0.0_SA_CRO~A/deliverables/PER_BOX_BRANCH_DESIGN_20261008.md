# Per-box branches -- design, first cut (4.0.0_SA_CRO~A, 2026-10-08 ~18:0xZ)

**Asked by:** Andrew-direct ~17:4xZ, verbatim in the last addenda of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`, call 5
(branch model): *"5.) A for now but we need to get on to B very soon it is a priority."* (A = one trunk, B = per-box.)
Routed to this seat: "keep one trunk now; per-box branches are a priority, design starts now".
**Status:** DESIGN. Nothing is built or changed. Open calls are in section 7.
**Vintage:** laptop, 2026-10-08 17:4xZ-18:0xZ.

---

## 1. What per-box branches fix, and what they do not

**Fix.**
- **Pushes stop racing.** Today four box managers push one branch, `CLOUD`. A push that lands second is rejected,
  so its box fetches, merges and pushes again. Under per-box branches each box pushes only its own branch, so a box's
  push never races another box's.
- **A box's mistake stays on its box until integration.** Today a bad commit on any box reaches every box at the next
  drain. Under per-box branches it reaches `CLOUD` only when the integrator merges that box, after the merge grade.
- **Each box drains on its own clock.** A box under load (site Z today) can stop taking the trunk without stopping
  the others.

**Do not fix.** Commit waiting inside one box: the two-phase commit already handles that, and it is per worktree
whatever the branch. Conflicts between boxes: they move to the integrator and do not go away.

**Cost.** Cross-box visibility gets slower: a commit on dell1 reaches the laptop only after dell1 pushes, the
integrator merges, and the laptop takes the trunk. The one-trunk ruling of 2026-09-24 (LD-0613, commit `da62baab4a`)
retired the earlier two-branch form (`CLOUD` plus `SITEZ`) and its "parity" step. That form had two writers of the
trunk and a merge in both directions. The design below keeps exactly one writer of `CLOUD`.

## 2. The model

| Branch | Who writes it | How |
|---|---|---|
| `box/laptop`, `box/sitez`, `box/dell1`, `box/dell2` | that box's seats commit to it (shared tree checked out on it); that box's manager (MSTR) pushes it | fast-forward push only; it never races, because only one box pushes it |
| `CLOUD` (the trunk) | ONE integrator, nobody else | merges each `box/*` branch in, in a linked worktree, then pushes |
| linked worktrees (workers, drains) | unchanged | branch from the box branch instead of `CLOUD` |

## 3. The four flows

1. **Commit** (every seat): unchanged. `safe-commit` works on the branch checked out; two-phase is per worktree.
2. **Box push** (each box's manager): `git push origin box/<box>`. Fast-forward only. No fetch-merge loop, because
   nobody else writes that branch.
3. **Integrate** (the one integrator): for each `origin/box/*` that is ahead of `CLOUD`, merge it into `CLOUD` in a
   linked drain worktree (fast fix F1's shape), run the grade, run the tree-drop check, and push `CLOUD`. A conflict
   between two boxes stops that box's merge and is resolved there. The other boxes' merges go on.
4. **Take the trunk** (each box's manager): merge `origin/CLOUD` into `box/<box>` in a drain worktree, then
   fast-forward the shared tree (F1 again). This is what keeps every box on current trunk.

## 4. Who integrates

**Recommended: the laptop manager (`0.0.0_AB_MSTR`), with site Z's manager (`0.0.0_AB_MSTR~Z`) as named standby.** It
already runs `/integrate`. One writer means `CLOUD` pushes cannot race at all. A standby takes over only on a recorded
handover. Two live integrators would re-create the race this removes.
Rejected: a GitHub Action merging on GitHub's side. Our grade and tree-drop check run locally, and Actions minutes are
under a budget question (CTO record addendum ~17:0xZ).

## 5. Prior art to reuse

- **The Dells already push per-box branches:** 159 `origin/q/<box>/<branch>/r<N>` branches (99 dell1, 60 dell2). By
  tip author (MEASURED): `2.0.0_SA_COO~M1` 45, `1.0.0_SA_CTO~DELL1` 20, `0.0.0_AB_MSTR~DELL2` 16, `0.0.0_AB_MSTR~DELL1` 14,
  `1.0.0_SA_CTO~DELL2` 13, and the rest at 8 or fewer. 149 of the 159 tips are already in `CLOUD`, so they are integrated
  and simply never deleted. Nothing in `.claude/skills` names them (searched), so how they get merged is not written
  down. Per-box branches replace them with ONE
  long-lived branch per box. The old `q/*` branches are tidied after the cut-over (a delete, so Andrew's word).
- **F1 (drain in a linked worktree, then fast-forward the shared tree)** is already live on the laptop (worktree
  `C:/tmp/drain-20261008T171400Z` seen at 17:1xZ). Flows 3 and 4 are F1 applied twice.
- **Two-phase safe-commit** (`2d3effcf0f`) is branch-agnostic.

## 6. Cut-over (what has to change)

1. **Tooling that names `CLOUD`** (MEASURED, `comp-find '\bCLOUD\b' .tools .claude/skills`, 239 hits across 48 of
   595 files): 5 definition-level, 25 scripts, 8 tests, 11 skill docs. The ones that decide behaviour:
   `.tools/hooks/never-rules-gate.sh` (the shared-branch list: add `box/*`, so no rebase or force-push of a box
   branch); `.tools/git-hooks/pre-push-safe-deploy.sh`; `.tools/surprise-row-gate.py`; `.tools/cleanup-disk.ps1`
   (a worktree is merged when its HEAD is in `origin/CLOUD` OR in its box branch); `.tools/stitch-refresh` (the
   graph's freshness: decide whether it reads `CLOUD` or every `box/*`, see call 3); `/integrate` and `/git-pull`.
   Each of the 48 needs reading once; most will read "the branch checked out" instead of the literal.
2. **The switch on each box, at a quiet moment:** create `box/<box>` at that box's current `CLOUD` tip, push it,
   then `git switch box/<box>` in the shared tree. A switch between two branches at the same commit leaves the working
   files and uncommitted edits as they are.
3. **The integrator's first pass** merges all four box branches into `CLOUD`. They start equal to `CLOUD`, so it is a
   no-op, and it proves the path end to end.
4. **Rollback:** each box switches back to `CLOUD` after one last box-branch merge. Nothing is deleted until the
   model has run clean.

## 7. Open calls (for Andrew; recommendations beneath)

1. **Who integrates?** REC: laptop manager, site Z manager as standby (section 4).
2. **How often does the integrator merge, and how often does each box take the trunk?** REC: event-driven. A box push
   triggers an integrator pass when the integrator next runs `/govern` (now every 30 minutes, Andrew ~17:4xZ). Each
   box takes the trunk on its own `/govern` pass. Cross-box lag is then at most about two governor cycles. That is a
   bound derived from the cadence, not measured.
3. **What does the shared graph read for "current state"?** REC: all four `origin/box/*` branches plus `CLOUD`, so a
   seat sees another box's in-flight work before it is integrated. That is Andrew's "they always know current state".
4. **Order of the cut-over:** REC: site Z first (it is the box under strain today), then the Dells, the laptop last,
   because the laptop is the integrator.

## 8. Not checked

- How often a `CLOUD` push is rejected today: no log records rejected pushes, so the size of fix 1 is not measured.
- How the existing `q/*` branches are merged into `CLOUD` (149 of 159 are in; the 10 that are not were not read).
- The 48 files have not been read one by one.
- The other boxes' tooling copies are assumed to equal the laptop's at the trunk.
