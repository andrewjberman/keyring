#!/usr/bin/env python3
"""
operator_tool.py -- Project-closure operator for persistent agent-driven execution.
(Invoked via the `operator` PATH shim. File named operator_tool.py -- NOT operator.py --
 because `.tools/` lands on sys.path[0] and an `operator.py` there shadows the stdlib
 `operator` module, breaking every `.tools/*.py` invocation. Renamed per Andrew 2026-07-10.

 REGRESSED AND RESTORED 2026-07-29 (0.0.0_AB_MSTR~Z): the 07-10 rename was only ever made in
 the working tree and NEVER COMMITTED -- `operator_tool.py` appears in no commit, while
 `operator.py` stayed in HEAD and kept accruing work (F-013 @97801044b). So the hazard was
 live for ~19 days. Measured cost at restore time: 17 of 23 python-shebang `.tools/comp-*`
 died on `AttributeError: partially initialized module 're'` -- among them comp-which AND
 comp-grep/comp-glob, i.e. Rule 21's rail entrypoint and BOTH its designated fallbacks, plus
 comp-freshness and the comp-denytest/comp-tagauthz gates.

 DO NOT RE-ADD an `operator.py` here. The failure is silent at the rename site and only
 surfaces as an unrelated-looking circular-import crash in OTHER tools.)

Premise: while a project is "active", the agent does not stop until every task
order for that project is <status>complete</status>. Forks in the road (state
ambiguity, unresolvable dependencies, missing evidence) elevate to CTO, who
resolves based on historical patterns + best judgment.

MANDATORY for 2.0.0_SA_COO when driving a registered project.
OPTIONAL for any agent managing a long-running process on a project.

Semantics:
  The operator inspects current project state (JSON + task orders + inferred
  dependency state) and emits a directive for the agent's current turn. One
  invocation = one directive. The agent runs the operator at the top of each
  turn until the operator signals DONE or FORK.

Exit codes:
  0   continue    -- pending/staged TOs remain; directive emitted with next action
  1   done        -- every TO for this project is complete
  2   fork        -- ambiguity detected; elevation body emitted; agent MCPs CTO

Usage:
  operator.py <PROJECT_CODE>                 emit directive (exit 0/1/2)
  operator.py <PROJECT_CODE> --agent SERIAL  scope directive to a specific agent
  operator.py <PROJECT_CODE> --render        emit .tools/operator-<PROJECT>.sh
  operator.py <PROJECT_CODE> --elevate       emit CTO-elevation MCP body
  operator.py <PROJECT_CODE> --json          emit machine-readable state

Project code format: {4-char MACRO}_{6-char CODE}, e.g. ADVI_ROLLUP.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Windows cp1252 stdout corrupts non-ASCII (em-dashes in project phases, etc.).
# Force UTF-8 with replacement so operator output is stable.
if isinstance(sys.stdout, io.TextIOBase):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = REPO_ROOT / "org" / "projects"
TIER_ROOTS = [
    REPO_ROOT / "org" / "tier1_exec",
    REPO_ROOT / "org" / "tier2_senior",
    REPO_ROOT / "org" / "tier3_junior",
]
TOOLS_DIR = REPO_ROOT / ".tools"
BROKER_DB = REPO_ROOT / "org" / "mcp" / "broker.db"
LIVENESS_THRESHOLD_S = 120  # seconds before an agent is considered stale

PROJECT_CODE_RE = re.compile(r"^[A-Z]{4}_[A-Z0-9]{6}$")
STATUS_RE = re.compile(r"<status>\s*([A-Za-z_]+)\s*</status>")
ID_RE = re.compile(r"<id>\s*(.+?)\s*</id>", re.DOTALL)
ISSUED_TO_RE = re.compile(r"<issued_to>\s*(.+?)\s*</issued_to>", re.DOTALL)
DEP_STATUS_RE = re.compile(r'<dependency\b[^>]*?\bstatus="([A-Za-z_]+)"', re.DOTALL)
DEP_TO_RE = re.compile(r'<dependency\b[^>]*?\bto="([^"]+)"', re.DOTALL)


def die(msg: str, code: int = 2) -> None:
    print(f"[OPERATOR] {msg}", file=sys.stderr)
    sys.exit(code)


def validate_code(code: str) -> None:
    if not PROJECT_CODE_RE.match(code):
        die(f"project code '{code}' does not match {{MACRO}}_{{CODE}} (e.g. ADVI_ROLLUP)", code=3)


def load_project(code: str) -> dict:
    """F-013: routed through the sovereign-exclusion loader.

    A DRIVER, not a display tool -- it drives a project's TOs to completion. A held
    code reaching here would be ACTED ON, not merely printed. So the exclusion must
    bite on the by-CODE path, not only on enumeration:

        A FILTER ON THE LIST IS NOT A FILTER ON THE ITEM.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lib import project_registry as _pr

    if _pr.is_sovereign_excluded(code):
        die(
            f"project {code} is SOVEREIGN-EXCLUDED and cannot be driven.\n"
            "  Andrew, 2026-07-10: 'just exclude those items, we will deal with them later.'\n"
            "  This is a hold, not a bug. Do not route around it.",
            code=3,
        )
    data = _pr.load_project(code)
    if data is None:
        die(f"project {code} not found (or unreadable) under {PROJECTS_DIR}", code=3)
    return data


