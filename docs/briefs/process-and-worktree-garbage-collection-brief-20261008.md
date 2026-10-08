# Brief (draft): process and worktree garbage collection across the fabric

**Drafted by:** 0.0.0_AB_MSTR~DELL1, on Andrew's word at the dell1 terminal, 2026-10-08 ~15:3xZ.
**For:** laptop 4.0.0_SA_CRO (L1 owner: this draft is input to the brief, not the brief of record) and laptop
1.0.0_SA_CTO (placement, L2 endpoint). Likely home: NFRA_CTLPLN, beside C-KIT and C-SEATS.
**Status:** DRAFT. It records the word, the measurements and the two approaches. It decides nothing.

## 1. Andrew's words, verbatim

Asked what was making every box sluggish (the laptop rebooted, site Z likely next, dell2 winding down):

> "I think the slowdowns come from 1 or multiple of these items: 1.) Storage overload from constant worktrees, weighing on
> write ability. 2.) Anthropic server-side capacity issues. 3.) git commit/merge/etc concurrency overload."

> "another issue is that it could be around powershell sessions that have been running for long periods ... it could be bash
> process storm too, yes."

On the finding:

> "so in essence what we need is a garbage collector, youve ruled out git? i have ruled out anthropic."

And the ask for this brief:

> "Yeah i need you to draft a brief on this matter. I think theres two ways to approach it, the simple fast way is that we have
> some kind of automated/threshold-based garbage collector. The better long-term way is to not design python/bash scripts that
> obsolesce without self-terminating."

## 2. What was measured (dell1, 2026-10-08 ~15:0xZ-15:2xZ)

| Read | Value | Instrument |
| --- | --- | --- |
| bash.exe processes | 173 before, 34 after cleanup | Win32_Process census |
| typeperf.exe / awk.exe | 63 / 63 before, 1 / 1 after | Win32_Process census |
| Total CPU (16 cores) | ~43% before, ~17% after, 11% at 15:21Z | `\Processor(_Total)\% Processor Time` |
| Disk | queue ~0.01, 13% of 1.9 TB used | PhysicalDisk counters, `df` |
| Free RAM | 41.6 of 63.7 GB | Win32_OperatingSystem |
| git | 1 git.exe live, no stale `.lock`; a 392-commit merge graded in 155 s | process census, `.git` lock census, timed `safe-merge.sh` |
| Linked worktrees | 36, each ~2.8 GB / 63,700 files; 21 have their HEAD already merged into CLOUD; 16 have a last commit older than 24 h | `git worktree list --porcelain`, `merge-base --is-ancestor`, `du` |
| Anthropic-side errors | ruled out by Andrew; no API-error records found in dell1's session logs (that log only sees this session) | transcript read |
| Long-lived powershell.exe | 8, oldest 10-06 20:43, ~76-105 MB each | Win32_Process census |

**The cause on dell1 was a process leak, and the leak was the fabric manager's own.** A Defender-CPU watch ran as a Monitor
(`typeperf ... -si 30 | awk ...`). The harness kills a Monitor at 30 minutes, but that kill does not reach a native Windows
child such as `typeperf.exe`, so every re-arm left a full tree behind: 63 trees from 10-07 03:37 to 10-08 10:49. Stopping
them cut CPU from ~43% to ~17%. The script now bounds itself (`typeperf -sc 58`, 29 minutes), so a re-arm can never stack.

**Site Z (its fabric manager's read, 15:1xZ):** no such leak (0 typeperf, 0 awk; one bus-consumer tree; one inbox-watch tree per
seat). It runs 84 bash, 46 python and 13 claude processes with 20.0 of 63.5 GB free. Andrew notes site Z runs more than twice
dell1's seats, which accounts for the python count. Its long-lived powershell sessions and its seats' own Monitors were not read.

**The counter-examples already in the estate** are the two watchers that never leaked: `org/mcp/inbox-watch.sh` exits itself at
1770 s and prints its own re-arm line, and `.tools/agentbus-sqs.sh watch` exits at 1700 s and takes a PID lock that refuses a
second consumer. Both self-terminate before the harness kill and both refuse to stack. That is the long-term pattern Andrew
names, already working in two places.

## 3. The two approaches (Andrew's framing)

### A. Simple and fast: an automated, threshold-based garbage collector

A per-box reaper, run on a schedule or by each box's fabric manager in its `/govern` cycle, that finds and stops orphaned
process trees and prunes dead worktrees.

- **Processes.** Candidates: a process whose owning Claude session no longer exists (its parent chain reaches no live
  claude.exe); or a second or later copy of the same long-running command, keeping only the newest. A threshold (for example,
  more than N copies of one command line, or bash.exe above a box-specific count) decides when it acts or reports.
- **Worktrees.** Candidates: a linked worktree whose HEAD is an ancestor of CLOUD, whose `git status --porcelain` is empty, and
  whose last commit is older than a set age. On dell1 today, 21 of 36 pass the first test.
- **Cost.** Little code. It treats the symptom, so a new leaking script is found only after it has piled up.

### B. Better, long-term: scripts that cannot outlive their purpose

A design rule, enforced where possible, that every long-running script ends itself.

- **Bounded lifetime.** A watcher exits before the harness kill (as inbox-watch and agentbus watch do), and any native child it
  starts is bounded too (`-sc`, `-n`, `timeout`).
- **Single instance.** A PID lock that refuses a second copy, as agentbus watch already does.
- **Owner-bound.** A child exits when its parent session is gone, rather than being re-parented and forgotten.
- **Worktrees** are removed by the drain that merges them, as the last step of the merge, not left for later.
- **Cost.** More design work, and it binds every author. It removes the cause, so A shrinks to a safety net.

The two are not exclusive. One plausible order, for the CTO to rule on: A first as the net, B as the standard.

## 4. Constraints the design must meet

- **Alert/monitor moratorium (CLAUDE.md section 5).** A reaper that acts is not an alert, but one that only notifies would be.
  Whether a report-only mode is allowed is Andrew's call.
- **Destructive acts need a human word (CLAUDE.md Agent Autonomy).** Removing a worktree or a branch deletes data. Approach A's
  worktree half needs Andrew's standing permission, scoped (for example: merged, clean, older than N hours), or it stays
  report-only. Stopping a leaked process deletes no data.
- **Seat roles (rule 32).** Process hygiene on a box is its fabric manager's lane. A cross-box standard is a project for the
  laptop CTO.
- **No device-specific logic (LD-0405)** and **Git Bash default utilities only (rule 16)**: the reaper must derive paths, and
  must work without pgrep/pkill. PowerShell `Get-CimInstance Win32_Process` gives ParentProcessId and CreationDate.
- **Never kill a seat's live work.** The negative control is a live seat's own Monitor tree and its Bash tool shells.

## 5. Open questions for L1/L2

1. Who runs A: each fabric manager in `/govern`, a Windows scheduled task, or both?
2. What thresholds, and are they per box (site Z runs more than twice dell1's seats)?
3. Does the worktree half act, or only report, until Andrew gives a standing scope?
4. Where does B's rule live: CLAUDE.md, a lint at commit time (for example, flag a long-running loop with no exit bound in a
   script under a Monitor), or the skill bodies that arm Monitors?
5. Should long-lived powershell.exe sessions be in scope? On dell1 they were not a measurable load.
