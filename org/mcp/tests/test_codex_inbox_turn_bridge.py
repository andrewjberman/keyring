from __future__ import annotations

import asyncio
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock


SCRIPT = Path(__file__).resolve().parents[1] / "codex-inbox-turn-bridge.py"
SPEC = importlib.util.spec_from_file_location("codex_inbox_turn_bridge", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)


class CodexInboxTurnBridgeTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def unread(self, filename: str) -> Path:
        path = Path(self.temp_dir.name) / filename
        path.write_text("pending", encoding="utf-8")
        return path

    async def test_discovery_accepts_remote_tui_vscode_source(self) -> None:
        client = AsyncMock()
        cwd = Path(self.temp_dir.name).resolve()
        client.request.return_value = {
            "data": [
                {
                    "id": "thread-vscode",
                    "cwd": str(cwd),
                    "source": "vscode",
                    "status": {"type": "active", "activeFlags": []},
                    "parentThreadId": None,
                }
            ]
        }

        thread_id = await bridge.discover_thread(client, cwd, 0.1)

        self.assertEqual(thread_id, "thread-vscode")
        method, params = client.request.await_args.args
        self.assertEqual(method, "thread/list")
        self.assertEqual(params["sourceKinds"], ["cli", "vscode"])

    async def test_idle_thread_calls_turn_start_directly(self) -> None:
        client = AsyncMock()
        client.request.side_effect = [
            {
                "thread": {
                    "status": {"type": "idle"},
                    "turns": [],
                }
            },
            {"turn": {"id": "turn-1", "status": "inProgress"}},
        ]

        action = await bridge.deliver_nudge(
            client,
            "thread-1",
            "4.0.0_SA_CRO~A",
            "message.md",
            self.unread("message.md"),
        )

        self.assertEqual(action, "turn/start")
        self.assertEqual(client.request.await_args_list[0].args[0], "thread/read")
        method, params = client.request.await_args_list[1].args
        self.assertEqual(method, "turn/start")
        self.assertEqual(params["threadId"], "thread-1")
        self.assertEqual(params["input"][0]["type"], "text")
        self.assertIn("[HARD-NUDGE] message.md", params["input"][0]["text"])

    async def test_active_thread_is_steered_immediately(self) -> None:
        client = AsyncMock()
        client.request.side_effect = [
            {
                "thread": {
                    "status": {"type": "active", "activeFlags": []},
                    "turns": [{"id": "turn-7", "status": "inProgress"}],
                }
            },
            {},
        ]

        action = await bridge.deliver_nudge(
            client,
            "thread-1",
            "4.0.0_SA_CRO~A",
            "go.md",
            self.unread("go.md"),
        )

        self.assertEqual(action, "turn/steer")
        method, params = client.request.await_args_list[1].args
        self.assertEqual(method, "turn/steer")
        self.assertEqual(params["expectedTurnId"], "turn-7")

    async def test_unloaded_thread_is_resumed_then_started(self) -> None:
        client = AsyncMock()
        client.request.side_effect = [
            {
                "thread": {
                    "status": {"type": "notLoaded"},
                    "turns": [],
                }
            },
            {"thread": {"id": "thread-1"}},
            {"turn": {"id": "turn-1", "status": "inProgress"}},
        ]

        action = await bridge.deliver_nudge(
            client,
            "thread-1",
            "4.0.0_SA_CRO~A",
            "resume.md",
            self.unread("resume.md"),
        )

        self.assertEqual(action, "turn/start-after-resume")
        self.assertEqual(
            [call.args[0] for call in client.request.await_args_list],
            ["thread/read", "thread/resume", "turn/start"],
        )

    async def test_idle_start_race_falls_back_to_same_host_queue(self) -> None:
        client = AsyncMock()
        client.request.side_effect = [
            {"thread": {"status": {"type": "idle"}, "turns": []}},
            bridge.RpcError("turn/start", {"code": -32000, "message": "race"}),
            {"data": [], "nextCursor": None},
            {"queuedSubmission": {"id": "queued-1"}},
        ]

        action = await bridge.deliver_nudge(
            client,
            "thread-1",
            "4.0.0_SA_CRO~A",
            "race.md",
            self.unread("race.md"),
        )

        self.assertEqual(action, "turn/queue-added")
        self.assertEqual(
            [call.args[0] for call in client.request.await_args_list],
            ["thread/read", "turn/start", "thread/queue/list", "thread/queue/add"],
        )

    async def test_absent_file_cancels_every_matching_queued_submission(self) -> None:
        client = AsyncMock()
        message_id = bridge.nudge_message_id("4.0.0_SA_CRO~A", "gone.md")
        client.request.side_effect = [
            {
                "data": [
                    {"id": "queued-1", "clientUserMessageId": message_id},
                    {"id": "queued-2", "clientUserMessageId": message_id},
                ],
                "nextCursor": None,
            },
            {"deleted": True},
            {"deleted": True},
        ]
        absent = Path(self.temp_dir.name) / "gone.md"

        action = await bridge.deliver_nudge(
            client,
            "thread-1",
            "4.0.0_SA_CRO~A",
            "gone.md",
            absent,
        )

        self.assertEqual(action, "stale-file-absent")
        self.assertEqual(
            [call.args[0] for call in client.request.await_args_list],
            ["thread/queue/list", "thread/queue/delete", "thread/queue/delete"],
        )

    async def test_nonsteerable_active_turn_is_deferred_without_queueing(self) -> None:
        client = AsyncMock()
        active = {
            "thread": {
                "status": {"type": "active"},
                "turns": [{"id": "turn-7", "status": "inProgress"}],
            }
        }
        client.request.side_effect = [
            active,
            bridge.RpcError("turn/steer", {"code": -32000}),
            active,
            bridge.RpcError("turn/steer", {"code": -32000}),
        ]

        action = await bridge.deliver_nudge(
            client,
            "thread-1",
            "4.0.0_SA_CRO~A",
            "defer.md",
            self.unread("defer.md"),
        )

        self.assertEqual(action, "defer-active-nonsteerable")
        self.assertNotIn(
            "thread/queue/add",
            [call.args[0] for call in client.request.await_args_list],
        )

    async def test_queue_nudge_once_collapses_legacy_duplicates(self) -> None:
        client = AsyncMock()
        message_id = bridge.nudge_message_id("4.0.0_SA_CRO~A", "one.md")
        client.request.side_effect = [
            {
                "data": [
                    {"id": "queued-1", "clientUserMessageId": message_id},
                    {"id": "queued-2", "clientUserMessageId": message_id},
                    {"id": "queued-3", "clientUserMessageId": message_id},
                ],
                "nextCursor": None,
            },
            {"deleted": True},
            {"deleted": True},
        ]

        action = await bridge.queue_nudge_once(
            client,
            "thread-1",
            "4.0.0_SA_CRO~A",
            "one.md",
            bridge.nudge_text("4.0.0_SA_CRO~A", "one.md"),
            self.unread("one.md"),
        )

        self.assertEqual(action, "turn/queue-existing")
        self.assertEqual(
            [call.args[0] for call in client.request.await_args_list],
            ["thread/queue/list", "thread/queue/delete", "thread/queue/delete"],
        )

    async def test_file_move_cancels_pending_queue_without_another_nudge(self) -> None:
        client = AsyncMock()
        serial = "4.0.0_SA_CRO~A"
        filename = "handled.md"
        message_id = bridge.nudge_message_id(serial, filename)
        client.request.side_effect = [
            {
                "data": [
                    {"id": "queued-1", "clientUserMessageId": message_id},
                    {"id": "queued-2", "clientUserMessageId": message_id},
                ],
                "nextCursor": None,
            },
            {"deleted": True},
            {"deleted": True},
        ]
        unread = self.unread(filename)
        delivered = {filename}
        task = asyncio.create_task(
            bridge.cancel_handled_nudges(
                client, "thread-1", serial, delivered, 0.01
            )
        )
        unread.unlink()
        try:
            await asyncio.sleep(0.05)
        finally:
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)

        self.assertEqual(delivered, set())
        self.assertEqual(
            [call.args[0] for call in client.request.await_args_list],
            ["thread/queue/list", "thread/queue/delete", "thread/queue/delete"],
        )

    def test_nudge_text_preserves_exact_filename_and_handling_order(self) -> None:
        text = bridge.nudge_text("4.0.0_SA_CRO~A", "exact.md")
        self.assertIn("[HARD-NUDGE] exact.md", text)
        self.assertIn("CRO Base is an immediate Go", text)
        self.assertIn("only after acting move that exact file", text)


if __name__ == "__main__":
    unittest.main()
