#!/usr/bin/env python3
"""
fabric-check.py -- fused fabric telemetry + status display.

Cross-references TWO signals to give the true state of every agent in the fabric:

  1. OBJECTIVE liveness, from PostToolUse telemetry (org/mcp/agent_telemetry/*.jsonl).
     Telemetry is real tool calls -- it cannot be faked or go phantom. Dual-signal
     per the LD-0070 TELEMETRY_LIVENESS_FRAMEWORK:
       LIVE          = most-recent kind:work entry within 120s
       SESSION_ALIVE = most-recent entry of ANY kind within 600s
       STALE         = last activity > 600s ago

  2. DECLARED status, from the broker summary (org/mcp/liveness.json `summary`),
     which the agent self-sets via register_agent / heartbeat / set_summary.

The value of fusing them: get_live_agents() reports liveness from the heartbeat
file, which can read LIVE for a dead session (the "phantom-live" failure class).
Telemetry-derived liveness is ground truth; the declared summary is a claim. When
they disagree -- summary says "working on X" but telemetry is STALE -- that is a
PHANTOM and fabric-check flags it.

DECLARED-STATUS TAXONOMY (what agents should put in their summary):
  WORKING: <task>            -- actively working; name the task
  IDLE: available            -- no work assigned; ready for dispatch
  BLOCKED: <blocker>         -- waiting on a dependency; name it
  BLOCKED-SOVEREIGN: <ask>   -- blocked AND the block needs an Andrew/MSTR ruling

fabric-check is robust to the looser legacy phrasings (it infers from telemetry +
keyword-matches the summary) but flags STATUS-UNCLEAR when an alive agent's summary
declares no clear working/idle/blocked state, so the taxonomy gets adopted.

Read-only. No MCP, no broker round-trip, no writes. Any agent can run it ad hoc.

Usage:
  python .tools/fabric-check.py            # full fabric view
  python .tools/fabric-check.py --json     # machine-readable (for /drive chaining)
  python .tools/fabric-check.py --blocks   # only BLOCKED + SOVEREIGN + PHANTOM (COO drive triage)
"""
from __future__ import annotations
import glob
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

# Canonical thresholds (LD-0070 TELEMETRY_LIVENESS_FRAMEWORK §1.1)
LIVE_WORK_S = 120      # last kind:work within this -> LIVE (dispatch-grade)
SESSION_ALIVE_S = 600  # last any-kind within this -> session alive
# An agent is shown if it is in liveness.json OR had any telemetry within this window.
RELEVANCE_S = 900      # 15 min -- keeps the historical lane files out of the view
# DEAF window: a lane counts as "was a live session that went deaf" only if it had
# telemetry within this window. Older (or never) = just an offline agent with leftover
# mail, NOT a deaf-live-session needing respawn. Bounds the unread-inbox signal.
DEAF_RECENT_S = 7200   # 2h

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
LIVENESS = os.path.join(ROOT, "org", "mcp", "liveness.json")
TELDIR = os.path.join(ROOT, "org", "mcp", "agent_telemetry")

WORK_KINDS = {"work"}  # kinds that count as substantive work for the LIVE signal


def _tail_lines(path: str, max_bytes: int = 32768) -> list[str]:
    """Return the last chunk of a file as lines (telemetry is chronological append)."""
    try:
        sz = os.path.getsize(path)
        with open(path, "rb") as f:
            if sz > max_bytes:
                f.seek(-max_bytes, os.SEEK_END)
                f.readline()  # drop partial first line
            data = f.read()
        return data.decode("utf-8", errors="replace").splitlines()
    except OSError:
        return []


def telemetry_signals(serial: str) -> dict:
    """Most-recent work-ts and any-ts (unix) for a serial, from its jsonl tail."""
    path = os.path.join(TELDIR, serial + ".jsonl")
    last_any = 0.0
    last_work = 0.0
    last_tool = ""
    for line in reversed(_tail_lines(path)):
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except ValueError:
            continue
        ts = float(row.get("ts_unix") or 0)
        if ts <= 0:
            continue
        if ts > last_any:
            last_any = ts
            last_tool = row.get("tool_name", "")
        if row.get("kind") in WORK_KINDS and ts > last_work:
            last_work = ts
        # tail is reverse-chronological; once we've passed both freshest marks we can stop early
        if last_any and last_work and (last_any - ts) > SESSION_ALIVE_S * 2:
            break
    return {"last_any": last_any, "last_work": last_work, "last_tool": last_tool}


INBOX_DIR = os.path.join(ROOT, "org", "mcp", "inbox")
REAPED_FILE = os.path.join(ROOT, "org", "mcp", "reaped_serials.json")
REAPED_RECENT_S = 21600  # 6h -- a serial reaped within this is excluded from DEAF


def reaped_recently() -> set:
    """Serials intentionally reaped within REAPED_RECENT_S (optional org/mcp/reaped_serials.json,
    {serial: reaped_ts_unix}). A reaped lane is intentionally dead -- not a DEAF lane needing
    respawn -- so DEAF detection excludes it (COO LD-0158 tuning). No file => empty set => no-op."""
    try:
        with open(REAPED_FILE, "r", encoding="utf-8", errors="replace") as f:
            d = json.load(f)
        now = time.time()
        return {s for s, ts in d.items() if (now - float(ts)) < REAPED_RECENT_S}
    except (OSError, ValueError, TypeError):
        return set()


def lane_inbox_dir(serial: str) -> str:
    """The CANONICAL inbox dir a serial's mail is actually delivered to.

    Mirrors the two writers, and it MUST keep mirroring them:
      - server.py send_message   -> INBOX_DIR/<base>/~<suffix>/   (nested, per-tilde isolation)
      - inbox-watch.sh WATCH_DIR -> INBOX_BASE/<base>/~<suffix>/  (the lane's Monitor)

    A base (non-tilde) serial resolves to INBOX_DIR/<serial>/.

    DEFECT-3 (this fix). The old code read `INBOX_DIR/<serial>` for EVERY serial, so for a lane
    `A~B` it read the FLAT dir `inbox/A~B/` -- which exists on disk for many lanes (legacy,
    pre-2026-04-20 per-tilde isolation) and which NOTHING HAS WRITTEN TO SINCE. It is a decoy:
    always present, always 0 unread, so a lane could never be classified DEAF.

    This is NOT "the enumerator was blind." It read a directory that is guaranteed to answer
    'healthy'. An instrument reporting confidently on something other than what it claims to
    measure -- the same class as a 0-row parquet that passes `exists` and `bytes > N`.

    Incident: 2026-07-09. `0.4.0_DS_ClientPlatform~B` sat with 3 undelivered messages -- one a
    sovereign cancellation -- in `inbox/0.4.0_DS_ClientPlatform/~B/`. `--blocks` read
    `inbox/0.4.0_DS_ClientPlatform~B/`, found 0, and printed `deaf=2`. The answer was 3, and the
    missing lane held a GO to edit the producer of a frozen client-facing AUA.
    """
    if "~" in serial:
        base, suffix = serial.split("~", 1)
        return os.path.join(INBOX_DIR, base, "~" + suffix)
    return os.path.join(INBOX_DIR, serial)


