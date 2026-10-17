"""MDPF_DEMQUE DQ-t-69 criterion AC3 (read-only, no network, no vendor): the drawer's own read of the day's room, `standing_drawer.py --room --day D`,
on the REAL allowance file and the real requests folder, with an EMPTY actuals ledger and an EMPTY budget directory (so nothing is drawn and no carry-over).
SURF-OK when the one JSON line printed (last stdout line) for the Saturday 2026-10-17 reads: trading_day false, untagged 5858, surfaces A 350000 /
B 1500000 / C 400000 / D 100000 / E 150000, daily_total_left 2500000; AND for the Monday 2026-10-19 (a trading day, the drawer's TRADING_DAY gate)
reads trading_day true, untagged 0, every surface 0. Else SURF-BAD <why>. Run from the worktree root.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

DRAWER = os.path.join("data", "mdpf", "scripts", "demque", "standing_drawer.py")
SURF = {"A": 350000, "B": 1500000, "C": 400000, "D": 100000, "E": 150000}


def bad(why: str) -> int:
    print("SURF-BAD " + why)
    return 1


def room(day: str, tmp: str) -> dict:
    env = dict(os.environ)
    env["RIVALFUNDS_BBG_BUDGET_DIR"] = os.path.join(tmp, "budget")
    os.makedirs(env["RIVALFUNDS_BBG_BUDGET_DIR"], exist_ok=True)
    r = subprocess.run([sys.executable, DRAWER, "--room", "--day", day, "--actuals", os.path.join(tmp, "no_actuals.jsonl")],
                       capture_output=True, text=True, timeout=100, check=False, env=env)
    if r.returncode != 0 or not r.stdout.strip():
        raise RuntimeError("standing_drawer --room rc=%d: %s" % (r.returncode, (r.stderr or r.stdout)[-300:]))
    return json.loads(r.stdout.strip().splitlines()[-1])


def main() -> int:
    try:
        with tempfile.TemporaryDirectory() as tmp:
            sat, mon = room("2026-10-17", tmp), room("2026-10-19", tmp)
    except Exception as exc:  # a failed read is BAD, never an error
        return bad("%s: %s" % (type(exc).__name__, exc))
    if sat.get("trading_day") is not False or sat.get("untagged") != 5858 or sat.get("surfaces") != SURF or sat.get("daily_total_left") != 2500000:
        return bad("Saturday room reads %s" % json.dumps(sat, sort_keys=True))
    if mon.get("trading_day") is not True or mon.get("untagged") != 0 or mon.get("surfaces") != {k: 0 for k in SURF}:
        return bad("Monday room reads %s" % json.dumps(mon, sort_keys=True))
    print("SURF-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
