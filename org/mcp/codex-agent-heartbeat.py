#!/usr/bin/env python3
"""Persistent Codex registration and heartbeat companion.

This process intentionally does not monitor or consume the filesystem inbox.
It reuses the broker server's guarded registration/liveness implementation and
cancels its broker message poller; delivery belongs to codex-inbox-monitor.py.

THE SUMMARY IS A MEASUREMENT, NEVER AN ASSERTION (repaired 2026-08-26).
The previous version carried a hardcoded argparse default --
"WORKING: Codex non-consuming inbox monitor active" -- that was broadcast
regardless of whether any monitor existed. Measured on the live box: three
seats (4.0.0_SA_CRO, ~A, ~B) all published that identical sentence while only
ONE had a bridge and detector; the other two were deaf with green liveness.
A value and a guess shared one type. Now every beat derives the summary from
bridge-state.json plus live PID probes, so a deaf seat REPORTS deaf
(DEGRADED) and false readiness is inexpressible from this process.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path

import server as comms


def heartbeat_needs_reregistration(serial: str, result: str) -> bool:
    return result.strip() == f"{serial} is not registered. Call register_agent first."


def default_runtime_dir(serial: str) -> Path:
    """Mirror start-codex-seat.ps1's runtime-dir derivation EXACTLY."""
    sanitized = re.sub(r"[^A-Za-z0-9_.~-]", "_", serial)
    return Path(__file__).resolve().parents[2] / ".runtime" / "codex-seats" / sanitized


def compute_summary(runtime_dir: Path, note: str = "") -> str:
    """Derive the seat summary from OBSERVED component state.

    Pure over (bridge-state.json contents, PID liveness probes) so the arms
    are unit-testable. Reuses the broker's own _pid_alive (ctypes OpenProcess
    on Windows -- probe only, never a signal).
    """
    state_path = runtime_dir / "bridge-state.json"
    suffix = f" | {note}" if note else ""
    if not state_path.is_file():
        return (
            "DEGRADED: bridge not bound (no bridge-state.json) -- seat NOT "
            "inbox-reachable; wake requires manual delivery" + suffix
        )
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return (
            "DEGRADED: bridge-state.json unreadable -- seat inbox-reachability "
            "UNKNOWN" + suffix
        )
    bridge_pid = state.get("bridge_pid")
    detector_pid = state.get("detector_pid")
    thread_id = str(state.get("thread_id") or "")
    missing = []
    if not (bridge_pid and comms._pid_alive(int(bridge_pid))):
        missing.append(f"bridge pid={bridge_pid} DEAD")
    if not (detector_pid and comms._pid_alive(int(detector_pid))):
        missing.append(f"detector pid={detector_pid} DEAD/absent")
    if not thread_id:
        missing.append("thread UNBOUND")
    if missing:
        return (
            "DEGRADED: " + "; ".join(missing) + " -- seat NOT inbox-reachable"
            + suffix
        )
    return (
        f"READY: codex seat bound thread={thread_id[:8]} bridge={bridge_pid} "
        f"detector={detector_pid} (measured each beat)" + suffix
    )


async def run(
    serial: str, note: str, interval_seconds: float, runtime_dir: Path
) -> int:
    async def register() -> bool:
        result = await comms.register_agent(
            serial, summary=compute_summary(runtime_dir, note)
        )
        print(result, flush=True)
        if f"Registered {serial} as live" not in result:
            return False

        # register_agent starts the Claude-oriented broker polling task. A
        # Codex session uses the non-consuming filesystem detector instead, so
        # keep the registration/heartbeat half and explicitly stop the
        # consuming half.
        poll_task = comms._poll_task
        if poll_task is not None:
            poll_task.cancel()
            await asyncio.gather(poll_task, return_exceptions=True)
            comms._poll_task = None
        return True

    if not await register():
        return 2

    while True:
        await asyncio.sleep(interval_seconds)
        result = await comms.heartbeat(
            serial, summary=compute_summary(runtime_dir, note)
        )
        if "Heartbeat OK" not in result:
            print(result, file=sys.stderr, flush=True)
            if heartbeat_needs_reregistration(serial, result):
                if await register():
                    continue
                return 2
            return 3


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Register a Codex lane and keep broker heartbeats active."
    )
    parser.add_argument("--serial", required=True)
    parser.add_argument(
        "--note",
        default="",
        help="Optional context APPENDED to the measured summary. The summary "
        "itself is always derived from bridge-state.json + PID probes; there "
        "is deliberately no way to assert readiness from the command line.",
    )
    parser.add_argument(
        "--runtime-dir",
        type=Path,
        default=None,
        help="Seat runtime dir holding bridge-state.json (default: derived)",
    )
    parser.add_argument("--interval-seconds", type=float, default=30.0)
    args = parser.parse_args(argv)
    if args.interval_seconds <= 0 or args.interval_seconds >= comms.STALE_THRESHOLD:
        parser.error(
            f"--interval-seconds must be greater than zero and below {comms.STALE_THRESHOLD}"
        )
    if args.runtime_dir is None:
        args.runtime_dir = default_runtime_dir(args.serial)
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        return asyncio.run(
            run(args.serial, args.note, args.interval_seconds, args.runtime_dir)
        )
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
