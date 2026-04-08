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
import os
import re
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


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
            )
        for e in data.get("edges", []):
            g.edges.append(Edge(
                source=e["source"], target=e["target"],
                edge_type=e["edge_type"], metadata=e.get("metadata", {}),
            ))
        return g


# ---------------------------------------------------------------------------
# Graph building: orchestrate extraction passes
# ---------------------------------------------------------------------------

def build_graph(workspace_root: Path) -> TraceGraph:
    """Build the full trace graph from all extraction passes."""
    from .extract_s3 import extract_s3_edges
    from .extract_api import extract_api_edges
    from .extract_eventbridge import extract_eventbridge_edges
    from .extract_lambda_routes import extract_lambda_routes

    g = TraceGraph(built_at=time.time())

    # Pass 2 (priority): S3 artifact mapper
    extract_s3_edges(g, workspace_root)

    # Pass 1: API route extractor
    extract_api_edges(g, workspace_root)

    # Pass 4: EventBridge trigger mapper
    extract_eventbridge_edges(g, workspace_root)

    # Pass 5: Lambda handler router (must run after Pass 1 + Pass 2)
    extract_lambda_routes(g, workspace_root)

    return g


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


def format_blast(node_id: str, results: list[tuple[Node, Edge, int]]) -> str:
    """Format blast radius as advisory warnings."""
    if not results:
        return f"No downstream consumers found for: {node_id}"

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
    lines.append(f"WARNING: {node_id} affects {len(results)} downstream nodes")
    return "\n".join(lines)
