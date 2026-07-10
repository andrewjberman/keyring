"""
Full-stack trace graph — unified node/edge model for cross-layer tracing.

Nodes represent components, endpoints, Lambdas, S3 artifacts, gold scripts,
EventBridge rules, and CloudFront behaviors. Edges represent data flow
relationships (imports, fetches, S3 reads/writes, triggers, routes).

Two CLI tools walk this graph:
  opal-trace: bidirectional walk from a starting node
  opal-blast: downstream-only traversal (blast radius)

Zero API calls. Pure static analysis.
"""

from __future__ import annotations

import json
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Node + Edge types
# ---------------------------------------------------------------------------

NODE_TYPES = {
    "COMPONENT",      # React component (.tsx/.jsx)
    "ENDPOINT",       # API function (fetch wrapper)
    "LAMBDA",         # Lambda handler
    "S3_ARTIFACT",    # S3 key/path
    "GOLD_SCRIPT",    # EC2 gold script (optionally :function_name)
    "EVENTBRIDGE",    # CloudWatch/EventBridge rule
    "CLOUDFRONT",     # CloudFront behavior pattern
}

EDGE_TYPES = {
    "IMPORTS",        # file-to-file import
    "FETCHES",        # component -> endpoint URL
    "READS_S3",       # Lambda/script reads from S3 path
    "WRITES_S3",      # script writes to S3 path
    "CALLS",          # caller function -> callee function
    "CALLED_BY",      # callee function -> caller function (blast-radius walk)
    "TRIGGERS",       # EventBridge -> Lambda
    "ROUTES",         # CloudFront -> origin
}


@dataclass
class Node:
    id: str                          # unique key (usually file path or S3 key)
    node_type: str                   # one of NODE_TYPES
    label: str                       # human-readable name
    file_path: str = ""              # source file (if applicable)
    function_name: str = ""          # specific function within file
    run_order: int = -1              # execution order for GOLD_SCRIPT
    metadata: dict = field(default_factory=dict)
    source_sha: str = ""             # SHA-256 of source file at index time (ADHC_COMPIL_V4.012)


def _compute_file_sha(path: Path) -> str:
    """Return short (12-char) SHA-256 hex of file contents; empty string on miss."""
    try:
        import hashlib
        h = hashlib.sha256()
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(65536), b''):
                h.update(chunk)
        return h.hexdigest()[:12]
    except (OSError, FileNotFoundError):
        return ""


# Source extensions worth hashing for drift when a node's file_path is a DIRECTORY
# (a Lambda bundle root). Skip vendored/cache trees so the aggregate is stable and cheap.
_DIR_SHA_EXTS = {".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".json",
                 ".yaml", ".yml", ".toml", ".sh", ".txt", ".cfg", ".ini", ".sql", ".html"}
_DIR_SHA_SKIP = {"__pycache__", ".git", "node_modules", ".terraform",
                 ".venv", "venv", "dist", "build", ".mypy_cache", ".pytest_cache"}
_DIR_SHA_MAX_FILES = 5000   # pathological-tree guard -> '' (a bounded, honest miss)


def _compute_dir_sha(path: Path) -> str:
    """Deterministic 12-char aggregate SHA over a directory's source files.

    Hash = sha256 over sorted (posix-relpath, per-file-sha) pairs, so editing ANY
    tracked source file under `path` (a Lambda's bundle dir) changes the aggregate ->
    the node drifts. Bounded to source extensions; skips vendored/cache dirs. Returns
    '' on empty/miss/overflow (NFRA_TOOLPASS B5/B6 fix, 3.0.0_SA_CVO~B): a Lambda node
    whose file_path is its source DIRECTORY was silently unfreshenable because
    `is_file()` was False; hashing the dir makes it freshness-checked.
    """
    try:
        import hashlib
        entries: list[tuple[str, str]] = []
        for f in sorted(path.rglob("*")):
            if any(part in _DIR_SHA_SKIP for part in f.parts):
                continue
            if not f.is_file() or f.suffix.lower() not in _DIR_SHA_EXTS:
                continue
            entries.append((f.relative_to(path).as_posix(), _compute_file_sha(f)))
            if len(entries) > _DIR_SHA_MAX_FILES:
                return ""
        if not entries:
            return ""
        h = hashlib.sha256()
        for rel, sha in entries:
            h.update(rel.encode("utf-8"))
            h.update(b"\x00")
            h.update(sha.encode("utf-8"))
            h.update(b"\n")
        return h.hexdigest()[:12]
    except (OSError, FileNotFoundError):
        return ""


