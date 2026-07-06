#!/usr/bin/env python3
"""commit_queue_gc.py -- NFRA_CMTQUE results/dlq garbage-collection.

Reaps the CMTQUE hot store's already-terminal backlog via the SHARED reap contract
(org/mcp/reap_lib.py) -- the SAME policy the broker archival uses, so it can't drift:
  - RESULTS: a client reads its result then deletes it. A client that DIED mid-wait
    ORPHANS its result file -> reaped after the retention floor (its commit already
    landed / was recorded; the result is a stale receipt).
  - DLQ: poison requests (transient-exhausted / corrupt / crash-orphan) -> archived to
    a dated dir (kept for triage), then removed after the retention floor.

NEVER touches requests/ or processing/ (in-flight) -- only results/ + dlq/.
No reclaim step: filesystem unlink frees space immediately (unlike SQLite VACUUM).

Invoked periodically by the commit-worker daemon (bash shells out):
    python .tools/commit_queue_gc.py [--dry-run] [--archive-only] [--retention-hours 24]
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import time
from pathlib import Path

# reap_lib.py is co-located in .tools/ (this file's own dir). The broker consumer
# (org/mcp/archive_messages.py) imports the SAME module via sys.path -> one shared policy.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from reap_lib import ReapSubstrate, reap  # noqa: E402


def queue_root() -> Path:
    gitdir = subprocess.check_output(
        ["git", "rev-parse", "--absolute-git-dir"], text=True
    ).strip()
    return Path(gitdir) / "commit-queue"


def build_substrate(root: Path, retention_hours: float) -> ReapSubstrate:
    results_dir = root / "results"
    dlq_dir = root / "dlq"
    archive_dir = root / "archive"
    gc_log = root / "gc.log"
    cutoff = time.time() - retention_hours * 3600.0

    terminal_dirs = (results_dir, dlq_dir)

    def select_eligible() -> list:
        elig: list = []
        for d in terminal_dirs:
            if not d.is_dir():
                continue
            for f in d.iterdir():
                # skip the atomic-write temp files; only aged, terminal entries
                if f.is_file() and not f.name.startswith(".tmp.") and f.stat().st_mtime < cutoff:
                    elig.append(f)
        return elig

    def total_count() -> int:
        return sum(
            1
            for d in terminal_dirs
            if d.is_dir()
            for f in d.iterdir()
            if f.is_file() and not f.name.startswith(".tmp.")
        )

    def archive(cands: list) -> int:
        # DLQ -> copy to a dated archive dir (poison record). RESULTS -> a gc.log line
        # (the receipt is ephemeral; the commit itself is durable in git). Both count
        # as "archived" so the reap contract's verify(written==eligible) holds and
        # nothing is silently dropped.
        written = 0
        stamped = time.strftime("%Y-%m-%d", time.gmtime())
        dated = archive_dir / stamped
        with open(gc_log, "a", encoding="utf-8") as lg:
            for f in cands:
                if f.parent.name == "dlq":
                    dated.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(str(f), str(dated / f.name))
                    lg.write(f"{stamped} ARCHIVED-DLQ {f.name}\n")
                else:
                    lg.write(f"{stamped} REAPED-ORPHAN-RESULT {f.name}\n")
                written += 1
            lg.flush()
        return written

    def delete(cands: list) -> int:
        d = 0
        for f in cands:
            try:
                f.unlink()
                d += 1
            except OSError:
                pass
        return d

    # reclaim=None: fs unlink reclaims immediately (no VACUUM analogue).
    return ReapSubstrate(
        name="cmtque",
        select_eligible=select_eligible,
        archive=archive,
        delete=delete,
        total_count=total_count,
        reclaim=None,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="NFRA_CMTQUE results/dlq garbage-collection")
    ap.add_argument("--retention-hours", type=float, default=24.0,
                    help="reap terminal result/dlq entries older than this (default 24h)")
    ap.add_argument("--dry-run", action="store_true", help="report only; no writes")
    ap.add_argument("--archive-only", action="store_true",
                    help="archive but do not delete (live-safe)")
    args = ap.parse_args()

    try:
        root = queue_root()
    except (subprocess.CalledProcessError, OSError) as exc:
        print(f"ERROR: not in a git repo / cannot resolve queue root: {exc}", file=sys.stderr)
        return 2
    if not root.is_dir():
        print(f"OK: no commit-queue at {root} (nothing to gc).")
        return 0

    substrate = build_substrate(root, args.retention_hours)
    reap(substrate, dry_run=args.dry_run, archive_only=args.archive_only)
    return 0


if __name__ == "__main__":
    sys.exit(main())
