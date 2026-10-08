# NFRA_CMTQUE (the commit queue) as the GitOps long-term path -- assessment

**Author:** `4.0.0_SA_CRO~A` | **Written:** 2026-10-08 ~16:3xZ | **Asked by:** Andrew-direct ~16:1xZ, verbatim in
`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261008_161xZ_CMTQUE_LONG_TERM_PATH.md` @`aad9d4de4b`.
**Context:** brief `docs/briefs/cluster-gitops-shared-branch-brief-20261008.md` @`58a71ae779`; fast fixes
`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/GITOPS_FAST_FIXES_20261008.md` @`5504357066`.
**Vintage:** laptop only, 2026-10-08 16:1xZ-16:3xZ. Each claim carries its class: MEASURED (run here today), READ
(source or record printed today), INFER (reasoned, not run).

---

## 1. Bottom line

**Do not revive the commit queue as built.** It attacks the smaller of the two git stalls, and reviving it now costs
a re-port of seven gate families plus a CloudWatch alarm set the standing alarm moratorium forbids.

**Take its best idea instead: shrink what runs inside the commit lock.** Today one commit holds the lock for about
11.4 s. Most of that is separate bash and python processes starting up for gates that read only that commit's own
files. Run those gates on a private index before taking the lock, in one process instead of about a dozen, and the
lock only has to cover writing the commit (INFER: a second or two). That gets "agents never wait on each other" without a
new daemon. Put together with fast fix F1 (drain the trunk in a separate worktree), it removes both stalls.

**Keep one trunk.** Per box, the commit lock is busy about a fifth of the time at the laptop's measured peak hour. A
branch-model change would not shorten any single commit, and it would add merges, which are the larger stall today.

## 2. What the commit queue is, and where it stopped (READ)

- **Design** (`docs/architecture/NFRA_CMTQUE_PRD.md`, 2026-07-06, local-daemon substrate Andrew-ratified): agents keep
  calling `safe-commit.sh`, which becomes a thin client that drops a commit request in a local queue. One commit-worker
  daemon per clone commits requests one at a time and hands back the hash. The agent still waits for its hash
  (design decision D1, "semi-sync"), so it waits in an orderly line rather than a spin loop.
- **Built:** worker (`.tools/commit-worker.sh`, 756 lines), queue library (`.tools/commit_queue_lib.sh`), launcher,
  CloudWatch alarms and an SNS (AWS notification service) subscriber (TO-4), gate re-assertion in the worker (TO-5F), a
  concurrency proof script. The supervisor in `org/mcp/server.py:1148-1156` starts the worker only when
  `SAFE_COMMIT_USE_QUEUE=1`.
- **Never switched on:** the load test and cutover (TO-6R) never ran. LD-0255 (2026-07-07) found 100% of commits on the
  old lock. Building it caused a 23-process worker fork storm (LD-0249), later fixed with an atomic singleton (LD-0251).