def _compute_path_sha(path: Path) -> str:
    """SHA for a file OR a directory; '' if neither resolves. The single entry both the
    indexer (add_node) and the freshness check use, so 'file-backed' node types can point
    at a file or a bundle dir and still be freshness-checked identically."""
    if path.is_file():
        return _compute_file_sha(path)
    if path.is_dir():
        return _compute_dir_sha(path)
    return ""


@dataclass
class Edge:
    source: str                      # node id
    target: str                      # node id
    edge_type: str                   # one of EDGE_TYPES
    metadata: dict = field(default_factory=dict)


@dataclass
class TraceGraph:
    """The full-stack trace graph."""
    nodes: dict[str, Node] = field(default_factory=dict)
    edges: list[Edge] = field(default_factory=list)
    built_at: float = 0.0

    # Adjacency indices (built lazily)
    _forward: dict[str, list[Edge]] = field(default_factory=dict, repr=False)
    _reverse: dict[str, list[Edge]] = field(default_factory=dict, repr=False)
    _indexed: bool = field(default=False, repr=False)

    def add_node(self, node: Node):
        # Compute source SHA at index time when file_path resolves to a real file
        # (ADHC_COMPIL_V4.012 STALE_NODE_WARN). Skip if SHA already populated.
        if node.file_path and not node.source_sha:
            try:
                fp = Path(node.file_path)
                if not fp.is_absolute():
                    # Resolve against workspace root (parent of org/modules/graph)
                    fp = Path(__file__).resolve().parent.parent.parent.parent / node.file_path
                # file OR directory (a Lambda bundle dir) -> a source_sha; '' if neither
                # resolves. Previously `is_file()`-only, so a dir file_path minted a node
                # that LOOKED file-backed but was silently skipped by the freshness check
                # (NFRA_TOOLPASS B5/B6).
                node.source_sha = _compute_path_sha(fp)
            except Exception:
                pass
        self.nodes[node.id] = node
        self._indexed = False

    def add_edge(self, edge: Edge):
        # Auto-create nodes if they don't exist
        if edge.source not in self.nodes:
            self.nodes[edge.source] = Node(id=edge.source, node_type="UNKNOWN", label=edge.source)
        if edge.target not in self.nodes:
            self.nodes[edge.target] = Node(id=edge.target, node_type="UNKNOWN", label=edge.target)
        self.edges.append(edge)
        self._indexed = False

    def _build_index(self):
        self._forward = {}
        self._reverse = {}
        for edge in self.edges:
            self._forward.setdefault(edge.source, []).append(edge)
            self._reverse.setdefault(edge.target, []).append(edge)
        self._indexed = True

    def downstream(self, node_id: str, max_depth: int = 10) -> list[tuple[Node, Edge, int]]:
        """Walk forward (downstream) from a node. Returns [(node, edge, depth), ...]."""
        if not self._indexed:
            self._build_index()
        visited = set()
        result = []
        queue = [(node_id, 0)]
        while queue:
            current, depth = queue.pop(0)
            if current in visited or depth > max_depth:
                continue
            visited.add(current)
            for edge in self._forward.get(current, []):
                target_node = self.nodes.get(edge.target)
                if target_node and edge.target not in visited:
                    result.append((target_node, edge, depth + 1))
                    queue.append((edge.target, depth + 1))
        return result

    def upstream(self, node_id: str, max_depth: int = 10) -> list[tuple[Node, Edge, int]]:
        """Walk backward (upstream) from a node. Returns [(node, edge, depth), ...]."""
        if not self._indexed:
            self._build_index()
        visited = set()
        result = []
        queue = [(node_id, 0)]
        while queue:
            current, depth = queue.pop(0)
            if current in visited or depth > max_depth:
                continue
            visited.add(current)
            for edge in self._reverse.get(current, []):
                source_node = self.nodes.get(edge.source)
                if source_node and edge.source not in visited:
                    result.append((source_node, edge, depth + 1))
                    queue.append((edge.source, depth + 1))
        return result

    def find_node(self, query: str) -> list[Node]:
        """Find nodes matching a query string (substring match on id or label)."""
        q = query.lower()
        return [n for n in self.nodes.values()
                if q in n.id.lower() or q in n.label.lower()]

    def save(self, path: Path):
        """Serialize graph to JSON."""
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "built_at": self.built_at,
            "nodes": {k: asdict(v) for k, v in self.nodes.items()},
            "edges": [asdict(e) for e in self.edges],
        }
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> TraceGraph:
        """Deserialize graph from JSON."""
        data = json.loads(path.read_text(encoding="utf-8"))
        g = cls(built_at=data.get("built_at", 0))
        for k, v in data.get("nodes", {}).items():
            md = v.get("metadata", {})
            g.nodes[k] = Node(
                id=v["id"], node_type=v["node_type"], label=v["label"],
                file_path=v.get("file_path", ""), function_name=v.get("function_name", ""),
                run_order=v.get("run_order", -1), metadata=md,
                source_sha=v.get("source_sha", ""),
            )
        for e in data.get("edges", []):
            g.edges.append(Edge(
                source=e["source"], target=e["target"],
                edge_type=e["edge_type"], metadata=e.get("metadata", {}),
            ))
        return g


