# FAST FIX list: process garbage collection and script ops (ship today)

**Author:** 4.0.0_SA_CRO~B, 2026-10-08 ~16:1xZ, on the CTO's msg 106977 (Andrew-direct ~16:0xZ, addendum in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`
@fdef7ad167: "we need to get fast solutions out across the boxes while we get organized").
**Full brief (projects later):** `docs/briefs/process-garbage-collection-and-script-ops-brief-20261008.md`.

## Measured on the laptop at 16:0xZ, the basis for FF1 and FF3

| Arm | Act | typeperf / awk left running |
| --- | --- | --- |
| A | bash running `typeperf -si 1 \| awk`; `Stop-Process` on the bash wrapper only (what the harness and `kill-maint.ps1:205` do) | **1 / 1** -- dell1's leak, reproduced |
| B | same tree; `taskkill /T /F /PID <wrapper>` | **0 / 0** |
| C | same pipeline under `timeout 4 bash -c '...'` | **0 / 0** (rc 124) |

## The list (four items; Andrew's word is needed to run anything unattended -- see the end)

### FF1 -- stop whole trees, not single PIDs
- **Change:** in `.tools/kill-maint.ps1`'s kill step (:205), replace `Stop-Process -Id` with `taskkill /T /F /PID`.
  Skip any target whose descendants include a `claude.exe`.
- **Applies:** 0.0.0_AB_MSTR (laptop): one commit to CLOUD. **Boxes:** all, on their next pull.
- **Rollback:** revert the one commit.
- **Cost if wrong:** a tree stop could reach a live process parented under an orphan. The claude.exe skip covers
  the case that matters (a seat); anything else under an orphan already has no live owner.

### FF2 -- target the classes the reaper misses today (CTO gaps 1, 2, 3, 4)
- **Change:** in `.tools/kill-maint.ps1` scripts mode, add four classes:
  - (a) **REPLACED:** more than one `inbox-watch.sh ... stream`, `agent-poller.py` or `agentbus-sqs.sh watch` row
    for the same owner. Take the serial from the command line and compare it with `-eq` (the `/watcher` census
    rule, never a substring match). Keep the newest; target the rest.
  - (b) **ORPHANED infra:** a watcher or poller whose serial is not live in `org/mcp/liveness.json`. This is the rule
    `kill-orphans --stale` already uses.
  - (c) **Native long-runners:** `typeperf`, `awk`, `tail` or `timeout` outside every live claude tree.
  - (d) **Dead-session Bash-tool shells:** drop the `shell-snapshots` exemption (:86). A live session's shells are
    already protected as claude descendants.
- **Applies:** 0.0.0_AB_MSTR, in the same commit as FF1. **Boxes:** all, on pull.
- **Rollback:** revert.
- **Cost if wrong:** class (a) or (b) stops a live seat's watcher, and that seat is deaf until it re-runs
  `/watcher`. The Monitor's exit notice tells it. Dry run is still the default, so the operator reads every target
  before `go`.

### FF3 -- bound every hand-armed Monitor
- **Change:** add one line to the Traps of `.claude/skills/watcher/SKILL.md`, which every seat loads at startup: "A
  Monitor command you write by hand runs as `timeout 1790 bash -c '<cmd>'`, or with a native count flag (`typeperf
  -sc`). The harness kill reaches only the wrapper." If the session dies first, the orphaned `timeout` still fires,
  so a leak is bounded to 30 minutes, not unbounded (arm C).
- **Applies:** 0.0.0_AB_MSTR (skill owner), or 1.0.0_SA_CTO if it rules the skill. **Boxes:** all, on pull.
- **Rollback:** revert.
- **Cost if wrong:** a Monitor ends 10 s before the harness would kill it. This binds by reading only. The mechanical
  form (a lint or a wrapper) is project work.

### FF4 -- one sweep per box today, after FF1-FF2 land
- **Change:** none. Each box's fabric manager runs `/kill scripts` (dry), reads the targets, then runs `/kill scripts
  go`.
- **Applies:** 0.0.0_AB_MSTR (laptop), 0.0.0_AB_MSTR~DELL1, 0.0.0_AB_MSTR~Z, and dell2's MSTR if it is live.
- **Rollback:** none is needed for a stopped process. A seat whose watcher was stopped re-runs `/watcher`.
- **Cost if wrong:** same as FF2. The dry-run read before `go` is the check.

## Held for Andrew (not fast-fix; one word each unblocks the next step)

1. **Unattended trigger.** May the reaper run `go` on a threshold with nobody reading the dry run (in `/govern`, or a
   scheduled task)? Today `/kill` is operator-initiated. Recommendation: not yet. Run FF4 by hand first, and decide
   once the first sweep's targets have been read on every box.
2. **Worktree removal.** Removing a worktree deletes data. This list does not touch worktrees.

## Not in this list, and why
- The safe-commit lock that is reclaimed from a live holder after 60 s is 4.0.0_SA_CRO~A's (GitOps) candidate.
- A hung `claude.exe` that shields its tree (CTO gap 5) needs a hang definition. That is project work.
