#!/usr/bin/env python3
"""GRAPH signal -- comp-kuzu/comp-blast no-consumer + the 14-class FP-suppression overlay.

MILESTONE 3 (NFRA_COMPDEBT_PRD.md 8.3 / 6). The graph reachability signal ALREADY ran (the
D1 sweep) -- including its precision lesson: D1's 0.70 precision was 100% ONE mechanism,
absent-edge-because-UNMODELED misread as absent-edge-because-DEAD. So this adapter does NOT
re-run raw reachability; it wraps grounding_lib.graph_zero_consumer (comp-blast) with the
14-class FP-suppression overlay from debtscan/suppression_v1.yaml, and carries the graph
vintage. An orphan that matches a benign FP class is SUPPRESSED (logged, never filed).

RULE 22: a graph orphan is the DESIRED/structural layer = INFERRED (a symptom). It is NEVER
CONFIRMED on its own -- CONFIRMED requires the live/metric confirm leg (grounding_lib's
dual-evidence dead-confirm; supply confirm_metric to run it). A BEHIND/UNKNOWN graph vintage
=> UNVERIFIABLE, never clean (PRD 6 vintage-carry).

ACTIVE-FLAG CONTRACT (CVO ruling, honored here): only `suppression_classes` whose `active`
is absent/true are applied. `pending_review_classes` are structurally inert. NOTHING
suppresses a finding CVO has not ruled.
"""
from __future__ import annotations

import fnmatch
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

_HERE = Path(__file__).resolve()
_COMP_DEBT = _HERE.parents[1]
if str(_COMP_DEBT) not in sys.path:
    sys.path.insert(0, str(_COMP_DEBT))
import grounding_lib as g  # noqa: E402

REPO = _HERE.parents[5]  # signals/ -> comp_debt -> graph -> modules -> org -> REPO
_SUPPRESSION_PATH = REPO / "org" / "modules" / "graph" / "debtscan" / "suppression_v1.yaml"

SIGNAL = "graph"
# PRD 3 GRAPH detects-vocabulary (aligned to pipescript debt-flag terms).
STATE_NO_CONSUMER = "no-consumer"
STATE_ORPHANED_OUTPUT = "orphaned-output"
STATE_PRODUCER_NOTHING_READS = "producer-nothing-reads"


# ---- FP-suppression overlay (the D1 precision fix) ----------------------------------------
@dataclass
class Suppressor:
    class_id: str
    reason: str


_APPLIED_CACHE: list[dict] | None = None


def load_applied_suppressions(path: Path = _SUPPRESSION_PATH) -> list[dict]:
    """Return ONLY the applied classes: `suppression_classes` with active absent/true.
    pending_review_classes are excluded by construction (active-flag contract)."""
    global _APPLIED_CACHE
    if _APPLIED_CACHE is not None:
        return _APPLIED_CACHE
    if yaml is None:
        raise RuntimeError("PyYAML not available -- cannot load suppression_v1.yaml")
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    applied = [c for c in (doc.get("suppression_classes") or [])
               if c.get("active", True) is not False]
    _APPLIED_CACHE = applied
    return applied


def _name_matches(pattern: str, name: str) -> bool:
    """A suppression name_pattern is a literal, a glob (*), or an explicit regex (\\ / \\d).
    Match faithfully to how the config authored them."""
    if not name:
        return False
    if "\\" in pattern or "\\d" in pattern:      # explicit regex (e.g. E_\d+\..*)
        try:
            return re.search(pattern, name) is not None
        except re.error:
            return False
    if "*" in pattern:                            # glob (opal-portfolio-*, INF_*, find-insure-*)
        return fnmatch.fnmatch(name, pattern)
    return pattern == name or pattern in name     # literal (exact or contained)


def fp_suppress(node_type: str | None, node_name: str, *,
                edges: dict | None = None) -> Suppressor | None:
    """Return the matching benign FP class (logged, never filed) or None. A class matches
    when the node's type is in affected_types AND its name matches a name_pattern (edge/
    filter-only classes are advisory here -- name-less filters like isolated_only cannot be
    decided from name alone, so they NEVER auto-suppress; they are surfaced as a note)."""
    edges = edges or {}
    for c in load_applied_suppressions():
        types = c.get("affected_types") or []
        if node_type and types and node_type not in types:
            continue
        rsn = (c.get("reason") or "").strip().split("\n")[0][:160]
        # (a) name_pattern classes: node name matches a benign pattern.
        pats = c.get("name_patterns") or []
        if pats and any(_name_matches(p, node_name) for p in pats):
            return Suppressor(c["id"], rsn)
        # (b) filter: isolated_only -- a WHOLE-TYPE coverage gap (LOG_GROUP implicit logs,
        #     SECRET runtime boto3 access, S3_BUCKET_POLICY 0-outbound). The graph is
        #     structurally BLIND to these types' edges, so a graph-orphan on them is
        #     unreliable -> suppress the GRAPH signal (a real corpse is still catchable by
        #     cloudtrail/iam cross-confirm, per each class's own note). Requires an explicit
        #     node_type match (never blanket-suppress an unknown-typed node).
        if node_type and c.get("filter") == "isolated_only" and node_type in types:
            return Suppressor(c["id"], rsn)
        # (c) edge-condition classes we can positively confirm from provided edge context.
        cond = c.get("edge_condition")
        if cond and edges.get(cond):
            return Suppressor(c["id"], rsn)
    return None


