#!/usr/bin/env python3
"""Bridge non-consuming inbox nudges into a live Codex app-server thread.

The bridge deliberately delegates filesystem detection to
``codex-inbox-monitor.py``.  It never reads, moves, deletes, or acknowledges an
inbox message.  Its only mutation is submitting a user input to the Codex
thread hosted by the configured app-server endpoint.

Delivery policy:

* idle thread: ``turn/start`` directly instantiates a new turn;
* active thread: ``turn/steer`` against the exact in-progress turn;
* unloaded thread: resume it, then start or queue one input;
* a race between status inspection and submission is retried once;
* one dispatch exists per ``(serial, filename)`` while the exact unread file
  exists; queue duplicates are collapsed and deleted when the file is handled.

This process must connect to the *same* app-server as the interactive TUI.
Starting a second embedded app-server cannot wake an already-idle Windows TUI.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
import time
import uuid
from pathlib import Path
from typing import Any

import websockets


HARD_NUDGE_RE = re.compile(r"^\[HARD-NUDGE\] ([^\\/]+\.md)$", re.IGNORECASE)
RETRYABLE_RPC_CODES = {-32001}


class RpcError(RuntimeError):
    def __init__(self, method: str, error: Any) -> None:
        super().__init__(f"{method} failed: {error}")
        self.method = method
        self.error = error

    @property
    def code(self) -> int | None:
        if isinstance(self.error, dict) and isinstance(self.error.get("code"), int):
            return self.error["code"]
        return None


class AppServerClient:
    def __init__(self, endpoint: str, auth_token: str | None = None) -> None:
        self.endpoint = endpoint
        self.auth_token = auth_token
        self._socket: Any = None
        self._reader: asyncio.Task[None] | None = None
        self._pending: dict[int, asyncio.Future[Any]] = {}
        self._next_id = 1

    async def __aenter__(self) -> "AppServerClient":
        headers = None
        if self.auth_token:
            headers = {"Authorization": f"Bearer {self.auth_token}"}
        self._socket = await websockets.connect(
            self.endpoint,
            additional_headers=headers,
            max_size=16 * 1024 * 1024,
        )
        self._reader = asyncio.create_task(self._read_loop())
        await self.request(
            "initialize",
            {
                "clientInfo": {
                    "name": "ajb-codex-inbox-turn-bridge",
                    "title": "AJB Codex inbox turn bridge",
                    "version": "1.0.0",
                },
                "capabilities": {"experimentalApi": True},
            },
        )
        return self

    async def __aexit__(self, *_: object) -> None:
        if self._socket is not None:
            await self._socket.close()
        if self._reader is not None:
            await asyncio.gather(self._reader, return_exceptions=True)

    async def _read_loop(self) -> None:
        assert self._socket is not None
        try:
            async for raw in self._socket:
                message = json.loads(raw)
                request_id = message.get("id")
                if request_id is None or request_id not in self._pending:
                    # Notifications are intentionally ignored.  The TUI remains
                    # the presentation client for the shared thread.
                    continue
                future = self._pending.pop(request_id)
                if "error" in message:
                    future.set_exception(RpcError("request", message["error"]))
                else:
                    future.set_result(message.get("result"))
        except BaseException as exc:
            for future in self._pending.values():
                if not future.done():
                    future.set_exception(exc)
            self._pending.clear()
            if not isinstance(exc, asyncio.CancelledError):
                raise

    async def request(
        self,
        method: str,
        params: dict[str, Any],
        *,
        attempts: int = 4,
    ) -> Any:
        assert self._socket is not None
        delay = 0.1
        for attempt in range(attempts):
            request_id = self._next_id
            self._next_id += 1
            future = asyncio.get_running_loop().create_future()
            self._pending[request_id] = future
            await self._socket.send(
                json.dumps({"id": request_id, "method": method, "params": params})
            )
            try:
                return await future
            except RpcError as exc:
                exc.method = method
                if exc.code not in RETRYABLE_RPC_CODES or attempt + 1 >= attempts:
                    raise RpcError(method, exc.error) from exc
                await asyncio.sleep(delay)
                delay *= 2
        raise AssertionError("unreachable")


def default_runtime_dir(serial: str) -> Path:
    """Mirror start-codex-seat.ps1's runtime-dir derivation EXACTLY."""
    import re as _re
    sanitized = _re.sub(r"[^A-Za-z0-9_.~-]", "_", serial)
    return workspace_root() / ".runtime" / "codex-seats" / sanitized