def scan_task_orders(code: str) -> list[dict]:
    results: list[dict] = []
    for tier_root in TIER_ROOTS:
        if not tier_root.exists():
            continue
        for agent_dir in sorted(tier_root.iterdir()):
            to_dir = agent_dir / "task_orders"
            if not to_dir.is_dir():
                continue
            for to_file in sorted(to_dir.glob(f"{code}.*.md")):
                results.append(parse_to(to_file, agent_dir.name))
    return results


def parse_to(path: Path, owning_agent: str) -> dict:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return {
            "file": str(path.relative_to(REPO_ROOT)),
            "owning_agent": owning_agent,
            "issued_to": owning_agent,
            "id": path.stem,
            "status": "unreadable",
            "deps_ok": False,
            "deps_raw": [],
            "error": str(e),
        }

    status_m = STATUS_RE.search(text)
    id_m = ID_RE.search(text)
    issued_m = ISSUED_TO_RE.search(text)
    dep_statuses = DEP_STATUS_RE.findall(text)
    dep_targets = DEP_TO_RE.findall(text)

    status = status_m.group(1).lower() if status_m else "unknown"
    deps_ok = all(d.lower() == "complete" for d in dep_statuses) if dep_statuses else True

    return {
        "file": str(path.relative_to(REPO_ROOT)),
        "owning_agent": owning_agent,
        "issued_to": (issued_m.group(1).strip() if issued_m else owning_agent).split()[0],
        "id": id_m.group(1).strip() if id_m else path.stem,
        "status": status,
        "deps_ok": deps_ok,
        "deps_raw": [d.lower() for d in dep_statuses],
        "dep_targets": [t.strip() for t in dep_targets],
    }


def classify(tos: list[dict]) -> dict:
    buckets = {
        "complete": [],
        "pending": [],
        "actionable_staged": [],  # staged AND deps met
        "blocked": [],              # staged/hold AND deps not met
        "unknown": [],
    }
    for to in tos:
        s = to["status"]
        if s in ("complete", "deferred"):
            # `deferred` = formally scoped out (re-PRD supersession, etc.).
            # Counts as "not outstanding" for project-closure purposes; same bucket as complete.
            buckets["complete"].append(to)
        elif s in ("pending", "active"):
            # `active` = mid-execution on another lane (e.g. base-lane TO appearing in a scoped project view).
            # Same bucket as pending — doesn't fork, doesn't block, just not-done-yet.
            buckets["pending"].append(to)
        elif s == "staged":
            (buckets["actionable_staged"] if to["deps_ok"] else buckets["blocked"]).append(to)
        elif s in ("hold", "blocked"):
            buckets["blocked"].append(to)
        else:
            buckets["unknown"].append(to)
    return buckets


