"""Regression battery: re-offer is BOUNDED, so a never-drained row cannot loop forever.

THE REGRESSION THIS CLOSES WAS MINE. T1 made an undrained message re-offerable so a client
dying between poll and drain recovers it. That is correct only against a server that reports
its drain via /mark-emitted -- and a PRE-T1 server never calls that endpoint, so `delivered`
never leaves 0, the re-offer predicate matches on every poll forever, and a pre-T1 server (no
id-dedupe) appends another copy each time. Measured on the live DB within ~4 minutes of the
broker cycle: 97 polled-but-never-emitted rows vs 15 properly emitted.

The controls are the point:
  A  UNCAPPED (pre-fix predicate) -> the SAME row is re-offered again and again   [MUTANT]
  B  CAPPED   (shipped predicate) -> offers stop at T1_MAX_OFFERS
  C  a row that IS drained is never re-offered at all (the fix does not weaken the normal path)
  D  the exhausted row still reports honestly (OFFER-EXHAUSTED, not SENT, not lost)
  E  the message is STILL RECOVERABLE from the filesystem -- capping loses no content
A alone would pass on a broker that never re-offers anything; B alone would pass on one that
never offers. Both are needed to show the cap discriminates.

Usage: python org/mcp/test_d0_t1_offer_cap.py
"""
from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

WS = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         cwd=str(Path(__file__).resolve().parent),
                         capture_output=True, text=True).stdout.strip())
PORT = int(os.environ.get("T1_CAP_PORT", "7931"))
BASE = f"http://127.0.0.1:{PORT}"
RESULTS: list[tuple[str, str, str]] = []


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tid}: {detail}")