# ---------------------------------------------------------------------------
# Freshness check (ADHC_COMPIL_V4.012 STALE_NODE_WARN)
# ---------------------------------------------------------------------------

def check_node_freshness(graph: TraceGraph, workspace_root: Path) -> list[tuple[str, str, str]]:
    """Walk all nodes with file_path + source_sha; recompute current SHA; return drift list.

    Returns list of (node_id, indexed_sha, current_sha) tuples for nodes whose
    current file SHA differs from indexed SHA. Empty list = no drift.

    Skips nodes where source_sha is empty (first-build case; CTO AC5 — no false
    positives on empty cache).
    """
    drift: list[tuple[str, str, str]] = []
    # Memoize per resolved path within this pass: multiple Lambda nodes can share one
    # bundle dir (8 nodes share data/find/imo/scripts), so hash each unique path once.
    _sha_cache: dict[str, str] = {}

    def _current_sha(p: Path) -> str:
        key = str(p)
        if key not in _sha_cache:
            _sha_cache[key] = _compute_path_sha(p)
        return _sha_cache[key]

    for node in graph.nodes.values():
        if not node.file_path or not node.source_sha:
            continue
        fp = Path(node.file_path)
        if not fp.is_absolute():
            fp = workspace_root / node.file_path
        if not fp.exists():
            # File/dir deleted since index — count as drift
            drift.append((node.id, node.source_sha, "<missing>"))
            continue
        current = _current_sha(fp)   # file OR directory-aggregate (B5/B6)
        if current and current != node.source_sha:
            drift.append((node.id, node.source_sha, current))
    return drift


def emit_stale_warn(drift: list[tuple[str, str, str]], stream=None) -> None:
    """Emit STALE_NODE_WARN to stderr (or provided stream) for each drift entry.

    Output goes to stderr by default to preserve clean stdout for structured
    tool output (CTO AC2: stdout unchanged).
    """
    if not drift:
        return
    if stream is None:
        stream = sys.stderr
    print(f"STALE_NODE_WARN: {len(drift)} node(s) have source-file SHA drift since last comp-build:",
          file=stream)
    for node_id, indexed, current in drift[:10]:
        print(f"  {node_id}: indexed={indexed} -> current={current}",
              file=stream)
    if len(drift) > 10:
        print(f"  ... and {len(drift) - 10} more (rerun comp-build to refresh)",
              file=stream)
    else:
        print("  Rerun: comp-build", file=stream)


