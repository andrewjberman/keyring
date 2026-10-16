#!/usr/bin/env python3
"""A2 BACKFILL_CAP 50 to 62: the worker's commit moves exactly one line in exactly one pipeline file.

Run from the worker's worktree root. Compares HEAD~1 to HEAD (the worker makes ONE commit):
  - integrations/bloomberg/pipeline/etf_daily_pull.py: 1 insertion, 1 deletion, the new line is `BACKFILL_CAP = 62`;
  - every other changed path is in ALLOWED (the order's own file and the worker's proof_of_spec instance), never code.
Prints A2-DIFF-OK on a pass; A2-DIFF-BAD <reason> otherwise. Plain ASCII, stdlib only, terminates.
"""
import subprocess
import sys

TARGET = "integrations/bloomberg/pipeline/etf_daily_pull.py"
ALLOWED_PREFIXES = (
    "org/missions/D8/MDPF/MDPF_SECHIST/task-orders/",
    "org/missions/D8/MDPF/MDPF_SECHIST/deliverables/",
    "org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/",
)


def git(*a):
    r = subprocess.run(["git"] + list(a), capture_output=True, text=True, timeout=60)
    return r.returncode, r.stdout


def main():
    rc, names = git("diff", "--name-only", "HEAD~1", "HEAD")
    if rc != 0:
        print("A2-DIFF-BAD git diff rc=%d" % rc)
        return 1
    paths = [p for p in names.splitlines() if p]
    if TARGET not in paths:
        print("A2-DIFF-BAD target not changed (changed=%r)" % paths)
        return 1
    extra = [p for p in paths if p != TARGET and not p.startswith(ALLOWED_PREFIXES)]
    if extra:
        print("A2-DIFF-BAD other paths changed: %r" % extra)
        return 1
    rc, num = git("diff", "--numstat", "HEAD~1", "HEAD", "--", TARGET)
    cols = num.split()
    if rc != 0 or cols[:2] != ["1", "1"]:
        print("A2-DIFF-BAD numstat=%r (want 1 insertion, 1 deletion)" % num.strip())
        return 1
    rc, patch = git("diff", "-U0", "HEAD~1", "HEAD", "--", TARGET)
    adds = [ln[1:] for ln in patch.splitlines() if ln.startswith("+") and not ln.startswith("+++")]
    dels = [ln[1:] for ln in patch.splitlines() if ln.startswith("-") and not ln.startswith("---")]
    if adds != ["BACKFILL_CAP = 62"] or dels != ["BACKFILL_CAP = 50"]:
        print("A2-DIFF-BAD lines add=%r del=%r" % (adds, dels))
        return 1
    print("A2-DIFF-OK paths=%d" % len(paths))
    return 0


if __name__ == "__main__":
    sys.exit(main())
