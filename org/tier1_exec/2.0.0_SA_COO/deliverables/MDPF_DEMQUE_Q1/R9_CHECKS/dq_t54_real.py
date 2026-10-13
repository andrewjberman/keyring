"""MDPF_DEMQUE round 9, DQ-t-54 criterion AC2 (read only, no vendor call, writes only temp ledger directories it creates).

`standing_drawer.py --carry-over --day D [--budget-dir DIR]` prints ONE JSON line
{"day", "ceiling", "trading_days": [...], "spent": {date: n}, "carried_over", "room", "claim"}.

Arm 2: an empty budget directory reads carried_over 0, claim "absent", room == ceiling.
Arm 1: a temp directory holds one JSON-lines ledger per UTC day for the five trading days between the previous fire day (Sun 2026-10-11) and the fire day (Sat 2026-10-17):
production spends 1,000 on Monday, ceiling + 500 on Wednesday and 0 on the other three. The line must read
carried_over == (ceiling - 1000) + 0 + ceiling + ceiling (Wednesday overspent carries 0, never negative) and room == ceiling + carried_over, claim not "absent".
Arm 3: the REAL default directory on this device (no site Z ledger here) reads carried_over 0 with claim "absent" and does not raise.
CARRY-REAL-OK; else CARRY-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "standing_drawer.py")
FIRE_DAY = "2026-10-17"


def _bad(why):
    print("CARRY-REAL-BAD " + why)
    return 1


def _run(args):
    r = subprocess.run([sys.executable, TOOL, "--carry-over", "--day", FIRE_DAY] + args,
                       capture_output=True, text=True, timeout=55, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip())
    return json.loads(ls[-1]), ""


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    empty = tempfile.mkdtemp(prefix="dq_t54_empty_")
    a, e = _run(["--budget-dir", empty])
    if a is None:
        return _bad("arm2 " + e)
    print("arm2 empty dir: carried_over=%s claim=%s room=%s ceiling=%s" % (a.get("carried_over"), a.get("claim"), a.get("room"), a.get("ceiling")))
    ceil = a.get("ceiling")
    if not (isinstance(ceil, int) and ceil > 0 and a.get("carried_over") == 0 and a.get("claim") == "absent" and a.get("room") == ceil):
        return _bad("arm2 expected carried_over 0, claim absent, room == ceiling")
    d = tempfile.mkdtemp(prefix="dq_t54_led_")
    spends = {"2026-10-12": 1000, "2026-10-13": 0, "2026-10-14": ceil + 500, "2026-10-15": 0, "2026-10-16": 0}
    for day, n in spends.items():
        with open(os.path.join(d, "bbg_budget_%s.jsonl" % day), "w", encoding="utf-8") as fh:
            if n:
                fh.write(json.dumps({"at": day + "T11:00:00Z", "mode": "daily", "rows": n, "batch_id": "t54"}) + "\n")
    b, e = _run(["--budget-dir", d])
    if b is None:
        return _bad("arm1 " + e)
    expect = (ceil - 1000) + 0 + ceil + ceil
    print("arm1 synthetic ledger: carried_over=%s expected=%s room=%s claim=%s" % (b.get("carried_over"), expect, b.get("room"), b.get("claim")))
    if b.get("carried_over") != expect or b.get("room") != ceil + expect or b.get("claim") == "absent":
        return _bad("arm1 carried_over/room mismatch")
    c, e = _run([])
    if c is None:
        return _bad("arm3 " + e)
    print("arm3 real default dir: carried_over=%s claim=%s" % (c.get("carried_over"), c.get("claim")))
    if c.get("carried_over") != 0 or c.get("claim") != "absent":
        return _bad("arm3 expected 0 and absent on a device with no site Z ledger")
    print("CARRY-REAL-OK carried over %d cells into the %s fire; a missing ledger carries 0 and says so" % (expect, FIRE_DAY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