def _count_md(d: str) -> tuple[int, float]:
    """(count, newest_mtime) of top-level *.md files directly in dir `d`."""
    count = 0
    newest = 0.0
    try:
        for fn in os.listdir(d):
            if fn.endswith(".md"):
                p = os.path.join(d, fn)
                if os.path.isfile(p):
                    count += 1
                    m = os.path.getmtime(p)
                    if m > newest:
                        newest = m
    except OSError:
        pass
    return count, newest


def unread_inbox(serial: str) -> tuple[int, float]:
    """(count, newest_mtime) of unread top-level *.md in the serial's CANONICAL inbox dir.
    The stream Monitor mv's delivered messages to read/, so top-level *.md left in
    the inbox = messages NOT yet processed by the lane's Monitor. A pile of these on
    a telemetry-quiet lane = the lane is DEAF (dead Monitor + no self-tick to re-arm)."""
    return _count_md(lane_inbox_dir(serial))


def legacy_flat_orphans(serial: str) -> int:
    """Top-level *.md stranded in the FLAT dir `inbox/<base>~<suffix>/` for a lane.

    NOT merely a legacy artifact -- it is STILL BEING WRITTEN. `.tools/operator.py:539-541` does
    `inbox_dir = inbox_root / agent; inbox_dir.mkdir(parents=True, exist_ok=True)` where `agent`
    is the TO's `<issued_to>`, which org/XXX.md REQUIRES to carry the `~lane` suffix. So the live
    dispatch path writes a lane's GO to the flat dir AND CREATES IT ON DEMAND.

    Non-zero => real mail stranded where no Monitor watches and no `check_inbox` reads. Counted,
    NEVER treated as delivered: reading the decoy as a live inbox is what this fix exists to stop,
    and folding these into `unread` would pin the lane DEAF forever (see is_deaf / the WARN text).
    0 for base serials -- their flat dir IS the canonical one."""
    if "~" not in serial:
        return 0
    flat = os.path.join(INBOX_DIR, serial)
    if os.path.abspath(flat) == os.path.abspath(lane_inbox_dir(serial)):
        return 0
    return _count_md(flat)[0]


def enumerate_inbox_lanes() -> tuple[set, int, int, int]:
    """Every inbox identity on disk, across BOTH dir conventions.

    Returns (serials, n_base, n_nested, n_legacy_flat).

    The old code walked only `os.listdir(INBOX_DIR)`, so a lane whose ONLY dir is the nested
    `inbox/<base>/~<suffix>/` (the canonical, actively-written one) was never a candidate at all.
    Lanes that also happen to own a legacy flat dir were candidates -- but were then read at the
    decoy path. Both roads led to `0 unread`.
    """
    serials: set = set()
    n_base = n_nested = n_flat = 0
    try:
        top = os.listdir(INBOX_DIR)
    except OSError:
        return serials, 0, 0, 0
    for dn in top:
        dp = os.path.join(INBOX_DIR, dn)
        if not os.path.isdir(dp):
            continue
        if "~" in dn:                       # FLAT lane dir: inbox/<base>~<suffix>/ -- unwatched,
            serials.add(dn)                 # and still created on demand by operator.py:541
            n_flat += 1
            continue
        serials.add(dn)                     # base serial: inbox/<base>/
        n_base += 1
        try:
            for sub in os.listdir(dp):      # nested lanes: inbox/<base>/~<suffix>/
                if sub.startswith("~") and os.path.isdir(os.path.join(dp, sub)):
                    serials.add(dn + sub)
                    n_nested += 1
        except OSError:
            pass
    return serials, n_base, n_nested, n_flat


def is_deaf(unread: int, age_any: float, serial: str, reaped: set) -> bool:
    """DEAF predicate, factored out so the positive control can exercise BOTH directions.

    A guard that only ever fires on the failing input is untested: an enumerator that finds 0
    deaf lanes and an enumerator that cannot see lanes print the same 0. The self-test asserts
    this returns True on a genuinely-deaf lane AND False on a live one.
    """
    return (unread > 0 and SESSION_ALIVE_S < age_any < DEAF_RECENT_S
            and serial not in reaped)


# CODEX SEATS (2026-09-03, 0.0.0_AB_MSTR 93745 item 2, measured at 15:11Z): a Codex seat's inbox detector is
# NON-CONSUMING by design (org/mcp/CODEX_INBOX_MONITOR.md) -- it never moves a file to read/ and the runtime has no
# ack surface, so `unread` is structurally > 0 the moment mail arrives and the predicate above read five live,
# committing Codex lanes as DEAF. The unread limb carries no information for such a seat; its liveness oracle is
# its heartbeat (codex-agent-heartbeat.py registers and beats the full serial). A seat IS a Codex seat when the
# launcher's runtime dir exists: .runtime/codex-seats/<serial sanitized exactly as codex-agent-heartbeat.py does>.
_CODEX_RUNTIME = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".runtime", "codex-seats")


def is_codex_seat(serial: str) -> bool:
    return os.path.isdir(os.path.join(_CODEX_RUNTIME, re.sub(r"[^A-Za-z0-9_.~-]", "_", serial)))


def is_deaf_codex(hb_age: float, serial: str, reaped: set) -> bool:
    """A Codex seat is deaf when its HEARTBEAT has gone quiet inside the deaf window (never on unread mail)."""
    return SESSION_ALIVE_S < hb_age < DEAF_RECENT_S and serial not in reaped


# Denominator for the deaf verdict, published by gather() and printed by --blocks.
# "A verdict without its universe is not a verdict" (CTO 205745Z, render_open_deploys).
ENUM_STATS: dict = {"enumerated": 0, "base": 0, "nested": 0, "legacy_flat": 0, "orphans": 0}


PROJECTS_DIR = os.path.join(ROOT, "org", "projects")
_TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))


