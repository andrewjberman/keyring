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
import socket
import errno
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
sys.path.insert(0, str(WORKSPACE_ROOT / ".tools"))  # for the shared python->bash resolver
from git_bash_resolver import git_bash  # noqa: E402  NEVER bare 'bash' (python-spawned -> System32 WSL stub)
sys.path.insert(0, str(Path(__file__).resolve().parent))  # org/mcp on path BEFORE the guards import (harness-import safe)
import broker_arg_guards  # noqa: E402  call-boundary guards (D0-T1, pure, same dir) -- see _install_strict_kwargs
import cvo_send_guard  # noqa: E402  the L8 correspondence guard (spine v2.1; Andrew-direct 2026-09-03 "Recs approved")
_REPO_ROOT = Path(__file__).resolve().parents[2]
CQ_HB_STALE_SEC = 30
BROKER_PORT = int(os.environ.get("OPAL_BROKER_PORT", "7800"))
BROKER_URL = f"http://127.0.0.1:{BROKER_PORT}"
# 2.0 -> 10.0 (Andrew cleanup 2026-07-30, MSTR low-level audit): at 2s x 7 sessions this
# poll was ~97% of broker request volume once agent-poller went to 15s, and the broker had
# burned 64,228 CPU-s in 5 days (~15% of a core) serving it. Worst-case added message
# latency is bounded by the 5s inbox watcher anyway; channel push is unaffected.
# DEPLOYED-NOT-RUNNING: a live session keeps its loaded constant until restart.
POLL_INTERVAL_S = 10.0  # seconds between broker polls

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
            # BOUNDED RETRY (2026-08-29, 1.0.0_SA_CTO). On Windows os.replace raises
            # PermissionError/WinError 5 when the DESTINATION is open by any process.
            # The mutex above is held on liveness.LOCK, a DIFFERENT file, so it is
            # structurally incapable of preventing that -- the holder is not a
            # participant. Measured: 3 sidecar deaths total against ~2,850 consecutive
            # successful beats at one seat, so the holder is TRANSIENT (a continuous
            # holder is incompatible with that rate). 5 x 50 ms therefore covers it.
            # WHAT the holder is remains UNMEASURED -- no handle tooling on this device.
            # Re-raises on exhaustion ON PURPOSE: a swallow would turn a loud death into
            # silent liveness drift, which is strictly worse than the defect being fixed.
            for _attempt in range(5):
                try:
                    os.replace(str(tmp), str(LIVENESS_FILE))
                    break
                except PermissionError:
                    if _attempt == 4:
                        raise
                    _time.sleep(0.05)
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


def _sender_conflict(claimed_from: str, my_serial: str | None):
    """G-A extension (2026-07-14, 0.0.0_AB_MSTR): classify a send_message sender claim.
    Returns (kind, message) or None if the claim is clean.

    THE SURFACE, proven live before this landed: send_message took from_agent as FREE
    TEXT and wrote it verbatim into the inbox header, the filename, the broker payload,
    and the channel push. On 2026-07-14 (01:51Z + 02:38Z) two messages landed in the
    CTO's inbox stamped with the CTO's OWN serial, sent by 0.4.0_DS_ClientPlatform by
    accident (sender field pattern-completed from the recipient), no check, exit 0,
    self-reported both times -- so the historical incidence is UNKNOWABLE: an unreported
    forged sender leaves no scar. On a fabric where "Andrew ruled X" relays agent-to-
    agent as the NORMAL case, a forged sender line is the most useful forgery available.
    The sender's own second report said it best: care is not a control.

    TWO kinds, same severity logic as the registration guard above:

      FORGED     -- the caller IS registered (my_serial known) and claims a DIFFERENT
                    sender. The CROSS class: one process asserting an identity it does
                    not hold. A lane suffix is an identity (~B != base -- F-024). No
                    legitimate silent case exists -> HARD REFUSE; identity_override
                    escapes it AND stamps the true author into the message artifact,
                    so even a permitted relay is never silent impersonation.
      UNVERIFIED -- the caller never registered in this server process, so the claim
                    cannot be checked against anything. ADVISORY: deliver, but stamp
                    the message sender-unverified + audit. Hard-refusing here would
                    sever the one channel an agent has to report a broken registration
                    path (the G-A lesson: never block the recovery path).

    Pure over (claimed_from, my_serial) so it is directly replay-testable.
    Callers canonicalise BOTH sides first (partial serials resolve via _identity_key).
    """
    if not my_serial:
        return ("UNVERIFIED", (
            f"SENDER UNVERIFIED (advisory) -- this session never called register_agent, "
            f"so from_agent={claimed_from} cannot be checked against a registration. "
            f"The message was delivered carrying a sender-unverified stamp, and the "
            f"send was audited. Register at session start to send verified."
        ))
    if claimed_from != my_serial:
        return ("FORGED", (
            f"SEND REFUSED -- sender identity guard (NFRA_IDENTITY G-A). This session "
            f"is registered as {my_serial}; from_agent claimed {claimed_from}. A process "
            f"cannot send as an identity it does not hold (a lane suffix IS an identity). "
            f"Two junk messages were forged into the CTO's inbox exactly this way on "
            f"2026-07-14 -- by accident. Send as {my_serial}, or pass from_agent=\"\" to "
            f"auto-fill your registered serial. Legitimate relay: "
            f"send_message(..., identity_override=\"<reason>\") -- audited, and the true "
            f"author is stamped into the delivered message."
        ))
    return None


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
_GUARD_VERSION = "GA-3"   # GA-1 = classify+refuse-both (as-built); GA-2 = CTO severity ruling + unconditional audit;
                          # GA-3 (2026-07-14, MSTR) = sender gate on send_message + self-scope gates on
                          # set_summary / check_inbox(mark_read) + CROSS_REFUSED rows (hard refusals were
                          # previously invisible to this log -- only overrides were audited)
_guard_active_logged = False


