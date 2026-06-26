# BROKER_OPS — how the agent-comms broker is run + restarted

One-read answer to "how do I restart the broker / why didn't my server.py change take effect."
Authored 2026-06-26 (1.0.0_SA_CTO + 0.0.0_AB_MSTR concur) after the LD-0220 tier0_utility
wiring fix (`b353b27dd`) took 3 messages to re-derive who restarts the broker and why it's
not an agent.

## The two processes (don't conflate them)

1. **`opal-agent-comms` — a RUNTIME-LAUNCHED MCP SERVER, not an agent-ownable daemon.**
   `.mcp.json`: `"opal-agent-comms": { "command": "python", "args": ["org/mcp/server.py"], cwd: workspace }`.
   The Claude Code runtime launches one `python org/mcp/server.py` (stdio) per client connection.
   It is the very channel agents message through — **an agent cannot kill/relaunch it** (no PID we
   own; MSYS `ps` can't even enumerate the detached native-Windows process). Resolution logic
   (`_resolve_agent_folder`, server.py ~389, incl. `TIER_DIRS`) is loaded **at MCP-server-process
   start**.

2. **`broker.py` on `:7800` — a separate SQLite-backed singleton.** Registration + message state
   lives here and **persists across an `opal-agent-comms` reconnect** (and across compaction). So a
   reconnect does NOT drop registrations or lose inbox messages (filesystem inboxes persist too).

## The operational fact (the thing people re-derive)

A **code change to `server.py`** (e.g. adding a `TIER_DIRS` entry, editing `_resolve_agent_folder`)
is **not live in any session already running** — every live session loaded the OLD `server.py` at
its start. The on-disk commit is inert until **the runtime relaunches the MCP server**.

- **Agents CANNOT self-apply a `server.py` change.** Committing it (BASE_EXEC lane) is necessary but
  not sufficient. Do not guess-kill the process.
- **Applying it is an OPERATOR action:** Andrew reconnects `opal-agent-comms` via the `/mcp` command
  (reconnect), or restarts the client. That re-execs `python org/mcp/server.py` with the new code.

## Procedure for a server.py change

1. Commit `org/mcp/server.py` (BASE_EXEC — CTO/COO/CVO) + push.
2. Ask the operator (Andrew) to **reconnect `opal-agent-comms`** (`/mcp` reconnect, or client restart).
   Low-risk: registration (`:7800` SQLite) + filesystem inboxes survive; only the in-memory resolver
   reloads.
3. **Verify** post-reconnect: a `send_message` to an agent the change newly enables RESOLVES (no
   "Recipient not found in org"); the new agent runs `/watcher` to register itself (resolution-enable
   and self-registration are distinct — the reconnect enables the broker to FIND the folder; the agent
   still calls `register_agent`).

## Why "not us"

Restarting a shared, runtime-owned MCP server from inside an agent session is both impossible (it's
the channel we speak through) and a fabric-wide control-plane action. The CTO/COO/CVO own the
`server.py` CODE (BASE_EXEC); the runtime/operator owns the process LIFECYCLE. Clean split.
