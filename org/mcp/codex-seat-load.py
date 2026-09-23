#!/usr/bin/env python3
"""Derive one Codex seat's canonical, repository-local startup context."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


SERIAL_PATTERN = re.compile(
    r"^(?P<version>[0-9]+\.[0-9]+\.[0-9]+)_"
    r"(?P<role>[A-Za-z]+)_(?P<name>[A-Za-z0-9]+)"
    r"(?:~(?P<lane>[A-Za-z0-9]+))?$"
)
REQUIRED_CONTRACTS = (
    "AGENTS.md",
    "org/XXX.md",
    "org/mcp/CODEX_INBOX_MONITOR.md",
)
ROLE_FILES_MANIFEST = "org/mcp/codex-seat-role-files.json"


class SeatLoadError(ValueError):
    """A deterministic seat context cannot be produced."""


def parse_serial(serial: str) -> tuple[str, str | None]:
    match = SERIAL_PATTERN.fullmatch(serial)
    if not match:
        raise SeatLoadError(
            f"invalid full serial {serial!r}; expected N.N.N_ROLE_Name[~Lane]"
        )
    lane = match.group("lane")
    base = serial.split("~", 1)[0]
    return base, lane


def _agent_homes(workspace: Path, serial: str) -> list[Path]:
    org = workspace / "org"
    if not org.is_dir():
        raise SeatLoadError(f"missing org directory: {org}")
    homes: list[Path] = []
    for tier in sorted(org.iterdir(), key=lambda item: item.name):
        if not tier.is_dir() or not tier.name.startswith("tier"):
            continue
        candidate = tier / serial
        if candidate.is_dir():
            homes.append(candidate)
    return homes


def _one_home(workspace: Path, serial: str, label: str) -> Path:
    homes = _agent_homes(workspace, serial)
    if not homes:
        raise SeatLoadError(f"no {label} home found for {serial}")
    if len(homes) != 1:
        rendered = ", ".join(str(path) for path in homes)
        raise SeatLoadError(f"ambiguous {label} home for {serial}: {rendered}")
    return homes[0]


def _relative(workspace: Path, path: Path) -> str:
    return path.relative_to(workspace).as_posix()


def _role_files(workspace: Path, role_home: Path, serial: str) -> tuple[list[str], str]:
    """Use a checked-in exact-seat reading list when declared; preserve other seats."""
    manifest = workspace / ROLE_FILES_MANIFEST
    if manifest.is_file():
        try:
            document = json.loads(manifest.read_text(encoding="utf-8-sig"))
        except (ValueError, OSError) as exc:
            raise SeatLoadError(f"invalid role-files manifest {manifest}: {exc}") from exc
        if (not isinstance(document, dict) or document.get("version") != 1
                or not isinstance(document.get("seats"), dict)):
            raise SeatLoadError(f"invalid role-files manifest structure: {manifest}")
        seats = document["seats"]
        if serial in seats:
            entries = seats[serial]
            if (not isinstance(entries, list) or not entries
                    or any(not isinstance(item, str) or not item for item in entries)):
                raise SeatLoadError(f"invalid role_files list for {serial}")
            resolved = []
            for item in entries:
                path = (workspace / item).resolve()
                if Path(item).is_absolute() or not path.is_relative_to(workspace):
                    raise SeatLoadError(f"role file must be workspace-relative: {item}")
                if not path.is_file():
                    raise SeatLoadError(f"missing declared role file for {serial}: {item}")
                resolved.append(_relative(workspace, path))
            required = {_relative(workspace, role_home / name)
                        for name in ("README.md", "prompt.md")}
            if not required.issubset(resolved) or len(resolved) != len(set(resolved)):
                raise SeatLoadError(
                    f"role_files for {serial} must include base README.md/prompt.md once "
                    "and contain no duplicate paths"
                )
            return resolved, ROLE_FILES_MANIFEST
    return ([
        _relative(workspace, item)
        for item in sorted(role_home.iterdir(), key=lambda entry: entry.name)
        if item.is_file() and not item.name.startswith(".")
    ], "base-role-root")


def build_context(workspace: Path, serial: str) -> dict[str, object]:
    workspace = workspace.resolve()
    base, lane = parse_serial(serial)

    missing = [item for item in REQUIRED_CONTRACTS if not (workspace / item).is_file()]
    if missing:
        raise SeatLoadError("missing required contract(s): " + ", ".join(missing))

    role_home = _one_home(workspace, base, "base role")
    # A tilde suffix is an additive runtime/registration identity used to
    # parallelize one agent role. It does not mint a second repository home.
    # Suffixed seats therefore share the base role's logs, task orders, and
    # deliverables while retaining their exact serial everywhere runtime
    # identity matters (registration, inbox routing, status, and runtime dir).
    seat_home = role_home
    inbox = workspace / "org" / "mcp" / "inbox" / base
    if lane:
        inbox = inbox / f"~{lane}"

    role_files, role_files_source = _role_files(workspace, role_home, serial)
    runtime_serial = re.sub(r"[^A-Za-z0-9_.~-]", "_", serial)

    return {
        "document_kind": "codex_seat_load_context",
        "serial": serial,
        "base_serial": base,
        "lane": lane,
        "workspace": str(workspace),
        "contracts": list(REQUIRED_CONTRACTS),
        "role_home": _relative(workspace, role_home),
        "seat_home": _relative(workspace, seat_home),
        "role_files": role_files,
        "role_files_source": role_files_source,
        "task_orders": _relative(workspace, seat_home / "task_orders"),
        "logs": _relative(workspace, seat_home / "logs"),
        "deliverables": _relative(workspace, seat_home / "deliverables"),
        "inbox": _relative(workspace, inbox),
        "read_inbox": _relative(workspace, inbox / "read"),
        "runtime": f".runtime/codex-seats/{runtime_serial}",
        "status_command": (
            "powershell -NoProfile -ExecutionPolicy Bypass -File "
            f"org/mcp/codex-seat-status.ps1 -Serial {serial}"
        ),
        "task_context_advisory_only": ".comp-graph/.agent_context",
        "launcher": "org/mcp/start-codex-seat.ps1",
        "handoff": "org/mcp/handoff-codex-seat.ps1",
        "monitor_ownership": {
            "launcher": ["codex-agent-heartbeat.py", "codex-inbox-turn-bridge.py"],
            "bridge": ["codex-inbox-monitor.py"],
        },
        "prohibited_runtime_helpers": [
            "inbox-watch.sh",
            "check-inbox.sh",
            "agent-poller.py",
            "duplicate codex-inbox-monitor.py",
            "model-side notify() bridge",
        ],
    }


def build_prompt(context: dict[str, object]) -> str:
    serial = context["serial"]
    return (
        f"Use $load to initialize the exact Codex seat {serial}. "
        "The full serial was supplied by the ajb2 launcher; do not infer or "
        "alter it, and do not ask the user to repeat it. Execute the skill's "
        "repository-local startup sequence before other work. The launcher "
        "provides bare `comp-*` commands to this Codex PowerShell seat via "
        "the repository's canonical command shims: run `comp-which "
        "\"your question\"` before searches and inspections, then run the "
        "routed compiler tool by its bare name."
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serial", required=True)
    parser.add_argument("--workspace", default=os.getcwd())
    parser.add_argument("--format", choices=("json", "prompt"), default="json")
    args = parser.parse_args(argv)

    try:
        context = build_context(Path(args.workspace), args.serial)
    except (OSError, SeatLoadError) as exc:
        print(f"codex-seat-load: {exc}", file=sys.stderr)
        return 2

    if args.format == "prompt":
        print(build_prompt(context))
    else:
        print(json.dumps(context, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
