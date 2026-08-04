# Claude Code hooks — ajb_workspace

PostToolUse / PreToolUse hook scripts wired into `.claude/settings.local.json`.
That settings file is git-tracked, so wiring here reaches every agent on the
workspace (sessions pick it up on next launch).

## Hooks

| Script | Hook | Matcher | Purpose |
|--------|------|---------|---------|
| `block-bare-inbox-watch.sh` | PreToolUse | `Bash\|PowerShell` | Rejects bare-relative-path `inbox-watch.sh` launches that create PPID=1 zombies. |
| `post-tool-telemetry.sh` | PostToolUse | `*` | Per-tool-call agent telemetry — appends one JSONL line per call to `org/mcp/agent_telemetry/<serial>.jsonl`. |
| `post-send-commitment.sh` | PostToolUse | `*` | Active-commitment detection — scans outbound `send_message` bodies for commitment language and appends to the sender's `.active-commitments` ledger. |

Ported from corporeal `mcp_runner/hooks/` (2026-05-20). See the incorporation
plan and `org/mcp/agent_telemetry/` + `org/mcp/append-commitment.sh`.

## Agent identity attribution

Both PostToolUse hooks resolve the agent serial in this order:

1. `OPAL_AGENT_SERIAL` environment variable (set it before launching `claude`
   for per-process attribution that survives a shared working directory).
2. `SERIAL=` line in `.comp-graph/.agent_context` (written by `org/XXX.md`
   startup Step 1 E — the workspace-native fallback).
3. `_unknown` — debugging signal that a session is unattributed.

## Telemetry output

`org/mcp/agent_telemetry/<serial>.jsonl` (gitignored — ephemeral runtime state),
one append-only line per tool call:

```
{"ts":"2026-05-20T13:24:43Z","agent":"0.4.0_DS_ClientPlatform","tool":"Edit","kind":"work","session_id":"abc123"}
```

### `kind` field

- `loop` — supervisor/infrastructure tool calls that should NOT count toward
  staleness: `check_inbox` / `heartbeat` / roster polls, Bash matching
  `inbox-watch` / `check-inbox` / `kill-orphans` / `pgrep -f inbox-watch`,
  `Skill` invocations for `loop` or `stimulus-scan`.
- `work` — everything else (Edit, Read, real Bash, `send_message`, …).

A consumer computes staleness against the last `kind:work` ts, so an agent
whose only recent activity is self-pinging the watcher correctly reads as
STALE despite fresh telemetry entries.

## Failure mode

Both hooks are silent-fail (`set -u`, never `set -e`, always `exit 0`). A hook
error must never disrupt the agent. Missing telemetry surfaces downstream as a
gap in classification — a meta-signal that the hook itself is misconfigured.

## Hardening (defer until a pattern surfaces)

- **Disk growth** — JSONL files grow unbounded. Add rotation if needed:
  `find org/mcp/agent_telemetry -name '*.jsonl' -mtime +7 -delete`.
- **Torn lines** — POSIX guarantees atomic writes <4KB; wrap `printf >>` in
  `flock` only if torn lines are ever observed (note: `flock` is absent from
  Git Bash 3.6.7 — see CLAUDE.md Rule 16).
