"""
Pass 1: API Route Extractor — extract FETCHES edges from portal components.

Scans portal/src/api/endpoints/*.ts for fetch wrapper functions.
Scans portal/src/pages/**/*.tsx for calls to those functions.
Builds COMPONENT -> ENDPOINT -> (URL pattern) edges.

Zero API calls. Pure regex extraction.
"""

from __future__ import annotations

import re
from pathlib import Path

from .trace_graph import TraceGraph, Node, Edge

# ---------------------------------------------------------------------------
# API endpoint extraction (from .ts endpoint files)
# ---------------------------------------------------------------------------

# Match: export async function getFoo(...) or export const getFoo = async (...)
_TS_EXPORT_FN = re.compile(
    r"""export\s+(?:async\s+)?function\s+(\w+)\s*\("""
)
_TS_EXPORT_CONST_FN = re.compile(
    r"""export\s+const\s+(\w+)\s*=\s*(?:async\s*)?\("""
)

# Match fetch/axios URLs: fetch(`/api/scoped/...`) or axiosInstance.get("/api/...")
_FETCH_URL = re.compile(
    r"""(?:fetch|get|post|put|delete|patch)\s*\(\s*[`'"]([^`'"]+)[`'"]""",
    re.IGNORECASE
)

# Template literal URLs: `${BASE_URL}/artifacts/foo.json`
_TEMPLATE_URL = re.compile(
    r"""[`]([^`]*\$\{[^}]+\}[^`]*)[`]"""
)

# Match: const BASE_URL = "/api/scoped/advisor-intelligence"
_BASE_URL_CONST = re.compile(
    r"""(?:const|let|var)\s+(\w*(?:BASE|URL|PREFIX|API|ENDPOINT)\w*)\s*=\s*[`'"]([^`'"]+)[`'"]""",
    re.IGNORECASE
)

# ---------------------------------------------------------------------------
# Component -> endpoint function call extraction
# ---------------------------------------------------------------------------

# Match: import { getFoo, getBar } from '@/api/endpoints/advisor-intelligence'
_TS_NAMED_IMPORT = re.compile(
    r"""import\s*\{([^}]+)\}\s*from\s*['"]([^'"]+)['"]"""
)

# Match: getFoo() or getFoo(arg1, arg2)
def _make_call_pattern(fn_name: str) -> re.Pattern:
    return re.compile(rf'\b{re.escape(fn_name)}\s*\(')


# ---------------------------------------------------------------------------
# Main extraction
# ---------------------------------------------------------------------------

def extract_api_edges(graph: TraceGraph, workspace_root: Path):
    """Extract API route edges from portal source."""

    portal_dir = workspace_root / "portal"
    if not portal_dir.exists():
        return

    api_dir = portal_dir / "src" / "api" / "endpoints"
    pages_dir = portal_dir / "src" / "pages"

    # --- Phase A: Extract endpoint functions and their URLs ---
    endpoint_registry: dict[str, dict] = {}  # fn_name -> {url, file, ...}

    if api_dir.exists():
        for ts_file in sorted(api_dir.glob("*.ts")):
            try:
                content = ts_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            rel_path = str(ts_file.relative_to(workspace_root)).replace("\\", "/")

            # Extract base URL constants
            base_urls = {}
            for m in _BASE_URL_CONST.finditer(content):
                base_urls[m.group(1)] = m.group(2)

            # Extract exported functions
            fn_names = set()
            for pattern in (_TS_EXPORT_FN, _TS_EXPORT_CONST_FN):
                for m in pattern.finditer(content):
                    fn_names.add(m.group(1))

            # For each function, find its fetch URL
            for fn_name in fn_names:
                # Find the function body (approximate: from def to next export or EOF)
                fn_pattern = re.compile(
                    rf'(?:export\s+(?:async\s+)?function\s+{re.escape(fn_name)}\s*\('
                    rf'|export\s+const\s+{re.escape(fn_name)}\s*=)',
                )
                fn_match = fn_pattern.search(content)
                if not fn_match:
                    continue

                # Get chunk from function start to next export or EOF
                start = fn_match.start()
                next_export = re.search(r'\nexport\s+', content[start + 10:])
                end = start + 10 + next_export.start() if next_export else len(content)
                chunk = content[start:end]

                # Extract URLs from this function's body
                urls = []
                for m in _FETCH_URL.finditer(chunk):
                    url = m.group(1)
                    # Resolve template variables
                    for var_name, var_val in base_urls.items():
                        url = url.replace(f"${{{var_name}}}", var_val)
                    urls.append(url)

                for m in _TEMPLATE_URL.finditer(chunk):
                    url = m.group(1)
                    for var_name, var_val in base_urls.items():
                        url = url.replace(f"${{{var_name}}}", var_val)
                    urls.append(url)

                endpoint_node_id = f"endpoint:{fn_name}"
                graph.add_node(Node(
                    id=endpoint_node_id,
                    node_type="ENDPOINT",
                    label=fn_name,
                    file_path=rel_path,
                    metadata={"urls": urls, "source_file": ts_file.name},
                ))

                endpoint_registry[fn_name] = {
                    "node_id": endpoint_node_id,
                    "urls": urls,
                    "file": rel_path,
                }

                # If URL points to an S3 artifact path, link to S3 node
                for url in urls:
                    # /api/scoped/advisor-intelligence/artifacts/employee_leaderboard.json
                    # -> maps to S3: gold/artifacts/employee_leaderboard.json
                    artifact_match = re.search(r'/artifacts?/([^\s?#]+)', url)
                    if artifact_match:
                        artifact_name = artifact_match.group(1)
                        # Try to find matching S3 node (exact suffix match,
                        # not substring -- prevents employee_leaderboard.json
                        # from matching getBooksAccountComposition)
                        for node_id, node in list(graph.nodes.items()):
                            if node.node_type == "S3_ARTIFACT" and node.label.endswith(artifact_name):
                                graph.add_edge(Edge(
                                    source=node_id, target=endpoint_node_id,
                                    edge_type="READS_S3",
                                    metadata={"url": url},
                                ))

    # --- Phase B: Extract component -> endpoint function calls ---
    if pages_dir.exists():
        for tsx_file in sorted(pages_dir.rglob("*.tsx")):
            try:
                content = tsx_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            rel_path = str(tsx_file.relative_to(workspace_root)).replace("\\", "/")
            component_name = tsx_file.stem

            # Find imports from API endpoints
            imported_fns = set()
            for m in _TS_NAMED_IMPORT.finditer(content):
                names = [n.strip().split(' as ')[0].strip() for n in m.group(1).split(',')]
                source = m.group(2)
                if 'api/' in source or 'endpoints/' in source:
                    for name in names:
                        if name in endpoint_registry:
                            imported_fns.add(name)

            if not imported_fns:
                continue

            # Create component node
            component_node_id = f"component:{rel_path}"
            graph.add_node(Node(
                id=component_node_id,
                node_type="COMPONENT",
                label=component_name,
                file_path=rel_path,
            ))

            # Check which imported functions are actually called
            for fn_name in imported_fns:
                call_pattern = _make_call_pattern(fn_name)
                if call_pattern.search(content):
                    endpoint_info = endpoint_registry[fn_name]
                    graph.add_edge(Edge(
                        source=component_node_id,
                        target=endpoint_info["node_id"],
                        edge_type="FETCHES",
                        metadata={"function": fn_name},
                    ))
