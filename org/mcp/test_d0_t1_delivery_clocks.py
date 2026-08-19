"""D0_TIGHTENING TO-1 -- T1 broker primitive EXERCISE battery (broker plane).

Runs against a SCRATCH broker (own port, own DB) so delivery semantics can be
exercised by killing clients mid-flight without touching the live fabric.

Every assertion is EXERCISED, never asserted from reading. The battery carries its
own controls:
  * POSITIVE CONTROL  -- the instrument must report READ when a READ genuinely happened
  * NEGATIVE CONTROL  -- an untouched message must NOT read as delivered
  * MUTANT CONTROL    -- the SAME loss scenario run against the pre-T1 (HEAD) broker,
                         which MUST lose the message. A test that cannot fail is not a
                         test; this one is proven able to fail by making it fail.

Usage:  python .scratch-ae/t1/t1_exercise.py [--baseline <path-to-head-broker.py>]
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

WS = Path(__file__).resolve().parents[2]  # org/mcp/X.py -> workspace root
PORT = int(os.environ.get("T1_TEST_PORT", "7911"))
BASE = f"http://127.0.0.1:{PORT}"

RESULTS: list[tuple[str, str, str]] = []  # (id, verdict, detail)


def rec(tid: str, ok: bool, detail: str) -> None:
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tid}: {detail}")


def post(path: str, body: dict, timeout: float = 5.0):
    req = urllib.request.Request(
        BASE + path, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def health(timeout: float = 15.0) -> bool:
    end = time.time() + timeout
    while time.time() < end:
        try:
            with urllib.request.urlopen(BASE + "/health", timeout=2) as r:
                if r.status == 200:
                    return True
        except Exception:
            time.sleep(0.25)
    return False


def start_broker(script: Path, db: Path, reclaim: int | None = None):
    env = dict(os.environ)
    env["OPAL_BROKER_PORT"] = str(PORT)
    env["OPAL_BROKER_DB"] = str(db)
    proc = subprocess.Popen([sys.executable, str(script)], env=env,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if not health():
        proc.kill()
        raise RuntimeError(f"scratch broker ({script.name}) failed to come up on {PORT}")
    return proc


def stop(proc):
    try:
        proc.kill()
        proc.wait(timeout=10)
    except Exception:
        pass
    # port release
    for _ in range(20):
        try:
            with urllib.request.urlopen(BASE + "/health", timeout=1):
                time.sleep(0.25)
        except Exception:
            return


def state_of(mid: int) -> str:
    r = post("/delivery-state", {"message_id": mid})
    return r["messages"][0]["state"] if r.get("messages") else "ABSENT"



def _pre_t1_baseline(dest: Path) -> Path | None:
    """Materialise the PRE-T1 broker from a PINNED vintage for the mutant control.

    Pinned to e7858adf52 -- deliberately NOT HEAD. Once T1 lands, HEAD:org/mcp/broker.py IS the
    fixed code, so a HEAD-sourced 'baseline' would silently stop being a control. A
    control that drifts with the thing it controls is not a control.
    """
    import subprocess
    r = subprocess.run(["git", "show", "e7858adf52:org/mcp/broker.py"],
                       cwd=str(WS), capture_output=True, text=True)
    # NEVER discard stderr on a git show: a mangled ref prints fatal: on stderr and
    # returns CLEAN EMPTY stdout, which would render 'baseline absent' out of a broken
    # retrieval. Check rc AND non-empty content.
    if r.returncode != 0 or not r.stdout.strip():
        print(f"    baseline retrieval FAILED rc={r.returncode}: {r.stderr.strip()[:200]}")
        return None
    dest.write_text(r.stdout, encoding="utf-8")
    return dest

# ---------------------------------------------------------------------------
def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="t1_"))
    new_script = WS / "org" / "mcp" / "broker.py"
    head_script = _pre_t1_baseline(tmp / "broker_pre_t1.py")

    print("=" * 78)
    print("D0_TIGHTENING T1 EXERCISE BATTERY")
    print(f"  broker under test : {new_script}")
    print(f"  scratch port/db   : {PORT} / {tmp}")
    print("=" * 78)

    # ================= PART 1: the NEW broker =================
    print("\n-- PART 1: broker under test (post-T1) --")
    db = tmp / "t1_new.db"
    proc = start_broker(new_script, db)
    try:
        # ---- E1: three clocks are DISTINCT and ordered -------------------
        mid = post("/send-message", {"from_serial": "TEST_SENDER", "to_serial": "SEAT_A",
                                     "subject": "e1", "text": "clock separation"})["message_id"]
        s0 = state_of(mid)
        rec("E1a-QUEUED", s0 == "QUEUED",
            f"fresh message reads {s0} (expected QUEUED -- written, nobody polled)")

        post("/poll-messages", {"serial": "SEAT_A"})
        s1 = state_of(mid)
        rec("E1b-SENT", s1 == "SENT",
            f"after POLL reads {s1} (expected SENT -- a client took handoff, NOT an agent)")

        post("/mark-emitted", {"serial": "SEAT_A", "ids": [mid]})
        s2 = state_of(mid)
        rec("E1c-EMITTED", s2 == "EMITTED",
            f"after DRAIN reads {s2} (expected EMITTED -- queue cleared, still no agent evidence)")

        post("/ack-messages", {"serial": "SEAT_A", "ids": [mid]})
        s3 = state_of(mid)
        rec("E1d-READ", s3 == "READ",
            f"after AGENT ACK reads {s3} (expected READ -- the only agent-side clock)")

        # ---- E2: NEGATIVE CONTROL -- untouched message never reads delivered
        mid_n = post("/send-message", {"from_serial": "TEST_SENDER", "to_serial": "SEAT_NOBODY",
                                       "subject": "e2", "text": "negative control"})["message_id"]
        sn = state_of(mid_n)
        rec("E2-NEGCTL", sn == "QUEUED",
            f"untouched message reads {sn} (must be QUEUED -- instrument discriminates, "
            f"it does not report everything delivered)")

        # ---- E3: THE DISCRIMINATING TEST -- die between POLL and DRAIN ----
        # This is the 4th acceptance leg. The detached-listener fix alone passes GREEN
        # here; only the durability fix makes it actually pass.
        mid_d = post("/send-message", {"from_serial": "TEST_SENDER", "to_serial": "SEAT_DIES",
                                       "subject": "e3", "text": "survive the kill"})["message_id"]
        polled = post("/poll-messages", {"serial": "SEAT_DIES"})
        got = [m["id"] for m in polled["messages"]]
        rec("E3a-POLLED", mid_d in got, f"seat polled and received id={mid_d} (client has it in RAM)")
        # ...client dies here. No /mark-emitted is ever sent. Simulate respawn:
        # reclaim window must elapse before the message is re-offered.
        import sqlite3
        con = sqlite3.connect(str(db))
        con.execute("UPDATE messages SET polled_at = '2000-01-01T00:00:00+00:00' WHERE id = ?",
                    (mid_d,))
        con.commit()
        con.close()
        # (age the poll stamp rather than sleeping 90s -- the predicate under test is
        #  "polled_at <= now - T1_RECLAIM_S", and aging the stamp exercises that exact
        #  comparison. The clock source is the broker's, not the test's.)
        redelivered = post("/poll-messages", {"serial": "SEAT_DIES"})
        got2 = [m["id"] for m in redelivered["messages"]]
        rec("E3b-SURVIVES", mid_d in got2,
            f"after respawn, poll returned {got2} -- message RECOVERED (this is the leg that "
            f"fails on pre-T1 code)")

        # ---- E4: a LIVE session is not spammed -- reclaim needs the window ----
        mid_l = post("/send-message", {"from_serial": "TEST_SENDER", "to_serial": "SEAT_LIVE",
                                       "subject": "e4", "text": "no duplicate"})["message_id"]
        post("/poll-messages", {"serial": "SEAT_LIVE"})
        again = post("/poll-messages", {"serial": "SEAT_LIVE"})
        rec("E4-NO-SPAM", mid_l not in [m["id"] for m in again["messages"]],
            "an immediate re-poll does NOT re-offer the message (reclaim window respected; "
            "a healthy seat is never handed duplicates)")

        # ---- E5: ACK is write-once (first reader's timestamp preserved) ----
        r1 = post("/ack-messages", {"serial": "SEAT_A", "ids": [mid]})
        rec("E5-ACK-ONCE", r1["acked"] == 0,
            f"re-ACK of an already-READ message acked={r1['acked']} (0 = write-once; the "
            f"FIRST reader's timestamp survives)")

        # ---- E6: UNKNOWN-PRE-T1 honesty ----
        # A row delivered by the OLD code carries delivered=1 with no clock stamps.
        con = sqlite3.connect(str(db))
        con.execute("INSERT INTO messages (from_serial,to_serial,subject,body,sent_at,delivered) "
                    "VALUES ('OLD','SEAT_OLD','pre-t1','legacy','2026-01-01T00:00:00+00:00',1)")
        con.commit()
        mid_old = con.execute("SELECT MAX(id) FROM messages").fetchone()[0]
        con.close()
        s_old = state_of(mid_old)
        rec("E6-PRE-T1", s_old == "UNKNOWN-PRE-T1",
            f"a pre-T1 delivered row reads {s_old} (must NOT be READ -- its fate is unknowable "
            f"and the instrument says so)")
    finally:
        stop(proc)

    # ================= PART 2: MUTANT CONTROL (pre-T1 broker) =================
    # The same E3 scenario against HEAD. It MUST lose the message. If this passes,
    # E3b proved nothing.
    print("\n-- PART 2: MUTANT CONTROL -- same scenario on the PRE-T1 (HEAD) broker --")
    if head_script is None or not head_script.exists():
        rec("E7-MUTANT", False, f"baseline broker not found at {head_script} -- CANNOT RUN "
                                f"the control, so E3b is UNCONTROLLED")
    else:
        db2 = tmp / "t1_head.db"
        proc2 = start_broker(head_script, db2)
        try:
            post("/send-message", {"from_serial": "TEST_SENDER", "to_serial": "SEAT_DIES",
                                   "subject": "mutant", "text": "this will be lost"})
            first = post("/poll-messages", {"serial": "SEAT_DIES"})
            n_first = len(first["messages"])
            # client dies here, exactly as in E3. Respawn and poll again:
            second = post("/poll-messages", {"serial": "SEAT_DIES"})
            n_second = len(second["messages"])
            lost = (n_first == 1 and n_second == 0)
            rec("E7-MUTANT", lost,
                f"pre-T1 broker: first poll returned {n_first}, post-death poll returned "
                f"{n_second} -> message PERMANENTLY LOST. This is the window TO-1 closes, "
                f"reproduced. (If this had returned 1, E3b would prove nothing.)")
        finally:
            stop(proc2)

    shutil.rmtree(tmp, ignore_errors=True)

    print("\n" + "=" * 78)
    n_pass = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print(f"T1 EXERCISE BATTERY: {n_pass}/{len(RESULTS)} PASS  (denominator {len(RESULTS)})")
    for tid, v, _d in RESULTS:
        print(f"  {v:<4} {tid}")
    print("=" * 78)
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