def _audit_identity(kind: str, claimed_serial: str, my_pid: int, reason: str, conflict: str) -> None:
    """Append an audited identity row. Best-effort -- never blocks registration.

    kind: CROSS_OVERRIDE (a hard refusal that was forced) | SERIAL_HELD (an advisory
    collision that proceeded). Both are audited; the SERIAL_HELD rows are the
    measurement that decides whether direction (2) ever earns a promotion to HARD.
    """
    try:
        # Dedupe the kinds that can fire in a tight loop (heartbeat every 30-60s; an
        # unregistered script hammering send_message). Refusal/override rows on the
        # SEND/SUMMARY/INBOX gates stay un-deduped -- each one is a distinct act.
        if kind in ("SERIAL_HELD", "CROSS_REFUSED", "SEND_UNVERIFIED"):
            key = (kind, claimed_serial, conflict)
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


def _broker_probe(timeout: float = 2.0) -> str:
    """ONE probe of BROKER_URL/health -> "ok" | "absent" | "unknown".

    THE DEFECT THIS REPLACES (0.0.0_AB_MSTR 83915, fixed 2026-08-30 by 1.0.0_SA_CTO): the old
    probe was a bare `except: return False` with a 2 s timeout, so a live-but-BUSY broker read
    as ABSENT and _ensure_broker spawned a second daemon -- both 08-29 duplicate brokers were
    born at a seat startup, the busiest moment for that process. A probe must never let an
    instrument failure become a negative verdict.

    ABSENT is ONLY "nothing is bound to the port" -- the one observation that licenses starting
    a daemon. A timeout, a reset, an HTTP error, malformed JSON: UNKNOWN -- a live broker that
    is slow looks exactly like that, and the two need OPPOSITE responses (retry vs start).

    ⛔ WHY THE PORT TABLE AND NOT "connection refused" (measured on this box 2026-08-30 02:3xZ):
    a closed loopback port here does NOT refuse -- the SYN is dropped and BOTH a raw connect and
    urlopen read `TimeoutError` after the full timeout (7891 closed: 2.02 s / 2.04 s; 7800 live:
    0.00 s / 0.36 s). So at the socket level "no listener" and "busy listener" are the SAME
    observation on this host, and a refused-vs-timeout split would read every absent broker as
    UNKNOWN and never start one. The OS port table is the discriminator that cannot be fooled by
    load: an EXCLUSIVE bind attempt on 127.0.0.1:PORT succeeds iff no socket owns the port
    (released immediately), and fails EADDRINUSE iff one does -- even one bound with
    SO_REUSEADDR (the HTTPServer default that lets two listeners coexist on Windows, which is the
    duplicate's own mechanism). Host-local, stdlib-only, no PowerShell.
    """
    owned = _port_has_listener(BROKER_PORT)
    if owned is False:
        return "absent"
    # owned is True (a listener exists) or None (could not tell): only an HTTP "ok" is decisive.
    try:
        req = urllib.request.Request(f"{BROKER_URL}/health")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
        return "ok" if isinstance(data, dict) and data.get("status") == "ok" else "unknown"
    except ConnectionRefusedError:
        return "absent"
    except urllib.error.URLError as e:
        if isinstance(getattr(e, "reason", None), ConnectionRefusedError):
            return "absent"
        return "unknown"
    except Exception:
        return "unknown"


