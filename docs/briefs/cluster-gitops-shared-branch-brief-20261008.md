# BRIEF -- GitOps across the cluster: one shared branch, many boxes, 60+ committing seats

**Author:** `4.0.0_SA_CRO` | **Written:** 2026-10-08 ~15:5xZ (UTC) | **Mode:** NEW
**Status: DRAFT handed to `4.0.0_SA_CRO~A`**, which holds the GitOps L1 on Andrew's word of ~16:0xZ
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_160xZ_CRO_BASE_GRAPH_OPS_CRO_A_GITOPS_CRO_B_GC.md`).
`~A` adopts, amends or rewrites it; it is not the brief of record until `~A` says so.
**Asked by:** Andrew, through `1.0.0_SA_CTO` (msg 106963). Verbatim record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md` @`2ecfd5e4fc`.
Related Andrew word, same morning, at this seat: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_154xZ_COHERENCE_CALLS_A_B_YES_DELLS_MAY_WRITE_GRAPH_SHARED_FOLDER_IS_THE_BRANCH.md` @`70950bbf31`.
**Consumer:** `1.0.0_SA_CTO` `/endpoint --forward`.
**Sibling:** process garbage collection (L1 to `4.0.0_SA_CRO~A`; input draft `docs/briefs/process-and-worktree-garbage-collection-brief-20261008.md` on origin @`4d069108b5`).
**Vintage:** laptop shared tree, branch `CLOUD`, 2026-10-08 15:45Z-15:5xZ. Local git and process reads only. No other box was read.

---

## ANDREW'S WORDS, VERBATIM

> "I believe that operating on a shared branch with 60 plus agents that are all committing and pushing and merging and
> doing who knows what at the same time is the root of these complete suffocations, these complete stranglings of
> process. That is on one side, an issue that we need to figure out. ... We need to figure out how we are going to
> handle get ops across the organization, across the cluster. ... we need to move quickly on it."

> "The \"shared folder\" is the shared branch on git in my opinion. The more important thing is the shared graph read
> access so they always know current state when doing things across the estate."

**Two requirements in his words:** (1) find whether, and how, concurrent git work on one branch strangles the boxes,
and fix how the cluster does git; (2) the shared branch IS the cluster's shared working copy. No separate live file
system is wanted. Every seat must be able to read current state.

**The one finding that shapes the brief.** Andrew's hypothesis has not been tested cluster-wide. dell1 measured git as
not the cause on its own box: one git process, no stale lock, a 392-commit merge done in 155 s. The cause there was a
process leak. The laptop read below shows **how git can stall seats without using much CPU**: one commit at a time per
box, and a box-wide refusal of every commit while a merge is open. That is a queue, and it shows up as waiting, not as
load. The brief therefore asks for the cause to be measured per box before anything is cut (O5). It also names the
territory to fix if the measurement confirms it.

---

## PART I -- THE OUTCOME TERRITORY

### THE CANDIDATE THREAD (becomes FWD-1 at L2)

**One box, one seat, one commit through a drain, and its arrival on a second box.**
1. On one box, while that box's integrator is merging the trunk in (a drain), a seat commits a one-file change and gets
   its commit in seconds. It is not refused and not queued behind the drain.
2. The integrator pushes. A seat on a second box, starting its next act, sees that commit, or reads it in the shared
   graph, without anyone messaging it.

This is the smallest journey that crosses all three things Andrew named: committing, merging and pushing. It runs on
two boxes with the concurrency switched on, and each step is something a seat or the integrator does.

### O1 -- A seat commits without waiting on another seat

A seat on a busy box commits its own paths and moves on, whatever the other seats on that box are doing. Today it
waits its turn behind them. Source: Part IV findings 2 and 3.

### O2 -- A seat keeps committing while its box integrates the trunk

The box's integrator fetches, merges and pushes. The box's other seats keep committing while that happens and do not
stop. Today a merge in progress on the shared tree refuses every seat's commit on that box until the merge closes.
Source: Part IV finding 3.

### O3 -- A seat on any box starts from current work

A seat starting an act on any box works from a trunk that holds every other box's committed work, give or take a lag
the seat can read. A seat never unknowingly re-does or contradicts work that another box committed hours earlier.
Source: Part IV finding 5 (the laptop was 445 ahead of origin and 17 behind).

### O4 -- A seat reads current state of the estate before acting across it

A seat about to change a surface of the estate (a Lambda, a bucket, a pipeline, a file other projects touch) reads one
shared place and learns that surface's current state, including whether another box has committed or merged against it.
This is Andrew's "shared graph read access so they always know current state". Source: Andrew's call 4 above. The
graph's fabric layer itself is the coherence project's build (Part II). This project owns the git side that feeds it:
what has been committed, merged and pushed, and on which box.

### O5 -- Andrew asks "is git why this box is slow right now?" and gets a measured answer

Andrew, or a box's integrator, asks the question on any box and gets an answer. The answer separates git's share
(time seats spent waiting on a commit lock, a merge refusal, a push or a fetch) from process load and the other causes.
It is read on demand, not a monitor. This settles Andrew's hypothesis per box and later shows whether the fix worked.
Source: Part IV findings 1 and 6; Part VII.

### O6 -- An integrator lands a box's work without conflict thrash

The integrator on any box merges `origin/CLOUD` and pushes with a conflict set that stays small and is known before the
merge. Repeated collisions on one file, such as a log, a channel or a generated index that several boxes append to,
are designed out instead of being resolved by hand at every drain. Source: Part IV findings 4 and 7.

### O7 -- Andrew picks the cluster's branch model knowing what each costs

Andrew chooses between keeping one shared trunk and the other workable shapes, and the choice is written down with its
cost to O1-O6. The other shapes include per-box branches merged on a cadence, per-project branches, and a
merge-request queue. He confirmed the trunk as the shared copy today. This outcome is the decision record, not a
migration. Source: Part IV finding 8 (the 2026-09-24 one-trunk ruling, LD-0613).

---

## PART II -- WHERE THE BOUNDARY SITS

| This project OWNS | It RELIES ON (owned elsewhere) |
|---|---|
| How a seat commits on a box: the commit path, its lock or queue, and what refuses it | **Process garbage collection** (sibling, `4.0.0_SA_CRO~A`): reaping zombie processes AND stale worktrees. A worktree's disk weight is GC's; a worktree as a way to isolate commits is this project's. |
| How a box integrates: fetch, merge and push by the integrator, and what that blocks | **Multi-agent coherence / the cloud graph's fabric layer** (the brief this seat writes next, as an addition to `NFRA_CTLPLN`, on Andrew's call A of 15:4xZ): BOX, SEAT, COMMIT nodes in the graph. This project supplies the git facts; that one models and serves them. |
| Which branch model the cluster runs (O7) | **NFRA_CTLPLN** (control plane): which boxes may push, the Dell permissions (Dell push to `CLOUD` is lifted, CTO record of 2026-10-08 ~00:4xZ), seat roles. |
| The per-box "is git the cause" read (O5) | **The gates themselves** (owned-paths, surprise-row, ds-precommit, law-lock, never-rules): their rules are not changed here. Only where and when they run in the commit path is in scope. |
| Shared append-only files that collide at every merge (O6) | **The portal repo** (`DEV`/`PROD`): out of scope. It has its own branch discipline. |

Not in scope: the reel's live shared folder (Andrew's call 4: "a category error"; the branch is the shared folder).

---

## PART III -- THE QUALITATIVE BAR

- A seat's commit is never the reason another seat on the same box sat idle. A seat's log never shows "waiting for the
  commit mutex" or "merge in progress, re-run" as the step that cost it its turn.
- A box's integrator can drain the trunk at any hour without telling the box's seats to stop.
- When Andrew calls a box slow, the integrator answers "git: yes or no, and which part" from a read, not from a guess.
  dell1 needed a manual census to rule git out today; under this bar it would not.
- A seat on dell2 does not learn from a merge conflict that the laptop changed the same file this morning. It learns
  that before it starts, from the trunk or the graph.
- Andrew does not have to choose between the boxes being in step and the seats being able to work.

---

## PART IV -- THE SUBSTRATE: what exists, measured

1. **Volume [READ, laptop, `git log` on CLOUD, last 24 h to 15:45Z].** 1,341 commits by 122 distinct author strings, of
   which 304 were merges. The busiest hours were 12Z-14Z at 168, 161 and 140 commits an hour, about one every
   22 seconds. Repo: 61,327 commits, 63,682 tracked files, packs 1.41 GiB in 4 packs.
2. **One commit at a time per box [READ, `.tools/safe-commit.sh:351-387`].** Every safe-commit takes a box-wide mutex
   (`.git/commit-queue.lock`, a `mkdir` lock). A waiting seat polls once a second and gives up after 60 s (exit 3). The
   gates run inside the lock, so the lock is held for the whole gate run. A queued alternative exists, but it is DORMANT:
   `SAFE_COMMIT_USE_QUEUE=1` plus a live worker, "dormant by default ... until the TO-6 canary/cutover"
   (`safe-commit.sh:282-286`). [INFER] Under a busy hour, every gate-second is a second every other seat on the box
   waits.
   **Hazard [READ code, effect INFER]:** a waiter deletes the lock when the lock directory's mtime is 60 s old
   (`:363-372`), even if the holder is alive. A commit whose gates run past 60 s can lose its lock to a second seat,
   and two commits then share one index.
3. **An open merge refuses every commit on the box [READ, `safe-commit.sh` MERGE-REFUSED block, ~:240-267].** While the
   shared tree has `MERGE_HEAD`, every seat's safe-commit is refused with "wait for the merge to finish ... then
   re-run", and "there is deliberately no override". The laptop audit log (`org/git-author-override-audit.log`) records
   MERGE-REFUSED **91 times since 2026-10-01**, plus 8 MERGE-REFUSED-LATE, against 3,877 PASS. Per day: 9, 12, 9, 6, 17,
   8, 23 and 15 (10-08 to 15:44Z). [INFER] That count is a floor on stalls: a seat told to "re-run" may wait and try
   again, and its idle time is not recorded.
4. **The integration path is a merge into the shared tree [READ, `.claude/skills/integrate/SKILL.md`].** One trunk
   since 2026-09-24 (LD-0613). Both MSTRs push `CLOUD`, with fetch plus `merge --no-ff origin/CLOUD` and never a rebase.
   Since the 2026-10-08 Dell lift the Dells push too (Part II). The merge happens in the shared working tree, which is
   what makes finding 3 fire. CLAUDE.md 14b already names the append-only shared file as a guaranteed conflict.
5. **The boxes drift apart [READ, `git rev-list --left-right --count origin/CLOUD...HEAD` at 15:45Z].** The laptop was
   **445 commits ahead of origin and 17 behind.** The handoff of 14:43Z records the laptop's shared tree as "891 commits
   behind origin last night until it was brought level". Origin carries 203 remote branches, including per-box queue
   branches (`origin/q/dell1/CLOUD/r10` and others), so some boxes already publish work on side branches.
6. **The cost of one git read on this tree [READ, timed, laptop].** `git status --porcelain` 1,163 ms with 218
   untracked paths, and 288 ms with `-uno`. None of `core.fsmonitor`, `core.untrackedCache`, `feature.manyFiles` or
   `index.version` is set. [INFER] Every gate that calls `git status` or `git diff` pays this inside the lock of
   finding 2.
7. **Hooks on every commit [READ, `.git/hooks`].** pre-commit (COMP isolation, owned-paths, ledger check),
   commit-msg, post-commit and pre-push (safe-deploy). Their per-commit time was not measured.
8. **Prior art on GitOps shape.** `docs/briefs/opal-ai-gitops-split-brief-20260923.md` (a submodule split for
   `opal_ai`, portal-shaped) shows the estate already uses repo boundaries as a concurrency tool. The portal runs one
   `DEV` with its own rules. The two-branch protocol of 2026-08-12 to 2026-09-24 (per-device SITEZ) was retired for one
   trunk, and its lessons are in `/integrate`.
9. **The other boxes [READ secondhand, dell1 draft section 2].** dell1 had one git process, no stale `.lock`, and a
   392-commit merge in 155 s. Its cause was 63 leaked `typeperf`/`awk` trees, so GC territory. dell1 holds 36 linked
   worktrees of about 2.8 GB and 63,700 files each. The laptop holds 2. Site Z (84 bash, 46 python, 13 claude) had no
   git read.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The per-box cause measurement (O5) has to exist before the fix is chosen, or the fix may land on the wrong cause, as
  it nearly did on dell1.
- The dormant commit queue (finding 2) has an owner and a TO-6 cutover. Whether to revive it, replace it or retire it is
  a PRD question, and the project that built it has not been read (Part VII).
- Any change to which box pushes, or to the merge path, touches LD-0367/0368 and LD-0613, and the control plane's push
  rows. Those are Andrew's and the CTO's.
- The coherence fabric layer (O4) needs a git-side feed per box: commits, merges and pushes with the box named. Box
  attribution in git is inferred from serials today.
- Gate semantics (finding 7) must not weaken. Moving a gate out of the lock is in scope; dropping one is not.
- The GC sibling must not reap a worktree a seat is committing in. The two projects share the worktree.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-08 15:45Z-15:5xZ on the laptop. Status ages; cut nothing from this part.
- `.git/*.lock`: none. git.exe processes: 0. bash.exe 22, python.exe 10, claude.exe 4 (`tasklist`).
- Worktrees: 2. Local branches: 76. Remote branches: 203.
- Ahead/behind origin: 445 / 17.
- MERGE-REFUSED today: 15 to 15:44Z.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **It does not claim git is the cause.** Nothing here measures seat idle time against git. The MERGE-REFUSED count is
  refusals, not minutes lost. dell1's read points the other way on dell1.
- No box but the laptop was read directly. dell2 and site Z had no git measurement at all.
- Whether `org/git-author-override-audit.log` holds other boxes' rows (it is a tracked file and merges carry it) was
  not read. The per-day counts may mix boxes.
- Gate and hook run times per commit, push rejection counts and fetch times were not measured. Neither was how often
  the 60 s lock reclaim of finding 2 has fired.
- The commit-queue project (TO-6) was not read.
- The second safe-commit this session ran in the background, and its duration was not taken.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/cluster-gitops-shared-branch-brief-20261008.md
  PROJECT           NONE-YET (CTO places; candidate home NFRA_CTLPLN beside the coherence addition)
  EXISTING PRD      NONE
  SIBLING PROJECTS  process GC (4.0.0_SA_CRO~A; draft @4d069108b5); coherence fabric layer (CRO brief next, NFRA_CTLPLN);
                    NFRA_CTLPLN (push rights, Dell lifts); opal_ai GitOps split (2026-09-23 brief)
  PRIOR ART         .tools/safe-commit.sh mutex :351-387 + dormant queue :282-286 + MERGE-REFUSED block;
                    .tools/commit_queue_lib.sh; .tools/safe-merge.sh; .claude/skills/integrate/SKILL.md (one trunk, LD-0613);
                    CLAUDE.md 14b (own worktree; append-only shared file inversion)
  MEASURED AT       2026-10-08 15:45Z-15:5xZ, laptop, CLOUD @70950bbf31
```
