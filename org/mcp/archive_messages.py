#!/usr/bin/env python3
"""archive_messages.py -- offload DELIVERED broker messages to a persistent
weekly archive, then (optionally) prune + VACUUM broker.db to reclaim space.

WHY: broker.py accumulates delivered messages forever -- it prunes `agents`
(dead PIDs) + `events` (MAX_EVENTS) but NEVER `messages`. Delivered rows are
dead weight (no broker query ever reads delivered=1), so they pile up and every
poll/health scan pays for them (the PID-21028 CPU spin). This offloads them to
org/mcp/message_archive/messages_YYYY-Www.jsonl (append-only, grep-able), then
prunes + VACUUMs.

THREE modes (safety-graded):
  --archive-only   COPY eligible messages to the archive. READ-ONLY on broker.db
                   -- safe to run while the broker is live. Does NOT delete/vacuum.
  (default)        archive + DELETE the archived rows + VACUUM. The DELETE is safe
                   live (delivered rows aren't contended); the VACUUM needs
                   EXCLUSIVE access -- run with the broker STOPPED, else it fails
                   to lock (caught + reported, archive already safely written).
  --dry-run        report eligible counts by week; no writes at all.

SAFE INVARIANTS: archive-then-delete, verified count before any delete; NEVER
touches undelivered (delivered=0) or messages newer than --retention-days; logs
what it moved (no silent truncation).

Usage:
  python org/mcp/archive_messages.py --dry-run
  python org/mcp/archive_messages.py --archive-only            # copy now, live-safe
  python org/mcp/archive_messages.py                            # archive+prune+vacuum (broker stopped)
  python org/mcp/archive_messages.py --retention-days 7         # keep last 7d delivered in the live DB
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

MCP_DIR = Path(__file__).resolve().parent
DB_PATH = MCP_DIR / "broker.db"
ARCHIVE_DIR = MCP_DIR / "message_archive"


def iso_week(sent_at: str) -> str:
    try:
        dt = datetime.fromisoformat(sent_at)
    except (ValueError, TypeError):
        return "unknown"
    y, w, _ = dt.isocalendar()
    return f"{y}-W{w:02d}"


def offload(db_path: Path = DB_PATH, archive_dir: Path = ARCHIVE_DIR,
            retention_days: int = 0, dry_run: bool = False,
            archive_only: bool = False, do_vacuum: bool = True) -> dict:
    """Offload delivered messages older than retention_days. retention_days=0
    means archive ALL delivered (the broker never re-reads them)."""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=retention_days)).isoformat()

    # read-only connection for the SELECT/archive phase (safe on the live broker)
    ro = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True, timeout=30)
    ro.row_factory = sqlite3.Row
    total = ro.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
    rows = ro.execute(
        "SELECT id, from_serial, to_serial, subject, body, sent_at, delivered "
        "FROM messages WHERE delivered=1 AND sent_at < ? ORDER BY id",
        (cutoff,),
    ).fetchall()
    ro.close()
    n = len(rows)
    kept = total - n
    print(f"eligible (delivered=1, sent_at<{cutoff[:10]}): {n} of {total} total  (keeping {kept})")

    wk_counts = Counter(iso_week(r["sent_at"]) for r in rows)
    for w, c in sorted(wk_counts.items()):
        print(f"   {w}: {c}")

    if dry_run:
        return {"eligible": n, "total": total, "archived": 0, "dry_run": True}
    if n == 0:
        print("nothing to offload.")
        return {"eligible": 0, "total": total, "archived": 0}

    # 1. ARCHIVE (append to weekly JSONL) -- verified before any delete
    archive_dir.mkdir(parents=True, exist_ok=True)
    by_week: dict[str, list] = {}
    for r in rows:
        by_week.setdefault(iso_week(r["sent_at"]), []).append(dict(r))
    written = 0
    for wk, msgs in sorted(by_week.items()):
        fp = archive_dir / f"messages_{wk}.jsonl"
        with open(fp, "a", encoding="utf-8") as f:
            for m in msgs:
                f.write(json.dumps(m, ensure_ascii=True) + "\n")
                written += 1
            f.flush()
            os.fsync(f.fileno())
    if written != n:
        print(f"ERROR: wrote {written} != eligible {n}; NOT deleting.", file=sys.stderr)
        sys.exit(1)
    print(f"OK: archived {written} messages -> {archive_dir} ({len(by_week)} weekly files)")

    if archive_only:
        print("archive-only: broker.db untouched (run without --archive-only, broker stopped, to prune+vacuum).")
        return {"eligible": n, "total": total, "archived": written, "deleted": 0}

    # 2. DELETE the archived rows (autocommit; chunked; by id)
    rw = sqlite3.connect(str(db_path), timeout=30, isolation_level=None)
    rw.execute("PRAGMA busy_timeout = 30000")
    ids = [r["id"] for r in rows]
    deleted = 0
    rw.execute("BEGIN")
    CH = 500
    for i in range(0, len(ids), CH):
        chunk = ids[i:i + CH]
        rw.execute(f"DELETE FROM messages WHERE id IN ({','.join('?' * len(chunk))})", chunk)
        deleted += len(chunk)
    rw.execute("COMMIT")
    print(f"OK: deleted {deleted} rows from broker.db")

    # 3. VACUUM (reclaim file bytes -- the actual CPU fix). Needs exclusive lock.
    if do_vacuum:
        before = db_path.stat().st_size
        try:
            rw.execute("VACUUM")
            after = db_path.stat().st_size
            print(f"OK: VACUUM {before/1e6:.1f}MB -> {after/1e6:.1f}MB")
        except sqlite3.OperationalError as e:
            print(f"WARN: VACUUM could not lock (broker still holding broker.db?): {e}", file=sys.stderr)
            print("      Rows are archived + deleted; re-run VACUUM with the broker stopped to reclaim disk.", file=sys.stderr)
    rw.close()
    return {"eligible": n, "total": total, "archived": written, "deleted": deleted}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--retention-days", type=int, default=0,
                    help="keep delivered msgs newer than this in the live DB (0 = archive all delivered)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--archive-only", action="store_true",
                    help="copy to archive only; do NOT delete/vacuum (live-safe)")
    ap.add_argument("--no-vacuum", action="store_true")
    args = ap.parse_args()
    offload(retention_days=args.retention_days, dry_run=args.dry_run,
            archive_only=args.archive_only, do_vacuum=not args.no_vacuum)


if __name__ == "__main__":
    main()