def _port_has_listener(port: int) -> bool | None:
    """Host-local, OS-level: is ANY socket bound to 127.0.0.1:port? True / False / None (could
    not tell). Exclusive bind: on Windows SO_EXCLUSIVEADDRUSE makes the bind fail 10048 even
    against a SO_REUSEADDR listener; on POSIX a plain bind fails EADDRINUSE. Success = nobody --
    the probe socket is closed at once and never listens."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        if sys.platform == "win32" and hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            s.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        s.bind(("127.0.0.1", int(port)))
        return False
    except OSError as e:
        if e.errno in (errno.EADDRINUSE, 10048) or getattr(e, "winerror", None) == 10048:
            return True
        return None
    finally:
        try:
            s.close()
        except Exception:
            pass


def _broker_state(retries: int = 3, timeout: float = 2.0, backoff: float = 0.5) -> str:
    """Bounded re-probe. "ok" / "absent" are decisive on first sight; only "unknown" is
    retried (backoff 0.5 s, 1.0 s, ...). Returns "unknown" if every probe was -- and the
    caller must treat that as NOT-YET, never as absent. Same shape as the liveness lock
    retry at the top of this file (:149-154): bounded, then a stated outcome."""
    last = "unknown"
    for i in range(max(1, retries)):
        last = _broker_probe(timeout)
        if last != "unknown":
            return last
        if i + 1 < retries:
            _time.sleep(backoff * (i + 1))
    return last


def _broker_health() -> bool:
    """Is a broker LIVE on BROKER_URL? True ONLY on a probed "ok". False on "absent" AND on
    "unknown" -- so a caller that wants to START a daemon must NOT key on this bool: it reads
    _broker_state() and starts only on "absent" (see _ensure_broker)."""
    return _broker_state() == "ok"


def _ensure_broker() -> bool:
    """Start the broker if it's not already running. Returns True if available."""
    global _broker_available
    _state = _broker_state()
    if _state == "ok":
        _broker_available = True
        return True
    if _state == "unknown":
        # A slow or resetting listener is NOT an absent one. Starting a daemon here is the
        # duplicate-broker incident by construction (83915); report, and let the next call
        # re-probe. _broker_available stays as it was.
        log.warning("broker probe UNKNOWN after bounded retries (timeout/transport, NOT a "
                    "refusal) -- a live-but-busy broker reads like this; NOT starting a second "
                    "daemon. Re-probed on the next call.")
        return False

    log.info("Starting broker daemon (probe read ABSENT: connection refused on the port)...")
    try:
        # Launch broker as detached subprocess
        if sys.platform == "win32":
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            DETACHED_PROCESS = 0x00000008
            # --- D0_TIGHTENING T1 primitive (iii): DOUBLE-SPAWN.
            #
            # DETACHED_PROCESS alone does NOT survive a seat kill, and this is measured,
            # not reasoned: it detaches the CONSOLE, never the parent-child RECORD.
            # Win32_Process.ParentProcessId is stamped at creation and persists, and
            # `.tools/kill-agent.ps1:126-133` (Stop-ProcessTree) reaps by RECURSIVE
            # ParentProcessId descent from the seat's claude.exe. So the "detached"
            # broker was still enumerable as a descendant and still died -- R4's measured
            # fabric-wide listener death on 2026-08-19.
            #
            # Measured 2026-08-19 on this box, live broker pid 25428:
            #     25428:python.exe <- 4644:python.exe <- 26272:claude.exe   [REAPABLE]
            #
            # The fix is to SEVER the link: spawn an intermediate that immediately exits.
            # The broker's ParentProcessId then names a dead pid, so a tree walk from any
            # seat never enumerates it. Measured chains for the three candidates:
            #     A  Popen+DETACHED_PROCESS ->  child <- spawner <- ...   REAPABLE
            #     B  double-spawn           ->  child (dead-ends)        SURVIVES
            #     C  WMI Win32_Process.Create -> child <- WmiPrvSE <- ... SURVIVES
            # B is chosen over C on the build ladder: stdlib only, no PowerShell/WMI
            # dependency and no extra privileges. The port bind remains the singleton
            # mutex, so severing parentage cannot produce a second broker.
            # Rollback = restore the single Popen below.
            _launcher = (
                "import subprocess,sys;"
                "subprocess.Popen([sys.executable, {brk!r}],"
                "creationflags=0x00000200|0x00000008,"
                "stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,"
                "stdin=subprocess.DEVNULL)"
            ).format(brk=str(BROKER_SCRIPT))
            _mid = subprocess.Popen(
                [sys.executable, "-c", _launcher],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                creationflags=CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS,
            )
            try:
                # The intermediate must EXIT for the link to be severed. Waiting on it is
                # the whole mechanism, not hygiene -- a still-live intermediate keeps the
                # broker inside the seat's tree.
                _mid.wait(timeout=15)
            except Exception:
                log.warning("broker launcher did not exit within 15s; the broker may "
                            "still be parented to this seat and reapable by a tree kill")
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
    # Resolve bash explicitly: a python(Windows) subprocess invoking bare 'bash' Windows-resolves to the
    # System32 WSL stub, which SILENTLY fails (Popen succeeds, stub dies, stderr->DEVNULL, we return True on
    # a dead worker -- the 12-day silent-outage class, 0.7.0_AE_CloudOps~B 2026-07-19). Use the shared resolver.
    bash_exe = git_bash() or ("bash" if sys.platform != "win32" else None)
    if bash_exe is None:
        log.warning("commit-worker launch: no Git Bash resolved (bare 'bash' -> WSL stub); refusing to launch")
        return False
    try:
        popen_kw = dict(stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        if sys.platform == "win32":
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            DETACHED_PROCESS = 0x00000008
            subprocess.Popen([bash_exe, str(COMMIT_WORKER), "--daemon"],
                             creationflags=CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS, **popen_kw)
        else:
            subprocess.Popen([bash_exe, str(COMMIT_WORKER), "--daemon"], start_new_session=True, **popen_kw)
    except Exception as exc:
        log.warning("commit-worker launch failed: %s", exc)
        return False
    # VERIFY, do not ASSUME: a Popen that spawned a doomed WSL stub raises nothing. Poll for the worker to
    # write a FRESH heartbeat before reporting success -- otherwise this reports success on a dead worker.
    # Cap sized above the measured cold-start (~4.25s on this host, 0.7.0_AE_CloudOps~B 2026-07-19 exercise)
    # so a legitimately-slow startup is not false-negatived; a real WSL-stub death never advances the hb.
    for _ in range(32):                       # ~8s cap; only reached when the worker was down (rare path)
        _time.sleep(0.25)
        if _commit_worker_alive():
            log.info("commit-worker daemon confirmed live (fresh heartbeat)")
            return True
    log.warning("commit-worker launched but no fresh heartbeat within 8s (silent-launch guard tripped)")
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
    Returns empty string if no queued messages.

    RECIPIENT LABELING (CVO finding 20260730T215623Z, the retrieval half): this block
    prepends the CALLING session's own queued broker mail onto WHATEVER tool response
    comes next -- including a get_agent_status render for a DIFFERENT agent -- and it
    previously carried no recipient labels at all, so the caller's own mail read as the
    queried agent's (measured live: 13 MSTR-addressed messages rendered under
    '# Status: 1.0.0_SA_CTO~C'). Every drain now names the session it was queued for
    and every message names its addressed serial, so a misdelivered or misattributed
    message is VISIBLE instead of silently double-claimed."""
    global _piggyback_queue
    if not _piggyback_queue:
        return ""
    msgs = _piggyback_queue[:]
    _piggyback_queue = []

    # --- D0_TIGHTENING T1 (EMITTED clock). Tell the broker these ids left the volatile
    # queue and entered a tool response; the broker flips delivered=1 HERE, not at poll.
    # Until this call lands, the rows stay re-offerable -- which is exactly what makes a
    # seat killed between poll and drain recover its mail instead of losing it forever.
    # This is EMITTED, never READ: the clear precedes the response reaching a model
    # (the orphan-watcher mv-before-echo shape), so no agent-side claim may rest on it.
    _emit_ids = [m["id"] for m in msgs if m.get("id") is not None]
    if _emit_ids and _broker_available:
        _broker_fetch("/mark-emitted", {"serial": _my_serial or "", "ids": _emit_ids})
    # The ids are surfaced to the agent so a genuine agent-side ACK can name them.
    _ack_hint = ""
    if _emit_ids:
        _ack_hint = ("\n(delivery-state: these are EMITTED, not READ. To record READ -- the "
                     "only clock an orphan cannot forge -- call "
                     f"ack_messages(\"{','.join(str(i) for i in _emit_ids)}\").)\n")
    _mine = _my_serial or "this session (serial unset)"
    lines = [f"URGENT: {len(msgs)} message(s) received while idle -- queued for **{_mine}** "
             "(this session's OWN broker mail, NOT the queried agent's):\n"]
    for msg in msgs:
        lines.append(f"--- Message from {msg.get('from_serial', '?')} "
                     f"to {msg.get('to_serial') or _mine} ---")
        subj = msg.get("subject", "(no subject)")
        lines.append(f"Subject: {subj}")
        lines.append(msg.get("body", ""))
        lines.append("---\n")
    lines.append(_ack_hint)
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
            _queued_ids = {m.get("id") for m in _piggyback_queue}
            for msg in result["messages"]:
                # D0_TIGHTENING T1: dedupe on the broker's row id. A reclaimed message
                # (polled once, never drained, re-offered after T1_RECLAIM_S) must not
                # stack a second copy onto a session that is merely idle.
                if msg.get("id") is not None and msg["id"] in _queued_ids:
                    continue
                _queued_ids.add(msg.get("id"))
                # Primary: queue for piggyback on next tool response
                _piggyback_queue.append({
                    "id": msg.get("id"),
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
        # GA-3: audit the refusal itself. Until 2026-07-14 only OVERRIDES wrote a row,
        # so the guard's most decisive action was its least measurable one.
        _audit_identity("CROSS_REFUSED", live_serial, my_pid, "-", _message)
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
        # GA-3: refusals audited (deduped -- heartbeat fires every 30-60s, and a stuck
        # phantom beating against the guard would otherwise bury the log).
        _audit_identity("CROSS_REFUSED", live_serial, my_pid, "-", _message)
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
    identity_override: str = "",
    ctx: Context = None,
) -> str:
    """Update this agent's work summary. Visible to all agents via
    get_live_agents and get_agent_status. Keep it to 1-2 sentences
    describing current task (e.g., 'Running gold layer for ADVI_PRICES').

    SELF-SCOPE GUARD (G-A, 2026-07-14): a summary is a self-claim -- writing
    another agent's summary is refused (identity_override forces it, audited)."""
    global _active_ctx
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found."

    # --- G-A self-scope gate (2026-07-14, MSTR). Until now ANY caller could rewrite
    # ANY live agent's summary -- the exact WORKING:/BLOCKED: line COO's /drive
    # classifies the fabric on -- unchecked and unaudited. Same one-comparison guard
    # as the sender gate: the summary key is an identity, and this session holds
    # exactly one.
    if not _my_serial:
        return ("set_summary REFUSED: this session never registered, and a summary "
                "is a self-claim. Call register_agent first.")
    _target = _identity_key(agent_serial, folder.name)
    if _target != _my_serial:
        if not identity_override:
            _audit_identity("SUMMARY_FOREIGN_REFUSED", _target, os.getpid(),
                            f"caller={_my_serial}", "")
            return (f"set_summary REFUSED: you are registered as {_my_serial} and asked "
                    f"to write {_target}'s summary. A summary is a self-claim. "
                    f"identity_override=\"<reason>\" forces it (audited).")
        _audit_identity("SUMMARY_FOREIGN_OVERRIDE", _target, os.getpid(),
                        identity_override, f"caller={_my_serial}")

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

    # =====================================================================================
    # RV-0049 F-004 (MSTR): DEREGISTRATION WROTE NO AUDIT LINE. 750 audit entries, ZERO records.
    # *** THIS IS THE ONE PRIMITIVE THAT CAN UN-PERSON AN AGENT, AND IT LEFT NO TRAIL. ***
    # Exercised today, twice, on live agents: MSTR was deregistered mid-session and found out only
    # when a later heartbeat() failed; the CTO deregistered HIMSELF via F-024 and knew only because
    # the return string happened to name the serial it actually acted on.
    # An action nobody can review is an action nobody can catch being wrong -- and F-024 proves it
    # CAN be wrong about WHICH AGENT it acted on. Record the REQUESTED serial and the RESOLVED one
    # separately: if they ever differ again, the log says so instead of a human noticing a dead
    # heartbeat 40 minutes later.
    # =====================================================================================
    try:
        from datetime import datetime as _dt, timezone as _tz
        _ts = _dt.now(_tz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        _line = (
            f"{_ts} DEREGISTER caller={caller or 'UNKNOWN'} requested={agent_serial} "
            f"resolved={resolved} liveness={'removed' if removed_liveness else 'absent'} "
            f"broker={'removed' if removed_broker else 'absent'} pollers_killed={pollers_killed}"
        )
        if resolved != agent_serial:
            _line += "  *** RESOLVED != REQUESTED -- a DIFFERENT AGENT was acted on (F-024 class) ***"
        # NOTE: use the SAME idiom the rest of this file already uses (:377, :399). My first draft
        # referenced a `WORKSPACE` constant that DOES NOT EXIST -- it would have raised NameError,
        # been swallowed by the `except` below, and written NOTHING: a SILENT NO-OP AUDIT, shipped as
        # the fix FOR a missing audit. The exact class this whole file's RV findings are about, written
        # into the remedy for it. Caught by checking the constant instead of assuming it.
        _audit = Path(__file__).resolve().parent / "agent-spawn-audit.log"
        with _audit.open("a", encoding="utf-8") as _fh:
            _fh.write(_line + "\n")
    except Exception:
        pass  # never let the audit write break the recovery primitive itself

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
    to_agent: str = "",
    subject: str = "",
    body: str = "",
    identity_override: str = "",
    to_agents: list[str] | None = None,
    ctx: Context = None,
) -> str:
    """Send an async message to another agent. The message is stored in their
    inbox and will be surfaced when they next call get_agent_status or
    check_inbox.

    If the recipient is registered as LIVE, the message is also pushed
    instantly via MCP channel notification (no polling required).

    SENDER IDENTITY GUARD (NFRA_IDENTITY G-A, 2026-07-14): from_agent must be
    YOUR registered serial -- a mismatch is refused (audited). Pass from_agent=""
    to auto-fill it. identity_override="<reason>" permits a relay send; the true
    author is then stamped into the delivered message.

    RECIPIENT LIST (D0_TIGHTENING T1): pass to_agents=["A","B","C"] to address several
    seats in ONE act and get a PER-RECIPIENT result map -- {DELIVERED | QUEUED | REFUSED}
    per serial, never a silent aggregate. A dead seat returns QUEUED (written + waiting),
    an unresolvable serial returns REFUSED (nothing written). Writing "cc: X" in the BODY
    copies NOBODY -- that is the measured LD-0424 class this parameter exists to make
    inexpressible. to_agent (single) keeps its exact legacy call shape and receipt.

    Use this for status updates, questions, or handoff notes."""
    global _active_ctx
    _active_ctx = ctx

    # --- NFRA_IDENTITY G-A sender gate (2026-07-14, MSTR). Before this, from_agent
    # was written verbatim into the header/filename/broker/push with NO check --
    # the fabric's identity fields were assertions by the sender, not facts, and
    # two accidental forgeries landed in the CTO's inbox under his own serial the
    # night this shipped. Runs FIRST: a refused sender writes no state at all.
    claimed = (from_agent or "").strip()
    if not claimed:
        if not _my_serial:
            return ("SEND REFUSED: from_agent is empty and this session never "
                    "registered, so the sender cannot be inferred. Call "
                    "register_agent first, or pass your serial explicitly.")
        claimed = _my_serial
    else:
        _from_folder = _resolve_agent_folder(claimed)
        claimed = _identity_key(claimed, _from_folder.name if _from_folder else None)
    _sender_stamp = ""
    _sender_note = ""
    _s_conflict = _sender_conflict(claimed, _my_serial)
    if _s_conflict:
        _s_kind, _s_message = _s_conflict
        if _s_kind == "FORGED":
            if not identity_override:
                _audit_identity("SEND_FORGED_REFUSED", claimed, os.getpid(),
                                f"caller={_my_serial}", _s_message)
                return _s_message
            # Permitted relay: the delivered artifact names its TRUE author, so an
            # authorized impersonation is never a silent one.
            _audit_identity("SEND_FORGED_OVERRIDE", claimed, os.getpid(),
                            identity_override, f"caller={_my_serial}")
            _sender_stamp = (f"**Sender-override:** actually sent by {_my_serial}; "
                             f"reason: {identity_override}\n")
        else:  # UNVERIFIED -- deliver, stamped + audited (never block the recovery path)
            _audit_identity("SEND_UNVERIFIED", claimed, os.getpid(), "-", _s_message)
            _sender_stamp = ("**Sender-unverified:** the sending session was not "
                             "registered; this from-line is asserted, not proven.\n")
            _sender_note = " [sender unverified -- register_agent to send verified]"
    from_agent = claimed

    # --- D0_T1 CHECK 2 (instance backstop; COO seating 64310 + amendment 64318 -- STRUCTURAL,
    # ZERO THRESHOLDS): an empty body refuses, both directions, before any write. Nine measured
    # empty sends in one night all carried "delivered" receipts; the receipt observes the
    # envelope, never the content. Runs AFTER the identity gate (which must stay first so a
    # forged sender is audited, not answered) and BEFORE any delivery state.
    _env_refusal = broker_arg_guards.empty_envelope_refusal(subject, body)
    if _env_refusal:
        return _env_refusal

    # --- D0_TIGHTENING T1 primitive (i): recipient-LIST send.
    # The body-cc class is measured (LD-0424: DT's freeze release lost to an in-body
    # "cc" that copied nobody). A list parameter makes that class INEXPRESSIBLE: you
    # either name a recipient and get a per-recipient verdict, or you did not send.
    # Backward compatible by construction -- `to_agent: str` is untouched and a
    # single-recipient call returns the exact legacy receipt string.
    _recipients: list[str] = []
    for _r in (to_agents or []):
        _r = (_r or "").strip()
        if _r and _r not in _recipients:
            _recipients.append(_r)
    _single = (to_agent or "").strip()
    if _single and _single not in _recipients:
        _recipients.insert(0, _single)
    if not _recipients:
        return ("SEND REFUSED: no recipient. Pass to_agent=\"<serial>\" or "
                "to_agents=[\"<serial>\", ...]. (Nothing was sent.)")

    # --- L8 CORRESPONDENCE GUARD (spine v2.1 L8 "Not engaged"; Andrew-direct 2026-09-03 ~04:5xZ "Recs
    # approved", CTO /open-calls CALL 1). A send from 3.0.0_SA_CVO to ANY Tier-2 serial is REFUSED while a
    # tree project reads dep_stage EXECUTING (L7-L9); the finding travels up to the COO or the CTO. Runs
    # AFTER the identity gate (a forged CVO is audited as a forgery first) and BEFORE any write, over the
    # whole recipient list (a partial delivery would let a cc to the COO carry the body to the worker).
    # Decision and census live in cvo_send_guard.py so the daemon's HTTP path grades with the same code.
    _l8_refusal = cvo_send_guard.cvo_worker_send_refusal(
        from_agent, _recipients, cvo_send_guard.executing_tree_projects(_REPO_ROOT))
    if _l8_refusal:
        _audit_identity("SEND_CVO_WORKER_REFUSED", from_agent, os.getpid(),
                        "to=" + ",".join(_recipients), _l8_refusal[:200])
        return _l8_refusal
    # --- LD-0529 (Andrew-direct 2026-09-03 ~13:1xZ, "Mechanism works"): a Tier-0/Tier-1 -> Tier-2 send that
    # carries an ACT is refused unless it cites a task order assigned to that recipient. The issuer's dispatch
    # passes; acks and act-free information pass. Decision and citation resolver live in cvo_send_guard.py.
    _t2_refusal = cvo_send_guard.tier2_act_send_refusal(from_agent, _recipients, subject, body, _REPO_ROOT)
    if _t2_refusal:
        _audit_identity("SEND_TIER2_ACT_REFUSED", from_agent, os.getpid(),
                        "to=" + ",".join(_recipients), _t2_refusal[:200])
        return _t2_refusal

    _results = []
    for _rcpt in _recipients:
        _results.append(await _deliver_to_one(
            from_agent, _rcpt, subject, body, _sender_stamp, _sender_note))

    # Single-recipient call -> the legacy receipt string, byte-for-byte shape.
    if len(_results) == 1 and not to_agents:
        return _results[0]["receipt"]

    # Multi-recipient -> a PER-RECIPIENT map. Never a silent aggregate: an aggregate
    # is what let a body-cc read as delivery.
    _lines = [f"send_message -> {len(_results)} recipient(s). PER-RECIPIENT RESULT:"]
    for _r in _results:
        _lines.append(f"  {_r['state']:<9} {_r['to']}   {_r['detail']}")
    _n_ref = sum(1 for _r in _results if _r["state"] == "REFUSED")
    _n_q = sum(1 for _r in _results if _r["state"] == "QUEUED")
    _n_d = sum(1 for _r in _results if _r["state"] == "DELIVERED")
    _lines.append(f"  -- {_n_d} DELIVERED / {_n_q} QUEUED / {_n_ref} REFUSED "
                  f"(denominator {len(_results)})")
    if _n_q:
        _lines.append("  QUEUED = written to inbox + broker, no LIVE session to push to. "
                      "Not a failure, and NOT a delivery -- it waits for the seat.")
    if _n_ref:
        _lines.append("  REFUSED = serial does not resolve in org. NOTHING was written "
                      "for that recipient.")
    return "\n".join(_lines) + _sender_note


