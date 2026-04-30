# inbox-watch.sh — Design Brief

**Date:** 2026-04-30  
**Author:** 0.4.0_DS_ClientPlatform_A  
**Commits:** 944618d86 (orphan fix), fdd6361d9 (auto-respawn)

---

## Background: Why exit-on-message?

Claude Code fires an agent interrupt through exactly one mechanism: a background
task completing (exiting). There is no push-notification API, no file-watcher
hook, no stdout-line interrupt. The entire inbox notification system is built on
this constraint:

1. Agent launches `inbox-watch.sh` with `run_in_background=true` → Claude Code
   assigns the process a task ID and monitors it.
2. Script polls `org/mcp/inbox/<agent>/` every 5 seconds.
3. When a `.md` file appears, the script prints it and **exits**.
4. Claude Code sees the task exit → fires the completion notification → agent
   context is interrupted and the output is surfaced.

Exit-on-message is therefore load-bearing. Converting the script to a long-running
loop that never exits would eliminate all interrupts.

---

## What changed in today's commits

### Commit 944618d86 — orphan guard fix

**Bug:** When an agent launches `inbox-watch.sh` via `run_in_background=true`,
the bash process is detached from the Claude Code session and re-parented to
PID 1 by the OS. The single-watcher guard interpreted `ppid == 1` as a sign the
process was orphaned and killed it, leaving no watcher running.

**Fix:** Removed the `ppid -eq 1` condition. The guard now uses only
`! kill -0 $pid` (process liveness) to decide if an existing watcher should be
reaped. A detached-but-live process is not an orphan.

```bash
# Before
if [ -z "$ppid" ] || [ "$ppid" -eq 1 ] || ! kill -0 "$ppid" 2>/dev/null; then

# After
if [ -z "$ppid" ] || ! kill -0 "$pid" 2>/dev/null; then
```

### Commit fdd6361d9 — auto-respawn on delivery

**Problem:** After the tracked instance exits (firing the interrupt), the inbox
was unwatched until the agent manually re-launched the script. Any message
delivered during that window was not missed (it stayed in the inbox directory)
but the agent would not be interrupted to process it.

**Change:** Immediately before `exit 0`, the script spawns a new untracked copy
of itself with a 1-second delay:

```bash
SAFE_SERIAL=$(printf '%s' "$SERIAL" | tr '/~' '__')
( sleep 1; exec bash "$0" "$SERIAL" >> "/tmp/inbox-watch-${SAFE_SERIAL}.log" 2>&1 ) &
disown $! 2>/dev/null || true
exit 0
```

The 1-second delay is required because the single-watcher guard must see the
original instance as gone before the new copy starts. Without it, the new copy
finds the original PID still alive and exits immediately.

The respawned copy is redirected to `/tmp/inbox-watch-<serial>.log` rather than
stdout so it does not interfere with any future tracked instances.

---

## Current state: what works and what does not

| Scenario | Behavior |
|----------|----------|
| First message after a `run_in_background` launch | Agent interrupted ✓ |
| Inbox always has an active watcher | Yes (auto-respawn) ✓ |
| Messages lost during handoff gap | No (1-second gap at most) ✓ |
| Second+ messages while running on untracked copy | Delivered to log, **no interrupt** ✗ |
| Agent re-registers tracked instance | Kills untracked copy, full interrupt coverage restored ✓ |

The core limitation: Claude Code has no API for a script to self-register as
a tracked background task. Only processes launched by the agent via
`run_in_background=true` are tracked. Every auto-respawned copy is invisible to
the task system.

---

## What full interrupt coverage requires

Full coverage — every message triggers an agent interrupt regardless of how long
ago the agent last re-registered — requires one of the following:

### Option 1: Re-registration protocol (no code changes needed)

The simplest operational fix. Agent startup protocol already requires launching
inbox-watch; extend it to also re-register after processing each notification.
This is already partially in place (CLAUDE.md feedback: "relaunch IMMEDIATELY on
every task-notification exit"). The auto-respawn change makes this less critical
(messages are never lost) but full interrupt coverage still requires the agent to
re-register.

**Cost:** Agent discipline only. No code.  
**Gap:** Agents that go many hours without re-registering accumulate untracked
messages in the log file silently.

---

### Option 2: Periodic re-registration via CronCreate

An agent-level cron (using Claude Code's `CronCreate` tool) fires every N minutes
and re-launches inbox-watch with `run_in_background=true`. This replaces the
untracked copy with a tracked one on a cadence.

```
CronCreate(interval=900, command="bash org/mcp/inbox-watch.sh <serial>", run_in_background=true)
```

**Cost:** Per-agent setup. Does not require changes to inbox-watch.sh.  
**Gap:** Up to N minutes between re-registrations during which new messages do
not interrupt. N=15 is a reasonable default.

---

### Option 3: Sentinel file + Claude Code hook (requires platform feature)

If Claude Code supported a `PostFileWrite` hook (triggered when a file appears
in a watched directory), inbox-watch.sh could be retired entirely:

```
hook: on file create in org/mcp/inbox/<agent>/  →  bash org/mcp/inbox-watch.sh <agent>
```

The hook would launch a fresh tracked instance on every delivery, guaranteeing
an interrupt with no polling gap. This is the architecturally correct solution.

**Cost:** Requires Claude Code to add a filesystem-event hook type. Not currently
available (hooks only fire on tool use events).  
**Gap:** Platform dependency.

---

### Option 4: Long-running watcher with Monitor tool

Redesign inbox-watch.sh to never exit — it runs forever and prints a structured
marker when messages arrive. The agent calls `Monitor(pid)` to stream its output.
Each stdout line from Monitor produces a notification.

The problem: `Monitor` is a blocking tool call. The agent must be explicitly
waiting on it; it does not interrupt an agent that is doing other work. This
makes it unsuitable as a background interrupt mechanism without additional
scaffolding.

**Cost:** Significant redesign. Does not solve the background interrupt problem
with current Claude Code tooling.

---

## Recommendation

**Short term:** Option 1 + Option 2 in combination. The auto-respawn change
(already shipped) ensures no messages are ever lost. Option 2 (periodic cron
re-registration) caps the interrupt-coverage gap at a known bound without
requiring any changes to the script or agent startup protocol.

**Long term:** File Option 3 as a Claude Code feature request. It is the only
solution that makes inbox notification deterministic without polling or manual
re-registration.

---

## File locations

| File | Role |
|------|------|
| `org/mcp/inbox-watch.sh` | The watcher script |
| `org/mcp/inbox/<agent>/*.md` | Unread messages (watched) |
| `org/mcp/inbox/<agent>/read/*.md` | Delivered messages (archived) |
| `/tmp/inbox-watch-<serial>.log` | Output from auto-respawned (untracked) copies |
| `org/mcp/INBOX_WATCH_ORPHAN_BUG.md` | Prior incident write-up |