# ---------------------------------------------------------------------------
# Graph building: orchestrate extraction passes
# ---------------------------------------------------------------------------

def build_graph(workspace_root: Path) -> TraceGraph:
    """Build the full trace graph from all extraction passes."""
    from .extract_s3 import extract_s3_edges
    from .extract_api import extract_api_edges
    from .extract_eventbridge import extract_eventbridge_edges, extract_lambda_ec2_edges
    from .extract_lambda_routes import extract_lambda_routes
    from .extract_sfn import extract_sfn_invoke_edges
    from .extract_event_invoke import extract_event_invoke_edges

    g = TraceGraph(built_at=time.time())

    # Pass 2 (priority): S3 artifact mapper
    extract_s3_edges(g, workspace_root)

    # Pass 1: API route extractor
    extract_api_edges(g, workspace_root)

    # Pass 4: EventBridge trigger mapper
    extract_eventbridge_edges(g, workspace_root)

    # Pass 4b: Lambda -> EC2 SSM invocation edges
    extract_lambda_ec2_edges(g, workspace_root)

    # Pass 5: Lambda handler router (must run after Pass 1 + Pass 2)
    extract_lambda_routes(g, workspace_root)

    # Pass 6 (ADHC_COMPIL_V4.020): pipeline-DAG injection for both BD and INF gold.
    # Brings comp-trace + comp-blast back to Tier A (cross-segment): INF gold script
    # nodes (`gold:INF_*`) + s3:platinum/* nodes appear in the cross-layer graph
    # alongside BD gold. Previously `comp-pipescript inject` was a separate step that
    # got wiped on every comp-build rebuild (see V4.017 OPS Cat 2 finding).
    _inject_full_pipeline_into_graph(g, workspace_root)

    # Pass 7 (NFRA_GRAPHUNI.SFNBRIDGE): Step Functions -> Lambda invoke edges. Runs after the Lambda
    # passes so it links to existing lambda:* nodes; creates any it needs. Brings SFN-orchestrated
    # dependents into comp-blast/comp-iam blast radius (bounded invoke-edge projection; deep SFN = comp-aws).
    extract_sfn_invoke_edges(g, workspace_root)

    # Pass 8 (NFRA_GRAPHUNI): the OTHER Lambda-invoke mechanisms -- event-source-mappings (SQS/stream) +
    # SNS(protocol=lambda) -> Lambda. LIVE-derived (read-only boto), NOT static .tf: deploys are TF-only so
    # declared front-runs live, and a .tf parse would emit declared-not-applied phantom edges. Graceful
    # no-op without creds. Completes the non-code invoke-edge coverage in comp-blast/comp-iam blast radius.
    extract_event_invoke_edges(g, workspace_root)

    return g


