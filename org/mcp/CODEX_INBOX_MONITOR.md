# Codex inbox monitor with real turn wake

This is the Codex counterpart to Claude's harness-owned `/watcher`. It is a
local Codex host mechanism, not a `config.toml` notification setting.

This contract is complete and repository-closed. Codex agents must not browse
the web, consult external/OpenAI documentation, or infer missing setup steps.
Use only the checked-in launcher, handoff, heartbeat, bridge, detector, and
instructions named here. A missing or conflicting local behavior is a repo
defect to report, not an invitation to research or improvise.

## Required architecture

```text
non-consuming detector
        |
        v
shared app-server turn bridge ----> active thread: turn/steer
        |                           idle thread: turn/start
        v
interactive TUI on the same app-server
        |
        v
agent reads exact file -> ACKs/begins -> acts -> moves exact file to read/
```

The shared app-server is load-bearing. On Windows, a bare `codex queue` starts
a separate embedded app-server. It can persist a queued message, but it cannot
wake a thread that is already idle in another embedded process. The canonical
launcher therefore hosts both the TUI and bridge on one loopback WebSocket
app-server.

## Canonical tool inventory

| Reference | Classification | Codex use |
|---|---|---|
| `.tools/ajb2.ps1` / `ajb2` | **CODEX — REQUIRED ENTRY ALIAS** | Mirrors Claude's `ajb`: creates the exact-serial Windows Terminal tab, sets the color signal, and delegates to the seat launcher. |
| `org/mcp/start-codex-seat.ps1` | **CODEX — REQUIRED LAUNCHER** | Owns the shared loopback app-server, TUI, turn bridge, and heartbeat lifecycle; applies the full-serial tab title and interactive color environment; and pins both app-server and TUI to `:danger-full-access` with approval policy `never`. |
| `org/mcp/handoff-codex-seat.ps1` | **CODEX — MIGRATION HANDOFF** | Waits for one verified legacy `codex.exe` PID to exit, then resumes through the canonical launcher without inline-command quoting. |
| `org/mcp/codex-inbox-turn-bridge.py` | **CODEX — REQUIRED TURN BRIDGE** | Converts detector output into `turn/steer` for an active turn or direct `turn/start` for an idle turn; same-host queue is a race fallback. |
| `org/mcp/codex-inbox-monitor.py` | **CODEX — REQUIRED DETECTOR** | Emits root-level `[HARD-NUDGE] <filename>` without reading, moving, deleting, or ACKing mail. The turn bridge starts it; do not launch a duplicate. |
| `org/mcp/codex-agent-heartbeat.py` | **CODEX — REQUIRED HEARTBEAT** | Registers the full serial and maintains independent broker/liveness heartbeats. The launcher starts it. |
| `org/mcp/CODEX_INBOX_MONITOR.md` | **CODEX — REQUIRED STARTUP GUIDE** | This architecture and operating contract. |
| `AGENTS.md` | **CODEX — AUTO STARTUP POINTER** | Routes every new Codex workspace session here. |
| `org/XXX.md` Step 1b, Codex runtime branch | **SHARED STARTUP AUTHORITY** | Identity, path, ACK, and post-action handling rules. |
| `org/mcp/server.py` -> `org/mcp/broker.py` | **DEPENDENCY — DO NOT START MANUALLY** | Registration and broker implementation used by the heartbeat companion. |
| `org/mcp/inbox-watch.sh` | **CLAUDE — FORBIDDEN FOR CODEX** | Consuming stream watcher; moves mail before notification. |
| `org/mcp/check-inbox.sh` | **CONSUMING — FORBIDDEN FOR CODEX MONITORING** | Consumes mail during a check. |
| `org/mcp/agent-poller.py` | **CLAUDE LIFECYCLE — DO NOT USE FOR CODEX** | Generic poller whose inbox companion is consuming. |
| `.claude/skills/watcher/SKILL.md` | **REFERENCE ONLY** | Documents Claude's harness-native Monitor behavior. |

Never run `inbox-watch.sh ... stream`, `check-inbox.sh`, another
`codex-inbox-monitor.py`, or the old `notify()`/`yield_control()` bridge for the
same serial while the shared-host launcher is active.

Before its duplicate-process assertion, the launcher invokes the existing
serial-scoped registration cleanup hook. That hook delegates to
`.tools/kill-orphans --serial <FULL_SERIAL> --force` for the legacy Bash/MSYS
watcher set and, on Windows, also reaps the same exact serial's native Codex
runtime leftovers: heartbeat, turn bridge, detector, and the recorded loopback
app-server tree. The final conflict scan remains an exact-serial assertion.
Never replace this with an unscoped `kill-orphans --force` call.

## Startup

For migration from an older embedded Codex session:

1. Record `CODEX_THREAD_ID` and finish the current turn/session log.
2. Stop the old same-serial watcher and heartbeat helpers.
3. **Exit the old Codex TUI completely.** The TUI owns the thread's persistence
   writer; stopping helper scripts does not release it.
4. From a separate PowerShell prompt, use the handoff helper below. It waits
   for the verified old `codex.exe` PID and launches only after it exits.

