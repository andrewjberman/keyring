# GitOps FAST FIXES -- ship-today list (4.0.0_SA_CRO~A, 2026-10-08 ~16:1xZ)

**Asked by:** `1.0.0_SA_CTO` msg 106976, carrying Andrew-direct ~16:0xZ, verbatim in the addendum of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`
@`fdef7ad167`: *"these briefs dont necessarily have to be full on registered projects, just yet ... we need to get fast
solutions out across the boxes while we get organized"*.
**Brief behind it:** `docs/briefs/cluster-gitops-shared-branch-brief-20261008.md` @`58a71ae779`.
**Vintage:** laptop, 2026-10-08 15:50Z-16:1xZ. Git 2.55.0.windows.2, bash 5.3.15. No other box was read.

Ordered by expected relief. The seat named under each fix applies it, and only on its own box. A fix to a tracked file
reaches the other boxes by the trunk. A config fix does not travel, so each box's MSTR applies it itself.

---

## F1 -- Drain the trunk in a linked worktree, not in the shared tree

**Why [READ].** `/integrate` Step 1 (`.claude/skills/integrate/SKILL.md:36` and the merge-window bullet below it) merges
`origin/CLOUD` into the SHARED tree with `--no-commit` and lets the merge commit's hooks grade the whole merged index:
"on a large merge that is 15-45 minutes". `MERGE_HEAD` is open for that whole window, and `safe-commit.sh` refuses every
commit on that tree with no override (brief finding 3: 91 refusals on the laptop since 10-01). `MERGE_HEAD` and the
commit lock are per WORKTREE, not per box: a linked worktree has its own git dir (measured:
`C:/tmp/wk-ctlpln-14` -> `.git/worktrees/wk-ctlpln-14`). A drain in a linked worktree therefore refuses nobody.

**Change (the `/integrate` Step 1 text; no code).**
1. `git worktree add <scratch>/drain-<ts> -b drain/<box>/<ts> CLOUD`.
2. In it: `git fetch origin`, then `bash .tools/safe-merge.sh origin/CLOUD`. The long grade runs here, and the shared
   tree keeps committing. Run the TREE-drop check (`--diff-filter=D`, same skill) here, before anything moves.
3. Catch-up, in the worktree: merge the local commits that landed on `CLOUD` during the grade
   (`bash .tools/safe-merge.sh CLOUD`). This delta is minutes of one box's commits, so its grade is short.
4. In the shared tree: `git merge --ff-only drain/<box>/<ts>`. A fast-forward opens no `MERGE_HEAD` and runs no commit
   hook, so it takes seconds. If it refuses because `CLOUD` moved again, repeat step 3.
5. Push from the shared tree as today, then `git worktree remove` the drain worktree and delete its branch.

**Who / where.** `0.0.0_AB_MSTR` edits the skill text. Each box's integrator (`0.0.0_AB_MSTR`, `~Z`, `~DELL1`,
`~DELL2`) drains this way from its next drain on.
**Rollback.** Drain as Step 1 reads today. Nothing persists apart from the skill text.
**Cost if wrong.** Step 4 fails safe: git refuses a fast-forward that would overwrite a local modification. The real
risks are a missed tree-drop check (step 2 must run it before step 4) and a 2.8 GB worktree per drain while it exists,
which the GC sibling (`4.0.0_SA_CRO~B`) must not reap mid-drain. Worst case, the integrator falls back to today's path.

## F2 -- Make the commit lock's reclaim liveness-based, logged, and spawn-free

**Why [READ `.tools/safe-commit.sh:351-387`].** A waiter deletes the lock once the lock DIRECTORY is 60 s old
(`:363-376`). Nothing refreshes that mtime, so a LIVE holder whose gates run past 60 s loses its lock, and two commits
share one index. The reclaim logs nothing. Each waiter runs `cat`, `stat`, `date` and `sleep` every second, which is
about 4 new processes a second per waiter. The one timed one-file docs commit took 12.8 s end to end (16:0xZ), so a
60 s gate run is plausible for a larger commit.

**Change (one commit to `.tools/safe-commit.sh`, legacy lock loop only).**
- Read the holder with the builtin `read -r holder_pid < "$LOCK_DIR/pid"`.
- Reclaim only when (a) `kill -0` says the holder is dead, (b) no pid file has appeared for 10 consecutive polls, or
  (c) this waiter has seen the SAME live holder for `SAFE_COMMIT_LOCK_STALE_SEC` (default 600), counted by the waiter's
  own loop counter and not by mtime. **[SUPERSEDED: as listed, (c) could never fire, because a waiter gives up at 300 s
  before it has watched a holder for 600 s (found by `0.0.0_AB_MSTR`, LD-0622). `1.0.0_SA_CTO` ruled the default to
  240 s under the 300 s give-up (msg 106997).]**
- Append a `LOCK-RECLAIM <holder> <reason>` row to the audit log on every reclaim. Append `LOCK-WAIT <seconds>` on any
  acquisition that waited. This gives the brief's O5 its first measured git-wait number from today.
- Wait with `read -t 1` on a held-open FIFO (the no-spawn pattern of `org/mcp/inbox-watch.sh`, `_wait5`) in place of
  `sleep 1`. Fall back to `sleep` if `mkfifo` fails.
- Raise the waiter's give-up (`SAFE_COMMIT_LOCK_TIMEOUT`, exit 3) from 60 s to 300 s. Without the age reclaim, a waiter
  behind a long, legitimate gate run should wait, not fail.

**Who / where.** `0.0.0_AB_MSTR` (fabric infrastructure). One commit, carried to every box by the trunk. Before it
lands: `bash -n`, then a two-waiter exercise against a scratch lock dir (`SAFE_COMMIT_LOCK_DIR` is already an override)
with the holder kept alive past 60 s, as positive control, and killed, as negative control.
**Rollback.** `git revert` the one commit.
**Cost if wrong.** HIGH BLAST RADIUS: every commit on every box goes through this loop, so a syntax or logic error stops
the fabric committing. That is why the exercise is a precondition. A hung live holder now blocks its tree for up to 10
minutes instead of 1. The trade is deliberate: today that case silently corrupts the index.

## F3 -- Turn on git's untracked cache on every clone

**Why [MEASURED, laptop shared tree, 3 runs each, 16:0xZ].** `git status --porcelain` took 776-1,027 ms. With
`core.untrackedCache=true` it took 402-464 ms warm (837 ms on the first, cache-filling run). Every gate that calls
`git status` pays this inside the commit lock (brief finding 6). `git update-index --test-untracked-cache` on the C:
volume: OK.

**Change.** `git config core.untrackedCache true` in each clone, then one `git status` to fill the cache.
**Who / where.** Each box's MSTR, on its own clone, once (config is per clone and does not travel by the trunk). Run
`git update-index --test-untracked-cache` on that box's volume first, and skip the box if it fails.
**Rollback.** `git config --unset core.untrackedCache`.
**Cost if wrong.** Low. On a filesystem with unreliable directory mtimes git could miss a new untracked file in a
status read, and the test above guards that. **Left out on purpose:** `core.fsmonitor=true` measured faster still
(241-537 ms), but it starts a persistent `git fsmonitor--daemon` per worktree, the process class the GC sibling is
reducing. The test daemon this seat started was stopped at once (`git fsmonitor--daemon stop`). That call is
`4.0.0_SA_CRO~B`'s.

## F4 -- A union merge driver for the append-only shared files

**ROLLED BACK (2026-10-08 ~16:4xZ, `0.0.0_AB_MSTR` msg 106995, LD-0622, commit `a769a69d2a`; rollback accepted by
`1.0.0_SA_CTO` msg 106997).** At its first real use, union auto-merged both `INVESTIGATION_v1.md` files and the row gate
refused the merged index: the rows sit inside ONE JSON list per file, and union inserted them at different points,
leaving an unparseable block. A conflict would have returned the drain to `safe-merge --continue`; the union left no
such path. **This list's error:** it called these files line-appended without reading their format. A row-aware driver,
or one file per writer, is project work under brief O6. The text below is kept as written.

**Why [READ].** CLAUDE.md 14b: two branches appending to one surprise channel "land at the same offset and guarantee a
conflict". `/integrate` already tells the integrator to resolve an append collision as a UNION by hand, as was done in
`df1ab13b26` ("surprise-channel append collision resolved as a union"). Each such conflict stops a drain for a human
resolution.

**Change (one commit to `.gitattributes`).**
```
org/missions/**/surprise-channel/investigations/INVESTIGATION_v*.md merge=union
org/surprise_channel/**/INVESTIGATION_v*.md merge=union
```
**Who / where.** `0.0.0_AB_MSTR`. One commit, carried by the trunk to every box.
**Rollback.** Delete the two lines.
**Cost if wrong.** If a row in these files is EDITED in place on both sides, union keeps both versions with no conflict
marker, so a silent duplicate replaces a loud conflict. The surprise-row gate grades rows at commit time but does not
run on a fast-forward. Scope is deliberately limited to these two patterns. Other append-only logs are not added
until each one's edit pattern has been read.

---

## Not on the list, and why

- **Reviving the NFRA_CMTQUE commit queue** (brief finding 10): not ship-today. It needs its parked TO-6 cutover read
  and LD-0255's fork-storm and EDR findings answered.
- **A per-box "is git the cause" read (brief O5):** F2's two log rows are its ship-today seed. The full read is the
  project's.
- **Branch-model change (brief O7):** Andrew's call. Nothing on this list changes the one-trunk model.

## What this list does not claim

- Only the laptop was measured. The F3 timings and the F1 refusal count do not transfer to the other boxes as numbers.
- F1 assumes `safe-merge.sh` behaves the same in a linked worktree. Its own header says it resolves state per worktree
  (`--git-path`), but that was read, not run, for this list.
- F2's change was specified, not written or exercised.
