"""
NFRA_GRAPHUNI P2/D2 -- the ONE shared marker-headed graph read-API (PRD ruling 2).

(org/modules/graph/comp_marker_read.py.) The single read path every structure-tool
(comp-blast/trace/xref/platinum) calls, so no tool ever reads a private
divergent-vintage local cache (.comp-graph/graph.json) again --
the structural fix for the stale-cache phantom class (a deleted script folded from a
pre-reboot cache; the 1347-vs-1337 catch). ONE head-resolution + ONE provenance-header
site (ruling 2: NOT per-tool), which is also where the D4 one-head invariant lives.

WHAT IT DOES
  - Resolves the marker HEAD (reuses infra/aws/globgrph/_provenance + _canonical: the same
    _branch_head.main.json oracle + auto-refresh comp-kuzu uses) and surfaces the
    current/BEHIND/UNKNOWN-VINTAGE provenance header on EVERY call (D4).
  - Projects the unified Nessie/Kuzu graph (CloudNode/CloudEdge at the marker head) into a
    TraceGraph-shaped object (org.modules.graph.trace_graph), ID-CANONICALIZED into the
    TraceGraph namespace (gold:/s3:/lambda:/endpoint:) so the byte-for-byte lens logic of
    the re-pointed tools is unchanged and the P2 no-regression diff (vs CVO~B's frozen
    fixture) measures REAL coverage, not id cosmetics.
  - GRAPHDEPTH P3 depth-scoping composes on the SAME handle (~C-coordinated, sign-off
    20260701T050200Z): every node carries its node_type_grain `grains` SET (many-to-many)
    + its CONTAINS-ladder `level`; nodes(scope_grain=) is a membership filter; drill()/
    rollup() traverse the drilldown_seams; rollup() shares comp_coverage_check.rollup_defects()
    (ONE existential definition, 047ce51d0 -- never a parallel impl).

GOVERN BINDING (populate-govern-read): grain vocab is LOADED from ~C's grain_contract in
comp-coverage-map.yaml (node_type_grain + drilldown_seams + rollup), never hardcoded --
so this read-handle can't drift from the contract ~C governs + GRAPHUNI populates.

Author: 0.8.0_AE_CloudComp~D (NFRA_GRAPHUNI P2/D2). 2026-07-01. Signature ~C-signed-off
(4 governor conditions: grains-as-SET / drill-rollup-direction / level=None-for-resource /
rollup_defects-binding). Re-point targets: org/modules/graph/cli.py::_get_graph (blast/
trace/xref), platinum_cli.py. No-regression fixture: org/tier1_exec/3.0.0_SA_CVO/
NFRA_GRAPHUNI_P0-CVO_fixture/ (9d5765b82).
"""

from __future__ import annotations

import json
import os
import sys

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_WORKSPACE = os.path.abspath(os.path.join(_THIS_DIR, "..", "..", ".."))
_GLOBGRPH = os.path.join(_WORKSPACE, "infra", "aws", "globgrph")
_COVERAGE_MAP = os.path.join(_THIS_DIR, "comp-coverage-map.yaml")

# Reuse the globgrph Kuzu marker-head machinery (the SAME oracle comp-kuzu uses) + the
# grain-contract seam helper. Path-inserted, not duplicated (populate-govern-read).
for _p in (_GLOBGRPH, _THIS_DIR, _WORKSPACE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from org.modules.graph.trace_graph import Node, Edge, TraceGraph  # noqa: E402


def _as_epoch(v) -> float:
    """built_at may be an epoch (float/int) or an ISO-8601 string (the _build_manifest form).
    Returns a float epoch; 0.0 if unparseable (built_at is informational on the projection)."""
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str) and v.strip():
        import calendar
        import time
        try:
            return float(calendar.timegm(time.strptime(v[:19], "%Y-%m-%dT%H:%M:%S")))
        except Exception:  # noqa: BLE001
            return 0.0
    return 0.0


# ---- grain contract (LOADED from ~C's comp-coverage-map.yaml, never hardcoded) ----------

