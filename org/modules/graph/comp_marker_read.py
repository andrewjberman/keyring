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
        return {"node_type_grains": {}, "ladder_levels": [], "drilldown": {}}
    # node_type_grain: grain -> [node_types]; invert to node_type -> {grains} (MANY-to-MANY).
    nt_grains: dict[str, set] = {}
    for grain, types in (gc.get("node_type_grain", {}) or {}).items():
        for t in (types or []):
            nt_grains.setdefault(t, set()).add(grain)
    ladder = ((gc.get("node_grain_ladder", {}) or {}).get("levels", []) or [])
    return {"node_type_grains": nt_grains, "ladder_levels": ladder,
            "drilldown": gc.get("drilldown_seams", {}) or {}}


_GC = _load_grain_contract()
# drilldown seam directions (~C clarification 1, sign-off): drill coarse->fine =
# RUNS/CONTAINS forward + OWNED_BY reverse; rollup = the opposite.
_DRILL_FORWARD = ("RUNS", "CONTAINS")
_DRILL_REVERSE = ("OWNED_BY",)


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
        self._tg: TraceGraph | None = None

    # -- GRAPHUNI re-point surface: the byte-compatible TraceGraph projection --
    def as_tracegraph(self) -> TraceGraph:
        """Id-canonicalized TraceGraph at the marker head. Each Node.metadata carries
        `grains` (SET) + `level` for GRAPHDEPTH depth-scoping (extra metadata keys do NOT
        change the lens logic, which reads id/node_type/label/file_path/function_name)."""
        if self._tg is not None:
            return self._tg
        g = TraceGraph(built_at=_as_epoch(self.provenance.get("built_at")))
        for rn in self._raw_nodes:
            nt = rn.get("node_type") or "UNKNOWN"
            props = rn.get("props") or {}
            cid = canon_id(rn.get("node_id") or rn.get("arn") or "", nt)
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
            s = canon_id(re.get("src") or "", "")
            t = canon_id(re.get("dst") or "", "")
            g.add_edge(Edge(source=s, target=t, edge_type=re.get("edge_type") or "UNKNOWN"))
        self._tg = g
        return g

    # -- GRAPHDEPTH P3 surface (~C-coordinated) --
    def nodes(self, *, scope_grain=None) -> list[Node]:
        """Grain-scoped node set. scope_grain (str | set | None) filters by MEMBERSHIP in
        each node's grains SET (~C refinement: many-to-many, not equality)."""
        g = self.as_tracegraph()
        if scope_grain is None:
            return list(g.nodes.values())
        want = {scope_grain} if isinstance(scope_grain, str) else set(scope_grain)
        return [n for n in g.nodes.values()
                if want & set(n.metadata.get("grains") or [])]

    def _adj(self, forward: bool):
        g = self.as_tracegraph()
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
        g = self.as_tracegraph()
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
    """Open the canonical marker-head Kuzu DB read-only (auto-refreshed on HEAD-advance,
    same oracle as comp-kuzu), read CloudNode/CloudEdge, and return the head-pinned handle
    with its provenance header resolved. Raises on a missing DB (a VISIBLE gap, never a
    silent stale read)."""
    import kuzu
    import _canonical
    import _provenance

    path = db_path or _canonical.CANONICAL_DB_PATH
    if _canonical.is_canonical(path):
        try:
            _canonical.ensure_fresh(path)   # marker-oracle auto-refresh (HEAD-advance)
        except Exception:  # noqa: BLE001 -- provenance header still records the vintage below
            pass
    if not os.path.exists(path):
        raise RuntimeError("marker-head Kuzu DB not found at %s (run kuzu_load.py)" % path)

    prov = {"marker_head": None, "nodes_snapshot_id": None, "status": "UNKNOWN-VINTAGE",
            "built_at": None, "header": None}
    try:
        man = _provenance.read_manifest(path) or {}
        if isinstance(man, dict):
            sv = man.get("source_vintage") or {}
            # the resolved graph_nodes snapshot IS the head pin the DB reads AT (D4 identity).
            # The Nessie commit hash lives in the S3 _branch_head marker, not the local manifest;
            # the snapshot-id is the durable pin identity, so marker_head = nodes_snapshot_id here.
            prov["nodes_snapshot_id"] = sv.get("nodes_snapshot_id")
            prov["marker_head"] = sv.get("nodes_snapshot_id")
            prov["built_at"] = man.get("built_at")
        hdr = _provenance.format_provenance_header(path) or ""
        prov["header"] = hdr
        low = hdr.lower()
        if "head: current" in low or "pin == marker" in low:
            prov["status"] = "current"
        elif "behind" in low:
            prov["status"] = "BEHIND"
        elif "unknown vintage" in low or "unknown-vintage" in low:
            prov["status"] = "UNKNOWN-VINTAGE"
    except Exception:  # noqa: BLE001 -- absent provenance => UNKNOWN-VINTAGE (surfaced, not silent)
        pass

    db = kuzu.Database(path, read_only=True)
    conn = kuzu.Connection(db)
    nodes = _fetch_nodes(conn)
    edges = _fetch_edges(conn)
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
