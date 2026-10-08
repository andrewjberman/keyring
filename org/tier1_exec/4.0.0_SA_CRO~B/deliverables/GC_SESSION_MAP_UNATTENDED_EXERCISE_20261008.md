# GC: the session map and the unattended reaper -- build and exercise record (laptop, 2026-10-08 16:4xZ-17:3xZ)

**Author:** 4.0.0_SA_CRO~B, leading on Andrew-direct ~16:4xZ
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_164xZ_REAPER_UNATTENDED_OK_IF_SESSION_SHELLS_ASSIGNED.md`).
Andrew's condition: unattended runs are fine "as long as there is a clear mechanism of assigning PIDs to Claude Code
and Codex session shells. Those should never be killed".
**Files:** `.tools/kill-maint.ps1` (session map, MSYS link, unattended mode); `.tools/kill-maint-task.ps1` (new: the
box's scheduled task: install, uninstall, status). **Rollback:** revert the commit, then run
`.tools\kill-maint-task.ps1 -Uninstall` on any box where the task was installed.

## 1. The mechanism: how a PID is assigned to a session

1. **Agent roots:** every `claude.exe` and every `codex.exe`.
2. **Session shell:** the outermost shell process (powershell / pwsh / cmd / bash) above a root, stopping at the
   terminal. Measured shape on the laptop: `WindowsTerminal -> powershell.exe (session shell) -> claude.exe | codex.exe
   (Codex: app-server + TUI under one shell)`.
3. **Session PIDs:** the session shell's entire Windows process subtree.
4. **MSYS link:** Git Bash fork/exec leaves a Windows parent that has already exited, so a seat's Bash-tool jobs and
   Monitor commands read as parentless in `Win32_Process`. MSYS's own table (`ps -al`: PID, PPID, WINPID) keeps the real
   chain, so every MSYS descendant of an in-session WINPID joins that session, with its Windows subtree. When the
   session ends its shells die, the chain breaks (PPID 1), and the leftover work becomes reapable.
5. **Serial:** a seat's `liveness.json` pid (`server.py` for Claude, `codex-agent-heartbeat.py` for Codex) lies inside
   its session, which names the seat.
6. **Printed on every run** as `--- session shells ---`, one row per session: kind, shell PID, roots, PID count,
   serial. No PID in that map is ever a target, in any mode. Name-matched `claude*` / `codex*` trees are protected as
   well, and `codex` joins `claude` on the hard-deny name list.

Live map at 17:2xZ: 8 sessions (7 Claude Code, 1 Codex), every one bound to its serial (0.0.0_AB_MSTR, 1.0.0_SA_CTO,
4.0.0_SA_CRO, ~A, ~B, 2.0.0_SA_COO~C, ~G, and Codex 0.7.0_AE_CloudOps), 0 targets. 2.0.0_SA_COO~G, launched
mid-exercise, was mapped on the next run with no change.

## 2. Unattended mode (`-Unattended`)

Scripts mode only (apps mode is never unattended) + Execute, with two guards that stop nothing and write
`KILL-MAINT-ABORT`:

- agent processes are running but the session map is empty;
- Git Bash processes are running but no MSYS table could be read;
- more than `-MaxTargets` (default 25) trees qualify, since a classifier fault looks like a flood.

Every run writes one `KILL-MAINT-RUN` line (sessions, session PIDs, targets, killed, failed, MSYS rows/joined, ms) to
`org/mcp/agent-spawn-audit.log`, plus one `KILL-MAINT` line per stopped tree. A process whose command line cannot be
read is never a target.

## 3. Exercises

| # | Exercise | Result |
| --- | --- | --- |
| 1 | Live dry run, real cap 1860 s | 8 sessions mapped and bound, 0 targets |
| 2 | Background Bash job (`sleep 240`) and a Monitor (`timeout 1770 bash -c 'sleep 240'`) in this session | before the MSYS link: both `sleep`s and the `timeout` read OUTSIDE the session; after: all three inside |
| 3 | In-flight `git commit` with a 45 s pre-commit hook, run in this session | git.exe, `sh .git/hooks/pre-commit` and its `sleep` all inside the session |
| 4 | Flood guard: planted orphan tree, `-Unattended -MaxTargets 0` | `ABORT: 4 targets exceed -MaxTargets 0 -- nothing stopped`; KILL-MAINT-ABORT logged; plant still alive |
| 5 | Unattended run on the plant (cap lowered to 5 s for the test) | plant tree stopped, 0 typeperf/awk left, KILL-MAINT + KILL-MAINT-RUN logged; this seat's watcher alive |
| 6 | Scheduled task, installed from this worktree and fired by hand | first run ~151 s, because console writes stall under a headless console with no reader (phase probe: CIM 0.45 s, `ps -al` 0.75 s, liveness 0.09 s). After redirecting output to `%TEMP%\opal-kill-maint-last-run.log`: 8 s wall, 4.4 s internal, result 0x0, KILL-MAINT-RUN written. The task was then uninstalled |
| 7 | Installer refusal | S4U registration is refused without admin ("Access is denied"), AND the first installer printed OK after that failure. Fixed: Interactive logon, `-ErrorAction Stop`, and a read-back that throws if the task is absent |

## 4. Incident during exercise 5 (owned here)

With the Monitor cap lowered to 5 s, the unattended run also stopped a 8-second-old `bash .git\hooks/pre-commit`
belonging to another seat's in-flight commit (16:55:07Z). The 1.0.0_SA_CTO commit at 16:55:00Z landed, and no
`.git/index.lock` was left, so no seat was blocked. The process was gone before its owner could be read.
Exercise 3 shows a hook run from a session maps correctly, so this one was launched outside any session map.
Remedy in this commit: a running git hook (`hooks/pre-*|post-*|prepare-*|commit-*`) is now an in-flight never-target,
like safe-commit. At the real 1860 s cap an 8-second process is never a candidate, but safe-merge hooks run 15-45
minutes, so the never-target rule is what protects them.

## 5. Not done here

- The scheduled task is NOT installed on any box. That waits for the landing and for Andrew's calls on cadence and
  rollout.
- dell1, dell2 and site Z were not exercised.
- CTO gap 5 (a hung `claude.exe`) is moot: session shells are never targets.