def _load_grain_contract() -> dict:
    """node_type -> set(grains) + the CONTAINS ladder + drilldown_seams, from the SSOT ~C
    governs. Fail-soft to an empty map (grain attribution then absent, surfaced -- never a
    wrong-but-silent grain)."""
    try:
        import yaml
        with open(_COVERAGE_MAP, "r", encoding="utf-8") as fh:
            gc = (yaml.safe_load(fh) or {}).get("grain_contract", {}) or {}
    except Exception:  # noqa: BLE001
        return {"node_type_grains": {}, "ladder_levels": [], "drilldown": [], "strata": []}
    # node_type_grain: grain -> [node_types]; invert to node_type -> {grains} (MANY-to-MANY).
    nt_grains: dict[str, set] = {}
    for grain, types in (gc.get("node_type_grain", {}) or {}).items():
        for t in (types or []):
            nt_grains.setdefault(t, set()).add(grain)
    ladder = ((gc.get("node_grain_ladder", {}) or {}).get("levels", []) or [])
    return {"node_type_grains": nt_grains, "ladder_levels": ladder,
            "drilldown": gc.get("drilldown_seams", []) or [],
            "strata": gc.get("strata", []) or []}


_GC = _load_grain_contract()


def _derive_drill_directions(drilldown, strata):
    """Derive the coarse->fine (drill FORWARD) vs fine->coarse (drill REVERSE) drilldown edge-type
    sets from grain_contract.drilldown_seams + the strata order (~C P3 sign-off refinement -- DERIVED
    from the contract, NOT hardcoded, so a future 4th stratum-stitcher propagates automatically). An
    edge is drill-FORWARD (coarse->fine) iff its from_stratum is COARSER (earlier in the strata order)
    than its to_stratum; else drill-REVERSE (drilling coarse->fine traverses it backward -- e.g.
    OWNED_BY object->resource). rollup() uses the opposite directions (fine->coarse)."""
    order = {s: i for i, s in enumerate(strata or [])}
    fwd, rev = [], []
    for seam in (drilldown or []):
        et = seam.get("edge_type")
        fi, ti = order.get(seam.get("from_stratum")), order.get(seam.get("to_stratum"))
        if not et or fi is None or ti is None:
            continue
        (fwd if fi < ti else rev).append(et)
    return tuple(dict.fromkeys(fwd)), tuple(dict.fromkeys(rev))


# DERIVED from grain_contract.drilldown_seams + strata (~C P3 sign-off refinement -- was hardcoded
# ('RUNS','CONTAINS')/('OWNED_BY',)). Fail-soft to that canonical 3-seam set if the contract is
# unreadable, so a YAML read failure is never a silent no-op traversal.
_DRILL_FORWARD, _DRILL_REVERSE = _derive_drill_directions(_GC["drilldown"], _GC["strata"])
if not _DRILL_FORWARD and not _DRILL_REVERSE:
    _DRILL_FORWARD, _DRILL_REVERSE = ("RUNS", "CONTAINS"), ("OWNED_BY",)

# The TRACE-GRAPH SCOPE (byte-match target for the re-point): the node namespaces + edge types
# the pre-delta .comp-graph/graph.json trace graph carried (grounded on CVO~B's frozen
# graph.json.pinned_predelta: node ns gold/s3/lambda/endpoint/eventbridge/component; edges
# CALLS/READS_S3/WRITES_S3/FETCHES/TRIGGERS -- NOTABLY NO CONTAINS). as_tracegraph() projects
# EXACTLY this scope so comp-blast/trace/xref reproduce their pre-delta answers set-equal; the
# marker-head's unification EXPANSION (CONTAINS containers + RUNS/OWNED_BY infra strata + the
# resource/portal/MS namespaces) stays available to GRAPHDEPTH via the FULL projection
# (nodes()/drill()/rollup()), never leaking into the re-pointed tools' default answers.
_TRACEGRAPH_NAMESPACES = frozenset(("gold", "s3", "lambda", "endpoint", "eventbridge", "component"))
_TRACEGRAPH_EDGE_TYPES = frozenset(("CALLS", "READS_S3", "WRITES_S3", "FETCHES", "TRIGGERS"))