async def _deliver_to_one(from_agent: str, to_agent: str, subject: str, body: str,
                          _sender_stamp: str = "", _sender_note: str = "") -> dict:
    """One recipient's delivery -- the pre-T1 send path, unchanged in behavior.

    Returns {to, state, detail, receipt} where state is DELIVERED | QUEUED | REFUSED.
    DELIVERED means a live session was pushed to; QUEUED means the message is durably
    written and waiting; REFUSED means the serial does not resolve and nothing was
    written. A caller may never collapse these three into a success boolean.
    """
    to_folder = _resolve_agent_folder(to_agent)
    if not to_folder:
        return {"to": to_agent, "state": "REFUSED",
                "detail": "serial does not resolve in org -- nothing written",
                "receipt": f"Recipient '{to_agent}' not found in org."}

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
    # To: carries the FULL ADDRESSED SERIAL, suffix included (CVO finding 20260730T215623Z,
    # measured by 0.7.0_AE_CloudOps~B: this line wrote to_folder.name -- the agent FOLDER,
    # which never carries a ~suffix -- so a lane-addressed message ROUTED to the nested lane
    # dir while its own header claimed the BASE held it; the lane reader could not tell the
    # message was theirs. LD-0202 family, header-vs-routing variant. The halt-gate's LD-0131
    # recipient filter base-strips To: before comparing, so the full serial is compatible.)
    msg_content = (
        f"# Message from {from_agent}\n"
        f"**To:** {to_agent}\n"
        f"**Date:** {ts}\n"
        f"{_sender_stamp}"
        f"**Subject:** {subject}\n\n"
        f"{body}\n"
    )
    msg_path.write_text(msg_content, encoding="utf-8")

    # Route through broker for cross-session delivery.
    # If to_agent has an instance suffix (~B), route to that specific instance.
    # If no suffix, route to the base serial — all instances poll the same inbox.
    delivery_methods = ["filesystem"]
    broker_target = to_agent if _instance_suffix(to_agent) else to_folder.name

    _msg_id = None
    if _broker_available:
        result = _broker_fetch("/send-message", {
            "from_serial": from_agent,
            "to_serial": broker_target,
            "subject": subject,
            "text": body,
        })
        if result and result.get("ok"):
            delivery_methods.append("broker")
            _msg_id = result.get("message_id")

    # D0_TIGHTENING T1: stamp the broker row id into the FILE. Without it a
    # consumption-side ack has to guess which row it just read (by subject/timestamp),
    # and a guessing ACK is worse than none -- it would mark the wrong message READ.
    if _msg_id is not None:
        msg_path.write_text(
            msg_content.replace("**Subject:**", f"**Msg-ID:** {_msg_id}\n**Subject:**", 1),
            encoding="utf-8")

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
    receipt = (f"Message delivered to {delivered_to} (inbox {inbox_label}): {filename} "
               f"({' + '.join(delivery_methods)}){_sender_note}")

    # DELIVERED vs QUEUED turns on whether a LIVE session existed to push to. A dead
    # seat yields QUEUED -- written and waiting -- never a silent success.
    state = "DELIVERED" if live_targets else "QUEUED"
    detail = (f"id={_msg_id} via {'+'.join(delivery_methods)}"
              if live_targets else
              f"id={_msg_id} written to inbox {inbox_label}; no live session")
    return {"to": to_agent, "state": state, "detail": detail, "receipt": receipt}