def write_bridge_state(
    runtime_dir: Path,
    serial: str,
    thread_id: str,
    endpoint: str,
    detector_pid: int | None,
) -> None:
    """The machine-readable binding record. The heartbeat DERIVES its summary
    from this file plus live PID probes -- a summary is a measurement here,
    never an argparse default. Written atomically (tmp + replace)."""
    import json as _json
    runtime_dir.mkdir(parents=True, exist_ok=True)
    state = {
        "serial": serial,
        "thread_id": thread_id,
        "endpoint": endpoint,
        "bridge_pid": os.getpid(),
        "detector_pid": detector_pid,
        "bound_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    tmp = runtime_dir / "bridge-state.json.tmp"
    tmp.write_text(_json.dumps(state, indent=2), encoding="utf-8")
    tmp.replace(runtime_dir / "bridge-state.json")


def workspace_root() -> Path:
    return Path(__file__).resolve().parents[2]


def nudge_text(serial: str, filename: str) -> str:
    return (
        f"[HARD-NUDGE] {filename}\n"
        f"Inbox event for {serial}. Read only the exact unread root-level file named "
        f"{filename}. A message from CRO Base is an immediate Go unless its body "
        "explicitly says hold: ACK by naming message content, begin the order "
        "immediately, perform the first required action, and only after acting move "
        "that exact file into read/. If the exact file is already absent, treat this "
        "as a stale duplicate and do not substitute another filename."
    )


def nudge_message_id(serial: str, filename: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"ajb-inbox:{serial}:{filename}"))


def unread_path_for(serial: str, filename: str) -> Path:
    if HARD_NUDGE_RE.fullmatch(f"[HARD-NUDGE] {filename}") is None:
        raise ValueError(f"invalid inbox filename: {filename!r}")
    base, separator, lane = serial.partition("~")
    if not base or (separator and not lane) or "~" in lane:
        raise ValueError(f"invalid agent serial: {serial!r}")
    inbox = workspace_root() / "org" / "mcp" / "inbox" / base
    if lane:
        inbox /= f"~{lane}"
    return inbox / filename


def in_progress_turn_id(thread: dict[str, Any]) -> str | None:
    for turn in reversed(thread.get("turns") or []):
        if turn.get("status") == "inProgress" and isinstance(turn.get("id"), str):
            return turn["id"]
    return None


async def read_thread(client: AppServerClient, thread_id: str) -> dict[str, Any]:
    response = await client.request(
        "thread/read", {"threadId": thread_id, "includeTurns": True}
    )
    return response["thread"]


async def queue_nudge(
    client: AppServerClient,
    thread_id: str,
    text: str,
    client_message_id: str,
) -> dict[str, Any]:
    response = await client.request(
        "thread/queue/add",
        {
            "threadId": thread_id,
            "input": [{"type": "text", "text": text, "text_elements": []}],
            "clientUserMessageId": client_message_id,
        },
    )
    return response["queuedSubmission"]


async def list_queued_submissions(
    client: AppServerClient,
    thread_id: str,
) -> list[dict[str, Any]]:
    submissions: list[dict[str, Any]] = []
    cursor: str | None = None
    seen_cursors: set[str] = set()
    while True:
        params: dict[str, Any] = {"threadId": thread_id, "limit": 100}
        if cursor is not None:
            params["cursor"] = cursor
        response = await client.request("thread/queue/list", params)
        submissions.extend(response.get("data") or [])
        cursor = response.get("nextCursor")
        if not cursor or cursor in seen_cursors:
            return submissions
        seen_cursors.add(cursor)


async def delete_queued_submission(
    client: AppServerClient,
    thread_id: str,
    queued_submission_id: str,
) -> bool:
    response = await client.request(
        "thread/queue/delete",
        {
            "threadId": thread_id,
            "queuedSubmissionId": queued_submission_id,
        },
    )
    return bool(response.get("deleted"))


async def cancel_queued_nudges(
    client: AppServerClient,
    thread_id: str,
    serial: str,
    filename: str,
) -> int:
    message_id = nudge_message_id(serial, filename)
    queued = await list_queued_submissions(client, thread_id)
    matching = [
        submission
        for submission in queued
        if submission.get("clientUserMessageId") == message_id
        and isinstance(submission.get("id"), str)
    ]
    deleted = 0
    for submission in matching:
        if await delete_queued_submission(client, thread_id, submission["id"]):
            deleted += 1
    return deleted


