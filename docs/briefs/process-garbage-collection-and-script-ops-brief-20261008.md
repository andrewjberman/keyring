# L1 Brief: process garbage collection and script ops -- no process outlives its purpose

**Author:** 4.0.0_SA_CRO~B (L1), 2026-10-08 ~16:0xZ, on the CTO's L1 ask (msg 106972).
**Andrew's word:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`
(the advisory, plus the ~15:5xZ re-placement naming CRO~B) and
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_155xZ_CRO_B_SESSION_FOCUS_GC_AND_SCRIPT_OPS.md`.
**Inputs:** the dell1 draft, `git show 4d069108b5:docs/briefs/process-and-worktree-garbage-collection-brief-20261008.md`
(its measurements are cited, not re-measured); 4.0.0_SA_CRO~A's laptop measurements (msg 106970); the CTO's gap list
for `.tools/kill-maint.ps1` (msg 106966).
**Consumer:** 1.0.0_SA_CTO, `/endpoint --forward` at L2. **Mode:** NEW. This brief does not decompose, sequence or
dispatch.

Andrew's framing, kept: two approaches. **(A) fast and easy:** a threshold-based reaper that kills zombie, replaced or
session-orphaned processes. **(B) longer-term:** the high-traffic critical scripts (watcher, Monitors, agentbus,
safe-commit, safe-deploy) "obsolesce peacefully in the absence of a session that is actively using them."

---

## PART I -- THE OUTCOME TERRITORY

### Candidate thread (becomes FWD-1)

**The box operator (Andrew, or a box's fabric manager `0.0.0_AB_MSTR*`) runs one command on one box, sees every
zombie, replaced or session-orphaned process tree named with its reason, says go, and the trees are gone. A re-census
shows none left, and every live seat on the box keeps working: its mail still arrives and its next commit lands.**
Coarse grain: one box (the laptop), one planted orphan of each class, the default thresholds. Every outcome below
enriches this journey.

### O1 -- One command finds every dead tree, and only dead trees
An operator on any box runs one reaper and gets each candidate tree with its class (ZOMBIE, REPLACED, ORPHANED) and
the evidence for it. It runs dry by default. The four existing reapers collapse into it (Part IV F1).

### O2 -- The reaper knows whose process it is
For every long-running fabric process (inbox watcher, poller, broker, agentbus consumer, a seat's Monitor), the
reaper can name the owning seat or session and say whether that owner is live. A watcher whose seat is live is never
a candidate, even when its parent process is dead by design (Part IV F2).

### O3 -- A replaced copy is recognised as replaced
When a seat re-arms a watcher or Monitor and the old copy survives, the operator sees two copies of one owner's
command and the reaper stops the older one. The copy that survives is the one the seat armed last.

### O4 -- Stopping a tree stops all of it
When the reaper stops a tree, every descendant goes with it, including native Windows children such as `typeperf.exe`
(the dell1 leak class). No grandchild is left behind as a new orphan.

### O5 -- The reaper never breaks a live seat's work
A reaper run in go mode leaves every live seat's watcher, poller, Bash-tool shells, MCP servers and in-flight
`safe-commit` / `safe-merge` / `safe-deploy` untouched, and leaves no lock behind that blocks another seat (Part IV
F5). The seat notices nothing.

### O6 -- The reaper runs when the box needs it, without anyone asking
When a box crosses a threshold (Andrew's word: "thresholds based"), the reaper runs on its own. Who triggers it and
what the thresholds are is Part V; it acts, it does not notify (Part II, moratorium).

### O7 -- An operator can see afterwards what was stopped and why
For any box and any window, an operator reads which trees were stopped, the class, the owner and the evidence. The
existing audit trails are the carrier (Part IV F3); nothing pushes a notification.

### O8 -- The named high-traffic scripts end themselves when no session uses them
For each script Andrew named (inbox watcher, the Monitors seats arm, agentbus, safe-commit, safe-deploy) plus the
broker and poller that ride with them, a reader can say how it ends without its session: bounded lifetime, single
instance, owner-bound, and any native child bounded too. Each script either already does (several do: Part IV F3) or
is brought to it.

### O9 -- A seat's hand-written Monitor cannot leave a tree behind
A seat that arms an ad-hoc Monitor (not from a skill) gets the same guarantee as the watcher: when the harness kills
the Monitor at 30 minutes, or the session ends, nothing the command started keeps running. This is the dell1
`typeperf | awk` class, and today no census can see it before it piles up (Part IV F7).

### O10 -- An author writes a script that cannot leak, and is told before arming one that can
An agent writing a new long-running script or Monitor command finds one standard and one copyable pattern, and gets a
refusal or warning when the script has no exit bound. The standard needs a home (Part V).

### O11 -- Stale worktrees are collected (safety net)
An operator sees which linked worktrees are merged into CLOUD, clean and old, and they are removed within a scope
Andrew has granted. This is the dell1 draft's worktree half. Removing a worktree at drain time sits with GitOps (Part
II).

---

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** the reaper (O1-O7), the script lifecycle standard and its enforcement (O8-O10), and the
stale-worktree sweep (O11) as a safety net.

**Sibling projects, named:**
- **GitOps across the cluster (4.0.0_SA_CRO~A).** Owns git concurrency on the shared branch, lock contention and the
  worktree-per-seat policy, including removing a worktree as the drain's last step. Boundary: this project guarantees
  that stopping a process leaves no git lock behind (O5); GitOps owns how locks are contended. If GitOps makes the
  drain remove worktrees, O11 shrinks to a net.
- **Multi-device graph coherence (4.0.0_SA_CRO base).** Andrew's call A (15:4xZ, record
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/` @70950bbf31) puts a box-activity map in the cloud graph. Such a map could
  read this reaper's census; this project does not build it.