@mcp.tool()
async def check_inbox(agent_serial: str, mark_read: bool = False,
                      identity_override: str = "", ctx: Context = None) -> str:
    """Check an agent's inbox for pending messages. Set mark_read=True to
    archive messages after reading (moves to inbox/read/).

    Reading ANY agent's inbox is legal (inspection). DRAINING one (mark_read=True)
    is self-scoped: on a foreign serial it is refused -- moving another agent's
    unread mail to read/ is the orphan-thief effect as an API call.
    identity_override="<reason>" forces it (audited; e.g. dead-agent cleanup)."""
    global _active_ctx
    _active_ctx = ctx

    folder = _resolve_agent_folder(agent_serial)
    if not folder:
        return f"Agent '{agent_serial}' not found."

    # --- G-A self-scope gate on the DRAIN only (2026-07-14, MSTR). Foreign reads
    # stay free -- COO/MSTR legitimately inspect. But mark_read=True moves the
    # target's UNREAD messages out of their delivery path, which is exactly what
    # the orphan watchers did to dead MSTR's respawn requests on 2026-07-13.
    if mark_read:
        if not _my_serial:
            return ("check_inbox(mark_read=True) REFUSED: this session never "
                    "registered, so self-scope cannot be verified. Read without "
                    "mark_read, or call register_agent first. (Nothing was read "
                    "or moved.)")
        _target = _identity_key(agent_serial, folder.name)
        if _target != _my_serial:
            if not identity_override:
                _audit_identity("INBOX_DRAIN_REFUSED", _target, os.getpid(),
                                f"caller={_my_serial}", "")
                return (f"check_inbox(mark_read=True) REFUSED: you are {_my_serial}; "
                        f"draining {_target}'s inbox would move THEIR unread messages "
                        f"to read/ before they see them. Re-call with mark_read=False "
                        f"to inspect, or identity_override=\"<reason>\" to force "
                        f"(audited). (Nothing was read or moved.)")
            _audit_identity("INBOX_DRAIN_OVERRIDE", _target, os.getpid(),
                            identity_override, f"caller={_my_serial}")

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
        # D0_TIGHTENING T1 (READ clock). Collect Msg-IDs BEFORE the move, then ack them.
        # This is one of exactly two sound READ oracles; the other is an agent-side
        # ack_messages call. `read/` mtime, ps, and an empty inbox remain BANNED (22b) --
        # they observe the watcher, not the agent.
        _read_ids = []
        for msg, _src in pairs:
            try:
                _head = msg.read_text(encoding="utf-8", errors="replace")[:400]
                _m = re.search(r"^\*\*Msg-ID:\*\*\s*(\d+)\s*$", _head, re.MULTILINE)
                if _m:
                    _read_ids.append(int(_m.group(1)))
            except Exception:
                pass
        for msg, src in pairs:
            read_dir = src / "read"
            read_dir.mkdir(exist_ok=True)
            msg.rename(read_dir / msg.name)
        _ack_res = None
        if _read_ids and _broker_available:
            _ack_body = {"serial": _my_serial or agent_serial, "ids": _read_ids}
            # The broker's recipient check (2026-08-30) refuses an ack on a row not addressed
            # to the acking serial. A FOREIGN drain reaches this line only through the audited
            # INBOX_DRAIN_OVERRIDE branch above, so that is the one case that carries the
            # override flag -- and acked_by still records the cleaner, never the dead seat.
            if (mark_read and identity_override and _my_serial
                    and _identity_key(agent_serial, folder.name) != _my_serial):
                _ack_body["override"] = True
            _ack_res = _broker_fetch("/ack-messages", _ack_body)
        parts.append(f"\n--- Archived {len(pairs)} messages to read/")
        if _read_ids and isinstance(_ack_res, dict) and _ack_res.get("refused"):
            parts.append(
                f"--- READ ack REFUSED for {_ack_res.get('refused')} id(s) not addressed to "
                f"{_my_serial}: {_ack_res.get('refused_ids')} -- the files moved to read/, but "
                f"the READ clock for those rows is UNWRITTEN (broker recipient check).")
        if _read_ids:
            # REPORT THE ACTUAL OUTCOME. This block previously announced "READ ack recorded"
            # UNCONDITIONALLY -- it claimed the READ clock had been written even when the
            # broker call FAILED. That is exactly the class this primitive exists to retire:
            # a delivery claim resting on something other than a consumption act.
            # Measured live 2026-08-19: a post-T1 server against the still-pre-T1 broker gets
            # 404 on /ack-messages, so the unconditional message would have asserted READ for
            # every drained message across the entire version-skew window.
            if _ack_res is not None:
                parts.append(f"--- READ ack recorded for message id(s): "
                             f"{', '.join(str(i) for i in _read_ids)}")
            else:
                parts.append(
                    "--- READ ack NOT recorded: the broker did not accept /ack-messages "
                    f"(ids {', '.join(str(i) for i in _read_ids)}). You read these messages, "
                    "but the READ CLOCK IS UNWRITTEN -- do not cite them as acked. A pre-T1 "
                    "broker has no /ack-messages route until it restarts.")

    return "\n".join(parts)


