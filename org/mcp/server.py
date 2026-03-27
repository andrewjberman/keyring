"""
Opal Agent MCP Server -- Inter-agent communication for the Opal Capital org.

Exposes tools that let any agent query another agent's status, read logs,
check task orders, and leave async messages. Eliminates Andrew as the
intermediary for routine agent-to-agent coordination.

v2: Adds liveness tracking, agent summaries, and channel push notifications
    (inspired by claude-peers-mcp). Agents that call register_agent on startup
    appear as "live" and receive instant message push via MCP channel.

v3: Adds broker integration for cross-session message routing. The broker
    (broker.py) is a singleton HTTP server on localhost:7800 backed by SQLite.
    Auto-launched by register_agent if not already running. Each MCP server
    polls the broker every 2s for inbound messages and pushes them via
    MCP channel notification into the active Claude session.

Run: python org/mcp/server.py
Transport: stdio (Claude Code connects directly)
"""

import os
import re
import json
import time
import asyncio
import signal
import logging
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from contextlib import contextmanager

# File locking — use a separate .lock file so the lock covers the entire
# read-modify-write cycle. msvcrt.locking on the data file itself only
# locks 1 byte, which is insufficient when 5+ pollers write concurrently.
import time as _time
LOCK_FILE = Path(__file__).resolve().parent / "liveness.lock"

from mcp.server.fastmcp import FastMCP, Context

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ORG_ROOT = Path(__file__).resolve().parent.parent          # org/
WORKSPACE_ROOT = ORG_ROOT.parent                           # ajb_workspace/
INBOX_DIR = Path(__file__).resolve().parent / "inbox"
INBOX_DIR.mkdir(exist_ok=True)
LIVENESS_FILE = Path(__file__).resolve().parent / "liveness.json"
BROKER_SCRIPT = Path(__file__).resolve().parent / "broker.py"
BROKER_PORT = int(os.environ.get("OPAL_BROKER_PORT", "7800"))
BROKER_URL = f"http://127.0.0.1:{BROKER_PORT}"
POLL_INTERVAL_S = 2.0  # seconds between broker polls

TIER_DIRS = {
    "tier1_exec": ORG_ROOT / "tier1_exec",
    "tier2_senior": ORG_ROOT / "tier2_senior",
    "tier3_junior": ORG_ROOT / "tier3_junior",
}

# Liveness thresholds (seconds)
STALE_THRESHOLD = 120      # 2 min without heartbeat = stale
DEAD_THRESHOLD = 600       # 10 min = presumed dead, cleaned on next access

log = logging.getLogger("opal-agent-comms")

# ---------------------------------------------------------------------------
# Liveness registry (JSON file, atomic read/write)
# ---------------------------------------------------------------------------

