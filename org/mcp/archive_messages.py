#!/usr/bin/env python3
"""archive_messages.py -- offload DELIVERED broker messages to a persistent weekly
archive, then prune + VACUUM broker.db to reclaim space.

WHY: broker.py accumulates delivered messages forever (it prunes agents + events but
NEVER messages). Delivered rows are dead weight (no broker query re-reads delivered=1),
so they pile up and every poll/health scan pays for them (the 89MB choke, LD-0245). This
offloads them to org/mcp/message_archive/messages_YYYY-Www.jsonl (append-only, grep-able),
prunes, and VACUUMs.

The reap POLICY (never-touch-in-flight / archive-then-delete-verified / reclaim-is-the-fix
/ no-silent-truncation / dry-run|archive-only|full modes) is delegated to the SHARED
.tools/reap_lib.py -- the SAME contract .tools/commit_queue_gc.py uses, so the two can
never drift (LD-0246 synergy; reap_lib + refactor authored by 0.7.0_AE_CloudOps~B). This
module only supplies the SQLite substrate callbacks; offload()'s signature/return/behavior
are UNCHANGED -- broker.py's _maybe_archive_on_startup() calls it as-is.

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

# reap_lib lives in .tools/ (owned-paths: org/mcp is the exec lane, .tools is AE's).
_REPO = Path(__file__).resolve().parents[2]  # org/mcp/<file> -> repo root
sys.path.insert(0, str(_REPO / ".tools"))
from reap_lib import ReapSubstrate, reap  # noqa: E402

MCP_DIR = Path(__file__).resolve().parent   # LIVE: org/mcp/
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
    """UNCHANGED public interface. Body now delegates the reap POLICY to reap_lib.reap()
    with SQLite substrate callbacks. retention_days=0 archives ALL delivered."""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=retention_days)).isoformat()

    # total (for the return dict + the "keeping N" log); RO, live-safe.
    ro0 = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True, timeout=30)
    total = ro0.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
    ro0.close()

    def select_eligible() -> list:
        # NEVER in-flight: delivered=1 only, older than the retention cutoff.
        ro = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True, timeout=30)
        ro.row_factory = sqlite3.Row
        rows = ro.execute(
            "SELECT id, from_serial, to_serial, subject, body, sent_at, delivered "
            "FROM messages WHERE delivered=1 AND sent_at < ? ORDER BY id",
            (cutoff,),
        ).fetchall()
        ro.close()
        # weekly breakdown (preserved observable behavior)
        wk = Counter(iso_week(r["sent_at"]) for r in rows)
        print(f"eligible (delivered=1, sent_at<{cutoff[:10]}): {len(rows)} of {total} "
              f"total  (keeping {total - len(rows)})")
        for w, c in sorted(wk.items()):
            print(f"   {w}: {c}")
        return list(rows)

    def total_count() -> int:
        return total

    def archive(rows: list) -> int:
        archive_dir.mkdir(parents=True, exist_ok=True)
        by_week: dict = {}
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
        print(f"OK: archived {written} messages -> {archive_dir} ({len(by_week)} weekly files)")
        return written

    # DELETE + VACUUM share one rw connection (VACUUM needs it after the delete commits).
    _rw: dict = {}

    def _rw_conn() -> sqlite3.Connection:
        if "c" not in _rw:
            c = sqlite3.connect(str(db_path), timeout=30, isolation_level=None)
            c.execute("PRAGMA busy_timeout = 30000")
            _rw["c"] = c
        return _rw["c"]

    def delete(rows: list) -> int:
        rw = _rw_conn()
        ids = [r["id"] for r in rows]
        deleted = 0
        rw.execute("BEGIN")
        ch = 500
        for i in range(0, len(ids), ch):
            chunk = ids[i:i + ch]
            rw.execute(f"DELETE FROM messages WHERE id IN ({','.join('?' * len(chunk))})", chunk)
            deleted += len(chunk)
        rw.execute("COMMIT")
        print(f"OK: deleted {deleted} rows from broker.db")
        return deleted

    def reclaim():
        rw = _rw_conn()
        before = db_path.stat().st_size
        try:
            rw.execute("VACUUM")
            after = db_path.stat().st_size
            msg = f"{before / 1e6:.1f}MB -> {after / 1e6:.1f}MB"
            print(f"OK: VACUUM {msg}")
            return msg
        except sqlite3.OperationalError as e:
            print(f"WARN: VACUUM could not lock (broker still holding broker.db?): {e}",
                  file=sys.stderr)
            print("      Rows are archived + deleted; re-run VACUUM with the broker stopped.",
                  file=sys.stderr)
            return None

    substrate = ReapSubstrate(
        name="broker", select_eligible=select_eligible, archive=archive,
        delete=delete, total_count=total_count,
        reclaim=(reclaim if do_vacuum else None),
    )
    try:
        r = reap(substrate, dry_run=dry_run, archive_only=archive_only,
                 do_reclaim=do_vacuum)
    finally:
        if "c" in _rw:
            _rw["c"].close()

    # map reap() result back to offload()'s backward-compatible dict shape.
    return {"eligible": r["eligible"], "total": total,
            "archived": r["archived"], "deleted": r.get("deleted", 0),
            **({"dry_run": True} if r.get("dry_run") else {})}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--retention-days", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--archive-only", action="store_true")
    ap.add_argument("--no-vacuum", action="store_true")
    args = ap.parse_args()
    offload(retention_days=args.retention_days, dry_run=args.dry_run,
            archive_only=args.archive_only, do_vacuum=not args.no_vacuum)


if __name__ == "__main__":
    main()
