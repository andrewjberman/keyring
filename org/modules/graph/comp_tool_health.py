"""
comp-tool-health -- NFRA_TOOLHEALTH TH-B: the fused per-tool 3-axis HEALTH query + action taxonomy.

ONE query answers, per comp-tool -- "is this tool USED, correctly-ROUTED-to, AND actually
EFFECTIVE -- or ignored / misrouted / dead?" -> a verdict in {KEEP, FIX, PROMOTE, RETIRE} + the action.
This is a FUSION over LIVE sources, NOT a new telemetry stack, and NOT a fork of COMPLEARN.

The three axes + their live sources (PRD SS2; a fusion, read-only):
  - USED            frequency / recency / by-role         tool_activity (rolling-log + telemetry),
                                                          via comp_learns_score.load_corpus (un-forked)
  - RAIL_CONSISTENT chosen-over-raw vs bypassed-to-grep   comproute-routing.jsonl ranked[]+kind
                                                          (decision-vs-disambiguation QUALITY) + the
                                                          comp-which-rail.log route/escape aggregate
  - EFFECTIVE       does running it REACH the answer?     TH-A's recurring blind-run probe -- PENDING
                                                          (folds COMPPROOF-B1; join seam documented below)

The action taxonomy (PRD SS3) -- classify_full() encodes it EXACTLY:
    USED  RAIL  EFFECTIVE  -> verdict
    yes   yes   yes        -> KEEP
    yes   yes   no         -> FIX      (used + reached-for but does not reach the answer -- the load-
                                        bearing catch; ONLY the EFFECTIVE probe flips KEEP<->FIX)
    no    --    yes        -> PROMOTE  (effective but ignored -- a routing/HUD miss, feeds COMPROUTE)
    no    --    no|unknown -> RETIRE   (dead)

TWO-PHASE (PRD SS4 / the TO): this file is Phase-A -- the query over the 2 LIVE axes. With EFFECTIVE
pending (None), it emits the CONFIDENT verdicts now (KEEP-provisional + RETIRE) and reports FIX/PROMOTE
CANDIDATES as `pending_effective` (the load-bearing EFFECTIVE axis lands via TH-A). Phase-B is a ONE-
LINE wire: pass TH-A's per-tool effective bool into classify_full() -- the SAME function then yields
KEEP vs FIX purely on the EFFECTIVE axis (the load-bearing property, proven in --self-test).

VALUE-ANCHORED HONESTY GATE (inherited from COMPLEARN SS5, non-negotiable, CTO-arch-gated): a tool is
NEVER scored healthy on invocation-count. A KEEP cites a VALUE metric -- the mean OUTCOME value of its
runs (via comp_route.outcome_value, the ONE shared signal) + rail decision-quality -- so a heavily-USED
tool with low-value outcomes is a FIX/RETIRE candidate, not a keep. is_preventive_tool() is inherited
un-modified so an enforcement GATE's low observed value-per-run (drift silently PREVENTED = unobservable)
is not mistaken for FIX. --self-test + --goodhart-audit prove zero usage-Goodhart.

REUSE, do NOT fork: comp_learns_score (load_corpus / is_preventive_tool / parse_routing_log) +
comp_route.outcome_value. COMPLEARN stays COMPLETE (closed 2026-07-01); its tables are read-only.

Read-only, deterministic, no LLM, advisory-only (the CTO ratifies retire/fix/promote -- this never
mutates a toolset; mirrors COMPLEARN + NFRA_DEBTSCAN never-auto-delete).

Usage:
    comp-tool-health                     # the fused health table (all tools, ranked worst-first)
    comp-tool-health --verdict FIX       # filter to one verdict (KEEP|FIX|PROMOTE|RETIRE)
    comp-tool-health --tool comp-blast   # one tool, full 3-axis detail
    comp-tool-health --json              # machine-readable
    comp-tool-health --goodhart-audit    # prove the verdict is value-driven, not usage-driven
    comp-tool-health --self-test         # taxonomy + value-anchored-honesty + EFFECTIVE-flips-FIX tests

Author: 0.8.0_AE_CloudComp (NFRA_TOOLHEALTH TH-B). 2026-07-02.
Spec: docs/architecture/NFRA_TOOLHEALTH_PRD.md (SS3/SS5/SS6.1) + task_orders/NFRA_TOOLHEALTH.TH-B.*.
Reuses: org/modules/graph/comp_learns_score.py (COMPLEARN P2), comp_route.py (COMPROUTE L3).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict

_WS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, _WS)

# REUSE the COMPLEARN substrate un-forked: the corpus loader (federates rolling+routing+rail via the
# tool_activity emitter parsers), the preventive-gate detector, and -- transitively -- the ONE shared
# outcome-weighting (comp_route.outcome_value) that COMPLEARN TRAINS and COMPROUTE DECIDES on.
from org.modules.graph import comp_learns_score as cls  # noqa: E402
from org.modules.graph.comp_route import outcome_value  # noqa: E402

# --------------------------------------------------------------------------------------------
# Tunables (health thresholds -- QUALITY gates, never usage-count gates).
# --------------------------------------------------------------------------------------------
MIN_USED_EVENTS = 3          # < this many logged runs across the whole ledger => effectively unused
HEALTHY_OUTCOME = 0.6        # mean outcome value >= this => value-healthy (reuses the scorer threshold)
HEALTHY_DECISION_RATE = 0.5  # when a tool wins a route, >= this fraction are confident DECISIONs (not hedges)

_TOOL_RX = re.compile(r"^(comp-[a-z0-9]+(?:-[a-z0-9]+)*|pipescript)$")
_MANIFEST = os.path.join("org", "modules", "graph", "graph-call-manifest.yaml")


# --------------------------------------------------------------------------------------------
# The canonical tool universe (manifest) -- so a MANIFESTED-but-unused tool is a real RETIRE catch.
# --------------------------------------------------------------------------------------------
def load_manifest_tools() -> set:
    """Parse the canonical tool ids out of graph-call-manifest.yaml (the mandated catalog). Best-effort:
    an empty set if unreadable -- the universe then degrades to live-stream tools only (never a crash)."""
    path = os.path.join(_WS, _MANIFEST)
    tools: set = set()
    if not os.path.exists(path):
        return tools
    id_rx = re.compile(r'^\s*(?:- )?(?:id|tool|high_level_tool|name):\s*"?([A-Za-z0-9_\- ]+)"?')
    with open(path, encoding="utf-8", errors="replace") as fh:
        for ln in fh:
            m = id_rx.match(ln)
            if not m:
                continue
            for tok in re.findall(r"comp-[a-z0-9-]+|pipescript", m.group(1).strip()):
                if _TOOL_RX.match(tok):
                    tools.add(tok)
    return tools


def _canonical_tool(raw) -> str | None:
    """Normalize a rolling-log/routing tool string to a canonical comp-tool id, or None if it is not a
    recognizable tool token (filters the ~300 noise strings in the free-text tool column)."""
    if not raw:
        return None
    t = str(raw).strip().strip("`").lower()
    if _TOOL_RX.match(t):
        return t
    # a multi-tool cell ("comp-iam+comp-platinum" / "comp-blast, comp-xray") -> first recognizable token
    m = re.search(r"comp-[a-z0-9]+(?:-[a-z0-9]+)*|pipescript", t)
    return m.group(0) if m and _TOOL_RX.match(m.group(0)) else None


# --------------------------------------------------------------------------------------------
# The canonical action taxonomy (PRD SS3) -- ONE function, the full 4-verdict table. The skeleton
# calls it with effective=None; TH-A (Phase-B) calls the SAME function with a real bool, and KEEP<->FIX
# then flips PURELY on the EFFECTIVE axis (acceptance #2). rail_consistent/effective are tristate:
# True | False | None(unknown/pending). Returns (verdict, pending_effective, reason).
# --------------------------------------------------------------------------------------------
def classify_full(used: bool, rail_consistent, effective, preventive: bool = False):
    """Encode PRD SS3 exactly. Load-bearing: for a USED + RAIL-consistent tool, EFFECTIVE is the SOLE
    discriminator between KEEP and FIX."""
    if not used:
        # no / -- / effective
        if effective is True:
            return "PROMOTE", False, "effective but not used -- a routing/HUD miss (feeds COMPROUTE)"
        if effective is False:
            return "RETIRE", False, "not used and not effective -- dead"
        return "RETIRE", True, ("not used; EFFECTIVE pending (TH-A) -- RETIRE unless the probe shows "
                                "effective-but-ignored (-> PROMOTE)")
    # used == True
    rail_bad = (rail_consistent is False)
    if effective is None:
        if rail_bad:
            return "FIX", True, ("used but rail-inconsistent (bypassed/hedged); EFFECTIVE pending (TH-A) "
                                 "-- a routing fix regardless, confirmed FIX if the probe also fails")
        return "KEEP", True, ("used + rail-consistent + value-healthy; EFFECTIVE pending (TH-A) -- "
                              "provisional KEEP, flips to FIX only if the probe shows it does not reach "
                              "the answer")
    if effective is True:
        if rail_bad:
            return "FIX", False, "used + effective but rail-inconsistent -- a routing fix"
        return "KEEP", False, "used + rail-consistent + effective"
    # effective is False, used
    if preventive:
        return "KEEP", False, ("used + rail-consistent; EFFECTIVE-probe low BUT this is a preventive "
                               "GATE (value = drift silently PREVENTED, unobservable) -- not a FIX "
                               "(CTO caveat; mandatory human judgment before any retire)")
    return "FIX", False, "used + reached-for but does NOT reach the answer -- the load-bearing FIX"


def decide(used: bool, value_healthy: bool, rail_consistent, effective, preventive: bool = False):
    """THE per-tool decision = the SS5 value gate OVERLAID on the SS3 taxonomy (classify_full).

    The value gate (inherited COMPLEARN SS5, non-negotiable): a USED tool whose OWN outcome data is
    KNOWN-LOW (mean outcome < HEALTHY_OUTCOME, from the RESULT column) is NOT a KEEP on usage -- it is
    a value-grounded FIX candidate NOW (the EFFECTIVE probe would corroborate). A preventive GATE is
    TEMPERED out of this (low observed value-per-run = drift silently prevented, not a FIX). Everything
    else delegates to the pure 3-axis taxonomy. Returns (verdict, pending_effective, reason)."""
    if used and not value_healthy and not preventive:
        return "FIX", (effective is None), ("value-grounded FIX: known-low mean outcome (< "
                                            f"{HEALTHY_OUTCOME}) -- used but its own runs do not deliver "
                                            "value (SS5 gate; usage does not protect it). The EFFECTIVE "
                                            "probe (TH-A) would corroborate.")
    return classify_full(used, rail_consistent, effective, preventive=preventive)


# --------------------------------------------------------------------------------------------
# USED axis -- presence + the VALUE-anchored outcome signal (never raw count for the verdict).
# --------------------------------------------------------------------------------------------
def build_used(rolling: list, telemetry: list) -> dict:
    """Per canonical tool: {events, roles, last_seen_epoch, mean_outcome_value, outcome_n}. The verdict
    reads mean_outcome_value (VALUE), not events (usage)."""
    agg: dict = defaultdict(lambda: {"events": 0, "roles": set(), "last": 0,
                                     "outcome_sum": 0.0, "outcome_n": 0})
    for r in rolling:
        tool = _canonical_tool(r.get("tool"))
        if not tool:
            continue
        a = agg[tool]
        a["events"] += 1
        if r.get("role"):
            a["roles"].add(r["role"])
        ts = r.get("ts_epoch") or 0
        if ts and ts > a["last"]:
            a["last"] = ts
        # VALUE: outcome value of this run (PASS/FAIL/...) via the ONE shared weighting. Only rows that
        # actually carry a result contribute -- a tool with no result cells has value_unknown, not 0.
        if r.get("result"):
            a["outcome_sum"] += outcome_value(r)
            a["outcome_n"] += 1
    for r in telemetry:                                   # telemetry adds activity volume + recency only
        tool = _canonical_tool(r.get("tool"))
        if not tool:
            continue
        a = agg[tool]
        a["events"] += 1
        if r.get("role"):
            a["roles"].add(r["role"])
        ts = r.get("ts_epoch") or 0
        if ts and ts > a["last"]:
            a["last"] = ts
    out: dict = {}
    for tool, a in agg.items():
        mean_outcome = round(a["outcome_sum"] / a["outcome_n"], 3) if a["outcome_n"] else None
        out[tool] = {
            "events": a["events"],
            "distinct_roles": len(a["roles"]),
            "last_seen_epoch": a["last"] or None,
            "mean_outcome_value": mean_outcome,           # the VALUE signal (None = unknown, not 0)
            "outcome_n": a["outcome_n"],
        }
    return out


# --------------------------------------------------------------------------------------------
# RAIL-CONSISTENT axis -- decision-vs-disambiguation QUALITY per tool (never route COUNT).
# --------------------------------------------------------------------------------------------
def build_rail(routing: list) -> dict:
    """Per canonical tool from comproute-routing.jsonl: how often it WON the route (ranked[0]) and,
    when it won, whether those routes were confident DECISIONs or hedged DISAMBIGUATIONs. rail-quality
    = decision-rate WHEN CHOSEN -- a QUALITY signal (the rail cleanly steers to it), never a count."""
    agg: dict = defaultdict(lambda: {"top_decision": 0, "top_disambig": 0, "top_other": 0,
                                     "runner_up": 0})
    for r in routing:
        kind = r.get("kind")
        ranked = r.get("ranked") or []
        for i, s in enumerate(ranked):
            tool = _canonical_tool(s.get("id"))
            if not tool:
                continue
            if i == 0:
                if kind == "decision":
                    agg[tool]["top_decision"] += 1
                elif kind == "disambiguation":
                    agg[tool]["top_disambig"] += 1
                else:
                    agg[tool]["top_other"] += 1
            else:
                agg[tool]["runner_up"] += 1
    out: dict = {}
    for tool, a in agg.items():
        wins = a["top_decision"] + a["top_disambig"] + a["top_other"]
        decisive = a["top_decision"]
        hedged = a["top_disambig"]
        denom = decisive + hedged
        decision_rate = round(decisive / denom, 3) if denom else None
        out[tool] = {"route_wins": wins, "decisions": decisive, "disambiguations": hedged,
                     "runner_up_only": a["runner_up"], "decision_rate": decision_rate}
    return out


def rail_state(rail_row: dict | None) -> str:
    """Tristate per tool: chosen | surfaced_not_chosen | no_signal.

    HONESTY NOTE (load-bearing): the rail log CANNOT cleanly say "tool X was bypassed to raw grep" --
    an escape row (RUN-GREP/RUN-GLOB) names the PRIMITIVE that ran, not the rich tool skipped. So the
    only clean per-tool rail signal is: does the router ROUTE queries TO this tool (chosen-over-raw)?
      - chosen             : the router routes to it (route_wins > 0) -- chosen-over-raw. (Router
                             CONFIDENCE -- decision vs disambiguation -- is a separate ANNOTATION, not
                             a verdict flip: a hedged near-tie is the router's nature on ambiguous
                             queries, NOT evidence the tool is bypassed.)
      - surfaced_not_chosen: appears as a routing CANDIDATE but is never the pick -- a routing/surfacing
                             note (feeds COMPROUTE), NOT a FIX.
      - no_signal          : never appears in the routing stream (most tools -- honest 'no signal').

    Deliberately NEVER returns an adverse 'inconsistent' that would force a used tool to FIX: the true
    used-but-ineffective FIX is the EFFECTIVE probe's (TH-A) job, and a value-grounded FIX comes from
    the RESULT-column outcome gate -- neither is router-hedging."""
    if not rail_row or rail_row["route_wins"] == 0:
        if rail_row and rail_row["runner_up_only"] > 0:
            return "surfaced_not_chosen"                  # a candidate, never the pick
        return "no_signal"
    return "chosen"


def router_confidence(rail_row: dict | None) -> str | None:
    """Annotation (NOT a verdict input): among the routes this tool WON, the share that were confident
    DECISIONs vs hedged DISAMBIGUATIONs. Low confidence => a COMPROUTE routing-rule refinement candidate
    (LD-0226), never a health FIX."""
    if not rail_row or rail_row.get("decision_rate") is None:
        return None
    return "high" if rail_row["decision_rate"] >= HEALTHY_DECISION_RATE else "low"


def rail_bool(state: str):
    """Map the rail tristate to the taxonomy's True/False/None. 'chosen' => rail-consistent (True);
    'surfaced_not_chosen'/'no_signal' => None (no ADVERSE signal -- never False, so router behavior
    alone never forces a used tool to FIX)."""
    return {"chosen": True, "surfaced_not_chosen": None, "no_signal": None}[state]


# --------------------------------------------------------------------------------------------
# Aggregate rail-enforcement context (fabric-level) + the ROUTE-POSTERIOR drift surface.
# Read the RAW rail log directly for an accurate route-vs-escape mix: the emitter's RAIL_ACTIONS
# whitelist predates the COMPROUTE DR2 posterior router, so it DROPS ROUTE-POSTERIOR* -- we count them
# here so the fabric context is honest AND we surface the drift (advisory; the emitter is not forked).
# --------------------------------------------------------------------------------------------
def rail_enforcement_context() -> dict:
    path = os.path.join(_WS, "org", "mcp", "comp-which-rail.log")
    route_family = {"ROUTE", "ROUTE-SURFACE", "ROUTE-POSTERIOR", "ROUTE-POSTERIOR-DISAMBIG"}
    escape_family = {"RUN-GREP", "RUN-GLOB", "RUN-LS"}
    counts: dict = defaultdict(int)
    if not os.path.exists(path):
        return {"available": False}
    line_rx = re.compile(r"^\S+\s+(\S+)\s")
    with open(path, encoding="utf-8", errors="replace") as fh:
        for ln in fh:
            m = line_rx.match(ln)
            if m:
                counts[m.group(1)] += 1
    routes = sum(counts[a] for a in route_family)
    escapes = sum(counts[a] for a in escape_family)
    denials = counts.get("DENY", 0)
    posterior_dropped = counts.get("ROUTE-POSTERIOR", 0) + counts.get("ROUTE-POSTERIOR-DISAMBIG", 0)
    return {
        "available": True,
        "routes": routes, "escapes": escapes, "denials": denials,
        "route_share": round(routes / (routes + escapes), 3) if (routes + escapes) else None,
        "emitter_whitelist_drop": {
            "route_posterior_rows_dropped": posterior_dropped,
            "note": ("tool_activity_emit.RAIL_ACTIONS predates the COMPROUTE DR2 posterior router and "
                     "excludes ROUTE-POSTERIOR* -- these routing rows are DROPPED from the catalog + "
                     "comp_learns_score. TH-B reads routing.jsonl (unaffected); advisory finding routed "
                     "to the COMPLEARN owner, emitter NOT forked."),
        },
    }


# --------------------------------------------------------------------------------------------
# The EFFECTIVE-feed join contract (TH-A) -- makes Phase-B a CONFIG wire, not a code change.
# --------------------------------------------------------------------------------------------
def load_effective_feed(path: str) -> dict:
    """Load TH-A's per-tool EFFECTIVE probe stream from JSON -> a normalized {canonical_tool: bool}.

    PROPOSED TH-A CONTRACT (subject to TH-A agreement per the TO's cross-domain coordination): a JSON
    object keyed by tool id, whose value is either a bare bool (effective yes/no) OR an object with an
    'effective' bool (extra probe fields ignored here). Examples both accepted:
        {"comp-blast": true, "comp-drift": false}
        {"comp-blast": {"effective": true, "reach": 0.9, "usability": 0.8}}
    Unknown/None values -> the tool stays EFFECTIVE-pending (never a silent False). Best-effort: a
    missing/unreadable file returns {} (the query degrades to the 2-live-axis skeleton, never a crash).
    When this feed is present, classify_full() yields the full 4-verdict and KEEP<->FIX flips PURELY on
    the EFFECTIVE axis -- the load-bearing property, now driven by real TH-A data."""
    feed: dict = {}
    if not path or not os.path.exists(path):
        return feed
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            raw = json.load(fh)
    except Exception:  # noqa: BLE001 -- a malformed feed degrades to skeleton, never crashes the query
        return feed
    if not isinstance(raw, dict):
        return feed
    for k, v in raw.items():
        tool = _canonical_tool(k)
        if not tool:
            continue
        if isinstance(v, bool):
            feed[tool] = v
        elif isinstance(v, dict) and isinstance(v.get("effective"), bool):
            feed[tool] = v["effective"]
        # anything else (None/number/str) -> leave the tool EFFECTIVE-pending (never a silent False)
    return feed


# --------------------------------------------------------------------------------------------
# The fused health query.
# --------------------------------------------------------------------------------------------
def health(effective_feed: dict | None = None) -> dict:
    """The ONE query. effective_feed = TH-A's {tool: bool} probe stream (Phase-B); None => the 2-live-
    axis skeleton (EFFECTIVE pending). Returns per-tool {used, rail_consistent, effective, verdict, ...}."""
    corpus = cls.load_corpus()
    manifest = load_manifest_tools()
    used_map = build_used(corpus.get("rolling", []), corpus.get("sessions", []))
    rail_map = build_rail(corpus.get("routing", []))
    effective_feed = effective_feed or {}

    # UNIVERSE = manifest tools (so a manifested-but-unused tool is a real RETIRE catch) UNION any live
    # tool carrying REAL signal (>= MIN_USED_EVENTS logged runs, or it won a route). This drops the
    # 1-2-event non-manifest free-text strings the rolling-log tool column contains (parse noise, not
    # tools) -- an honest universe, not a noise dump.
    def _has_signal(t: str) -> bool:
        um = used_map.get(t)
        rm = rail_map.get(t)
        return bool((um and um["events"] >= MIN_USED_EVENTS) or (rm and rm["route_wins"] > 0))

    universe = set(manifest) | {t for t in used_map if _has_signal(t)} | \
        {t for t in rail_map if _has_signal(t)}
    rows: list = []
    for tool in sorted(universe):
        um = used_map.get(tool)
        used = bool(um and um["events"] >= MIN_USED_EVENTS)
        mean_outcome = um["mean_outcome_value"] if um else None
        # value-healthy = outcomes are healthy OR unknown (absence of a RESULT is not evidence of
        # failure). A used tool with KNOWN-low outcomes fails the SS5 value gate (decide() -> FIX).
        value_healthy = (mean_outcome is None or mean_outcome >= HEALTHY_OUTCOME)
        preventive = cls.is_preventive_tool(tool)

        rmrow = rail_map.get(tool)
        rstate = rail_state(rmrow)
        rc_bool = rail_bool(rstate)
        eff = effective_feed.get(tool)                    # True/False from TH-A, else None (pending)
        verdict, pending, reason = decide(used, value_healthy, rc_bool, eff, preventive=preventive)

        rows.append({
            "tool": tool,
            "in_manifest": tool in manifest,
            "used": {
                "used": used,
                "events": um["events"] if um else 0,
                "distinct_roles": um["distinct_roles"] if um else 0,
                "last_seen_epoch": um["last_seen_epoch"] if um else None,
                "mean_outcome_value": mean_outcome,       # the VALUE metric the verdict rests on
                "outcome_n": um["outcome_n"] if um else 0,
            },
            "rail_consistent": {
                "state": rstate,
                "router_confidence": router_confidence(rmrow),   # annotation only (COMPROUTE feed)
                "detail": rmrow,
            },
            "effective": ("pending (TH-A)" if eff is None else eff),
            "verdict": verdict,
            "pending_effective": pending,
            "value_anchor": _value_anchor(used, mean_outcome, rstate, verdict, not value_healthy, preventive),
            "reason": reason,
        })

    rows.sort(key=lambda r: (_verdict_rank(r["verdict"], r["pending_effective"]),
                             -(r["used"]["events"])))
    counts = defaultdict(int)
    for r in rows:
        key = r["verdict"] + ("?" if r["pending_effective"] else "")
        counts[key] += 1
    return {
        "query": "fused per-tool 3-axis health (NFRA_TOOLHEALTH TH-B)",
        "phase": ("Phase-B (EFFECTIVE live from TH-A)" if effective_feed
                  else "Phase-A skeleton (2 live axes: USED + RAIL_CONSISTENT; EFFECTIVE pending TH-A)"),
        "corpus_source": corpus.get("source"),
        "value_metric": "mean OUTCOME value (comp_route.outcome_value) + rail decision-quality -- "
                        "NEVER invocation count (COMPLEARN SS5 gate, CTO-arch-gated)",
        "axes_live": ["USED", "RAIL_CONSISTENT"] + (["EFFECTIVE"] if effective_feed else []),
        "rail_enforcement": rail_enforcement_context(),
        "verdict_counts": dict(counts),
        "n_tools": len(rows),
        "tools": rows,
    }


def _value_anchor(used, mean_outcome, rstate, verdict, value_low, preventive) -> dict:
    """The explicit VALUE citation for the verdict (acceptance #3: every KEEP/PROMOTE cites value; no
    verdict rests on invocation-count). Machine-checkable -- keys are outcome/quality, never a count."""
    return {
        "mean_outcome_value": mean_outcome,               # value, not usage
        "value_healthy": (mean_outcome is None or mean_outcome >= HEALTHY_OUTCOME),
        "value_unknown": mean_outcome is None,
        "rail_quality": rstate,
        "value_low_flag": value_low,
        "preventive_gate": preventive,
        "basis": ("KEEP rests on value-healthy outcomes + rail decision-quality, NOT usage count"
                  if verdict == "KEEP" else
                  "PROMOTE rests on rail/effective signal without usage, NOT usage count"
                  if verdict == "PROMOTE" else
                  "FIX/RETIRE rests on low value-outcome / dead-signal, NOT usage count"),
    }


_VERDICT_ORDER = {"FIX": 0, "PROMOTE": 1, "RETIRE": 2, "KEEP": 3}


def _verdict_rank(verdict: str, pending: bool):
    # worst-first: confirmed FIX above pending; KEEP last. pending nudges within a verdict group.
    return (_VERDICT_ORDER.get(verdict, 9), 1 if pending else 0)


# --------------------------------------------------------------------------------------------
# Render.
# --------------------------------------------------------------------------------------------
def _render(h: dict, verdict_filter: str | None = None) -> str:
    L = ["=== comp-tool-health -- NFRA_TOOLHEALTH TH-B fused per-tool health (ADVISORY -- CTO ratifies) ===",
         h["phase"],
         f"corpus: {h['corpus_source']}   value metric: {h['value_metric']}"]
    rc = h["rail_enforcement"]
    if rc.get("available"):
        L.append(f"rail enforcement (fabric context, NOT a verdict input): routes={rc['routes']} "
                 f"escapes={rc['escapes']} denials={rc['denials']} route_share={rc['route_share']}")
        drop = rc["emitter_whitelist_drop"]["route_posterior_rows_dropped"]
        if drop:
            L.append(f"  [drift finding] emitter whitelist DROPS {drop} ROUTE-POSTERIOR* rows from the "
                     f"catalog+scorer (advisory -> COMPLEARN owner; TH-B reads routing.jsonl directly)")
    L.append(f"verdict counts: {h['verdict_counts']}   ('?' = pending EFFECTIVE / TH-A)")
    L.append("")
    hdr = f"{'VERDICT':<9} {'TOOL':<22} {'USED':>6} {'ROLES':>5} {'OUTCOME':>8} {'RAIL':<12} {'EFFECTIVE':<13} NOTE"
    L.append(hdr)
    L.append("-" * len(hdr))
    for r in h["tools"]:
        if verdict_filter and r["verdict"] != verdict_filter:
            continue
        v = r["verdict"] + ("?" if r["pending_effective"] else "")
        u = r["used"]
        mo = "n/a" if u["mean_outcome_value"] is None else f"{u['mean_outcome_value']:.2f}"
        note = r["reason"]
        if len(note) > 60:
            note = note[:57] + "..."
        L.append(f"{v:<9} {r['tool']:<22} {u['events']:>6} {u['distinct_roles']:>5} {mo:>8} "
                 f"{r['rail_consistent']['state']:<12} {str(r['effective']):<13} {note}")
    L.append("")
    L.append("ADVISORY ONLY -- no auto-mutation. FIX?/PROMOTE? are PENDING the EFFECTIVE probe (TH-A); "
             "KEEP is provisional (the probe could flip a rail-consistent KEEP to FIX). The CTO "
             "ratifies retire/fix/promote (PRD SS5.3).")
    return "\n".join(L)


def _render_tool(h: dict, tool: str) -> str:
    for r in h["tools"]:
        if r["tool"] == tool:
            return json.dumps(r, indent=2)
    return f"tool '{tool}' not found in the fused universe ({h['n_tools']} tools)."


# --------------------------------------------------------------------------------------------
# Value-anchored-honesty self-test (proves zero usage-Goodhart + the load-bearing EFFECTIVE flip).
# --------------------------------------------------------------------------------------------
def _self_test() -> tuple:
    checks = []

    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        return ok

    # (1) TAXONOMY encoded exactly (PRD SS3) -- the full 4-verdict table, effective as a real bool.
    ck("taxonomy.keep", classify_full(True, True, True)[0] == "KEEP")
    ck("taxonomy.fix", classify_full(True, True, False)[0] == "FIX")
    ck("taxonomy.promote", classify_full(False, None, True)[0] == "PROMOTE")
    ck("taxonomy.retire", classify_full(False, None, False)[0] == "RETIRE")

    # (2) LOAD-BEARING: for a USED + RAIL-consistent tool, EFFECTIVE is the SOLE KEEP<->FIX discriminator
    # (acceptance #2 -- FIX distinguishable from KEEP purely by the EFFECTIVE axis).
    keep = classify_full(True, True, True)[0]
    fix = classify_full(True, True, False)[0]
    ck("loadbearing.effective_alone_flips_keep_fix", keep == "KEEP" and fix == "FIX",
       f"same used+rail, effective yes->{keep} / no->{fix}")

    # (3) NO USAGE-GOODHART: a HEAVILY-used tool with LOW outcomes does NOT land a clean KEEP -- the
    # value gate demotes it (usage never protects a tool; mirrors comp_learns_score's Goodhart bite).
    rolling = ([{"tool": "comp-noisy", "role": "AE", "result": "FAIL", "ts_epoch": 100}] * 50
               + [{"tool": "comp-solid", "role": "AE", "result": "PASS", "ts_epoch": 100}] * 6)
    routing = [{"kind": "decision", "ranked": [{"id": "comp-noisy"}]}] * 5 + \
              [{"kind": "decision", "ranked": [{"id": "comp-solid"}]}] * 5
    um = build_used(rolling, [])
    rm = build_rail(routing)
    # noisy: 50 uses (heavy) but mean outcome 0.0 -> value gate fails -> FIX (usage never protects it).
    # solid: 6 uses but healthy outcome + chosen -> KEEP. Verdict tracks VALUE, not usage volume.
    noisy_vh = um["comp-noisy"]["mean_outcome_value"] >= HEALTHY_OUTCOME
    solid_vh = um["comp-solid"]["mean_outcome_value"] >= HEALTHY_OUTCOME
    noisy_verdict = decide(True, noisy_vh, rail_bool(rail_state(rm.get("comp-noisy"))), None)[0]
    solid_verdict = decide(True, solid_vh, rail_bool(rail_state(rm.get("comp-solid"))), None)[0]
    ck("goodhart.heavy_usage_low_value_not_keep",
       noisy_verdict != "KEEP" and solid_verdict == "KEEP",
       f"comp-noisy(50 uses,outcome0.0)->{noisy_verdict}  comp-solid(6 uses,outcome1.0)->{solid_verdict}")

    # (4) RETIRE is confidently emittable NOW (unused + no rail signal), independent of EFFECTIVE.
    v, pend, _ = classify_full(False, None, None)
    ck("skeleton.retire_confident_when_dead", v == "RETIRE", f"unused+no-signal -> {v} (pending={pend})")

    # (5) PROMOTE/FIX are correctly PENDING EFFECTIVE in the skeleton (used+rail-ok -> KEEP-provisional;
    # unused+rail-signal is handled at the query level -> RETIRE-partial pending). classify with eff=None:
    v_used, pend_used, _ = classify_full(True, True, None)
    ck("skeleton.used_railok_keep_provisional", v_used == "KEEP" and pend_used is True,
       f"used+rail-ok+eff-pending -> {v_used} pending={pend_used}")

    # (6) PREVENTIVE-gate temper: a used rail-consistent GATE with a FAILING effective probe is NOT
    # auto-FIX (its value is drift PREVENTED = unobservable) -- inherited comp_learns_score caveat.
    gate_v = classify_full(True, True, False, preventive=True)[0]
    plain_v = classify_full(True, True, False, preventive=False)[0]
    ck("preventive.gate_not_auto_fix", gate_v == "KEEP" and plain_v == "FIX",
       f"gate(eff=False)->{gate_v}  plain(eff=False)->{plain_v}")

    # (6b) VALUE-gate preventive temper: a USED preventive GATE with KNOWN-LOW outcome is NOT value-
    # FIXed by decide() (its low value-per-run is drift silently prevented), while a plain tool IS.
    gate_val = decide(True, False, True, None, preventive=True)[0]
    plain_val = decide(True, False, True, None, preventive=False)[0]
    ck("value_gate.preventive_gate_not_value_fixed", gate_val == "KEEP" and plain_val == "FIX",
       f"low-value gate->{gate_val}  low-value plain->{plain_val}")

    # (7) REUSE not fork: the shared outcome-weighting is comp_route's (one signal, two consumers).
    ck("reuse.shared_outcome_weighting", outcome_value({"result": "PASS"}) == 1.0
       and outcome_value({"result": "FAIL"}) == 0.0, "comp_route.outcome_value imported + consistent")

    # (8) Every verdict row exposes a VALUE anchor whose keys are outcome/quality, never a raw count
    # (structural anti-Goodhart -- acceptance #3), checked on the LIVE query.
    live = health()
    anchored = all(("mean_outcome_value" in r["value_anchor"] and "rail_quality" in r["value_anchor"])
                   for r in live["tools"])
    no_count_verdict = all("count" not in r["value_anchor"]["basis"].lower()
                           or "not" in r["value_anchor"]["basis"].lower() for r in live["tools"])
    ck("anchor.every_verdict_cites_value_not_count", anchored and no_count_verdict,
       f"{live['n_tools']} live tools, all cite an outcome/quality anchor")

    # (9) PHASE-B MACHINERY on REAL live tools (acceptance #2 demonstrated end-to-end, real feed pends
    # TH-A): take a live KEEP tool, feed EFFECTIVE=False via the same seam TH-A will use -> it flips to
    # a CONFIRMED FIX (not pending); feed EFFECTIVE=True -> it stays KEEP (final). USED + RAIL held
    # constant, so ONLY the EFFECTIVE axis moved the verdict. This proves the join wire works on the
    # live substrate today; TH-A just supplies the real probe values.
    # exclude preventive gates: their EFFECTIVE=False is TEMPERED (stays KEEP by design), so they are
    # the wrong probe for the plain KEEP->FIX flip (that temper is proven separately in check 6/6b).
    keep_tool = next((r["tool"] for r in live["tools"]
                      if r["verdict"] == "KEEP" and r["pending_effective"]
                      and not cls.is_preventive_tool(r["tool"])), None)
    if keep_tool:
        h_fix = health(effective_feed={keep_tool: False})
        h_keep = health(effective_feed={keep_tool: True})
        row_fix = next(r for r in h_fix["tools"] if r["tool"] == keep_tool)
        row_keep = next(r for r in h_keep["tools"] if r["tool"] == keep_tool)
        ck("phaseB.effective_feed_flips_live_keep_to_fix",
           row_fix["verdict"] == "FIX" and not row_fix["pending_effective"]
           and row_keep["verdict"] == "KEEP" and not row_keep["pending_effective"],
           f"{keep_tool}: eff=False -> {row_fix['verdict']}(final) / eff=True -> {row_keep['verdict']}(final)")
    else:
        ck("phaseB.effective_feed_flips_live_keep_to_fix", True, "no pending-KEEP live tool to exercise")

    ok = all(c["pass"] for c in checks)
    return ok, checks


def _goodhart_audit() -> dict:
    """Prove the health verdict is NOT a usage proxy, on the LIVE data: exhibit tools where the USAGE
    order and the VERDICT disagree (high-usage tools that are NOT KEEP, and low-usage tools that ARE)."""
    live = health()
    tools = live["tools"]
    by_use = sorted(tools, key=lambda r: -r["used"]["events"])
    high_use_not_keep = [{"tool": r["tool"], "events": r["used"]["events"], "verdict": r["verdict"],
                          "mean_outcome": r["used"]["mean_outcome_value"]}
                         for r in by_use[:15] if r["verdict"] != "KEEP"]
    low_use_keep = [{"tool": r["tool"], "events": r["used"]["events"], "verdict": r["verdict"]}
                    for r in tools if r["verdict"] == "KEEP" and r["used"]["events"] < 20]
    return {
        "is_usage_proxy": (not high_use_not_keep) and (not low_use_keep),
        "high_usage_NOT_keep": high_use_not_keep,
        "low_usage_IS_keep": low_use_keep[:8],
        "verdict": ("NOT a usage proxy -- the verdict tracks VALUE (outcome + rail quality), so "
                    "high-usage tools can be non-KEEP and low-usage tools can be KEEP"
                    if (high_use_not_keep or low_use_keep) else
                    "INCONCLUSIVE on this corpus (no divergence sample) -- inspect value_anchor per tool"),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="comp-tool-health -- NFRA_TOOLHEALTH TH-B fused per-tool health query")
    ap.add_argument("--verdict", choices=["KEEP", "FIX", "PROMOTE", "RETIRE"], help="filter to one verdict")
    ap.add_argument("--tool", help="one tool -- full 3-axis detail")
    ap.add_argument("--json", action="store_true", help="machine-readable")
    ap.add_argument("--goodhart-audit", action="store_true", help="prove the verdict is value-driven not usage-driven")
    ap.add_argument("--self-test", action="store_true", help="taxonomy + value-honesty + EFFECTIVE-flip self-test")
    ap.add_argument("--effective-feed", metavar="JSON",
                    help="TH-A EFFECTIVE probe stream (JSON {tool: bool}); present => full 4-verdict (Phase-B)")
    args = ap.parse_args()

    if args.self_test:
        ok, checks = _self_test()
        if args.json:
            print(json.dumps({"pass": ok, "checks": checks}, indent=2))
        else:
            print("=== comp-tool-health --self-test (taxonomy + value-anchored honesty) ===")
            for c in checks:
                print(f"  [{'PASS' if c['pass'] else 'FAIL'}] {c['check']}"
                      + (f"   ({c['detail']})" if c["detail"] else ""))
            print(f"\n{'OK: all checks pass' if ok else 'ERROR: one or more checks FAILED'}")
        return 0 if ok else 1

    if args.goodhart_audit:
        audit = _goodhart_audit()
        print(json.dumps(audit, indent=2) if args.json
              else "GOODHART AUDIT (is the health verdict a usage proxy?):\n"
                   + f"  high-usage NOT-KEEP: {[t['tool'] for t in audit['high_usage_NOT_keep']]}\n"
                   + f"  low-usage IS-KEEP:   {[t['tool'] for t in audit['low_usage_IS_keep']]}\n"
                   + f"  VERDICT: {audit['verdict']}")
        return 0

    feed = load_effective_feed(args.effective_feed) if args.effective_feed else None
    h = health(effective_feed=feed)
    if args.tool:
        print(_render_tool(h, _canonical_tool(args.tool) or args.tool))
    elif args.json:
        print(json.dumps(h, indent=2))
    else:
        print(_render(h, verdict_filter=args.verdict))
    return 0


if __name__ == "__main__":
    sys.exit(main())
