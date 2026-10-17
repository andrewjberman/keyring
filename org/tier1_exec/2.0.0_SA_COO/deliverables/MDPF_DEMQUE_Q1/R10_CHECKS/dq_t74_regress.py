"""MDPF_DEMQUE DQ-t-74 criterion AC2 (the difference control, no network): the drawer's existing tests and the surface-room tests still pass unedited.
OUT-OK when `pytest` over test_demque_standing_drawer.py, test_demque_standing_drawer_close.py and test_demque_surface_room.py exits 0 with no failure;
else OUT-BAD <tail>. Run from the worktree root."""
from __future__ import annotations

import os
import subprocess
import sys

HOME = os.path.join("data", "mdpf", "scripts", "demque")
FILES = ["test_demque_standing_drawer.py", "test_demque_standing_drawer_close.py", "test_demque_surface_room.py"]


def main() -> int:
    missing = [f for f in FILES if not os.path.isfile(os.path.join(HOME, f))]
    if missing:
        print("OUT-BAD no file " + ",".join(missing))
        return 1
    env = dict(os.environ)
    env.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", *FILES], capture_output=True, text=True,
                       timeout=110, check=False, cwd=HOME, env=env)
    out = (r.stdout + r.stderr).strip().splitlines()
    print("\n".join(out[-4:]))
    if r.returncode != 0:
        print("OUT-BAD pytest rc=%d" % r.returncode)
        return 1
    print("OUT-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