def project_codes() -> list[str]:
    """Registered project codes (org/projects/*.json basenames), longest-first."""
    codes = set()
    try:
        for p in glob.glob(os.path.join(PROJECTS_DIR, "*.json")):
            codes.add(os.path.splitext(os.path.basename(p))[0])
    except OSError:
        pass
    return sorted(codes, key=len, reverse=True)


def commits_by_author(days: int = 14) -> dict:
    """{author: [commits]} via fabric-commits.py --json (decoupled). Empty on any failure."""
    try:
        out = subprocess.run(
            [sys.executable, os.path.join(_TOOLS_DIR, "fabric-commits.py"),
             "--json", "--days", str(days)],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120,
        )
        return json.loads(out.stdout).get("by_author", {})
    except (OSError, ValueError, subprocess.SubprocessError):
        return {}


def _distinctive_tokens(codes: list[str]) -> dict:
    """{token: code} for code-tokens (split on _) that are UNIQUE to one code and len>=5.
    Lets a summary short-form ('MDLP', 'GLDINC', 'DEMOAUTH') map to its full code, while
    excluding shared macros (ADVI, ADHC, FIND...) that don't disambiguate."""
    tok_codes: dict[str, set] = {}
    for c in codes:
        for tok in c.split("_"):
            if len(tok) >= 5:
                tok_codes.setdefault(tok, set()).add(c)
    return {tok: next(iter(cs)) for tok, cs in tok_codes.items() if len(cs) == 1}


def infer_project(summary: str, agent_commits: list[dict], codes: list[str],
                  distinctive: dict | None = None) -> str:
    """Map an agent to a project (deterministic, best-effort): (1) exact code in summary,
    (2) a distinctive code-token in summary, (3) its latest commit's code, (4) dominant
    code across recent commits, (5) (unmapped). The one-line summary is authoritative;
    this tag is the inferred project context."""
    s = summary or ""
    for c in codes:                      # (1) longest-first; first exact summary hit wins
        if c in s:
            return c
    if distinctive is None:
        distinctive = _distinctive_tokens(codes)
    for tok, code in distinctive.items():  # (2) distinctive short-form in summary
        if tok in s:
            return code
    commits = agent_commits or []
    for cm in commits:                   # (3) latest commit's code (most recent work)
        for c in codes:
            if c in cm.get("subject", ""):
                return c
    hits = Counter()                     # (4) dominant code across recent commits
    for cm in commits:
        tt = cm.get("subject", "")
        for c in codes:
            if c in tt:
                hits[c] += 1
                tt = tt.replace(c, " ")
    if hits:
        return hits.most_common(1)[0][0]
    return "(unmapped)"


# The fabric MANDATES a leading state token (org/XXX.md Section F: "keep your broker summary an
# accurate status -- WORKING: <task> / IDLE: available / BLOCKED: <what> / BLOCKED-SOVEREIGN: <ask>").
# That token IS the declared state. Everything after it is PROSE.
_STATE_PREFIX = re.compile(
    r'^\s*\[?\s*(blocked[\s\-_]*sovereign|blocked|working|idle[\s\-_]*available|idle|standing[\s\-_]*by)'
    r'\s*\]?\s*[:\-—]',
    re.IGNORECASE)
_PREFIX_TO_STATE = {
    "blocked-sovereign": "SOVEREIGN", "blocked": "BLOCKED",
    "working": "WORKING", "idle-available": "IDLE", "idle": "IDLE", "standing-by": "IDLE",
}


def classify_declared(summary: str) -> tuple[str, str]:
    """Parse the self-declared state from the summary. Returns (state, detail).

    >> THE LEADING STATE TOKEN IS AUTHORITATIVE AND SHORT-CIRCUITS EVERY PROSE HEURISTIC. <<

    THE BUG THIS FIXES (COO, 2026-07-13 -- and it flagged the CTO one hour after he landed the rule
    it violates): the prose heuristics below scan for the SUBSTRING "blocked on"/"blocker"/"blocked:"
    ANYWHERE in the summary. A CTO summary reading

        "IDLE-AVAILABLE: all AoR blockers RULED (...). Nothing blocked on me."

    contains the substring "blocked on" -- inside the words "NOTHING BLOCKED ON ME" -- and was scored
    **BLOCKED**. So was a CVO summary reporting that the blockers were CLOSED.

    *** IT MEASURED THE TOKEN, NOT THE BEHAVIOUR. *** (CLAUDE.md Rule 22a: CENSUS BY FUNCTION, NEVER
    BY MENTION -- a matcher cannot tell an assertion from its negation.)

    And the failure is ANTI-CORRELATED WITH THE TRUTH: the more explicitly an agent declares itself
    unblocked ("no blockers", "nothing blocked on me", "blockers RULED"), the more certainly it trips
    the flag -- while an agent that says nothing passes clean. `blocked>0` is a /drive GATE, so this
    taxed exactly the reporting behaviour the fabric wants and sent COO chasing phantoms.

    THE DATA TO DO THIS RIGHT WAS ALREADY THERE: both mis-flagged agents led with a correct, machine-
    readable state token, and the classifier ignored it to go grep the prose. So: match the PREFIX
    first and return. The prose heuristics survive ONLY as a fallback for a summary that declares no
    token at all (legacy/undeclared), which is the case they were actually written for.
    """
    s = (summary or "").strip()
    low = s.lower()
    if not s:
        return ("UNCLEAR", "(no summary set)")

    # --- AUTHORITATIVE: the declared state token. No prose is consulted. ---
    m = _STATE_PREFIX.match(s)
    if m:
        key = re.sub(r'[\s_]+', '-', m.group(1).strip().lower())
        state = _PREFIX_TO_STATE.get(key)
        if state:
            # A BLOCKED-prefixed summary may still be a sovereign ASK; keep that refinement,
            # but only for a summary that actually declared itself BLOCKED.
            if state == "BLOCKED" and ("sovereign" in low or "needs andrew" in low
                                       or "awaiting andrew" in low):
                return ("SOVEREIGN", s)
            return (state, s)

    # --- FALLBACK ONLY: no state token declared. Legacy prose heuristics. ---
    # Sovereign request -- a block REQUESTING an Andrew/MSTR ruling (NOT a report of a
    # past ruling). Request-phrasing only: explicit BLOCKED-SOVEREIGN token, or a
    # request verb (needs/awaiting/pending/requires) + andrew/sovereign. Deliberately
    # excludes report phrasings ("per andrew ruling", "andrew-direct", "sovereign
    # decision made") that caused false escalations.
    sov_markers = ("blocked-sovereign", "[sovereign", "[bl-sov",
                   "needs andrew", "awaiting andrew", "pending andrew", "requires andrew",
                   "needs sovereign", "awaiting sovereign", "pending sovereign",
                   "requires sovereign", "sovereign-decision-request", "needs a sovereign",
                   "needs a ruling from andrew", "sovereign call needed",
                   "needs sovereign ruling", "sovereign discretion needed")
    if any(m in low for m in sov_markers):
        return ("SOVEREIGN", s)
    # Explicit blocked -- with a NEGATION GUARD. Even in the token-less fallback, a matcher
    # must not read "NO blockers" / "NOTHING blocked on me" / "NOT blocked" as a block. A
    # substring matcher cannot tell an assertion from its negation, so the negation is checked
    # FIRST and wins. (Same defect, one level down: it is the reason the prefix rule above exists.)
    _negated = ("no blockers", "no blocker", "nothing blocked", "not blocked", "none blocked",
                "no blocks", "nothing is blocked", "blockers ruled", "blockers closed",
                "blockers cleared", "unblocked", "no longer blocked")
    if not any(n in low for n in _negated):
        if "blocked:" in low or "blocked on" in low or low.startswith("blocked") \
           or "[blocked" in low or "blocker:" in low:
            return ("BLOCKED", s)
    # Soft-block: holding/pending a ruling or decision (a hold that stalls a
    # workstream until someone decides -- the single-point block class COO must
    # resolve). Distinct from "awaiting next TO" idle (those phrases not matched here).
    softblock = ("holding for", "holding build for", "holding build pending",
                 "pending ruling", "pending a ruling", "awaiting ruling",
                 "for ruling on", "pending decision", "awaiting decision",
                 "needs a ruling", "pending coo ruling", "blocked pending",
                 "held pending", "gated on a decision", "awaiting a decision")
    if any(m in low for m in softblock):
        return ("BLOCKED", s)
    # Idle / available (explicit or the common legacy phrasings)
    # NOTE: "no blockers" was REMOVED from this list 2026-07-13. It is a statement about
    # BLOCKERS, not an assertion of IDLENESS -- and it produced the MIRROR of the BLOCKED bug:
    # an agent mid-build reporting "grinding the round-8.2 build, no blockers" was classified
    # IDLE, so /drive would dispatch fresh work onto a busy agent. Same mention-vs-function
    # defect, opposite bucket. (Found by the test written for the BLOCKED half.)
    idle_markers = ("idle", "available", "standing by", "stand-down", "stand down",
                    "nothing to", "no work", "quiet", "parked",
                    "awaiting", "at-gate", "at gate", "no-work")
    if any(m in low for m in idle_markers):
        return ("IDLE", s)
    # Otherwise treat a non-empty summary as a work description
    return ("WORKING", s)