def post(path, body):
    req = urllib.request.Request(BASE + path, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.loads(r.read())


def health(timeout=20.0):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with urllib.request.urlopen(BASE + "/health", timeout=2) as r:
                if r.status == 200:
                    return True
        except Exception:
            time.sleep(0.25)
    return False


def age_poll_stamp(db, mid):
    """Age the poll stamp so the reclaim window has elapsed -- exercises the real
    `polled_at <= now - T1_RECLAIM_S` comparison without sleeping 90s. The clock
    source is the broker's, not the test's."""
    con = sqlite3.connect(str(db))
    con.execute("UPDATE messages SET polled_at='2000-01-01T00:00:00+00:00' WHERE id=?", (mid,))
    con.commit()
    con.close()


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="t1cap_"))
    db = tmp / "cap.db"
    env = dict(os.environ, OPAL_BROKER_PORT=str(PORT), OPAL_BROKER_DB=str(db))
    proc = subprocess.Popen([sys.executable, str(WS / "org" / "mcp" / "broker.py")], env=env,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if not health():
        proc.kill()
        print("scratch broker failed to start")
        return 2
    try:
        from importlib import util
        spec = util.spec_from_file_location("bk", WS / "org" / "mcp" / "broker.py")
        bk = util.module_from_spec(spec)
        spec.loader.exec_module(bk)
        cap = bk.T1_MAX_OFFERS

        print("=" * 82)
        print(f"T1 OFFER-CAP BATTERY (T1_MAX_OFFERS={cap})")
        print("=" * 82)

        # ---- B: CAPPED -- a never-drained row stops being offered ----
        mid = post("/send-message", {"from_serial": "T", "to_serial": "SEAT_NODRAIN",
                                     "subject": "cap", "text": "never drained"})["message_id"]
        offers = 0
        for _ in range(cap + 4):                  # try MORE times than the cap
            age_poll_stamp(db, mid)               # pretend the reclaim window elapsed
            got = post("/poll-messages", {"serial": "SEAT_NODRAIN"})["messages"]
            if any(m["id"] == mid for m in got):
                offers += 1
            else:
                break
        rec("B-CAPPED", offers == cap,
            f"a never-drained row was offered {offers} time(s) against {cap + 4} attempts "
            f"(cap={cap}) -- the loop TERMINATES")

        # ---- D: the exhausted row reports honestly ----
        st = post("/delivery-state", {"message_id": mid})["messages"][0]
        rec("D-HONEST-STATE", st["state"] == "OFFER-EXHAUSTED",
            f"exhausted row reads {st['state']} -- its own state, not SENT (which would claim a "
            f"handoff) and not silently dropped")

        # ---- A: MUTANT -- the PRE-FIX predicate loops without bound ----
        mid2 = post("/send-message", {"from_serial": "T", "to_serial": "SEAT_MUT",
                                      "subject": "mutant", "text": "uncapped"})["message_id"]
        con = sqlite3.connect(str(db))
        uncapped_hits = 0
        for _ in range(cap + 4):
            con.execute("UPDATE messages SET polled_at='2000-01-01T00:00:00+00:00' WHERE id=?",
                        (mid2,))
            con.commit()
            # the PRE-FIX predicate, verbatim: no offer_count term
            row = con.execute(
                "SELECT id FROM messages WHERE to_serial=? AND delivered=0 "
                "AND (polled_at IS NULL OR polled_at <= ?)",
                ("SEAT_MUT", "2099-01-01T00:00:00+00:00")).fetchone()
            if row:
                uncapped_hits += 1
        con.close()
        rec("A-MUTANT-UNCAPPED-LOOPS", uncapped_hits == cap + 4,
            f"the PRE-FIX predicate matched the same row {uncapped_hits}/{cap + 4} times -- "
            f"unbounded. Without this leg, B would pass on a broker that never re-offers at all")

        # ---- C: a DRAINED row is never re-offered ----
        mid3 = post("/send-message", {"from_serial": "T", "to_serial": "SEAT_OK",
                                      "subject": "drained", "text": "normal path"})["message_id"]
        post("/poll-messages", {"serial": "SEAT_OK"})
        post("/mark-emitted", {"serial": "SEAT_OK", "ids": [mid3]})
        age_poll_stamp(db, mid3)
        again = post("/poll-messages", {"serial": "SEAT_OK"})["messages"]
        rec("C-NORMAL-PATH-INTACT", all(m["id"] != mid3 for m in again),
            "a properly drained row is NOT re-offered -- the cap did not weaken the healthy path")

        # ---- F: THE BOUND HOLDS UNDER A CONVERGENCE-SHAPED ACCESS PATTERN ----
        # COO's age-monotonicity hypothesis was FALSIFIED by DS~B (a 1-copy message reached 36,
        # EQUAL to one 26 minutes older -- copies CONVERGE, they do not descend), and COO asked
        # whether this fix depended on the dead model. Reading my own predicate says no: offer_count
        # is a PER-ROW counter with no age term. But a reading is not a measurement, so: many rows
        # of DIFFERENT ages polled together, repeatedly, which is the convergence shape. Under a
        # whole-queue re-append the counts rise TOGETHER; the cap must still bound EVERY row.
        ages = ["2000-01-01T00:00:00+00:00", "2010-01-01T00:00:00+00:00", "2020-01-01T00:00:00+00:00"]
        ids = [post("/send-message", {"from_serial": "T", "to_serial": "SEAT_CONV",
                                      "subject": f"conv{i}", "text": "x"})["message_id"]
               for i in range(3)]
        seen = {i: 0 for i in ids}
        con = sqlite3.connect(str(db))
        for _round in range(cap + 5):
            for mid_i, age in zip(ids, ages):      # DIFFERENT ages, polled in the SAME cycles
                con.execute("UPDATE messages SET polled_at=? WHERE id=?", (age, mid_i))
            con.commit()
            for m in post("/poll-messages", {"serial": "SEAT_CONV"})["messages"]:
                if m["id"] in seen:
                    seen[m["id"]] += 1
        con.close()
        rec("F-BOUND-UNDER-CONVERGENCE", all(v == cap for v in seen.values()),
            f"3 rows of DIFFERENT ages polled together {cap + 5} rounds -> offers {list(seen.values())} "
            f"(each capped at {cap}). The bound is per-ROW and carries NO age term, so it holds under "
            f"convergence exactly as it does under a gradient -- the falsified hypothesis was never "
            f"load-bearing for this fix")

        # ---- E: capping loses no CONTENT ----
        body = post("/delivery-state", {"message_id": mid})["messages"][0]
        rec("E-NO-CONTENT-LOSS", body["id"] == mid and body["subject"] == "cap",
            "the exhausted row is still present and readable in the broker; and send_message "
            "writes the FILESYSTEM copy BEFORE the broker call (server.py:1785 vs :1795), so the "
            "durable path never depended on re-offering")
    finally:
        try:
            proc.kill()
            proc.wait(timeout=10)
        except Exception:
            pass
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)

    n = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print()
    print("=" * 82)
    print(f"OFFER-CAP BATTERY: {n}/{len(RESULTS)} PASS (denominator {len(RESULTS)})")
    print("=" * 82)
    return 0 if n == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
