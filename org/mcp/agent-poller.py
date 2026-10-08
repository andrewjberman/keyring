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
    4. Single instance per serial via the named mutex Local\\opal-poller-<serial>;
       re-reads liveness[serial].pid each cycle and follows a re-registration;
       exits if the serial's entry is removed (never recreates it).

What it does NOT do:
    - Does NOT touch the inbox. Inbox watching is handled by a separate script:
      inbox-watch.sh (runs in background, checks every 5s, prints new messages
      to stdout, moves them to read/).
    - Does NOT delete liveness.json entries on exit. server.py's _clean_stale
      handles that on the next MCP write (within DEAD_THRESHOLD = 10 min).

Exit: Ctrl+C, kill -9, or MCP server PID dies. All three paths are clean —
the frozen last_seen_epoch is enough signal for the rest of the system.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from contextlib import contextmanager

SCRIPT_DIR = Path(__file__).resolve().parent
# OPAL_LIVENESS_FILE overrides the registry path (scratch exercises only); the
# default is unchanged.
LIVENESS_FILE = Path(os.environ.get("OPAL_LIVENESS_FILE") or (SCRIPT_DIR / "liveness.json"))
ORG_ROOT = SCRIPT_DIR.parent

# Heartbeat cadence. Bounded by server.py STALE_THRESHOLD (120s) -- a heartbeat
# must land well inside it or a live agent grades STALE. 15s leaves an 8x margin
# (40x against DEAD_THRESHOLD 600s) and cuts liveness.json rewrites ~87% vs the
# prior 2s, which was 60x oversampled against the 120s threshold it feeds.
# Andrew-direct 2026-07-30. Broker pruning is UNAFFECTED by this constant:
# broker.py _clean_stale evicts on _pid_alive(), not on heartbeat age.
POLL_INTERVAL = 15  # seconds
BROKER_PORT = int(os.environ.get("OPAL_BROKER_PORT", "7800"))
BROKER_URL = f"http://127.0.0.1:{BROKER_PORT}"

# File locking — use a separate .lock file so the lock covers the entire
# read-modify-write cycle. msvcrt.locking on the data file itself only
# locks 1 byte, which is insufficient when 5+ pollers write concurrently.
LOCK_FILE = LIVENESS_FILE.with_suffix(".lock")


# CL channel routing RETIRED (LD-0202 E2). Since LD-0034 ALL serials (ws + CL)
# use the unified opal-agent-comms broker (liveness.json, port 7800). The legacy
# per-CL-channel switch (_is_cl_serial / _switch_to_cl_channel -> complearns-
# agent-comms / cl_liveness.json / port 7801) routed CL serials to a broker that
# no longer runs -- dead routing. Removed.


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
    """Is a process with this PID actually RUNNING (not merely addressable)?

    A HANDLE IS NOT A RUNNING PROCESS. On Windows a process object outlives the
    process itself for as long as anyone holds a handle to it, so OpenProcess()
    SUCCEEDS on an exited-but-not-reaped pid. The previous implementation returned
    True on that handle and never asked whether the process had exited -- so this
    probe could not distinguish RUNNING from EXITED, and it was the sole liveness
    gate on the poller's exit path.

    Consequence (2026-07-13, exercised): when the host OOM'd and killed the fabric,
    2.0.0_SA_COO's MCP server (pid 15900) died -- and its poller kept writing
    last_seen every 2s and heartbeating the broker every 10s, indefinitely, because
    _pid_alive(15900) returned True. Every instrument in the fabric (get_live_agents,
    get_agent_status, fabric-check) reported a DEAD executive as LIVE with a 1-second
    heartbeat, fabric-check's DEAF detector could never fire for it, and the identity
    guard refused to respawn the serial because it was "held by a LIVE process."
    An absent field is a gap; a confident wrong field is a FALSE WITNESS.

    Measured, with the two live agents as positive controls:
        pid    who                    OpenProcess-only   GetExitCodeProcess
        12780  MSTR (alive, control)  True               True
        5876   CTO  (alive, control)  True               True
        15900  COO  (DEAD)            True               False   <-- the forgery

    So: assert STILL_ACTIVE. Never infer liveness from addressability.
    """
    if pid <= 0:
        return False
    if sys.platform == "win32":
        import ctypes
        kernel32 = ctypes.windll.kernel32
        PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        STILL_ACTIVE = 259
        handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
        if not handle:
            return False
        try:
            code = ctypes.c_ulong()
            ok = kernel32.GetExitCodeProcess(handle, ctypes.byref(code))
            if not ok:
                # Cannot read the exit code -> we CANNOT OBSERVE liveness. Say so by
                # failing closed (dead), never by defaulting to alive: the whole point
                # of this probe is to let a poller notice its agent is gone.
                return False
            return code.value == STILL_ACTIVE
        finally:
            kernel32.CloseHandle(handle)
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


