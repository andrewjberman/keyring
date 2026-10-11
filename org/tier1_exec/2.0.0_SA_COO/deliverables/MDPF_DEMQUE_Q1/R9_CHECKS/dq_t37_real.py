"""MDPF_DEMQUE round 9, DQ-t-37 criterion AC2 (REAL served store, S3 read only, nothing written): `extend_frontier.py --plan --today <tomorrow>`
(the local date plus one day, computed here) exits non-zero, prints no JSON plan and names the local date; `--plan` with no `--today` and
`--plan --today <the local date>` both exit 0 and print the same frontier. FUT-REAL-OK; else FUT-REAL-BAD <why>.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "extend_frontier.py")


def _run(*extra):
    return subprocess.run([sys.executable, TOOL, "--plan"] + list(extra), capture_output=True, text=True, timeout=110, check=False)


def _plan(r):
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    return json.loads(lines[-1]) if lines else None


def main() -> int:
    if not os.path.isfile(TOOL):
        print("FUT-REAL-BAD no file " + TOOL)
        return 1
    today = dt.date.today()
    tomorrow = _run("--today", (today + dt.timedelta(days=1)).isoformat())
    default = _run()
    same = _run("--today", today.isoformat())
    text = tomorrow.stdout + tomorrow.stderr
    print("tomorrow: rc=%d %s" % (tomorrow.returncode, text.strip().splitlines()[-1][:160] if text.strip() else ""))
    a, b = _plan(default), _plan(same)
    print("default: rc=%d frontier=%s; today: rc=%d frontier=%s" % (default.returncode, a and a.get("frontier"), same.returncode, b and b.get("frontier")))
    arms = {
        "tomorrow_refused": tomorrow.returncode != 0 and _plan(tomorrow) is None,
        "names_local_date": today.isoformat() in text,
        "default_plans": default.returncode == 0 and a is not None,
        "today_equals_default": same.returncode == 0 and b is not None and b.get("frontier") == a.get("frontier"),
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        print("FUT-REAL-BAD arms=" + ",".join(bad))
        return 1
    print("FUT-REAL-OK a --today after the local date is refused; today and the default plan the same frontier")
    return 0


if __name__ == "__main__":
    sys.exit(main())
