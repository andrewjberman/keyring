"""PostToolUse hook launcher for agent-poller.py.

Invoked by the Claude Code harness after `mcp__opal-agent-comms__register_agent`
completes. Reads the hook JSON from stdin, extracts tool_input.agent_serial,
checks if a poller is already running for that serial via a pidfile, and
spawns `agent-poller.py <serial>` as a detached background process if not.

Detaches properly on both Windows (DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
and POSIX (start_new_session=True) so the poller survives after Claude Code
closes its tool-response channel.

Silent on success. Fast on the happy path (single pidfile stat).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def _poller_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    if sys.platform == "win32":
        try:
            out = subprocess.run(
                ["tasklist", "/FI", f"PID eq {pid}", "/FO", "CSV", "/NH"],
                capture_output=True,
                text=True,
                timeout=5,
            )
        except Exception:
            return False
        # tasklist prints "INFO: No tasks ..." to stdout when nothing matches
        return "python" in out.stdout.lower()
    try:
        os.kill(pid, 0)
        return True
    except Exception:
        return False


def _spawn_detached(cmd: list[str]) -> subprocess.Popen | None:
    try:
        if sys.platform == "win32":
            DETACHED_PROCESS = 0x00000008
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            return subprocess.Popen(
                cmd,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
                close_fds=True,
            )
        return subprocess.Popen(
            cmd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
            close_fds=True,
        )
    except Exception:
        return None


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

    script_dir = Path(__file__).resolve().parent
    poller = script_dir / "agent-poller.py"
    if not poller.exists():
        return 0

    pid_dir = script_dir / ".poller_pids"
    try:
        pid_dir.mkdir(exist_ok=True)
    except Exception:
        return 0

    # One pidfile per serial. Instance serials (e.g. "0.4.0_DS~B") are kept
    # distinct so parallel workers each get their own poller.
    safe_name = serial.replace("/", "_").replace("\\", "_")
    pidfile = pid_dir / f"{safe_name}.pid"

    if pidfile.exists():
        try:
            old_pid = int(pidfile.read_text(encoding="utf-8").strip())
        except Exception:
            old_pid = 0
        if _poller_alive(old_pid):
            return 0

    proc = _spawn_detached([sys.executable, str(poller), serial])
    if proc is not None:
        try:
            pidfile.write_text(str(proc.pid), encoding="utf-8")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