- **NFRA_CTLPLN (C-KIT, C-SEATS).** The dell1 draft names it as the likely home. Seat roles (rule 32) put a box's
  process hygiene in its fabric manager's lane; the cross-box standard is a CTO placement.
- **Skills `/kill`, `/cleanup`, `/mstr-kill`, `/watcher`, `/agentbus`.** Their engines are this project's substrate
  (Part IV). Changing them is in scope; their other uses must keep working.

**Relied on, not owned:** the Claude Code harness (its 30-minute Monitor kill and session teardown are fixed facts we
design around, not change); Windows process primitives; per-session MCP servers (server.py, playwright), which are
in scope only to confirm they die with their session.

**Constraints that bound the design (CLAUDE.md):** the alert/monitor moratorium (a reaper that acts is not an alert;
a report-only notifier would be); destructive acts need Andrew's word (stopping a leaked process deletes no data;
removing a worktree does); no device-specific logic (LD-0405); Git Bash default utilities only (rule 16); the build
ladder (four reapers exist, so consolidate before building).

---

## PART III -- THE QUALITATIVE BAR

1. After a normal working day under fabric load, every bash, python and node process on a box belongs to a tree a live
   seat would call its own. The operator never hand-kills.
2. A go-mode run stops nothing a live seat would miss: no seat misses mail, finds its commit blocked, or has a Bash
   call die.
3. The dell1 `typeperf | awk` incident cannot recur silently. Either the tree ends itself, or the next reaper run
   stops all of it.
4. An agent writing a new watcher copies a working estate pattern. They do not reconstruct the lifecycle from an
   incident history.
5. The same reaper and the same standard run on every box (laptop, dell1, dell2, site Z) with no box named in the code.
6. The reaper replaces the four that exist. The estate does not end with five.

---

## PART IV -- THE SUBSTRATE (findings, each with what was measured)

**F1. Four reapers exist, each with its own rule, and none has a threshold or a duplicate test.**
- `.tools/kill-maint.ps1` (219 lines; `/kill scripts|apps|storage`): targets bash/python only; protects any descendant
  of a process named `*claude*` (:41-53), comms command lines (:58) and Bash-tool shells (:86); applies a 60 s age
  floor; and stops each process with `Stop-Process -Id` one PID at a time (:205). The CTO's five gaps (msg 106966):
  (1) a REPLACED duplicate under a live session is protected; (2) orphaned inbox-watch/broker copies are exempt by
  command line; (3) typeperf/awk are outside the name filter, and the per-PID stop orphans native children; (4) a dead
  session's Bash-tool shells are exempt; (5) one hung `claude.exe` shields its whole tree. Laptop dry run at
  15:4xZ: 0 targets.
- `.tools/kill-orphans` (+ `.ps1` wrapper): watchers, check-inbox hangs and pollers; `--stale` uses `liveness.json`,
  `--serial` is exact-tilde; reaps are audited as KILL-ORPHAN lines. This is the only existing reaper with an owner
  key (serial + liveness).
- `.tools/kill-zombie-bash.ps1`: any bash.exe with a dead parent, optionally idle ones too. A dead parent is the wrong
  test (F2).
- `.tools/kill-agent.ps1` (`/mstr-kill`): kills a seat's claude tree by serial and sweeps that serial's orphan
  watchers.
