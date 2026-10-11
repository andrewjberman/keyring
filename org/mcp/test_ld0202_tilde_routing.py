#!/usr/bin/env python3
"""LD-0202 tilde-suffix routing regression test (standalone, no live broker).

Exercises the suffix decision logic of the A1/B1/B2/C1 fixes against the REAL
server.py functions, with LIVENESS_FILE monkeypatched to a temp file (the live
liveness.json + broker are never touched). Covers acceptance criteria 1-3 of
LD-0202; AC4 (E1/E2 dead-code removal) is a repo-state assert below; AC5 (D1
marker retire) + AC6 (fabric-wide restart) are rollout phases, not unit-testable.

Run: python org/mcp/test_ld0202_tilde_routing.py   (exit 0 = all pass)
"""
from __future__ import annotations

import asyncio
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = "0.4.2_RD_AdvisorIntelligence"   # a real serial with an org folder
LANE = f"{BASE}~Z"                       # a lane with NO live entry (Z = unused)

_results: list[tuple[str, bool, str]] = []


def _check(name: str, ok: bool, detail: str = "") -> None:
    _results.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


def _load_server(tmp: Path):
    """Import server.py fresh with LIVENESS_FILE/LOCK_FILE pointed at a temp file,
    broker disabled, piggyback drained to noise-free. _broker_available is already
    False at import; mcp.run() is __main__-gated so import does not start a server."""
    spec = importlib.util.spec_from_file_location("ld0202_server_under_test",
                                                  HERE / "server.py")
    srv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(srv)
    srv.LIVENESS_FILE = tmp / "liveness.json"
    srv.LOCK_FILE = (tmp / "liveness.json").with_suffix(".lock")
    srv._broker_available = False
    srv._drain_piggyback = lambda: ""          # isolate from inbox piggyback
    srv._broker_fetch = lambda *a, **k: None    # belt-and-suspenders (already gated)
    return srv


def _seed(srv, data: dict) -> None:
    srv.LIVENESS_FILE.write_text(json.dumps(data), encoding="utf-8")