_ASCII_MAP = {
    "—": "-", "–": "-", "’": "'", "‘": "'",
    "“": '"', "”": '"', "…": "...", "•": "*", " ": " ",
}


def ascii_clean(s: str) -> str:
    """Sanitize a summary for display: map common unicode to ASCII, drop the rest.
    Keeps the workspace ASCII-only norm + avoids Windows charmap truncation if the
    fabric-check output is ever captured to a log/CloudWatch."""
    if not s:
        return ""
    for u, a in _ASCII_MAP.items():
        s = s.replace(u, a)
    return s.encode("ascii", "ignore").decode("ascii")


def humum(sec) -> str:
    """Human-readable age."""
    if sec is None:
        return "--"
    if sec < 0:
        return "?"
    if sec < 90:
        return f"{int(sec)}s"
    if sec < 5400:
        return f"{int(sec/60)}m"
    return f"{int(sec/3600)}h"


def gather() -> list[dict]:
    now = time.time()
    liveness = {}
    try:
        with open(LIVENESS, "r", encoding="utf-8", errors="replace") as f:
            liveness = json.load(f)
    except (OSError, ValueError):
        liveness = {}

    # candidate serials: registered (liveness.json) UNION recently-active (telemetry)
    # UNION any serial with unread top-level inbox (a deaf lane may be telemetry-stale
    # + unregistered yet still have a pile of undelivered messages -- must not be filtered out)
    serials = set(liveness.keys())
    try:
        for fn in os.listdir(TELDIR):
            if fn.endswith(".jsonl") and fn != ".jsonl":
                serials.add(fn[:-len(".jsonl")])
    except OSError:
        pass
    # UNION every inbox identity on disk -- BOTH dir conventions, base + nested ~lanes.
    # Unconditional (no "has a top-level .md" precondition): the relevance filter below is what
    # drops dormant lanes, and it does so on telemetry+registration, not on a directory listing
    # taken at the wrong path. A lane must be ENUMERABLE before it can be judged.
    inbox_serials, n_base, n_nested, n_flat = enumerate_inbox_lanes()
    serials.update(inbox_serials)
    ENUM_STATS.update({"enumerated": len(inbox_serials), "base": n_base,
                       "nested": n_nested, "legacy_flat": n_flat, "orphans": 0})

    reaped = reaped_recently()
    rows = []
    for serial in serials:
        tel = telemetry_signals(serial)
        info = liveness.get(serial, {})
        summary = info.get("summary", "")
        hb = float(info.get("last_seen_epoch") or 0)
        registered = serial in liveness
        unread, unread_newest = unread_inbox(serial)
        # Mail stranded in the legacy flat decoy dir: counted for EVERY enumerated lane (before
        # the relevance filter), never counted as delivered. Non-zero = a real reachability hole.
        ENUM_STATS["orphans"] += legacy_flat_orphans(serial)

        last_any = tel["last_any"]
        last_work = tel["last_work"]
        age_any = (now - last_any) if last_any else 1e12
        age_work = (now - last_work) if last_work else 1e12

        # relevance filter: skip dormant historical lanes. Keep a lane only if it is
        # registered, recently active, OR a DEAF candidate (unread + recently-a-live-
        # session). A long-offline lane with leftover mail (unread but no telemetry in
        # 2h) is NOT actionable here -- skip it.
        deaf_candidate = unread > 0 and age_any < DEAF_RECENT_S
        if not registered and age_any > RELEVANCE_S and not deaf_candidate:
            continue

        # objective liveness from telemetry (ground truth)
        if age_work <= LIVE_WORK_S:
            live = "LIVE"
        elif age_any <= SESSION_ALIVE_S:
            live = "ALIVE"     # session alive but no recent substantive work
        else:
            live = "STALE"

        decl_state, detail = classify_declared(summary)

        # DEAF: unread messages piling in the CANONICAL inbox while telemetry is quiet
        # (>600s) = the lane's Monitor isn't delivering + it's not self-ticking to re-arm.
        # Post-LD-0157 (no /work self-tick) this is the reachability failure mode for a
        # lane whose persistent Monitor died -- OR, per 2026-07-09, was never armed at all.
        # ("Absent" and "died" are different states and only one of them respawns.)
        if is_codex_seat(serial):
            # a Codex seat's unread count is structurally non-zero (non-consuming detector): judge its heartbeat
            deaf = is_deaf_codex((now - hb) if hb else 1e12, serial, reaped)
        else:
            deaf = is_deaf(unread, age_any, serial, reaped)  # reaped lanes excluded (COO tuning)

        # coherence: does declared status match objective telemetry?
        coherence = "OK"
        if deaf:
            coherence = "DEAF"      # unread inbox + telemetry-quiet = unreachable lane
        elif live == "STALE" and decl_state == "WORKING":
            coherence = "PHANTOM"   # claims working, telemetry says dead
        elif live in ("LIVE", "ALIVE") and decl_state == "UNCLEAR":
            coherence = "UNCLEAR"   # alive but declares no clear state
        elif live == "STALE" and not registered:
            coherence = "GONE"      # not registered + no recent telemetry

        rows.append({
            "serial": serial,
            "live": live,
            "declared": decl_state,
            "coherence": coherence,
            "age_work_s": None if age_work > 1e11 else round(age_work),
            "age_any_s": None if age_any > 1e11 else round(age_any),
            "last_tool": tel["last_tool"],
            "summary": summary,
            "detail": detail,
            "registered": registered,
            "hb_age_s": round(now - hb) if hb else None,
            "unread": unread,
        })
    return rows


