"""MDPF_DEMQUE round 9, DQ-t-36 criterion AC2: the guard on the REAL served store (S3 read only, nothing written). `extend_frontier.py --plan
--today 2026-06-30` (a frontier before every file's end, 2026-06-22/23) must exit non-zero, write no JSON plan, and name the store's latest
valid_to in its message; `--plan --today 2026-10-12` must still print a plan ending 2026-10-12. GUARD-REAL-OK; else GUARD-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "extend_frontier.py")


def _run(day):
    return subprocess.run([sys.executable, TOOL, "--plan", "--today", day], capture_output=True, text=True, timeout=110, check=False)


def main() -> int:
    if not os.path.isfile(TOOL):
        print("GUARD-REAL-BAD no file " + TOOL)
        return 1
    early = _run("2026-06-30")
    out = (early.stdout + early.stderr)
    print("early: rc=%d %s" % (early.returncode, out.strip().splitlines()[-1][:200] if out.strip() else ""))
    late = _run("2026-10-12")
    lines = [ln for ln in late.stdout.splitlines() if ln.strip().startswith("{")]
    plan = json.loads(lines[-1]) if lines else {}
    print("late: rc=%d end=%s symbols=%s" % (late.returncode, plan.get("end"), plan.get("symbols")))
    arms = {
        "early_refused": early.returncode != 0 and not any(ln.strip().startswith("{") for ln in early.stdout.splitlines()),
        "early_names_valid_to": "2026-06-2" in out,
        "late_plans": late.returncode == 0 and plan.get("end") == "2026-10-12" and plan.get("symbols") == 141,
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        print("GUARD-REAL-BAD arms=" + ",".join(bad))
        return 1
    print("GUARD-REAL-OK a frontier before the store's end is refused; 2026-10-12 plans 141 symbols")
    return 0


if __name__ == "__main__":
    sys.exit(main())