@mcp.tool(meta={"anthropic/alwaysLoad": True})  # OPAL_ANALYST sec11 S2: schema RESIDENT at session
# start (no ToolSearch hop) -- the READ-clock primitive every seat calls; ruled CTO~Z msg 2617.
async def ack_messages(message_ids: str, ctx: Context = None) -> str:
    """Record that YOU READ specific broker messages -- the READ clock (D0_TIGHTENING T1).

    This is the ONLY delivery signal an orphan cannot forge, and the only one that
    claims an AGENT saw a message. Call it after a piggyback drain surfaces message ids
    to you. Pass a comma-separated id list, e.g. ack_messages("41,42").

    Why this exists: the fabric has THREE clocks and used to conflate them. A broker
    poll (SENT) means a client process took handoff. A piggyback drain (EMITTED) means
    the volatile queue cleared -- and that clear precedes the response ever reaching a
    model, structurally the orphan-watcher mv-before-echo shape. Neither is evidence an
    agent read anything. An ACK placed at either transport act would inherit exactly the
    conflation this primitive exists to retire."""
    global _active_ctx
    _active_ctx = ctx

    ids = []
    for tok in str(message_ids).replace(" ", ",").split(","):
        tok = tok.strip()
        if tok.isdigit():
            ids.append(int(tok))
    if not ids:
        return ("ack_messages: no numeric ids parsed from "
                f"{message_ids!r}. Nothing acked.")
    if not _my_serial:
        return ("ack_messages REFUSED: this session never registered, so the ACK could "
                "not name an agent -- and an unattributed ACK is exactly the kind of "
                "producer-side signal this primitive replaces. Call register_agent first.")
    if not _broker_available:
        return "ack_messages: broker unavailable. Nothing acked (reported, not swallowed)."
    res = _broker_fetch("/ack-messages", {"serial": _my_serial, "ids": ids})
    if res is None:
        return "ack_messages: broker call FAILED. Nothing acked (reported, not swallowed)."
    n = res.get("acked", 0)
    refused = int(res.get("refused", 0) or 0)          # absent on a pre-fix broker -> 0
    refused_ids = res.get("refused_ids", []) or []
    skipped = len(ids) - n - refused
    acked_ids = [i for i in ids if i not in refused_ids]
    out = f"READ ack recorded by {_my_serial} for {n} message(s): {acked_ids if refused else ids}"
    if refused > 0:
        out += (f"\n  REFUSED {refused} id(s) NOT ADDRESSED TO {_my_serial}: {refused_ids} -- an ACK "
                f"lands only on the true recipient's row (broker recipient check, 2026-08-30). A "
                f"drain's suggested ids or a peer's copy of a broadcast are not yours to ack; the true "
                f"recipient's READ slot stays open for them. Nothing was written for these ids.")
    if skipped > 0:
        out += (f"\n  ({skipped} already carried an ACK -- an ACK is write-once, so the "
                f"FIRST reader's timestamp is preserved rather than overwritten.)")
    return out