async def queue_nudge_once(
    client: AppServerClient,
    thread_id: str,
    serial: str,
    filename: str,
    text: str,
    unread_path: Path,
) -> str:
    message_id = nudge_message_id(serial, filename)
    queued = await list_queued_submissions(client, thread_id)
    matching = [
        submission
        for submission in queued
        if submission.get("clientUserMessageId") == message_id
        and isinstance(submission.get("id"), str)
    ]
    if matching:
        # Preserve one durable wake and collapse any duplicates left by an
        # older bridge before this process came online.
        for duplicate in matching[1:]:
            await delete_queued_submission(client, thread_id, duplicate["id"])
        return "turn/queue-existing"
    if not unread_path.is_file():
        return "stale-file-absent"
    await queue_nudge(client, thread_id, text, message_id)
    return "turn/queue-added"


def queued_nudge_filename(
    submission: dict[str, Any], serial: str
) -> str | None:
    for item in submission.get("input") or []:
        if not isinstance(item, dict) or item.get("type") != "text":
            continue
        text = item.get("text")
        if not isinstance(text, str):
            continue
        first_line = text.splitlines()[0] if text else ""
        match = HARD_NUDGE_RE.fullmatch(first_line)
        if match is None:
            continue
        filename = match.group(1)
        if submission.get("clientUserMessageId") == nudge_message_id(
            serial, filename
        ):
            return filename
    return None


async def reconcile_queued_nudges(
    client: AppServerClient,
    thread_id: str,
    serial: str,
) -> tuple[set[str], int]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for submission in await list_queued_submissions(client, thread_id):
        filename = queued_nudge_filename(submission, serial)
        if filename is not None and isinstance(submission.get("id"), str):
            grouped.setdefault(filename, []).append(submission)

    delivered: set[str] = set()
    deleted = 0
    for filename, submissions in grouped.items():
        unread_path = unread_path_for(serial, filename)
        keep = 1 if unread_path.is_file() else 0
        for submission in submissions[keep:]:
            if await delete_queued_submission(client, thread_id, submission["id"]):
                deleted += 1
        if keep:
            delivered.add(filename)
    return delivered, deleted


async def start_nudge(
    client: AppServerClient,
    thread_id: str,
    text: str,
    client_message_id: str,
) -> None:
    await client.request(
        "turn/start",
        {
            "threadId": thread_id,
            "input": [{"type": "text", "text": text, "text_elements": []}],
            "clientUserMessageId": client_message_id,
        },
        attempts=1,
    )


async def deliver_nudge(
    client: AppServerClient,
    thread_id: str,
    serial: str,
    filename: str,
    unread_path: Path | None = None,
) -> str:
    text = nudge_text(serial, filename)
    message_id = nudge_message_id(serial, filename)
    unread_path = unread_path or unread_path_for(serial, filename)

    async def still_unread() -> bool:
        if unread_path.is_file():
            return True
        await cancel_queued_nudges(client, thread_id, serial, filename)
        return False

    for race_attempt in range(2):
        if not await still_unread():
            return "stale-file-absent"
        thread = await read_thread(client, thread_id)
        status = (thread.get("status") or {}).get("type")

        if status == "notLoaded":
            await client.request("thread/resume", {"threadId": thread_id})
            if not await still_unread():
                return "stale-file-absent"
            try:
                await start_nudge(client, thread_id, text, message_id)
                return "turn/start-after-resume"
            except RpcError:
                # Resume/start can race with another client. The same-host
                # queue preserves the filename for the next idle boundary.
                return await queue_nudge_once(
                    client, thread_id, serial, filename, text, unread_path
                )

        if status == "active":
            active_turn_id = in_progress_turn_id(thread)
            if active_turn_id is None:
                await asyncio.sleep(0.1)
                continue
            if not await still_unread():
                return "stale-file-absent"
            try:
                await client.request(
                    "turn/steer",
                    {
                        "threadId": thread_id,
                        "expectedTurnId": active_turn_id,
                        "input": [
                            {"type": "text", "text": text, "text_elements": []}
                        ],
                        "clientUserMessageId": message_id,
                    },
                    attempts=1,
                )
                return "turn/steer"
            except RpcError:
                if race_attempt == 0:
                    await asyncio.sleep(0.1)
                    continue
                # A non-steerable active turn (review/compact) will be retried
                # by the detector after the active boundary. Do not enqueue a
                # turn for every detector repeat.
                return "defer-active-nonsteerable"

        if status == "idle":
            if not await still_unread():
                return "stale-file-absent"
            try:
                # This is the explicit dormant-wake primitive: it creates a
                # model turn even though no prior turn is active.
                await start_nudge(client, thread_id, text, message_id)
                return "turn/start"
            except RpcError:
                # A status race may make direct start temporarily invalid.
                return await queue_nudge_once(
                    client, thread_id, serial, filename, text, unread_path
                )

        if status == "systemError":
            raise RuntimeError(f"thread {thread_id} is in systemError state")

        await asyncio.sleep(0.1)

    return await queue_nudge_once(
        client, thread_id, serial, filename, text, unread_path
    )


