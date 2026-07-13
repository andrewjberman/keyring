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

from __future__ import annotations

import os
import re
import json
import time
import asyncio
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

from mcp.server.fastmcp import FastMCP, Context  # noqa: E402  (after LOCK_FILE by design)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ORG_ROOT = Path(__file__).resolve().parent.parent          # org/
WORKSPACE_ROOT = ORG_ROOT.parent                           # ajb_workspace/
INBOX_DIR = Path(__file__).resolve().parent / "inbox"
INBOX_DIR.mkdir(exist_ok=True)
LIVENESS_FILE = Path(__file__).resolve().parent / "liveness.json"
BROKER_SCRIPT = Path(__file__).resolve().parent / "broker.py"
# NFRA_CMTQUE commit-worker daemon (MSTR internal-ops lane, LD-0246/0251; singleton v2 verified).
COMMIT_WORKER = Path(__file__).resolve().parents[2] / ".tools" / "commit-worker.sh"  # repo/.tools/
CQ_HB_STALE_SEC = 30
BROKER_PORT = int(os.environ.get("OPAL_BROKER_PORT", "7800"))
BROKER_URL = f"http://127.0.0.1:{BROKER_PORT}"
POLL_INTERVAL_S = 2.0  # seconds between broker polls

# tier0_exec holds ONLY the Tier-0 agent (0.0.0_AB_MSTR), so the broker can
# resolve / register / message it. It is deliberately SEPARATE from org/tier0/
# (the Constitution + ledger/cycles/ratifications control plane) -- org/tier0/
# must never be scanned here, or its subdirs (audit/, cycles/, ledger/,
# ratifications/) would be mistaken for agent folders.
# tier0_utility holds the principal-facing Utility Agents (0.0.N_UA_<toolset>);
# it contains ONLY agent folders, so scanning it is safe (LD-0220, 2026-06-26).
TIER_DIRS = {
    "tier0_exec": ORG_ROOT / "tier0_exec",
    "tier0_utility": ORG_ROOT / "tier0_utility",
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

def _safe_json_loads(raw: str, backup_path: Path | None = None) -> dict:
    """Parse JSON with fallback for trailing-garbage corruption.
    When concurrent writers race on liveness.json, the file can end up with
    extra trailing characters (e.g., '}}' instead of '}'). This tries the
    fast path first, then progressively strips trailing bytes.

    F2 (LD-0202): when a NON-empty file is corrupt beyond repair this returns
    {}, and a subsequent write=True would then OVERWRITE the file with {},
    SILENTLY + UNRECOVERABLY wiping every live agent. If backup_path is given,
    preserve the corrupt bytes to a `.corrupt` sidecar first so the entries are
    recoverable. (The freeze-vs-reset write policy on a detected-corrupt file is
    flagged as a follow-on; this change is pure data-preservation, no behavior
    change to the normal or write path.)"""
    raw = raw.strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Try stripping trailing characters one at a time (up to 8)
        for i in range(1, 9):
            try:
                return json.loads(raw[:-i])
            except (json.JSONDecodeError, ValueError):
                continue
        if backup_path is not None:
            try:
                corrupt_sidecar = backup_path.parent / (backup_path.name + ".corrupt")
                corrupt_sidecar.write_text(raw, encoding="utf-8")
                log.warning("liveness.json corrupt beyond repair -- preserved bytes to %s "
                            "before {} fallback (recovery source)", corrupt_sidecar.name)
            except OSError:
                log.warning("liveness.json corrupt beyond repair AND .corrupt backup failed")
        else:
            log.warning("liveness.json is corrupted beyond repair, resetting to {}")
        return {}


@contextmanager
def _locked_liveness(write=False):
    """Read (and optionally write) liveness.json with file locking.
    Yields the parsed dict. If write=True, the dict is written back on exit.
    Uses a separate .lock file for mutual exclusion (msvcrt 1-byte lock
    on the data file itself is insufficient with 5+ concurrent pollers).
    Writes use atomic rename (write to .tmp, then os.replace) to prevent
    partial-write corruption when the new content is shorter than the old."""
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
        data = _safe_json_loads(raw, backup_path=LIVENESS_FILE)
        yield data
        if write:
            tmp = LIVENESS_FILE.with_suffix(".json.tmp")
            tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
            os.replace(str(tmp), str(LIVENESS_FILE))
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
# NFRA_IDENTITY.G-A -- broker-side PID identity guard (the enforcing chokepoint).
# ---------------------------------------------------------------------------
# The 2026-07-12/13 SEV: a compacted session re-derived its serial from the SHARED
# .comp-graph/.agent_context and operated as ANOTHER agent for ~9h. Nothing checked
# the claim against the broker, so the mis-adoption looked confirmed by every
# subsequent action (registration just OVERWROTE). The detection was available at
# every step and never fired: "is my PID already registered under a different
# serial?" -- one comparison catches the whole class mechanically.
# Design: 1.0.0_SA_CTO SEV_IDENTITY_MISADOPTION_GATE_20260713.md (d1aa23968).
#
# TWO directions, and they are DIFFERENT KINDS OF CLAIM. That is why they carry
# different severities (CTO arch-ruling 2026-07-13, on 0.7.0_AE_CloudOps~A's build):
#
#   (1) CROSS -- my PID is already LIVE under a DIFFERENT serial.  --> HARD REFUSE.
#       A LOGICAL impossibility: one process cannot be two agents. There is no
#       legitimate case, so a refusal here has no false-positive branch, and this
#       direction ALONE closes the 07-12/13 SEV (the phantom's FIRST registration
#       would have named the conflict). Refusing is risk-free.
#
#   (2) SERIAL HELD -- the claimed serial is LIVE under a DIFFERENT PID. --> ADVISORY.
#       An EMPIRICAL claim about the world, and it rests on a predicate that is
#       COARSER THAN THE CLAIM IT WOULD LICENSE: _pid_alive(pid) answers "does SOME
#       process hold this PID", NOT "is THAT AGENT alive". It cannot distinguish:
#         - the real incumbent (a true conflict),
#         - a lingering orphan MCP process from a dead session (fabric-demonstrated),
#         - a RECYCLED Windows PID now held by an unrelated process.
#       Its verdict is invariant under the thing we actually care about. A HARD
#       refusal on (2) would therefore block a LEGITIMATE respawn whenever the dead
#       incumbent's entry is still inside the 120s STALE_THRESHOLD and its PID
#       happens to resolve alive -- and the population most exposed to that is
#       agents that just died and are RESPAWNING. A guard that blocks the recovery
#       path converts a transient failure into a permanent one (the fabric silently
#       loses an agent: it never registers, so it is invisible to every scan -- the
#       exact "unresponsive agent" churn the SEV already cost us 9h on).
#       So (2) WARNS + AUDITS UNCONDITIONALLY and lets the registration proceed.
#
#       We go from ZERO signal on duplicate-serial collisions (today) to a logged,
#       measurable one -- WITHOUT adding a new way to lose an agent. The audit line
#       is what lets us MEASURE the collision rate; promote (2) to HARD only on that
#       evidence. (Banked lesson, applied verbatim: "measure the rate before sizing
#       the reaper" -- do not harden a gate against a rate nobody has measured.)


def _pid_alive(pid: int) -> bool:
    """True if the OS process exists. Cross-platform, no deps.

    NEVER uses os.kill on Windows (there, os.kill TERMINATES rather than probing).
    Returns True on an undeterminable probe so direction-(2) FAILS OPEN -- a guard
    that cannot tell must not refuse a legitimate restart.
    """
    if not pid or pid <= 0:
        return False
    try:
        if sys.platform.startswith("win"):
            import ctypes
            # PROCESS_QUERY_LIMITED_INFORMATION (0x1000) -- probe only, no side effects.
            handle = ctypes.windll.kernel32.OpenProcess(0x1000, False, int(pid))
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
                return True
            return False
        os.kill(int(pid), 0)  # POSIX: signal 0 = existence probe
        return True
    except (OSError, ProcessLookupError):
        return False
    except Exception:
        return True  # undeterminable -> fail OPEN (never block a legit restart)


def _identity_conflict(claimed_serial: str, data: dict, my_pid: int):
    """The guard. Returns (kind, message) or None if the claim is clean.

    kind is "CROSS" (hard-refuse) or "SERIAL_HELD" (advisory) -- see the severity
    rationale in the block comment above. The CALLER decides what to do with each;
    this function only classifies, so the severity policy is testable in isolation.

    Pure over (claimed_serial, liveness-dict, pid) so it is directly replay-testable.
    """
    # (1) CROSS: this PID is already live under a DIFFERENT serial. HARD.
    for serial, info in data.items():
        if serial == claimed_serial:
            continue
        if info.get("pid") == my_pid and _liveness_status(info) == "live":
            elapsed = int(time.time() - info.get("last_seen_epoch", 0))
            return ("CROSS", (
                f"IDENTITY CONFLICT -- NOT REGISTERED. PID {my_pid} is currently "
                f"{serial} (live {elapsed}s ago); you claimed {claimed_serial}. "
                f"A process cannot hold two identities. If you compacted and re-derived "
                f"your serial from .comp-graph/.agent_context, that file is SHARED and is "
                f"NOT an identity source -- you are {serial}. "
                f"Legitimate override: register_agent(..., identity_override=\"<reason>\") (audited)."
            ))
    # (2) SERIAL HELD by another process that still resolves alive. ADVISORY --
    # _pid_alive cannot tell a real incumbent from an orphan or a recycled PID,
    # so this WARNS and proceeds; it must never block a legitimate respawn.
    info = data.get(claimed_serial)
    if info and info.get("pid") and info.get("pid") != my_pid:
        if _liveness_status(info) == "live" and _pid_alive(info["pid"]):
            elapsed = int(time.time() - info.get("last_seen_epoch", 0))
            return ("SERIAL_HELD", (
                f"IDENTITY WARNING -- REGISTERED ANYWAY (advisory). {claimed_serial} was "
                f"already held by PID {info['pid']} (heartbeat {elapsed}s ago) and that PID "
                f"still resolves ALIVE; you are PID {my_pid}. This is NOT proof of a phantom: "
                f"the probe cannot distinguish a live incumbent from a lingering orphan MCP "
                f"process or a recycled OS PID, so it does not block you. But if you did NOT "
                f"expect to be sharing this serial, ONE of you is a phantom -- confirm which "
                f"(broker + org/mcp/agent-spawn-audit.log) BEFORE acting as {claimed_serial}. "
                f"Collision audited."
            ))
    return None


def _identity_decide(conflict, identity_override: str):
    """Map a classified conflict + override to an ACTION. Returns (action, message).

    action: ALLOW (clean) | REFUSE (hard-block, no state written)
          | OVERRIDE (a hard block that was explicitly forced -- audit, then proceed)
          | WARN (advisory -- audit, surface the warning, and PROCEED)

    THE SEVERITY RULING LIVES HERE AND NOWHERE ELSE. Both call sites (register_agent
    and heartbeat) route through it, so the policy cannot silently drift apart between
    them, and it is testable in isolation without writing to the real liveness.json.
    CTO arch-ruling 2026-07-13: CROSS is HARD (a logical impossibility -- no false-
    positive branch exists); SERIAL_HELD is ADVISORY (an empirical claim resting on a
    probe coarser than the claim -- must never block a legitimate respawn).
    """
    if not conflict:
        return ("ALLOW", "")
    kind, message = conflict
    if kind == "CROSS":
        return ("OVERRIDE", message) if identity_override else ("REFUSE", message)
    return ("WARN", message)


# Dedupe for the advisory audit: heartbeat fires every 30-60s, and a persistent
# SERIAL_HELD collision would otherwise write an audit row on every beat, burying
# the signal we added the row to measure. One row per (serial, other-pid) per window.
_IDENTITY_AUDIT_WINDOW = 300
_identity_audited: dict = {}

# --- THE DENOMINATOR (0.7.0_AE_CloudOps~A, 2026-07-13 -- he caught this in MY promotion path) ---
# The guard ACTIVATES per-session when the MCP server process starts and reads THIS FILE OFF DISK.
# It does NOT activate on the git land. (Demonstrated live: AE~A's session was served a register_agent
# schema carrying the G-A docstring while `git show HEAD:org/mcp/server.py | grep -c "IDENTITY GUARD"`
# returned 0 -- his uncommitted working-tree edit was already ENFORCING.)
#
# Consequence for the SERIAL_HELD promotion path: a server that started on the PRE-audit build
# ENFORCES but does NOT RECORD. So counting SERIAL_HELD rows against WALL-CLOCK systematically
# UNDERSTATES the collision rate -- and understates it most in the window where sessions are still
# running the un-auditing build. A quiet log would be indistinguishable from "no session was running
# the auditing code yet."  ==> That is, exactly, an instrument whose verdict cannot see the
# distinction it is being asked to license -- the same class the guard's own severity ruling turns on.
#
# So: every server process that arms the guard writes ONE `IDENTITY_GUARD_ACTIVE` row stamped with the
# guard version. The denominator is COUNTABLE from the log itself, not inferred from wall-clock:
#     denominator = grep -c "IDENTITY_GUARD_ACTIVE .*guard=GA-2"   (server-starts running the auditing build)
#     numerator   = grep -c "IDENTITY_SERIAL_HELD"                 (collisions those servers actually saw)
# NEVER promote direction (2) to HARD off a row count that cannot show its denominator.
_GUARD_VERSION = "GA-2"   # GA-1 = classify+refuse-both (as-built); GA-2 = CTO severity ruling + unconditional audit
_guard_active_logged = False


def _audit_identity(kind: str, claimed_serial: str, my_pid: int, reason: str, conflict: str) -> None:
    """Append an audited identity row. Best-effort -- never blocks registration.

    kind: CROSS_OVERRIDE (a hard refusal that was forced) | SERIAL_HELD (an advisory
    collision that proceeded). Both are audited; the SERIAL_HELD rows are the
    measurement that decides whether direction (2) ever earns a promotion to HARD.
    """
    try:
        if kind == "SERIAL_HELD":
            key = (claimed_serial, conflict)
            now = time.time()
            last = _identity_audited.get(key, 0)
            if now - last < _IDENTITY_AUDIT_WINDOW:
                return
            _identity_audited[key] = now
        line = (
            f"{datetime.now(timezone.utc).isoformat()} IDENTITY_{kind} "
            f"guard={_GUARD_VERSION} serial={claimed_serial} pid={my_pid} reason={reason!r} "
            f"conflict={(conflict.splitlines()[0] if conflict else '')!r}\n"
        )
        path = Path(__file__).resolve().parent / "agent-spawn-audit.log"
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(line)
    except Exception:
        pass


def _audit_guard_active(serial: str, my_pid: int) -> None:
    """Emit ONE row per server process recording that the guard armed, and at what version.

    This row IS the denominator (see the block comment above). Without it, a quiet
    SERIAL_HELD log cannot be distinguished from a log nobody was writing to.
    """
    global _guard_active_logged
    if _guard_active_logged:
        return
    _guard_active_logged = True
    try:
        line = (
            f"{datetime.now(timezone.utc).isoformat()} IDENTITY_GUARD_ACTIVE "
            f"guard={_GUARD_VERSION} serial={serial} pid={my_pid}\n"
        )
        path = Path(__file__).resolve().parent / "agent-spawn-audit.log"
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(line)
    except Exception:
        pass


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


def _commit_worker_alive() -> bool:
    """True iff a live commit-worker holds worker.pid with a fresh heartbeat (mirrors
    cq_worker_alive() in commit_queue_lib.sh). Heartbeat-freshness is the primary,
    win32-safe signal; the atomic mkdir worker.lock is the real singleton guard.
    (NFRA_CMTQUE TO-6 phase-1; authored by 0.7.0_AE_CloudOps~B, wired by MSTR.)"""
    try:
        gitdir = subprocess.check_output(
            ["git", "rev-parse", "--absolute-git-dir"],
            cwd=str(ORG_ROOT.parent), text=True, timeout=5,  # never let a hung git block register
        ).strip()
    except Exception:
        return False
    qroot = Path(gitdir) / "commit-queue"
    pidf, hbf = qroot / "worker.pid", qroot / "worker.hb"
    if not pidf.exists() or not hbf.exists():
        return False
    try:
        hb = int(hbf.read_text().strip())
    except (ValueError, OSError):
        return False
    return (time.time() - hb) < CQ_HB_STALE_SEC     # fresh heartbeat -> alive


def _ensure_commit_worker() -> bool:
    """Start the commit-worker daemon if it's not already live. Mirrors _ensure_broker().
    Best-effort: a launch failure NEVER blocks registration (the caller wraps it, and the
    safe-commit D6 fallback-to-mutex + the WorkerDown alarm cover a transient miss).
    Race-safe: the worker's atomic mkdir worker.lock makes a concurrent multi-launch a
    single-winner no-op (singleton v2 independently verified -- 12 racing -> 1 winner)."""
    if _commit_worker_alive():
        return True
    log.info("Starting commit-worker daemon...")
    try:
        if sys.platform == "win32":
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            DETACHED_PROCESS = 0x00000008
            subprocess.Popen(
                ["bash", str(COMMIT_WORKER), "--daemon"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL,
                creationflags=CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS,
            )
        else:
            subprocess.Popen(
                ["bash", str(COMMIT_WORKER), "--daemon"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL,
                start_new_session=True,
            )
        return True
    except Exception as exc:
        log.warning("commit-worker launch failed: %s", exc)
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

def _base_serial(agent_serial: str) -> str:
    """Strip instance suffix from a serial.  '0.4.0_DS_ClientPlatform~B' -> '0.4.0_DS_ClientPlatform'."""
    return agent_serial.split("~")[0]


def _instance_suffix(agent_serial: str) -> str | None:
    """Return the instance suffix if present.  '...~B' -> 'B', '...' -> None."""
    parts = agent_serial.split("~", 1)
    return parts[1] if len(parts) > 1 else None


def _identity_key(agent_serial: str, folder_name: str | None) -> str:
    """The key an agent is REGISTERED under -- liveness, broker, poller pattern.

    *** A FOLDER IS A FILE LOCATION. A SERIAL IS AN IDENTITY. *** Lanes SHARE a folder by design
    (they read the same role docs) and do NOT share a registration. Folding a lane onto its base
    folder-name is RV-0048 F-024: it made lane zombies immortal AND made deregistering a lane kill
    its BASE agent. register_agent stores the FULL suffixed serial; this must agree with it.

    A suffixed serial is returned VERBATIM. An unsuffixed one may be canonicalised via the folder
    (so a partial like '0.4.0_DS' resolves to '0.4.0_DS_ClientPlatform') -- that path cannot cross
    identities, because a base serial has no lane to be confused with.
    """
    if _instance_suffix(agent_serial):
        return agent_serial
    return folder_name or agent_serial


def _resolve_agent_folder(agent_serial: str) -> Path | None:
    """Find an agent's folder across all tier directories.
    Instance suffixes (e.g., ~B) are stripped before lookup so all instances
    of the same agent resolve to the same canonical folder."""
    base = _base_serial(agent_serial)
    for tier_dir in TIER_DIRS.values():
        if not tier_dir.exists():
            continue
        for d in tier_dir.iterdir():
            if d.is_dir() and d.name == base:
                return d
    # Fuzzy match -- serial might be a prefix
    for tier_dir in TIER_DIRS.values():
        if not tier_dir.exists():
            continue
        for d in tier_dir.iterdir():
            if d.is_dir() and d.name.startswith(base):
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
    identity_override: str = "",
    ctx: Context = None,
) -> str:
    """Register this agent as live. Call once at session startup.
    Sets PID, timestamp, and optional work summary visible to all agents.
    Enables instant message push via MCP channel notifications.
    Auto-launches the broker daemon for cross-session message routing.

    IDENTITY GUARD (NFRA_IDENTITY.G-A): refuses the registration if this PID is
    already live under a DIFFERENT serial, or the claimed serial is held by a
    different LIVE process. Pass identity_override="<reason>" to force it
    (audited). Your serial NEVER comes from .comp-graph/.agent_context -- that
    file is shared and answers "what TO", never "who am I"."""
    global _active_ctx, _my_serial, _poll_task
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found in org hierarchy."

    # Instance support: register under full serial (with ~suffix) for liveness,
    # but resolve folder/inbox from base serial.  Multiple instances of the
    # same agent share the same org folder, logs, and task_orders.
    live_serial = agent_serial  # e.g. "0.4.0_DS_ClientPlatform~B"

    # --- NFRA_IDENTITY.G-A: the enforcing chokepoint (before ANY state is written) ---
    my_pid = os.getpid()
    _identity_warning = ""
    _audit_guard_active(live_serial, my_pid)   # one row per server process == THE DENOMINATOR
    with _locked_liveness(write=False) as _snapshot:
        _conflict = _identity_conflict(live_serial, dict(_snapshot), my_pid)
    _action, _message = _identity_decide(_conflict, identity_override)
    if _action == "REFUSE":
        # HARD -- name the conflict verbatim so the phantom's FIRST registration
        # surfaces it (the 07-12/13 SEV would have died right here). No state is
        # written; the caller is NOT registered.
        return _message
    if _action == "OVERRIDE":
        _audit_identity("CROSS_OVERRIDE", live_serial, my_pid, identity_override, _message)
    elif _action == "WARN":
        # SERIAL_HELD -- advisory. Audit the collision and PROCEED; the warning
        # rides the return value so the agent sees it but is never blocked.
        _audit_identity("SERIAL_HELD", live_serial, my_pid, identity_override or "-", _message)
        _identity_warning = _message + "\n\n"

    _my_serial = live_serial

    # Update liveness.json (local file, always works)
    now = time.time()
    with _locked_liveness(write=True) as data:
        _clean_stale(data)
        data[live_serial] = {
            "pid": os.getpid(),
            "summary": summary,
            "base_serial": folder.name,
            "registered_at": datetime.now(timezone.utc).isoformat(),
            "last_seen": datetime.now(timezone.utc).isoformat(),
            "last_seen_epoch": now,
        }

    # Start broker and register with it (for cross-session messaging)
    broker_status = "unavailable"
    if _ensure_broker():
        result = _broker_fetch("/register", {
            "serial": live_serial,
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

    # Ensure the commit-queue worker is up -- GATED on SAFE_COMMIT_USE_QUEUE=1 (the TO-6
    # canary/cutover sessions only). Gated (not ungated) = no idle daemon before the flip +
    # blast radius capped to queue-enabled lanes. The singleton is atomic-verified (12 racing
    # -> 1 winner, LD-0251) so ungated would also be safe -- gating is deliberate defense-in-
    # depth. Best-effort + wrapped: a launch failure NEVER blocks registration (safe-commit D6
    # fallback-to-mutex + WorkerDown alarm cover a miss). NFRA_CMTQUE TO-6 phase-1.
    if os.environ.get("SAFE_COMMIT_USE_QUEUE") == "1":
        try:
            _ensure_commit_worker()
        except Exception:
            pass

    instance_note = ""
    if _instance_suffix(agent_serial):
        instance_note = f"\nInstance: ~{_instance_suffix(agent_serial)} (folder: {folder.name})"

    return (
        f"{_identity_warning}"
        f"Registered {live_serial} as live (PID {os.getpid()}).\n"
        f"Summary: {summary or '(none)'}\n"
        f"Broker: {broker_status}\n"
        f"Channel push: enabled. Call heartbeat() periodically to stay live."
        f"{instance_note}"
    )


@mcp.tool()
async def heartbeat(
    agent_serial: str,
    summary: str = "",
    identity_override: str = "",
    ctx: Context = None,
) -> str:
    """Update last-seen timestamp. Optionally update work summary.
    Call periodically (recommended: every 30-60s) to stay in 'live' state.
    If not called for 2 min, status degrades to 'stale'.

    IDENTITY GUARD (NFRA_IDENTITY.G-A): refuses if this PID is live under a
    DIFFERENT serial (you cannot heartbeat an identity you do not hold).
    identity_override="<reason>" forces it (audited)."""
    global _active_ctx
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found."

    # Use full serial (with instance suffix) for liveness tracking
    live_serial = agent_serial

    # --- NFRA_IDENTITY.G-A: same chokepoint on the heartbeat path. A mis-adopted
    # session that skipped register_agent (or was already registered before the
    # guard shipped) must not be able to keep the phantom identity alive.
    # Same severity split as register_agent: CROSS is hard (a process cannot beat
    # for an identity it does not hold); SERIAL_HELD is advisory (the probe cannot
    # prove the incumbent is real, and killing an agent's heartbeat on a bad probe
    # would silently drop it out of every liveness scan).
    my_pid = os.getpid()
    _identity_warning = ""
    with _locked_liveness(write=False) as _snapshot:
        _conflict = _identity_conflict(live_serial, dict(_snapshot), my_pid)
    _action, _message = _identity_decide(_conflict, identity_override)
    if _action == "REFUSE":
        return _message
    if _action == "OVERRIDE":
        _audit_identity("CROSS_OVERRIDE", live_serial, my_pid, identity_override, _message)
    elif _action == "WARN":
        _audit_identity("SERIAL_HELD", live_serial, my_pid, identity_override or "-", _message)
        _identity_warning = _message + "\n\n"

    now = time.time()
    with _locked_liveness(write=True) as data:
        _clean_stale(data)
        if live_serial not in data:
            # Backward-compat base fallback ONLY for an UNSUFFIXED caller (genuine
            # pre-tilde registration). A SUFFIXED caller (~X) whose own entry was
            # pruned by _clean_stale (quiet >DEAD_THRESHOLD) or never created must NOT
            # fall back to the base entry -- doing so CLOBBERS the base agent's summary
            # with the lane's (LD-0202 B1, the root clobber). Re-register the lane.
            if _instance_suffix(agent_serial) is None and folder.name in data:
                live_serial = folder.name
            else:
                return f"{live_serial} is not registered. Call register_agent first."
        entry = data[live_serial]
        entry["last_seen"] = datetime.now(timezone.utc).isoformat()
        entry["last_seen_epoch"] = now
        if summary:
            entry["summary"] = summary

    # Also heartbeat the broker (best-effort)
    if _broker_available:
        payload = {"serial": live_serial}
        if summary:
            payload["summary"] = summary
        _broker_fetch("/heartbeat", payload)

    urgent = _drain_piggyback()
    if urgent:
        return _identity_warning + urgent + f"Heartbeat OK for {folder.name}."
    return _identity_warning + f"Heartbeat OK for {folder.name}."


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
        # Prefer the full serial (with ~suffix). Base fallback ONLY for an UNSUFFIXED
        # caller -- a SUFFIXED caller must never write its summary onto the base entry
        # (LD-0202 B2 clobber, same class as B1).
        if agent_serial in data:
            live_serial = agent_serial
        elif _instance_suffix(agent_serial) is None and folder.name in data:
            live_serial = folder.name
        else:
            return f"{agent_serial} is not registered. Call register_agent first."
        data[live_serial]["summary"] = summary

    return f"Summary updated for {agent_serial}: \"{summary}\""


@mcp.tool()
async def deregister_agent(
    agent_serial: str,
    kill_pollers: bool = True,
    ctx: Context = None,
) -> str:
    """Remove an agent from liveness tracking and the broker. Use this to
    clean up stale agents from prior sessions. Also kills any orphaned
    agent-poller processes for that serial (unless kill_pollers=False).
    Restricted to CTO (1.0.0) and COO (2.0.0)."""
    global _active_ctx
    _active_ctx = ctx

    # Auth check: only CTO and COO can deregister agents
    caller = _my_serial or ""
    if not (caller.startswith("1.0.0") or caller.startswith("2.0.0")):
        return f"Denied: only CTO/COO can deregister agents. Caller: {caller or '(not registered)'}"

    # =====================================================================================
    # RV-0048 F-024 (CTO, 2026-07-13 -- IT DEREGISTERED *ME*, MID-INCIDENT).
    #
    # THE BUG: `resolved = _resolve_agent_folder(x).name` -- and _resolve_agent_folder looks up
    # by _base_serial(), which STRIPS the ~lane suffix. So `resolved` was always the BASE serial,
    # and it was then used as the LIVENESS KEY, the BROKER KEY, and the POLLER-KILL PATTERN.
    # Meanwhile register_agent (:770-773) registers under the FULL serial, WITH the suffix.
    #   register writes '1.0.0_SA_CTO~B'   ...   deregister deleted '1.0.0_SA_CTO'
    # CONSEQUENCE, both halves live:
    #   (a) a LANE could never be deregistered -- its zombie registration was structurally immortal;
    #   (b) every attempt to clean a lane zombie SILENTLY KILLED ITS BASE AGENT INSTEAD.
    # Exercised for real during the 2026-07-13 post-crash recovery: deregister_agent("1.0.0_SA_CTO~B")
    # returned "Deregistered 1.0.0_SA_CTO", removed the CTO's liveness record and killed 2 of his
    # pollers -- while the CTO was the agent performing the recovery. deregister is restricted to
    # CTO/COO, and CTO~B is a LANE OF CTO, so *the one authorized survivor, cleaning up the zombie he
    # is most likely to meet, deregisters himself.* The repair primitive self-destructs.
    #
    # THE ROOT CONFUSION: A FOLDER IS A FILE LOCATION. A SERIAL IS AN IDENTITY. They are not the
    # same key, and deregistration is an act on the IDENTITY. Lanes share a folder (by design --
    # they read the same role docs); they do NOT share a registration.
    # =====================================================================================
    folder = _resolve_agent_folder(agent_serial)
    resolved = _identity_key(agent_serial, folder.name if folder else None)

    removed_liveness = False
    removed_broker = False
    pollers_killed = 0

    # 1. Remove from liveness.json
    with _locked_liveness(write=True) as data:
        if resolved in data:
            del data[resolved]
            removed_liveness = True

    # 2. Remove from broker
    if _broker_available:
        result = _broker_fetch("/unregister", {"serial": resolved})
        if result and result.get("ok"):
            removed_broker = True

    # 3. Kill orphaned poller processes
    if kill_pollers:
        try:
            if sys.platform == "win32":
                import subprocess as _sp
                out = _sp.check_output(
                    ["powershell", "-Command",
                     f"Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
                     f"Where-Object {{ $_.CommandLine -match 'agent-poller.*{re.escape(resolved)}' }} | "
                     f"ForEach-Object {{ Stop-Process -Id $_.ProcessId -Force; $_.ProcessId }}"],
                    text=True, timeout=10,
                )
                pollers_killed = len([ln for ln in out.strip().splitlines() if ln.strip()])
            else:
                import subprocess as _sp
                out = _sp.check_output(
                    ["pkill", "-f", f"agent-poller.py {resolved}"],
                    text=True, timeout=5,
                )
                pollers_killed = 1
        except Exception:
            pass

    parts = [f"Deregistered {resolved}:"]
    parts.append(f"  liveness.json: {'removed' if removed_liveness else 'not found'}")
    parts.append(f"  broker: {'removed' if removed_broker else 'not found or unavailable'}")
    if kill_pollers:
        parts.append(f"  pollers killed: {pollers_killed}")
    return "\n".join(parts)


@mcp.tool()
async def deregister_all_stale(
    keep_serials: list[str] | None = None,
    ctx: Context = None,
) -> str:
    """Remove ALL agents from liveness/broker EXCEPT those in keep_serials.
    Kills all orphaned poller processes for removed agents.
    Restricted to CTO (1.0.0) and COO (2.0.0).

    Example: deregister_all_stale(keep_serials=["2.0.0_SA_COO", "0.4.0_DS_ClientPlatform"])"""
    global _active_ctx
    _active_ctx = ctx

    caller = _my_serial or ""
    if not (caller.startswith("1.0.0") or caller.startswith("2.0.0")):
        return f"Denied: only CTO/COO can deregister agents. Caller: {caller or '(not registered)'}"

    keep = set(keep_serials or [])
    removed = []

    # 1. Clean liveness.json
    with _locked_liveness(write=True) as data:
        to_remove = [s for s in data if s not in keep]
        for serial in to_remove:
            del data[serial]
            removed.append(serial)

    # 2. Clean broker
    if _broker_available:
        for serial in removed:
            _broker_fetch("/unregister", {"serial": serial})

    # 3. Kill orphaned pollers for removed agents
    total_killed = 0
    if removed:
        try:
            if sys.platform == "win32":
                import subprocess as _sp
                # Build regex that matches any removed serial
                pattern = "|".join(re.escape(s) for s in removed)
                out = _sp.check_output(
                    ["powershell", "-Command",
                     f"Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
                     f"Where-Object {{ $_.CommandLine -match 'agent-poller' -and $_.CommandLine -match '{pattern}' }} | "
                     f"ForEach-Object {{ Stop-Process -Id $_.ProcessId -Force; $_.ProcessId }}"],
                    text=True, timeout=15,
                )
                total_killed = len([ln for ln in out.strip().splitlines() if ln.strip()])
            else:
                import subprocess as _sp
                for serial in removed:
                    try:
                        _sp.check_call(["pkill", "-f", f"agent-poller.py {serial}"], timeout=5)
                        total_killed += 1
                    except Exception:
                        pass
        except Exception:
            pass

    lines = [f"Deregistered {len(removed)} agent(s), kept {len(keep)}:"]
    for s in removed:
        lines.append(f"  - {s}")
    lines.append(f"Pollers killed: {total_killed}")
    if keep:
        lines.append(f"Kept: {', '.join(sorted(keep))}")
    return "\n".join(lines)


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
    parts.append(f"# Status: {agent_serial}\n")

    # Liveness lookup. A SUFFIXED query (~X) resolves to its EXACT lane key ONLY --
    # NO base fallback, or an absent/dead lane silently renders the BASE agent's
    # state under the "# Status: ...~X" header (LD-0202 A1). Base fallback is kept
    # for an unsuffixed query (genuine pre-tilde backward-compat).
    with _locked_liveness() as data:
        if _instance_suffix(agent_serial) is not None:
            info = data.get(agent_serial)
        else:
            info = data.get(agent_serial) or data.get(folder.name)
    if info:
        status = _liveness_status(info)
        elapsed = int(time.time() - info.get("last_seen_epoch", 0))
        marker = {"live": "LIVE", "stale": "STALE", "dead": "OFFLINE"}[status]
        parts.append(f"**Liveness:** {marker} (last seen {elapsed}s ago, PID {info.get('pid', '?')})")
        if info.get("summary"):
            parts.append(f"**Working on:** {info['summary']}")
        parts.append("")
    else:
        _q_suffix = _instance_suffix(agent_serial)
        if _q_suffix is not None:
            parts.append(f"**Liveness:** NOT REGISTERED (lane ~{_q_suffix} has not registered; "
                         "base state NOT shown -- query the base serial explicitly for base)\n")
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

    # Check inbox — tilde agents have a private nested inbox/base/~suffix/ dir
    _inbox_suffix = _instance_suffix(agent_serial)
    if _inbox_suffix:
        inbox = INBOX_DIR / folder.name / f"~{_inbox_suffix}"
    else:
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

    # Inbox routing (per-tilde filesystem isolation, 2026-04-20):
    # - to_agent has ~suffix -> nested inbox/{base}/~{suffix}/ (strictly private)
    # - to_agent has no suffix -> base inbox/{base}/ (base-serial traffic only)
    # Tilded and base lanes are fully isolated: a tilded send does NOT reach
    # a base-serial check_inbox, and vice versa. No cross-contamination.
    to_suffix = _instance_suffix(to_agent)
    if to_suffix:
        inbox = INBOX_DIR / to_folder.name / f"~{to_suffix}"
    else:
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

    # Route through broker for cross-session delivery.
    # If to_agent has an instance suffix (~B), route to that specific instance.
    # If no suffix, route to the base serial — all instances poll the same inbox.
    delivery_methods = ["filesystem"]
    broker_target = to_agent if _instance_suffix(to_agent) else to_folder.name

    if _broker_available:
        result = _broker_fetch("/send-message", {
            "from_serial": from_agent,
            "to_serial": broker_target,
            "subject": subject,
            "text": body,
        })
        if result and result.get("ok"):
            delivery_methods.append("broker")

    # Attempt direct channel push to all live instances of this agent
    with _locked_liveness() as data:
        # Find all live entries matching the base serial (includes instances)
        base = _base_serial(to_agent)
        target_suffix = _instance_suffix(to_agent)
        live_targets = []
        for serial, info in data.items():
            if _base_serial(serial) == base and _liveness_status(info) == "live":
                # Channel-push must match broker/fs routing EXACTLY (LD-0202 C1):
                # a base-addressed send (target_suffix=None) pushes to the BASE
                # instance ONLY; a suffixed send to the exact instance. (Was
                # `if target_suffix and ...` -- the short-circuit on a base send
                # fanned the push out to base + EVERY ~lane while broker/fs reached
                # base only -> spurious cross-lane session interrupts.)
                if _instance_suffix(serial) != target_suffix:
                    continue
                live_targets.append(serial)

    for target_serial in live_targets:
        pushed = await _push_channel_message(
            content=f"Message from {from_agent}: [{subject}] {body}",
            meta={
                "from_agent": from_agent,
                "to_agent": target_serial,
                "subject": subject,
                "inbox_file": filename,
            },
        )
        if pushed:
            if "channel push" not in delivery_methods:
                delivery_methods.append("channel push")

    # Report the ACTUAL delivery target, not the base folder name. A ~suffix send
    # routes correctly above (nested inbox/{base}/~{suffix}/ + broker to_serial keeps
    # the suffix + channel push filtered to the matching instance), but reporting
    # `to_folder.name` (the BASE) made every ~B send LOOK like a wrong-channel
    # suffix-drop -> recurring false alarms + verification scrambles. Report the full
    # suffixed serial + the true nested inbox path so the receipt matches reality.
    # Andrew-direct 2026-06-17 (LD-0195).
    delivered_to = to_agent if to_suffix else to_folder.name
    inbox_label = f"{to_folder.name}/~{to_suffix}" if to_suffix else to_folder.name
    return f"Message delivered to {delivered_to} (inbox {inbox_label}): {filename} ({' + '.join(delivery_methods)})"


@mcp.tool()
async def check_inbox(agent_serial: str, mark_read: bool = False, ctx: Context = None) -> str:
    """Check an agent's inbox for pending messages. Set mark_read=True to
    archive messages after reading (moves to inbox/read/)."""
    global _active_ctx
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found."

    # Per-tilde isolation read (2026-04-20):
    # - caller with ~suffix reads ONLY the per-instance dir
    # - caller without suffix reads ONLY the base dir
    # No cross-reads: base-serial check_inbox never surfaces tilded traffic,
    # and a tilded check_inbox never surfaces base-serial traffic. This is a
    # deliberate reversal of the pre-2026-04-20 behavior which leaked base
    # messages into tilded readers and vice versa.
    caller_suffix = _instance_suffix(agent_serial)
    if caller_suffix:
        src_inbox = INBOX_DIR / folder.name / f"~{caller_suffix}"
    else:
        src_inbox = INBOX_DIR / folder.name

    urgent = _drain_piggyback()

    # Gather messages from the single applicable inbox. Skip nested ~* subdirs
    # when reading the base dir (they belong to tilded instances, not base).
    pairs = []  # list of (msg_path, source_inbox)
    if src_inbox.exists():
        for f in src_inbox.iterdir():
            if f.suffix == ".md" and f.is_file():
                pairs.append((f, src_inbox))
    pairs.sort(key=lambda p: p[0].name)

    if not pairs:
        display_name = agent_serial if caller_suffix else folder.name
        if urgent:
            return urgent + f"Inbox empty for {display_name} (broker messages shown above)."
        return f"Inbox empty for {display_name}."

    parts = []
    if urgent:
        parts.append(urgent)
    display_name = agent_serial if caller_suffix else folder.name
    parts.append(f"# Inbox for {display_name} ({len(pairs)} messages)\n")
    for msg, _src in pairs:
        parts.append(f"---\n## {msg.name}\n")
        parts.append(msg.read_text(encoding="utf-8", errors="replace"))

    if mark_read and pairs:
        for msg, src in pairs:
            read_dir = src / "read"
            read_dir.mkdir(exist_ok=True)
            msg.rename(read_dir / msg.name)
        parts.append(f"\n--- Archived {len(pairs)} messages to read/")

    return "\n".join(parts)


@mcp.tool()
async def list_agents(tier: str = "", ctx: Context = None) -> str:
    """List all agents in the org, optionally filtered by tier
    ('tier0_exec', 'tier1_exec', 'tier2_senior', 'tier3_junior'). Returns
    agent serial, role, latest log date, and liveness status."""
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

            # Liveness badge — check for instances (~suffix) too
            base = agent_dir.name
            live_instances = []
            for serial, info in live_data.items():
                if _base_serial(serial) == base and _liveness_status(info) == "live":
                    live_instances.append(serial)

            if live_instances:
                if len(live_instances) == 1 and live_instances[0] == base:
                    badge = "[LIVE]"
                else:
                    suffixes = [_instance_suffix(s) or "base" for s in live_instances]
                    badge = f"[LIVE x{len(live_instances)}: {', '.join(suffixes)}]"
            else:
                # Check for stale/dead single entry
                info = live_data.get(base)
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
