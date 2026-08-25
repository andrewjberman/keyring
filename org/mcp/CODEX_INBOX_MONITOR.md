# Codex non-consuming inbox monitor

This is the Codex counterpart to the Claude-oriented consuming stream watcher.
It is a local session mechanism, not a standard Codex configuration setting.

## Components

- `codex-inbox-monitor.py` detects root-level `.md` arrivals and writes only
  `[HARD-NUDGE] <filename>` to stdout. It repeats the line every 15 seconds
  while the file remains unread. It cannot read, move, delete, or ACK.
- A persistent Codex `functions.exec` bridge forwards each detector line with
  `notify(line)` and immediately calls `yield_control()`.
- `codex-agent-heartbeat.py` separately registers the full serial and maintains
  broker/liveness heartbeats. It cancels the Claude-oriented broker poller so it
  cannot compete with the detector for message delivery.

## Canonical tool inventory

Give this table to any Codex lane. Paths are workspace-relative and
device-independent.

| Reference | Classification | Codex use |
|---|---|---|
| `org/mcp/codex-inbox-monitor.py` | **CODEX — REQUIRED** | Non-consuming root-level `.md` detector; initial backlog + 15-second repeat nudges. |
| `org/mcp/codex-agent-heartbeat.py` | **CODEX — REQUIRED** | Full-serial registration and independent broker heartbeat; disables the consuming broker poll task. |
| `org/mcp/CODEX_INBOX_MONITOR.md` | **CODEX — REQUIRED STARTUP GUIDE** | Contains the persistent `functions.exec` `notify()`/`yield_control()` bridge and handling order. |
| `AGENTS.md` | **CODEX — AUTO STARTUP POINTER** | Routes a newly opened Codex workspace session to `org/XXX.md` and this guide. |
| `org/XXX.md` Step 1b, Codex runtime branch | **SHARED STARTUP AUTHORITY** | Identity/path/ACK rules and the Codex-vs-Claude branch. |
| `org/mcp/server.py` | **DEPENDENCY — DO NOT START MANUALLY** | Registration/heartbeat implementation imported by the Codex companion. |
| `org/mcp/broker.py` | **DEPENDENCY — DO NOT DUPLICATE** | SQLite-backed broker singleton used through `server.py`. |
| `org/mcp/inbox-watch.sh` | **CLAUDE — FORBIDDEN FOR CODEX** | Consuming stream watcher; moves mail before emitting. |
| `org/mcp/check-inbox.sh` | **CONSUMING — FORBIDDEN FOR CODEX MONITORING** | Consuming inbox check; not a Codex sweep. |
| `org/mcp/agent-poller.py` | **CLAUDE LIFECYCLE — DO NOT USE FOR CODEX** | Generic MCP-server-PID poller whose documented inbox companion is consuming. |
| `.claude/skills/watcher/SKILL.md` | **REFERENCE ONLY** | Explains Claude's harness-native Monitor behavior; not a Codex skill or launcher. |

Never run `inbox-watch.sh <serial> stream`, `check-inbox.sh`, or another
consuming watcher for the same serial while this mechanism is active.

## Codex bridge

Run the heartbeat companion as one persistent command:

```powershell
python -u org/mcp/codex-agent-heartbeat.py --serial '4.0.0_SA_CRO~A'
```

Run the detector from a persistent `functions.exec` cell. The bridge logic is:

```javascript
const started = await tools.exec_command({
  cmd: "python -u org/mcp/codex-inbox-monitor.py --serial '4.0.0_SA_CRO~A'",
  shell: "powershell",
  login: false,
  workdir: WORKSPACE_ROOT,
  yield_time_ms: 10000,
});
let state = started;
let pending = "";
while (state.session_id) {
  pending += state.output || "";
  const lines = pending.split(/\r?\n/);
  pending = lines.pop() || "";
  let nudged = false;
  for (const line of lines) {
    if (/^\[HARD-NUDGE\] [^\\/]+\.md$/i.test(line)) {
      notify(line);
      nudged = true;
    }
  }
  if (nudged) yield_control();
  state = await tools.write_stdin({session_id: state.session_id, yield_time_ms: 5000});
}
```

The workspace root is supplied by the active Codex session; neither script
contains a device-specific workspace path.

## Required handling order

1. Read the exact filename from the canonical unread root.
2. Treat a CRO Base message as immediate Go unless its body explicitly says hold.
3. ACK and begin the order immediately.
4. Complete the required first action/handling.
5. Move that exact file to `read/`.

The monitor never performs step 5. That mutation remains an explicit agent action.

## Claude `/watcher` comparison and Codex boundary

Claude's immediate interruption comes from its harness-native persistent Monitor
task. The consuming shell watcher is only the detector; it is not what starts a
model turn. Codex `notify()` plus `yield_control()` can surface detector output at
an active tool boundary, but the currently exposed Codex tools cannot create a
new reasoning turn after the agent has yielded its final response.

The repeat nudge closes a reliability gap: a transient notification or bridge
restart cannot make a still-unread file disappear from attention. It does not
claim to supply the missing dormant-turn wake primitive. Exact Claude parity
requires a Codex host callback that resumes the agent when `notify()` fires (or
an equivalent native monitor/automation trigger). Until then, every active turn
must begin by sweeping the canonical unread root before doing other work.

## Tests

```powershell
python -m unittest org.mcp.tests.test_codex_inbox_monitor -v
```

The tests assert exact output, root-only matching, repeat nudges, and that the
unread file still exists with identical content after every nudge.
