#!/usr/bin/env python3
"""Machine-readable Codex seat readiness probe.

Exit 0 ONLY on the full green conjunction; any missing, duplicate, or
contradictory component is nonzero with the exact failed check named.

WHY THIS EXISTS (2026-08-26): the fabric had NO single instrument that
answered "is this seat actually reachable?" -- liveness freshness, broker
connection, and the heartbeat's (then-hardcoded) summary all read green on a
seat whose bridge had exited and whose detector never spawned. Every partial
probe was producer-side. This probe is the consumer-side conjunction:

  1. bridge-state.json exists and parses            (the binding record)
  2. app-server accepts a TCP connect on the bound endpoint
  3. exactly ONE heartbeat process for the EXACT serial
  4. exactly ONE bridge process for the EXACT serial, pid == state
  5. exactly ONE detector process for the EXACT serial, pid == state
  6. thread bound (nonempty thread_id)
  7. liveness entry fresh AND its pid IS the observed heartbeat pid
  8. NO consuming watcher (inbox-watch.sh) holds this serial
  9. unread root-level inbox count (informational, never gates)

Exact-serial matching uses the launcher's own lookaround pattern, so a base
serial never matches its lanes (2.0.0_SA_COO vs 2.0.0_SA_COO~X class).
"""

from __future__ import annotations

import argparse
import json
import re
import socket
import subprocess
import sys
import time
from pathlib import Path


def workspace_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_runtime_dir(serial: str) -> Path:
    sanitized = re.sub(r"[^A-Za-z0-9_.~-]", "_", serial)
    return workspace_root() / ".runtime" / "codex-seats" / sanitized


def enumerate_processes() -> list[dict]:
    """[{pid, cmdline}] for every process with a command line. PowerShell CIM
    is the one enumerator on this box that reliably yields full command lines
    (MSYS ps truncates and misses detached natives -- measured trap)."""
    script = (
        "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine } | "
        "ForEach-Object { [pscustomobject]@{ pid = $_.ProcessId; "
        "cmdline = $_.CommandLine } } | ConvertTo-Json -Compress"
    )
    out = subprocess.run(
        ["powershell", "-NoProfile", "-Command", script],
        capture_output=True, text=True, timeout=60,
    )
    if out.returncode != 0 or not out.stdout.strip():
        raise RuntimeError(f"process enumeration failed: {out.stderr.strip()[:200]}")
    data = json.loads(out.stdout)
    if isinstance(data, dict):
        data = [data]
    return [{"pid": int(d["pid"]), "cmdline": str(d["cmdline"])} for d in data]


def serial_pattern(serial: str) -> re.Pattern:
    # The launcher's own exact-serial lookaround: no substring match in either
    # direction (base !~ lane, lane !~ base).
    return re.compile(r"(?<![\w~])" + re.escape(serial) + r"(?![~\w])")


def matching(procs: list[dict], component: str, serial: str) -> list[int]:
    pat = serial_pattern(serial)
    return [
        p["pid"] for p in procs
        if component in p["cmdline"] and pat.search(p["cmdline"])
    ]