_MUTEX_HANDLE = None  # held for the process lifetime; the OS frees it on exit


def _acquire_single_instance(serial: str) -> bool:
    """Take the per-serial named mutex. False = another poller already holds it.

    Windows only. The OS releases a named mutex when its last handle closes,
    which includes process death, so a crashed poller leaves no stale state.
    Fails open (returns True) if the mutex cannot be created at all.
    """
    global _MUTEX_HANDLE
    if sys.platform != "win32":
        return True
    import ctypes
    from ctypes import wintypes
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.CreateMutexW.restype = wintypes.HANDLE
    kernel32.CreateMutexW.argtypes = [ctypes.c_void_p, wintypes.BOOL, wintypes.LPCWSTR]
    ERROR_ALREADY_EXISTS = 183
    name = "Local\\opal-poller-" + re.sub(r"[^A-Za-z0-9._~-]", "_", serial)
    handle = kernel32.CreateMutexW(None, False, name)
    err = ctypes.get_last_error()
    if not handle:
        print(f"WARN: CreateMutexW failed for {name} (err {err}); continuing without "
              f"single-instance guard", file=sys.stderr)
        return True
    if err == ERROR_ALREADY_EXISTS:
        kernel32.CloseHandle(handle)
        return False
    _MUTEX_HANDLE = handle
    return True


def _read_entry_pid(serial: str) -> tuple[str, int | None]:
    """Read liveness[serial].pid. Returns (state, pid).

    state: "ok" (entry with an int pid), "gone" (serial absent from a readable
    file), or "unknown" (read failed, or entry has no int pid). Only "gone" is
    a verdict; "unknown" never ends the poller.
    """
    try:
        with _locked_liveness(write=False) as data:
            entry = data.get(serial)
            if entry is None:
                return "gone", None
            pid = entry.get("pid") if isinstance(entry, dict) else None
            if isinstance(pid, int):
                return "ok", pid
            return "unknown", None
    except Exception as e:
        print(f"WARN: liveness read failed: {e}", file=sys.stderr)
        return "unknown", None


def _update_heartbeat(serial: str) -> str:
    """Update last_seen_epoch in liveness.json. Returns "ok", "gone" or "error".

    Never recreates a deleted entry: an absent serial means the registration
    was removed (deregister / _clean_stale), and resurrecting it under the
    poller's own pid made the poller its own liveness witness.
    """
    now = time.time()
    try:
        with _locked_liveness(write=True) as data:
            if serial not in data:
                return "gone"
            data[serial]["last_seen"] = datetime.now(timezone.utc).isoformat()
            data[serial]["last_seen_epoch"] = now
        return "ok"
    except Exception as e:
        print(f"WARN: heartbeat failed: {e}", file=sys.stderr)
        return "error"


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
    # Single instance per serial, enforced by the poller itself (the launch
    # hook's pidfile check is only a fast path).
    if not _acquire_single_instance(serial):
        print(f"OK: poller already running for {serial} (named mutex held); exiting",
              file=sys.stderr)
        sys.exit(0)
    # All serials (ws + CL) use the unified opal-agent-comms broker since LD-0034.
    # The per-CL-channel switch is RETIRED (LD-0202 E2) -- see note above.
    channel = "opal-agent-comms"
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
    print("  Mode: HEARTBEAT ONLY (inbox handled by conversation-side MCP)")
    sys.stdout.flush()

    broker_cycle = 0
    try:
        while True:
            # Follow the registration: re-read liveness[serial].pid every cycle.
            # A re-register (new session, same serial) rewrites the pid; watch
            # the new server if it is live. A removed entry ends the poller.
            state, entry_pid = _read_entry_pid(full_serial)
            if state == "gone":
                print(
                    f"OK: {full_serial} no longer in {LIVENESS_FILE} -- poller exiting",
                    file=sys.stderr,
                )
                sys.exit(0)
            if (state == "ok" and entry_pid != mcp_pid and entry_pid != os.getpid()
                    and _pid_alive(entry_pid)):
                print(f"  Now tracking MCP server PID: {entry_pid} (was {mcp_pid})",
                      file=sys.stderr)
                mcp_pid = entry_pid

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

            # Heartbeat to liveness.json (every cycle = 15s). Never recreates.
            if _update_heartbeat(full_serial) == "gone":
                print(
                    f"OK: {full_serial} no longer in {LIVENESS_FILE} -- poller exiting",
                    file=sys.stderr,
                )
                sys.exit(0)

            # Heartbeat to broker (every 5th cycle = 75s, reduce HTTP chatter).
            # Cadence-independent for liveness: broker.py _clean_stale evicts on
            # _pid_alive(), never on heartbeat age -- so this may lag safely.
            broker_cycle += 1
            if broker_cycle >= 5:
                _broker_heartbeat(full_serial)
                broker_cycle = 0

            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print(f"\nPoller stopped for {full_serial}")


if __name__ == "__main__":
    main()
