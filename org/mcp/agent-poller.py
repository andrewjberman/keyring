"""Background agent poller — keeps heartbeat alive every 2 seconds.

Usage (run in background at session startup):
    python org/mcp/agent-poller.py <agent_serial>

What it does:
    1. Updates last_seen_epoch in liveness.json every 2 seconds (keeps agent LIVE)
    2. Heartbeats the broker (if running) for cross-session visibility

What it does NOT do:
    - It does NOT touch the inbox. Inbox watching is handled by a separate
      script: inbox-watch.sh (runs in background, checks every 5s, prints
      new messages to stdout, moves them to read/).

Exit: Ctrl+C or kill the process. The agent will go STALE after 2 minutes,
DEAD after 10 minutes, then get cleaned from liveness.json automatically.
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

# File locking (Windows-compatible)
if sys.platform == "win32":
    import msvcrt
    def _lock_file(f, exclusive=False):
        msvcrt.locking(f.fileno(), msvcrt.LK_LOCK if exclusive else msvcrt.LK_LOCK, 1)
    def _unlock_file(f):
        try:
            f.seek(0)
            msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
        except Exception:
            pass
else:
    import fcntl
    def _lock_file(f, exclusive=False):
        fcntl.flock(f.fileno(), fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)
    def _unlock_file(f):
        fcntl.flock(f.fileno(), fcntl.LOCK_UN)


@contextmanager
def _locked_liveness(write=False):
    LIVENESS_FILE.touch(exist_ok=True)
    mode = "r+" if write else "r"
    try:
        f = open(LIVENESS_FILE, mode, encoding="utf-8")
    except FileNotFoundError:
        LIVENESS_FILE.write_text("{}", encoding="utf-8")
        f = open(LIVENESS_FILE, mode, encoding="utf-8")
    try:
        _lock_file(f, exclusive=write)
        raw = f.read().strip()
        data = json.loads(raw) if raw else {}
        yield data
        if write:
            f.seek(0)
            f.truncate()
            json.dump(data, f, indent=2)
    finally:
        _unlock_file(f)
        f.close()


def _find_agent_folder(serial: str) -> Path | None:
    """Find the agent's folder in the org hierarchy."""
    for tier in ["tier1_exec", "tier2_senior", "tier3_junior"]:
        tier_dir = ORG_ROOT / tier
        if not tier_dir.exists():
            continue
        for entry in tier_dir.iterdir():
            if entry.is_dir() and serial in entry.name:
                return entry
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
    agent_folder = _find_agent_folder(serial)

    if not agent_folder:
        print(f"ERROR: Agent folder not found for '{serial}'")
        sys.exit(1)

    full_serial = agent_folder.name
    print(f"Poller started for {full_serial} (PID {os.getpid()})")
    print(f"  Heartbeat interval: {POLL_INTERVAL}s")
    print(f"  Liveness: {LIVENESS_FILE}")
    print(f"  Mode: HEARTBEAT ONLY (inbox handled by conversation-side MCP)")
    sys.stdout.flush()

    broker_cycle = 0
    try:
        while True:
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
