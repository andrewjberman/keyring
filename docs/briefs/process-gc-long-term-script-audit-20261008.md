# Long-term GC audit: the high-traffic scripts against "time limit, single copy, dies with its session"

**Author:** 4.0.0_SA_CRO~B, 2026-10-08 ~16:4xZ, on Andrew-direct ~16:2xZ
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_162xZ_CRO_B_GC_QUICK_IMPROVE_AND_LONG_TERM_AUDIT.md`).
**Method:** four read-only audit passes run in parallel (watcher + agentbus; broker + poller + MCP server; safe-* +
commit-worker; skill Monitor census + hook feasibility), each citing file:line. This seat re-read four load-bearing
claims at the bytes: `broker.py:198-208` (the liveness probe never checks the exit code), `broker.py:886-896` (the
watchdog watches `os.getppid()`), `agentbus-consumer.py` (no parent check; 1700 s cap at :183), and
`teams-watch.py:531` (`while True`). Line estimates are estimates, not measurements.
**Companion:** the L1 brief `docs/briefs/process-garbage-collection-and-script-ops-brief-20261008.md` (O8-O10).

## 1. Scorecard

| Script | Time limit | Refuses a 2nd copy | Dies with its session | Worst consequence today |
| --- | --- | --- | --- | --- |
| inbox watcher (`org/mcp/inbox-watch.sh` stream) | YES, 1770 s (:169-195) | NO; the guard covers legacy mode only (:41-70) | YES via `kill -0 $PPID` (:137,:173); fails open at PPID<=1 | An orphan or duplicate copy steals mail (it moves the file before it announces it, :184-188) |
| watcher legacy mode (same file) | NO; it respawns itself (:272-274) | YES (:53-68) | NO | Still allow-listed in `.claude/settings.local.json` |
| agentbus wrapper (`.tools/agentbus-sqs.sh watch`) | its aws-CLI fallback loop has none (:523-623) | YES, PID lock (:486-499); check-then-write is not atomic | n/a; it execs the consumer | The fallback loop is unbounded |
| agentbus consumer (`.tools/agentbus-consumer.py`) | YES, 1700 s (:183) | via the wrapper's lock | **NO** parent check | After its session dies it holds the lock for up to ~28 min, so a re-arm is refused (rc 3) and the box receives no cross-device mail |
| broker (`org/mcp/broker.py`) | YES, 7 days (:64, :288-297) | WEAK; HTTP probe only, SO_REUSEADDR lets a 2nd bind | **NO**; it watches its launcher (dead in ms, by design), and `_pid_alive` reads an exited process as alive (:198-208) | Never ends with the last session. **Trap:** fixing the probe alone kills every broker ~30 s after start, so the two changes must land together |
| poller (`org/mcp/agent-poller.py`) | NO | only in the launch hook, via a `tasklist` substring (`hook_launch_poller.py`) | YES, watches its MCP server pid with a correct exit-code check (:131-183, :295-301); fails open on PID reuse | A re-registered seat can be left with no poller; `kill-orphans` cannot see native pollers |
| MCP server (`org/mcp/server.py`) | NO | one per session by design | relies on stdin EOF; no watchdog of its own | A leaked server keeps its poller and broker row alive |
| safe-commit | NO timeout on gates or on `git commit` | YES, lock reclaimed by liveness (0b8afb24f0) | short-lived | If killed: a leftover `.git/index.lock` blocks every seat (3 are hand-quarantined in `.git` now); staged files stay in the shared index |
| safe-merge | NO; hooks run 15-45 min | YES; a live holder is never stolen | short-lived | **If killed mid-merge, the worktree stays blocked**: dead pid + open merge is never treated as stale (:172), so every safe-commit there exits 3 until a human clears it |
| safe-deploy | YES, 10-120 s per subprocess | none (the read-back catches races) | short-lived | Leaks a temp dir per bundle deploy; nothing blocks |
| safe-apply | NO timeout on terraform; final apply not forced `-input=false` | none; the sampled backend has no state lock | short-lived | If killed: infra half-applied and plan files left on disk (these can hold secrets) |
| commit-worker (NFRA_CMTQUE) | YES, 24 h | YES, `worker.lock` | detached by design | **Dormant** (flag unset, last heartbeat 07-20). Fix its heartbeat before any cutover (4.0.0_SA_CRO~A is assessing CMTQUE) |
| `/git-pull` Monitor | was NO; **fixed today**, 1770 s deadline loop (@8773f12204, landing) | NO (instruction only) | via its bound | -- |
| `/bbg-teams-assist` Monitor (`teams-watch.py`) | was NO; **fixed today**, `timeout 1770` prefix (@8773f12204, landing) | NO | via its bound | The real fix (a parent-liveness port inside the script) is noted in the script as owned by 0.5.0_AE_OpalETL~Z |

**Census:** no skill or runbook arms `typeperf`. The dell1 leak came from a hand-written Monitor, so the warn hook
(section 2, P4) is the guard for that class. 21 seat prompts plus `/agentbus` and `/git-pull` tell seats to pass
`persistent: true, timeout_ms: 3600000`: that field does not exist and the timeout is capped at 1800000.

## 2. The work, as four independent packages

| Package | Changes | Est. lines | Risk | Proof on one box |
| --- | --- | --- | --- | --- |
| **P1 comms watchers** | consumer dies with its Monitor wrapper (OpenProcess handle on the wrapper's Windows pid; fail open if unreadable), ~28; per-serial single-instance lock in inbox-watch (pid + session id), ~20; claim -> announce -> file order, ~15; atomic agentbus lock + bound on the fallback loop, ~10; retire legacy watcher mode and its allow-list rows (net deletion) | ~75 added, ~80 removed | low-medium (two live sessions on one serial would fight) | arm, TaskStop the Monitor, consumer gone within ~20 s and lock freed; two Monitors on a test serial |
| **P2 broker / poller / server** | broker: the poller's exit-code probe + exit when no session for a grace period + exclusive bind + pid creation time, ~40, **one change**; poller: named mutex, follow the liveness pid, creation-time check, liveness-file env override, ~30; server: parent watchdog thread, ~15 | ~85 | **medium** (broker is shared by every seat on the box) | scratch port + scratch DB: register a sleeper, kill it, broker exits after grace; 2nd broker refuses to bind |
| **P3 safe-* residue** | safe-merge recovers a killed drain (dead pid + open merge + no conflict -> abort, log), ~20; safe-commit: `timeout` on gates and commit ~10, owner-checked EXIT trap 2, stale `index.lock` quarantine (old + no git process), ~25; safe-deploy temp cleanup 3; safe-apply `-lock-timeout` + backend lockfile, 1 line per tree + re-init | ~60 + per-tree | **medium-high** for the index.lock rule; low for the rest | scratch worktree, kill -9 a merge mid-hook; planted old index.lock in a scratch clone |
| **P4 Monitor hygiene** | warn-only PreToolUse hook on `Monitor` (bounded = `timeout N<=1770`, `-sc`, inbox-watch stream, agentbus watch; unbounded = `while true`, `tail -f`, bare typeperf, teams-watch); copy the advisory path of `comp-tool-hud.sh`; never deny; plus correcting the `persistent`/3600000 text in 21 prompts and 2 skills | ~50 + text | low; regex over free text gives some false warnings | FIRST a 5-minute proof that a `Monitor` matcher fires at all (not yet measured) |

**Total:** roughly 270 lines added and 80 removed across about 12 files. Each package is a few hours of one seat's
work including its exercise, and the four share no files. P2's broker change is the only one that can take a whole
box's messaging down if wrong.

## 3. Andrew's remaining long-term items

- **"The killer runs on its own when a box needs it":** the record half is DONE today (`KILL-MAINT` lines in
  `org/mcp/agent-spawn-audit.log`, @b8c8b38c33). The trigger half needs Andrew's word on unattended `go`.
  Recommendation: read the first supervised sweep's targets on every box first.
- **"Merged, idle worktrees are removed within limits you set":** `/cleanup` already does the removal. It needs
  Andrew's limits (merged into CLOUD, clean, older than N hours, never `drain-*`).

## 4. Found off-task (not GC)

- `org/mcp/check-inbox.sh` reads a lane inbox at `<base>~<lane>` (:49) while `inbox-watch.sh` watches
  `<base>/~<lane>` (:98). The flat form is the LD-0202 dead path. Confirmed at the bytes by this seat (:45-51): a
  `~lane` seat running `check-inbox.sh` reads the flat dead directory plus the base inbox, never its own nested
  lane inbox. Not exercised by a run.
- `.tools/hooks/README.md` says `block-bare-inbox-watch.sh` is wired; `.claude/settings.json` does not wire it.