def bucket(rows: list[dict]) -> dict:
    """First-match-wins priority. Actionable buckets (BLOCKED/SOVEREIGN/STALE_VERIFY)
    float to the top of attention; declared-idle beats telemetry-quiet (a parked
    agent legitimately makes no tool calls); NEEDS_STATUS captures the status-hygiene
    gap (empty/undeclared summary) Andrew wants surfaced."""
    b = {"WORKING": [], "IDLE": [], "BLOCKED": [], "SOVEREIGN": [],
         "DEAF": [], "STALE_VERIFY": [], "NEEDS_STATUS": [], "STALE": []}
    for r in rows:
        if r["coherence"] == "DEAF":
            # unreachable lane (unread inbox + telemetry-quiet) -- highest-priority
            # reachability emergency: it cannot be tasked until respawned.
            b["DEAF"].append(r)
        elif r["declared"] == "SOVEREIGN":
            b["SOVEREIGN"].append(r)
        elif r["declared"] == "BLOCKED":
            b["BLOCKED"].append(r)
        elif r["coherence"] == "UNCLEAR" or r["declared"] == "UNCLEAR":
            # empty / no clear state declared -- status hygiene gap
            b["NEEDS_STATUS"].append(r)
        elif r["declared"] == "IDLE":
            # declared idle/parked/available -- telemetry-quiet is consistent; fine
            b["IDLE"].append(r)
        elif r["live"] == "STALE":
            # summary reads as work but no tool activity > 600s: finished-but-stale
            # summary, OR a stuck/dead session. Needs a look (could be a stuck owner).
            b["STALE_VERIFY"].append(r)
        else:
            b["WORKING"].append(r)
    return b


def render(rows: list[dict]) -> str:
    b = bucket(rows)
    out = []
    out.append(f"FABRIC CHECK  ({time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())})")
    out.append("liveness = telemetry-derived dual-signal (LD-0070): LIVE<120s work, ALIVE<600s any, STALE>600s")
    out.append("")

    def section(title, key, hint=""):
        items = b[key]
        head = f"{title} ({len(items)})"
        if hint:
            head += f"   {hint}"
        out.append(head)
        if not items:
            out.append("  (none)")
        for r in sorted(items, key=lambda x: x["serial"]):
            aw = humum(r["age_work_s"])
            aa = humum(r["age_any_s"])
            agestr = f"work {aw}/act {aa}"
            s = ascii_clean((r["summary"] or "").replace("\n", " "))
            if len(s) > 140:
                s = s[:137] + "..."
            out.append(f"  {r['serial']:<30} [{r['live']:<5}] {agestr:<16} | {s}")
        out.append("")

    # DEAF section -- custom (show unread count; the actionable detail)
    out.append(f"DEAF / UNREACHABLE ({len(b['DEAF'])})   <-- unread inbox + telemetry-quiet: lane can't be tasked; COO -> MSTR RESPAWN")
    if not b["DEAF"]:
        out.append("  (none)")
    for r in sorted(b["DEAF"], key=lambda x: x["serial"]):
        aa = humum(r["age_any_s"])
        out.append(f"  {r['serial']:<30} [{r['live']:<5}] act {aa:<6} unread={r.get('unread', 0)} | "
                   f"{ascii_clean((r['summary'] or '(no summary)'))[:90]}")
    out.append("")

    section("WORKING", "WORKING")
    section("IDLE / AVAILABLE", "IDLE")
    section("BLOCKED", "BLOCKED", "<-- COO /drive: resolve or escalate EACH")
    section("SOVEREIGN-DECISION REQUESTS", "SOVEREIGN", "<-- needs Andrew/MSTR ruling; COO declares")
    section("STALE-VERIFY (summary reads as work, telemetry > 600s)", "STALE_VERIFY",
            "<-- stuck/dead session OR finished-but-stale summary: verify or nudge a refresh")
    section("NEEDS-STATUS (no clear working/idle/blocked declared)", "NEEDS_STATUS",
            "<-- ask agent to set WORKING: / IDLE: available / BLOCKED: <what>")
    section("STALE (quiet, declared-idle)", "STALE")

    nd = len(b["DEAF"])
    nb, ns, nsv = len(b["BLOCKED"]), len(b["SOVEREIGN"]), len(b["STALE_VERIFY"])
    nns = len(b["NEEDS_STATUS"])
    out.append(f"SUMMARY: {len(b['WORKING'])} working | {len(b['IDLE'])} idle | "
               f"{nd} deaf | {nb} blocked | {ns} sovereign-req | {nsv} stale-verify | "
               f"{nns} needs-status")
    # machine-parseable line for /drive chaining
    out.append(f"FABRIC-CHECK-RESULT deaf={nd} blocked={nb} sovereign={ns} stale_verify={nsv} "
               f"needs_status={nns}")
    if nd:
        out.append("ACTION-REQUIRED: DEAF lane(s) -- unreachable, can't be tasked. COO: respawn-request to MSTR (re-arms its Monitor). Critical for ~A lanes (no self-tick).")
    elif nb or ns:
        out.append("ACTION-REQUIRED: blocked/sovereign present -- COO must resolve or escalate this cycle.")
    elif nsv:
        out.append("ACTION-REQUIRED: stale-verify present -- COO: confirm those owners are alive (could be a single-point stall).")
    else:
        out.append("ACTION-REQUIRED: none critical -- fabric flowing; nudge any needs-status to declare state.")
    return "\n".join(out)


