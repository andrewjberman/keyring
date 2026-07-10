#!/usr/bin/env python3
"""send_message delivery-path witness: WHERE does the channel push actually land?

Standalone, no live broker, no live inbox, no live liveness.json.

WHY THIS FILE EXISTS
--------------------
`test_ld0202_tilde_routing.py` AC3.C1 guards the channel-push targeting filter in
`send_message`. It does so by RE-IMPLEMENTING that filter locally (its own `_targets()`
helper, comment: "Replicate the exact post-fix filter ... using the module's own
helpers"). It never calls `send_message` and never calls `_push_channel_message`
(grep: 0 occurrences of each). It therefore asserts on a hand-copy of the code under
test, is green today, and would stay green no matter where the push went.

This file CALLS THE REAL `send_message`.

WHAT IT WITNESSES (all three source-confirmed, all three exercised here)
-----------------------------------------------------------------------
  D1  THE PUSH TARGETS THE SENDER.
        server.py:1119-1120  send_message  -> `_active_ctx = ctx`   (the SENDER's Context)
        server.py:1187-1199  the loop      -> `_push_channel_message(...)`
        server.py:369        that fn       -> `ctx = _active_ctx`
        server.py:377                      -> `ctx.session.send_log_message(...)`
      `meta["to_agent"]` is passed and never read. The receipt still prints
      `channel push`. That token is a liveness.json lookup (server.py:1176) wearing
      the costume of a delivery receipt.

  D2  SUFFIX MISMATCH = TOTAL SILENT LOSS TO A LIVE AGENT.
      Recipient live as `BASE~B`; sender addresses `BASE`:
        filesystem   server.py:1131-1135  -> inbox/BASE/    (the ~B lane watches inbox/BASE/~B/)
        broker       server.py:1157       -> to_serial=BASE; broker.py `WHERE to_serial = ?`
                     server.py:553-554    -> the ~B agent polls with `_my_serial = "BASE~B"`
        channel push server.py:1183       -> skipped, then :1188 pushes to the sender anyway
      Three for three, and the receipt returns the word "delivered".

  D3  NULL: no active ctx -> `_push_channel_message` returns False, nobody receives.

CONTROLS. A rail that cannot fail is not a rail. D1's "recipient got 0" is only
evidence because V1 shows the SAME recorder registers a 1 when `_active_ctx` is the
recipient. Without V1, a dead recorder and a self-push are indistinguishable.

MODES
  (default)        assert CURRENT behavior. exit 0 = DEFECT REPRODUCED.
  --assert-fixed   assert POST-FIX behavior. exit 0 = fix verified.
                   Run this after the server.py fix merges; it is the regression test.

EXIT CODES     0 = expectations met   1 = expectations violated   2 = could not evaluate
Run: python org/mcp/test_send_message_push_target.py   (add --assert-fixed post-merge)

Authored 0.7.0_AE_CloudOps. server.py is CTO's arch surface; this file touches it not at all.
"""
from __future__ import annotations

import asyncio
import importlib.util
import json
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = "0.4.2_RD_AdvisorIntelligence"   # a real serial with an org folder (as LD-0202 uses)
LANE = f"{BASE}~B"
SENDER = "0.7.0_AE_CloudOps"

_results: list[tuple[str, bool, str]] = []
_broker_payloads: list[dict] = []


def _check(name: str, ok: bool, detail: str = "") -> None:
    _results.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


class _FakeSession:
    def __init__(self) -> None:
        self.received: list[str] = []

    async def send_log_message(self, level, data, logger):  # noqa: ANN001
        self.received.append(data)


class _FakeCtx:
    def __init__(self) -> None:
        self.session = _FakeSession()


def _load_server(tmp: Path):
    """Import server.py fresh, fully isolated. mcp.run() is __main__-gated."""
    spec = importlib.util.spec_from_file_location("push_target_server_under_test",
                                                  HERE / "server.py")
    srv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(srv)
    srv.LIVENESS_FILE = tmp / "liveness.json"
    srv.LOCK_FILE = (tmp / "liveness.json").with_suffix(".lock")
    srv.INBOX_DIR = tmp / "inbox"
    srv.INBOX_DIR.mkdir(parents=True, exist_ok=True)
    srv._drain_piggyback = lambda: ""

    # Mirror production: the broker ACCEPTS the row (it does -- under whatever
    # to_serial send_message hands it). Capture the payload so the broker-miss
    # limb is EXERCISED, not merely read off the source.
    srv._broker_available = True

    def _fake_broker_fetch(path, payload=None, *a, **k):  # noqa: ANN001
        if path == "/send-message" and payload:
            _broker_payloads.append(dict(payload))
        return {"ok": True}

    srv._broker_fetch = _fake_broker_fetch
    return srv


def _seed(srv, data: dict) -> None:
    srv.LIVENESS_FILE.write_text(json.dumps(data), encoding="utf-8")


def _live(pid: int = 111) -> dict:
    return {"pid": pid, "summary": "s", "last_seen_epoch": time.time(), "last_seen": "x"}