- Unrelated despite the name: `.tools/reap_lib.py` and `.tools/commit_queue_gc.py` reap broker message rows and
  commit-queue result files, not processes. Their archive-then-delete policy, dry-run mode and no-silent-truncation
  rule are reusable shape.

**F2. A dead parent is normal for healthy fabric infra, so a parent-chain test flags every healthy watcher.** Laptop
census at 15:5xZ (this seat), matching CRO~A's 15:50Z read: every process with a dead parent is a broker, an
`agent-poller.py` or an `inbox-watch.sh ... stream`, one per live seat. The owner key has to be something else. Two
keys already exist: the serial in the command line plus `org/mcp/liveness.json` (kill-orphans; the poller's serial is
on its command line), and the MCP server PID the poller watches.

**F3. Self-ending prior art is already in the estate and audited.**
- `org/mcp/inbox-watch.sh` stream mode: exits when its parent wrapper dies (`kill -0 $PPID`, :112-158); exits itself
  at 1770 s; waits on a FIFO so its poll loop spawns no processes. It FAILS OPEN when the parent reads as PID <= 1 (a
  native parent): the parent check is skipped and only the expiry bounds it.
- `org/mcp/agent-poller.py`: exits when its MCP server PID dies (:295-301).
- `org/mcp/broker.py`: a parent watchdog every 30 s (:303-345) and a max-uptime exit (:295).
- `.tools/agentbus-sqs.sh watch`: a PID lock that refuses a second consumer and clears itself when the holder is dead
  (:486-501), a release trap, and an exit at 1700 s (dell1 draft).
- `org/mcp/orphan-audit.log`: 7,789 lines, the latest `WATCHER-SELF-EXIT ... parent gone` at 14:46Z. The self-exit
  runs and leaves evidence.

**F4. The harness Monitor kill reaches the wrapper, not its descendants.** dell1: a native `typeperf` child survived
every re-arm (63 trees, CPU ~43% -> ~17% once stopped). The inbox-watch header records the same for an MSYS child
("wrapper reaped, child survived", exercised 2026-07-10). Any command a Monitor runs must therefore bound itself and
all of its children. The harness will not do it.

**F5. safe-commit and safe-merge are short-lived. The way they fail to "obsolesce" is a lock they leave behind, not a
lingering process.**
- `safe-commit.sh`: a `commit-queue.lock` mkdir mutex (:351-387). It clears when the holder PID is dead or the lock is
  older than 60 s, and the EXIT trap releases it.
- `safe-merge.sh`: a `safe-merge.lock.d` lock (:156-180). It is cleared as stale only when the holder PID is dead AND
  no merge is open AND no conflict state exists. A conflict deliberately holds the lock.
- So a reaper that stops a `safe-merge` mid-merge leaves the merge open and the lock held, which blocks every seat.
  Git's own `index.lock` has no self-clear at all. In-flight `safe-*` is O5's must-not-touch arm.
- `safe-deploy.sh` (183 lines): the census pattern found no background launch, lock or trap. Its body was not read.

**F6. A native tree-kill exists (build ladder rung 4).** `taskkill /T /F /PID <pid>` stops a process and all of its
descendants. Windows Job Objects tie children to a parent's lifetime. Neither is used by any reaper today.
`kill-maint.ps1` stops one PID at a time (F1).

**F7. Monitor and background loops are spread across eight skill files (16 pattern matches), and ad-hoc ones have no
census at all.** A pattern census over `.claude/skills` (Monitor / run_in_background / while true / tail -f /
typeperf) matched agentbus, watcher, cloud-ops, git-pull (6), 49-schwab-conv, bbg-teams-assist, terminal-upload and
teams-assist (`teams-watch.py`). Those matches were counted, not each graded. A Monitor command a seat writes
mid-session (the dell1 case) appears in no file.

**F8. The commit-worker daemon (NFRA_CMTQUE, `.tools/commit-worker.sh`) is a designed long-lived process.** It was
not running on the laptop at 15:5xZ. Its lifecycle was not read (Part VII).

**F9. Worktree prior art: the `/cleanup` skill** already removes fully merged worktrees and husks for disk space.
dell1: 36 worktrees, 21 merged into CLOUD, 16 with a last commit older than 24 h (dell1 draft). Laptop at 15:59Z:
2 worktrees including the main tree, 1 merged.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not sequenced.

1. **An owner key for every long-running fabric process** that the reaper can read and a live seat cannot lose: the
   serial (or session id) on the command line, checked against `liveness.json` or the session file. Today the watcher
   and poller carry it; a seat's ad-hoc Monitor does not.