def render_agents(rows: list[dict]) -> str:
    """Agent -> project activity: each non-dead agent mapped to the project it's working,
    with a one-line what-it's-doing (from its broker summary). Project inferred from the
    summary's project-code reference, else its recent commits."""
    codes = project_codes()
    distinctive = _distinctive_tokens(codes)
    ba = commits_by_author()
    live = [r for r in rows if r["live"] in ("LIVE", "ALIVE")]
    mapped = []
    for r in live:
        proj = infer_project(r["summary"], ba.get(r["serial"], []), codes, distinctive)
        one = ascii_clean((r["summary"] or "(no summary)").replace("\n", " "))
        if len(one) > 110:
            one = one[:107] + "..."
        mapped.append((proj, r["serial"], r["live"], one))
    mapped.sort(key=lambda x: (x[0] == "(unmapped)", x[0], x[1]))
    out = [f"AGENT -> PROJECT ACTIVITY ({len(mapped)} live agents)  [telemetry-mapped]"]
    if not mapped:
        out.append("  (no live agents)")
    for proj, serial, lv, one in mapped:
        out.append(f"  {proj:<22} {serial:<28} [{lv:<5}] {one}")
    return "\n".join(out)


def render_open_deploys() -> str:
    """TO #5 (deploy-completion ledger contract): surface OPEN deploy ledgers
    in every fabric-check pass so a half-landed deploy cannot slip past a COO
    /drive tick (NEVER-law e38cc2b16). Read-only here -- the RED alert itself
    is fired by `deploy_ledger.py check --red` (chained in /drive)."""
    state_dir = Path(__file__).resolve().parent.parent / "org" / "critical_paths" / ".open_deploys"
    # Only real deploy-completion sentinels. SKIP dotfiles -- e.g. .unindexed_red_state.json is
    # deploy_ledger.py's own alert-dedup STATE MAP ({ledger-path -> last-RED-alert-ts}), NOT an
    # open-deploy sentinel; it has no `opened_at` and was throwing a spurious [UNREADABLE] each scan.
    # (Filtering by name-suffix would be wrong -- real sentinels aren't all named *_deploy_completion,
    # e.g. nfra-toolhealth-emit-wiring.json -- so exclude dotfiles, not by-suffix.)
    sentinels = sorted(
        p for p in state_dir.glob("*.json") if not p.name.startswith(".")
    ) if state_dir.exists() else []
    if not sentinels:
        # Carry the denominator here too: "0 scanned" is a DIFFERENT claim from "we found none",
        # and a reader must be able to tell an empty universe from an unread one.
        return "OPEN-DEPLOYS: 0 scanned, 0 held, 0 stranded -- no sentinels; nothing half-landed"
    from datetime import datetime, timezone

    # HELD / SOVEREIGN-GATED alignment (CTO-assigned 2026-07-09; read-side only, NO new semantics).
    # This reader used to classify on `age_h > window_hours` alone -- a PROXY -- while deploy_ledger
    # classifies on the LEGS (the PROPERTY: every apply leg proven + only verify legs open + a named
    # structured gate => HELD, tracked-not-stranded). Same sentinels, same cycle, OPPOSITE verdicts:
    # fabric-check called 5 legitimately-HELD ledgers "OVERRUN: close or roll back" every cycle, so
    # COO's own block-detector cried wolf 5x forever -- and the correct response to a detector that
    # always cries wolf is to ignore it, which is precisely how a REAL half-landed deploy gets missed.
    #
    # We IMPORT deploy_ledger's _qualifies_as_held rather than re-implement it. A second copy of
    # "is this stranded?" would be the same proxy-vs-property bug one layer up; single-sourcing means
    # the two instruments cannot diverge again. _qualifies_as_held reads the LEGS, so a genuinely
    # half-landed strand (an open APPLY leg) can never claim HELD to escape the RED.
    _held_import_err = None
    try:
        if _TOOLS_DIR not in sys.path:
            sys.path.insert(0, _TOOLS_DIR)
        from deploy_ledger import (  # noqa: E402  -- single source of truth
            DEFAULT_HELD_STALE_DAYS, HELD_STATUS, _held_age_days, _qualifies_as_held,
        )
    except Exception as e:  # fail LOUD, never silently fall back to the proxy
        _held_import_err = e

    now = datetime.now(timezone.utc)
    lines = []
    n_risk = 0    # genuinely stranded: past window, NOT held  -> the half-landed risk
    n_held = 0    # HELD-SOVEREIGN-GATED: apply-proven, verify open, named gate -> tracked
    n_stale = 0   # a legit hold that sat too long -> a distinct nudge, not the half-land RED
    if _held_import_err is not None:
        lines.append(f"  [DEGRADED] cannot import deploy_ledger HELD semantics ({_held_import_err}) "
                     "-- falling back to the age>window PROXY; HELD ledgers will read as stranded")
    for sp in sentinels:
        try:
            st = json.loads(sp.read_text(encoding="utf-8"))
            opened = datetime.fromisoformat(st["opened_at"])
            age_h = (now - opened).total_seconds() / 3600.0
            open_legs = [leg["id"] for leg in st["legs"] if not leg.get("proof")]

            held_ok = False
            if _held_import_err is None:
                held_ok, _held_reason = _qualifies_as_held(st)
            if held_ok:
                gate = st["gate"]
                held_days = _held_age_days(st, now)
                if held_days is not None and held_days > DEFAULT_HELD_STALE_DAYS:
                    n_stale += 1
                    lines.append(f"  [HELD-STALE] {st['slug']} held={held_days:.1f}d "
                                 f"(>{DEFAULT_HELD_STALE_DAYS}d) gate={gate['type']}/{gate['ref']} "
                                 f"open-verify={open_legs} author={st['author']}"
                                 "  <- nudge the gate or reconsider the hold")
                else:
                    n_held += 1
                    hd = f"{held_days:.1f}d" if held_days is not None else "?"
                    lines.append(f"  [{HELD_STATUS}] {st['slug']} held={hd} "
                                 f"gate={gate['type']}/{gate['ref']} open-verify={open_legs} "
                                 f"author={st['author']}  -- apply legs proven; tracked-not-stranded")
                continue

            # NOT held -> the original logic, unchanged. "stranded" (a half-landed RISK) means the
            # deploy OVERRAN its window with legs still open. An IN-WINDOW open leg is just PENDING.
            # A ledger that CLAIMS a gate but does not qualify (e.g. an open apply leg) lands here --
            # the anti-escape-hatch, identical to deploy_ledger's.
            if age_h > st.get("window_hours", 4):
                n_risk += 1
                claim = " [HELD-CLAIM REJECTED]" if st.get("gate") else ""
                lines.append(f"  [PAST-WINDOW] {st['slug']} age={age_h:.1f}h "
                             f"stranded={open_legs} author={st['author']}{claim}"
                             "  <- OVERRUN: close or roll back")
            else:
                lines.append(f"  [in-window] {st['slug']} age={age_h:.1f}h "
                             f"pending={open_legs} author={st['author']}")
        except Exception as e:  # never let a corrupt sentinel kill the check
            lines.append(f"  [UNREADABLE] {sp.name} err={e}")

    # DENOMINATOR (CTO acceptance criterion 3, 205745Z): "a verdict without its universe is not a
    # verdict." Always state how many sentinels were SCANNED alongside the verdict, so a reader can
    # tell "0 stranded because we checked 5 and all are held" apart from "0 stranded because we
    # checked nothing" -- the exact ambiguity that let this reader be silent-and-trusted.
    note = []
    if n_stale:
        note.append(f"{n_stale} of the held are HELD-STALE -- nudge the gate")
    if not n_risk and not n_held and not n_stale:
        note.append("all in-window, none stranded")
    hdr = (f"OPEN-DEPLOYS: {len(sentinels)} scanned, {n_held + n_stale} held, {n_risk} stranded"
           + (f" ({'; '.join(note)})" if note else "") + ":")
    return "\n".join([hdr] + lines)


