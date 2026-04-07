"""
In: Interpret -- Cross-Reference Graph Builder (D-mode).

Extracts all internal references between files and builds a directed
citation graph. Tells you which objects are foundational vs. peripheral
without reading content.

Zero API calls. Pure regex extraction + graph construction.

Spec: ONT.CORE.KF_ACCELERATION Section 2.2
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .. import ModuleOutput
from ..perceive.filesystem_scanner import FileMetadata


@dataclass
class GraphNode:
    """A file in the citation graph."""
    path: str
    filename: str
    in_degree: int = 0          # How many files reference this one
    out_degree: int = 0         # How many files this references
    orphan: bool = False        # Zero in AND zero out
    references_to: list[str] = field(default_factory=list)    # Outgoing edges
    referenced_by: list[str] = field(default_factory=list)    # Incoming edges


@dataclass
class CrossRefGraph:
    """Complete citation graph for a corpus."""
    nodes: dict[str, GraphNode] = field(default_factory=dict)
    edge_count: int = 0
    orphans: list[str] = field(default_factory=list)
    highest_authority: list[dict] = field(default_factory=list)  # Sorted by in_degree desc
    highest_integration: list[dict] = field(default_factory=list)  # Sorted by out_degree desc


# Reference extraction patterns
_MD_LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
_SPEC_ID_REF = re.compile(r"\b(ONT|SYS|APP)\.(CORE|DERIVED|META)\.\w+\b")
_PY_IMPORT = re.compile(r"^(?:from\s+([\w.]+)\s+)?import\s+(.+)$", re.MULTILINE)
_YAML_REF = re.compile(r'(?:extends|ref|\$ref):\s*["\']?([^\s"\']+)')
_PATH_LITERAL = re.compile(r'["\']([a-zA-Z_][\w/.-]*\.(?:md|json|yaml|yml|py))["\']')


def _extract_references(file_path: Path, content: str, all_paths: set[str]) -> list[str]:
    """Extract all references from a file to other files in the corpus."""
    refs = set()
    parent = file_path.parent

    # Markdown links
    for m in _MD_LINK.finditer(content):
        target = m.group(2)
        if not target.startswith("http"):
            resolved = _resolve_ref(target, parent, all_paths)
            if resolved:
                refs.add(resolved)

    # Spec ID references (e.g., ONT.CORE.ARCHETYPES)
    for m in _SPEC_ID_REF.finditer(content):
        spec_id = m.group(0)
        # Try to match against filenames
        for p in all_paths:
            fname = Path(p).stem.upper()
            if spec_id.split(".")[-1] in fname:
                refs.add(p)

    # Python imports
    for m in _PY_IMPORT.finditer(content):
        from_module = m.group(1) or ""
        if from_module and ".." not in from_module:
            # Try to resolve to a file path
            candidate = from_module.replace(".", "/") + ".py"
            for p in all_paths:
                if p.endswith(candidate):
                    refs.add(p)

    # YAML references
    for m in _YAML_REF.finditer(content):
        target = m.group(1)
        resolved = _resolve_ref(target, parent, all_paths)
        if resolved:
            refs.add(resolved)

    # Path literals in strings
    for m in _PATH_LITERAL.finditer(content):
        target = m.group(1)
        resolved = _resolve_ref(target, parent, all_paths)
        if resolved:
            refs.add(resolved)

    # Don't self-reference
    refs.discard(str(file_path))
    return sorted(refs)


def _resolve_ref(target: str, parent_dir: Path, all_paths: set[str]) -> str | None:
    """Try to resolve a reference string to an actual file path."""
    # Absolute match
    if target in all_paths:
        return target

    # Relative to parent
    resolved = parent_dir / target
    resolved_str = str(resolved).replace("\\", "/")
    if resolved_str in all_paths:
        return resolved_str

    # Filename match (last resort)
    target_name = Path(target).name
    for p in all_paths:
        if Path(p).name == target_name:
            return p

    return None


def build_graph(file_metadata: list[FileMetadata]) -> CrossRefGraph:
    """Build a cross-reference graph from file metadata."""
    all_paths = {m.path.replace("\\", "/") for m in file_metadata}
    graph = CrossRefGraph()

    # Initialize nodes
    for meta in file_metadata:
        norm_path = meta.path.replace("\\", "/")
        graph.nodes[norm_path] = GraphNode(
            path=norm_path,
            filename=meta.filename,
        )

    # Extract references
    for meta in file_metadata:
        norm_path = meta.path.replace("\\", "/")
        try:
            content = Path(meta.path).read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        refs = _extract_references(Path(meta.path), content, all_paths)
        node = graph.nodes[norm_path]
        node.references_to = refs
        node.out_degree = len(refs)
        graph.edge_count += len(refs)

        # Update incoming edges
        for ref in refs:
            if ref in graph.nodes:
                graph.nodes[ref].referenced_by.append(norm_path)
                graph.nodes[ref].in_degree += 1

    # Compute orphans and rankings
    for path, node in graph.nodes.items():
        if node.in_degree == 0 and node.out_degree == 0:
            node.orphan = True
            graph.orphans.append(node.filename)

    # Top authority (most referenced)
    by_authority = sorted(
        graph.nodes.values(), key=lambda n: n.in_degree, reverse=True
    )
    graph.highest_authority = [
        {"path": n.path, "filename": n.filename, "in_degree": n.in_degree}
        for n in by_authority[:10] if n.in_degree > 0
    ]

    # Top integration (most referencing)
    by_integration = sorted(
        graph.nodes.values(), key=lambda n: n.out_degree, reverse=True
    )
    graph.highest_integration = [
        {"path": n.path, "filename": n.filename, "out_degree": n.out_degree}
        for n in by_integration[:10] if n.out_degree > 0
    ]

    return graph


def execute(inputs: dict, config: dict) -> ModuleOutput:
    """Build cross-reference graph from Pe output.

    Inputs:
        pe_output: list[FileMetadata]
    """
    pe_output: list[FileMetadata] = inputs.get("pe_output", [])

    graph = build_graph(pe_output)

    return ModuleOutput(
        data=graph,
        confident=[],
        ambiguous=[],
        mode="D",
        stage="In",
        stats={
            "nodes": len(graph.nodes),
            "edges": graph.edge_count,
            "orphans": len(graph.orphans),
            "orphan_files": graph.orphans,
            "top_authority": graph.highest_authority[:5],
            "top_integration": graph.highest_integration[:5],
        },
    )
