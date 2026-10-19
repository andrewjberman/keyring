"""MDPF_DEMQUE DQ-t-78 criterion AC1 (site Z, read-only): the sweep task is registered as the order says.
TASK-OK when the Windows task named by `standing_drawer.py --task-name --sweep` exists, its schedule is daily, its start time is 4:00:00 PM
(16:00 local; site Z's clock is US Eastern, the same clock the 10:00 ET drawer task uses), and its action runs standing_drawer.py with both --apply
and --sweep. Else TASK-BAD <why>. Run from the repository root at site Z.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

DRAWER = os.path.join("data", "mdpf", "scripts", "demque", "standing_drawer.py")


def bad(why: str) -> int:
    print("TASK-BAD " + why)
    return 1


def main() -> int:
    try:
        n = subprocess.run([sys.executable, DRAWER, "--task-name", "--sweep"], capture_output=True, text=True, timeout=60, check=False)
        name = n.stdout.strip().splitlines()[-1] if n.returncode == 0 and n.stdout.strip() else ""
        if not name:
            return bad("standing_drawer --task-name --sweep rc=%d: %s" % (n.returncode, (n.stderr or n.stdout)[-200:]))
        q = subprocess.run(["schtasks", "/query", "/tn", name, "/v", "/fo", "list"], capture_output=True, text=True, timeout=60, check=False)
        if q.returncode != 0:
            return bad("no task %s: %s" % (name, (q.stderr or q.stdout).strip()[-200:]))
        out = q.stdout
        run_line = " ".join(re.findall(r"Task To Run:\s*(.*)", out))
        if "standing_drawer.py" not in run_line or "--apply" not in run_line or "--sweep" not in run_line:
            return bad("task %s runs %r" % (name, run_line))
        if not re.search(r"Schedule Type:\s*Daily", out):
            return bad("task %s is not a daily schedule" % name)
        if not re.search(r"Start Time:\s*(4:00:00 PM|16:00:00)", out):
            return bad("task %s start time is %r" % (name, re.findall(r"Start Time:\s*(.*)", out)))
    except Exception as exc:  # a failed read is BAD, never an error
        return bad("%s: %s" % (type(exc).__name__, exc))
    print("TASK-OK %s" % name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