async def cancel_handled_nudges(
    client: AppServerClient,
    thread_id: str,
    serial: str,
    delivered: set[str],
    poll_seconds: float,
) -> None:
    while True:
        await asyncio.sleep(poll_seconds)
        for filename in tuple(delivered):
            if unread_path_for(serial, filename).is_file():
                continue
            try:
                deleted = await cancel_queued_nudges(
                    client, thread_id, serial, filename
                )
                delivered.discard(filename)
                print(
                    f"[TURN-BRIDGE-CANCELLED] {filename} queued={deleted}",
                    flush=True,
                )
            except Exception as exc:
                print(
                    f"[TURN-BRIDGE-CANCEL-RETRY] {filename}: {exc}",
                    file=sys.stderr,
                    flush=True,
                )


async def discover_thread(
    client: AppServerClient,
    cwd: Path,
    timeout_seconds: float,
) -> str:
    """Poll thread/list until exactly one loaded CLI thread exists for cwd.

    timeout_seconds == 0 means SUPERVISED-INDEFINITE: keep polling forever,
    emitting a [TURN-BRIDGE-WAITING] line every ~15s so the log proves
    liveness. This is the FRESH-LAUNCH default: a brand-new TUI thread does
    not appear in the state DB until the operator's first persisted turn, so
    any finite deadline here is a race against a human -- the measured
    2026-08-26 failure mode (CRO base + ~B: bridge exited on this timeout,
    the detector -- a CHILD of this process -- never existed, and the
    heartbeat's hardcoded summary reported the seat green anyway).
    A finite value keeps its fail-loud meaning (tests, preflight callers).
    """
    loop = asyncio.get_running_loop()
    deadline = (loop.time() + timeout_seconds) if timeout_seconds > 0 else None
    started = loop.time()
    last_wait_line = started
    wanted_cwd = str(cwd.resolve()).casefold()
    while deadline is None or loop.time() < deadline:
        response = await client.request(
            "thread/list",
            {
                "limit": 50,
                "sortKey": "updated_at",
                # A TUI attached with ``codex --remote`` is reported by the
                # shared app-server as ``vscode`` even though the foreground
                # client is the Codex CLI.  Accept both representations while
                # the cwd/status/parent filters below select the seat thread.
                "sourceKinds": ["cli", "vscode"],
                "archived": False,
                "cwd": str(cwd.resolve()),
                "useStateDbOnly": True,
            },
        )
        loaded = [
            thread
            for thread in response.get("data", [])
            if str(thread.get("cwd", "")).casefold() == wanted_cwd
            and (thread.get("status") or {}).get("type") in {"idle", "active"}
            and thread.get("parentThreadId") is None
        ]
        if len(loaded) == 1:
            return loaded[0]["id"]
        if len(loaded) > 1:
            ids = ", ".join(thread["id"] for thread in loaded)
            raise RuntimeError(
                f"multiple loaded CLI threads match {cwd}: {ids}; pass --thread-id"
            )
        now = loop.time()
        if deadline is None and now - last_wait_line >= 15.0:
            print(
                f"[TURN-BRIDGE-WAITING] no loaded CLI thread yet for {cwd} "
                f"(t={int(now - started)}s; supervised discovery continues)",
                flush=True,
            )
            last_wait_line = now
        await asyncio.sleep(0.25)
    raise TimeoutError(f"no loaded CLI thread appeared for {cwd} within timeout")


