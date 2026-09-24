---
name: watcher
description: Ensure this seat is reachable -- registered LIVE on the broker with exactly one persistent inbox Monitor for this session. Run at session start, after a restart or compaction, or when reachability is in doubt. The 30-minute re-arm is NOT this skill -- it is the one Monitor call the [WATCHER-EXPIRED] line prints. Self-scoped.
---

# /watcher -- inbox reachability

The inbox watcher is a Monitor running `inbox-watch.sh <serial> stream`: one `[INBOX] <file>` event per message
(the file is already in your `read/` dir). The harness kills every Monitor at 30 minutes, so the script exits itself
at 1770 s and prints `[WATCHER-EXPIRED]` with the exact re-arm command.

**RE-ARM = ONE MONITOR CALL, SAME TURN, NO SKILL LOAD.** Copy the command from the `[WATCHER-EXPIRED]` line and arm it
with `timeout_ms: 1800000`. Run this full skill only at load, after a restart, or when events stop arriving.

History and the incidents behind each trap: `docs/references/WATCHER_HISTORY.md`.

## Steps (at load)

0. **Serial** = your FULL serial including any `~lane`. A lane inbox is `org/mcp/inbox/<base>/~<lane>/`, never
   `inbox/<base>~<lane>/`.
1. **Registration:** `get_agent_status(<serial>)`; if STALE or absent, `register_agent(<serial>, summary=...)`.
2. **Census your script rows** (PowerShell; the `@( )` wrap is load-bearing in 5.1):
   ```powershell
   $rows = @(Get-CimInstance Win32_Process -Filter "Name='bash.exe'" |
     Where-Object { $_.CommandLine -match 'inbox-watch\.sh <serial-regex> stream' -and $_.CommandLine -notmatch ' -c ' })
   $rows | Select-Object ProcessId, CreationDate ; "script rows: $($rows.Count)"
   ```
   - **0 rows:** arm (step 3).
   - **1 row:** healthy if you armed it this session. Reap nothing.
   - **N>1:** `Stop-Process -Id <pid> -Force` every row EXCEPT the pid you RECORDED at your last arm. No recorded
     pid means reap nothing and re-arm. MSYS `kill` fails silently on an aged orphan, so never use it.
3. **Arm:** resolve the prefix (`test -d /cygdrive/c && echo /cygdrive/c || echo /c`), then call the Monitor tool with
   command `bash <prefix>/Users/AndrewBerman/Desktop/ajb_workspace/org/mcp/inbox-watch.sh <serial> stream` and
   `timeout_ms: 1800000`. Re-run the census and RECORD the new row's ProcessId, because every arm creates a new pid.
4. **Inbox pull:** `check-inbox <serial>`, plus `get_delivery_state(<serial>, since=<last alive>)`. Every row not
   READ is unread mail: read it, act, then `ack_messages` it.
5. **Report:** `heartbeat(<serial>, summary=...)`, then:
   ```
   /watcher <serial>
     REGISTRATION: OK | re-registered
     MONITOR:      armed task <id>, script pid <pid> | reaped <pids>
     INBOX:        empty | N acted
   ```

## Traps (one line each)

- `TaskList` does not list Monitors; an empty TaskList proves nothing.
- Never launch stream mode under Bash `run_in_background`: it notifies only on exit, and stream mode never exits.
- A live watcher's parent shell reads DEAD seconds after the arm. That is normal; a dead parent is not the test.
- An orphan steals mail (`mv` to `read/`, then echo into a dead pipe). `read/`, `ps` and mtimes are not delivery
  evidence; only an ack is.
- A wrong drive prefix returns a task id, then dies `exit 127` in a separate notification.
- The agentbus consumer (`/agentbus`) is a separate Monitor with the same 30-minute death; re-arm it on its expiry
  notice.
- No `/watcher` cron and no loop. The Monitor is the standing mechanism.
