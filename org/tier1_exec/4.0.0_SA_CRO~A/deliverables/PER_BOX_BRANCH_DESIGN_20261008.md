# Per-box branches -- design, first cut (4.0.0_SA_CRO~A, 2026-10-08 ~18:0xZ)

**Asked by:** Andrew-direct ~17:4xZ, verbatim in the last addenda of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`, call 5
(branch model): *"5.) A for now but we need to get on to B very soon it is a priority."* (A = one trunk, B = per-box.)
Routed to this seat: "keep one trunk now; per-box branches are a priority, design starts now".
**Status:** DESIGN, calls answered ~18:0xZ (section 9). Nothing is built yet.
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

## 9. Andrew's answers, 2026-10-08 ~18:0xZ (laptop terminal, to 4.0.0_SA_CRO~A), VERBATIM

> "1.) I like that. 2.) This needs to be structured in a more clever way. I think every 30min "could" work for this,
> but accordingly each MSTR agent would have to structure their govern loop on another part of the hour. e.g. Laptop
> always starts govern loop at top of the hour, Sitez always 6 min past the top of the hour, dell1 always 12 min past
> the top of the hour, dell2 always 18 min past the top of the hour, with the remaining time as buffer before the next
> batch of integrations. It's a very tight schedule and it makes me a little nervous because it doesnt feel size
> invariant, but if our merge process is clean enough (and not overly redundant, e.g. scanning multiple times and etc)
> i think it works. How would you approach with this in mind? 3.) Rec approved. 4.) Rec approved sure."

Then: "Get in touch with CTO and let the conclusions to these points be known quickly because we're already under strain."

**Settled:** (1) the laptop MSTR is the one integrator, with site Z's MSTR as standby on a recorded handover;
(3) the graph reads every `origin/box/*` branch plus `CLOUD`; (4) site Z switches first, then the Dells, the laptop last.

## 10. Call 2: the cadence, made size-invariant (4.0.0_SA_CRO~A's answer to Andrew's question)

Keep Andrew's offsets (laptop :00 and :30, site Z :06/:36, dell1 :12/:42, dell2 :18/:48). Three rules make them a
load-spreading convenience rather than the thing that keeps the boxes safe, so an overrun delays work and never
collides:

1. **Only the integrator writes `CLOUD`; a box writes only `box/<box>`.** The four boxes share no writable ref, so two
   box passes cannot collide, however long either one runs. The only ordering that matters is integrator, then boxes.
2. **Every box pass is: take the trunk first, then push its own branch.** The box branch the integrator merges next
   already contains `CLOUD` as of that box's last pass. Each integration merge therefore carries only that box's own
   new commits and conflicts only with what landed since. Merges stay small however many boxes there are.
3. **The integrator merges ALL boxes that are ahead in ONE pass with ONE grade.** One octopus merge of the box branches
   that are ahead, one tree-drop check, one push. A box that conflicts is dropped from the octopus and merged on its
   own, or held to the next pass. The cost grows with the size of the changes, not with the number of boxes, and
   nothing is scanned twice. **No overlap:** a pass that is still running when its next slot arrives skips that slot.

**Lag:** a commit on any box is in `CLOUD` within one interval after its box's next pass, and on every other box one
pass after that. Under 30 minutes that is roughly 30-60 minutes (a bound from the cadence, not measured). The graph
sees the box branch as soon as it is pushed (call 3), so seats know in-flight work well before it is integrated.

**The one size-variant part is the integrator's grade.** `/integrate` says a large merge grade takes 15-45 minutes
(`.claude/skills/integrate/SKILL.md:65`); dell1 measured a 392-commit merge at 155 s (dell1 draft brief, section 2).
Before the cadence is trusted, 4.0.0_SA_CRO~A (owner of `safe-merge.sh` per 1.0.0_SA_CTO msg 107030) times one real
integration pass and, if the grade is the long pole, makes it grade only the paths the merge changes.

## 11. Andrew-direct ~18:3xZ: merge time, VERBATIM, and what it changes

> "Regarding your comment about potentially long integrate/merge cycles, we need to continually figure out how to get
> time down on the scripts and processess related to those functions. I think if we get on a clean managed schedule as
> is being defined here, it should mitigate that, but we of course want to dive in and explore what is actually the
> root of the issue behind these long merges, which usually are taking that long because they are failing multiple
> times. This is why we need to figure out a method of doing this that is stable and preferably size invariant."

**What it changes:** B3 stops being "time one pass" and becomes the ROOT CAUSE of long merges. Andrew's hypothesis is
that a merge is long because it FAILS and is re-run several times, not because a single run is slow. The measurement
has to count attempts per drain, name what refused each failed attempt (a conflict, the row gate, the tree-drop check,
a hook, an index reset under the merge), and time each attempt. A fix then targets the most frequent refusal class,
and the success measure is "first attempt lands", not a faster single run. Owner: 4.0.0_SA_CRO~A (owner of
`safe-merge.sh`, msg 107030).

## 12. B1 closed: the CLOUD-literal pass (4.0.0_SA_CRO~A, 2026-10-08 ~19:3xZ)

Census: 239 hits in 48 of 595 files (`comp-find 'CLOUD' .tools .claude/skills`, 17:5xZ). Changed, each tested:

| File | Change | Commit |
|---|---|---|
| `.tools/git-hooks/pre-push-safe-deploy.sh` (+ new `test-pre-push-box-deploy.sh`) | B2: deploys on the authoring box's own `box/<box>` push; an integration push of CLOUD deploys nothing | `84bbe98f80` |
| `.tools/hooks/never-rules-gate.sh` | `box/*` is a shared branch (no rebase; integrator-only push/pull) | `7b8188d74a` |
| `.tools/git-hooks/branch-content-isolation-check.sh` | the CL-path refusal also fires on `box/*` | `7b8188d74a` |
| `.claude/skills/integrate/SKILL.md`, `.claude/skills/git-pull/SKILL.md` | BOX PASS, INTEGRATOR PASS, slots, skip-not-overlap; `/git-pull` is a no-op on a switched box | `dfaf3f59b1` |
| `.tools/surprise-row-gate.py` | `origin/box/*` counts as published (landed by 1.0.0_SA_CTO, LOOP_MECHANISM lane) | `1394c97b72` |

**Read and left unchanged, because `CLOUD` stays the trunk:** these name `origin/CLOUD` or `CLOUD` as the trunk (a
merge base, the published trunk, a default ref), and that stays true under per-box branches: `crossbox-deploy-check.py`,
`deploy_ledger.py`, `drift_producer.py`, `integrate-directives.py` (`--a origin/CLOUD` default), `named_commit_check.py`
(an off-trunk commit is admitted when published on any branch, and `origin/box/<box>` is one), `seat-gates-dry-pass.py`
(`--ref CLOUD` default; pass `--ref box/<box>` on a switched box), `sprint-device-census.py`, `comp-schedule`,
`mstr-record-check.py` (test text), `install-mstr-ledger-check.sh` (restricts CL authors to `COMP` only),
`verify-device.sh` (a rebase test string), `inbox-resolver-conformance.py` (comment). `tool_index.py` and `comp-which` match
`MS-CLOUD` / `AWS-CLOUD`, which are not the branch. Not this seat's: `cleanup-disk.ps1` and `worktree_gc.py` (B5,
4.0.0_SA_CRO~B); `stitch-refresh` and `fabric-activity.py` (B4, 4.0.0_SA_CRO); `safe_deploy_core.py` (4.0.0_SA_CRO~B).
Tests and docs that name `CLOUD` as the trunk stay correct for the same reason.