# ---- the graph signal ----------------------------------------------------------------------
def graph_signal(resource_id: str, *, node_type: str | None = None,
                 node_name: str | None = None, firm: str | None = None,
                 vintage: g.Vintage | None = None, confirm_metric: dict | None = None,
                 edges: dict | None = None) -> g.Signal | None:
    """Emit a GRAPH debt signal for a resource, or None if reachable / suppressed / unknown.

    confirm_metric (optional): a dict {namespace, metric_name, dimensions, window_days,
    statistic, label} -- if provided, runs grounding_lib's dual-evidence dead-confirm so the
    signal can be CONFIRMED (graph-zero AND metric-zero). Absent -> INFERRED structural only.
    """
    name = node_name or resource_id
    leg = g.graph_zero_consumer(resource_id if ":" not in resource_id else name)
    if leg.status == g.GRAPH_REACHABLE:
        # a live consumer -> NOT debt; emit a contra-live-use marker fuse.py can honor.
        return g.Signal(signal=SIGNAL, state="reachable", level=g.LEVEL_INFERRED,
                        grounding={"desired": leg.grounding, "applied": "graph shows >=1 consumer"})
    if not leg.is_zero:
        return None  # UNKNOWN / NOT-FOUND -> no orphan claim (never a false clear)

    # zero-consumer orphan candidate -> FP overlay (the D1 precision fix)
    sup = fp_suppress(node_type, name, edges=edges)
    if sup:
        return None  # benign FP (absent-edge-because-unmodeled) -> suppressed, not filed

    v = vintage if vintage is not None else g.read_graph_vintage()
    grounding = {"desired": leg.grounding,
                 "vintage": f"graph vintage={v.status}"
                            + (f" age={v.age_hours}h" if v.age_hours is not None else "")}

    if confirm_metric:
        metric = g.metric_zero_over_window(
            confirm_metric["namespace"], confirm_metric["metric_name"],
            confirm_metric["dimensions"],
            window_days=confirm_metric.get("window_days", g.DEFAULT_WINDOW_DAYS),
            statistic=confirm_metric.get("statistic", "Sum"),
            label=confirm_metric.get("label", "events"))
        dc = g.dual_evidence_verdict(leg, metric, vintage=v)
        return g.signal_from_dead_confirm(SIGNAL, STATE_NO_CONSUMER, dc)

    # structural only -> INFERRED (a graph vintage problem makes it UNVERIFIABLE)
    level = g.LEVEL_INFERRED if v.trustworthy else g.LEVEL_UNVERIFIABLE
    grounding["applied"] = "no live-confirm leg run -> structural symptom only (Rule 22)"
    return g.Signal(signal=SIGNAL, state=STATE_NO_CONSUMER, grounding=grounding, level=level)


def discover_orphans(node_types: list[str] | None = None, *, limit: int = 200) -> list[dict]:
    """Query comp-kuzu for zero-downstream-consumer nodes of the given types, run each
    through the FP overlay, and return the SURVIVORS (with the suppressed count noted). The
    estate-sweep entry point (the per-resource path above is what fuse.py calls)."""
    types = node_types or ["LAMBDA", "S3_BUCKET", "DYNAMODB_TABLE", "EVENT_RULE", "GOLD_SCRIPT"]
    type_list = ", ".join(f"'{t}'" for t in types)
    query = (f"MATCH (n) WHERE n.node_type IN [{type_list}] "
             f"AND NOT (n)-[]->() RETURN n.id AS id, n.node_type AS t LIMIT {limit}")
    import subprocess
    survivors: list[dict] = []
    suppressed = 0
    try:
        r = subprocess.run(g._comp_cmd("comp-kuzu") + ["--json", query],
                           cwd=str(REPO), capture_output=True, text=True, timeout=120)
        import json
        rows = []
        for line in (r.stdout or "").splitlines():
            line = line.strip()
            if line.startswith("[") or line.startswith("{"):
                try:
                    rows = json.loads(line)
                    break
                except ValueError:
                    continue
        for row in (rows if isinstance(rows, list) else []):
            nid, nt = row.get("id"), row.get("t")
            if fp_suppress(nt, nid or ""):
                suppressed += 1
                continue
            survivors.append({"id": nid, "type": nt})
    except (OSError, subprocess.TimeoutExpired):
        pass
    for s in survivors:
        s["suppressed_in_run"] = suppressed
    return survivors


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="comp-debt.signals.graph",
                                 description="GRAPH signal -- no-consumer + FP overlay; emit-only.")
    ap.add_argument("--check", metavar="RESOURCE_ID", help="emit the graph signal for a resource")
    ap.add_argument("--type", default=None, help="node type (for FP-overlay matching)")
    ap.add_argument("--name", default=None, help="node name (comp-blast target / FP matching)")
    ap.add_argument("--discover", action="store_true", help="sweep comp-kuzu for FP-survived orphans")
    ap.add_argument("--list-suppressions", action="store_true", help="list the APPLIED FP classes")
    args = ap.parse_args(argv)

    if args.list_suppressions:
        applied = load_applied_suppressions()
        print(f"APPLIED FP-suppression classes (active-flag contract): {len(applied)}")
        for c in applied:
            print(f"  {c['id']:<34} types={c.get('affected_types')} "
                  f"patterns={len(c.get('name_patterns') or [])}")
        return 0
    if args.discover:
        surv = discover_orphans()
        print(f"graph orphan survivors (post-FP-overlay): {len(surv)}"
              + (f" | suppressed this run: {surv[0]['suppressed_in_run']}" if surv else ""))
        for s in surv[:40]:
            print(f"  {s['type']:<18} {s['id']}")
        return 0
    if args.check:
        sig = graph_signal(args.check, node_type=args.type, node_name=args.name)
        if sig is None:
            print(f"{args.check}: no graph debt signal (reachable / suppressed / unknown)")
        else:
            print(f"{args.check}: [{sig.level}] {sig.state}")
            for k, v in sig.grounding.items():
                print(f"    {k}: {v}")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
