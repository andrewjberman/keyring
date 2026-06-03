"""Background agent poller — keeps heartbeat alive every 2 seconds.

Usage (run in background at session startup):
    python org/mcp/agent-poller.py <agent_serial>

What it does:
    1. At startup, reads the MCP server PID from liveness.json[serial]["pid"]
       (written by the preceding register_agent call). This is the pid of the
       `python org/mcp/server.py` child process that the Claude Code session
       spawned for this agent. If the MCP server dies (terminal closed, session
       ended, crash), we treat the agent as gone and exit.
    2. Every 2 seconds, verifies the MCP server PID is still alive. If dead,
       exits cleanly so last_seen_epoch stops advancing and _clean_stale in
       server.py + broker.py naturally prunes the agent within their thresholds
       (no manual deregister_agent call needed).
    3. While the MCP server is alive, updates last_seen_epoch in liveness.json
       every 2 seconds and heartbeats the broker every 10 seconds.

What it does NOT do:
    - Does NOT touch the inbox. Inbox watching is handled by a separate script:
      inbox-watch.sh (runs in background, checks every 5s, prints new messages
      to stdout, moves them to read/).
    - Does NOT delete liveness.json entries on exit. server.py's _clean_stale
      handles that on the next MCP write (within DEAD_THRESHOLD = 10 min).

Exit: Ctrl+C, kill -9, or MCP server PID dies. All three paths are clean —
the frozen last_seen_epoch is enough signal for the rest of the system.
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from contextlib import contextmanager

SCRIPT_DIR = Path(__file__).resolve().parent
LIVENESS_FILE = SCRIPT_DIR / "liveness.json"
ORG_ROOT = SCRIPT_DIR.parent

POLL_INTERVAL = 2  # seconds
BROKER_PORT = int(os.environ.get("OPAL_BROKER_PORT", "7800"))
BROKER_URL = f"http://127.0.0.1:{BROKER_PORT}"

# File locking — use a separate .lock file so the lock covers the entire
# read-modify-write cycle. msvcrt.locking on the data file itself only
# locks 1 byte, which is insufficient when 5+ pollers write concurrently.
LOCK_FILE = LIVENESS_FILE.with_suffix(".lock")


# CL channel routing (ADHC_CLCOMM): COMP_LEARNS agents register on a
# physically-separate MCP channel (complearns-agent-comms) with its own
# liveness file (cl_liveness.json) and broker port (7801). hook_launch_poller
# spawns this same poller for both channels, so the poller routes itself by
# serial prefix at startup. Non-CL serials keep the existing opal-channel
# defaults (liveness.json + port 7800) — no behavior change for them.
CL_SERIAL_PREFIXES = ("1.1.0_", "2.1.0_")
CL_SERIAL_SUBSTRING = "_CompLearns"


def _is_cl_serial(serial: str) -> bool:
    base = serial.split("~", 1)[0]
    return base.startswith(CL_SERIAL_PREFIXES) or CL_SERIAL_SUBSTRING in base


def _switch_to_cl_channel() -> None:
    global LIVENESS_FILE, LOCK_FILE, BROKER_PORT, BROKER_URL
    LIVENESS_FILE = SCRIPT_DIR / "cl_liveness.json"
    LOCK_FILE = LIVENESS_FILE.with_suffix(".lock")
    BROKER_PORT = int(os.environ.get("CL_BROKER_PORT", "7801"))
    BROKER_URL = f"http://127.0.0.1:{BROKER_PORT}"


@contextmanager
def _locked_liveness(write=False):
    LIVENESS_FILE.touch(exist_ok=True)
    LOCK_FILE.touch(exist_ok=True)
    lock_fh = open(LOCK_FILE, "r+", encoding="utf-8")
    try:
        if sys.platform == "win32":
            import msvcrt
            # Retry loop — another poller may hold the lock briefly
            for _ in range(50):
                try:
                    msvcrt.locking(lock_fh.fileno(), msvcrt.LK_NBLCK, 1)
                    break
                except OSError:
                    time.sleep(0.05)
            else:
                msvcrt.locking(lock_fh.fileno(), msvcrt.LK_LOCK, 1)
        else:
            import fcntl
            fcntl.flock(lock_fh.fileno(), fcntl.LOCK_EX)

        # Lock acquired — safe to read/modify/write liveness.json
        raw = LIVENESS_FILE.read_text(encoding="utf-8").strip()
        data = json.loads(raw) if raw else {}
        yield data
        if write:
            LIVENESS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    finally:
        try:
            if sys.platform == "win32":
                import msvcrt
                lock_fh.seek(0)
                msvcrt.locking(lock_fh.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(lock_fh.fileno(), fcntl.LOCK_UN)
        except Exception:
            pass
        lock_fh.close()


def _find_agent_folder(serial: str) -> Path | None:
    """Find the agent's folder in the org hierarchy.

    Tier list MUST stay in parity with inbox-watch.sh's resolver
    (tier0_exec tier1_exec tier2_senior tier3_junior) — a divergence is
    exactly the MSTR infra-finding (2026-06-03): tier0_exec was omitted here,
    so the tier0 MSTR serial (org/tier0_exec/0.0.0_AB_MSTR) failed resolution,
    the poller exited immediately, last_seen_epoch decayed, and kill-orphans
    reap-exposed MSTR's LD-0146 stream watcher. (tier3_rd is absent from BOTH
    resolvers — a separate consistent gap, flagged, not a divergence.)
    """
    for tier in ["tier0_exec", "tier1_exec", "tier2_senior", "tier3_junior"]:
        tier_dir = ORG_ROOT / tier
        if not tier_dir.exists():
            continue
        for entry in tier_dir.iterdir():
            if entry.is_dir() and serial in entry.name:
                return entry
    return None


def _pid_alive(pid: int) -> bool:
    """Cross-platform check: does a running process exist with this PID?"""
    if pid <= 0:
        return False
    if sys.platform == "win32":
        import ctypes
        kernel32 = ctypes.windll.kernel32
        PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
        if handle:
            kernel32.CloseHandle(handle)
            return True
        return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def _read_mcp_pid(serial: str) -> int | None:
    """Read the MCP server PID that register_agent recorded for this serial.

    register_agent writes {"pid": os.getpid()} at the time of the call, where
    os.getpid() is the `python org/mcp/server.py` child process. The PostToolUse
    hook spawns this poller AFTER register_agent returns, so the entry should
    already be present. Retry a few times to tolerate any filesystem lag.
    """
    for _ in range(5):
        try:
            with _locked_liveness(write=False) as data:
                entry = data.get(serial)
                if entry and isinstance(entry.get("pid"), int):
                    return entry["pid"]
        except Exception:
            pass
        time.sleep(0.2)
    return None


def _update_heartbeat(serial: str) -> bool:
    """Update last_seen_epoch in liveness.json. Returns True if successful."""
    now = time.time()
    try:
        with _locked_liveness(write=True) as data:
            if serial not in data:
                data[serial] = {
                    "pid": os.getpid(),
                    "summary": "background poller active",
                    "registered_at": datetime.now(timezone.utc).isoformat(),
                    "last_seen": datetime.now(timezone.utc).isoformat(),
                    "last_seen_epoch": now,
                }
            else:
                data[serial]["last_seen"] = datetime.now(timezone.utc).isoformat()
                data[serial]["last_seen_epoch"] = now
        return True
    except Exception as e:
        print(f"WARN: heartbeat failed: {e}", file=sys.stderr)
        return False


def _broker_heartbeat(serial: str) -> None:
    """Best-effort heartbeat to the broker for cross-session visibility."""
    try:
        data = json.dumps({"serial": serial}).encode("utf-8")
        req = urllib.request.Request(
            f"{BROKER_URL}/heartbeat",
            data=data,
            method="POST",
            headers={"Content-Type": "application/json"},
        )
        urllib.request.urlopen(req, timeout=2)
    except Exception:
        pass  # broker may not be running; that's fine


def main():
    if len(sys.argv) < 2:
        print("Usage: python agent-poller.py <agent_serial>")
        sys.exit(1)

    serial = sys.argv[1]
    # Route to CL channel BEFORE any helper touches LIVENESS_FILE / BROKER_URL.
    # Helpers resolve module globals at call time, so mutating here is enough.
    channel = "opal-agent-comms"
    if _is_cl_serial(serial):
        _switch_to_cl_channel()
        channel = "complearns-agent-comms"
    # Strip instance suffix (e.g. "~A") before folder lookup -- org folders
    # never include the suffix. Keep the original serial for liveness.json ops
    # so ~A and ~B remain distinct entries.
    base_for_lookup = serial.split("~")[0]
    agent_folder = _find_agent_folder(base_for_lookup)

    if not agent_folder:
        print(f"ERROR: Agent folder not found for '{serial}'")
        sys.exit(1)

    # Use original serial (with suffix) so heartbeats update the correct
    # liveness.json entry and the broker tracks the right instance.
    full_serial = serial

    # Discover the MCP server PID we're proxying for. If we can't find it,
    # something is wrong with the hook ordering — exit rather than heartbeat
    # indefinitely for a phantom agent.
    mcp_pid = _read_mcp_pid(full_serial)
    if mcp_pid is None:
        print(
            f"ERROR: no MCP server PID for {full_serial} in {LIVENESS_FILE}; "
            f"poller exiting",
            file=sys.stderr,
        )
        sys.exit(0)

    print(f"Poller started for {full_serial} (my PID {os.getpid()})")
    print(f"  Channel: {channel} (broker port {BROKER_PORT})")
    print(f"  Tracking MCP server PID: {mcp_pid}")
    print(f"  Heartbeat interval: {POLL_INTERVAL}s")
    print(f"  Liveness: {LIVENESS_FILE}")
    print(f"  Mode: HEARTBEAT ONLY (inbox handled by conversation-side MCP)")
    sys.stdout.flush()

    broker_cycle = 0
    try:
        while True:
            # Watchdog: if the MCP server process we're proxying for has died,
            # the terminal was closed / session ended / process crashed. Exit
            # so last_seen_epoch stops advancing — server.py's _clean_stale
            # then prunes this agent within DEAD_THRESHOLD (10 min), and the
            # broker's _clean_stale prunes it within ~30s via its own PID
            # liveness check. No manual deregister_agent call required.
            if not _pid_alive(mcp_pid):
                print(
                    f"MCP server PID {mcp_pid} is no longer alive -- "
                    f"poller exiting for {full_serial}",
                    file=sys.stderr,
                )
                sys.exit(0)

            # Heartbeat to liveness.json (every cycle = 2s)
            _update_heartbeat(full_serial)

            # Heartbeat to broker (every 5th cycle = 10s, reduce HTTP chatter)
            broker_cycle += 1
            if broker_cycle >= 5:
                _broker_heartbeat(full_serial)
                broker_cycle = 0

            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print(f"\nPoller stopped for {full_serial}")


if __name__ == "__main__":
    main()
