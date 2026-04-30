# inbox-watch.sh / cl-inbox-watch.sh — Design Brief

**Date:** 2026-04-30  
**Scope:** Opal (`org/mcp/inbox-watch.sh`) and COMP_LEARNS (`org/mcp/cl-inbox-watch.sh`)

---

## Background: Why exit-on-message?

Claude Code fires an agent interrupt through exactly one mechanism: a background
task completing (exiting). There is no push-notification API, no file-watcher
hook, no stdout-line interrupt. The entire inbox notification system is built on
this constraint:

1. Agent launches inbox-watch with `run_in_background=true` via the Bash tool.
   Claude Code assigns the process a task ID and monitors it.
2. Script polls the agent's inbox directory every 5 seconds.
3. When a `.md` file appears, the script prints it and **exits**.
4. Claude Code sees the task exit → fires the completion notification → agent
   context is interrupted and the output is surfaced.

Exit-on-message is therefore load-bearing. Converting the script to a long-running
loop that never exits eliminates all interrupts.

---

## Architecture: Two channels, one design

The workspace runs two parallel inbox-watch scripts serving separate agent groups:

| Script | MCP channel | Inbox dir | Agent group |
|--------|-------------|-----------|-------------|
| `org/mcp/inbox-watch.sh` | `opal-agent-comms` | `org/mcp/inbox/` | Opal agents (`ajb_workspace`) |
| `org/mcp/cl-inbox-watch.sh` | `complearns-agent-comms` | `org/mcp/cl_inbox/` | COMP_LEARNS agents (`feature_clb`) |

Both share the same exit-on-message design, serial-based isolation, and
single-watcher guard. They diverge only in inbox channel directory and
respawn policy (see below).

---

## Fixes shipped 2026-04-30

### Fix 1 — ppid==1 orphan guard removal

**Bug:** When an agent launches inbox-watch via `run_in_background=true`, the
bash process is detached from the Claude Code session and re-parented to PID 1
by the OS. The single-watcher guard interpreted `ppid==1` as a sign the process
was orphaned and killed it, leaving no watcher running.

**Root cause:** The guard used parent PID (`$ppid`) for the liveness test. A
detached-but-live process has ppid==1, so the guard fired incorrectly.

**Fix:** Remove the `ppid==1` condition. Use process liveness (`! kill -0 "$pid"`)
against the watcher's own PID, not its parent:

```bash
# Before (cl-inbox-watch.sh; inbox-watch.sh was already fixed in 944618d86)
if [ -z "$ppid" ] || [ "$ppid" -eq 1 ] || ! kill -0 "$ppid" 2>/dev/null;

# After (both scripts)
if [ -z "$ppid" ] || ! kill -0 "$pid" 2>/dev/null;
```

**Shipped:** `944618d86` (inbox-watch.sh, 2026-04-30); applied to cl-inbox-watch.sh
in this session.

### Fix 2 — eval-wrapper false-positive in ps-ef fallback

**Bug:** On Windows Git Bash, `pgrep` is absent (removed in Git Bash 3.6.7,
2026-03-29). The fallback path uses `ps -ef | awk` to find existing watcher
processes. Claude Code wraps every `run_in_background` command as:

```
/usr/bin/bash -c -l eval bash org/mcp/inbox-watch.sh <serial>
```

This eval-wrapper process appears in `ps -ef` output and matches both the
`inbox-watch[.]sh` pattern and the `$NF == ser` (last field = serial) check.
The guard treats it as a live duplicate watcher and exits immediately — before
the actual watcher ever starts.

**Fix:** Pipe through `grep -v eval` before the awk filter:

```bash
# Before
existing=$(ps -ef | awk -v ser="$SERIAL" -v me="$$" '$2 != me && $NF == ser && $0 ~ "inbox-watch[.]sh" {print $2}')

# After
existing=$(ps -ef | grep -v eval | awk -v ser="$SERIAL" -v me="$$" '$2 != me && $NF == ser && $0 ~ "inbox-watch[.]sh" {print $2}')
```

**Shipped:** COMP branch commits `c471b2fd9` + `d26a36492` (2.1.0_SC_CompLearns);
ported to CLOUD inbox-watch.sh and cl-inbox-watch.sh in this session.

**Note on scope:** This bug affects Windows Git Bash (`pgrep` absent → ps-ef path
taken). On Linux/Mac where `pgrep` is present, the primary path is used and the
eval-wrapper does not interfere. The fix is safe on all platforms — `grep -v eval`
is a no-op filter on systems where the eval wrapper doesn't appear.

### Fix 3 — auto-respawn on delivery (inbox-watch.sh only, fdd6361d9)

**Problem (Opal only):** After the tracked instance exits (firing the interrupt),
the inbox was unwatched until the agent manually re-launched. Any message during
that window was not missed (it remained in the inbox directory) but the agent
would not be interrupted.

**Change:** Before `exit 0`, the script spawns a new untracked copy with a 1-second
delay (required so the guard sees the original as gone before the new copy starts):

```bash
SAFE_SERIAL=$(printf '%s' "$SERIAL" | tr '/~' '__')
( sleep 1; exec bash "$0" "$SERIAL" >> "/tmp/inbox-watch-${SAFE_SERIAL}.log" 2>&1 ) &
disown $! 2>/dev/null || true
exit 0
```

The respawned copy writes to `/tmp/inbox-watch-<serial>.log` rather than stdout
so it does not interfere with future tracked instances.

---

## Respawn policy divergence (intentional)