@contextmanager
def _locked_liveness(write=False):
    """Read (and optionally write) liveness.json with file locking.
    Yields the parsed dict. If write=True, the dict is written back on exit.
    Uses a separate .lock file for mutual exclusion (msvcrt 1-byte lock
    on the data file itself is insufficient with 5+ concurrent pollers)."""
    LIVENESS_FILE.touch(exist_ok=True)
    LOCK_FILE.touch(exist_ok=True)
    lock_fh = open(LOCK_FILE, "r+", encoding="utf-8")
    try:
        if sys.platform == "win32":
            import msvcrt
            for _ in range(50):
                try:
                    msvcrt.locking(lock_fh.fileno(), msvcrt.LK_NBLCK, 1)
                    break
                except OSError:
                    _time.sleep(0.05)
            else:
                msvcrt.locking(lock_fh.fileno(), msvcrt.LK_LOCK, 1)
        else:
            import fcntl
            fcntl.flock(lock_fh.fileno(), fcntl.LOCK_EX)

        raw = LIVENESS_FILE.read_text(encoding="utf-8").strip()
        data = json.loads(raw) if raw else {}
        yield data
        if write:
            LIVENESS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    finally:
        try:
            if sys.platform == "win32":
                import msvcrt
                lock_fh.seek(0)
                msvcrt.locking(lock_fh.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(lock_fh.fileno(), fcntl.LOCK_UN)
        except Exception:
            pass
        lock_fh.close()


def _clean_stale(data: dict) -> None:
    """Remove entries that exceed DEAD_THRESHOLD. Mutates data in place."""
    now = time.time()
    dead = [
        serial for serial, info in data.items()
        if now - info.get("last_seen_epoch", 0) > DEAD_THRESHOLD
    ]
    for serial in dead:
        del data[serial]


def _liveness_status(info: dict) -> str:
    """Return 'live', 'stale', or 'dead' based on last_seen_epoch."""
    elapsed = time.time() - info.get("last_seen_epoch", 0)
    if elapsed < STALE_THRESHOLD:
        return "live"
    elif elapsed < DEAD_THRESHOLD:
        return "stale"
    return "dead"


# ---------------------------------------------------------------------------
# Broker client (HTTP calls to localhost broker for cross-session routing)
# ---------------------------------------------------------------------------

_broker_available = False  # set True after successful health check


def _broker_fetch(path: str, body: dict | None = None, timeout: float = 3.0) -> dict | list | None:
    """POST JSON to the broker. Returns parsed response or None on failure."""
    url = f"{BROKER_URL}{path}"
    data = json.dumps(body or {}).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, method="POST",
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


def _broker_health() -> bool:
    """Check if the broker is running."""
    try:
        req = urllib.request.Request(f"{BROKER_URL}/health")
        with urllib.request.urlopen(req, timeout=2) as resp:
            data = json.loads(resp.read())
            return data.get("status") == "ok"
    except Exception:
        return False


def _ensure_broker() -> bool:
    """Start the broker if it's not already running. Returns True if available."""
    global _broker_available
    if _broker_health():
        _broker_available = True
        return True

    log.info("Starting broker daemon...")
    try:
        # Launch broker as detached subprocess
        if sys.platform == "win32":
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            DETACHED_PROCESS = 0x00000008
            subprocess.Popen(
                [sys.executable, str(BROKER_SCRIPT)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                creationflags=CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS,
            )
        else:
            subprocess.Popen(
                [sys.executable, str(BROKER_SCRIPT)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                start_new_session=True,
            )

        # Wait for it to come up (up to 5 seconds)
        for _ in range(25):
            time.sleep(0.2)
            if _broker_health():
                _broker_available = True
                log.info("Broker started successfully")
                return True

        log.warning("Broker failed to start within 5 seconds")
        return False

    except Exception as e:
        log.warning(f"Failed to launch broker: {e}")
        return False


# ---------------------------------------------------------------------------
# Channel push (experimental claude/channel notification)
# ---------------------------------------------------------------------------

# Holds the Context from the most recent tool call so we can push
# notifications outside of a tool handler (e.g., from send_message).
_active_ctx: Context | None = None
_my_serial: str | None = None  # set on register_agent, used by polling loop
_poll_task: asyncio.Task | None = None

# ---------------------------------------------------------------------------
# Message piggyback queue — broker poll stores messages here; next tool
# response prepends them so the agent sees them in-conversation instantly.
# ---------------------------------------------------------------------------
_piggyback_queue: list[dict] = []


def _drain_piggyback() -> str:
    """Drain the piggyback queue and return formatted urgent header.
    Returns empty string if no queued messages."""
    global _piggyback_queue
    if not _piggyback_queue:
        return ""
    msgs = _piggyback_queue[:]
    _piggyback_queue = []
    lines = [f"URGENT: {len(msgs)} message(s) received while idle:\n"]
    for msg in msgs:
        lines.append(f"--- Message from {msg.get('from_serial', '?')} ---")
        subj = msg.get("subject", "(no subject)")
        lines.append(f"Subject: {subj}")
        lines.append(msg.get("body", ""))
        lines.append("---\n")
    lines.append("Act on these messages NOW before proceeding with your response.\n\n")
    return "\n".join(lines)


async def _push_channel_message(
    content: str,
    source: str = "opal-agent-comms",
    meta: dict | None = None,
) -> bool:
    """Push an instant message into the active Claude session.
    Uses standard MCP logging (send_log_message) which is the official
    protocol mechanism for server-initiated messages to the client.
    Returns True if sent, False if no active session."""
    ctx = _active_ctx
    if ctx is None:
        return False
    try:
        session = ctx.session
        # Use standard MCP logging — the official server-to-client push mechanism.
        # Previous attempt used a custom 'notifications/claude/channel' method
        # which Claude Code silently ignored (non-standard).
        await session.send_log_message(
            level="warning",
            data=content,
            logger=source,
        )
        return True
    except Exception as e:
        log.warning(f"Channel push failed: {e}")
        return False


async def _poll_broker_loop():
    """Background loop: poll broker for inbound messages.
    Runs every POLL_INTERVAL_S seconds while this MCP server is alive.

    Delivery strategy (dual path):
    1. Queue messages for piggyback — the next MCP tool call response will
       prepend them, guaranteeing the agent sees them in-conversation.
    2. Also attempt channel push (best-effort) — if Claude Code ever supports
       server-initiated notifications, this gives instant delivery.
    """
    while True:
        await asyncio.sleep(POLL_INTERVAL_S)
        if not _broker_available or not _my_serial:
            continue
        try:
            result = _broker_fetch("/poll-messages", {"serial": _my_serial})
            if not result or not result.get("messages"):
                continue
            for msg in result["messages"]:
                # Primary: queue for piggyback on next tool response
                _piggyback_queue.append({
                    "from_serial": msg["from_serial"],
                    "to_serial": msg["to_serial"],
                    "subject": msg.get("subject", ""),
                    "body": msg["body"],
                    "sent_at": msg.get("sent_at", ""),
                })

                # Secondary: attempt channel push (best-effort, may not work)
                await _push_channel_message(
                    content=f"Message from {msg['from_serial']}: [{msg.get('subject', '')}] {msg['body']}",
                    meta={
                        "from_agent": msg["from_serial"],
                        "to_agent": msg["to_serial"],
                        "subject": msg.get("subject", ""),
                        "sent_at": msg["sent_at"],
                    },
                )
        except Exception as e:
            log.debug(f"Broker poll error: {e}")


# ---------------------------------------------------------------------------
# Helpers (original)
# ---------------------------------------------------------------------------

def _resolve_agent_folder(agent_serial: str) -> Path | None:
    """Find an agent's folder across all tier directories."""
    for tier_dir in TIER_DIRS.values():
        if not tier_dir.exists():
            continue
        for d in tier_dir.iterdir():
            if d.is_dir() and d.name == agent_serial:
                return d
    # Fuzzy match -- serial might be a prefix
    for tier_dir in TIER_DIRS.values():
        if not tier_dir.exists():
            continue
        for d in tier_dir.iterdir():
            if d.is_dir() and d.name.startswith(agent_serial):
                return d
    return None


def _latest_log_folder(agent_folder: Path) -> Path | None:
    """Return the most recent date folder under agent/logs/."""
    logs_dir = agent_folder / "logs"
    if not logs_dir.exists():
        return None
    date_folders = sorted(
        [d for d in logs_dir.iterdir() if d.is_dir()],
        key=lambda d: d.name,
        reverse=True,
    )
    return date_folders[0] if date_folders else None


def _read_file_truncated(path: Path, max_lines: int = 200) -> str:
    """Read a file, truncating to max_lines."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        if len(lines) > max_lines:
            return "\n".join(lines[:max_lines]) + f"\n\n... truncated ({len(lines)} total lines)"
        return text
    except Exception as e:
        return f"ERROR reading {path}: {e}"


def _list_task_orders(agent_folder: Path, status_filter: str | None = None,
                      project_filter: str | None = None) -> list[dict]:
    """Parse task orders from an agent's task_orders/ folder."""
    to_dir = agent_folder / "task_orders"
    if not to_dir.exists():
        return []
    results = []
    for f in sorted(to_dir.iterdir()):
        if not f.name.endswith(".md"):
            continue
        if project_filter and not f.name.startswith(project_filter):
            continue
        content = f.read_text(encoding="utf-8", errors="replace")
        # Extract status
        status_match = re.search(r"<status>(.*?)</status>", content)
        status = status_match.group(1).strip() if status_match else "unknown"
        if status_filter and status != status_filter:
            continue
        # Extract issued_by
        issued_match = re.search(r"<issued_by>(.*?)</issued_by>", content)
        issued_by = issued_match.group(1).strip() if issued_match else "unknown"
        # Extract objective (first 200 chars)
        obj_match = re.search(r"<objective>(.*?)</objective>", content, re.DOTALL)
        objective = obj_match.group(1).strip()[:200] if obj_match else ""
        results.append({
            "file": f.name,
            "status": status,
            "issued_by": issued_by,
            "objective_preview": objective,
        })
    return results


# ---------------------------------------------------------------------------
# MCP Server
# ---------------------------------------------------------------------------

mcp = FastMCP("opal-agent-comms")


# ---- Liveness tools (new) ------------------------------------------------

@mcp.tool()
async def register_agent(
    agent_serial: str,
    summary: str = "",
    ctx: Context = None,
) -> str:
    """Register this agent as live. Call once at session startup.
    Sets PID, timestamp, and optional work summary visible to all agents.
    Enables instant message push via MCP channel notifications.
    Auto-launches the broker daemon for cross-session message routing."""
    global _active_ctx, _my_serial, _poll_task
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found in org hierarchy."

    _my_serial = folder.name

    # Update liveness.json (local file, always works)
    now = time.time()
    with _locked_liveness(write=True) as data:
        _clean_stale(data)
        data[folder.name] = {
            "pid": os.getpid(),
            "summary": summary,
            "registered_at": datetime.now(timezone.utc).isoformat(),
            "last_seen": datetime.now(timezone.utc).isoformat(),
            "last_seen_epoch": now,
        }

    # Start broker and register with it (for cross-session messaging)
    broker_status = "unavailable"
    if _ensure_broker():
        result = _broker_fetch("/register", {
            "serial": folder.name,
            "pid": os.getpid(),
            "summary": summary,
        })
        if result and result.get("ok"):
            broker_status = f"connected (port {BROKER_PORT})"

            # Start background polling loop for inbound cross-session messages
            if _poll_task is None or _poll_task.done():
                loop = asyncio.get_event_loop()
                _poll_task = loop.create_task(_poll_broker_loop())
        else:
            broker_status = "registration failed"

    return (
        f"Registered {folder.name} as live (PID {os.getpid()}).\n"
        f"Summary: {summary or '(none)'}\n"
        f"Broker: {broker_status}\n"
        f"Channel push: enabled. Call heartbeat() periodically to stay live."
    )


@mcp.tool()
async def heartbeat(
    agent_serial: str,
    summary: str = "",
    ctx: Context = None,
) -> str:
    """Update last-seen timestamp. Optionally update work summary.
    Call periodically (recommended: every 30-60s) to stay in 'live' state.
    If not called for 2 min, status degrades to 'stale'."""
    global _active_ctx
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found."

    now = time.time()
    with _locked_liveness(write=True) as data:
        _clean_stale(data)
        if folder.name not in data:
            return f"{folder.name} is not registered. Call register_agent first."
        entry = data[folder.name]
        entry["last_seen"] = datetime.now(timezone.utc).isoformat()
        entry["last_seen_epoch"] = now
        if summary:
            entry["summary"] = summary

    # Also heartbeat the broker (best-effort)
    if _broker_available:
        payload = {"serial": folder.name}
        if summary:
            payload["summary"] = summary
        _broker_fetch("/heartbeat", payload)

    urgent = _drain_piggyback()
    if urgent:
        return urgent + f"Heartbeat OK for {folder.name}."
    return f"Heartbeat OK for {folder.name}."


@mcp.tool()
async def set_summary(
    agent_serial: str,
    summary: str,
    ctx: Context = None,
) -> str:
    """Update this agent's work summary. Visible to all agents via
    get_live_agents and get_agent_status. Keep it to 1-2 sentences
    describing current task (e.g., 'Running gold layer for ADVI_PRICES')."""
    global _active_ctx
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found."

    with _locked_liveness(write=True) as data:
        if folder.name not in data:
            return f"{folder.name} is not registered. Call register_agent first."
        data[folder.name]["summary"] = summary

    return f"Summary updated for {folder.name}: \"{summary}\""


@mcp.tool()
async def get_live_agents(pod: str = "", ctx: Context = None) -> str:
    """List all agents currently registered as live or stale, with their
    summaries, last-seen times, and PIDs. Use for situational awareness
    before sending messages or issuing task orders.

    Optional pod filter: pass a pod number (e.g., '4') to see only that
    pod's agents plus CTO/COO. Omit to see all."""
    global _active_ctx
    _active_ctx = ctx

    pod_num = int(pod) if pod else None

    with _locked_liveness(write=True) as data:
        _clean_stale(data)

    # Re-read after cleanup (released lock)
    with _locked_liveness() as data:
        if not data:
            return "No agents currently registered as live."

        # Filter by pod if requested
        filtered = {}
        for serial, info in data.items():
            if pod_num is not None:
                # Tier 1 (CTO/COO) always pass
                if serial.startswith(("1.0.0_", "2.0.0_")):
                    filtered[serial] = info
                else:
                    try:
                        parts = serial.split("_", 1)[0].split(".")
                        if int(parts[1]) == pod_num:
                            filtered[serial] = info
                    except (IndexError, ValueError):
                        filtered[serial] = info
            else:
                filtered[serial] = info

        if not filtered:
            return f"No live agents found{f' for pod {pod_num}' if pod_num else ''}."

        header = f"# Live agents ({len(filtered)} shown"
        if pod_num is not None and len(filtered) < len(data):
            header += f", {len(data) - len(filtered)} in other pods"
        header += ")\n"

        lines = [header]
        for serial, info in sorted(filtered.items()):
            status = _liveness_status(info)
            elapsed = int(time.time() - info.get("last_seen_epoch", 0))
            marker = "LIVE" if status == "live" else "STALE"
            lines.append(f"- **{serial}** [{marker}] (PID {info.get('pid', '?')}, {elapsed}s ago)")
            if info.get("summary"):
                lines.append(f"  Summary: {info['summary']}")

        return "\n".join(lines)


# ---- Original tools (enhanced) -------------------------------------------

@mcp.tool()
async def get_agent_status(agent_serial: str, ctx: Context = None) -> str:
    """Get an agent's current status: liveness, summary, latest log summary,
    pending task orders, and blockers. Use this on startup to check
    downstream/upstream agents."""
    global _active_ctx
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found in org hierarchy."

    urgent = _drain_piggyback()
    parts = []
    if urgent:
        parts.append(urgent)
    parts.append(f"# Status: {folder.name}\n")

    # Liveness info
    with _locked_liveness() as data:
        info = data.get(folder.name)
    if info:
        status = _liveness_status(info)
        elapsed = int(time.time() - info.get("last_seen_epoch", 0))
        marker = {"live": "LIVE", "stale": "STALE", "dead": "OFFLINE"}[status]
        parts.append(f"**Liveness:** {marker} (last seen {elapsed}s ago, PID {info.get('pid', '?')})")
        if info.get("summary"):
            parts.append(f"**Working on:** {info['summary']}")
        parts.append("")
    else:
        parts.append("**Liveness:** NOT REGISTERED (agent has not called register_agent)\n")

    # Latest log
    log_folder = _latest_log_folder(folder)
    if log_folder:
        log_files = sorted(log_folder.iterdir())
        parts.append(f"## Latest logs ({log_folder.name})")
        for lf in log_files:
            if lf.suffix == ".md":
                parts.append(f"\n### {lf.name}")
                # Extract Status and Blockers sections
                content = lf.read_text(encoding="utf-8", errors="replace")
                for section in ["Current State", "Blockers", "Next Steps"]:
                    pattern = rf"## {section}\s*\n(.*?)(?=\n## |\Z)"
                    match = re.search(pattern, content, re.DOTALL)
                    if match:
                        text = match.group(1).strip()
                        if len(text) > 500:
                            text = text[:500] + "..."
                        parts.append(f"**{section}:**\n{text}\n")
    else:
        parts.append("No logs found.")

    # Pending task orders
    pending = _list_task_orders(folder, status_filter="pending")
    if pending:
        parts.append(f"## Pending task orders ({len(pending)})")
        for to in pending:
            parts.append(f"- `{to['file']}` (from {to['issued_by']}): {to['objective_preview'][:120]}...")
    else:
        parts.append("## No pending task orders")

    # Check inbox
    inbox = INBOX_DIR / folder.name
    if inbox.exists():
        messages = sorted(inbox.iterdir())
        unread = [m for m in messages if m.suffix == ".md"]
        if unread:
            parts.append(f"\n## Inbox ({len(unread)} messages)")
            for msg in unread[-5:]:  # Show last 5
                parts.append(f"- {msg.name}")

    return "\n".join(parts)


@mcp.tool()
async def read_agent_latest_log(agent_serial: str, log_name: str = "", ctx: Context = None) -> str:
    """Read the full content of an agent's most recent log. If log_name is
    provided, reads that specific log file; otherwise reads all logs from
    the latest date folder."""
    global _active_ctx
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found."

    log_folder = _latest_log_folder(folder)
    if not log_folder:
        return f"No logs found for {agent_serial}."

    if log_name:
        target = log_folder / log_name
        if not target.exists():
            # Try fuzzy match
            matches = [f for f in log_folder.iterdir() if log_name.lower() in f.name.lower()]
            if matches:
                target = matches[0]
            else:
                return f"Log '{log_name}' not found in {log_folder.name}/. Available: {[f.name for f in log_folder.iterdir()]}"
        return f"# {target.name}\n\n{_read_file_truncated(target)}"

    # Read all logs from latest date
    parts = [f"# All logs from {log_folder.name} for {folder.name}\n"]
    for lf in sorted(log_folder.iterdir()):
        if lf.suffix == ".md":
            parts.append(f"---\n## {lf.name}\n")
            parts.append(_read_file_truncated(lf, max_lines=150))
    return "\n".join(parts)


@mcp.tool()
async def list_task_orders(
    agent_serial: str,
    status: str = "",
    project: str = "",
    ctx: Context = None,
) -> str:
    """List task orders for an agent. Optionally filter by status
    ('pending'/'complete') and/or project code prefix (e.g., 'ADVI_PRICES')."""
    global _active_ctx
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found."

    orders = _list_task_orders(
        folder,
        status_filter=status or None,
        project_filter=project or None,
    )
    if not orders:
        filters = []
        if status:
            filters.append(f"status={status}")
        if project:
            filters.append(f"project={project}")
        filter_str = f" (filters: {', '.join(filters)})" if filters else ""
        return f"No task orders found for {agent_serial}{filter_str}."

    lines = [f"# Task orders for {folder.name}\n"]
    for o in orders:
        lines.append(f"- [{o['status'].upper()}] `{o['file']}` (from {o['issued_by']})")
        if o["objective_preview"]:
            lines.append(f"  {o['objective_preview'][:150]}")
    return "\n".join(lines)


@mcp.tool()
async def query_project(project_code: str, ctx: Context = None) -> str:
    """Get full project status: JSON metadata, registry row, and all related
    task orders across every agent."""
    global _active_ctx
    _active_ctx = ctx

    projects_dir = ORG_ROOT / "projects"
    json_path = projects_dir / f"{project_code}.json"

    parts = [f"# Project: {project_code}\n"]

    # Project JSON
    if json_path.exists():
        data = json.loads(json_path.read_text(encoding="utf-8"))
        parts.append(f"**Name:** {data.get('name', '?')}")
        parts.append(f"**Status:** {data.get('status', '?')}")
        parts.append(f"**Phase:** {data.get('phase', '?')}")
        parts.append(f"**Blocking:** {data.get('blocking', 'none')}")
        parts.append(f"**Pods:** {data.get('pods', [])}")
        parts.append(f"**Pipeline:** {data.get('pipeline', '?')}")
        if data.get("threads"):
            parts.append(f"**Threads:** {len(data['threads'])}")
            for t in data["threads"]:
                parts.append(f"  - {t.get('serial', '?')}: {t.get('topic', '?')} [{t.get('status', '?')}]")
    else:
        parts.append(f"No project JSON found at {json_path}")

    # Find all task orders referencing this project across all agents
    parts.append(f"\n## Task orders for {project_code}\n")
    found = False
    for tier_dir in TIER_DIRS.values():
        if not tier_dir.exists():
            continue
        for agent_dir in sorted(tier_dir.iterdir()):
            if not agent_dir.is_dir():
                continue
            orders = _list_task_orders(agent_dir, project_filter=project_code)
            if orders:
                found = True
                for o in orders:
                    parts.append(
                        f"- **{agent_dir.name}** [{o['status'].upper()}] `{o['file']}`"
                    )
    if not found:
        parts.append("No task orders found.")

    return "\n".join(parts)


@mcp.tool()
async def send_message(
    from_agent: str,
    to_agent: str,
    subject: str,
    body: str,
    ctx: Context = None,
) -> str:
    """Send an async message to another agent. The message is stored in their
    inbox and will be surfaced when they next call get_agent_status or
    check_inbox.

    If the recipient is registered as LIVE, the message is also pushed
    instantly via MCP channel notification (no polling required).

    Use this for status updates, questions, or handoff notes."""
    global _active_ctx
    _active_ctx = ctx

    to_folder = _resolve_agent_folder(to_agent)
    if not to_folder:
        return f"Recipient '{to_agent}' not found in org."

    inbox = INBOX_DIR / to_folder.name
    inbox.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    safe_from = re.sub(r"[^a-zA-Z0-9._-]", "_", from_agent)
    safe_subject = re.sub(r"[^a-zA-Z0-9._-]", "_", subject)[:40]
    filename = f"{ts}_{safe_from}_{safe_subject}.md"

    msg_path = inbox / filename
    msg_content = (
        f"# Message from {from_agent}\n"
        f"**To:** {to_folder.name}\n"
        f"**Date:** {ts}\n"
        f"**Subject:** {subject}\n\n"
        f"{body}\n"
    )
    msg_path.write_text(msg_content, encoding="utf-8")

    # Route through broker for cross-session delivery (recipient's MCP
    # server polls the broker and pushes via channel into their session)
    delivery_methods = ["filesystem"]

    if _broker_available:
        result = _broker_fetch("/send-message", {
            "from_serial": from_agent,
            "to_serial": to_folder.name,
            "subject": subject,
            "text": body,
        })
        if result and result.get("ok"):
            delivery_methods.append("broker")

    # Also attempt direct channel push if recipient is in THIS session
    # (same-session push is instant, no broker round-trip needed)
    with _locked_liveness() as data:
        recipient_info = data.get(to_folder.name)

    if recipient_info and _liveness_status(recipient_info) == "live":
        pushed = await _push_channel_message(
            content=f"Message from {from_agent}: [{subject}] {body}",
            meta={
                "from_agent": from_agent,
                "to_agent": to_folder.name,
                "subject": subject,
                "inbox_file": filename,
            },
        )
        if pushed:
            delivery_methods.append("channel push")

    return f"Message delivered to {to_folder.name} inbox: {filename} ({' + '.join(delivery_methods)})"


@mcp.tool()
async def check_inbox(agent_serial: str, mark_read: bool = False, ctx: Context = None) -> str:
    """Check an agent's inbox for pending messages. Set mark_read=True to
    archive messages after reading (moves to inbox/read/)."""
    global _active_ctx
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found."

    inbox = INBOX_DIR / folder.name
    if not inbox.exists():
        return f"No inbox for {folder.name} (no messages received)."

    urgent = _drain_piggyback()

    messages = sorted([f for f in inbox.iterdir() if f.suffix == ".md"])
    if not messages:
        if urgent:
            return urgent + f"Inbox empty for {folder.name} (broker messages shown above)."
        return f"Inbox empty for {folder.name}."

    parts = []
    if urgent:
        parts.append(urgent)
    parts.append(f"# Inbox for {folder.name} ({len(messages)} messages)\n")
    for msg in messages:
        parts.append(f"---\n## {msg.name}\n")
        parts.append(msg.read_text(encoding="utf-8", errors="replace"))

    if mark_read and messages:
        read_dir = inbox / "read"
        read_dir.mkdir(exist_ok=True)
        for msg in messages:
            msg.rename(read_dir / msg.name)
        parts.append(f"\n--- Archived {len(messages)} messages to read/")

    return "\n".join(parts)


@mcp.tool()
async def list_agents(tier: str = "", ctx: Context = None) -> str:
    """List all agents in the org, optionally filtered by tier
    ('tier1_exec', 'tier2_senior', 'tier3_junior'). Returns agent serial,
    role, latest log date, and liveness status."""
    global _active_ctx
    _active_ctx = ctx

    # Load liveness data once
    with _locked_liveness() as live_data:
        pass  # just read

    results = []
    dirs = {tier: TIER_DIRS[tier]} if tier and tier in TIER_DIRS else TIER_DIRS

    for tier_name, tier_dir in dirs.items():
        if not tier_dir.exists():
            continue
        for agent_dir in sorted(tier_dir.iterdir()):
            if not agent_dir.is_dir():
                continue
            log_folder = _latest_log_folder(agent_dir)
            latest_date = log_folder.name if log_folder else "no logs"
            pending_count = len(_list_task_orders(agent_dir, status_filter="pending"))

            # Liveness badge
            info = live_data.get(agent_dir.name)
            if info:
                status = _liveness_status(info)
                badge = {"live": "[LIVE]", "stale": "[STALE]", "dead": "[OFFLINE]"}[status]
            else:
                badge = ""

            results.append(
                f"- **{agent_dir.name}** {badge} ({tier_name}) "
                f"| last log: {latest_date} | pending TOs: {pending_count}"
            )

    if not results:
        return "No agents found."

    return f"# Org agents ({len(results)} total)\n\n" + "\n".join(results)


@mcp.tool()
async def get_org_summary(ctx: Context = None) -> str:
    """Get a high-level org summary: live agents, active projects, their
    statuses, and agents with pending work. Quick situational awareness tool."""
    global _active_ctx
    _active_ctx = ctx

    parts = ["# Org Summary\n"]

    # Live agents
    with _locked_liveness(write=True) as data:
        _clean_stale(data)

    with _locked_liveness() as data:
        if data:
            parts.append(f"## Live agents ({len(data)})\n")
            for serial, info in sorted(data.items()):
                status = _liveness_status(info)
                marker = "LIVE" if status == "live" else "STALE"
                summary = info.get("summary", "")
                line = f"- **{serial}** [{marker}]"
                if summary:
                    line += f" -- {summary}"
                parts.append(line)
            parts.append("")

    # Active projects
    projects_dir = ORG_ROOT / "projects"
    registry = projects_dir / "REGISTRY.md"
    if registry.exists():
        content = registry.read_text(encoding="utf-8", errors="replace")
        # Extract active projects table
        active_match = re.search(
            r"## Active Projects\s*\n\n\|.*?\n\|.*?\n(.*?)(?=\n---|\n## |\Z)",
            content, re.DOTALL,
        )
        if active_match:
            parts.append("## Active Projects\n")
            parts.append("| Project | Phase | Blocking |")
            parts.append("|---------|-------|----------|")
            for line in active_match.group(1).strip().splitlines():
                cols = [c.strip() for c in line.split("|")]
                if len(cols) >= 7:
                    code = cols[1]
                    phase = cols[4][:80] + "..." if len(cols[4]) > 80 else cols[4]
                    blocking = cols[6][:60] + "..." if len(cols[6]) > 60 else cols[6]
                    parts.append(f"| {code} | {phase} | {blocking} |")

    # Agents with pending work
    parts.append("\n## Agents with pending task orders\n")
    for tier_dir in TIER_DIRS.values():
        if not tier_dir.exists():
            continue
        for agent_dir in sorted(tier_dir.iterdir()):
            if not agent_dir.is_dir():
                continue
            pending = _list_task_orders(agent_dir, status_filter="pending")
            if pending:
                parts.append(f"**{agent_dir.name}** ({len(pending)} pending):")
                for p in pending:
                    parts.append(f"  - `{p['file']}`")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run(transport="stdio")
