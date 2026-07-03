#!/usr/bin/env python3
"""USAGE signal -- tool/artifact un-invoked over N days (agent_telemetry + rail-log).

MILESTONE 3 (NFRA_COMPDEBT_PRD.md 8.3 / 3 / ruling-3). Reuses the existing invocation
streams -- org/mcp/agent_telemetry/*.jsonl (per-agent PostToolUse stream) + comp-which-rail.log
(comp-grep/comp-glob runs) -- to detect a tool/artifact that has not been invoked in N days.

RULE 22: a "not invoked in the telemetry we have" reading is a SYMPTOM = INFERRED. Telemetry
is bounded (~10-30d retention) and incomplete (not every path is instrumented), so absence of
an invocation is NOT proof of disuse -- it never promotes to a reserved word on its own.

RULING 3 (served-artifact coldness -- the honest v1 scope): there is NO query-log over served
JSON (the portal reads it from S3 via CloudFront; no Trino/Athena log). So for a SERVED
ARTIFACT, v1 does NOT claim coldness from access logs; it routes to the GRAPH no-consumer
signal (the graph structurally knows if a portal component reads the artifact) and STATES the
residual gap LOUDLY: end-user S3/CloudFront access-log coldness is UNCOVERED in v1 (a
fast-follow), never a false-clean.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_HERE = Path(__file__).resolve()
_COMP_DEBT = _HERE.parents[1]
if str(_COMP_DEBT) not in sys.path:
    sys.path.insert(0, str(_COMP_DEBT))
import grounding_lib as g  # noqa: E402

REPO = _HERE.parents[5]  # signals/ -> comp_debt -> graph -> modules -> org -> REPO
_TELEMETRY_DIR = REPO / "org" / "mcp" / "agent_telemetry"
_RAIL_LOG = REPO / "org" / "mcp" / "comp-which-rail.log"
# The canonical comp-TOOL invocation log (comp_log_auto.py appends every comp-* run). Markdown
# table: | YYYY-MM-DD | serial | TO | tool | args | result |. Covers comp-tool coldness (which
# agent_telemetry, logging Claude tools, and the rail-log, logging only comp-grep/glob, miss).
_COMP_TOOLS_LOG = REPO / "org" / "compiler-tools-log.md"

SIGNAL = "usage"
DEFAULT_WINDOW_DAYS = 30

# The residual gap comp-debt v1 does NOT cover -- stated on every served-artifact path so a
# cold-served claim is never a false-clean.
SERVED_ARTIFACT_RESIDUAL = (
    "USAGE v1 is TOOLS-ONLY (ruling-3): served-artifact coldness is NOT claimed from access "
    "logs. Use the GRAPH no-consumer signal for served artifacts; end-user S3/CloudFront "
    "access-log coldness is the STATED RESIDUAL gap (a fast-follow), never a false-clean.")

_RAIL_TS_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s")
_RAIL_TOOL_RE = re.compile(r"\btool=(\S+)")


def _now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(tzinfo=None)


def _parse_ts(s: str) -> dt.datetime | None:
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).replace(tzinfo=None)
    except (ValueError, AttributeError):
        return None


@dataclass
class LastSeen:
    name: str
    last_ts: dt.datetime | None
    source: str
    days_since: float | None


def last_seen(name: str, *, telemetry_dir: Path = _TELEMETRY_DIR,
              rail_log: Path = _RAIL_LOG, comp_tools_log: Path = _COMP_TOOLS_LOG) -> LastSeen:
    """Most-recent invocation of `name` across agent_telemetry (Claude-tool_name), the rail-log
    (comp-grep/glob tool=), and the compiler-tools-log (comp-* tool column). Returns
    LastSeen(last_ts=None) if never observed in the available (bounded) streams."""
    latest: dt.datetime | None = None
    src = "none"
    # compiler-tools-log.md: the canonical comp-tool invocation table
    if comp_tools_log.is_file():
        try:
            for line in comp_tools_log.read_text(encoding="utf-8", errors="replace").splitlines():
                if name not in line or not line.startswith("|"):
                    continue
                cols = [c.strip() for c in line.split("|")]
                # | '' | date | serial | TO | tool | args | result | -> tool at index 4
                if len(cols) < 6 or cols[4] != name:
                    continue
                ts = _parse_ts(cols[1])  # date-only YYYY-MM-DD -> midnight
                if ts and (latest is None or ts > latest):
                    latest, src = ts, "compiler-tools-log.md"
        except OSError:
            pass
    # agent_telemetry: per-agent PostToolUse stream (tool_name = the invoked tool)
    if telemetry_dir.is_dir():
        for fp in telemetry_dir.glob("*.jsonl"):
            try:
                for line in fp.read_text(encoding="utf-8", errors="replace").splitlines():
                    if name not in line:
                        continue
                    try:
                        row = json.loads(line)
                    except ValueError:
                        continue
                    if row.get("tool_name") != name and name not in str(row.get("tool_name", "")):
                        continue
                    ts = _parse_ts(str(row.get("ts", "")))
                    if ts and (latest is None or ts > latest):
                        latest, src = ts, f"agent_telemetry/{fp.name}"
            except OSError:
                continue
    # comp-which-rail.log: comp-grep/comp-glob RUN events
    if rail_log.is_file():
        try:
            for line in rail_log.read_text(encoding="utf-8", errors="replace").splitlines():
                mt = _RAIL_TOOL_RE.search(line)
                if not mt or mt.group(1) != name:
                    continue
                mts = _RAIL_TS_RE.match(line)
                ts = _parse_ts(mts.group(1)) if mts else None
                if ts and (latest is None or ts > latest):
                    latest, src = ts, "comp-which-rail.log"
        except OSError:
            pass
    days = ((_now() - latest).total_seconds() / 86400.0) if latest else None
    return LastSeen(name=name, last_ts=latest, source=src, days_since=days)


def usage_signal(name: str, *, window_days: int = DEFAULT_WINDOW_DAYS) -> g.Signal | None:
    """Emit a USAGE debt signal for a TOOL when un-invoked over the window. INFERRED only
    (telemetry is bounded + incomplete -> a symptom, Rule 22). None when recently used."""
    ls = last_seen(name)
    if ls.last_ts is not None and ls.days_since is not None and ls.days_since <= window_days:
        return None  # invoked within the window -> live use, no signal
    if ls.last_ts is None:
        state, detail = "un-invoked", (f"no invocation of '{name}' in the telemetry/rail streams "
                                       f"(bounded ~{window_days}d retention -- absence is INFERRED, "
                                       "not proof of disuse)")
    else:
        state, detail = "cold", (f"last invoked {ls.days_since:.0f}d ago ({ls.source}) "
                                 f"> {window_days}d window")
    return g.Signal(signal=SIGNAL, state=state, level=g.LEVEL_INFERRED,
                    grounding={"desired": f"USAGE tool-coldness: {detail}",
                               "applied": "telemetry is bounded + not fully instrumented -> INFERRED",
                               "resource_id": name})


def served_artifact_signal(resource_id: str, *, node_name: str | None = None) -> g.Signal:
    """Served-artifact coldness (ruling-3): route to the GRAPH no-consumer signal + attach the
    residual-gap statement. Returns a Signal carrying the graph verdict OR, if the graph gives
    no signal, an explicit RESIDUAL-UNCOVERED marker (never a false-clean)."""
    from . import graph as graph_signal_mod  # local import to avoid a heavy load unless used
    gs = graph_signal_mod.graph_signal(resource_id, node_name=node_name)
    if gs is not None:
        gs.grounding["usage_residual"] = SERVED_ARTIFACT_RESIDUAL
        return gs
    return g.Signal(signal=SIGNAL, state="served-residual-uncovered", level=g.LEVEL_INFERRED,
                    grounding={"desired": f"served artifact {resource_id}: no graph no-consumer signal",
                               "applied": SERVED_ARTIFACT_RESIDUAL,
                               "resource_id": resource_id})


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="comp-debt.signals.usage",
                                 description="USAGE signal -- tool/artifact coldness; emit-only. v1 TOOLS-ONLY.")
    ap.add_argument("--tool", metavar="NAME", help="check a tool/skill's invocation recency")
    ap.add_argument("--served", metavar="RESOURCE_ID", help="served-artifact coldness (routes to graph no-consumer)")
    ap.add_argument("--window-days", type=int, default=DEFAULT_WINDOW_DAYS)
    args = ap.parse_args(argv)
    if args.served:
        s = served_artifact_signal(args.served)
        print(f"{args.served}: [{s.level}] {s.state}")
        for k, v in s.grounding.items():
            print(f"    {k}: {v}")
        return 0
    if args.tool:
        ls = last_seen(args.tool)
        seen = (f"last seen {ls.days_since:.1f}d ago ({ls.source})" if ls.last_ts
                else "NOT seen in the telemetry/rail streams")
        print(f"tool '{args.tool}': {seen}")
        sig = usage_signal(args.tool, window_days=args.window_days)
        if sig:
            print(f"  -> USAGE signal [{sig.level}] {sig.state}: {sig.grounding['desired']}")
        else:
            print("  -> no USAGE signal (invoked within window)")
        print(f"  NOTE: {SERVED_ARTIFACT_RESIDUAL}")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
