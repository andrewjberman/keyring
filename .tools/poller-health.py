#!/usr/bin/env python
"""poller-health -- CORRECT fabric-wide agent-poller health check.

Replaces the broken `ps -ef | grep agent-poller.py` detection that produced a
FALSE "0 pollers fabric-wide" alarm on 2026-06-05 (which kicked off a whole
poller FIX-charter for a non-problem). Root cause of the false negative: pollers
are spawned DETACHED (DETACHED_PROCESS, no MSYS parent) as native Windows
python.exe, and Git Bash's MSYS `ps -ef` does NOT enumerate detached native
Windows processes -> the grep finds zero even when every poller is running.

THE AUTHORITATIVE SIGNAL is liveness.json freshness, NOT a process grep: the
agent-poller's entire job is to refresh liveness.json[serial]["last_seen_epoch"]
every ~2s while its MCP server is alive. So an agent with FRESH liveness (<600s)
HAS a working poller by definition; a registered agent gone STALE (>600s) is the
real "poller down (or session ended)" signal. We corroborate with the
.poller_pids/<serial>.pid PID where present (secondary; can be stale via PID
reuse), but liveness-freshness is the truth.

Usage:
  python .tools/poller-health.py            # human report + exit 0 (healthy) / 1 (alert)
  python .tools/poller-health.py --quiet     # one-line verdict only

LOUD by design: prints a clear ALERT line if 0 agents are fresh (genuine
fabric-wide poller outage = comms-at-risk) so a REAL outage surfaces as an alert
rather than silently. Rule-16 safe: pure python (no pgrep/pkill/flock), works
with the Git-Bash-3.6.7 default install.
"""
from __future__ import annotations

import io
import json
import os
import sys
import time
from pathlib import Path

FRESH_SECS = 600  # matches kill-orphans live-threshold (LD-0063)
ROOT = Path(__file__).resolve().parent.parent
LIVENESS = ROOT / "org" / "mcp" / "liveness.json"
PID_DIR = ROOT / "org" / "mcp" / ".poller_pids"


def _pid_alive(pid: int) -> bool:
    if not pid or pid <= 0:
        return False
    if sys.platform == "win32":
        try:
            import subprocess
            out = subprocess.run(
                ["tasklist", "/FI", f"PID eq {pid}", "/FO", "CSV", "/NH"],
                capture_output=True, text=True, timeout=5,
            )
            return "python" in out.stdout.lower()
        except Exception:
            return False
    try:
        os.kill(pid, 0)
        return True
    except Exception:
        return False


def _poller_pid(serial: str):
    f = PID_DIR / f"{serial.replace('/', '_').replace(chr(92), '_')}.pid"
    if not f.exists():
        return None
    try:
        return int(f.read_text(encoding="utf-8").strip())
    except Exception:
        return None


def main(argv) -> int:
    quiet = "--quiet" in argv
    try:
        data = json.load(io.open(LIVENESS, encoding="utf-8"))
    except Exception as e:
        print(f"POLLER-HEALTH ALERT: cannot read liveness.json ({e}) -- cannot assess fabric poller health")
        return 1
    if not isinstance(data, dict):
        print("POLLER-HEALTH ALERT: liveness.json malformed")
        return 1

    now = time.time()
    fresh, stale = [], []
    for serial, entry in data.items():
        if not isinstance(entry, dict):
            continue
        try:
            age = now - float(entry.get("last_seen_epoch") or entry.get("last_seen") or 0)
        except Exception:
            continue
        (fresh if age < FRESH_SECS else stale).append((serial, age, entry.get("pid")))

    n_fresh = len(fresh)
    if not quiet:
        print(f"=== poller-health ({time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(now))}) ===")
        for serial, age, mcp_pid in sorted(fresh):
            ppid = _poller_pid(serial)
            corrob = ("poller-pid alive" if ppid and _pid_alive(ppid)
                      else "poller-pid stale/absent (liveness fresh = poller working anyway; pidfile lag)")
            print(f"  FRESH  {serial}: liveness {age:.0f}s  | {corrob}")
        for serial, age, mcp_pid in sorted(stale):
            print(f"  STALE  {serial}: liveness {age:.0f}s (>600s -- session ended or poller down)")

    if n_fresh == 0:
        print("POLLER-HEALTH ALERT: 0 agents with fresh liveness (<600s) -- pollers may be DOWN fabric-wide; MCP comms at risk. (If you ran `ps|grep agent-poller` and saw 0, that is an MSYS false-negative on detached Windows python -- this check is authoritative.)")
        return 1
    print(f"POLLER-HEALTH OK: {n_fresh} agent(s) with fresh liveness (<600s) = {n_fresh} working poller(s); {len(stale)} stale/ended.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