def _inject_full_pipeline_into_graph(g: "TraceGraph", workspace_root: Path) -> None:
    """ADHC_COMPIL_V4.020: bake pipeline-DAG edges into comp-build output for BD + INF gold.

    This runs the same logic as `extract_pipeline.inject_pipeline_edges` but for both
    BD and INF gold pipelines, in-process during graph build. Side effects:
      - INF gold scripts registered as `gold:INF_*` nodes
      - s3:platinum/* nodes promoted (D_04 + INF_D_04 hardcoded platinum writes)
      - s3:gold/canonical/holdings, etc., named-prefix nodes baked-in for both pipelines
    """
    from .extract_pipeline import (build_pipeline_dag, build_inf_gold_dag,
                                   build_mdpf_dag, inject_pipeline_edges)

    # BD gold (idempotent if already populated by extract_s3_edges; injects platinum
    # write nodes that extract_s3_edges' regex misses).
    bd_dag = build_pipeline_dag(workspace_root)
    inject_pipeline_edges(bd_dag, workspace_root, _graph=g)

    # INF gold (new; previously absent from cross-layer graph).
    inf_dag = build_inf_gold_dag(workspace_root)
    inject_pipeline_edges(inf_dag, workspace_root, _graph=g)

    # MDPF (NFRA_DEBTSCAN TO-D1 iteration, CVO FP #5): the mdpf tree was not
    # stitched at all, so its bucket reads were invisible to the reachability
    # sweep (a live mdpf gold script's read of opal-data-etfs read as an
    # orphaned bucket). build_mdpf_dag already exists (TOOL-02); injecting it
    # here puts mdpf scripts + their key-grain S3 I/O into the cross-layer
    # graph. NOTE: keys are bare (no bucket attribution -- the extractor
    # records key constants only), so BUCKET-grain reachability for non-firm
    # buckets still rides the FP_MDPF_UNSTITCHED suppression until the
    # bucket-qualified extractor leg (TOOL-02 follow-on) lands.
    mdpf_dag = build_mdpf_dag(workspace_root)
    inject_pipeline_edges(mdpf_dag, workspace_root, _graph=g)


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def format_trace(node_id: str, results: list[tuple[Node, Edge, int]], direction: str) -> str:
    """Format trace results as human-readable text."""
    if not results:
        return f"No {direction} connections found for: {node_id}"

    lines = [f"{'UPSTREAM' if direction == 'up' else 'DOWNSTREAM'} trace from: {node_id}", ""]
    for node, edge, depth in results:
        indent = "  " * depth
        arrow = "<-" if direction == "up" else "->"
        lines.append(f"{indent}{arrow} [{edge.edge_type}] {node.label} ({node.node_type})")
        if node.file_path:
            lines.append(f"{indent}   file: {node.file_path}")
    return "\n".join(lines)


@dataclass
class DeltaResult:
    """Result of diffing two graph snapshots."""
    added_nodes: list[Node] = field(default_factory=list)
    removed_nodes: list[Node] = field(default_factory=list)
    added_edges: list[Edge] = field(default_factory=list)
    removed_edges: list[Edge] = field(default_factory=list)

    @property
    def has_changes(self) -> bool:
        return bool(self.added_nodes or self.removed_nodes
                    or self.added_edges or self.removed_edges)

    def summary(self) -> str:
        """One-line summary of changes."""
        parts = []
        if self.added_nodes:
            parts.append(f"+{len(self.added_nodes)} nodes")
        if self.removed_nodes:
            parts.append(f"-{len(self.removed_nodes)} nodes")
        if self.added_edges:
            parts.append(f"+{len(self.added_edges)} edges")
        if self.removed_edges:
            parts.append(f"-{len(self.removed_edges)} edges")
        return ", ".join(parts) if parts else "no changes"


def diff_graphs(baseline: TraceGraph, current: TraceGraph) -> DeltaResult:
    """Compare two graph snapshots and return the delta."""
    result = DeltaResult()

    # Node diff by id
    baseline_ids = set(baseline.nodes.keys())
    current_ids = set(current.nodes.keys())

    for nid in current_ids - baseline_ids:
        result.added_nodes.append(current.nodes[nid])
    for nid in baseline_ids - current_ids:
        result.removed_nodes.append(baseline.nodes[nid])

    # Edge diff by (source, target, edge_type) tuple
    def _edge_key(e: Edge) -> tuple[str, str, str]:
        return (e.source, e.target, e.edge_type)

    baseline_edge_keys = {}
    for e in baseline.edges:
        baseline_edge_keys[_edge_key(e)] = e

    current_edge_keys = {}
    for e in current.edges:
        current_edge_keys[_edge_key(e)] = e

    for key in set(current_edge_keys) - set(baseline_edge_keys):
        result.added_edges.append(current_edge_keys[key])
    for key in set(baseline_edge_keys) - set(current_edge_keys):
        result.removed_edges.append(baseline_edge_keys[key])

    # Sort for stable output
    result.added_nodes.sort(key=lambda n: n.id)
    result.removed_nodes.sort(key=lambda n: n.id)
    result.added_edges.sort(key=lambda e: (e.source, e.target))
    result.removed_edges.sort(key=lambda e: (e.source, e.target))

    return result