def enum_denominator() -> str:
    """Machine-parseable universe of the deaf verdict, appended to FABRIC-CHECK-RESULT."""
    e = ENUM_STATS
    return (f"enumerated={e['enumerated']} base_serials={e['base']} nested_lanes={e['nested']} "
            f"legacy_flat={e['legacy_flat']} flat_orphans={e['orphans']}")


def deaf_denominator_line(nd: int = 0) -> str:
    """Human line stating the deaf numerator OVER its universe.

    `deaf=0` from a check that enumerated 39 lanes and `deaf=0` from a check that enumerated
    none are the same string and opposite facts. Print the denominator so a reader can tell
    them apart -- the same rule render_open_deploys() already applies to deploy sentinels.
    """
    e = ENUM_STATS
    line = (f"DEAF-COVERAGE: deaf={nd} over {e['enumerated']} enumerated inboxes "
            f"({e['base']} base serials, {e['nested']} nested ~lanes, "
            f"{e['legacy_flat']} flat-lane dirs)")
    if e["orphans"]:
        # The WARN names the WRITER, not the lane (COO requirement, 232922Z). A reader who sees
        # `flat_orphans=4` reaches for the obvious local fix -- delete the files, "clean up" the
        # dirs -- which DESTROYS THE ONLY EVIDENCE the dispatch path is broken and leaves
        # operator.py:539 writing the next one. The loud->quiet inversion: the obvious remedy
        # removes the symptom that is the sole evidence of the defect.
        line += (
            f"\nWARN: flat_orphans={e['orphans']} -- message(s) written to an UNWATCHED path "
            f"(inbox/<base>~<lane>/). No Monitor watches it; no check_inbox reads it."
            f"\n      FIX THE WRITER (.tools/operator.py:539 -- `inbox_root / agent` resolves a "
            f"~lane serial to the flat dir and mkdir's it on demand)."
            f"\n      Do NOT delete these files: they are the only evidence the dispatch path is broken."
            f"\n      Do NOT hand-deliver them into a live agent either -- a queued GO has no expiry, "
            f"and delivering a stale authorization executes it. Report to the sender; they decide."
        )
    return line