@mcp.tool()
async def get_delivery_state(agent_serial: str = "", message_id: int = 0,
                             since: str = "", limit: int = 50,
                             ctx: Context = None) -> str:
    """Per-message delivery state: SENT / EMITTED / READ -- never an aggregate.

    The receipt query for D0_TIGHTENING T1. Use it instead of filesystem heuristics
    (`read/` mtime, ps, an empty inbox) -- those observe the WATCHER, not the agent,
    and an orphan watcher drives them to REACHABLE precisely when the agent is deaf.

    States:
      QUEUED          written; no client has polled it yet
      SENT            a client process took handoff (says NOTHING about an agent)
      EMITTED         drained into a tool response (no agent-side evidence)
      READ            an agent acked it -- the only state that claims an agent saw it
      UNKNOWN-PRE-T1  delivered under the pre-T1 code; its fate is unknowable, and
                      saying so is the point. Never reported as READ."""
    global _active_ctx
    _active_ctx = ctx

    if not _broker_available:
        return "get_delivery_state: broker unavailable (reported, not swallowed)."
    payload: dict = {"limit": limit}
    if message_id:
        payload["message_id"] = message_id
    if agent_serial:
        payload["serial"] = agent_serial
    if since:
        payload["since"] = since
    if not message_id and not agent_serial:
        return ("get_delivery_state: pass message_id=<id> or agent_serial=\"<serial>\" "
                "(optionally since=\"<iso8601>\").")

    res = _broker_fetch("/delivery-state", payload)
    if res is None:
        return "get_delivery_state: broker call FAILED (reported, not swallowed)."
    if "error" in res:
        return f"get_delivery_state: {res['error']}"

    msgs = res.get("messages", [])
    if not msgs:
        # Print the frame with the zero. A bare 0 does not say what it is 0 OF.
        scope = f"message_id={message_id}" if message_id else f"to_serial={agent_serial}"
        return (f"get_delivery_state: 0 rows for {scope}"
                f"{' since ' + since if since else ''} (limit {limit}). "
                f"Zero ROWS MATCHED -- not zero delivered.")

    lines = [f"# Delivery state -- {len(msgs)} message(s) "
             f"[{'message_id=' + str(message_id) if message_id else 'to ' + agent_serial}"
             f"{', since ' + since if since else ''}, limit {limit}]", ""]
    counts: dict = {}
    for m in msgs:
        counts[m["state"]] = counts.get(m["state"], 0) + 1
        lines.append(f"  [{m['state']:<14}] id={m['id']:<6} {m['sent_at']}  "
                     f"{m['from_serial']} -> {m['to_serial']}")
        lines.append(f"                   subj: {m['subject'][:70]}")
        stamps = []
        if m.get("polled_at"):
            stamps.append(f"SENT@{m['polled_at']}")
        if m.get("emitted_at"):
            stamps.append(f"EMITTED@{m['emitted_at']}")
        if m.get("acked_at"):
            stamps.append(f"READ@{m['acked_at']} by {m.get('acked_by') or '?'}")
        lines.append(f"                   {' | '.join(stamps) if stamps else 'no clock stamps yet'}")
    lines.append("")
    lines.append("  TOTALS: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
                 + f"  (denominator {len(msgs)})")
    # ACKABLE DENOMINATOR (COO finding 2026-08-19T2354Z, carried into the instrument).
    # A rate shaped acked/total FOLDS A STRUCTURAL IMPOSSIBILITY INTO A BEHAVIOURAL FAILURE.
    # Measured: the 72-message batch in flight at the 23:32:01Z broker cycle came back
    # content-complete but WITHOUT IDS -- they were queued under the pre-cycle broker, so no
    # ack can ever name them. Any acked/delivered ratio computed over them shows a permanent
    # shortfall that NO ACTION CAN EVER CLOSE, pointed at agents who did nothing wrong.
    # So the denominator is split: rows that COULD be acked, and rows that structurally cannot.
    # Same shape as the ledger lint's no-header class -- reported separately, never folded in.
    _unackable = counts.get("UNKNOWN-PRE-T1", 0)
    _ackable = len(msgs) - _unackable
    _read = counts.get("READ", 0)
    lines.append(f"  ACKABLE DENOMINATOR: {_ackable} of {len(msgs)} "
                 f"({_unackable} structurally UN-ACKABLE and excluded)")
    if _ackable:
        lines.append(f"  READ COVERAGE: {_read}/{_ackable} of the ACKABLE rows "
                     f"-- never {_read}/{len(msgs)}, which would count the impossible as unmet.")
    if _unackable:
        lines.append("  NOTE: UNKNOWN-PRE-T1 rows predate the T1 clocks (or were in flight at a "
                     "broker cycle). Their fate is genuinely unknowable and NO ACK CAN NAME THEM "
                     "-- do not read them as READ, and do not read them as non-compliance either.")
    return "\n".join(lines)


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
# D0_T1 CHECK 1 (the CLASS-level fix; CTO ruling 64300, settled spec MSTR 64327):
# STRICT KWARGS AT THE TOOL BOUNDARY, for EVERY tool -- an unknown parameter REFUSES with a
# did-you-mean instead of being silently dropped by pydantic's ignore-extras default. Installed
# once, after every @mcp.tool() registration above, by wrapping ToolManager.call_tool: the check
# runs BEFORE argument validation and BEFORE any tool body, so a refused call executes nothing
# and writes nothing. NOT a governed gate (approves/holds/routes nothing to a human) and NOT
# notification machinery (synchronous refusal on the call; nothing emitted, nothing watched).
# ---------------------------------------------------------------------------

def _install_strict_kwargs(mcp_instance) -> None:
    _tm = mcp_instance._tool_manager
    _orig_call = _tm.call_tool

    async def _strict_call_tool(name, arguments, context=None, convert_result=False):
        _tool = _tm.get_tool(name)
        if _tool is not None and isinstance(arguments, dict):
            _known = set(_tool.fn_metadata.arg_model.model_fields.keys())
            if getattr(_tool, "context_kwarg", None):
                _known.discard(_tool.context_kwarg)
            _unknown = broker_arg_guards.unknown_kwargs(arguments, _known)
            if _unknown:
                raise ValueError(broker_arg_guards.strict_kwargs_message(name, _unknown, sorted(_known)))
        return await _orig_call(name, arguments, context=context, convert_result=convert_result)

    _tm.call_tool = _strict_call_tool


_install_strict_kwargs(mcp)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run(transport="stdio")
