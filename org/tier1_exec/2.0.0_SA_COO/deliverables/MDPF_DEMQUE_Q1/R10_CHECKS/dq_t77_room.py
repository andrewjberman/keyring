"""MDPF_DEMQUE DQ-t-77 criterion AC2 (read-only, no network, no vendor): the drawer's own sweep read on the REAL allowance file.
SWEEP-OK when, run from the worktree root:
  (1) `standing_drawer.py --task-name --sweep` prints mdpf-demque-sweep-daily (the builder's name);
  (2) `standing_drawer.py --room --sweep --day 2026-10-19` (a MONDAY, a trading day) with an EMPTY actuals ledger and a budget directory holding an
      EMPTY bbg_budget_2026-10-19.jsonl prints one JSON line with pass "sweep", trading_day true and daily_total_left 2500000;
  (3) the same with NO budget file for that day prints daily_total_left 0 and reason PRODUCTION_SPEND_UNREAD (fail closed).
Else SWEEP-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

DRAWER = os.path.join("data", "mdpf", "scripts", "demque", "standing_drawer.py")
DAY = "2026-10-19"


def bad(why: str) -> int:
    print("SWEEP-BAD " + why)
    return 1


def run(args, budget_dir, tmp):
    env = dict(os.environ)
    env["RIVALFUNDS_BBG_BUDGET_DIR"] = budget_dir
    env["OPAL_DEMQUE_HOME"] = os.path.join(tmp, "home")
    r = subprocess.run([sys.executable, DRAWER, *args], capture_output=True, text=True, timeout=100, check=False, env=env)
    if r.returncode != 0 or not r.stdout.strip():
        raise RuntimeError("standing_drawer %s rc=%d: %s" % (" ".join(args), r.returncode, (r.stderr or r.stdout)[-300:]))
    return r.stdout.strip().splitlines()[-1]


def main() -> int:
    try:
        with tempfile.TemporaryDirectory() as tmp:
            name = run(["--task-name", "--sweep"], os.path.join(tmp, "b0"), tmp)
            if name.strip() != "mdpf-demque-sweep-daily":
                return bad("--task-name --sweep printed %r" % name)
            actuals = os.path.join(tmp, "no_actuals.jsonl")
            b1 = os.path.join(tmp, "b1")
            os.makedirs(b1)
            open(os.path.join(b1, "bbg_budget_%s.jsonl" % DAY), "w").close()
            full = json.loads(run(["--room", "--sweep", "--day", DAY, "--actuals", actuals], b1, tmp))
            if full.get("pass") != "sweep" or full.get("trading_day") is not True or full.get("daily_total_left") != 2500000:
                return bad("empty ledger read %s" % json.dumps(full, sort_keys=True))
            b2 = os.path.join(tmp, "b2")
            os.makedirs(b2)
            none = json.loads(run(["--room", "--sweep", "--day", DAY, "--actuals", actuals], b2, tmp))
            if none.get("daily_total_left") != 0 or none.get("reason") != "PRODUCTION_SPEND_UNREAD":
                return bad("absent ledger read %s" % json.dumps(none, sort_keys=True))
    except Exception as exc:  # a failed read is BAD, never an error
        return bad("%s: %s" % (type(exc).__name__, exc))
    print("SWEEP-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
