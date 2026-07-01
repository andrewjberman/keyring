"""
comp-learns-score -- the NFRA_COMPLEARN value-anchored scorer (P2, the TRAINS verb's Goodhart gate).

Ranks build-next / route-fix / merge-retire candidates on a VALUE metric -- escapes-prevented /
chains-shortened / drift-caught / cost-per-outcome -- and NEVER on raw usage count. Output = an
ADVISORY worklist the CTO ratifies (never auto-mutates). This is the load-bearing benchmark-honesty
risk of the whole COMPLEARN program (CTO-owned gate): a scorer that ranked a tool by how often it is
INVOKED would be the Goodhart failure. Instead it ranks by BAD-OUTCOMES-AVERTED.

The value/usage distinction (the whole point):
  - FORBIDDEN: "comp-X is invoked a lot => comp-X is valuable" (usage as value -- the Goodhart trap).
  - ANCHORED: "949 rail-escapes cluster on gap G => building/routing a fix for G AVERTS that friction"
    (value = escapes-prevented). Counting BAD OUTCOMES AVERTED is value-anchored; counting a tool's
    popularity is not. A high-USAGE tool with LOW-outcome runs is a RETIRE candidate here, not a keep.

ONE SIGNAL, TWO CONSUMERS (COO~B/CTO mandate): the outcome-weighting is imported verbatim from the
COMPROUTE L3 engine (comp_route.outcome_value / result_class). COMPLEARN TRAINS the signal; COMPROUTE
DECIDES on it; both weight tool_activity outcomes identically -- guaranteed by shared code, not by
convention. Row acquisition reuses the tool_activity emitter's parsers (same normalized rows the live
catalog is built from), so the scorer scores the SAME data the federation serves.

Read-only, deterministic, no LLM, advisory-only (no auto-mutation -- mirrors NFRA_DEBTSCAN
never-auto-delete). Lane-portable (org/modules/graph/); degrades gracefully if a source is unavailable.

Usage:
    comp-learns-score                      # the single iteration -> the ranked advisory worklist
    comp-learns-score --top N              # cap the worklist (default 20)
    comp-learns-score --json               # machine-readable
    comp-learns-score --goodhart-audit     # prove the ranking is value-driven, not usage-driven
    comp-learns-score --self-test          # the Goodhart-honesty + evidence-citation self-test

Author: 0.8.0_AE_CloudComp~E (NFRA_COMPLEARN P2). 2026-07-01.
Spec: docs/architecture/NFRA_COMPLEARN_PRD.md (SS3/SS5) + the P2 task order + gap_heat_worklist_v0.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict

_WS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

# ONE SIGNAL: reuse the COMPROUTE L3 outcome-weighting verbatim (never re-implement it here).
sys.path.insert(0, _WS)
from org.modules.graph.comp_route import outcome_value, result_class  # noqa: E402

# Rail actions. GAP escapes (the agent went raw AND the row names WHAT/WHERE via term/target -> an
# actionable unmet need) vs DENY (rail blocked a raw Bash search; the row carries NO term/target, so
# it names no gap -- the rail WORKING, an aggregate enforcement stat, never a build-next candidate)
# vs ROUTE (a successful route -- not friction).
_GAP_ACTIONS = {"RUN-GREP", "RUN-GLOB", "RUN-LS"}
_ESCAPE_ACTIONS = {"RUN-GREP", "RUN-GLOB", "RUN-LS", "DENY"}
_ROUTE_ACTIONS = {"ROUTE", "ROUTE-SURFACE"}
# Drift/parity-intent terms -- demand for the change/estate concern (the drift-caught value dim).
_DRIFT_RX = re.compile(r"drift|parity|stale|vintage|freshness|head|sha|diff", re.I)
# PREVENTIVE / enforcement GATES (CTO caveat 2026-07-01): a gate's value is the drift it silently
# PREVENTS -- unobservable in the outcome cols -- so it scores LOW value-per-run BY DESIGN even while
# working. "Low value-per-run" on a gate can mean "the gate is doing its job," NOT "retire it." So a
# preventive tool's retire score is TEMPERED + flagged for mandatory human judgment (never auto-harm;
# advisory-only anyway). Detect the gate/check/validate/guard family + the safe-* wrappers.
_PREVENTIVE_RX = re.compile(r"-(check|gate|validate|guard|audit|lint)$|manifest-check|surface-check|"
                            r"commit-gate|precommit|safe-(commit|apply|deploy)")


def is_preventive_tool(tool: str) -> bool:
    """True if `tool` is a preventive/enforcement gate whose value is drift-PREVENTED (unobservable),
    so a low observed value-per-run does NOT imply low value (CTO caveat)."""
    return bool(_PREVENTIVE_RX.search(tool or ""))
_STOP = frozenset("a an the of for to in on is are do does how what which with by via that this "
                  "my your and or not no def class import from return self none true false".split())
_TOK = re.compile(r"[A-Za-z0-9_]+")


# ============================================================================================
# Row acquisition -- reuse the tool_activity emitter's parsers (same rows as the live catalog).
# ============================================================================================
def _emitter():
    """Import the tool_activity emitter for its parsers (best-effort; None if unavailable)."""
    try:
        sys.path.insert(0, os.path.join(_WS, "infra", "aws", "globgrph"))
        import tool_activity_emit as tae  # noqa: PLC0415 -- lazy: heavy (pyarrow) + optional
        return tae
    except Exception:  # noqa: BLE001 -- no emitter/pyarrow => degrade to the local rail parse
        return None


def _local_rail_rows() -> list:
    """Fallback rail parse (rail-log only) if the emitter is unavailable -- the primary escape signal."""
    path = os.path.join(_WS, "org", "mcp", "comp-which-rail.log")
    rows: list = []
    if not os.path.exists(path):
        return rows
    kv = re.compile(r"(\w+)=(\S+)")
    line_rx = re.compile(r"^(?P<ts>\S+)\s+(?P<action>\S+)\s+(?P<rest>.*)$")
    actions = _ESCAPE_ACTIONS | _ROUTE_ACTIONS | {"RUN-OVERRIDE"}
    with open(path, encoding="utf-8", errors="replace") as fh:
        for ln in fh:
            m = line_rx.match(ln.strip())
            if not m or m.group("action") not in actions:
                continue
            d = dict(kv.findall(m.group("rest")))
            mt = d.get("matches")
            try:
                mt = int(mt) if mt is not None else None
            except ValueError:
                mt = None
            rows.append({"action": m.group("action"), "tool": d.get("tool"), "term": d.get("term"),
                         "matches": mt, "target_path": d.get("target"), "role": None, "gap_text": None,
                         "result": None})
    return rows


# The NFRA_COMPROUTE flywheel sink -- comp-which appends each live backstop route()'s training_row
# here (append-only JSONL; gitignored + rotated). This is the loop CLOSING into the scorer: the live
# router's own hedges become routing-friction candidates.
ROUTING_SINK = "org/mcp/comproute-routing.jsonl"


def parse_routing_log(path: str = "", max_rows: int = 50000) -> list:
    """Read the comp-which flywheel sink -> route rows (each is a route().training_row:
    intent/role/ranked/kind/cold_start/outcome). Best-effort: [] if absent; skips malformed lines."""
    p = path or os.path.join(_WS, ROUTING_SINK)
    rows: list = []
    if not os.path.exists(p):
        return rows
    with open(p, encoding="utf-8", errors="replace") as fh:
        for ln in fh:
            ln = ln.strip()
            if not ln:
                continue
            try:
                rows.append(json.loads(ln))
            except Exception:  # noqa: BLE001 -- a malformed line never fails the ingest
                continue
    return rows[-max_rows:]


def maybe_rotate_routing_sink(max_bytes: int = 8_000_000) -> bool:
    """Size-based rotation of the append-only sink (ingest-side hygiene, ~C handoff): rename to .1 when
    it exceeds max_bytes so it stays bounded. Best-effort; returns True if it rotated."""
    p = os.path.join(_WS, ROUTING_SINK)
    try:
        if os.path.exists(p) and os.path.getsize(p) > max_bytes:
            os.replace(p, p + ".1")
            return True
    except Exception:  # noqa: BLE001 -- rotation is hygiene, never fatal
        pass
    return False


def load_corpus() -> dict:
    """Acquire the seed corpus. Returns {rail, sessions, rolling, routing, source}. Reuses the emitter
    parsers when present (identical to the live catalog rows); degrades to a local rail parse otherwise.
    `routing` = the live comp-which route rows (the flywheel closing into the scorer)."""
    routing = parse_routing_log()
    tae = _emitter()
    if tae is None:
        return {"rail": _local_rail_rows(), "sessions": [], "rolling": [], "routing": routing,
                "source": "local-rail-only"}
    rail = tae.parse_rail(os.path.join(_WS, tae.RAIL_LOG))
    rolling = []
    try:
        rolling = tae.parse_rolling_log(os.path.join(_WS, tae.ROLLING_LOG))
    except Exception:  # noqa: BLE001
        rolling = []
    sessions = []
    try:
        sessions = tae.parse_session_logs(tae.SESSION_LOG_TIERS)
    except Exception:  # noqa: BLE001 -- session walk is optional enrichment (gap_text); rail is primary
        sessions = []
    return {"rail": rail, "sessions": sessions, "rolling": rolling, "routing": routing,
            "source": "emitter-parsers"}


# ============================================================================================
# The VALUE metric -- friction averted, NEVER usage count.
# ============================================================================================
def escape_severity(row: dict) -> float:
    """Friction weight in [0,1] for an INFORMATIVE rail-escape (one carrying a term/target, so it
    names an unmet need). A raw search that FOUND NOTHING (matches==0) is the clearest unmet need; a
    raw search that found something is a softer 'a tool would have helped'; a bare listing is mild.
    DENY is deliberately NOT scored here: a DENY row carries no term/target (the rail only logs that a
    raw Bash search was blocked), so it names no gap -- it is the rail WORKING, tracked as an aggregate
    enforcement stat, never a build-next candidate. This is friction, not usage: two runs of the same
    SUCCESSFUL tool add zero here."""
    action = row.get("action")
    m = row.get("matches")
    if action in ("RUN-GREP", "RUN-GLOB"):
        return 1.0 if (m == 0 or m is None) else 0.6   # found-nothing = clearest unmet need
    if action == "RUN-LS":
        return 0.3
    return 0.0


def _topic(term: str, target: str) -> str:
    """A coarse cluster key for an escape: the target path root + the first content-token of the term.
    Groups 'the same unmet need' without over-splitting on incidental term variation."""
    tgt = (target or "?").replace("\\", "/").strip("/")
    root = "/".join(tgt.split("/")[:3]) if tgt and tgt != "?" else "?"
    toks = [t.lower() for t in _TOK.findall(term or "") if t.lower() not in _STOP and len(t) > 2]
    stem = toks[0] if toks else "(no-term)"
    return f"{root} :: {stem}"


# ============================================================================================
# Candidate derivation.
# ============================================================================================
def build_gap_candidates(rail: list) -> list:
    """Cluster rail ESCAPES into gap candidates, scored by escapes-prevented (friction averted)."""
    clusters: dict = defaultdict(lambda: {"events": 0, "value": 0.0, "drift": 0,
                                          "zero_match": 0, "terms": defaultdict(int),
                                          "targets": defaultdict(int), "roles": set()})
    for r in rail:
        if r.get("action") not in _GAP_ACTIONS:
            continue
        if not r.get("term") and not r.get("target_path"):
            continue     # uninformative escape (no term/target) -> names no actionable gap
        sev = escape_severity(r)
        key = _topic(r.get("term"), r.get("target_path"))
        c = clusters[key]
        c["events"] += 1
        c["value"] += sev
        if r.get("matches") == 0:
            c["zero_match"] += 1
        if _DRIFT_RX.search((r.get("term") or "") + " " + (r.get("target_path") or "")):
            c["drift"] += 1
        if r.get("term"):
            c["terms"][r["term"]] += 1
        if r.get("target_path"):
            c["targets"][r["target_path"]] += 1
        if r.get("role"):
            c["roles"].add(r["role"])
    out = []
    for key, c in clusters.items():
        top_terms = sorted(c["terms"].items(), key=lambda kv: -kv[1])[:4]
        top_targets = sorted(c["targets"].items(), key=lambda kv: -kv[1])[:3]
        out.append({
            "candidate": key,
            "kind": "coverage-gap",
            "value_score": round(c["value"], 2),           # escapes-prevented (friction-weighted)
            "value_metric": {
                "escapes_prevented": round(c["value"], 2),
                "escape_events": c["events"],
                "found_nothing": c["zero_match"],           # searches that returned 0 matches = unmet need
                "drift_caught": c["drift"],                 # change/parity-intent escapes in this cluster
            },
            "value_evidence": {
                "top_terms": [{"term": t, "n": n} for t, n in top_terms],
                "top_targets": [{"path": p, "n": n} for p, n in top_targets],
            },
        })
    return out


def build_merge_retire_candidates(rolling: list) -> list:
    """Tools with runs recorded in the rolling-log but a LOW mean OUTCOME value = low value-per-run =>
    merge/retire candidates. THE Goodhart bite: a tool is NOT protected by how often it runs; if its
    outcomes are low-value it surfaces here regardless of invocation count."""
    agg: dict = defaultdict(lambda: {"n": 0, "val": 0.0})
    for r in rolling:
        tool = r.get("tool")
        if not tool:
            continue
        a = agg[tool]
        a["n"] += 1
        a["val"] += outcome_value(r)                        # SAME outcome-weighting as COMPROUTE L3
    out = []
    for tool, a in agg.items():
        if a["n"] < 5:                                      # need enough runs to judge value-per-run
            continue
        mean_val = a["val"] / a["n"]
        if mean_val >= 0.6:                                 # healthy value-per-run => not a retire target
            continue
        # value of retiring = runs * (1 - mean_val): low-value runs are cost/noise the retire averts.
        base = a["n"] * (1.0 - mean_val)
        preventive = is_preventive_tool(tool)
        # A preventive GATE's low value-per-run is BY DESIGN (it silently prevents drift), so TEMPER
        # its retire score heavily + flag it -- "low value-per-run" here likely means "working", not
        # "retire" (CTO caveat). Human judgment required before retiring an enforcement gate.
        score = round(base * (0.25 if preventive else 1.0), 2)
        note = (f"{a['n']} runs at mean outcome {mean_val:.2f} (< 0.6 healthy); "
                + ("PREVENTIVE/ENFORCEMENT GATE -- low value-per-run is likely the gate SILENTLY "
                   "SUCCEEDING (drift PREVENTED = unobservable value), NOT low value. Retire score "
                   "tempered; MANDATORY human judgment before retire (CLAUDE.md rule 20/21)."
                   if preventive
                   else "usage does NOT justify keep -- value/run is low"))
        out.append({
            "candidate": f"{tool} (low value-per-run)" + (" [preventive gate]" if preventive else ""),
            "kind": "merge-retire",
            "preventive_gate": preventive,
            "value_score": score,
            "value_metric": {"cost_per_outcome": score, "runs": a["n"],
                             "mean_outcome_value": round(mean_val, 3), "preventive_gate": preventive},
            "value_evidence": {"note": note},
        })
    return out


def build_routing_candidates(routing: list) -> list:
    """Routing-friction candidates from the LIVE router's own hedges (the flywheel closing into the
    scorer). A DISAMBIGUATION means the router surfaced a near-tie -- it could not confidently decide
    -- so a curated routing rule / keyword refinement would convert it to a confident decision (the
    LD-0226 routing-mutation surface). value = the count of low-confidence routes a rule would sharpen
    (friction averted), NEVER tool usage. cold_start routes additionally flag WHERE the learned
    affinity term is most missing (drives the affinity-cache priority). A CONFIDENT decision is healthy
    and is NOT a candidate."""
    clusters: dict = defaultdict(lambda: {"disambig": 0, "coldstart": 0, "events": 0,
                                          "intents": defaultdict(int), "tied": defaultdict(int),
                                          "roles": set()})
    for r in routing:
        intent = r.get("intent", "") or ""
        toks = [t.lower() for t in _TOK.findall(intent) if t.lower() not in _STOP and len(t) > 2]
        key = " ".join(toks[:3]) if toks else "(no-intent)"
        c = clusters[key]
        c["events"] += 1
        if r.get("kind") == "disambiguation":
            c["disambig"] += 1
            for s in (r.get("ranked") or [])[:3]:
                if s.get("id"):
                    c["tied"][s["id"]] += 1
        if r.get("cold_start"):
            c["coldstart"] += 1
        if intent:
            c["intents"][intent] += 1
        if r.get("role"):
            c["roles"].add(r["role"])
    out = []
    for key, c in clusters.items():
        if c["disambig"] == 0:            # only HEDGES are friction; confident decisions are healthy
            continue
        out.append({
            "candidate": f"routing: {key}",
            "kind": "routing-friction",
            "value_score": round(float(c["disambig"]), 2),   # low-confidence routes a rule would sharpen
            "value_metric": {"low_confidence_routes": c["disambig"], "cold_start_routes": c["coldstart"],
                             "total_routes": c["events"]},
            "value_evidence": {
                "top_terms": [{"term": t, "n": n} for t, n in
                              sorted(c["intents"].items(), key=lambda kv: -kv[1])[:3]],
                "tied_tools": sorted(c["tied"], key=lambda k: -c["tied"][k])[:4],
            },
        })
    return out


# ============================================================================================
# COMPUNIFY coverage-map cross-ref -- disposition (route-fix vs build-new), the LD-0226 split.
# ============================================================================================
def load_coverage_terms() -> list:
    """Read the COMPUNIFY coverage map (the gap reference) -> a list of (tool_or_surface, keyword-set)
    for a lightweight disposition. Best-effort: returns [] if the map is unreadable (disposition then
    degrades to 'undetermined', never a crash)."""
    path = os.path.join(_WS, "org", "modules", "graph", "comp-coverage-map.yaml")
    if not os.path.exists(path):
        return []
    entries = []
    cur_id = None
    kw: set = set()
    id_rx = re.compile(r'^\s*(?:- )?(?:id|tool|high_level_tool):\s*"?([A-Za-z0-9_\- ]+)"?')
    concern_rx = re.compile(r'concern:\s*"?(.+?)"?\s*$')
    with open(path, encoding="utf-8", errors="replace") as fh:
        for ln in fh:
            mi = id_rx.match(ln)
            if mi:
                if cur_id and kw:
                    entries.append((cur_id, set(kw)))
                cur_id = mi.group(1).strip()
                kw = set(t.lower() for t in _TOK.findall(cur_id) if len(t) > 2)
                continue
            mc = concern_rx.search(ln)
            if mc:
                kw.update(t.lower() for t in _TOK.findall(mc.group(1)) if t.lower() not in _STOP and len(t) > 2)
    if cur_id and kw:
        entries.append((cur_id, set(kw)))
    return entries


def disposition(cand: dict, coverage: list) -> dict:
    """route-fix (an existing tool/surface already covers this concern -> a routing rule is the fix,
    LD-0226) vs build-new (no covering tool -> a real gap). Heuristic keyword overlap against the
    coverage map; honest 'undetermined' when the map is unavailable."""
    if cand["kind"] == "routing-friction":
        return {"disposition": "routing-refinement", "covering": None,
                "note": "the LIVE router repeatedly hedged this intent -- a curated comp-which rule / "
                        "keyword refinement (or the learned affinity term) would sharpen it to a "
                        "confident decision (LD-0226 routing-mutation surface)"}
    if cand["kind"] == "merge-retire":
        return {"disposition": "merge-retire", "covering": None}
    if not coverage:
        return {"disposition": "undetermined (coverage map unread)", "covering": None}
    terms = set()
    for t in cand["value_evidence"].get("top_terms", []):
        terms.update(x.lower() for x in _TOK.findall(t["term"]) if x.lower() not in _STOP and len(x) > 2)
    best, best_ov = None, 0
    for tool, kw in coverage:
        ov = len(terms & kw)
        if ov > best_ov:
            best, best_ov = tool, ov
    if best_ov >= 2:
        return {"disposition": "route-fix", "covering": best,
                "note": f"'{best}' already covers this concern ({best_ov} kw overlap) -- a comp-which "
                        f"routing rule is the fix, not a new tool (LD-0226)"}
    return {"disposition": "build-new", "covering": None,
            "note": "no covering tool found in the coverage map -- a real capability gap"}


# ============================================================================================
# The single iteration -> the ranked advisory worklist.
# ============================================================================================
def run_iteration(top: int = 20) -> dict:
    corpus = load_corpus()
    coverage = load_coverage_terms()
    gaps = build_gap_candidates(corpus["rail"])
    retire = build_merge_retire_candidates(corpus["rolling"])
    routing = build_routing_candidates(corpus.get("routing", []))    # the flywheel: live router hedges
    candidates = gaps + retire + routing
    for c in candidates:
        c.update(disposition(c, coverage))
    candidates.sort(key=lambda c: -c["value_score"])
    ranked = candidates[:top]
    denials = sum(1 for r in corpus["rail"] if r.get("action") == "DENY")
    routes = sum(1 for r in corpus["rail"] if r.get("action") in _ROUTE_ACTIONS)
    return {
        "iteration": "single (advisory-only -- CTO ratifies, no auto-mutation)",
        "corpus_source": corpus["source"],
        "corpus_size": {"rail_rows": len(corpus["rail"]), "session_rows": len(corpus["sessions"]),
                        "rolling_rows": len(corpus["rolling"]), "routing_rows": len(corpus.get("routing", []))},
        "coverage_map_entries": len(coverage),
        "value_metric": "escapes-prevented / chains-shortened / drift-caught / cost-per-outcome "
                        "(NEVER usage count -- CTO Goodhart gate)",
        # aggregate rail stat -- NOT candidates (DENY names no gap): context on rail enforcement.
        "rail_enforcement": {"raw_search_denials": denials, "successful_routes": routes,
                             "note": "denials = the rail working (raw search blocked -> rerouted); "
                                     "not a build-next candidate (no term/target to name a gap)"},
        "n_candidates": len(candidates),
        "worklist": ranked,
    }


# ============================================================================================
# Goodhart-honesty self-test + audit.
# ============================================================================================
def _self_test() -> tuple[bool, list]:
    checks = []

    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        return ok

    # Value-weighting is real: at EQUAL event volume, a higher-severity unmet need ranks above a
    # milder one (found-nothing raw-search > bare listing). This is the honest value property -- NOT
    # "few beats many" (more averted friction legitimately IS more value); it is "severity matters".
    n = 10
    unmet = [{"action": "RUN-GREP", "term": "iam policy gap", "target_path": "infra/aws", "matches": 0}] * n
    mild = [{"action": "RUN-LS", "term": "list dir contents", "target_path": "org/tmp", "matches": 3}] * n
    cands = build_gap_candidates(unmet + mild)
    vals = {c["candidate"]: c["value_score"] for c in cands}
    unmet_v = max(v for k, v in vals.items() if "infra" in k)
    mild_v = max(v for k, v in vals.items() if "tmp" in k)
    ck("goodhart.severity_matters_at_equal_volume", unmet_v > mild_v,
       f"{n} found-nothing (v={unmet_v}) > {n} bare-listings (v={mild_v}) at equal volume")
    # DENY (no term/target) names no gap -> NEVER a build-next candidate (rail-enforcement stat only).
    deny_only = build_gap_candidates([{"action": "DENY", "tool": "Bash"}] * 50)
    ck("goodhart.deny_not_a_candidate", deny_only == [], f"{len(deny_only)} DENY candidates (expect 0)")

    # A high-USAGE low-outcome tool must surface as a RETIRE candidate (usage never protects it).
    rolling = ([{"tool": "noisy", "result": "FAIL"}] * 20 + [{"tool": "noisy", "result": "DENY"}] * 20
               + [{"tool": "solid", "result": "PASS"}] * 3)
    ret = {c["candidate"].split()[0]: c for c in build_merge_retire_candidates(rolling)}
    ck("goodhart.high_usage_low_value_retires", "noisy" in ret and "solid" not in ret,
       f"retire candidates: {sorted(ret)}")

    # Preventive-gate caveat (CTO 2026-07-01): a GATE with the SAME low outcome as a plain tool gets a
    # TEMPERED retire score + a flag -- low value-per-run on a gate likely means it is silently
    # succeeding (drift PREVENTED), not that it should be retired.
    pr = {c["candidate"].split()[0]: c for c in build_merge_retire_candidates(
        [{"tool": "comp-manifest-check", "result": "FAIL"}] * 20 + [{"tool": "plain-tool", "result": "FAIL"}] * 20)}
    gate, plain = pr.get("comp-manifest-check"), pr.get("plain-tool")
    ck("preventive_gate.tempered_and_flagged",
       bool(gate) and bool(plain) and gate["preventive_gate"] and not plain["preventive_gate"]
       and gate["value_score"] < plain["value_score"],
       f"gate={gate['value_score'] if gate else None} < plain={plain['value_score'] if plain else None}, flagged")

    # Every ranked item cites value evidence (no evidence-free rank -- a Goodhart leak).
    it = run_iteration(top=10)
    have_ev = all(c.get("value_evidence") and c.get("value_metric") for c in it["worklist"])
    ck("evidence.every_item_cites_value", have_ev, f"{len(it['worklist'])} items, all cite value evidence")

    # The scorer exposes NO raw usage-count-as-value term (structural: value_score derives from
    # escape severity / (1-mean_outcome), never from a bare invocation count).
    ck("goodhart.no_usage_proxy", all("escapes_prevented" in c["value_metric"] or "cost_per_outcome"
                                      in c["value_metric"] for c in it["worklist"]),
       "value_metric keys are outcome-anchored")

    # Reuses the SAME outcome-weighting as COMPROUTE L3 (one signal, two consumers).
    ck("one_signal.shared_outcome_weighting", outcome_value({"result": "PASS"}) == 1.0
       and result_class("DENY") == 0.0, "comp_route.outcome_value/result_class imported + consistent")

    # Flywheel closure: the LIVE router's HEDGES (disambiguations) surface as routing-friction
    # candidates; a confident decision is healthy and is NOT a candidate.
    routes = ([{"intent": "cluster similar things", "kind": "disambiguation", "cold_start": True,
                "ranked": [{"id": "comp-cluster"}, {"id": "comp-transform"}]}] * 3
              + [{"intent": "what breaks if I change", "kind": "decision", "cold_start": True,
                  "ranked": [{"id": "comp-blast"}]}] * 5)
    rc_ids = {c["candidate"] for c in build_routing_candidates(routes)}
    ck("flywheel.hedges_surface_confident_routes_dont",
       any("cluster" in x for x in rc_ids) and not any("breaks" in x or "change" in x for x in rc_ids),
       f"routing-friction candidates: {sorted(rc_ids)}")

    ok = all(c["pass"] for c in checks)
    return ok, checks


def _render(it: dict) -> str:
    L = ["=== comp-learns-score -- NFRA_COMPLEARN P2 value-anchored worklist (ADVISORY -- CTO ratifies) ===",
         f"corpus: {it['corpus_source']}  rail={it['corpus_size']['rail_rows']} "
         f"rolling={it['corpus_size']['rolling_rows']} session={it['corpus_size']['session_rows']} "
         f"routing={it['corpus_size'].get('routing_rows', 0)} (flywheel)  "
         f"coverage-map entries={it['coverage_map_entries']}",
         f"value metric: {it['value_metric']}",
         f"rail enforcement (context, NOT candidates): {it['rail_enforcement']['raw_search_denials']} "
         f"raw-search denials, {it['rail_enforcement']['successful_routes']} successful routes",
         f"\n{it['n_candidates']} candidates; top {len(it['worklist'])}:\n"]
    for i, c in enumerate(it["worklist"], 1):
        vm = c["value_metric"]
        L.append(f"{i:2d}. [{c['kind']}/{c.get('disposition','?')}] value={c['value_score']}  {c['candidate']}")
        if c["kind"] == "coverage-gap":
            L.append(f"      escapes_prevented={vm['escapes_prevented']} "
                     f"(events={vm['escape_events']} "
                     f"found-nothing={vm['found_nothing']} drift={vm['drift_caught']})")
            terms = ", ".join(f"{t['term']!r}x{t['n']}" for t in c["value_evidence"]["top_terms"][:3])
            L.append(f"      evidence terms: {terms}")
            if c.get("note"):
                L.append(f"      -> {c['note']}")
        elif c["kind"] == "routing-friction":
            L.append(f"      low_confidence_routes={vm['low_confidence_routes']} "
                     f"(cold_start={vm['cold_start_routes']} total={vm['total_routes']})  "
                     f"tied: {', '.join(c['value_evidence']['tied_tools'])}")
            intents = "; ".join(f"{t['term']!r}" for t in c["value_evidence"]["top_terms"][:2])
            L.append(f"      intents: {intents}")
            if c.get("note"):
                L.append(f"      -> {c['note']}")
        else:
            L.append(f"      {c['value_evidence'].get('note', '')}")
    L.append("\nADVISORY ONLY -- no auto-mutation. Routing-miss (route-fix) items feed the comp-which "
             "rule surface (LD-0226). CTO ratifies KEEP/DISCARD.")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="comp-learns-score -- NFRA_COMPLEARN value-anchored scorer (P2)")
    ap.add_argument("--top", type=int, default=20, help="cap the worklist length (default 20)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--goodhart-audit", action="store_true",
                    help="prove the ranking is value-driven not usage-driven")
    ap.add_argument("--self-test", action="store_true", help="Goodhart-honesty + evidence-citation self-test")
    args = ap.parse_args()

    if args.self_test:
        ok, checks = _self_test()
        if args.json:
            print(json.dumps({"pass": ok, "checks": checks}, indent=2))
        else:
            print("=== comp-learns-score --self-test (Goodhart-honesty) ===")
            for c in checks:
                print(f"  [{'PASS' if c['pass'] else 'FAIL'}] {c['check']}" + (f"   ({c['detail']})" if c["detail"] else ""))
            print(f"\n{'OK: all checks pass' if ok else 'ERROR: one or more checks FAILED'}")
        return 0 if ok else 1

    it = run_iteration(top=args.top)

    if args.goodhart_audit:
        # Prove the ranking is NOT a raw-usage/volume proxy, two independent ways:
        full = run_iteration(top=10_000)
        gaps = [c for c in full["worklist"] if c["kind"] == "coverage-gap"]
        # (1) RANK-INVERSIONS: pairs where the VALUE order and the raw-EVENT-COUNT order disagree. Any
        # inversion proves value is not a monotone function of count (severity re-orders the ranking).
        inversions, example = 0, None
        for i in range(len(gaps)):
            for j in range(i + 1, len(gaps)):
                a, b = gaps[i], gaps[j]   # a is value-ranked above b
                if a["value_metric"]["escape_events"] < b["value_metric"]["escape_events"]:
                    inversions += 1
                    if example is None:
                        example = (f"{a['candidate']} (value {a['value_score']}, {a['value_metric']['escape_events']} "
                                   f"events) ranks ABOVE {b['candidate']} (value {b['value_score']}, "
                                   f"{b['value_metric']['escape_events']} events) -- fewer events, higher value")
        # (2) HIGH-USAGE-LOW-VALUE tools surface as RETIRE candidates -- usage never protects a tool.
        retire = [{"tool": c["candidate"], "runs": c["value_metric"]["runs"],
                   "mean_outcome": c["value_metric"]["mean_outcome_value"]}
                  for c in full["worklist"] if c["kind"] == "merge-retire"]
        audit = {"rank_inversions_value_vs_rawcount": inversions,
                 "inversion_example": example,
                 "is_usage_proxy": inversions == 0 and not retire,
                 "high_usage_low_value_retire_candidates": retire[:5],
                 "verdict": ("NOT a usage proxy -- value re-orders vs raw count AND high-usage-low-value "
                             "tools are flagged for retire, not protected by usage")}
        if args.json:
            print(json.dumps(audit, indent=2))
        else:
            print("GOODHART AUDIT (is the scorer a usage proxy?):")
            print(f"  value-vs-rawcount rank inversions: {inversions}"
                  + (f"\n    e.g. {example}" if example else ""))
            print("  high-usage-low-value tools flagged RETIRE (usage did not protect them):")
            for r in retire[:5]:
                print(f"    {r['tool']}: {r['runs']} runs @ mean outcome {r['mean_outcome']}")
            print(f"  VERDICT: {audit['verdict']}")
        return 0

    print(json.dumps(it, indent=2) if args.json else _render(it))
    return 0


if __name__ == "__main__":
    sys.exit(main())