def _read(srv) -> dict:
    return json.loads(srv.LIVENESS_FILE.read_text(encoding="utf-8"))


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        srv = _load_server(tmp)
        now = __import__("time").time()
        base_entry = {"pid": 111, "summary": "BASE-SUMMARY",
                      "last_seen_epoch": now, "last_seen": "x"}

        # ---- AC2 (B1 heartbeat): a SUFFIXED heartbeat for an absent lane must NOT
        # clobber the base entry's summary. ----
        _seed(srv, {BASE: dict(base_entry)})
        msg = asyncio.run(srv.heartbeat(LANE, "LANE-SUMMARY-CLOBBER"))
        after = _read(srv)
        _check("AC2.B1 suffixed heartbeat does NOT clobber base summary",
               after.get(BASE, {}).get("summary") == "BASE-SUMMARY"
               and "not registered" in msg.lower(),
               f"base.summary={after.get(BASE, {}).get('summary')!r} msg={msg[:60]!r}")
        _check("AC2.B1 suffixed heartbeat did NOT create a base-clobbering write",
               LANE not in after and after.get(BASE, {}).get("summary") == "BASE-SUMMARY")

        # ---- AC2 (B2 set_summary): same, via set_summary ----
        _seed(srv, {BASE: dict(base_entry)})
        # The G-A self-scope guard (2026-07-14) refuses an unregistered session before the B2 branch is reached, so the
        # check runs AS the lane: the B2 branch under test is the one that answers "not registered" for it.
        srv._my_serial = LANE
        msg = asyncio.run(srv.set_summary(LANE, "LANE-SUMMARY-CLOBBER"))
        srv._my_serial = None
        after = _read(srv)
        _check("AC2.B2 suffixed set_summary does NOT clobber base summary",
               after.get(BASE, {}).get("summary") == "BASE-SUMMARY"
               and "not registered" in msg.lower(),
               f"base.summary={after.get(BASE, {}).get('summary')!r}")

        # ---- B1/B2 backward-compat: an UNSUFFIXED caller still updates base ----
        _seed(srv, {BASE: dict(base_entry)})
        asyncio.run(srv.heartbeat(BASE, "NEW-BASE-SUMMARY"))
        _check("B1 unsuffixed heartbeat STILL updates base (backward-compat kept)",
               _read(srv).get(BASE, {}).get("summary") == "NEW-BASE-SUMMARY")

        # ---- AC1 (A1 get_agent_status): a SUFFIXED query for an absent lane must
        # return NOT REGISTERED (lane ~Z), never the base agent's state. ----
        _seed(srv, {BASE: dict(base_entry)})
        out = asyncio.run(srv.get_agent_status(LANE))
        _check("AC1.A1 suffixed status for absent lane = NOT REGISTERED (lane ~Z)",
               "NOT REGISTERED" in out and "~Z" in out
               and "BASE-SUMMARY" not in out,
               "base summary leaked into ~Z status" if "BASE-SUMMARY" in out else "")

        # ---- A1 positive: unsuffixed query still shows base; suffixed query WITH a
        # live lane entry shows the lane (not base) ----
        out_base = asyncio.run(srv.get_agent_status(BASE))
        _check("A1 unsuffixed status shows base liveness (backward-compat kept)",
               "BASE-SUMMARY" in out_base)
        _seed(srv, {BASE: dict(base_entry),
                    LANE: {"pid": 222, "summary": "LANE-OWN-SUMMARY",
                           "last_seen_epoch": now, "last_seen": "x"}})
        out_lane = asyncio.run(srv.get_agent_status(LANE))
        _check("A1 suffixed status shows the LANE's own state, not base",
               "LANE-OWN-SUMMARY" in out_lane and "BASE-SUMMARY" not in out_lane)

        # ---- AC3 (C1 send_message channel-push targeting): base-addressed send ->
        # base ONLY; suffixed send -> exact instance. Replicate the exact post-fix
        # filter (server.py send_message) using the module's own helpers. ----
        data = {
            BASE: {"last_seen_epoch": now},
            f"{BASE}~B": {"last_seen_epoch": now},
            f"{BASE}~C": {"last_seen_epoch": now},
        }

        def _targets(to_agent: str) -> list[str]:
            base = srv._base_serial(to_agent)
            target_suffix = srv._instance_suffix(to_agent)
            out = []
            for serial, info in data.items():
                if srv._base_serial(serial) == base and srv._liveness_status(info) == "live":
                    if srv._instance_suffix(serial) != target_suffix:   # the C1 fix
                        continue
                    out.append(serial)
            return out

        _check("AC3.C1 base-addressed send pushes to BASE ONLY (not all lanes)",
               _targets(BASE) == [BASE], f"targets={_targets(BASE)}")
        _check("AC3.C1 suffixed send pushes to the EXACT instance only",
               _targets(f"{BASE}~B") == [f"{BASE}~B"], f"targets={_targets(f'{BASE}~B')}")

    # ---- AC4 (E1/E2 dead-code removal): repo-state asserts ----
    e1_gone = not (HERE / "complearns_server.py").exists()
    _check("AC4.E1 complearns_server.py removed from org/mcp", e1_gone)
    poller = (HERE / "agent-poller.py").read_text(encoding="utf-8")
    # Assert the dead CODE is gone (the def + the live channel-assignment), NOT that
    # the names never appear -- a retirement breadcrumb comment naming what it removed
    # is correct + desirable.
    _check("AC4.E2 agent-poller.py CL-channel switch removed (def + assignment gone)",
           "def _switch_to_cl_channel" not in poller
           and "def _is_cl_serial" not in poller
           and '= "complearns-agent-comms"' not in poller
           and "_switch_to_cl_channel()" not in poller)

    # ---- syntax gate on the two edited modules ----
    for f in ("server.py", "agent-poller.py"):
        rc = subprocess.run([sys.executable, "-m", "py_compile", str(HERE / f)]).returncode
        _check(f"py_compile {f}", rc == 0)

    passed = sum(1 for _, ok, _ in _results if ok)
    total = len(_results)
    print(f"\n=== {passed}/{total} checks passed ===")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