| Script | Policy | Rationale |
|--------|--------|-----------|
| `inbox-watch.sh` (Opal) | **Auto-respawn** — untracked child spawned before exit | Continuous coverage. Messages never lost during handoff gap. Untracked copies do not interrupt, but messages accumulate in the log for the agent to process on next relaunch. |
| `cl-inbox-watch.sh` (COMP_LEARNS) | **No auto-respawn** — agents MUST relaunch | Deliberate design: orphan stdout disconnects from the Claude Code task tracker. COMP_LEARNS agents run in controlled sessions where every delivery must trigger an interrupt. Unattended gap coverage is secondary. |

**The auto-respawn limitation:** Untracked copies don't fire Claude Code interrupts.
Second+ messages delivered while an untracked copy runs appear in the log file but
produce no interrupt. Agent re-registration via `run_in_background=true` restores
full interrupt coverage.

---

## Full interrupt coverage options

### Option 1: Re-registration after every notification (no code changes)

Agent startup protocol already requires launching inbox-watch; extend it to also
relaunch immediately after processing each notification. This closes the
untracked-copy gap and is already partially mandated (see org/XXX.md Step 1b section C).

**Cost:** Agent discipline only.  
**Gap:** Agents running many hours without re-registering accumulate untracked messages silently.

---

### Option 2: Periodic re-registration via CronCreate (recommended for autonomous loop agents)

An agent-level cron (using Claude Code's `CronCreate` tool) fires every 15 minutes
and re-launches inbox-watch via `run_in_background=true`. This replaces the
untracked copy with a tracked instance on a cadence, capping the interrupt-coverage
gap at a known bound.

```python
# At session startup, AFTER the initial run_in_background inbox-watch launch
CronCreate(
    interval=900,  # 15 minutes
    prompt="Relaunch inbox-watch for interrupt coverage: use the Bash tool with run_in_background=true to run: bash org/mcp/inbox-watch.sh {your_serial}"
)
```

**Cost:** One CronCreate call per session. No code changes.  
**Gap:** Up to 15 minutes between tracked instances. Acceptable for /loop agents.  
**When to use:** Any agent running in autonomous `/loop` mode for extended periods.

---

### Option 3: Sentinel file + Claude Code hook (requires platform feature)

If Claude Code supported a `PostFileWrite` hook triggered when a file appears in a
watched directory, inbox-watch.sh could be retired entirely:

```
hook: on file create in org/mcp/inbox/<agent>/  →  bash org/mcp/inbox-watch.sh <agent>
```

Every delivery would launch a fresh tracked instance, guaranteeing an interrupt
with no polling gap.

**Cost:** Requires Claude Code to add filesystem-event hooks. Not currently available
(hooks fire on tool use events only).  
**Gap:** Platform dependency.

---

### Option 4: Long-running watcher with Monitor tool

Redesign inbox-watch.sh to never exit — runs forever, prints a structured marker when
messages arrive. The agent calls `Monitor(pid)` to stream output.

**Problem:** `Monitor` is blocking. The agent must be explicitly waiting on it; it
does not interrupt an agent doing other work. Unsuitable as a background interrupt
mechanism.

**Cost:** Significant redesign. Does not solve the problem with current Claude Code tooling.

---

## Recommendation

**Short term:** Option 1 + Option 2 in combination.
- All agents: relaunch inbox-watch immediately after every notification (Option 1 — already mandated).
- Autonomous `/loop` agents: additionally call `CronCreate(interval=900, ...)` at session startup
  (Option 2) as a backstop. Even if the agent forgets to relaunch after a notification, the cron
  re-registers a tracked instance within 15 minutes.

**Long term:** File Option 3 as a Claude Code feature request. It is the only solution that makes
inbox notification fully deterministic without polling or manual re-registration.

---

## Current state after 2026-04-30 fixes

| Scenario | inbox-watch.sh (Opal) | cl-inbox-watch.sh (COMP_LEARNS) |
|----------|-----------------------|---------------------------------|
| First message after tracked launch | Interrupt fires ✓ | Interrupt fires ✓ |
| ppid==1 false-positive kills live watcher | Fixed ✓ | Fixed ✓ |
| Eval-wrapper false-positive (Windows) | Fixed ✓ | N/A — pgrep path used on Linux |
| Inbox always has an active watcher | Yes (auto-respawn) ✓ | No — agent must relaunch (by design) |
| Messages lost during handoff | No (1-second gap max) ✓ | No gap (no handoff) ✓ |
| Second+ messages on untracked copy | Log only, no interrupt ✗ | N/A |
| Agent re-registers tracked instance | Full interrupt coverage restored ✓ | Full interrupt coverage ✓ |

---

## File locations

| File | Role |
|------|------|
| `org/mcp/inbox-watch.sh` | Opal channel watcher |
| `org/mcp/cl-inbox-watch.sh` | COMP_LEARNS channel watcher |
| `org/mcp/inbox/<agent>/*.md` | Opal unread messages |
| `org/mcp/cl_inbox/<agent>/*.md` | COMP_LEARNS unread messages |
| `org/mcp/inbox/<agent>/read/*.md` | Opal delivered (archived) |
| `org/mcp/cl_inbox/<agent>/read/*.md` | COMP_LEARNS delivered (archived) |
| `/tmp/inbox-watch-<serial>.log` | Opal auto-respawn output (untracked copies) |
| `org/mcp/INBOX_WATCH_ORPHAN_BUG.md` | Prior orphan incident write-up |