def _namespace(canon: str) -> str:
    return canon.split(":", 1)[0] if ":" in canon else ""


def _script_of(canon: str):
    """The SCRIPT id of a canonical function id (gold:<script>:<fn> -> gold:<script>); None if
    not a function. Used for the scoped-projection script-grain s3 rollup."""
    if canon.startswith("gold:") and canon.count(":") >= 2:
        return canon.rsplit(":", 1)[0]
    return None


# ---- id canonicalization: Kuzu marker-head id -> TraceGraph namespace -------------------
# Grounded against the live CloudNode ids + CVO~B's frozen fixture answer ids (both sides
# confirmed 2026-07-01): pipeline:<firm>:gold:<rest> -> gold:<rest> ; opal-data-<firm>/<key>
# -> s3:<key> ; arn:...:function:<n> -> lambda:<n>. Grain rides THROUGH (ask #4a): a
# gold:<script>:<fn> still attributes function-grain, s3:<key> object-grain, via node_type.

def canon_id(node_id: str, node_type: str = "") -> str:
    nid = node_id or ""
    if nid.startswith("pipeline:"):
        # pipeline:<firm>:gold:<rest>  ->  gold:<rest>   (rest = <script>[:<fn>])
        parts = nid.split(":", 3)
        if len(parts) == 4 and parts[2] == "gold":
            return "gold:" + parts[3]
        return nid
    if nid.startswith("opal-data-"):
        # opal-data-<firm>/<key>  ->  s3:<key>
        slash = nid.find("/")
        return "s3:" + nid[slash + 1:] if slash != -1 else nid
    if nid.startswith("arn:aws:lambda:") and ":function:" in nid:
        return "lambda:" + nid.split(":function:", 1)[1]
    # already-canonical (gold:/s3:/lambda:/endpoint:/module:) or an as-yet-unmapped type
    # NOTE: s3-key glob-form (bare '*' vs '{*}') is NOT normalized here -- the frozen fixture
    # itself carries BOTH forms heterogeneously (per-key, from build_graph), so no single
    # normalization matches; the key-form + coverage divergence is the deferred re-point finding.
    return nid


def _grains_for(node_type: str) -> set:
    return set(_GC["node_type_grains"].get(node_type, set()))


_LADDER_LEVELS = set(_GC["ladder_levels"])


def _level_of(props: dict, node_type: str):
    """CONTAINS-ladder level from props.level if it is a real ladder token; None for pure
    resource-stratum nodes (~C clarification 2 -- they sit on the strata axis, not the ladder)."""
    lvl = (props or {}).get("level")
    return lvl if lvl in _LADDER_LEVELS else None


# ---- the shared handle -----------------------------------------------------------------