def probe_seat(
    serial: str,
    runtime_dir: Path,
    procs: list[dict],
    liveness: dict,
    now_epoch: float,
    tcp_probe=None,
) -> dict:
    """Pure over its inputs (process table, liveness dict, clock, TCP probe
    callable) so every arm is unit-testable without a live seat."""
    checks: dict[str, dict] = {}

    def check(name: str, ok: bool, detail: str) -> None:
        checks[name] = {"ok": bool(ok), "detail": detail}

    # 1. binding record
    state = None
    state_path = runtime_dir / "bridge-state.json"
    if state_path.is_file():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
            check("bridge_state", True, str(state_path))
        except (OSError, ValueError) as exc:
            check("bridge_state", False, f"unparseable: {exc}")
    else:
        check("bridge_state", False, f"absent: {state_path}")

    # 2. app-server endpoint
    endpoint = str((state or {}).get("endpoint") or "")
    m = re.fullmatch(r"ws://127\.0\.0\.1:(\d+)", endpoint)
    if not m:
        check("app_server", False, f"no bound endpoint in state ({endpoint!r})")
    else:
        port = int(m.group(1))
        probe = tcp_probe or _tcp_connect_ok
        ok = probe(port)
        check("app_server", ok, f"{endpoint} tcp-connect={'OK' if ok else 'REFUSED'}")

    # 3-5. exactly-one components, pids matching the state where recorded
    hb = matching(procs, "codex-agent-heartbeat.py", serial)
    check("heartbeat", len(hb) == 1, f"pids={hb} (need exactly 1)")
    br = matching(procs, "codex-inbox-turn-bridge.py", serial)
    br_ok = len(br) == 1 and (state or {}).get("bridge_pid") in br
    check("bridge", br_ok,
          f"pids={br} state.bridge_pid={(state or {}).get('bridge_pid')}")
    det = matching(procs, "codex-inbox-monitor.py", serial)
    det_ok = len(det) == 1 and (state or {}).get("detector_pid") in det
    check("detector", det_ok,
          f"pids={det} state.detector_pid={(state or {}).get('detector_pid')}")

    # 6. thread bound
    thread_id = str((state or {}).get("thread_id") or "")
    check("thread_bound", bool(thread_id), f"thread_id={thread_id or 'ABSENT'}")

    # 7. liveness fresh AND owned by the observed heartbeat
    entry = liveness.get(serial) or {}
    age = now_epoch - float(entry.get("last_seen_epoch") or 0)
    fresh = bool(entry) and age < 120
    owner_ok = fresh and len(hb) == 1 and entry.get("pid") == hb[0]
    check(
        "liveness",
        owner_ok,
        f"age={int(age) if entry else 'ABSENT'}s pid={entry.get('pid')} "
        f"heartbeat_pid={hb[0] if len(hb) == 1 else hb}",
    )

    # 8. no consuming watcher may hold this serial
    watchers = matching(procs, "inbox-watch.sh", serial)
    check("no_consuming_watcher", len(watchers) == 0, f"pids={watchers}")

    # 9. unread inbox (informational)
    base, _, lane = serial.partition("~")
    inbox = workspace_root() / "org" / "mcp" / "inbox" / base
    if lane:
        inbox = inbox / f"~{lane}"
    try:
        unread = sorted(
            e.name for e in inbox.iterdir()
            if e.is_file() and e.suffix.lower() == ".md"
        )
    except FileNotFoundError:
        unread = []
    checks["unread_inbox"] = {
        "ok": True,
        "detail": f"count={len(unread)}",
        "informational": True,
    }

    green = all(c["ok"] for c in checks.values())
    return {"serial": serial, "green": green, "checks": checks}


def _tcp_connect_ok(port: int) -> bool:
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=2):
            return True
    except OSError:
        return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--serial", required=True)
    parser.add_argument("--runtime-dir", type=Path, default=None)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    runtime_dir = args.runtime_dir or default_runtime_dir(args.serial)

    liveness_path = workspace_root() / "org" / "mcp" / "liveness.json"
    try:
        liveness = json.loads(liveness_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        liveness = {}

    try:
        procs = enumerate_processes()
    except Exception as exc:  # enumeration failure is an ERROR, never a clean red
        print(f"codex-seat-status: ERROR ({exc})", file=sys.stderr)
        return 3

    report = probe_seat(args.serial, runtime_dir, procs, liveness, time.time())
    if args.as_json:
        print(json.dumps(report, indent=2))
    else:
        verdict = "GREEN" if report["green"] else "RED"
        print(f"codex-seat-status {args.serial}: {verdict}")
        for name, c in report["checks"].items():
            mark = "OK " if c["ok"] else "FAIL"
            print(f"  [{mark}] {name:<22} {c['detail']}")
    return 0 if report["green"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
