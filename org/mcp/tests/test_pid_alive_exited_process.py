"""Regression: _pid_alive() must assert RUNNING, not merely ADDRESSABLE.

THE DEFECT (2026-07-13, host OOM killed the fabric):
    agent-poller._pid_alive() returned True on any OpenProcess() handle. On Windows a
    process OBJECT outlives the process while any handle is held, so OpenProcess()
    succeeds on an exited-but-unreaped pid. The poller's only exit condition is
    "my MCP server died" -- and it could never observe that. 2.0.0_SA_COO's poller kept
    writing last_seen every 2s and heartbeating the broker every 10s for a process that
    no longer existed. Every liveness instrument in the fabric reported a DEAD executive
    as LIVE with a 1-second heartbeat; the identity guard then refused to respawn the
    serial because it was "held by a LIVE process."

THE TEST THAT MATTERS is test_exited_process_with_open_handle_is_dead. It is the
PROVEN-RED case: subprocess.Popen holds the child's handle open after the child exits,
which is exactly the state that forged COO's heartbeat. The OLD implementation returns
True for it. A test suite with no case the old code fails cannot validate the fix --
a probe never observed to return False has not been shown able to.

The two live-pid cases are the PAIRED POSITIVE CONTROLS, and they are not decoration:
without them, a probe hard-wired to `return False` would pass every negative arm.
"""
from __future__ import annotations

import ctypes
import importlib.util
import os
import subprocess
import sys
from pathlib import Path

import pytest

POLLER = Path(__file__).resolve().parents[1] / "agent-poller.py"
pytestmark = pytest.mark.skipif(sys.platform != "win32", reason="Windows handle semantics")


def _load_pid_alive():
    spec = importlib.util.spec_from_file_location("agent_poller", POLLER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod._pid_alive


def _openprocess_only(pid: int) -> bool:
    """The OLD implementation, kept so the test can PROVE the bug was real."""
    k = ctypes.windll.kernel32
    h = k.OpenProcess(0x1000, False, pid)
    if h:
        k.CloseHandle(h)
        return True
    return False


# ---------------------------------------------------------------- positive controls
def test_own_pid_is_alive():
    """POSITIVE CONTROL. If this fails, every negative result below is meaningless."""
    assert _load_pid_alive()(os.getpid()) is True


def test_live_child_is_alive():
    """POSITIVE CONTROL on a pid we did not author."""
    p = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
    try:
        assert _load_pid_alive()(p.pid) is True
    finally:
        p.kill()
        p.wait()


# ---------------------------------------------------------------- the proven-RED case
def test_exited_process_with_open_handle_is_dead():
    """THE DEFECT, REPRODUCED. Popen still holds the handle after the child exits.

    This is the precise state COO's pid 15900 was in when the poller forged its
    heartbeat. If this ever goes green under the old logic, the fix has been reverted.
    """
    p = subprocess.Popen([sys.executable, "-c", "raise SystemExit(0)"])
    p.wait()  # child is EXITED -- but Popen keeps its process handle open

    # The bug, still demonstrable: the old probe calls this dead process ALIVE.
    assert _openprocess_only(p.pid) is True, (
        "The old OpenProcess-only probe no longer reports an exited process as alive. "
        "The handle was released early, so this test is no longer exercising the "
        "defect -- FIX THE TEST, do not delete it: without a proven-RED case the "
        "suite cannot validate the fix."
    )

    # The fix: it must say DEAD.
    assert _load_pid_alive()(p.pid) is False


def test_never_existed_pid_is_dead():
    assert _load_pid_alive()(0x7FFFFFF0) is False


def test_nonpositive_pid_is_dead():
    fn = _load_pid_alive()
    assert fn(0) is False
    assert fn(-1) is False
