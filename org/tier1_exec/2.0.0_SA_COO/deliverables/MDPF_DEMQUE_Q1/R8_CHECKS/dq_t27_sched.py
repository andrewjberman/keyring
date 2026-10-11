"""MDPF_DEMQUE round 8, DQ-t-27 criterion AC2 (run at site Z after the registration): the standing drawer's schedule and its registered task.
(a) `standing_drawer.py --schedule --from 2026-10-12 --days 14` prints exactly the non-trading days of 2026-10-12..2026-10-25
(10-17, 10-18, 10-24, 10-25), one fire each, taken from lib/trading_calendar.py by this check's own call; (b) `--task-name` prints the
task's name and `schtasks /Query /TN <name>` finds it; (c) the NEGATIVE arm: `--apply --day 2026-10-12` (a trading day, scratch
--output and --actuals) draws 0 cells and reports TRADING_DAY without signing in. DRSCH-OK; else DRSCH-BAD <why>.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, ".")
DRAWER = os.path.join("data", "mdpf", "scripts", "demque", "standing_drawer.py")


def _run(cmd, timeout=100):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
    return r.returncode, r.stdout, r.stderr


def _json_line(text):
    lines = [ln for ln in text.splitlines() if ln.strip().startswith("{")]
    return json.loads(lines[-1]) if lines else None


def _bad(why):
    print("DRSCH-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(DRAWER):
        return _bad("no file " + DRAWER)
    from lib.trading_calendar import is_trading_day
    start = dt.date(2026, 10, 12)
    want = [(start + dt.timedelta(days=i)).isoformat() for i in range(14) if not is_trading_day(start + dt.timedelta(days=i))]
    rc, out, err = _run([sys.executable, DRAWER, "--schedule", "--from", "2026-10-12", "--days", "14"])
    got = _json_line(out)
    if rc != 0 or not got or got.get("fires") != want:
        return _bad("schedule rc=%d want=%s got=%s %s" % (rc, want, got, err[-200:].strip()))
    print("schedule fires: %s" % got["fires"])
    rc, out, err = _run([sys.executable, DRAWER, "--task-name"])
    name = out.strip().splitlines()[-1].strip() if out.strip() else ""
    if rc != 0 or not name:
        return _bad("task-name rc=%d %s" % (rc, err[-200:].strip()))
    qrc, qout, _ = _run(["schtasks", "/Query", "/TN", name, "/FO", "LIST"])
    if qrc != 0:
        return _bad("task %r is not registered (schtasks rc=%d)" % (name, qrc))
    print("task registered: " + name)
    tmp = tempfile.mkdtemp(prefix="drawer_neg_")
    rc, out, err = _run([sys.executable, DRAWER, "--apply", "--day", "2026-10-12", "--output", tmp,
                         "--actuals", os.path.join(tmp, "actuals.jsonl")])
    res = _json_line(out)
    if rc not in (0, 2) or not res or res.get("cells_drawn") != 0 or "TRADING_DAY" not in str(res.get("stop_reason")):
        return _bad("trading-day arm rc=%d result=%s %s" % (rc, res, err[-200:].strip()))
    print("trading-day arm: cells_drawn=0 stop_reason=%s" % res.get("stop_reason"))
    print("DRSCH-OK 4 fires in 14 days, task %s registered, a trading day draws 0" % name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
