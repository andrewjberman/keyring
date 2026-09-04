"""
Opal Agent Broker — Cross-session message routing for concurrent agents.

Singleton HTTP server on localhost:7800. Auto-launched by server.py if not
already running. Backed by SQLite (WAL mode, in org/mcp/broker.db).

Each MCP server instance (one per Claude Code session) registers on startup,
heartbeats periodically, and polls for inbound messages. The broker routes
messages between sessions — the MCP server handles the channel push into
Claude's conversation.

Telemetry: all significant events are logged to an `events` table. The
monitor.py script polls /events and /status to render a live terminal feed.

Run standalone:  python org/mcp/broker.py
Auto-launched:   server.py calls _ensure_broker() on register_agent
Monitor:         python org/mcp/monitor.py
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from threading import Timer

if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
import cvo_send_guard  # noqa: E402  the L8 correspondence guard, shared with server.py (same dir)

_REPO_ROOT = Path(__file__).resolve().parents[2]
PORT = int(os.environ.get("OPAL_BROKER_PORT", "7800"))
# OPAL_BROKER_DB lets the T1 exercise battery run against a scratch DB on a scratch port.
# Exercising delivery semantics requires killing clients mid-flight; doing that against the
# live fabric DB would be an outage, and asserting the behavior instead of exercising it is
# exactly what this build exists to stop.
DB_PATH = (Path(os.environ["OPAL_BROKER_DB"]) if os.environ.get("OPAL_BROKER_DB")
           else Path(__file__).resolve().parent / "broker.db")

# Max events to retain (older are pruned on cleanup cycle)
MAX_EVENTS = 500

# Weekly message-archive offload (org/mcp/archive_messages.py). The messages table
# is never pruned by the cleanup cycle, so delivered rows (which no query re-reads)
# accumulate unbounded and the daemon spins scanning them (89MB / 36,940-row choke
# 2026-07-06, LD-0245). This runs the offload at startup, weekly-gated, BEFORE the
# persistent connection opens so its VACUUM has exclusive access.
ARCHIVE_INTERVAL_DAYS = 7
ARCHIVE_RETENTION_DAYS = 7          # keep undelivered + last-7d delivered in the live DB
ARCHIVE_MIN_BACKLOG = 500           # skip unless the aged-delivered backlog exceeds this
_ARCHIVE_MARKER = DB_PATH.parent / ".last_message_archive"

# Max-uptime self-restart: the startup archive-catch-up only fires when the broker
# RESTARTS, but register_agent relaunches only a DOWN broker -- a healthy one can run
# for weeks (CTO arch concern 2026-07-06, LD-0246). So after this uptime the broker
# gracefully self-exits; the next agent call relaunches it via server.py _ensure_broker,
# which fires the weekly archive catch-up. Guarantees the offload runs >=weekly
# regardless of session churn (belt to the startup-catch-up suspenders).
BROKER_MAX_UPTIME_S = ARCHIVE_INTERVAL_DAYS * 86400

# --- D0_TIGHTENING T1: three-clock delivery accounting -------------------------
# SENT    = polled_at   (a CLIENT PROCESS took handoff -- says NOTHING about an agent)
# EMITTED = emitted_at  (piggyback drain: the volatile queue cleared -- the clear
#                        precedes the response reaching a model; orphan-watcher shape)
# READ    = acked_at    (ONLY check_inbox(mark_read=True) or a genuine AGENT-side ack)
# Before T1, `delivered` was flipped AT POLL (broker.py:474) and the message then lived
# only in the server's in-memory _piggyback_queue. A client dying between poll and drain
# lost the message PERMANENTLY: re-delivery filters delivered=0 and the row was already 1,
# while the event log recorded "deliver" for a message no agent ever saw.
# Fix: poll stamps polled_at and leaves delivered=0; DRAIN flips delivered=1. An undrained
# message becomes re-offerable after T1_RECLAIM_S so a dead-before-drain client recovers it.
# T1_RECLAIM_S must exceed the server's POLL_INTERVAL_S (10s) by a wide margin so a healthy
# session is never re-offered mail it is about to drain; the server also dedupes by id.
T1_RECLAIM_S = 90

# BOUNDED RE-OFFER (added 2026-08-20 -- a REGRESSION FIX ON THE T1 DURABILITY CHANGE ITSELF).
# T1 made an undrained message re-offerable so a client dying between poll and drain recovers it.
# That is correct ONLY against a server that reports the drain via /mark-emitted. A PRE-T1 server
# never calls that endpoint, so `delivered` never leaves 0 and the re-offer predicate matches
# FOREVER -- and a pre-T1 server has no id-dedupe on its piggyback queue, so every re-offer
# APPENDS another copy. Measured on the live DB 2026-08-20T00:2xZ, ~4 minutes of mixed-version
# fabric: 97 rows polled-but-never-emitted vs 15 properly emitted, multiplicity age-monotonic
# because an older row has survived more re-offer cycles.
#
# RECOVERY IS A BOUNDED ACT, NOT A STANDING CONDITION. Re-offering N times is recovery;
# re-offering without limit is a loop that grows every consumer's payload without bound.
#
# SAFE BY PRECONDITION, not by hope: send_message writes the FILESYSTEM copy (server.py:1785)
# BEFORE it calls the broker (:1795), so the inbox dir is the durable path and the piggyback
# queue is a convenience. A row that stops being re-offered has NOT lost its content -- which is
# exactly why capping is the right lever and dropping the durability fix is not.
T1_MAX_OFFERS = 3

# ---------------------------------------------------------------------------
# Database setup
# ---------------------------------------------------------------------------

def _init_db() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH), timeout=5)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA busy_timeout = 3000")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS agents (
            serial      TEXT PRIMARY KEY,
            pid         INTEGER NOT NULL,
            summary     TEXT NOT NULL DEFAULT '',
            registered_at TEXT NOT NULL,
            last_seen   TEXT NOT NULL,
            last_seen_epoch REAL NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            from_serial TEXT NOT NULL,
            to_serial   TEXT NOT NULL,
            subject     TEXT NOT NULL DEFAULT '',
            body        TEXT NOT NULL,
            sent_at     TEXT NOT NULL,
            delivered   INTEGER NOT NULL DEFAULT 0
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            ts          TEXT NOT NULL,
            ts_epoch    REAL NOT NULL,
            event_type  TEXT NOT NULL,
            agent       TEXT NOT NULL DEFAULT '',
            detail      TEXT NOT NULL DEFAULT ''
        )
    """)

    # --- D0_TIGHTENING T1 migration: additive columns for the three clocks.
    # Additive + idempotent: an older broker binary ignores unknown columns, so a
    # mixed-version fabric degrades to present behavior rather than breaking.
    _cols = {r["name"] for r in conn.execute("PRAGMA table_info(messages)").fetchall()}
    for _col in ("polled_at", "emitted_at", "acked_at", "acked_by"):
        if _col not in _cols:
            conn.execute(f"ALTER TABLE messages ADD COLUMN {_col} TEXT")
    if "offer_count" not in _cols:
        conn.execute("ALTER TABLE messages ADD COLUMN offer_count INTEGER NOT NULL DEFAULT 0")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS schema_meta (
            key   TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    """)
    # The pre-T1 boundary. A row delivered under the old code carries delivered=1 with
    # polled_at NULL -- that pair is the mechanical discriminator get_delivery_state uses
    # to answer UNKNOWN-PRE-T1 (honest) instead of READ (a lie about an agent).
    conn.execute(
        "INSERT OR IGNORE INTO schema_meta (key, value) VALUES ('t1_migrated_at', ?)",
        (datetime.now(timezone.utc).isoformat(),),
    )

    conn.commit()
    return conn


db: sqlite3.Connection = None  # initialized in main


# ---------------------------------------------------------------------------
# Event logging
# ---------------------------------------------------------------------------

def _log_event(event_type: str, agent: str = "", detail: str = ""):
    """Record a telemetry event."""
    now = datetime.now(timezone.utc)
    db.execute(
        "INSERT INTO events (ts, ts_epoch, event_type, agent, detail) VALUES (?, ?, ?, ?, ?)",
        (now.isoformat(), time.time(), event_type, agent, detail),
    )
    # Don't commit here — caller commits as part of their transaction


# ---------------------------------------------------------------------------
# Stale cleanup (PID check)
# ---------------------------------------------------------------------------

def _pid_alive(pid: int) -> bool:
    """Check if a process is still running."""
    if sys.platform == "win32":
        import ctypes
        kernel32 = ctypes.windll.kernel32
        PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
        if handle:
            kernel32.CloseHandle(handle)
            return True
        return False
    else:
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False


def _clean_stale():
    """Remove agents whose PIDs no longer exist. Prune old events.

    Note: we deliberately do NOT delete undelivered messages for stale agents.
    A recipient's session can end and restart within seconds — dropping pending
    messages on a 30s timer created a race where the recipient's new MCP server
    process would register, call _poll_broker_loop, and find nothing because the
    broker had already evicted the message. Messages persist until explicitly
    marked delivered via _handle_poll_messages, so a re-registered agent picks
    them up on the next poll cycle.
    """
    rows = db.execute("SELECT serial, pid FROM agents").fetchall()
    for row in rows:
        if not _pid_alive(row["pid"]):
            _log_event("agent_stale", row["serial"], f"PID {row['pid']} no longer alive")
            db.execute("DELETE FROM agents WHERE serial = ?", (row["serial"],))

    # Prune old events
    db.execute(
        "DELETE FROM events WHERE id NOT IN (SELECT id FROM events ORDER BY id DESC LIMIT ?)",
        (MAX_EVENTS,),
    )

    db.commit()


def _schedule_cleanup():
    """Run stale cleanup every 30 seconds; self-restart past max uptime."""
    _clean_stale()
    # Max-uptime graceful self-restart so the weekly archive catch-up is guaranteed
    # to fire even if the broker never crash-restarts (CTO arch concern, LD-0246).
    if time.time() - _start_time > BROKER_MAX_UPTIME_S:
        try:
            _log_event("broker_uptime_restart", "",
                       f"uptime > {ARCHIVE_INTERVAL_DAYS}d -- graceful self-restart for weekly archive")
            db.commit()
        except Exception:
            pass
        print("[opal-broker] max uptime reached -- exiting for weekly archive catch-up",
              file=sys.stderr, flush=True)
        os._exit(0)
    t = Timer(30.0, _schedule_cleanup)
    t.daemon = True
    t.start()


# ---------------------------------------------------------------------------
# Parent-death watchdog (RV-0017 F-004)
# ---------------------------------------------------------------------------
# Captured at startup. If this PID disappears, the broker has been orphaned and
# must exit gracefully so it cannot accumulate CPU/state from agents whose
# sessions outlive its parent. Per RV-0017 incident 2026-05-27 PID 3812 orphan
# (8158 CPU-sec / 6h45m vs dead parent PID 20276).
_INITIAL_PARENT_PID = None
_WATCHDOG_INTERVAL_S = 30.0


def _parent_alive() -> bool:
    """True if the broker's launching parent process is still alive.

    Conservative: returns True on any uncertainty. The watchdog only fires
    on a definitive 'parent gone' signal, never on a transient PID-check
    failure.
    """
    if _INITIAL_PARENT_PID is None:
        return True
    return _pid_alive(_INITIAL_PARENT_PID)


def _parent_watchdog():
    """Re-arming watchdog: exit broker if launching parent process died."""
    try:
        if not _parent_alive():
            _log_event(
                "broker_orphan_exit",
                "",
                f"parent PID {_INITIAL_PARENT_PID} no longer alive -- exiting",
            )
            db.commit()
            print(
                f"[opal-broker] parent PID {_INITIAL_PARENT_PID} died -- exiting gracefully",
                file=sys.stderr, flush=True,
            )
            # os._exit bypasses the HTTPServer's serve_forever() select-loop
            # cleanly without requiring shutdown() coordination from another
            # thread. The Timer thread cannot call server.shutdown() because
            # serve_forever() must be running on a different thread, which is
            # not the case in single-thread mode.
            os._exit(0)
    except Exception as exc:
        # Watchdog failures must never crash the broker; log and re-arm.
        try:
            _log_event("watchdog_error", "", f"{type(exc).__name__}: {exc}")
            db.commit()
        except Exception:
            pass

    t = Timer(_WATCHDOG_INTERVAL_S, _parent_watchdog)
    t.daemon = True
    t.start()


# ---------------------------------------------------------------------------
# HTTP Request Handler
# ---------------------------------------------------------------------------

class BrokerHandler(BaseHTTPRequestHandler):
    """Handles broker API requests. All POST endpoints accept/return JSON."""

    def log_message(self, format, *args):
        """Route HTTP logs to stderr with broker prefix."""
        print(f"[opal-broker] {args[0]}", file=sys.stderr, flush=True)

    def _json_response(self, data: dict | list, status: int = 200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        return json.loads(raw) if raw else {}

    def do_GET(self):
        if self.path == "/health":
            count = db.execute("SELECT COUNT(*) as c FROM agents").fetchone()["c"]
            pending = db.execute("SELECT COUNT(*) as c FROM messages WHERE delivered = 0").fetchone()["c"]
            total_msgs = db.execute("SELECT COUNT(*) as c FROM messages").fetchone()["c"]
            total_events = db.execute("SELECT COUNT(*) as c FROM events").fetchone()["c"]
            self._json_response({
                "status": "ok",
                "agents": count,
                "pending_messages": pending,
                "total_messages": total_msgs,
                "total_events": total_events,
                "port": PORT,
                "uptime_s": int(time.time() - _start_time),
            })
        elif self.path == "/status":
            self._handle_status()
        elif self.path.startswith("/events"):
            self._handle_events_get()
        else:
            self._json_response({"name": "opal-agent-broker", "version": "2.0.0"})

    def _handle_status(self):
        """Full status snapshot: agents, queue depth, recent events."""
        agents = []
        for row in db.execute("SELECT * FROM agents ORDER BY serial").fetchall():
            alive = _pid_alive(row["pid"])
            elapsed = int(time.time() - row["last_seen_epoch"])
            agents.append({
                "serial": row["serial"],
                "pid": row["pid"],
                "alive": alive,
                "summary": row["summary"],
                "registered_at": row["registered_at"],
                "last_seen": row["last_seen"],
                "elapsed_s": elapsed,
            })

        pending = db.execute(
            "SELECT from_serial, to_serial, subject, sent_at FROM messages WHERE delivered = 0 ORDER BY sent_at"
        ).fetchall()
        queue = [dict(row) for row in pending]

        recent = db.execute(
            "SELECT * FROM events ORDER BY id DESC LIMIT 20"
        ).fetchall()
        events = [dict(row) for row in recent]

        self._json_response({
            "agents": agents,
            "queue": queue,
            "recent_events": events,
            "uptime_s": int(time.time() - _start_time),
        })

    def _handle_events_get(self):
        """GET /events?since_id=N — return events after the given ID."""
        # Parse query string
        since_id = 0
        if "?" in self.path:
            params = dict(p.split("=", 1) for p in self.path.split("?", 1)[1].split("&") if "=" in p)
            since_id = int(params.get("since_id", 0))

        rows = db.execute(
            "SELECT * FROM events WHERE id > ? ORDER BY id ASC LIMIT 50",
            (since_id,),
        ).fetchall()
        self._json_response([dict(row) for row in rows])

    def do_POST(self):
        try:
            body = self._read_json()
            path = self.path

            if path == "/register":
                self._handle_register(body)
            elif path == "/heartbeat":
                self._handle_heartbeat(body)
            elif path == "/set-summary":
                self._handle_set_summary(body)
            elif path == "/list-agents":
                self._handle_list_agents(body)
            elif path == "/send-message":
                self._handle_send_message(body)
            elif path == "/poll-messages":
                self._handle_poll_messages(body)
            elif path == "/mark-emitted":
                self._handle_mark_emitted(body)
            elif path == "/ack-messages":
                self._handle_ack_messages(body)
            elif path == "/delivery-state":
                self._handle_delivery_state(body)
            elif path == "/unregister":
                self._handle_unregister(body)
            else:
                self._json_response({"error": "not found"}, 404)

        except Exception as e:
            self._json_response({"error": str(e)}, 500)

    def _handle_register(self, body: dict):
        serial = body["serial"]
        pid = body["pid"]
        summary = body.get("summary", "")
        now = datetime.now(timezone.utc).isoformat()

        db.execute("DELETE FROM agents WHERE serial = ?", (serial,))
        db.execute(
            "INSERT INTO agents (serial, pid, summary, registered_at, last_seen, last_seen_epoch) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (serial, pid, summary, now, now, time.time()),
        )
        _log_event("register", serial, f"PID {pid}" + (f" | {summary}" if summary else ""))
        db.commit()
        self._json_response({"ok": True, "serial": serial})

    def _handle_heartbeat(self, body: dict):
        serial = body["serial"]
        now = datetime.now(timezone.utc).isoformat()
        db.execute(
            "UPDATE agents SET last_seen = ?, last_seen_epoch = ? WHERE serial = ?",
            (now, time.time(), serial),
        )
        if body.get("summary"):
            db.execute(
                "UPDATE agents SET summary = ? WHERE serial = ?",
                (body["summary"], serial),
            )
        db.commit()
        # Heartbeats are not logged to events (too noisy) — they update last_seen only
        self._json_response({"ok": True})

    def _handle_set_summary(self, body: dict):
        db.execute(
            "UPDATE agents SET summary = ? WHERE serial = ?",
            (body["summary"], body["serial"]),
        )
        _log_event("summary", body["serial"], body["summary"][:120])
        db.commit()
        self._json_response({"ok": True})

    def _handle_list_agents(self, body: dict):
        exclude = body.get("exclude_serial")
        rows = db.execute("SELECT * FROM agents").fetchall()

        agents = []
        for row in rows:
            if exclude and row["serial"] == exclude:
                continue
            if not _pid_alive(row["pid"]):
                db.execute("DELETE FROM agents WHERE serial = ?", (row["serial"],))
                continue
            agents.append({
                "serial": row["serial"],
                "pid": row["pid"],
                "summary": row["summary"],
                "registered_at": row["registered_at"],
                "last_seen": row["last_seen"],
            })
        db.commit()
        self._json_response(agents)

    def _handle_send_message(self, body: dict):
        from_serial = body["from_serial"]
        to_serial = body["to_serial"]
        subject = body.get("subject", "")
        text = body["text"]
        now = datetime.now(timezone.utc).isoformat()

        # L8 CORRESPONDENCE GUARD (spine v2.1 L8; Andrew-direct 2026-09-03 "Recs approved", CTO /open-calls
        # CALL 1) -- the same decision org/mcp/server.py applies before it posts here. This HTTP path is
        # reachable WITHOUT the server (a direct POST), so it grades on its own; a refused send inserts nothing.
        _l8 = cvo_send_guard.cvo_worker_send_refusal(
            from_serial, [to_serial], cvo_send_guard.executing_tree_projects(_REPO_ROOT), subject=subject, body=text)
        if _l8:
            _log_event("refused", from_serial, f"-> {to_serial} L8 guard: {_l8[:160]}")
            db.commit()
            self._json_response({"ok": False, "refused": _l8}, 403)
            return
        # LD-0529 -- the generalised Tier-0/Tier-1 -> Tier-2 act guard, the same decision the server applies.
        _t2 = cvo_send_guard.tier2_act_send_refusal(from_serial, [to_serial], subject, text, _REPO_ROOT)
        if _t2:
            _log_event("refused", from_serial, f"-> {to_serial} LD-0529 guard: {_t2[:160]}")
            db.commit()
            self._json_response({"ok": False, "refused": _t2}, 403)
            return

        # Always accept the insert. A recipient does not need to be currently
        # registered for us to queue a message — they may be mid-restart or the
        # sender may be racing ahead of the new session's register_agent call.
        # _poll_broker_loop in the recipient's MCP server will pick it up on
        # their next 2s poll tick once they register. messages has no FK to
        # agents, so this is safe.
        target = db.execute(
            "SELECT serial FROM agents WHERE serial = ?", (to_serial,)
        ).fetchone()
        recipient_state = "registered" if target else "pre-register"

        _cur = db.execute(
            "INSERT INTO messages (from_serial, to_serial, subject, body, sent_at, delivered) "
            "VALUES (?, ?, ?, ?, ?, 0)",
            (from_serial, to_serial, subject, text, now),
        )
        # Read the id from the INSERT's own cursor, NOT last_insert_rowid(): _log_event
        # below inserts into `events` on the same connection, so a deferred rowid read
        # returns the EVENT row and every later ACK would name the wrong message.
        message_id = _cur.lastrowid
        preview = text[:80] + "..." if len(text) > 80 else text
        _log_event(
            "message",
            from_serial,
            f"-> {to_serial} [{recipient_state}] [{subject}] {preview}",
        )
        db.commit()
        self._json_response({"ok": True, "recipient_state": recipient_state,
                             "message_id": message_id})

    def _handle_poll_messages(self, body: dict):
        """SENT clock. A poll means a CLIENT PROCESS took handoff -- nothing more.

        D0_TIGHTENING T1: this handler used to set delivered=1 here (the old line 474).
        That was the message-loss window: the message then lived only in the polling
        server's in-memory _piggyback_queue, and re-delivery filters delivered=0, so a
        client dying before it drained lost the message PERMANENTLY while the event log
        recorded a "deliver". Now the poll stamps polled_at ONLY; delivered flips at the
        DRAIN (/mark-emitted). An undrained message is re-offered after T1_RECLAIM_S, so
        a seat killed between poll and drain gets its mail on respawn. The server dedupes
        by id, so a re-offer to a still-live session is a no-op rather than a duplicate.
        """
        serial = body["serial"]
        now = datetime.now(timezone.utc)
        reclaim_cutoff = (now - timedelta(seconds=T1_RECLAIM_S)).isoformat()

        # Re-delivery predicate: never-polled, OR polled long enough ago that the polling
        # client is presumed dead before it drained. This is the half that makes a
        # polled-but-undrained message recoverable instead of lost.
        # offer_count < T1_MAX_OFFERS BOUNDS THE RECOVERY. Without it a server that never
        # reports its drain (every pre-T1 server) matches this predicate on every poll forever.
        rows = db.execute(
            "SELECT * FROM messages WHERE to_serial = ? AND delivered = 0 "
            "AND (polled_at IS NULL OR polled_at <= ?) "
            "AND offer_count < ? ORDER BY sent_at ASC",
            (serial, reclaim_cutoff, T1_MAX_OFFERS),
        ).fetchall()

        messages = []
        reclaimed = 0
        for row in rows:
            if row["polled_at"] is not None:
                reclaimed += 1
            messages.append({
                "id": row["id"],
                "from_serial": row["from_serial"],
                "to_serial": row["to_serial"],
                "subject": row["subject"],
                "body": row["body"],
                "sent_at": row["sent_at"],
            })
            db.execute(
                "UPDATE messages SET polled_at = ?, offer_count = offer_count + 1 WHERE id = ?",
                (now.isoformat(), row["id"]))

        if messages:
            # SENT, stated as SENT. The old text said "polled" and was read as delivery.
            detail = f"{len(messages)} message(s) SENT (polled; not yet emitted)"
            if reclaimed:
                detail += f" -- {reclaimed} RECLAIMED (polled earlier, never drained)"
            _log_event("sent", serial, detail)
        db.commit()
        self._json_response({"messages": messages})

    def _handle_mark_emitted(self, body: dict):
        """EMITTED clock. The piggyback drain cleared the volatile queue.

        This is where delivered flips to 1 -- the message has left the broker's
        responsibility and entered a tool response. It is EMITTED, not READ: the clear
        precedes the response ever reaching a model (structurally the orphan-watcher
        mv-before-echo shape), so nothing here may be reported as an agent having seen it.
        """
        serial = body.get("serial", "")
        ids = [int(i) for i in body.get("ids", [])]
        if not ids:
            self._json_response({"ok": True, "emitted": 0})
            return
        now = datetime.now(timezone.utc).isoformat()
        qmarks = ",".join("?" for _ in ids)
        cur = db.execute(
            f"UPDATE messages SET delivered = 1, emitted_at = ? "
            f"WHERE id IN ({qmarks}) AND delivered = 0",
            (now, *ids),
        )
        _log_event("emitted", serial,
                   f"{cur.rowcount} message(s) EMITTED (drained to tool response)")
        db.commit()
        self._json_response({"ok": True, "emitted": cur.rowcount})

    def _handle_ack_messages(self, body: dict):
        """READ clock -- the ONLY sound one, and the only one an orphan cannot forge.

        Written exclusively at a CONSUMPTION act: check_inbox(mark_read=True), or an
        agent-side ack naming the ids it possessed. An ACK placed at a transport act
        would inherit the exact conflation this primitive exists to retire.
        """
        serial = body.get("serial", "")
        ids = [int(i) for i in body.get("ids", [])]
        # RECIPIENT CHECK (2026-08-30, 1.0.0_SA_CTO on 0.0.0_AB_MSTR 84328). Before this line
        # the UPDATE carried no `to_serial` predicate: an ack from ANY registered serial landed
        # on ANY id, and because the row is write-once a mistyped or guessed id did not fail --
        # it permanently stole the true recipient's READ slot (measured: 84265, addressed to
        # 0.4.0_DE_ClientPlatform~D, acked by 0.8.0_AE_CloudComp~X; 341 of 22,596 acked rows
        # carried acked_by != to_serial at the time of the fix). Write-once is a RACE, not a
        # control. `override` is set ONLY by check_inbox(mark_read=True, identity_override=...)
        # -- the audited dead-agent-cleanup drain -- and acked_by still records the cleaner.
        override = bool(body.get("override"))
        if not ids:
            self._json_response({"ok": True, "acked": 0, "refused": 0, "refused_ids": []})
            return
        now = datetime.now(timezone.utc).isoformat()
        qmarks = ",".join("?" for _ in ids)
        refused_ids = []
        if not override:
            refused_ids = [
                int(r["id"]) for r in db.execute(
                    f"SELECT id FROM messages WHERE id IN ({qmarks}) "
                    f"AND acked_at IS NULL AND to_serial != ?",
                    (*ids, serial)).fetchall()
            ]
        recipient_clause = "" if override else " AND to_serial = ?"
        recipient_params = () if override else (serial,)
        # An ACK also settles the earlier clocks: a message an agent demonstrably read was
        # necessarily emitted. Never the reverse.
        cur = db.execute(
            f"UPDATE messages SET acked_at = ?, acked_by = ?, delivered = 1, "
            f"emitted_at = COALESCE(emitted_at, ?) "
            f"WHERE id IN ({qmarks}) AND acked_at IS NULL{recipient_clause}",
            (now, serial, now, *ids, *recipient_params),
        )
        _log_event("read", serial, f"{cur.rowcount} message(s) READ (agent-side ack)")
        if refused_ids:
            _log_event("read", serial,
                       f"{len(refused_ids)} ack(s) REFUSED -- id(s) not addressed to {serial}: "
                       f"{refused_ids} (recipient check; the true recipient's READ slot stays open)")
        db.commit()
        self._json_response({"ok": True, "acked": cur.rowcount,
                             "refused": len(refused_ids), "refused_ids": refused_ids,
                             "override": override})

    def _handle_delivery_state(self, body: dict):
        """Primitive (ii): per-message SENT / EMITTED / READ -- never an aggregate.

        States, in the fabric's own vocabulary:
          QUEUED          row exists, no client has polled it
          SENT            polled (a client process took handoff; says nothing about an agent)
          EMITTED         drained into a tool response (no agent-side evidence)
          READ            agent-side ack -- the only state that claims an agent saw it
          UNKNOWN-PRE-T1  delivered under the pre-T1 code (delivered=1, polled_at NULL).
                          Honest: that row's fate is unknowable. Never reported as READ.
        """
        serial = body.get("serial", "")
        message_id = body.get("message_id")
        since = body.get("since", "")
        limit = int(body.get("limit", 200))

        if message_id is not None:
            rows = db.execute("SELECT * FROM messages WHERE id = ?",
                              (int(message_id),)).fetchall()
        elif serial and since:
            rows = db.execute(
                "SELECT * FROM messages WHERE to_serial = ? AND sent_at >= ? "
                "ORDER BY sent_at ASC LIMIT ?", (serial, since, limit)).fetchall()
        elif serial:
            rows = db.execute(
                "SELECT * FROM messages WHERE to_serial = ? ORDER BY sent_at DESC LIMIT ?",
                (serial, limit)).fetchall()
        else:
            self._json_response({"error": "delivery-state needs message_id or serial"}, 400)
            return

        out = []
        for r in rows:
            keys = r.keys()
            polled = r["polled_at"] if "polled_at" in keys else None
            emitted = r["emitted_at"] if "emitted_at" in keys else None
            acked = r["acked_at"] if "acked_at" in keys else None
            if acked:
                state = "READ"
            elif (not r["delivered"]
                  and ("offer_count" in keys and (r["offer_count"] or 0) >= T1_MAX_OFFERS)):
                # Offered the bounded number of times, never confirmed emitted. Reported as its
                # OWN state rather than folded into SENT: "we stopped offering" is a different
                # fact from "a client took handoff", and the remedy differs too (read the
                # filesystem inbox, which still holds it).
                state = "OFFER-EXHAUSTED"
            elif r["delivered"] and polled is None and emitted is None:
                # Pre-T1 row: flipped by the old poll handler. Unknowable, and saying so
                # is the whole point -- this is the state that must never read as READ.
                state = "UNKNOWN-PRE-T1"
            elif emitted:
                state = "EMITTED"
            elif polled:
                state = "SENT"
            else:
                state = "QUEUED"
            out.append({
                "id": r["id"], "from_serial": r["from_serial"],
                "to_serial": r["to_serial"],
                "subject": r["subject"], "sent_at": r["sent_at"], "state": state,
                "polled_at": polled, "emitted_at": emitted,
                "acked_at": acked,
                "acked_by": (r["acked_by"] if "acked_by" in keys else None),
            })
        self._json_response({"messages": out, "count": len(out)})

    def _handle_unregister(self, body: dict):
        serial = body["serial"]
        _log_event("unregister", serial, "")
        db.execute("DELETE FROM agents WHERE serial = ?", (serial,))
        db.commit()
        self._json_response({"ok": True})


# ---------------------------------------------------------------------------
# Startup hygiene: singleton guard + weekly message-archive catch-up
# ---------------------------------------------------------------------------

def _existing_broker_healthy() -> bool:
    """True if a healthy broker already owns the port. Prevents redundant broker
    processes that would hold broker.db + block maintenance VACUUMs (the 3-orphan
    -broker issue 2026-07-06)."""
    import urllib.request
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/health", timeout=2) as r:
            return r.status == 200
    except Exception:
        return False


def _maybe_archive_on_startup():
    """Weekly-gated offload of delivered messages to org/mcp/message_archive/.
    Runs BEFORE the persistent connection opens, so archive_messages' VACUUM has
    exclusive access. No-op unless >ARCHIVE_INTERVAL_DAYS since last run AND the
    aged-delivered backlog exceeds ARCHIVE_MIN_BACKLOG. Never raises into startup."""
    try:
        if _ARCHIVE_MARKER.exists():
            try:
                last = datetime.fromisoformat(_ARCHIVE_MARKER.read_text().strip())
                if datetime.now(timezone.utc) - last < timedelta(days=ARCHIVE_INTERVAL_DAYS):
                    return
            except ValueError:
                pass
        cutoff = (datetime.now(timezone.utc) - timedelta(days=ARCHIVE_RETENTION_DAYS)).isoformat()
        ro = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True, timeout=5)
        n = ro.execute(
            "SELECT COUNT(*) FROM messages WHERE delivered=1 AND sent_at < ?", (cutoff,)
        ).fetchone()[0]
        ro.close()
        if n < ARCHIVE_MIN_BACKLOG:
            _ARCHIVE_MARKER.write_text(datetime.now(timezone.utc).isoformat())
            return
        sys.path.insert(0, str(DB_PATH.parent))
        import archive_messages
        print(f"[opal-broker] weekly archive: offloading {n} delivered messages...",
              file=sys.stderr, flush=True)
        archive_messages.offload(retention_days=ARCHIVE_RETENTION_DAYS, do_vacuum=True)
        _ARCHIVE_MARKER.write_text(datetime.now(timezone.utc).isoformat())
    except Exception as exc:
        # Startup archival must never block the broker from serving.
        print(f"[opal-broker] startup archive skipped: {type(exc).__name__}: {exc}",
              file=sys.stderr, flush=True)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

_start_time = time.time()


def main():
    global db, _start_time, _INITIAL_PARENT_PID
    _start_time = time.time()

    # Singleton guard: exit cleanly if a healthy broker already owns the port
    # (do this BEFORE opening broker.db so a redundant launch never holds a
    # connection that would block the archive VACUUM).
    if _existing_broker_healthy():
        print(f"[opal-broker] a healthy broker already owns :{PORT} -- exiting (singleton)",
              file=sys.stderr, flush=True)
        return

    # Weekly message-archive catch-up (before the persistent connection opens).
    _maybe_archive_on_startup()

    db = _init_db()

    # Capture launching parent PID for the watchdog. Allow override via env
    # for testing (OPAL_BROKER_PARENT_PID); production captures os.getppid().
    parent_env = os.environ.get("OPAL_BROKER_PARENT_PID")
    if parent_env:
        try:
            _INITIAL_PARENT_PID = int(parent_env)
        except ValueError:
            _INITIAL_PARENT_PID = os.getppid()
    else:
        _INITIAL_PARENT_PID = os.getppid()

    _log_event(
        "broker_start", "",
        f"port={PORT} parent_pid={_INITIAL_PARENT_PID} pid={os.getpid()}",
    )
    db.commit()

    _clean_stale()
    _schedule_cleanup()
    _parent_watchdog()

    server = HTTPServer(("127.0.0.1", PORT), BrokerHandler)
    print(
        f"[opal-broker] listening on 127.0.0.1:{PORT} (db: {DB_PATH})",
        file=sys.stderr, flush=True,
    )

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        _log_event("broker_stop", "", "keyboard interrupt")
        db.commit()
        print("[opal-broker] shutting down", file=sys.stderr, flush=True)
        server.shutdown()


if __name__ == "__main__":
    main()