async def detector_lines(
    serial: str,
    poll_seconds: float,
    repeat_seconds: float,
    on_spawn=None,
):
    detector = workspace_root() / "org" / "mcp" / "codex-inbox-monitor.py"
    process = await asyncio.create_subprocess_exec(
        sys.executable,
        "-u",
        str(detector),
        "--serial",
        serial,
        "--poll-seconds",
        str(poll_seconds),
        "--repeat-seconds",
        str(repeat_seconds),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    assert process.stdout is not None
    assert process.stderr is not None
    if on_spawn is not None:
        on_spawn(process.pid)

    async def copy_stderr() -> None:
        async for raw in process.stderr:
            print(raw.decode(errors="replace").rstrip(), file=sys.stderr, flush=True)

    stderr_task = asyncio.create_task(copy_stderr())
    try:
        async for raw in process.stdout:
            yield raw.decode(errors="replace").rstrip("\r\n")
    finally:
        if process.returncode is None:
            process.terminate()
        await process.wait()
        await stderr_task


async def run(args: argparse.Namespace) -> int:
    auth_token = None
    if args.auth_token_env:
        auth_token = os.environ.get(args.auth_token_env)
        if not auth_token:
            raise RuntimeError(f"{args.auth_token_env} is not set")

    async with AppServerClient(args.endpoint, auth_token) as client:
        if args.preflight_only:
            if args.thread_id is None:
                raise RuntimeError("--preflight-only requires --thread-id")
            await client.request("thread/resume", {"threadId": args.thread_id})
            print(
                f"[THREAD-PREFLIGHT-READY] thread={args.thread_id} "
                f"endpoint={args.endpoint}",
                flush=True,
            )
            return 0

        thread_id = args.thread_id
        if thread_id is None:
            thread_id = await discover_thread(client, args.cwd, args.discovery_timeout)
        print(
            f"[TURN-BRIDGE-READY] serial={args.serial} thread={thread_id} "
            f"endpoint={args.endpoint}",
            flush=True,
        )
        runtime_dir = args.runtime_dir or default_runtime_dir(args.serial)
        write_bridge_state(
            runtime_dir, args.serial, thread_id, args.endpoint, None
        )

        delivered, deleted = await reconcile_queued_nudges(
            client, thread_id, args.serial
        )
        if deleted:
            print(
                f"[TURN-BRIDGE-QUEUE-RECONCILED] deleted={deleted}",
                flush=True,
            )
        cancellation_task = asyncio.create_task(
            cancel_handled_nudges(
                client,
                thread_id,
                args.serial,
                delivered,
                args.poll_seconds,
            )
        )
        try:
            async for line in detector_lines(
                args.serial,
                args.poll_seconds,
                args.repeat_seconds,
                on_spawn=lambda pid: write_bridge_state(
                    runtime_dir, args.serial, thread_id, args.endpoint, pid
                ),
            ):
                match = HARD_NUDGE_RE.fullmatch(line)
                if match is None:
                    continue
                filename = match.group(1)
                unread_path = unread_path_for(args.serial, filename)
                try:
                    if filename in delivered and unread_path.is_file():
                        print(f"{line} [deduplicated]", flush=True)
                        continue
                    if not unread_path.is_file():
                        deleted = await cancel_queued_nudges(
                            client, thread_id, args.serial, filename
                        )
                        delivered.discard(filename)
                        print(
                            f"{line} [stale-file-absent; cancelled={deleted}]",
                            flush=True,
                        )
                        continue
                    action = await deliver_nudge(
                        client,
                        thread_id,
                        args.serial,
                        filename,
                        unread_path,
                    )
                    if not action.startswith(("defer-", "stale-")):
                        delivered.add(filename)
                    print(f"{line} [{action}]", flush=True)
                except Exception as exc:
                    # The detector repeats while the unread file exists. A
                    # failed/deferred dispatch remains visible without adding
                    # duplicate queued submissions.
                    print(
                        f"[TURN-BRIDGE-RETRY] {filename}: {exc}",
                        file=sys.stderr,
                        flush=True,
                    )
        finally:
            cancellation_task.cancel()
            await asyncio.gather(cancellation_task, return_exceptions=True)
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Start/steer a shared Codex thread for non-consuming inbox nudges."
    )
    parser.add_argument("--serial", required=True)
    parser.add_argument("--endpoint", required=True, help="Shared ws:// app-server URL")
    parser.add_argument("--thread-id")
    parser.add_argument("--cwd", type=Path, default=workspace_root())
    parser.add_argument("--auth-token-env")
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help="Resume the supplied thread on this host, report readiness, and exit.",
    )
    parser.add_argument("--poll-seconds", type=float, default=0.5)
    parser.add_argument("--repeat-seconds", type=float, default=15.0)
    parser.add_argument(
        "--discovery-timeout",
        type=float,
        default=0.0,
        help="0 (default) = supervised-indefinite discovery: poll forever and "
             "log [TURN-BRIDGE-WAITING]; a positive value fails loud on expiry. "
             "The old 120s default silently killed the bridge AND its detector "
             "child on every fresh launch slower than the deadline.",
    )
    parser.add_argument(
        "--runtime-dir",
        type=Path,
        default=None,
        help="Seat runtime dir for bridge-state.json (default: derived from serial)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    try:
        return asyncio.run(run(parse_args(sys.argv[1:] if argv is None else argv)))
    except KeyboardInterrupt:
        return 130
    except Exception as exc:
        print(f"codex-inbox-turn-bridge: {exc}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
