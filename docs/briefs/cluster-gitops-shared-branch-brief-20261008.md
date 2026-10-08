# BRIEF -- GitOps across the cluster: one shared branch, many boxes, 60+ committing seats

**Author:** drafted by `4.0.0_SA_CRO` (~15:5xZ); adopted with amendments by `4.0.0_SA_CRO~A` (~16:0xZ) | **Mode:** NEW
**Status: BRIEF OF RECORD (`4.0.0_SA_CRO~A`, 2026-10-08 ~16:0xZ).** `~A` holds the GitOps L1 on Andrew's word of ~16:0xZ
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_160xZ_CRO_BASE_GRAPH_OPS_CRO_A_GITOPS_CRO_B_GC.md`),
repeated to `~A` at its own terminal, 2026-10-08 ~15:5xZ, VERBATIM: *"I need you on the git ops, that will be your
focus for this session"*. Amendments by `~A` are marked **[~A]**: Part IV findings 2a, 10, 11 and 12, corrections to
findings 3 and 9, Part VI re-measured, Part VII narrowed.
**Asked by:** Andrew, through `1.0.0_SA_CTO` (msg 106963). Verbatim record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md` @`2ecfd5e4fc`.
Related Andrew word, same morning, at this seat: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_154xZ_COHERENCE_CALLS_A_B_YES_DELLS_MAY_WRITE_GRAPH_SHARED_FOLDER_IS_THE_BRANCH.md` @`70950bbf31`.
**Consumer:** `1.0.0_SA_CTO` `/endpoint --forward`.
**Sibling:** process garbage collection (L1 to `4.0.0_SA_CRO~B` since ~16:0xZ; input draft `docs/briefs/process-and-worktree-garbage-collection-brief-20261008.md` on origin @`4d069108b5`).
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
**[~A]** It also separates the processes the commit path itself starts, such as waiters' polling, gates and hooks, from
the processes the sibling GC project reaps, because LD-0255 found the two tangled. It is read on demand, not a monitor.
This settles Andrew's hypothesis per box and later shows whether the fix worked.
Source: Part IV findings 1, 2a, 6 and 10; Part VII.

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
| How a seat commits on a box: the commit path, its lock or queue, and what refuses it | **Process garbage collection** (sibling, `4.0.0_SA_CRO~B`): reaping zombie processes AND stale worktrees. A worktree's disk weight is GC's; a worktree as a way to isolate commits is this project's. |
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
   **2a. [~A] The reclaim is by age alone, it is silent, and waiting is not free [READ `safe-commit.sh:363-372`,
   printed 15:5xZ].** The reclaim tests the lock DIRECTORY's mtime. Nothing refreshes that mtime while the holder
   works, so after 60 s a live holder's lock is deleted on the same terms as a dead one's. The `kill -0` holder test
   above it (`:356-361`) runs first, but it only clears a dead holder; it does not protect a live one from the age
   test. Nothing is logged when the reclaim fires, so how often it has fired cannot be read from any record. Each
   waiting seat runs `cat`, `stat`, `date` and `sleep` once a second (all external binaries in Git Bash), so N waiters
   cost about 4N new processes a second for as long as the lock is held. The cost is a fact about the code. Its effect on the boxes is not measured.
3. **An open merge refuses every commit on the box [READ, `safe-commit.sh` MERGE-REFUSED block, ~:240-267].** While the
   shared tree has `MERGE_HEAD`, every seat's safe-commit is refused with "wait for the merge to finish ... then
   re-run", and "there is deliberately no override". The laptop audit log (`org/git-author-override-audit.log`) records
   MERGE-REFUSED **91 times since 2026-10-01**, plus 8 MERGE-REFUSED-LATE, against 3,877 PASS. Per day: 9, 12, 9, 6, 17,
   8, 23 and 15 (10-08 to 15:44Z). [INFER] That count is a floor on stalls: a seat told to "re-run" may wait and try
   again, and its idle time is not recorded.
   **[~A] Correction and split:** the log is NOT tracked (`git ls-files --error-unmatch` fails), so it is device-local
   and these counts are the laptop's alone; none of the 4,322 rows since 10-01 carries a `~Z` or `DELL` serial. The 91
   refusals by refused seat: `1.0.0_SA_CTO` 25, `4.0.0_SA_CRO` 14, `3.0.0_SA_CVO` 12, `2.0.0_SA_COO~Y` 8, `~P` 7, `~D` 6,
   `~C` 6, `~M` 5, with the remaining 8 seats at 3 or fewer each. Tier-1 seats take 51 of the 91.
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
   git read. **[~A] What origin shows instead [READ, `git log origin/CLOUD --since='24 hours ago'` by author suffix,
   15:5xZ]:** every box writes the trunk. `~Z` 168, `~M1` 104, `~RV` 99, `~C` 94, `0.0.0_AB_MSTR` 92, `~DELL2` 85,
   `~H` 76, `~DELL1` 73, then 18 more author strings below 60. A suffix names a lane, not a box, so the per-box split is
   inferred (Part V already notes that git carries no box field).
10. **[~A] The fix for this has been built before and is parked [READ `docs/architecture/NFRA_CMTQUE_PRD.md` status
    line; `org/tier0/ledger/LD-0255.md`; commit `22c3c9f8a3`].** NFRA_CMTQUE, a local commit-worker daemon (substrate
    Andrew-ratified 2026-07-06), was built to "manage the choke on commits" when the fabric is hot. LD-0255
    (2026-07-07) found its queue path dormant fabric-wide, with 100% of commits on the mutex of finding 2. It also found
    the build had caused a 23-process commit-worker fork storm (LD-0248/0249), and it measured the Huntress endpoint
    agent (`Rio.exe`) leaking about 34 MB a minute on the laptop, a leak Andrew linked to git process creation. Andrew,
    2026-07-07, VERBATIM (from LD-0255): *"we need to figure out our commit queue process better, the whole idea is that
    when the fabric is super hot, it should manage the choke on commits, but i suspect that first of all its not
    working and second its causing Huntress to go haywire"*. The project was moved to Inactive/On-Hold on 2026-07-14
    (`22c3c9f8a3`). This is the same hypothesis Andrew states today, three months earlier. Its PRD and its parked TO-6
    cutover are the first prior art the PRD must read before it buys anything new.
11. **[~A] Endpoint agent today [READ `Get-Process`, laptop 15:56Z].** No process matching
    huntress/rio/sentinel/crowd is running on the laptop now. Whether Huntress was removed, renamed or runs under
    another name was not established. LD-0255's leak therefore cannot be re-measured here today. The other boxes were
    not read.
12. **[~A] Ruled out on the laptop: OneDrive sync of the repo [READ registry, 15:5xZ].** The Desktop is not redirected
    into OneDrive (`User Shell Folders\Desktop` = `C:\Users\AndrewBerman\Desktop`; the business OneDrive root is
    `C:\Users\AndrewBerman\OneDrive - Opal Capital`). The OneDrive sync service holds 816 MB of working set, but the
    repo is outside its root.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The per-box cause measurement (O5) has to exist before the fix is chosen, or the fix may land on the wrong cause, as
  it nearly did on dell1.
- The dormant commit queue (finding 2) belongs to NFRA_CMTQUE, which is parked with its TO-6 cutover never run
  (finding 10). Whether to revive it, replace it or retire it is a PRD question. LD-0255's fork-storm and EDR findings
  bind whichever is chosen.
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
- **[~A] Re-read 15:56Z:** HEAD `8b4f996b64`; ahead/behind origin 445 / 21; origin `CLOUD` tip `4d069108b5`
  (2026-10-08 15:24Z); no `.git/*.lock` and no `commit-queue.lock`. Laptop processes at 15:50Z: 350 in total; bash 19,
  python 10, powershell 5, claude 5 sessions; CPU 22% over 8 cores; 14.3 of 31.7 GB RAM free; booted 14:51Z.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **It does not claim git is the cause.** Nothing here measures seat idle time against git. The MERGE-REFUSED count is
  refusals, not minutes lost. dell1's read points the other way on dell1.
- No box but the laptop was read directly. dell2 and site Z had no git measurement at all.
- **[~A]** The audit log's scope is settled: it is untracked and device-local, so its counts are the laptop's alone
  (finding 3). No other box's refusal count exists in this brief.
- Gate and hook run times per commit, push rejection counts and fetch times were not measured. How often the 60 s lock
  reclaim of finding 2 has fired cannot be measured, because nothing logs it (finding 2a).
- **[~A]** NFRA_CMTQUE was read at the level of its PRD status line, LD-0255 and the park commit only. Its TO-6
  cutover plan, its worker code and why Andrew was indifferent to it on 2026-07-14 were not read.
- **[~A]** The laptop rebooted at 14:51Z, so every process count in this brief describes a box about an hour from a
  clean start. It is not the state a slowdown builds up to.
- The second safe-commit this session ran in the background, and its duration was not taken.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/cluster-gitops-shared-branch-brief-20261008.md
  PROJECT           NONE-YET (CTO places; candidate home NFRA_CTLPLN beside the coherence addition)
  EXISTING PRD      NONE for this project; the parked NFRA_CMTQUE PRD docs/architecture/NFRA_CMTQUE_PRD.md covers
                    the commit-queue half of O1 (finding 10)
  SIBLING PROJECTS  process GC (4.0.0_SA_CRO~B; draft @4d069108b5); coherence fabric layer (CRO brief next, NFRA_CTLPLN);
                    NFRA_CTLPLN (push rights, Dell lifts); opal_ai GitOps split (2026-09-23 brief);
                    NFRA_CMTQUE (Inactive/On-Hold since 2026-07-14, @22c3c9f8a3)
  PRIOR ART         .tools/safe-commit.sh mutex :351-387 (reclaim :356-376) + dormant queue :282-286 + MERGE-REFUSED block;
                    .tools/commit_queue_lib.sh; .tools/safe-merge.sh; .claude/skills/integrate/SKILL.md (one trunk, LD-0613);
                    CLAUDE.md 14b (own worktree; append-only shared file inversion);
                    org/tier0/ledger/LD-0255.md (commit choke + EDR process-creation finding, 2026-07-07)
  MEASURED AT       2026-10-08 15:45Z-15:5xZ, laptop, CLOUD @70950bbf31 (draft);
                    15:50Z-15:56Z, laptop, HEAD @8b4f996b64 ([~A] amendments)
```
