"""MDPF_HEALGAP round 2: a Terraform file is fmt-clean (`terraform fmt -check`, offline, no init).

  python hg_tf_fmt.py <file>   -> FMT-OK or FMT-BAD <reason>
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys


def main(path: str) -> int:
    if not os.path.isfile(path):
        print("FMT-BAD no file " + path)
        return 1
    tf = shutil.which("terraform")
    if not tf:
        print("FMT-BAD terraform not on PATH")
        return 1
    r = subprocess.run([tf, "fmt", "-check", "-diff", path], capture_output=True, text=True, timeout=60, check=False,
                       env=dict(os.environ, CHECKPOINT_DISABLE="1"))
    if r.returncode != 0:
        print((r.stdout + r.stderr)[-1500:])
        print("FMT-BAD rc=%d" % r.returncode)
        return 1
    print("FMT-OK " + path)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: hg_tf_fmt.py <file>")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
