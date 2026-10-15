#!/usr/bin/env python3
"""test_worktree_gc_own_commit.py -- CT-af-1: a worktree is MERGED or CLEAN only with an own commit (WIP skeleton).

Standard library, temporary repositories only. Work in progress: arms are added below.
"""
from __future__ import annotations

import sys

ARMS: list[tuple[str, bool]] = []


def main() -> int:
    passed = sum(1 for _, r in ARMS if r)
    print(f"WORKTREE-GC-OWN-COMMIT arms={passed}/{len(ARMS)} ok={passed == len(ARMS) and len(ARMS) > 0}")
    return 0 if passed == len(ARMS) and len(ARMS) > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