2. **A whole-tree stop** that reaches native Windows children (F6).
3. **A threshold design.** Andrew asked for one; this brief invents no number. Candidates: copies per owner and
   command line, processes per live seat, a box-level count. The dell1 draft notes site Z runs over twice dell1's
   seats, so a threshold may need to be per seat, not per box.
4. **Andrew's words this brief cannot supply:**
   (a) who triggers the reaper: each fabric manager's `/govern` cycle, a Windows scheduled task, or both;
   (b) whether go-mode may run unattended or stays operator-initiated (`/kill` is operator-initiated today);
   (c) a standing scope for removing worktrees (merged + clean + older than N), or it stays report-only;
   (d) where the B standard lives: a CLAUDE.md rule (locked, needs his order), a commit-time lint, the skill bodies,
       or a wrapper every Monitor runs through.
5. **Deliberately produced negative and positive arms.** The laptop is clean right now (Part VI), so no FWD can wait
   for a leak to occur. A planted orphan watcher, a planted replaced duplicate and a planted `typeperf` tree are the
   positive arms; a live seat's own tree and an in-flight `safe-merge` are the must-not-touch arms.
6. **The same code on every box**, deriving paths (LD-0405) and using only default Git Bash utilities or PowerShell
   CIM (rule 16).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Do not cut outcomes from this part; it ages.

- **Laptop, 15:5xZ-15:59Z (this seat):** rebooted 14:51Z. 364 processes: 18 bash, 12 python, 10 node, 6 powershell,
  5 claude. Each live seat's tree is ~400 MB: PowerShell host ~88 MB, `server.py` ~70 MB, two playwright-MCP node
  processes ~180 MB, poller 28 MB, watcher 10 MB, two Bash-tool shells 18 MB. No zombie, replaced or orphaned tree is
  present. Every dead-parent process is by-design infra (F2).
- **dell1, ~15:0xZ-15:2xZ (dell1 draft):** 173 -> 34 bash after cleanup; 63 typeperf/awk trees; CPU ~43% -> ~17%.
  Disk and git were ruled out as the cause there.
- **site Z, 15:1xZ (dell1 draft, its MSTR's read):** 84 bash, 46 python, 13 claude; no typeperf leak. Its
  long-lived PowerShell hosts and its seats' Monitors were not read.
- **dell2:** winding down per the dell1 draft; not read.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- The bodies of `kill-zombie-bash.ps1`, `kill-orphans` (past its header), `safe-deploy.sh`, `agentbus-consumer.py`,
  `commit-worker.sh` and the eight Monitor-arming skills were not read. F1, F5, F7 and F8 rest on headers, cited line
  ranges and a pattern census.
- The claim that GitOps contention, not process leaks, is the main cause of the slowdowns is not tested here. dell1
  ruled out git on its box; Andrew names both sources. This brief covers the process half only.
- Long-lived PowerShell hosts are not scoped in or out. On dell1 they were not a measurable load (dell1 draft Q5).
- No box but the laptop was measured live by this seat.
- 4.0.0_SA_CRO~A's partial GC draft had not arrived when this was written. If it carries a measurement this brief
  lacks, an L1 amendment follows.
- No threshold value, timing or capacity figure is asserted.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/process-garbage-collection-and-script-ops-brief-20261008.md
  PROJECT           NONE-YET (CTO to register; candidate home NFRA_CTLPLN beside C-KIT / C-SEATS)
  EXISTING PRD      NONE
  SIBLING PROJECTS  GitOps across the cluster (4.0.0_SA_CRO~A); multi-device graph coherence (4.0.0_SA_CRO);
                    NFRA_CTLPLN
  PRIOR ART         .tools/kill-maint.ps1; .tools/kill-orphans(.ps1); .tools/kill-zombie-bash.ps1; .tools/kill-agent.ps1;
                    org/mcp/inbox-watch.sh (parent tie + 1770 s expiry); org/mcp/agent-poller.py (MCP-pid tie);
                    org/mcp/broker.py (parent watchdog + max uptime); .tools/agentbus-sqs.sh (PID lock + 1700 s);
                    .tools/safe-commit.sh and .tools/safe-merge.sh (self-clearing locks); .tools/reap_lib.py (reap policy shape);
                    /cleanup (worktrees); org/mcp/orphan-audit.log and org/mcp/agent-spawn-audit.log (audit carriers)
  INPUTS            dell1 draft @4d069108b5; msg 106970 (CRO~A); msg 106966 (CTO kill-maint gaps); msg 106972 (L1 ask)
  MEASURED AT       laptop 2026-10-08 15:5xZ-15:59Z (this seat); dell1 ~15:0xZ-15:2xZ and site Z 15:1xZ (dell1 draft)
```