def _find_cycle(edges: dict[str, list[str]]) -> list[str] | None:
    """DFS cycle detection. Returns the cycle path as a list of TO IDs, or None."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in edges}
    parent: dict[str, str | None] = {node: None for node in edges}

    def dfs(start: str) -> list[str] | None:
        stack = [(start, iter(edges.get(start, [])))]
        color[start] = GRAY
        while stack:
            node, it = stack[-1]
            next_node = next(it, None)
            if next_node is None:
                color[node] = BLACK
                stack.pop()
                continue
            if next_node not in color:
                continue  # dep target not in this project's TO set; ignore
            if color[next_node] == GRAY:
                # Cycle: reconstruct from next_node back to next_node via parent chain.
                cycle = [next_node]
                n = node
                while n is not None and n != next_node:
                    cycle.append(n)
                    n = parent[n]
                if n == next_node:
                    cycle.append(next_node)
                return list(reversed(cycle))
            if color[next_node] == WHITE:
                parent[next_node] = node
                color[next_node] = GRAY
                stack.append((next_node, iter(edges.get(next_node, []))))
        return None

    for start in edges:
        if color[start] == WHITE:
            cycle = dfs(start)
            if cycle:
                return cycle
    return None


def detect_forks(project: dict, buckets: dict, all_tos: list[dict]) -> list[dict]:
    forks: list[dict] = []

    if not all_tos:
        forks.append({
            "kind": "NO_TASK_ORDERS_FOUND",
            "detail": "Project is registered active but no TOs match its code prefix.",
            "suggest": "Confirm project code, author initial TOs, or close project if superseded.",
        })
        return forks

    # Cycle detection on the <dependency to="..."> graph.
    # TOs are nodes; edge A->B means A depends on B.
    id_set = {t["id"] for t in all_tos}
    edges = {t["id"]: [dep for dep in t["dep_targets"] if dep in id_set] for t in all_tos}
    cycle = _find_cycle(edges)
    if cycle:
        forks.append({
            "kind": "CIRCULAR_DEPS",
            "detail": cycle,
            "suggest": "Dependency chain contains a cycle -- at least one TO's <dependency to=...> tag is wrong or the decomposition is invalid. Cannot be resolved by waiting; must edit TO bodies.",
        })

    if buckets["unknown"]:
        forks.append({
            "kind": "UNKNOWN_STATUS",
            "detail": [t["file"] for t in buckets["unknown"]],
            "suggest": "Status tag missing or unrecognized; manual inspect + correct required.",
        })

    bad_pending = [t for t in buckets["pending"] if not t["deps_ok"]]
    if bad_pending:
        forks.append({
            "kind": "PENDING_WITHOUT_DEPS",
            "detail": [t["file"] for t in bad_pending],
            "suggest": "TO marked pending but dependencies not complete; verify whether TO was GO'd prematurely or deps are stale.",
        })

    forward_motion = buckets["pending"] or buckets["actionable_staged"]
    if not forward_motion and buckets["blocked"]:
        forks.append({
            "kind": "ALL_BLOCKED",
            "detail": [t["file"] for t in buckets["blocked"]],
            "suggest": "No pending/actionable TOs remain; every remaining TO is blocked on unmet deps or HOLD. Resolve a blocker or close project in partial state.",
        })

    if project.get("status") == "complete" and (buckets["pending"] or buckets["actionable_staged"] or buckets["blocked"]):
        forks.append({
            "kind": "PROJECT_MARKED_COMPLETE_BUT_TOS_OPEN",
            "detail": {
                "pending": [t["file"] for t in buckets["pending"]],
                "actionable_staged": [t["file"] for t in buckets["actionable_staged"]],
                "blocked": [t["file"] for t in buckets["blocked"]],
            },
            "suggest": "Project JSON says complete, but open TOs remain. Either project is prematurely closed OR these TOs are stale and need flip-to-complete.",
        })

    return forks


def emit_directive(code: str, project: dict, buckets: dict, forks: list[dict], agent_filter: str | None) -> int:
    total = sum(len(v) for v in buckets.values())
    complete = len(buckets["complete"])
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    print(f"# OPERATOR DIRECTIVE -- {code}")
    print(f"Generated: {now}")
    print(f"Progress:  {complete}/{total} TOs complete")
    phase = (project.get("phase") or "").strip()
    if phase:
        print(f"Phase:     {phase[:160]}")
    if agent_filter:
        print(f"Scoped to: {agent_filter}")
    print()

    if forks:
        print("## FORKS -- elevate to CTO")
        for f in forks:
            print(f"- **{f['kind']}**")
            detail = f["detail"]
            if isinstance(detail, (list, dict)):
                print(f"  detail: {json.dumps(detail, indent=2)}")
            else:
                print(f"  detail: {detail}")
            print(f"  suggest: {f['suggest']}")
        print()
        print("ACTION: run `operator.py " + code + " --elevate` to compose CTO MCP body, then dispatch via send_message.")
        print("LOOP_PACING: idle")
        return 2

    if total == 0:
        # Already folded into forks above, but guard.
        print("LOOP_PACING: idle")
        return 2

    if complete == total:
        print("## STATE: ALL TOs COMPLETE")
        print(f"Project {code} has reached terminal state. {complete} TOs closed.")
        print()
        print("ACTION: update `org/projects/{}.json` status to 'complete', move registry row to Completed table, stop operator loop for this project.".format(code))
        print("LOOP_PACING: done")
        return 1

    pending_scoped = _filter_by_agent(buckets["pending"], agent_filter)
    actionable_scoped = _filter_by_agent(buckets["actionable_staged"], agent_filter)
    blocked_scoped = _filter_by_agent(buckets["blocked"], agent_filter)

    if pending_scoped:
        pending_agents = list({t["issued_to"] for t in pending_scoped})
        liveness = check_liveness(pending_agents)
        dead = get_dead_agents(pending_agents)
        inbox_root = REPO_ROOT / "org" / "mcp" / "inbox"
        now_ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        print("## PENDING -- active now")
        for t in pending_scoped:
            agent = t["issued_to"]
            live = liveness.get(agent)
            pid = dead.get(agent)
            if pid is not None:
                liveness_tag = f" [AGENT_DEAD PID={pid} -- re-register prompt sent to base serial]"
                base = agent.split("~")[0]
                _write_reregister_prompt(agent, base, [t["id"]], inbox_root, now_ts, "2.0.0_SA_COO")
            elif live is False:
                liveness_tag = " [AGENT_DOWN -- MCP push required]"
            else:
                liveness_tag = " [LIVE]" if live else ""
            print(f"- [{agent}]{liveness_tag} {t['id']}")
            print(f"    file: {t['file']}")
        print()

    if actionable_scoped:
        print("## STAGED -- deps met, ready to GO")
        for t in actionable_scoped:
            print(f"- [{t['issued_to']}] {t['id']}")
            print(f"    file: {t['file']}")
        print()

    if blocked_scoped:
        print("## BLOCKED -- deps unmet / on HOLD")
        for t in blocked_scoped:
            deps = ",".join(t["deps_raw"]) or "--"
            print(f"- [{t['issued_to']}] {t['id']} (deps: {deps})")
            print(f"    file: {t['file']}")
        print()

    if not pending_scoped and not actionable_scoped:
        # Scoped view has no forward motion even though project overall does.
        print("## STATE: no forward motion for scoped agent -- project continues elsewhere.")
        print()
        print("ACTION: pick up a blocked TO's dependency, coordinate with upstream agent, or idle with heartbeat.")
        print("LOOP_PACING: idle")
        return 0

    print("ACTION:")
    if pending_scoped:
        print("  1. Drive each PENDING TO to close (validate evidence, Rule 7 pre-flag if applicable, flip to complete).")
        down = [t for t in pending_scoped if liveness.get(t["issued_to"]) is False]
        if down:
            for t in down:
                print(f"     AGENT_DOWN: send_message to {t['issued_to']} re: {t['id']} (channel push — inbox file already written)")
    if actionable_scoped:
        verb = "Send GO" if agent_filter != "2.0.0_SA_COO" else "Dispatch GO via MCP"
        print(f"  2. {verb} to STAGED TOs whose lane is idle.")
    print("  DO NOT STOP. Re-run operator at top of next turn.")
    print("LOOP_PACING: active")
    return 0


def _filter_by_agent(tos: list[dict], agent: str | None) -> list[dict]:
    if not agent:
        return tos
    return [t for t in tos if agent in t["issued_to"]]


def compose_elevation(code: str, project: dict, buckets: dict, forks: list[dict], agent: str | None) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    sender = agent or "2.0.0_SA_COO"

    if not forks:
        print(f"[OPERATOR] no forks detected on {code} -- elevation not required.")
        print(f"           Progress: {len(buckets['complete'])} complete / {sum(len(v) for v in buckets.values())} total.")
        if buckets["pending"] or buckets["actionable_staged"]:
            print("           ACTION: drive open TOs; re-run `operator " + code + "` for the directive.")
        return

    subject = f"OPERATOR ELEVATION -- {code}"
    body_lines = [
        f"Operator fork elevation generated {now} UTC.",
        "",
        f"Project phase: {(project.get('phase') or '').strip()[:240]}",
        "",
        "## Forks detected",
    ]
    for f in forks:
        body_lines.append(f"- **{f['kind']}**: {f['suggest']}")
        detail = f["detail"]
        if isinstance(detail, (list, dict)):
            body_lines.append("  ```")
            body_lines.append(json.dumps(detail, indent=2))
            body_lines.append("  ```")
        else:
            body_lines.append(f"  detail: {detail}")
    body_lines += [
        "",
        "## TO state",
        f"- complete:          {len(buckets['complete'])}",
        f"- pending:           {len(buckets['pending'])}",
        f"- actionable_staged: {len(buckets['actionable_staged'])}",
        f"- blocked:           {len(buckets['blocked'])}",
        f"- unknown:           {len(buckets['unknown'])}",
        "",
        "Requesting resolution per historical patterns + best judgment.",
        f"Operator is HALTED on {code} until your directive lands.",
    ]
    body = "\n".join(body_lines)

    print("## MCP-ready elevation -- paste into send_message")
    print(f"   from_agent: {sender}")
    print("   to_agent:   1.0.0_SA_CTO")
    print(f"   subject:    {subject}")
    print("   body:")
    for line in body.splitlines():
        print(f"     {line}")


def _pid_running(pid: int) -> bool:
    """Return True if the given PID is an active process. Platform-aware."""
    if pid <= 0:
        return False
    if sys.platform == "win32":
        # os.kill(pid, 0) is unreliable on Windows — use tasklist instead.
        try:
            import subprocess
            r = subprocess.run(
                ["tasklist", "/FI", f"PID eq {pid}", "/NH"],
                capture_output=True, text=True, timeout=5,
            )
            return str(pid) in r.stdout
        except Exception:
            return True  # assume alive if check fails
    else:
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False


def check_liveness(serials: list[str]) -> dict[str, bool]:
    """Query broker.db for agent liveness. Returns {serial: is_live}.

    An agent is live iff BOTH conditions hold:
      1. last_seen_epoch within LIVENESS_THRESHOLD_S (heartbeat recent)
      2. registered PID is still a running process
    If either fails the agent is considered dead/stale.
    """
    if not BROKER_DB.exists():
        return {}
    try:
        con = sqlite3.connect(str(BROKER_DB), timeout=3)
        now = time.time()
        rows = con.execute("SELECT serial, pid, last_seen_epoch FROM agents").fetchall()
        con.close()
        db = {r[0]: (r[1], r[2]) for r in rows}
        result = {}
        for s in serials:
            if s not in db:
                result[s] = False
                continue
            pid, last_seen = db[s]
            heartbeat_ok = (now - last_seen) < LIVENESS_THRESHOLD_S
            pid_ok = _pid_running(pid)
            result[s] = heartbeat_ok and pid_ok
        return result
    except Exception:
        return {}


def get_dead_agents(serials: list[str]) -> dict[str, int]:
    """Return {serial: pid} for agents whose PID is dead (session ended).

    Distinct from stale: a stale agent may just be slow on heartbeats.
    A dead agent has a PID that is no longer running — session definitely ended.
    """
    if not BROKER_DB.exists():
        return {}
    try:
        con = sqlite3.connect(str(BROKER_DB), timeout=3)
        rows = con.execute("SELECT serial, pid FROM agents").fetchall()
        con.close()
        dead = {}
        for serial, pid in rows:
            if serial in serials and pid and not _pid_running(pid):
                dead[serial] = pid
        return dead
    except Exception:
        return {}


def dispatch_gos(code: str, buckets: dict, agent_filter: str | None) -> int:
    """Write GO inbox messages and flip staged->pending for all actionable TOs.

    Groups by agent and sends ONE message per lane listing the full sequence
    the agent is authorized to execute — including currently-pending TOs that
    are already in motion. Agents must NOT stop between sequential TOs on their
    lane and wait for a new GO; the batch message covers the whole sequence.

    Returns the count of TOs dispatched.
    """
    actionable = _filter_by_agent(buckets["actionable_staged"], agent_filter)
    if not actionable:
        print("[DISPATCH] No actionable staged TOs — nothing to dispatch.")
        return 0

    inbox_root = REPO_ROOT / "org" / "mcp" / "inbox"
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    sender = "2.0.0_SA_COO"
    dispatched = 0

    # Group actionable TOs by agent.
    by_agent: dict[str, list[dict]] = {}
    for to in actionable:
        by_agent.setdefault(to["issued_to"], []).append(to)

    for agent, agent_tos in by_agent.items():
        inbox_dir = inbox_root / agent
        inbox_dir.mkdir(parents=True, exist_ok=True)

        # Also collect already-pending TOs for this agent — they're part of the
        # same authorized sequence and should be listed so the agent doesn't stop.
        already_pending = [
            t for t in buckets.get("pending", [])
            if t["issued_to"] == agent
        ]

        # NOT dead: [0] is an implicit bounds check (IndexError on empty). Deleting it --
        # ruff F841's 'obvious' fix -- would SILENTLY REMOVE A GUARD. Underscore keeps the
        # side-effect while silencing the lint. Pre-existing; preserved deliberately.
        _first_to = agent_tos[0]
        all_in_sequence = agent_tos + [t for t in already_pending if t not in agent_tos]

        # Build sequence block for the message body.
        seq_lines = []
        for i, t in enumerate(all_in_sequence):
            marker = "START HERE ->" if i == 0 else "  THEN ->"
            seq_lines.append(f"  {marker} {t['id']}")
            seq_lines.append(f"             {t['file']}")
        sequence_block = "\n".join(seq_lines)

        subject = f"GO -- {code} lane sequence ({len(all_in_sequence)} TOs)"
        sender_slug = re.sub(r"[^A-Za-z0-9]", "_", sender)[:30]
        subject_slug = re.sub(r"[^A-Za-z0-9]", "_", subject)[:55]
        filename = f"{timestamp}_{sender_slug}_{subject_slug}.md"

        msg = (
            f"# Message from {sender}\n"
            f"**To:** {agent}\n"
            f"**Date:** {timestamp}\n"
            f"**Subject:** {subject}\n\n"
            f"GO on the following sequence. Execute in order. "
            f"**Do NOT stop between TOs and wait for a new GO** — this message authorizes the full sequence.\n\n"
            f"SEQUENCE:\n{sequence_block}\n\n"
            f"RULE: If a TO is already complete when you reach it, move immediately to the next one. "
            f"Keep going until you hit a TO that is blocked (deps unmet) or the list is exhausted.\n\n"
            f"STARTUP CHECK: If your session resumed from context compaction, run the full Step 1b "
            f"startup sequence (register as {agent}, check_inbox + get_agent_status) BEFORE acting.\n\n"
            f"MCP COMPLETE to COO (2.0.0_SA_COO) after each TO with commit hash + evidence. "
            f"Final MCP when sequence exhausted.\n\n"
            f"-- operator.py --dispatch {timestamp}\n"
        )
        (inbox_dir / filename).write_text(msg, encoding="utf-8")
        print(f"[DISPATCH] GO -> {agent}: sequence of {len(all_in_sequence)} TOs")
        for t in agent_tos:
            print(f"[DISPATCH]   {t['id']}")

        # Flip staged -> pending for each actionable TO.
        for to in agent_tos:
            to_path = REPO_ROOT / to["file"]
            try:
                text = to_path.read_text(encoding="utf-8", errors="replace")
                note = f"<!-- auto-dispatch {timestamp} operator.py --dispatch -->"
                updated = re.sub(
                    r"<status>\s*staged\s*</status>(\s*<!--[^>]*-->)?",
                    f"<status>pending</status>{note}",
                    text,
                    count=1,
                )
                if updated != text:
                    to_path.write_text(updated, encoding="utf-8")
                    print(f"[DISPATCH] staged->pending: {to['file']}")
                else:
                    print(f"[DISPATCH] WARN: status not flipped (already pending?): {to['file']}")
            except OSError as e:
                print(f"[DISPATCH] WARN: could not flip {to['file']}: {e}", file=sys.stderr)
            dispatched += 1

    print(f"[DISPATCH] {dispatched} GO(s) sent for {code}.")

    # Liveness + PID check: flag dead/stale agents and auto-notify base serial.
    dispatched_agents = [t["issued_to"] for t in actionable]
    liveness = check_liveness(dispatched_agents)
    dead = get_dead_agents(dispatched_agents)

    for agent, is_live in liveness.items():
        if is_live:
            continue
        tos_for_agent = [t["id"] for t in actionable if t["issued_to"] == agent]
        pid = dead.get(agent)
        if pid is not None:
            # PID is dead — session ended. Auto-write re-register prompt to base serial.
            base_serial = agent.split("~")[0]
            print(f"[DISPATCH] AGENT_DEAD: {agent} — PID {pid} not running. Session ended. Auto-notifying base serial {base_serial}.")
            _write_reregister_prompt(agent, base_serial, tos_for_agent, inbox_root, timestamp, sender)
        else:
            print(f"[DISPATCH] AGENT_DOWN: {agent} — stale heartbeat; GO in inbox. COO must send_message via MCP. TOs: {', '.join(tos_for_agent)}")

    return dispatched


def _write_reregister_prompt(lane_serial: str, base_serial: str, to_ids: list[str], inbox_root: Path, timestamp: str, sender: str) -> None:
    """Write a re-register prompt to the base serial's inbox when a lane agent's PID is dead."""
    inbox_dir = inbox_root / base_serial
    inbox_dir.mkdir(parents=True, exist_ok=True)
    _base_slug = re.sub(r"[^A-Za-z0-9]", "_", base_serial)[:30]  # unused; re.sub is pure
    subject = f"REREGISTER -- {lane_serial} session ended"
    subject_slug = re.sub(r"[^A-Za-z0-9]", "_", subject)[:55]
    filename = f"{timestamp}_{re.sub(r'[^A-Za-z0-9]', '_', sender)[:30]}_{subject_slug}.md"
    msg = (
        f"# Message from {sender}\n"
        f"**To:** {base_serial}\n"
        f"**Date:** {timestamp}\n"
        f"**Subject:** {subject}\n\n"
        f"The {lane_serial} session has ended (PID dead). It has a pending GO waiting in its inbox.\n\n"
        f"Pending TOs: {', '.join(to_ids)}\n\n"
        f"ACTION: Start a new session, register as `{lane_serial}` (NOT `{base_serial}`), "
        f"then run check_inbox + get_agent_status to pick up the GO.\n\n"
        f"See org/XXX.md Step 1b for the full startup sequence.\n\n"
        f"-- operator.py --dispatch {timestamp}\n"
    )
    (inbox_dir / filename).write_text(msg, encoding="utf-8")
    print(f"[DISPATCH] Re-register prompt written to {base_serial} inbox.")


def render_shim(code: str, agent: str | None) -> None:
    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    out = TOOLS_DIR / f"operator-{code}"
    agent_arg = f'--agent "{agent}" ' if agent else ""
    script = f"""#!/bin/bash
