"""MDPF_DEMQUE DQ-t-75 criterion AC2 (the difference control, no network): the drawer's existing tests, the surface-room tests and the DQ-t-74 outcome tests still pass unedited.
EMPTY-OK when `pytest` over test_demque_standing_drawer.py, test_demque_standing_drawer_close.py and test_demque_surface_room.py exits 0 with no failure;
else EMPTY-BAD <tail>. Run from the worktree root."""
from __future__ import annotations

import os
import subprocess
import sys

HOME = os.path.join("data", "mdpf", "scripts", "demque")
FILES = ["test_demque_standing_drawer.py", "test_demque_standing_drawer_close.py", "test_demque_surface_room.py", "test_demque_outcome_per_request.py"]


def main() -> int:
    missing = [f for f in FILES if not os.path.isfile(os.path.join(HOME, f))]
    if missing:
        print("EMPTY-BAD no file " + ",".join(missing))
        return 1
    env = dict(os.environ)
    env.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", *FILES], capture_output=True, text=True,
                       timeout=110, check=False, cwd=HOME, env=env)
    out = (r.stdout + r.stderr).strip().splitlines()
    print("\n".join(out[-4:]))
    if r.returncode != 0:
        print("EMPTY-BAD pytest rc=%d" % r.returncode)
        return 1
    print("EMPTY-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
