"""Readiness negative tests -- the arms that make false readiness inexpressible.

Each test names the 2026-08-26 incident arm it closes: three seats broadcast
"WORKING: Codex non-consuming inbox monitor active" while two of them had no
bridge and no detector, because the summary was an argparse default and no
instrument observed the conjunction.
"""

from __future__ import annotations

import importlib.util
import asyncio
import contextlib
import json
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path

MCP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP))


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, MCP / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


heartbeat = load("codex_agent_heartbeat", "codex-agent-heartbeat.py")
status = load("codex_seat_status", "codex-seat-status.py")
bridge = load("codex_inbox_turn_bridge_r", "codex-inbox-turn-bridge.py")

SERIAL = "4.0.0_SA_CRO~B"
ALIVE = os.getpid()  # a PID that provably resolves alive
DEAD = 4_000_000     # far above any real PID on this box


def write_state(runtime: Path, bridge_pid, detector_pid, thread="thread-1"):
    runtime.mkdir(parents=True, exist_ok=True)
    (runtime / "bridge-state.json").write_text(
        json.dumps(
            {
                "serial": SERIAL,
                "thread_id": thread,
                "endpoint": "ws://127.0.0.1:59999",
                "bridge_pid": bridge_pid,
                "detector_pid": detector_pid,
                "bound_at": "2026-08-26T17:00:00Z",
            }
        ),
        encoding="utf-8",
    )


