#!/usr/bin/env python3
"""proof_instance_select.py -- which proof instance of an order a gate grades.

Context: OPLGTW round 42 item 6; 1.0.0_SA_CTO~Z msg 35688 (REC YES, the CVO adjudicates). Finding:
org/tier0_exec/0.0.0_AB_MSTR/deliverables/PROOF_INSTANCE_SELECTION_FINDING_20261018.md.

  * to-pipeline-gate.py check_complete_flip grades the FIRST match of an UNSORTED glob of
    deliverables/*/<stem>.proof_of_spec.json -- not the newest.
  * round-close-check.py proof_state returns OK at the FIRST instance that passes, so an older VALID instance can mask a
    newer FAILING one.

THIS MODULE IS INERT UNTIL ARMED. Unarmed, select() returns its input unchanged, so both gates behave exactly as they did.
ARMED (one of):
  - the flag file  org/mcp/proof-newest-instance.enforce  exists under the repo root, or
  - the environment variable PROOF_NEWEST_INSTANCE=1  (=0 forces OFF even when the file exists; for tests and a drill).
To disarm: delete the file. No other state.

Armed, with two or more candidate instances, select() returns the ONE newest, by this key (greatest wins):
  1. an instance with uncommitted work (untracked, staged or modified in the tree) is the newest: it is the one being written
     now, and a flip that adds a fresh instance in the same commit must grade it;
  2. the latest commit time of the instance file (git log -1 --format=%ct -- <path>);
  3. the numeric N of the holding folder's ~N suffix (so ~10 beats ~9, which a name sort gets wrong);
  4. the path, so the choice is deterministic.
COST: one `git log` (and one `git status`) per candidate, only when armed and there is more than one candidate.
NON-APPLICATION: a single instance; an order whose <proof_of_spec> block pins exactly one literal instance path (that path
never reaches select()).
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

FLAG = "org/mcp/proof-newest-instance.enforce"
ENV = "PROOF_NEWEST_INSTANCE"


def armed(root: str, env=None) -> bool:
    e = (env if env is not None else os.environ).get(ENV, "").strip()
    if e in ("0", "1"):
        return e == "1"
    return os.path.isfile(os.path.join(root, *FLAG.split("/")))


def _git(root: str, args: list) -> str:
    r = subprocess.run(["git", "-C", root] + args, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       timeout=60)
    return r.stdout if r.returncode == 0 else ""


def _suffix(path: str) -> int:
    m = re.search(r"~(\d+)$", os.path.basename(os.path.dirname(path.replace("\\", "/"))))
    return int(m.group(1)) if m else -1


def key(root: str, path: str) -> tuple:
    """(uncommitted, commit_time, ~N, path): the instance with the greatest key is the newest."""
    uncommitted = bool(_git(root, ["status", "--porcelain", "--", path]).strip())
    ct = _git(root, ["log", "-1", "--format=%ct", "--", path]).strip()
    return (1 if uncommitted else 0, int(ct) if ct.isdigit() else 0, _suffix(path), path.replace("\\", "/"))


def ranked(root: str, paths: list) -> list:
    """Every path, newest first, with its key (for the census and the tests)."""
    return sorted(((key(root, p), p) for p in paths), key=lambda kp: kp[0], reverse=True)


def select(root: str, paths: list, env=None) -> list:
    """The paths a gate should grade. Unarmed, or fewer than two: the input, unchanged and in its own order."""
    paths = list(paths)
    if len(paths) < 2 or not armed(root, env):
        return paths
    return [ranked(root, paths)[0][1]]


if __name__ == "__main__":
    # python .tools/proof_instance_select.py <repo root> <path> <path> ...   -> the ranked list, armed or not
    if len(sys.argv) < 3:
        print("usage: proof_instance_select.py <repo root> <instance path> <instance path> ...", file=sys.stderr)
        sys.exit(2)
    root = sys.argv[1]
    print("armed: %s" % armed(root))
    for k, p in ranked(root, sys.argv[2:]):
        print("%s  uncommitted=%d commit_time=%d ~N=%d" % (p, k[0], k[1], k[2]))