def main(assert_fixed: bool) -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        try:
            srv = _load_server(tmp)
        except Exception as e:  # noqa: BLE001
            print(f"[ERROR] could not import server.py: {e}")
            print("VERDICT: INDETERMINATE")
            return 2  # could not evaluate -- never 0

        # =============================================================
        # D1 -- push targets the SENDER. Recipient is live, correct suffix.
        # =============================================================
        _seed(srv, {BASE: _live()})
        sender_ctx, recipient_ctx = _FakeCtx(), _FakeCtx()
        _broker_payloads.clear()

        receipt = asyncio.run(
            srv.send_message(SENDER, BASE, "D1-subject", "D1-body", ctx=sender_ctx)
        )
        s_got = len(sender_ctx.session.received)
        r_got = len(recipient_ctx.session.received)
        token = "channel push" in receipt

        print(f"\n  D1 receipt: {receipt}")
        print(f"  D1 sender_got={s_got}  recipient_got={r_got}  receipt_claims_channel_push={token}\n")

        if assert_fixed:
            _check("D1 sender does NOT receive its own outbound push", s_got == 0,
                   f"sender_got={s_got}")
            _check("D1 receipt does not claim a push the recipient never got",
                   not token or r_got > 0)
        else:
            _check("D1 the push lands in the SENDER's own session", s_got == 1,
                   f"sender_got={s_got}")
            _check("D1 the RECIPIENT receives nothing from send_message", r_got == 0,
                   f"recipient_got={r_got}")
            _check("D1 yet the receipt still prints 'channel push'", token,
                   f"receipt={receipt[-40:]!r}")

        # -------- V1 VARIANCE CONTROL: the recorder CAN see the recipient. -------
        # Without this, D1's "recipient_got=0" is indistinguishable from a dead recorder.
        srv._active_ctx = recipient_ctx
        v1 = asyncio.run(srv._push_channel_message(content="V1", meta={"to_agent": BASE}))
        _check("V1 VARIANCE: same recorder registers a 1 when _active_ctx is the recipient",
               v1 is True and len(recipient_ctx.session.received) == 1,
               f"returned={v1} recipient_got={len(recipient_ctx.session.received)}")

        # -------- D3 NULL CONTROL --------
        srv._active_ctx = None
        before = len(sender_ctx.session.received) + len(recipient_ctx.session.received)
        d3 = asyncio.run(srv._push_channel_message(content="D3", meta={"to_agent": BASE}))
        after = len(sender_ctx.session.received) + len(recipient_ctx.session.received)
        _check("D3 NULL: no active ctx -> returns False, zero deliveries",
               d3 is False and after == before, f"returned={d3}")

        # =============================================================
        # D2 -- SUFFIX MISMATCH: recipient live as ~B, sender addresses BASE.
        #        The negative control that MUST fire.
        # =============================================================
        _seed(srv, {LANE: _live(pid=222)})          # ONLY the lane is live
        sender2 = _FakeCtx()
        _broker_payloads.clear()

        receipt2 = asyncio.run(
            srv.send_message(SENDER, BASE, "D2-subject", "D2-body", ctx=sender2)
        )

        base_dir = srv.INBOX_DIR / BASE
        lane_dir = srv.INBOX_DIR / BASE / "~B"
        in_base = sorted(p.name for p in base_dir.glob("*D2-subject*")) if base_dir.exists() else []
        in_lane = sorted(p.name for p in lane_dir.glob("*D2-subject*")) if lane_dir.exists() else []
        broker_to = [p.get("to_serial") for p in _broker_payloads]

        print(f"\n  D2 receipt: {receipt2}")
        print(f"  D2 filesystem -> base_dir={in_base}  lane_dir(~B)={in_lane}")
        print(f"  D2 broker     -> to_serial={broker_to}   (the live agent polls as {LANE!r})")
        print(f"  D2 channel    -> sender_got={len(sender2.session.received)}\n")

        # limb 1: filesystem misses the lane the live agent actually watches
        _check("D2 filesystem: message lands in inbox/BASE/, NOT the live ~B lane dir",
               len(in_base) == 1 and len(in_lane) == 0,
               f"base={in_base} lane={in_lane}")
        # limb 2: broker files it under a to_serial the live agent never polls
        _check("D2 broker: row filed under to_serial=BASE while the live agent polls '~B'",
               broker_to == [BASE], f"broker_to={broker_to}")
        # limb 3: no channel push at all (suffix filter at :1183 skipped the only live entry)
        _check("D2 channel: zero pushes (the one live instance was filtered out at :1183)",
               len(sender2.session.received) == 0,
               f"sender_got={len(sender2.session.received)}")

        if assert_fixed:
            _check("D2 receipt WARNS about the live-but-unaddressed instance",
                   ("SUFFIX MISMATCH" in receipt2) and (LANE in receipt2),
                   f"receipt={receipt2!r}")
            _check("D2 receipt never overstates: no bare 'UNDELIVERED'",
                   "UNDELIVERED" not in receipt2)
        else:
            _check("D2 receipt says 'delivered' though all 3 paths missed a LIVE agent",
                   "delivered" in receipt2.lower(), f"receipt={receipt2!r}")
            _check("D2 receipt never names the live instance it skipped (:1183 discards it)",
                   LANE not in receipt2, f"receipt={receipt2!r}")

    passed = sum(1 for _, ok, _ in _results if ok)
    total = len(_results)
    print(f"\n=== {passed}/{total} checks passed "
          f"({'POST-FIX expectations' if assert_fixed else 'CURRENT behavior'}) ===")

    if passed != total:
        if assert_fixed:
            print("VERDICT: fix NOT verified -- post-fix expectations violated.")
        else:
            print("VERDICT: current behavior does NOT match the documented defect.\n"
                  "         Either the fix landed (re-run with --assert-fixed) or the\n"
                  "         witness is stale. Do NOT read this as 'no defect'.")
        return 1

    if assert_fixed:
        print("VERDICT: FIX VERIFIED -- push no longer self-targets; suffix mismatch is loud.")
    else:
        print("VERDICT: DEFECT REPRODUCED, at the real call site.\n"
              "         D1 push self-targets the sender; the 'channel push' token is a\n"
              "         liveness.json lookup, not a delivery fact.\n"
              "         D2 a suffix mismatch loses the message on ALL THREE paths, and the\n"
              "         receipt says 'delivered'.\n"
              "         When the server.py fix lands, re-run with --assert-fixed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(assert_fixed="--assert-fixed" in sys.argv))
