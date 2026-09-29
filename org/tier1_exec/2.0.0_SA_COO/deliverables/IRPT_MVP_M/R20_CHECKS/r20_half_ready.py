"""Round 20 (~M) half-readiness check (IBM20-202-AC3, IBM20-203-AC3): the named never-widen half request exists,
has no {{slot}} left, and carries the act, the blast radius with a local candidate diff, and the rollback per key.

Usage: python r20_half_ready.py <half path>. Run from the repo (or worktree) root. Prints HALF-READY or NOT-READY.
"""
import os
import re
import sys

NEEDED = ("## The act", "## Blast radius", "Rollback per key", "candidate")


def main():
    if len(sys.argv) != 2:
        print("NOT-READY: usage r20_half_ready.py <half path>")
        return 1
    path = sys.argv[1]
    if not os.path.exists(path):
        print("NOT-READY: %s absent" % path)
        return 1
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    slots = re.findall(r"\{\{[^}]*\}\}", text)
    missing = [n for n in NEEDED if n not in text]
    if slots or missing:
        print("NOT-READY: %d slot(s), missing %s" % (len(slots), missing))
        return 1
    print("HALF-READY %s" % os.path.basename(path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