class HeartbeatSummaryIsMeasured(unittest.TestCase):
    """The summary can no longer assert what it did not observe."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.runtime = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_no_state_file_reports_degraded(self):
        # Incident arm: bridge never bound (fresh-launch timeout death).
        summary = heartbeat.compute_summary(self.runtime)
        self.assertIn("DEGRADED", summary)
        self.assertIn("NOT inbox-reachable", summary)

    def test_dead_bridge_reports_degraded(self):
        write_state(self.runtime, bridge_pid=DEAD, detector_pid=ALIVE)
        summary = heartbeat.compute_summary(self.runtime)
        self.assertIn("DEGRADED", summary)
        self.assertIn("bridge", summary)

    def test_dead_detector_reports_degraded(self):
        write_state(self.runtime, bridge_pid=ALIVE, detector_pid=DEAD)
        self.assertIn("DEGRADED", heartbeat.compute_summary(self.runtime))

    def test_live_conjunction_reports_ready(self):
        write_state(self.runtime, bridge_pid=ALIVE, detector_pid=ALIVE)
        summary = heartbeat.compute_summary(self.runtime)
        self.assertIn("READY", summary)
        self.assertIn("measured", summary)

    def test_the_old_lie_is_inexpressible(self):
        # The exact false sentence from the incident must be unproducible.
        write_state(self.runtime, bridge_pid=DEAD, detector_pid=DEAD)
        summary = heartbeat.compute_summary(self.runtime, note="monitor active")
        self.assertNotIn("WORKING: Codex non-consuming inbox monitor active",
                         summary.split(" | ")[0])
        self.assertIn("DEGRADED", summary)


class HeartbeatLostRegistrationRecovery(unittest.IsolatedAsyncioTestCase):
    async def test_run_reregisters_when_liveness_entry_is_lost(self):
        old_comms = heartbeat.comms
        done = asyncio.Event()

        class FakeComms:
            _poll_task = None

            def _broker_fetch(self, path):
                return [{"serial": SERIAL, "pid": os.getpid()}]

            def __init__(self):
                self.registrations = 0
                self.beats = 0

            async def register_agent(self, serial, summary):
                self.registrations += 1
                return f"Registered {serial} as live (PID 1)."

            async def heartbeat(self, serial, summary):
                self.beats += 1
                if self.beats == 1:
                    return f"{serial} is not registered. Call register_agent first."
                if self.registrations >= 2:
                    done.set()
                return f"Heartbeat OK for {serial}."

        fake = FakeComms()
        heartbeat.comms = fake
        try:
            task = asyncio.create_task(
                heartbeat.run(SERIAL, "", 0, Path(tempfile.gettempdir()))
            )
            await asyncio.wait_for(done.wait(), timeout=1)
            task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await task
        finally:
            heartbeat.comms = old_comms

        self.assertEqual(fake.registrations, 2)


def proc(pid: int, cmdline: str) -> dict:
    return {"pid": pid, "cmdline": cmdline}


def table(serial=SERIAL, hb=True, br=True, det=True, watcher=False, dup_hb=False):
    procs = []
    if hb:
        procs.append(proc(101, f"python -u codex-agent-heartbeat.py --serial {serial}"))
    if dup_hb:
        procs.append(proc(102, f"python -u codex-agent-heartbeat.py --serial {serial}"))
    if br:
        procs.append(proc(201, f"python -u codex-inbox-turn-bridge.py --serial {serial}"))
    if det:
        procs.append(proc(301, f"python -u codex-inbox-monitor.py --serial {serial}"))
    if watcher:
        procs.append(proc(401, f"bash org/mcp/inbox-watch.sh {serial} stream"))
    return procs


def liveness(serial=SERIAL, pid=101, fresh=True):
    return {serial: {"pid": pid,
                     "last_seen_epoch": time.time() - (5 if fresh else 500)}}


class StatusConjunction(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.runtime = Path(self.tmp.name)
        write_state(self.runtime, bridge_pid=201, detector_pid=301)
        self.tcp_ok = lambda port: True

    def tearDown(self):
        self.tmp.cleanup()

    def probe(self, procs, live=None):
        return status.probe_seat(
            SERIAL, self.runtime, procs, live or liveness(), time.time(),
            tcp_probe=self.tcp_ok,
        )

    def test_full_conjunction_is_green(self):
        self.assertTrue(self.probe(table())["green"])

    def test_heartbeat_alone_is_red(self):
        # THE incident arm: liveness green, bridge and detector absent.
        report = self.probe(table(br=False, det=False))
        self.assertFalse(report["green"])
        self.assertFalse(report["checks"]["bridge"]["ok"])
        self.assertFalse(report["checks"]["detector"]["ok"])

    def test_bridge_without_detector_is_red(self):
        self.assertFalse(self.probe(table(det=False))["green"])

    def test_duplicate_heartbeat_is_red(self):
        report = self.probe(table(dup_hb=True))
        self.assertFalse(report["green"])
        self.assertFalse(report["checks"]["heartbeat"]["ok"])

    def test_consuming_watcher_is_red(self):
        report = self.probe(table(watcher=True))
        self.assertFalse(report["green"])
        self.assertFalse(report["checks"]["no_consuming_watcher"]["ok"])

    def test_stale_liveness_is_red(self):
        self.assertFalse(
            self.probe(table(), live=liveness(fresh=False))["green"]
        )

    def test_liveness_owned_by_wrong_pid_is_red(self):
        # liveness green but registered to a pid that is NOT the heartbeat:
        # the false-attribution arm.
        self.assertFalse(self.probe(table(), live=liveness(pid=999))["green"])

    def test_base_serial_does_not_match_lane_processes(self):
        # exact-serial discipline: a base probe must not count lane helpers.
        lane_only = table(serial="4.0.0_SA_CRO~B")
        report = status.probe_seat(
            "4.0.0_SA_CRO", self.runtime, lane_only, {}, time.time(),
            tcp_probe=self.tcp_ok,
        )
        self.assertFalse(report["green"])
        self.assertFalse(report["checks"]["heartbeat"]["ok"])


class DiscoveryDeadline(unittest.IsolatedAsyncioTestCase):
    async def test_finite_timeout_still_fails_loud(self):
        class Empty:
            async def request(self, *_a, **_k):
                return {"data": []}

        with self.assertRaises(TimeoutError):
            await bridge.discover_thread(Empty(), Path.cwd(), 0.3)

    async def test_zero_means_wait_then_bind(self):
        # timeout 0 must SURVIVE an empty interval and bind when the thread
        # appears -- the fresh-launch arm the old 120s default killed.
        calls = {"n": 0}
        cwd = Path.cwd()

        class LateThread:
            async def request(self, *_a, **_k):
                calls["n"] += 1
                if calls["n"] < 3:
                    return {"data": []}
                return {"data": [{
                    "id": "thread-late",
                    "cwd": str(cwd.resolve()),
                    "status": {"type": "idle"},
                    "parentThreadId": None,
                }]}

        thread_id = await bridge.discover_thread(LateThread(), cwd, 0)
        self.assertEqual(thread_id, "thread-late")
        self.assertGreaterEqual(calls["n"], 3)


class SendIdentity(unittest.TestCase):
    """codex-send refuses before any read or write on identity mismatch."""

    def run_send(self, env_serial, argv):
        import subprocess
        env = dict(os.environ)
        if env_serial is None:
            env.pop("OPAL_AGENT_SERIAL", None)
        else:
            env["OPAL_AGENT_SERIAL"] = env_serial
        return subprocess.run(
            [sys.executable, "-u", str(MCP / "codex-send.py")] + argv,
            capture_output=True, text=True, env=env, timeout=60,
        )

    def test_caller_mismatch_refused(self):
        out = self.run_send(
            "0.0.0_AB_MSTR",
            ["--from-serial", SERIAL, "--to", "2.0.0_SA_COO",
             "--subject", "x", "--body", "y"],
        )
        self.assertEqual(out.returncode, 2)
        self.assertIn("does not match", out.stderr)

    def test_bad_serial_shape_refused(self):
        out = self.run_send(
            "not-a-serial",
            ["--from-serial", "not-a-serial", "--to", "2.0.0_SA_COO",
             "--subject", "x", "--body", "y"],
        )
        self.assertEqual(out.returncode, 2)

    def test_unregistered_sender_refused(self):
        # env matches but nobody registered this serial -> presence gate.
        ghost = "9.9.9_ZZ_GhostSeat"
        out = self.run_send(
            ghost,
            ["--from-serial", ghost, "--to", "2.0.0_SA_COO",
             "--subject", "x", "--body", "y"],
        )
        self.assertEqual(out.returncode, 2)
        self.assertIn("liveness", out.stderr)


if __name__ == "__main__":
    unittest.main()