def save_baseline(graph: TraceGraph, cache_dir: Path):
    """Save the current graph as the baseline for future xref comparisons."""
    baseline_path = cache_dir / "baseline.json"
    graph.save(baseline_path)
    return baseline_path


def format_delta(delta: DeltaResult) -> str:
    """Format a DeltaResult as human-readable text."""
    if not delta.has_changes:
        return "XREF: No changes since baseline."

    lines = [f"XREF DELTA: {delta.summary()}", ""]

    if delta.added_nodes:
        # Group by type
        by_type: dict[str, list[Node]] = {}
        for n in delta.added_nodes:
            by_type.setdefault(n.node_type, []).append(n)
        lines.append(f"ADDED NODES ({len(delta.added_nodes)}):")
        for ntype, nodes in sorted(by_type.items()):
            lines.append(f"  {ntype} ({len(nodes)}):")
            for n in nodes:
                detail = f" [{n.file_path}]" if n.file_path else ""
                lines.append(f"    + {n.label}{detail}")
        lines.append("")

    if delta.removed_nodes:
        by_type = {}
        for n in delta.removed_nodes:
            by_type.setdefault(n.node_type, []).append(n)
        lines.append(f"REMOVED NODES ({len(delta.removed_nodes)}):")
        for ntype, nodes in sorted(by_type.items()):
            lines.append(f"  {ntype} ({len(nodes)}):")
            for n in nodes:
                lines.append(f"    - {n.label}")
        lines.append("")

    if delta.added_edges:
        lines.append(f"ADDED EDGES ({len(delta.added_edges)}):")
        for e in delta.added_edges:
            lines.append(f"    + {e.source} -[{e.edge_type}]-> {e.target}")
        lines.append("")

    if delta.removed_edges:
        lines.append(f"REMOVED EDGES ({len(delta.removed_edges)}):")
        for e in delta.removed_edges:
            lines.append(f"    - {e.source} -[{e.edge_type}]-> {e.target}")
        lines.append("")

    return "\n".join(lines)


# Blast radius is bounded by EXTRACTED graph edges. Dynamic/FUNC-key reads the
# extractors don't model (the comp-pipescript D_02 advisor_timeseries miss class)
# produce no edge -> a real consumer is invisible. So "zero consumers" means "no
# EXTRACTED edge," NOT "provably none," and any count is a LOWER BOUND. Never let
# blast/phantom output read as "safe to delete/change."
BLAST_EDGE_CAVEAT = (
    "NOTE: counts EXTRACTED graph edges only (LOWER BOUND). Dynamic/FUNC-key "
    "consumers the extractors don't edge are NOT counted. Before treating a "
    "producer as orphan/safe, grep its artifact key for dynamic reads "
    "(comp-pipescript consumers / a literal-key grep)."
)


def format_blast(node_id: str, results: list[tuple[Node, Edge, int]]) -> str:
    """Format blast radius as advisory warnings."""
    if not results:
        return (f"No downstream consumers found for: {node_id} "
                f"(no EXTRACTED edge -- NOT provably zero).\n  {BLAST_EDGE_CAVEAT}")

    # Group by type
    by_type: dict[str, list[Node]] = {}
    for node, edge, depth in results:
        by_type.setdefault(node.node_type, []).append(node)

    lines = [f"BLAST RADIUS: {node_id}", ""]
    for ntype, nodes in sorted(by_type.items()):
        lines.append(f"  {ntype} ({len(nodes)}):")
        for n in nodes:
            lines.append(f"    - {n.label}")
    lines.append("")
    lines.append(f"WARNING: {node_id} affects >= {len(results)} downstream nodes")
    lines.append(f"  {BLAST_EDGE_CAVEAT}")
    return "\n".join(lines)