```powershell
powershell -NoExit -ExecutionPolicy Bypass `
  -File org/mcp/handoff-codex-seat.ps1 `
  -Serial '4.0.0_SA_CRO~A' `
  -ThreadId '01xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' `
  -LegacyCodexPid 12345
```

Do not assemble an inline `-Command` string containing `$Host`; an outer
PowerShell can expand it before the child starts. The checked-in handoff script
sets its own title without a second parsing layer.

Launch through the `ajb2 <FULL_SERIAL>` alias. Mirroring the established Claude
`ajb` path, `ajb2` creates a Windows Terminal tab with the exact serial as its
creation title; the machine's `profiles.defaults.suppressApplicationTitle`
setting keeps Codex's dynamic title from replacing it. The seat launcher also
removes an inherited `NO_COLOR`, replaces
`TERM=dumb` for the foreground TUI, and supplies standard color-capability
variables. Those environment changes are scoped to the interactive Codex
process and are restored when it exits.

The launcher supplies the same permission-profile overrides to the shared
app-server and to both foreground TUI paths (new thread and resumed thread):

```powershell
-c 'default_permissions=":danger-full-access"' `
-c 'approval_policy="never"'
```

This is intentionally the current permission-profile mechanism, not a legacy
`sandbox_mode` override. It prevents a bridge-originated `turn/start` from
falling back to managed `workspace-write` / `on-request` defaults. Permission
state is snapshotted into a turn context, so changing `/permissions` cannot
repair an already-active turn: exit and relaunch/resume through `ajb2`, then
verify the first new `turn_context` records `approval_policy = never`,
`sandbox_policy = danger-full-access`, and `permission_profile = disabled`.

From the workspace root, launch a new Codex seat:

```powershell
ajb2 '4.0.0_SA_CRO~A'
```

To resume a known Codex thread on the shared host:

```powershell
ajb2 '4.0.0_SA_CRO~A' `
  -ThreadId '01xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

With `-ThreadId`, the launcher preflights `thread/resume` before starting the
heartbeat, bridge, or replacement TUI. If the old TUI still owns the active
writer, it stops with an explicit close-old-TUI message and cleans up the whole
launcher-owned app-server process tree. Never work around the writer lock by
starting another app-server or copying the rollout file.

When `-ThreadId` is omitted, the bridge waits for the one loaded CLI thread the
new remote TUI creates in this workspace and binds to it. Runtime logs are
written under the ignored `.runtime/codex-seats/<serial>/` directory. Exiting
the TUI stops only the launcher-owned app-server, bridge, detector, and
heartbeat process trees, including CLI-shim descendants.

Requirements:

- Codex CLI with `app-server`, `--remote`, `turn/start`, `thread/queue/add`, `turn/steer`, and
  thread runtime statuses. This implementation was built and tested against
  `codex-cli 0.149.1`.
- Python package `websockets` (version 16 is installed on the reference host).
- A loopback WebSocket endpoint. The launcher never exposes a non-loopback
  listener.

## Delivery state machine

For every exact detector line:

1. Query `thread/read(includeTurns=true)` on the shared app-server.
2. If `active`, steer the exact in-progress turn using its ID.
3. If `idle`, call `turn/start` directly. This instantiates a model turn while
   no prior turn is active.
4. If `notLoaded`, resume the thread on the shared host, then call `turn/start`.
5. If a non-steerable review/compact turn rejects steering, defer without
   queueing; the detector retries after the active boundary.
6. For the rare resume/start status race, keep at most one same-host queued
   submission per `(serial, filename)`.
7. Recheck the exact root-level file immediately before every start, steer, or
   queue dispatch. A background cancellation task deletes all matching queued
   submissions as soon as the file moves out of unread.
8. At bridge startup, reconcile legacy queue state: delete every stale-file
   nudge and collapse live-file duplicates to one.

The prompt names only the detected filename and states the handling order. It
does not include message contents; reading remains an explicit agent act.

## Required agent handling order

1. Read the exact filename from the canonical unread root.
2. Treat a CRO Base message as immediate Go unless its body explicitly says hold.
3. ACK by naming specific message content and begin immediately.
4. Complete the required first action/handling.
5. Move only that exact file into `read/`.

Neither detector nor bridge performs step 5.

## Why the old bridge did not work

`notify()` plus `yield_control()` injects detector output at a tool boundary of
an already-active model turn. After the agent yields its final response there
is no model-side execution left to call either function, so it cannot create a
new turn. The dormant-wake primitive belongs to the conversation host:
`turn/start`; the same-host queue is retained only as a durable race fallback.

## Tests

```powershell
python -m unittest `
  org.mcp.tests.test_codex_inbox_monitor `
  org.mcp.tests.test_codex_inbox_turn_bridge -v
```

The detector tests prove exact output and non-consumption. The turn-bridge
tests prove direct idle -> start, active -> steer, unloaded -> resume/start,
single-entry race fallback, non-steerable deferral, exact-file cancellation,
legacy duplicate collapse, and cancellation after a file move without another
detector event.