class MarkerHeadGraph:
    """A head-pinned read handle over the unified graph. Construct via load_marker_head_graph()."""

    def __init__(self, nodes: list[dict], edges: list[dict], provenance: dict):
        self.provenance = provenance          # {status, marker_head, nodes_snapshot_id, built_at}
        self._raw_nodes = nodes               # [{node_id, node_type, arn, props}]
        self._raw_edges = edges               # [{src, dst, edge_type}]
        self._tg: TraceGraph | None = None        # scoped (re-point) projection cache
        self._full_tg: TraceGraph | None = None   # full (GRAPHDEPTH) projection cache

    # -- projection (scoped=trace-graph re-point target; unscoped=full estate for GRAPHDEPTH) --
    def _project(self, scoped: bool) -> TraceGraph:
        g = TraceGraph(built_at=_as_epoch(self.provenance.get("built_at")))
        keep: set = set()
        for rn in self._raw_nodes:
            nt = rn.get("node_type") or "UNKNOWN"
            props = rn.get("props") or {}
            cid = canon_id(rn.get("node_id") or rn.get("arn") or "", nt)
            if scoped and _namespace(cid) not in _TRACEGRAPH_NAMESPACES:
                continue   # unification-expansion node (resource/portal/MS strata) -> GRAPHDEPTH only
            keep.add(cid)
            grains = _grains_for(nt)
            g.add_node(Node(
                id=cid, node_type=nt,
                label=props.get("name") or rn.get("node_id") or cid,
                file_path=props.get("path", "") or props.get("file_path", ""),
                function_name=props.get("function_name", ""),
                metadata={"grains": sorted(grains), "level": _level_of(props, nt),
                          "grain": (sorted(grains)[0] if grains else None),
                          "marker_head": self.provenance.get("marker_head")},
            ))
        for re in self._raw_edges:
            et = re.get("edge_type") or "UNKNOWN"
            if scoped and et not in _TRACEGRAPH_EDGE_TYPES:
                continue   # CONTAINS/RUNS/OWNED_BY are unification/depth edges -> not in the trace-graph scope
            s = canon_id(re.get("src") or "", "")
            t = canon_id(re.get("dst") or "", "")
            if scoped and (s not in keep or t not in keep):
                continue
            g.add_edge(Edge(source=s, target=t, edge_type=et))
            # SCRIPT-GRAIN s3 ROLLUP (scoped only): the pre-delta trace graph modeled READS/WRITES_S3
            # at SCRIPT grain (script<->s3, 445 edges) alongside some function-grain (131); the
            # compute producer is function-grain only. Roll each function<->s3 up to script<->s3
            # (existential: a script reads/writes s3 iff a contained function does -- the function id
            # encodes its script) so cross-script blast/trace reachability matches the frozen fixture.
            if scoped and et in ("READS_S3", "WRITES_S3"):
                s_scr, t_scr = _script_of(s), _script_of(t)
                if s_scr and s_scr in keep and s_scr != s:
                    g.add_edge(Edge(source=s_scr, target=t, edge_type=et))
                if t_scr and t_scr in keep and t_scr != t:
                    g.add_edge(Edge(source=s, target=t_scr, edge_type=et))
        return g

    # -- GRAPHUNI re-point surface: the byte-compatible (trace-graph-SCOPED) projection --
    def as_tracegraph(self) -> TraceGraph:
        """Trace-graph-SCOPED, id-canonicalized projection at the marker head -- the byte-match
        target for the re-pointed comp-blast/trace/xref (only the pre-delta trace-graph scope:
        namespaces gold/s3/lambda/endpoint/eventbridge/component + edges CALLS/READS_S3/WRITES_S3/
        FETCHES/TRIGGERS). Each Node.metadata carries `grains` SET + `level` (harmless extra keys;
        the lens reads id/node_type/label/file_path/function_name)."""
        if self._tg is None:
            self._tg = self._project(scoped=True)
        return self._tg

    def full(self) -> TraceGraph:
        """FULL unified projection (all strata, unscoped) -- for GRAPHDEPTH nodes/drill/rollup."""
        if self._full_tg is None:
            self._full_tg = self._project(scoped=False)
        return self._full_tg

    # -- GRAPHDEPTH P3 surface (~C-coordinated) --
    def nodes(self, *, scope_grain=None) -> list[Node]:
        """Grain-scoped node set. scope_grain (str | set | None) filters by MEMBERSHIP in
        each node's grains SET (~C refinement: many-to-many, not equality)."""
        g = self.full()
        if scope_grain is None:
            return list(g.nodes.values())
        want = {scope_grain} if isinstance(scope_grain, str) else set(scope_grain)
        return [n for n in g.nodes.values()
                if want & set(n.metadata.get("grains") or [])]

    def _adj(self, forward: bool):
        g = self.full()
        adj: dict[str, list[Edge]] = {}
        for e in g.edges:
            key = e.source if forward else e.target
            adj.setdefault(key, []).append(e)
        return adj

    def drill(self, node_id: str, to_grain: str) -> list[Node]:
        """Coarse->fine over the drilldown seams: RUNS/CONTAINS forward + OWNED_BY reverse
        (~C clarification 1). Returns to_grain-grained descendants."""
        return self._traverse(canon_id(node_id, ""), to_grain,
                              fwd_types=_DRILL_FORWARD, rev_types=_DRILL_REVERSE)

    def rollup(self, node_id: str, to_grain: str) -> list[Node]:
        """Fine->coarse EXISTENTIAL rollup (~C clarification 1 direction: RUNS/CONTAINS
        reverse + OWNED_BY forward). Existential semantics are shared with
        comp_coverage_check.rollup_defects() (BINDING, 047ce51d0 -- no parallel impl)."""
        return self._traverse(canon_id(node_id, ""), to_grain,
                              fwd_types=_DRILL_REVERSE, rev_types=_DRILL_FORWARD)

    def _traverse(self, start: str, to_grain: str, fwd_types, rev_types) -> list[Node]:
        g = self.full()
        fwd, rev = self._adj(True), self._adj(False)
        want, seen, out, stack = to_grain, set(), [], [start]
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            for e in fwd.get(cur, []):
                if e.edge_type in fwd_types:
                    stack.append(e.target)
            for e in rev.get(cur, []):
                if e.edge_type in rev_types:
                    stack.append(e.source)
            if cur != start:
                nd = g.nodes.get(cur)
                if nd and want in set(nd.metadata.get("grains") or []):
                    out.append(nd)
        return out

    def rollup_defects(self):
        """Delegate to the ONE canonical existential-rollup-defect check (~C BINDING): the
        read-handle and the grain gate share comp_coverage_check.rollup_defects()."""
        import comp_coverage_check
        return comp_coverage_check.rollup_defects