# operator-{code} -- project operator shim (rendered by operator.py)
# Drives {code} to closure. MANDATORY for 2.0.0_SA_COO. Optional for other agents.
#
# Usage: operator-{code} [--agent SERIAL] [--elevate|--json|--render]
#
# Exit codes:
#   0  continue (directive emitted)
#   1  done (all TOs complete)
#   2  fork (elevate to CTO)

WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"
exec python "$WORKSPACE/.tools/operator.py" "{code}" {agent_arg}"$@"
"""
    out.write_text(script, encoding="utf-8")
    try:
        out.chmod(0o755)
    except OSError:
        pass  # Windows may not honour chmod; Git Bash still executes via #! line.
    print(f"[OPERATOR] rendered {out.relative_to(REPO_ROOT)}")


def emit_json(code: str, project: dict, buckets: dict, forks: list[dict]) -> None:
    payload = {
        "project": code,
        "phase": project.get("phase", ""),
        "status": project.get("status", ""),
        "counts": {k: len(v) for k, v in buckets.items()},
        "forks": forks,
        "tos": {
            k: [{"id": t["id"], "issued_to": t["issued_to"], "file": t["file"]} for t in v]
            for k, v in buckets.items()
        },
    }
    print(json.dumps(payload, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Project-closure operator. Emits a directive per turn until all TOs are complete.",
    )
    ap.add_argument("project_code", help="Project code, e.g. ADVI_ROLLUP")
    ap.add_argument("--agent", default=None, help="Filter directive to a specific agent serial. Omit for orchestrator-scope (recommended for COO/CTO).")
    ap.add_argument("--render", action="store_true", help="Render .tools/operator-<PROJECT> shim and exit 0")
    ap.add_argument("--elevate", action="store_true", help="Compose CTO MCP elevation body and exit 0")
    ap.add_argument("--json", action="store_true", help="Emit machine-readable state and exit 0")
    ap.add_argument("--dispatch", action="store_true", help="Auto-send GO messages + flip staged->pending for all actionable TOs, then emit directive")
    args = ap.parse_args()

    validate_code(args.project_code)
    project = load_project(args.project_code)
    tos = scan_task_orders(args.project_code)
    buckets = classify(tos)
    forks = detect_forks(project, buckets, tos)

    if args.render:
        render_shim(args.project_code, args.agent)
        return
    if args.dispatch:
        dispatch_gos(args.project_code, buckets, args.agent)
        # Fall through to emit_directive so caller gets the full state.
    if args.elevate:
        compose_elevation(args.project_code, project, buckets, forks, args.agent)
        return
    if args.json:
        emit_json(args.project_code, project, buckets, forks)
        return

    sys.exit(emit_directive(args.project_code, project, buckets, forks, args.agent))


if __name__ == "__main__":
    main()
