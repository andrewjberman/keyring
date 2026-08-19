"""D0_TIGHTENING TO-1 -- T1 primitive (i) EXERCISE: recipient-LIST send (server plane).

Acceptance T1-1: a three-recipient send with ONE DEAD SEAT returns 2 DELIVERED + 1 QUEUED,
never a silent aggregate; an unknown serial returns REFUSED.
Acceptance T1-2: the S1 body-cc replay (LD-0424) is DETECTABLE via the receipt query.

Exercised against the REAL send_message code path with a SCRATCH broker, SCRATCH inbox and
SCRATCH liveness file -- no live fabric state is written.
"""
from __future__ import annotations

import asyncio
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

WS = Path(__file__).resolve().parents[2]  # org/mcp/X.py -> workspace root
PORT = int(os.environ.get("T1_TEST_PORT2", "7912"))
BASE = f"http://127.0.0.1:{PORT}"
RESULTS: list[tuple[str, str, str]] = []


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tid}: {detail}")


def health(timeout=15.0):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with urllib.request.urlopen(BASE + "/health", timeout=2) as r:
                if r.status == 200:
                    return True
        except Exception:
            time.sleep(0.25)
    return False


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="t1send_"))
    db = tmp / "b.db"
    env = dict(os.environ)
    env["OPAL_BROKER_PORT"] = str(PORT)
    env["OPAL_BROKER_DB"] = str(db)
    proc = subprocess.Popen([sys.executable, str(WS / "org" / "mcp" / "broker.py")],
                            env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if not health():
        proc.kill()
        print("scratch broker failed to start")
        return 2

    try:
        spec = importlib.util.spec_from_file_location("opal_server_t1",
                                                      WS / "org" / "mcp" / "server.py")
        srv = importlib.util.module_from_spec(spec)
        sys.modules["opal_server_t1"] = srv
        spec.loader.exec_module(srv)

        # --- redirect every write surface to scratch ---
        srv.BROKER_URL = BASE
        srv._broker_available = True
        srv.INBOX_DIR = tmp / "inbox"
        srv.INBOX_DIR.mkdir(parents=True, exist_ok=True)
        srv.LIVENESS_FILE = tmp / "liveness.json"
        srv._my_serial = "0.8.0_AE_CloudComp"

        # Three REAL serials so _resolve_agent_folder resolves, plus one bogus.
        LIVE_1 = "1.0.0_SA_CTO"
        LIVE_2 = "2.0.0_SA_COO"
        DEAD = "3.0.0_SA_CVO"
        BOGUS = "9.9.9_NO_SUCH_SEAT"

        now = time.time()
        srv.LIVENESS_FILE.write_text(json.dumps({
            LIVE_1: {"pid": 1, "last_seen_epoch": now, "summary": "t1 fixture"},
            LIVE_2: {"pid": 2, "last_seen_epoch": now, "summary": "t1 fixture"},
            # DEAD deliberately absent -> not live -> must yield QUEUED, never silence.
        }), encoding="utf-8")

        # --- T1-1: three recipients, one dead ---
        out = asyncio.run(srv.send_message(
            from_agent="0.8.0_AE_CloudComp", to_agent="",
            subject="T1-1 three-recipient exercise",
            body="recipient-list send with one dead seat",
            to_agents=[LIVE_1, LIVE_2, DEAD]))
        print("\n--- send_message(to_agents=[live, live, dead]) returned ---")
        print(out)
        print("--- end ---\n")

        # Parse the PER-RECIPIENT rows only. A naive substring count over the whole
        # response also matches the summary line and the QUEUED explainer -- it reported
        # 3+3 against a correct 2+1. The instrument was wrong, not the code; count the
        # rows the map actually emits.
        def _rows(text):
            got = {}
            for ln in text.splitlines():
                parts = ln.strip().split()
                # parts[1] must be a SERIAL, not "=" -- the trailing explainer lines
                # ("QUEUED = written to inbox...") also start with a state token.
                if len(parts) >= 2 and parts[0] in ("DELIVERED", "QUEUED", "REFUSED") \
                        and parts[1] != "=" and not ln.strip().startswith("--"):
                    got.setdefault(parts[0], []).append(parts[1])
            return got

        rows = _rows(out)
        n_del = len(rows.get("DELIVERED", []))
        n_q = len(rows.get("QUEUED", []))
        rec("T1-1a", n_del == 2 and n_q == 1,
            f"3 recipients w/ one dead -> {n_del} DELIVERED + {n_q} QUEUED "
            f"(required: 2 + 1)")
        rec("T1-1b", DEAD in out and "QUEUED" in out,
            f"the dead seat {DEAD} is NAMED with its own state -- not folded into an "
            f"aggregate, not silent")
        rec("T1-1c", "denominator 3" in out,
            "the result map prints its DENOMINATOR (a count without its frame is the "
            "class this estate keeps getting bitten by)")

        # --- unknown serial -> REFUSED ---
        out2 = asyncio.run(srv.send_message(
            from_agent="0.8.0_AE_CloudComp", to_agent="",
            subject="T1-1 refused-path exercise", body="unknown serial",
            to_agents=[LIVE_1, BOGUS]))
        rec("T1-1d", "REFUSED" in out2 and BOGUS in out2,
            f"unknown serial {BOGUS} -> REFUSED and named (nothing written for it)")

        # --- backward compatibility: single recipient keeps the legacy receipt ---
        out3 = asyncio.run(srv.send_message(
            from_agent="0.8.0_AE_CloudComp", to_agent=LIVE_1,
            subject="T1-1 legacy shape", body="single recipient"))
        rec("T1-1e", out3.startswith("Message delivered to ") and "inbox" in out3,
            f"single-recipient call returns the LEGACY receipt shape unchanged: "
            f"{out3[:60]}...")

        # --- Msg-ID stamped into the file (what makes a precise READ ack possible) ---
        files = list((srv.INBOX_DIR / "1.0.0_SA_CTO").glob("*.md"))
        stamped = [f for f in files if "**Msg-ID:**" in f.read_text(encoding="utf-8")]
        rec("T1-1f", len(stamped) == len(files) and files,
            f"{len(stamped)}/{len(files)} delivered files carry **Msg-ID:** "
            f"(denominator {len(files)}) -- the ack can name the exact row")

        # --- T1-2: the S1 body-cc replay is DETECTABLE via the receipt query ---
        # Replay the measured LD-0424 shape: sender writes "cc: <seat>" in the BODY.
        body_cc = ("Freeze released, you may proceed.\n\ncc: " + LIVE_2 +
                   "\ncc: " + DEAD + "\n")
        asyncio.run(srv.send_message(
            from_agent="0.8.0_AE_CloudComp", to_agent=LIVE_1,
            subject="T1-2 body-cc replay (LD-0424 shape)", body=body_cc))

        def q(serial):
            return asyncio.run(srv.get_delivery_state(agent_serial=serial, limit=50))

        q1, q2, qd = q(LIVE_1), q(LIVE_2), q(DEAD)
        cc_in_1 = "T1-2 body-cc replay" in q1
        cc_in_2 = "T1-2 body-cc replay" in q2
        cc_in_d = "T1-2 body-cc replay" in qd
        rec("T1-2a", cc_in_1 and not cc_in_2 and not cc_in_d,
            f"receipt query shows the body-cc message reached {LIVE_1} ONLY "
            f"(reached {LIVE_2}: {cc_in_2}, reached {DEAD}: {cc_in_d}) -- the in-body "
            f"'cc' copied NOBODY, and the query NAMES that")
        rec("T1-2b", "TOTALS:" in q1 and "denominator" in q1,
            "the receipt query prints per-state TOTALS with a denominator")

        # POSITIVE CONTROL for the query: the same two seats DO both appear when the
        # recipient LIST is used. Without this, T1-2a could be an artifact of a query
        # that simply cannot see LIVE_2.
        asyncio.run(srv.send_message(
            from_agent="0.8.0_AE_CloudComp", to_agent="",
            subject="T1-2 POSITIVE CONTROL via to_agents",
            body="same two seats, addressed properly",
            to_agents=[LIVE_1, LIVE_2]))
        p1, p2 = q(LIVE_1), q(LIVE_2)
        rec("T1-2c", "POSITIVE CONTROL" in p1 and "POSITIVE CONTROL" in p2,
            "POSITIVE CONTROL: with to_agents, the SAME query sees the message at BOTH "
            "seats -- so T1-2a's absence is a real absence, not a blind query")
    finally:
        try:
            proc.kill()
            proc.wait(timeout=10)
        except Exception:
            pass
        shutil.rmtree(tmp, ignore_errors=True)

    print("\n" + "=" * 78)
    n_pass = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print(f"T1 SEND/RECEIPT BATTERY: {n_pass}/{len(RESULTS)} PASS (denominator {len(RESULTS)})")
    print("=" * 78)
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