- **Parked 2026-07-14** on Andrew's word, verbatim: *"Eh i dont care about it honestly at this point, i had already shut
  off 0.7.0~Z because they werent really doing anything and I wanted to save CPU"* (commit `22c3c9f8a3`). Named defects at
  park: a latched worker-down alarm, and "active two-path drift". **Closed 2026-08-25** in the spring clean ("we can
  reinvent a project"); not superseded.
- **Today (MEASURED 16:1xZ):** 0 commit-worker processes on the laptop; `SAFE_COMMIT_USE_QUEUE` is unset, so every
  commit takes the old lock path.

## 3. Where a commit's time goes today (MEASURED, laptop)

One real commit (`aad9d4de4b`, one new file), traced with timestamps on every line of `safe-commit.sh`:

| Segment | Time | How measured |
|---|---|---|
| Before the lock (argument parsing, checks) | 0.46 s | trace |
| **Lock held, in total** | **11.42 s** | trace: lock taken 0.46 s, released 11.88 s |
| -- safe-commit's own gates inside the lock (staging, risk reflex, commit-gate, to-pipeline-gate, decomp lint) | ~2.7 s | trace, 0.46 s to 3.15 s |
| -- the one `git commit --only` call, which runs git's three hooks | 8.48 s | trace |
| ---- pre-commit hook (7 checks of 0.24-0.72 s each) | 3.1-4.0 s | run alone on a private index, twice |
| ---- commit-msg hook (mass-deletion check) | 0.79 s | run alone |
| ---- post-commit hook (5 scripts) plus git writing the commit | ~3.7-4.6 s | INFER by subtraction; not run alone because one script sends PRD header notifications |

A second one-file commit earlier took 12.8 s end to end. Each pre-commit check costs 0.24-0.72 s for a one-file commit,
consistent with process start-up rather than work (INFER). Git itself is not the slow part: refreshing the
63,701-entry index took 0.40 s.

**How busy the lock is (MEASURED, laptop audit log, rows since 2026-10-01).** Peak hour: 70 commits (2026-10-07 09Z),
so 70 x 11.4 s = about 800 s, or 22% of the hour. Peak minute: 4 commits, so about 45 s of lock in 60 s. Waiting is
real in bursts and small on average. The merge window is different in kind: 15-45 minutes during which every commit on
the shared tree is refused (`/integrate` skill text; 91 refusals on the laptop since 10-01, brief finding 3).

## 4. The commit queue against your five long-term items

| Your item | What the queue does | Verdict |
|---|---|---|
| 1. Agents never wait on each other to commit | Replaces the spin loop with a first-in-first-out line, and ends the 60 s lock steal and the timeout storm. The worker still runs the full ~11 s per commit one at a time, so an agent behind four others still waits about 45 s. Its own design D3 (check the next commit while writing this one) overlaps at most two commits. | **Partly.** It makes waiting orderly; it does not make it short. |
| 2. Every box works from current trunk | No effect: it is per clone and touches no fetch, merge or push (PRD section 9 puts the push path out of scope). | **No.** |
| 3. A measured "is git why this box is slow" | Its CloudWatch queue-depth and latency gauges would answer part of it, but they are alarms and metrics under the standing moratorium. | **Not as built.** |
| 4. Shared files cannot conflict | No effect; conflicts happen at merge time, not commit time. | **No.** |
| 5. Branch model decision | No effect. | **No.** |

## 5. What reviving it would cost (READ)

1. **Gate drift.** Since the park, `safe-commit.sh` has had 33 commits and the worker 2. The live path now runs the
   surprise-row gate, the merge refusal, the commit-message verify, the naming gate, the to-pipeline gate, the
   decomposition lint and the risk reflex; the worker names none of them (0 matches for each in
   `commit-worker.sh`, against 1-26 in `safe-commit.sh`, MEASURED by grep). The git hooks are not drifted, because the
   worker still calls `git commit`. Each of the seven would need re-porting and re-proving, and a missed one is a gate
   silently dropped for every commit on the box.
2. **Alarm moratorium.** The design requires delivering CloudWatch alarms (D7; acceptance criterion AC4). CLAUDE.md
   section 5 forbids building alarms or monitors without Andrew's explicit ask. The latched worker-down alarm is a known
   open defect.
3. **One more long-running process per clone**, of the kind the garbage-collection sibling (`4.0.0_SA_CRO~B`) is trying
   to reduce, with the fork-storm history above.
4. **The "commit storm" it was built against is the same defect fast fix F2 removes** (the 60 s steal of a live
   holder's lock). Once F2 lands, the queue's main safety gain is already taken.

## 6. The long-term options for item 1, compared

| Option | What changes | Seats still wait? | Cost and risk |
|---|---|---|---|
| **A. Revive the queue as built** | Worker daemon owns the index | Yes, in line, ~11 s per commit ahead | Section 5. |
| **B. Shrink the locked section (RECOMMENDED)** | Run every gate that reads only the commit's own files on a private index (`GIT_INDEX_FILE`) built from HEAD plus the seat's paths, BEFORE the lock; fold the separate check scripts into one process; inside the lock, only stage onto the current HEAD, run the few gates that depend on HEAD, and write the commit | Only for the locked part (INFER: a second or two, not measured until built) | Each gate must be classed as "reads only its own files" or "depends on HEAD"; a misclass lets a commit through on a stale read. One script, no daemon, no alarm. The private-index read this assessment used to time the hooks shows the mechanism works with today's hooks. |
| C. A worktree per seat | Each seat commits in its own worktree with its own index and lock | No commit wait; merging takes its place | ~2.8 GB per worktree (dell1 measure); every seat's work becomes a merge, which is today's larger stall. |
| D. Lock-free ref update (`git commit-tree` plus `git update-ref` with the expected old value, retried) | No commit lock at all | No | The shared tree's index goes stale under it after every update and must be repaired; no prior art in the estate. Research option only. |

Option B is the queue's own design idea D3 (pipeline the gates, serialize only the commit), carried out without the
daemon. The queue's `commit-worker-concurrency-proof.sh` and acceptance criterion AC1 (ten or more simultaneous commits,
zero timeouts, measured tail latency) are worth reusing as B's load test. The contamination guard that D5 wanted to
retire also becomes unnecessary under B, because the gates read a private index, not the shared one.

## 7. The other four long-term items, briefly

- **2. Current trunk on every box:** once F1 takes the merge out of the shared tree, a drain no longer stops a box, so
  drains can run often (for example, after each push) instead of rarely. Cadence is the project's to set.
- **3. "Is git the cause" per box:** F2's `LOCK-WAIT` and `LOCK-RECLAIM` rows, plus one timing row per commit (lock
  held, hooks), answer it from a file read on demand. That is a log, not a monitor.
- **4. Conflict-free shared files:** there is no stopgap. The union rule (F4) was rolled back at its first use, because
  the surprise channels hold rows inside one JSON list per file (LD-0622). The design answer is one file per writer
  (per box or per seat) that readers join, or a merge driver that understands rows, so two boxes never edit the same
  list.
- **5. Branch model:** at the measured rates, one trunk is not the bottleneck. The commit lock is per clone and busy
  about 22% of the peak hour; the merge window is the stall, and per-box or per-project branches add merges. Your
  decision record should still carry the costs. Per-box branches: fewer pushes racing, but slower cross-box visibility
  (item 2 gets worse). Per-project branches: isolation, but each project's merge back becomes a drain of its own.

## 8. What this assessment does not claim

- Only the laptop was measured. Site Z runs about twice dell1's seats and its commit rate per clone was not read; its
  lock may be busier than 22%.
- Option B's locked time is an estimate until built. The post-commit share is by subtraction, not timed alone.
- The two-path drift list comes from gate names grepped in both files, not from a line-by-line diff, so a gate under
  another name could be missed in either direction.
- Process start-up time on a loaded box (dell1 was at 43% CPU before its cleanup) will be higher than on this laptop
  an hour after a reboot. The per-check costs above are a quiet-box floor.
- Huntress (the endpoint security agent LD-0255 tied to git process churn) is absent from the laptop and was not read on
  site Z today. Option B cuts process starts per commit, which is the direction LD-0255 points, but no effect on Huntress
  is claimed.