# ---- loader (reuses the comp-kuzu marker-head DB + provenance) --------------------------

def load_marker_head_graph(*, db_path: str | None = None) -> MarkerHeadGraph:
    """Read CloudNode/CloudEdge from the SERVED cloud graph and return the handle with its
    provenance resolved (TO-CG-D-7 / R7).

    WHAT THE "MARKER HEAD" MEANS NOW. It used to mean: a local DB, auto-refreshed when the marker
    oracle saw HEAD advance, whose manifest carried the `nodes_snapshot_id` it was built at. The
    refresh seam is gone and so is the local DB. The served projection is BUILT by the cloud engine
    at a pointer the service installs atomically, so the head pin is the SERVICE's `vintage` and the
    identity is its `manifest_sha256`. `status` is therefore always "current": a client cannot be
    handed a generation other than the installed one, so BEHIND has no state left to name. An
    UNREACHABLE service RAISES -- a VISIBLE gap, never a silent stale read, which is the property
    this function has always been written to protect.

    `db_path` is refused rather than ignored: a caller still holding a local path is asking for a
    surface that no longer exists, and answering from the served graph anyway would substitute one
    universe for another without saying so."""
    if db_path:
        raise RuntimeError(
            "local marker-head DB paths are RETIRED (NFRA_CLDGRPH R7): %r will not be opened. "
            "The marker-head graph is the SERVED projection." % db_path)
    import projection_client

    conn = projection_client.connect()
    nodes = _fetch_nodes(conn)
    edges = _fetch_edges(conn)
    prov = {
        "marker_head": conn.manifest_sha256,
        "nodes_snapshot_id": conn.manifest_sha256,
        "status": "current",
        "built_at": conn.vintage,
        "header": projection_client.vintage_line(conn,
                                                 {"nodes": len(nodes), "edges": len(edges)}),
    }
    return MarkerHeadGraph(nodes, edges, prov)


def _fetch_nodes(conn) -> list[dict]:
    out = []
    res = conn.execute("MATCH (n) RETURN n.node_id, n.node_type, n.arn, n.props")
    while res.has_next():
        row = res.get_next()
        out.append({"node_id": row[0], "node_type": row[1], "arn": row[2],
                    "props": _parse_props(row[3])})
    return out


def _fetch_edges(conn) -> list[dict]:
    out = []
    res = conn.execute("MATCH (a)-[e]->(b) RETURN a.node_id, b.node_id, e.edge_type")
    while res.has_next():
        row = res.get_next()
        out.append({"src": row[0], "dst": row[1], "edge_type": row[2]})
    return out


def _parse_props(raw) -> dict:
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str) and raw.strip():
        try:
            v = json.loads(raw)
            return v if isinstance(v, dict) else {}
        except Exception:  # noqa: BLE001
            return {}
    return {}
