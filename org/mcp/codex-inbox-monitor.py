#!/usr/bin/env python3
"""Non-consuming inbox detector for Codex sessions.

The process observes root-level Markdown filenames and emits exactly one line
per nudge. An unread filename is re-emitted periodically until another actor
handles it. The detector deliberately has no message-reading, acknowledgement,
move, or delete operation.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path


PREFIX = "[HARD-NUDGE] "


def workspace_root() -> Path:
    return Path(__file__).resolve().parents[2]


def inbox_for_serial(serial: str) -> Path:
    if not serial or "/" in serial or "\\" in serial:
        raise ValueError("serial must be a non-empty agent serial, not a path")
    if serial.count("~") > 1:
        raise ValueError("serial may contain at most one lane suffix")

    base, separator, lane = serial.partition("~")
    if not base or (separator and not lane):
        raise ValueError("invalid serial")

    inbox = workspace_root() / "org" / "mcp" / "inbox" / base
    if lane:
        inbox = inbox / f"~{lane}"
    return inbox


def root_markdown_names(inbox: Path) -> set[str]:
    try:
        return {
            entry.name
            for entry in inbox.iterdir()
            if entry.is_file() and entry.suffix.lower() == ".md"
        }
    except FileNotFoundError:
        return set()


def monitor(
    inbox: Path,
    poll_seconds: float,
    repeat_seconds: float,
    max_events: int | None,
) -> int:
    if poll_seconds <= 0:
        raise ValueError("poll interval must be greater than zero")
    if repeat_seconds <= 0:
        raise ValueError("repeat interval must be greater than zero")

    # No persisted detector state is intentional: files already unread at
    # startup emit on the first scan, so a restart cannot hide backlog.
    last_emitted: dict[str, float] = {}
    emitted = 0

    while True:
        current = root_markdown_names(inbox)
        now = time.monotonic()
        for name in sorted(current):
            previous = last_emitted.get(name)
            if previous is not None and now - previous < repeat_seconds:
                continue
            print(f"{PREFIX}{name}", flush=True)
            last_emitted[name] = now
            emitted += 1
            if max_events is not None and emitted >= max_events:
                return 0

        # Forget only absent names. If an exact filename is delivered again
        # after handling, it emits immediately rather than inheriting a timer.
        last_emitted = {
            name: timestamp
            for name, timestamp in last_emitted.items()
            if name in current
        }
        time.sleep(poll_seconds)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Emit non-consuming Codex hard nudges for unread inbox files."
    )
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--serial", help="Full agent serial, including any ~lane suffix")
    target.add_argument("--inbox", type=Path, help="Explicit inbox path (tests/debugging)")
    parser.add_argument("--poll-seconds", type=float, default=0.5)
    parser.add_argument(
        "--repeat-seconds",
        type=float,
        default=15.0,
        help="Re-emit a nudge while a file remains unread (default: 15 seconds)",
    )
    parser.add_argument(
        "--max-events",
        type=int,
        default=None,
        help="Exit after N emitted events (acceptance tests only)",
    )
    args = parser.parse_args(argv)
    if args.max_events is not None and args.max_events < 1:
        parser.error("--max-events must be at least 1")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        inbox = args.inbox.resolve() if args.inbox else inbox_for_serial(args.serial)
        return monitor(
            inbox,
            args.poll_seconds,
            args.repeat_seconds,
            args.max_events,
        )
    except (OSError, ValueError) as exc:
        print(f"codex-inbox-monitor: {exc}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
