"""Codex registration recovery and one-shot sender identity boundaries.

All broker and message side effects are isolated; no real registration,
inbox consumption, or helper process is started by these tests.
"""

from __future__ import annotations

import asyncio
import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

MCP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP))


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, MCP / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


heartbeat = load("registration_heartbeat", "codex-agent-heartbeat.py")
sender = load("registration_sender", "codex-send.py")
SERIAL = "3.0.0_SA_CVO~B"


class BrokerRegistrationProbe(unittest.TestCase):
    def probe(self, rows):
        with patch.object(heartbeat.comms, "_broker_fetch", return_value=rows), \
                patch.object(heartbeat.comms, "_ensure_broker") as ensure:
            result = heartbeat.broker_registration_status(SERIAL)
            ensure.assert_not_called()
            return result

    def test_exact_serial_and_pid_are_required(self):
        self.assertEqual(self.probe([{"serial": SERIAL, "pid": os.getpid()}]),
                         "registered")
        self.assertEqual(self.probe([{"serial": SERIAL, "pid": -1}]), "conflict")
        self.assertEqual(self.probe([{"serial": SERIAL.split("~")[0],
                                      "pid": os.getpid()}]), "missing")

    def test_missing_is_distinct_from_unreadable(self):
        self.assertEqual(self.probe([]), "missing")
        self.assertEqual(self.probe({"error": "busy"}), "unavailable")
        self.assertEqual(self.probe([None]), "unavailable")

    def test_transport_failure_uses_guarded_recovery(self):
        with patch.object(heartbeat.comms, "_broker_fetch",
                          side_effect=[None, []]) as fetch, \
                patch.object(heartbeat.comms, "_ensure_broker", return_value=True) as ensure:
            self.assertEqual(heartbeat.broker_registration_status(SERIAL), "missing")
            ensure.assert_called_once_with()
            self.assertEqual(fetch.call_count, 2)

    def test_unknown_broker_does_not_imply_missing_registration(self):
        with patch.object(heartbeat.comms, "_broker_fetch", return_value=None) as fetch, \
                patch.object(heartbeat.comms, "_ensure_broker", return_value=False):
            self.assertEqual(heartbeat.broker_registration_status(SERIAL), "unavailable")
            fetch.assert_called_once_with("/list-agents")


class HeartbeatRecovery(unittest.IsolatedAsyncioTestCase):
    async def test_broker_row_loss_recovers_even_while_local_heartbeat_is_ok(self):
        done = asyncio.Event()
        polls = []
        registrations = 0
        beats = 0

        async def register(serial, summary):
            nonlocal registrations
            registrations += 1
            self.assertEqual(serial, SERIAL)
            task = asyncio.create_task(asyncio.sleep(3600))
            polls.append(task)
            heartbeat.comms._poll_task = task
            return f"Registered {serial} as live (PID {os.getpid()})."

        async def beat(serial, summary):
            nonlocal beats
            beats += 1
            return f"Heartbeat OK for {serial}."

        def fetch(path):
            self.assertEqual(path, "/list-agents")
            if registrations == 1:
                return []  # the broker lost its row; local liveness survived
            done.set()
            return [{"serial": SERIAL, "pid": os.getpid()}]

        with patch.object(heartbeat.comms, "register_agent", side_effect=register), \
                patch.object(heartbeat.comms, "heartbeat", side_effect=beat), \
                patch.object(heartbeat.comms, "_poll_task", None), \
                patch.object(heartbeat.comms, "_broker_fetch", side_effect=fetch), \
                patch.object(heartbeat, "compute_summary", return_value="test"), \
                contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            task = asyncio.create_task(heartbeat.run(SERIAL, "", 0, Path("unused")))
            try:
                await asyncio.wait_for(done.wait(), timeout=1)
            finally:
                task.cancel()
                with contextlib.suppress(asyncio.CancelledError):
                    await task
                for poll in polls:
                    if not poll.done():
                        poll.cancel()
            self.assertIsNone(heartbeat.comms._poll_task)
        self.assertEqual(registrations, 2)
        self.assertGreaterEqual(beats, 2)
        self.assertTrue(all(poll.cancelled() for poll in polls))

    async def test_conflicting_broker_owner_is_not_overwritten(self):
        with patch.object(heartbeat.comms, "register_agent", new_callable=AsyncMock) as register, \
                patch.object(heartbeat.comms, "heartbeat", new_callable=AsyncMock) as beat, \
                patch.object(heartbeat.comms, "_poll_task", None), \
                patch.object(heartbeat, "compute_summary", return_value="test"), \
                patch.object(heartbeat, "broker_registration_status", return_value="conflict"), \
                contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            register.return_value = f"Registered {SERIAL} as live (PID {os.getpid()})."
            beat.return_value = f"Heartbeat OK for {SERIAL}."
            self.assertEqual(await heartbeat.run(SERIAL, "", 0, Path("unused")), 2)
            self.assertEqual(register.await_count, 1)


class OneShotSender(unittest.TestCase):
    def test_receipt_preserves_warning_and_explains_process_boundary(self):
        receipt = ("Message delivered (filesystem)"
                   " [sender unverified -- register_agent to send verified]")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "liveness.json").write_text(json.dumps({
                SERIAL: {"pid": 123, "last_seen_epoch": time.time()},
            }), encoding="utf-8")
            output = io.StringIO()
            with patch.object(sender, "__file__", str(root / "codex-send.py")), \
                    patch.dict(os.environ, {"OPAL_AGENT_SERIAL": SERIAL}), \
                    patch.object(sender.comms, "send_message", new_callable=AsyncMock) as send, \
                    patch.object(sender.comms, "register_agent", new_callable=AsyncMock) as register, \
                    contextlib.redirect_stdout(output):
                send.return_value = receipt
                result = sender.main(["--from-serial", SERIAL, "--to", "1.0.0_SA_CTO",
                                      "--subject", "test", "--body", "test body"])
                register.assert_not_called()
                send.assert_awaited_once_with(from_agent=SERIAL, to_agent="1.0.0_SA_CTO",
                                             subject="test", body="test body")
        self.assertEqual(result, 0)
        self.assertIn("sender unverified", output.getvalue())
        self.assertIn("one-shot process", output.getvalue())
        self.assertIn("do not register a second process", output.getvalue())
        self.assertNotIn("register_agent to send verified", output.getvalue())

    def test_other_receipts_are_not_rewritten(self):
        for receipt in ("SEND REFUSED: sender identity guard", "Message delivered",
                        "QUEUED for a dead recipient"):
            self.assertEqual(sender.explain_receipt(receipt), receipt)


if __name__ == "__main__":
    unittest.main()
