"""PostToolUse hook: SERIAL-SCOPED orphan-watcher cleanup on register_agent.

Invoked after mcp__opal-agent-comms__register_agent. Reads the registering serial
from stdin JSON (tool_input.agent_serial) and reaps ONLY that EXACT serial's orphan
watchers via `kill-orphans --serial <S> --force` -- tilde-specific, so an agent's
registration never touches another serial's (or another lane's) watcher.

REPLACES the prior fabric-wide `kill-orphans --stale --force` hook, which reaped
live-but-stale-reading watchers across the WHOLE fabric on every registration --
the root cause of the exit-143 LIVE-watcher reaps (MSTR analysis + Andrew-direct
2026-06-15: "it should only kill-orphans associated with the agent serial being
spawned, tilde-specific").

V4 self-kill guard (per-session marker): the scoped cleanup runs ONCE per
(session, serial), keyed on CLAUDE_CODE_SESSION_ID. At the first register the new
Monitor watcher is not yet armed (register precedes /watcher), so the only
same-serial watcher present is a prior-session orphan -- safe to reap. A
subsequent re-register in the SAME session finds the marker and SKIPS, so it can
never reap the agent's own now-live watcher. If CLAUDE_CODE_SESSION_ID is unset,
it degrades to run-every-register (V3 startup-safe + the rare V4 case is lossless).

Silent on success. Fast on the happy path (one marker stat).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    tool_input = payload.get("tool_input") or {}
    serial = tool_input.get("agent_serial")
    if not isinstance(serial, str) or not serial.strip():
        return 0
    serial = serial.strip()

    # org/mcp/<this>.py -> workspace
    workspace = Path(__file__).resolve().parent.parent.parent
    kill_orphans = workspace / ".tools" / "kill-orphans"
    if not kill_orphans.exists():
        return 0

    # V4 per-session marker: scoped cleanup runs once per (session, serial).
    marker = None
    session_id = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    if session_id:
        marker_dir = workspace / "org" / "mcp" / "sessions"
        try:
            marker_dir.mkdir(parents=True, exist_ok=True)
        except Exception:
            return 0
        safe_serial = serial.replace("/", "_").replace("\\", "_")
        marker = marker_dir / f"{session_id}.{safe_serial}.orphan-cleaned"
        if marker.exists():
            return 0  # already cleaned this session -> never reap the live watcher

    # Scoped, tilde-specific reap of THIS serial's orphan watchers only.
    try:
        subprocess.run(
            ["bash", str(kill_orphans), "--serial", serial, "--force"],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=12,
        )
    except Exception:
        pass

    if marker is not None:
        try:
            marker.write_text("1", encoding="utf-8")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
