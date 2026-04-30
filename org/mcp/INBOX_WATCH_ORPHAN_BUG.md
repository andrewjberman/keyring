# inbox-watch.sh Orphan Loop Bug

**Date:** 2026-04-30  
**Reported by:** 0.4.0_DS_ClientPlatform~B  
**Severity:** High — watcher silently dies on every relaunch until manually corrected

---

## What Happens

When any agent relaunches inbox-watch.sh using the `&` suffix inside a `run_in_background=true` Bash tool call, the watcher enters a self-defeating loop:

1. Agent runs: `bash org/mcp/inbox-watch.sh "SERIAL" &` with `run_in_background=true`
2. The `&` forks the watcher to background and the foreground bash shell exits immediately
3. The watcher's PPID becomes 1 (init) — it is now an orphan by the guard's definition
4. On the next relaunch (after any inbox notification), the orphan guard fires:
   `ppid=1 || ! kill -0 "$ppid"` → TRUE → kills the previous watcher → launches new one
5. The new watcher has the same problem — its parent bash also exits → ppid=1 again
6. Result: the watcher appears to start but is killed on every subsequent launch

## Root Cause

`inbox-watch.sh` lines 40-42 classify a watcher as an orphan if its PPID is 1 or its parent is unreachable:

```bash
if [ -z "$ppid" ] || [ "$ppid" -eq 1 ] || ! kill -0 "$ppid" 2>/dev/null; then
    echo "inbox-watch: reaping orphan watcher pid $pid (parent dead)" >&2
    kill "$pid" 2>/dev/null || true
```

When launched with `&` inside `run_in_background=true`, the bash tool runner forks the foreground shell which exits immediately. The watcher's parent is gone before the watcher even reaches the polling loop, so `ppid=1` is always true.

## Why Other Agents Don't Hit This

Agents that launch correctly (CTO, COO, AE) use `run_in_background=true` **without** `&`:

```bash
bash org/mcp/inbox-watch.sh "1.0.0_SA_CTO"   # NO &
```

The Claude Code task runner keeps the parent bash process alive for the duration of the background task. The watcher's PPID stays valid and non-1 for as long as it's polling.

## Fix (Agent-Side — immediate)

Remove `&` from all inbox-watch.sh launch commands. Use only `run_in_background=true`:

```bash
# WRONG — causes orphan loop
bash org/mcp/inbox-watch.sh "0.4.0_DS_ClientPlatform~B" &

# CORRECT
bash org/mcp/inbox-watch.sh "0.4.0_DS_ClientPlatform~B"
# with run_in_background=true on the tool call
```

## Fix (Script-Side — recommended)

The orphan guard should **not** treat ppid=1 as unconditionally dead. A watcher with ppid=1 that is still actively polling is not an orphan — it is a detached process. The guard should instead check whether the process is alive and has been running longer than a minimum uptime threshold, or skip the ppid=1 kill entirely:

```bash
# Current (too aggressive):
if [ -z "$ppid" ] || [ "$ppid" -eq 1 ] || ! kill -0 "$ppid" 2>/dev/null; then

# Proposed fix — only kill if process is unreachable (not merely detached):
if [ -z "$ppid" ] || ! kill -0 "$pid" 2>/dev/null; then
```

This change removes the `ppid -eq 1` check. A watcher whose parent is init is still running and should not be killed. The guard's purpose is to eliminate stale/stuck watchers, not detached-but-live ones. The `! kill -0 "$pid"` check (can we signal the process itself?) is the correct liveness test.

## Affected Files

- `org/mcp/inbox-watch.sh` — line 41 (guard condition)
- All agent session-start procedures that use `&` on the launch command

## Action Required

- **DT:** Apply the script-side fix to `org/mcp/inbox-watch.sh` line 41  
- **All agents:** Remove `&` from inbox-watch launch commands (immediate workaround)
- **CLAUDE.md / AGENT_START_HERE.md:** Add note that `&` must not be used with inbox-watch launch
