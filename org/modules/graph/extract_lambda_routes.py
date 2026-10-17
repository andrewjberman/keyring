"""
Pass 5: Lambda Handler Router -- connect ENDPOINT nodes to LAMBDA nodes.

Two-phase approach:
  Phase A: Build a Lambda source directory map from the function-map folder
           (infra/aws/lambda/ci/function-map/, one file per function, read through lib/opal_lambda_map.py).
           Maps function names to their source directories.
  Phase B: Scan Lambda handler source for API Gateway route patterns.
           Matches URL paths from ENDPOINT nodes (extract_api.py) to Lambda handlers.

This closes the full chain: COMPONENT -> ENDPOINT -> LAMBDA -> S3 -> GOLD_SCRIPT.

Also handles CloudFront-based routing where URL patterns in endpoint calls
map to Lambda functions via CloudFront behavior -> API Gateway origin.

Zero API calls. Pure static analysis.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from .trace_graph import TraceGraph, Node, Edge

# ---------------------------------------------------------------------------
# API Gateway patterns in Lambda handlers
# ---------------------------------------------------------------------------

# event['pathParameters']['clientKey']
_PATH_PARAMS = re.compile(
    r"""event\s*\[\s*['"]pathParameters['"]\s*\]\s*\[\s*['"](\w+)['"]\s*\]"""
)

# event['rawPath'] or event.get('rawPath')
_RAW_PATH = re.compile(
    r"""event\s*(?:\[['"]|\.\s*get\s*\(\s*['"])rawPath"""
)

# event['resource'] (API Gateway v1 route key)
_RESOURCE_PATH = re.compile(
    r"""event\s*\[\s*['"]resource['"]\s*\]"""
)

# Docstring/comment patterns that describe the route
# e.g., "GET /api/scoped/advisor-intelligence/artifacts/{key}"
_ROUTE_COMMENT = re.compile(
    r"""(?:GET|POST|PUT|DELETE|PATCH)\s+(\/[\w/{}.*-]+)""",
    re.IGNORECASE,
)

# S3 key in endpoint URL: /api/scoped/advisor-intelligence/artifacts/foo.json
# Maps to S3: gold/artifacts/foo.json
_ENDPOINT_S3_PATH = re.compile(
    r"""/api/(?:scoped|shared)/[\w-]+/(.+\.json)"""
)

# CloudFront behavior patterns from Terraform
# Maps URL prefixes to Lambda function origins
_CF_BEHAVIOR_PATTERN = re.compile(
    r"""path_pattern\s*=\s*"([^"]+)"""
)

# ---------------------------------------------------------------------------
# Lambda function map loader (one file per function, read through lib/opal_lambda_map.py)
# ---------------------------------------------------------------------------

_LIB = Path(__file__).resolve().parents[3] / "lib"


def _load_source_map(workspace_root: Path) -> dict[str, dict]:
    """Load the function-map folder under workspace_root. Returns {function_name: {source_dir, files, ...}}.

    Raises FileNotFoundError (folder absent) or ValueError (folder holds no function file). A silent empty map is
    the clean-looking false answer this loader used to give (NFRA_CTLPLN round 30 ruling 1), so it does not return one.
    """
    if str(_LIB) not in sys.path:
        sys.path.insert(0, str(_LIB))
    from opal_lambda_map import load_all  # noqa: PLC0415
    return load_all(str(workspace_root))


# ---------------------------------------------------------------------------
# URL-to-Lambda matching
# ---------------------------------------------------------------------------

# Known URL prefix -> Lambda function name mappings.
# Derived from CloudFront behaviors + API Gateway config.
# These are the routing rules that connect portal endpoint URLs to Lambda handlers.
_URL_LAMBDA_MAP = {
    "/api/scoped/advisor-intelligence/clients/": "bd-client-detail",
    "/api/scoped/advisor-intelligence/artifacts/": "opal-partners-data",
    "/api/scoped/advisor-intelligence/": "opal-partners-data",
    "/api/shared/advisor-intelligence/": "opal-partners-data",
    "/api/scoped/market-overview/": "opal-market-data-proxy",
    "/api/shared/market-overview/": "opal-market-data-proxy",
    "/api/scoped/portfolio-management/": "opal-portfolio-data",
    "/api/shared/portfolio-management/": "opal-portfolio-data",
    "/api/time-machine/": "bd-time-machine",
    "/api/data-refresh/": "opal-data-refresh-trigger",
}


def _match_url_to_lambda(url: str) -> str | None:
    """Match an endpoint URL to a Lambda function name using routing rules."""
    for prefix, lambda_name in _URL_LAMBDA_MAP.items():
        if url.startswith(prefix):
            return lambda_name
    return None


def extract_lambda_routes(graph: TraceGraph, workspace_root: Path):
    """Connect ENDPOINT nodes to LAMBDA nodes by matching URL patterns."""

    source_map = _load_source_map(workspace_root)

    # --- Phase A: Ensure all Lambda functions from source map are in the graph ---
    for fn_name, fn_info in source_map.items():
        lambda_node_id = f"lambda:{fn_name}"
        if lambda_node_id not in graph.nodes:
            source_dir = fn_info.get("source_dir", "")
            metadata = {
                "tf_file": fn_info.get("tf_file", ""),
                "pipeline": source_dir.split("/")[3] if "/" in source_dir and len(source_dir.split("/")) > 3 else "",
            }
            # Only set file_path to a source_dir that resolves ON DISK. The "EXTERNAL"
            # sentinel (code lives outside the repo, lambdamap_cli.py:127) and any
            # absent dir are NOT freshness-checkable; recording them as file_path mints
            # a node that LOOKS file-backed but is silently skipped by
            # check_node_freshness -> a Lambda edit that never registers as drift
            # (NFRA_TOOLPASS B5/B6). Preserve provenance in metadata instead of lying
            # via file_path. A real dir now gets a directory-aggregate sha (add_node).
            file_path = ""
            if source_dir == "EXTERNAL":
                metadata["source_dir"] = "EXTERNAL"
            elif source_dir:
                if (workspace_root / source_dir).exists():
                    file_path = source_dir
                else:
                    metadata["source_dir_unresolved"] = source_dir
            graph.add_node(Node(
                id=lambda_node_id,
                node_type="LAMBDA",
                label=fn_name,
                file_path=file_path,
                metadata=metadata,
            ))

    # --- Phase B: Match ENDPOINT URLs to Lambda functions ---
    endpoint_nodes = [
        n for n in graph.nodes.values()
        if n.node_type == "ENDPOINT"
    ]

    for endpoint in endpoint_nodes:
        urls = endpoint.metadata.get("urls", [])
        matched_lambdas = set()

        for url in urls:
            lambda_name = _match_url_to_lambda(url)
            if lambda_name:
                matched_lambdas.add(lambda_name)

        for lambda_name in matched_lambdas:
            lambda_node_id = f"lambda:{lambda_name}"
            if lambda_node_id not in graph.nodes:
                # Create Lambda node if it doesn't exist yet
                graph.add_node(Node(
                    id=lambda_node_id,
                    node_type="LAMBDA",
                    label=lambda_name,
                ))

            # Check if edge already exists (avoid duplicates)
            edge_exists = any(
                e.source == endpoint.id and e.target == lambda_node_id
                and e.edge_type == "FETCHES"
                for e in graph.edges
            )
            if not edge_exists:
                graph.add_edge(Edge(
                    source=endpoint.id,
                    target=lambda_node_id,
                    edge_type="FETCHES",
                    metadata={"urls": urls},
                ))

    # --- Phase C: Scan Lambda source for route patterns (documentation) ---
    # This adds metadata to LAMBDA nodes about what routes they serve,
    # useful for the trace output even when URL matching didn't fire.
    lambda_base = workspace_root / "infra" / "aws" / "lambda"
    if not lambda_base.exists():
        return

    for fn_name, fn_info in source_map.items():
        source_dir = workspace_root / fn_info.get("source_dir", "")
        if not source_dir.exists():
            continue

        lambda_node_id = f"lambda:{fn_name}"
        if lambda_node_id not in graph.nodes:
            continue

        # Read handler file for route documentation
        handler_file = source_dir / "lambda_function.py"
        if not handler_file.exists():
            continue

        try:
            content = handler_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        # Extract documented routes from comments/docstrings
        routes = set()
        for m in _ROUTE_COMMENT.finditer(content[:2000]):  # Only scan top of file
            routes.add(m.group(0))

        # Check for path parameter handling
        has_path_params = bool(_PATH_PARAMS.search(content))
        has_raw_path = bool(_RAW_PATH.search(content))

        if routes or has_path_params or has_raw_path:
            node = graph.nodes[lambda_node_id]
            node.metadata["documented_routes"] = sorted(routes)
            node.metadata["has_path_params"] = has_path_params
            node.metadata["has_raw_path"] = has_raw_path
