"""MDPF_SECHIST round 5, rows S2 / W2-S1: whole test files run green from the worktree root with no extra path set up.

Usage: python r5_suites_clean.py LABEL file1 [file2 ...]   (run from the worktree root)
Each file runs as its own pytest process (no color, no cache). Last line: <LABEL>-SUITES-OK files=<n>   or
<LABEL>-SUITES-BAD failing=<file:rc,...>.
"""
from __future__ import annotations

import os
import subprocess
import sys


def main(argv: list[str]) -> int:
    label, files = argv[1], argv[2:]
    env = {k: v for k, v in os.environ.items() if k not in ("FORCE_COLOR", "PY_COLORS", "PYTHONPATH")}
    bad = []
    for f in files:
        run = subprocess.run([sys.executable, "-m", "pytest", "-q", "--color=no", "-p", "no:cacheprovider", f],
                             capture_output=True, text=True, env=env)
        tail = (run.stdout + run.stderr).strip().splitlines()[-1:] or [""]
        print(f + " rc=" + str(run.returncode) + " | " + tail[0])
        if run.returncode != 0:
            bad.append(f + ":" + str(run.returncode))
    if bad:
        print(label + "-SUITES-BAD failing=" + ",".join(bad))
        return 1
    print(label + "-SUITES-OK files=" + str(len(files)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
