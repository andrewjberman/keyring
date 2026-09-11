# Codex workspace startup

Every Codex agent in this workspace must first read `org/XXX.md`. For messaging,
registration, and inbox monitoring, follow the **Codex runtime branch** in its
Step 1b and the canonical implementation guide at
`org/mcp/CODEX_INBOX_MONITOR.md`.

Codex seat startup is **repository-closed**. Do not browse the web, consult
external/OpenAI documentation, or infer a replacement procedure. Execute the
checked-in scripts and instructions exactly. If a required local file, command,
or behavior is missing or contradictory, report that as a repository defect;
do not research or improvise a workaround.

Codex must launch with the `ajb2 <FULL_SERIAL>` alias, which delegates to
`org/mcp/start-codex-seat.ps1`. The launcher hosts the TUI and
`org/mcp/codex-inbox-turn-bridge.py` on one app-server so an inbox arrival can
instantiate an idle turn or steer an active one. The bridge owns the
non-consuming `org/mcp/codex-inbox-monitor.py` detector; the launcher separately
owns `org/mcp/codex-agent-heartbeat.py`. It also owns the full-serial terminal
tab title and foreground TUI color environment. Never substitute the Claude consuming
`inbox-watch.sh ... stream`, `check-inbox.sh`, or the generic `agent-poller.py`.
Never launch a second detector or the retired model-side `notify()` bridge for
the same serial.

**Readiness is MEASURED, never announced** (repaired 2026-08-26). Liveness
freshness, broker connection, and the heartbeat summary are NOT readiness --
the summary is now computed from `bridge-state.json` + live PID probes, and
the one readiness oracle is `org\mcp\codex-seat-status.ps1 -Serial
<FULL_SERIAL>` (exit 0 = the full 9-check green conjunction; anything else
names the failed component). On a fresh seat the bridge SUPERVISES thread
discovery indefinitely (`[TURN-BRIDGE-WAITING]` lines in the runtime log are
normal until your first persisted turn) -- never conclude a failed launch
from a waiting bridge, and never work around it with a second helper.

**Routine outbound messages are ONE command, never research**:
`org\mcp\codex-send.ps1 -To <serial> -Subject "..." (-Body "..."|-BodyFile f)`
-- identity-gated on `OPAL_AGENT_SERIAL`, canonical nested routing, broker
push, structured receipt. No comp-which, no governance classification, no
hand-built inbox paths for a peer message.

When migrating an already-open embedded session, use
`org/mcp/handoff-codex-seat.ps1` from a separate PowerShell. Record the thread
ID, stop old helpers, then exit the old TUI; its `codex.exe` writer must close
before the shared-host launcher can resume that thread.

At the beginning of every active turn, sweep the canonical root-level inbox for
the full suffixed serial. A message is an immediate Go, whoever sent it, when it
names a task order in your own `task_orders/` home issued by `2.0.0_SA_COO` (or
its lane), or when it triggers an act the spine assigns to your seat by name (the
L1 brief, the L4-R PRD sign-off, the L8 compile, L9 adjudication and L10 slug --
`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`, owner table), unless its body
explicitly says hold: read the exact file, ACK and begin, act, and only then move
that exact file into `read/`. Any other ask is information or is routed back to
its sender; no sender serial makes a message a Go by itself.
