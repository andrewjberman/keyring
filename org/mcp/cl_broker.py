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

import json
import os
import signal
import sqlite3
import sys
import time
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from threading import Timer

PORT = int(os.environ.get("CL_BROKER_PORT", "7801"))
DB_PATH = Path(__file__).resolve().parent / "cl_broker.db"

# Max events to retain (older are pruned on cleanup cycle)
MAX_EVENTS = 500

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
    """Run stale cleanup every 30 seconds."""
    _clean_stale()
    t = Timer(30.0, _schedule_cleanup)
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

        db.execute(
            "INSERT INTO messages (from_serial, to_serial, subject, body, sent_at, delivered) "
            "VALUES (?, ?, ?, ?, ?, 0)",
            (from_serial, to_serial, subject, text, now),
        )
        preview = text[:80] + "..." if len(text) > 80 else text
        _log_event(
            "message",
            from_serial,
            f"-> {to_serial} [{recipient_state}] [{subject}] {preview}",
        )
        db.commit()
        self._json_response({"ok": True, "recipient_state": recipient_state})

    def _handle_poll_messages(self, body: dict):
        serial = body["serial"]
        rows = db.execute(
            "SELECT * FROM messages WHERE to_serial = ? AND delivered = 0 ORDER BY sent_at ASC",
            (serial,),
        ).fetchall()

        messages = []
        for row in rows:
            messages.append({
                "id": row["id"],
                "from_serial": row["from_serial"],
                "to_serial": row["to_serial"],
                "subject": row["subject"],
                "body": row["body"],
                "sent_at": row["sent_at"],
            })
            db.execute("UPDATE messages SET delivered = 1 WHERE id = ?", (row["id"],))

        if messages:
            _log_event("deliver", serial, f"{len(messages)} message(s) polled")
        db.commit()
        self._json_response({"messages": messages})

    def _handle_unregister(self, body: dict):
        serial = body["serial"]
        _log_event("unregister", serial, "")
        db.execute("DELETE FROM agents WHERE serial = ?", (serial,))
        db.commit()
        self._json_response({"ok": True})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

_start_time = time.time()


def main():
    global db, _start_time
    _start_time = time.time()
    db = _init_db()

    _log_event("broker_start", "", f"port={PORT}")
    db.commit()

    _clean_stale()
    _schedule_cleanup()

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
