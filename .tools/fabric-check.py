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
import json
import os
import sys
import time

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


def unread_inbox(serial: str) -> tuple[int, float]:
    """(count, newest_mtime) of unread top-level *.md in inbox/{serial}/.
    The stream Monitor mv's delivered messages to read/, so top-level *.md left in
    the inbox = messages NOT yet processed by the lane's Monitor. A pile of these on
    a telemetry-quiet lane = the lane is DEAF (dead Monitor + no self-tick to re-arm)."""
    d = os.path.join(INBOX_DIR, serial)
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


def classify_declared(summary: str) -> tuple[str, str]:
    """Parse the self-declared state from the summary. Returns (state, detail)."""
    s = (summary or "").strip()
    low = s.lower()
    if not s:
        return ("UNCLEAR", "(no summary set)")
    # Sovereign request -- highest precedence (a block needing Andrew/MSTR ruling)
    sov_markers = ("blocked-sovereign", "[sovereign", "sovereign decision",
                   "sovereign-decision", "needs andrew", "andrew ruling",
                   "needs sovereign", "sovereign discretion", "sovereign ruling")
    if any(m in low for m in sov_markers):
        return ("SOVEREIGN", s)
    # Explicit blocked
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
    idle_markers = ("idle", "available", "standing by", "stand-down", "stand down",
                    "nothing to", "no blockers", "no work", "quiet", "parked",
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
    try:
        for dn in os.listdir(INBOX_DIR):
            dp = os.path.join(INBOX_DIR, dn)
            if os.path.isdir(dp) and any(f.endswith(".md") for f in os.listdir(dp)):
                serials.add(dn)
    except OSError:
        pass

    rows = []
    for serial in serials:
        tel = telemetry_signals(serial)
        info = liveness.get(serial, {})
        summary = info.get("summary", "")
        hb = float(info.get("last_seen_epoch") or 0)
        registered = serial in liveness
        unread, unread_newest = unread_inbox(serial)

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

        # DEAF: unread messages piling in the top-level inbox while telemetry is quiet
        # (>600s) = the lane's Monitor isn't delivering + it's not self-ticking to re-arm.
        # Post-LD-0157 (no /work self-tick) this is the reachability failure mode for a
        # lane whose persistent Monitor died (esp. ~A lanes the broker can't push to).
        deaf = unread > 0 and SESSION_ALIVE_S < age_any < DEAF_RECENT_S

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


def main():
    args = sys.argv[1:]
    rows = gather()
    if "--json" in args:
        print(json.dumps({"rows": rows, "ts": time.time()}, indent=2))
        return
    if "--blocks" in args:
        b = bucket(rows)
        triage = ([("DEAF", r) for r in b["DEAF"]]
                  + [("BLOCKED", r) for r in b["BLOCKED"]]
                  + [("SOVEREIGN", r) for r in b["SOVEREIGN"]]
                  + [("STALE-VERIFY", r) for r in b["STALE_VERIFY"]])
        if not triage:
            print("FABRIC-CHECK: no deaf / blocks / sovereign-requests / stale-verify. Fabric flowing.")
            print("FABRIC-CHECK-RESULT deaf=0 blocked=0 sovereign=0 stale_verify=0")
            return
        print(f"FABRIC-CHECK TRIAGE ({len(triage)} items need COO attention):")
        for tag, r in triage:
            s = ascii_clean((r["summary"] or "(no summary)").replace("\n", " "))
            extra = f" unread={r.get('unread', 0)}" if tag == "DEAF" else ""
            print(f"  [{tag}] {r['serial']} [{r['live']}]{extra} :: {s[:150]}")
        print(f"FABRIC-CHECK-RESULT deaf={len(b['DEAF'])} blocked={len(b['BLOCKED'])} "
              f"sovereign={len(b['SOVEREIGN'])} stale_verify={len(b['STALE_VERIFY'])}")
        return
    print(render(rows))


if __name__ == "__main__":
    main()
