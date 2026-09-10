# Codex launcher registration review and repair authorization

**archetype:** DIAGNOSE

Received by `3.0.0_SA_CVO` through the Codex user channel on 2026-09-10, recorded at 08:26 Eastern. Exact user instruction:

> Yeah it might be a good idea to take this as an opportunity to make sure that the launcher-owned heartbeat for the codex path actually handles registration properly in the event there is a little glitch there. If you identify the nature of the issue, you have egress to fix and commit on the spot.

Scope: inspect launcher-owned registration, identify the issue, fix and commit under this direct authorization. No push authorized or performed. No second heartbeat, detector, or turn bridge.

Initial evidence: the running heartbeat's startup log records registration of `3.0.0_SA_CVO` at PID 22328 and a connected broker. The local liveness entry and the broker's `/list-agents` response both independently name PID 22328. The sender warning comes from the separate one-shot send process, whose imported `server._my_serial` is unset; `codex-send.py` already documents that distinction.

Recovery finding: `server.heartbeat` refreshes local liveness and ignores the broker heartbeat response; the broker's heartbeat handler returns OK even if its UPDATE found no registered row. The Codex companion currently re-registers only when the LOCAL entry is missing. A lost broker row with surviving local liveness therefore has no recovery in that companion.

— 3.0.0_SA_CVO
