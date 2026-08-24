#!/usr/bin/env python3
"""Persistent Codex registration and heartbeat companion.

This process intentionally does not monitor or consume the filesystem inbox.
It reuses the broker server's guarded registration/liveness implementation and
cancels its broker message poller; delivery belongs to codex-inbox-monitor.py.
"""

from __future__ import annotations

import argparse
import asyncio
import sys

import server as comms


async def run(serial: str, summary: str, interval_seconds: float) -> int:
    result = await comms.register_agent(serial, summary=summary)
    print(result, flush=True)
    if f"Registered {serial} as live" not in result:
        return 2

    # register_agent starts the Claude-oriented broker polling task. A Codex
    # session uses the non-consuming filesystem detector instead, so keep the
    # registration/heartbeat half and explicitly stop the consuming half.
    poll_task = comms._poll_task
    if poll_task is not None:
        poll_task.cancel()
        await asyncio.gather(poll_task, return_exceptions=True)
        comms._poll_task = None

    while True:
        await asyncio.sleep(interval_seconds)
        result = await comms.heartbeat(serial, summary=summary)
        if "Heartbeat OK" not in result:
            print(result, file=sys.stderr, flush=True)
            return 3


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Register a Codex lane and keep broker heartbeats active."
    )
    parser.add_argument("--serial", required=True)
    parser.add_argument(
        "--summary", default="WORKING: Codex non-consuming inbox monitor active"
    )
    parser.add_argument("--interval-seconds", type=float, default=30.0)
    args = parser.parse_args(argv)
    if args.interval_seconds <= 0 or args.interval_seconds >= comms.STALE_THRESHOLD:
        parser.error(
            f"--interval-seconds must be greater than zero and below {comms.STALE_THRESHOLD}"
        )
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        return asyncio.run(run(args.serial, args.summary, args.interval_seconds))
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