def self_test() -> int:
    """Positive control. Both directions, on a synthetic inbox tree.

    CTO 231518Z: "assert the enumerator finds a known-live lane ... it must report a lane that IS
    deaf, and must NOT report one that is live." A guard exercised only on its failing input is
    indistinguishable from a guard that always fires -- and one exercised only on its passing
    input is indistinguishable from a guard that never fires. Both directions or it proves nothing.
    """
    import shutil
    import tempfile
    global INBOX_DIR
    saved = INBOX_DIR
    tmp = tempfile.mkdtemp(prefix="fabcheck-selftest-")
    passed = failed = 0

    def check(name, got, want):
        nonlocal passed, failed
        if got == want:
            passed += 1
            print(f"  ok   {name}")
        else:
            failed += 1
            print(f"  FAIL {name}: got {got!r}, want {want!r}")

    try:
        INBOX_DIR = tmp
        base = os.path.join(tmp, "A_AGENT")
        os.makedirs(os.path.join(base, "~B"))
        os.makedirs(os.path.join(base, "~C"))
        os.makedirs(os.path.join(tmp, "A_AGENT~B"))          # legacy flat decoy, same lane
        os.makedirs(os.path.join(tmp, "D_AGENT~E"))          # legacy-flat-only lane
        os.makedirs(os.path.join(tmp, "Z_AGENT"))            # plain base serial

        # --- path resolution mirrors server.py + inbox-watch.sh ---
        check("lane_inbox_dir(lane) -> nested",
              lane_inbox_dir("A_AGENT~B"), os.path.join(tmp, "A_AGENT", "~B"))
        check("lane_inbox_dir(base) -> flat",
              lane_inbox_dir("Z_AGENT"), os.path.join(tmp, "Z_AGENT"))

        # --- THE REGRESSION: mail in the canonical nested dir must be SEEN ---
        with open(os.path.join(base, "~B", "m1.md"), "w") as f:
            f.write("x")
        check("nested unread is seen (the 2026-07-09 miss)", unread_inbox("A_AGENT~B")[0], 1)

        # --- THE DECOY: mail in the flat dir must NOT be read as delivered ---
        with open(os.path.join(tmp, "A_AGENT~B", "stranded.md"), "w") as f:
            f.write("x")
        check("flat decoy not counted as delivered", unread_inbox("A_AGENT~B")[0], 1)
        check("flat decoy surfaced as an orphan", legacy_flat_orphans("A_AGENT~B"), 1)
        check("base serial has no orphan concept", legacy_flat_orphans("Z_AGENT"), 0)

        # --- ENUMERATION: nested lanes exist as candidates at all ---
        serials, n_base, n_nested, n_flat = enumerate_inbox_lanes()
        check("enumerator finds nested lane ~B", "A_AGENT~B" in serials, True)
        check("enumerator finds nested lane ~C (known-live, no mail)", "A_AGENT~C" in serials, True)
        check("enumerator finds legacy-flat-only lane", "D_AGENT~E" in serials, True)
        check("enumerator finds base serial", "Z_AGENT" in serials, True)
        check("nested lane count", n_nested, 2)
        check("base serial count", n_base, 2)          # A_AGENT, Z_AGENT
        check("legacy flat count", n_flat, 2)          # A_AGENT~B, D_AGENT~E

        # --- POSITIVE CONTROL, BOTH DIRECTIONS, on the deaf predicate ---
        quiet = (SESSION_ALIVE_S + DEAF_RECENT_S) / 2.0   # telemetry-quiet but recently a session
        check("DEAF fires on a genuinely deaf lane", is_deaf(1, quiet, "A_AGENT~B", set()), True)
        check("DEAF silent on a LIVE lane (fresh telemetry)", is_deaf(1, 5.0, "A_AGENT~B", set()), False)
        check("DEAF silent on a lane with no mail", is_deaf(0, quiet, "A_AGENT~B", set()), False)
        check("DEAF silent on an intentionally-reaped lane",
              is_deaf(1, quiet, "A_AGENT~B", {"A_AGENT~B"}), False)
        check("DEAF silent on a long-dead lane (beyond window)",
              is_deaf(1, DEAF_RECENT_S + 1, "A_AGENT~B", set()), False)
        # --- CODEX seats: the unread limb is meaningless (non-consuming detector); the heartbeat decides ---
        check("CODEX: fresh heartbeat -> not deaf even with mail piled", is_deaf_codex(5.0, "C_AGENT~J", set()), False)
        check("CODEX: heartbeat quiet inside the window -> deaf", is_deaf_codex(quiet, "C_AGENT~J", set()), True)
        check("CODEX: never beat (age 1e12) -> beyond the window, not deaf-needing-respawn", is_deaf_codex(1e12, "C_AGENT~J", set()), False)
        check("CODEX: reaped -> silent", is_deaf_codex(quiet, "C_AGENT~J", {"C_AGENT~J"}), False)
        check("CODEX: a serial with no runtime dir is not a Codex seat", is_codex_seat("A_AGENT~B_NO_SUCH_SEAT"), False)

        # --- the pre-fix path proves the bug was real, not theoretical ---
        legacy_read = _count_md(os.path.join(INBOX_DIR, "A_AGENT~B"))[0]
        canonical_read = _count_md(lane_inbox_dir("A_AGENT~B"))[0]
        check("pre-fix path read the decoy (1 stranded, not the 1 real msg)", legacy_read, 1)
        check("post-fix path reads the canonical dir", canonical_read, 1)
        os.remove(os.path.join(tmp, "A_AGENT~B", "stranded.md"))
        check("pre-fix path on a clean decoy returns 0 while real mail waits",
              (_count_md(os.path.join(INBOX_DIR, "A_AGENT~B"))[0],
               _count_md(lane_inbox_dir("A_AGENT~B"))[0]), (0, 1))
    finally:
        INBOX_DIR = saved
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"\nself-test: {passed} passed, {failed} failed")
    return 1 if failed else 0


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        sys.exit(self_test())
    rows = gather()
    if "--json" in args:
        print(json.dumps({"rows": rows, "ts": time.time()}, indent=2))
        return
    if "--agents" in args:
        print(render_agents(rows))
        return
    if "--blocks" in args:
        b = bucket(rows)
        triage = ([("DEAF", r) for r in b["DEAF"]]
                  + [("BLOCKED", r) for r in b["BLOCKED"]]
                  + [("SOVEREIGN", r) for r in b["SOVEREIGN"]]
                  + [("STALE-VERIFY", r) for r in b["STALE_VERIFY"]])
        if not triage:
            print("FABRIC-CHECK: no deaf / blocks / sovereign-requests / stale-verify. Fabric flowing.")
            print(f"FABRIC-CHECK-RESULT deaf=0 blocked=0 sovereign=0 stale_verify=0 {enum_denominator()}")
            print(deaf_denominator_line())
            # DEFECT-2 FIX (COO 212646Z): OPEN-DEPLOYS is the NEVER-law deploy-completion gate
            # (e38cc2b16). It was printed ONLY on the triage-NON-empty path, so in --blocks mode a
            # CLEAN agent-axis returned here and the deploy gate NEVER RAN. Its visibility was
            # COUPLED to an unrelated condition -- whether some agent happened to be DEAF/BLOCKED --
            # and a clean fabric is the NORMAL state, so the gate was normally SILENT. "Fabric
            # flowing" was printed by a path that had not read a single deploy sentinel: the message
            # asserted more than the function verified. A detector going quiet is not a detector
            # being correct. The gate now runs on EVERY --blocks pass, clean or not.
            print(render_open_deploys())
            return
        print(f"FABRIC-CHECK TRIAGE ({len(triage)} items need COO attention):")
        for tag, r in triage:
            s = ascii_clean((r["summary"] or "(no summary)").replace("\n", " "))
            extra = f" unread={r.get('unread', 0)}" if tag == "DEAF" else ""
            print(f"  [{tag}] {r['serial']} [{r['live']}]{extra} :: {s[:150]}")
        print(f"FABRIC-CHECK-RESULT deaf={len(b['DEAF'])} blocked={len(b['BLOCKED'])} "
              f"sovereign={len(b['SOVEREIGN'])} stale_verify={len(b['STALE_VERIFY'])} "
              f"{enum_denominator()}")
        print(deaf_denominator_line(len(b["DEAF"])))
        print(render_open_deploys())
        return
    print(render(rows))
    print("")
    print(render_agents(rows))
    print("")
    print(render_open_deploys())


if __name__ == "__main__":
    main()
