"""
Pass 2: S3 Artifact Mapper — extract WRITES_S3 and READS_S3 edges.

Scans gold scripts for S3 write patterns (put_object, upload_file, save to S3).
Scans Lambda source for S3 read patterns (get_object, download_file, read from S3).
Builds GOLD_SCRIPT -> S3_ARTIFACT -> LAMBDA edges.

Also extracts the gold script run_order from filename prefix (A_00=0, A_01=1, etc.).

Zero API calls. Pure regex extraction.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path

from .trace_graph import TraceGraph, Node, Edge

# ADHC_COMPIL_V5 TO-VAL AC-VAL-Y.5 -- module-private cache for source-map
# reverse-lookup (source_dir → TF-canonical Lambda name). Populated lazily
# on first call to extract_s3_edges; cleared on test fixtures via setattr.
_lambda_source_map_cache: dict[str, str] | None = None

# ---------------------------------------------------------------------------
# S3 write patterns (gold scripts / Lambdas)
# ---------------------------------------------------------------------------

# s3.put_object(Bucket=..., Key="gold/artifacts/foo.json", ...)
_S3_PUT_OBJECT = re.compile(
    r"""(?:s3|s3_client|client)\.put_object\s*\([^)]*Key\s*=\s*(?:f?['"]([^'"]+)['"]|(\w+))""",
    re.DOTALL
)

# s3.upload_file(..., Key="gold/artifacts/foo.json")
_S3_UPLOAD = re.compile(
    r"""(?:s3|s3_client|client)\.upload_file(?:obj)?\s*\([^)]*Key\s*=\s*(?:f?['"]([^'"]+)['"]|(\w+))""",
    re.DOTALL
)

# Generic S3 key string patterns in gold scripts
# Matches: f"gold/artifacts/{name}.json", "gold/views/foo.parquet", etc.
_S3_KEY_LITERAL = re.compile(
    r"""['"](?:gold|silver|bronze|portal)/[\w/{}.-]+\.(?:json|parquet|csv|gz)['"]"""
)

# upload_json / _save_json / save_to_s3 style helpers
_S3_HELPER_WRITE = re.compile(
    r"""(?:upload_json|_save_json|save_to_s3|_upload_artifact)\s*\([^)]*['"]([^'"]+)['"]""",
)

# S3 key constructed with f-strings or variables
_S3_FSTRING_KEY = re.compile(
    r"""Key\s*=\s*f['"]([^'"]+)['"]"""
)

# ---------------------------------------------------------------------------
# S3 read patterns (Lambdas / gold scripts)
# ---------------------------------------------------------------------------

_S3_GET_OBJECT = re.compile(
    r"""(?:s3|s3_client|client)\.get_object\s*\([^)]*Key\s*=\s*(?:f?['"]([^'"]+)['"]|(\w+))""",
    re.DOTALL
)

_S3_READ_PARQUET = re.compile(
    r"""(?:pd\.read_parquet|read_parquet)\s*\([^)]*['"]([^'"]+)['"]"""
)

_S3_HELPER_READ = re.compile(
    r"""(?:load_json|_load_json|read_from_s3|_download_artifact|get_json)\s*\([^)]*['"]([^'"]+)['"]""",
)

# ---------------------------------------------------------------------------
# Gold script run_order extraction
# ---------------------------------------------------------------------------

_GOLD_PREFIX = re.compile(r'^([A-Z])_(\d{2})')

def _run_order(filename: str) -> int:
    """Extract run order from gold script filename. A_00=0, A_01=1, B_01=100, C_00=200, D_00=300."""
    m = _GOLD_PREFIX.match(filename)
    if not m:
        return -1
    letter_val = (ord(m.group(1)) - ord('A')) * 100
    num_val = int(m.group(2))
    return letter_val + num_val


# ---------------------------------------------------------------------------
# Function-level extraction for gold scripts
# ---------------------------------------------------------------------------

_PYTHON_DEF = re.compile(r'^def\s+(\w+)\s*\(', re.MULTILINE)


def _extract_function_graph(content: str) -> tuple[list[str], dict[str, set[str]]]:
    """Extract top-level function names and local call edges within one file."""
    try:
        tree = ast.parse(content)
    except SyntaxError:
        return [], {}

    function_nodes: list[str] = []
    top_level_defs: list[ast.FunctionDef | ast.AsyncFunctionDef] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            function_nodes.append(node.name)
            top_level_defs.append(node)

    local_names = set(function_nodes)
    call_map: dict[str, set[str]] = {name: set() for name in function_nodes}

    class _CallCollector(ast.NodeVisitor):
        def __init__(self):
            self.calls: set[str] = set()

        def visit_Call(self, node: ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in local_names:
                self.calls.add(node.func.id)
            self.generic_visit(node)

    for fn_node in top_level_defs:
        collector = _CallCollector()
        collector.visit(fn_node)
        collector.calls.discard(fn_node.name)
        call_map[fn_node.name] = collector.calls

    return function_nodes, call_map

# ---------------------------------------------------------------------------
# Constant resolution (e.g., TIMESERIES_CHART -> 'gold/artifacts/timeseries_chart.json')
# ---------------------------------------------------------------------------

_CONST_ASSIGNMENT = re.compile(
    r"""^(\w+)\s*=\s*['"]([^'"]+)['"]""", re.MULTILINE
)

# Single-hop prefix concatenation: TIER1_KEY = OUTPUT_PREFIX + 'tier1.json'
_CONST_CONCAT = re.compile(
    r"""^(\w+)\s*=\s*(\w+)\s*\+\s*['"]([^'"]+)['"]""", re.MULTILINE
)

def _resolve_constants(gold_dir: Path) -> dict[str, str]:
    """Build a map of constant names to their S3 key values from lib/s3_layout.py and similar."""
    constants = {}
    for lib_file in [
        gold_dir / "lib" / "s3_layout.py",
        gold_dir / "lib" / "config.py",
    ]:
        if lib_file.exists():
            try:
                content = lib_file.read_text(encoding="utf-8", errors="replace")
                for m in _CONST_ASSIGNMENT.finditer(content):
                    name, value = m.group(1), m.group(2)
                    if '/' in value and name.isupper():
                        constants[name] = value
            except Exception:
                pass
    return constants


# Pattern: _save_json(data, CONSTANT_NAME, ...) or s3.put_object(..., Key=CONSTANT, ...)
_S3_HELPER_CONST = re.compile(
    r"""(?:_save_json|upload_json|save_to_s3)\s*\([^,]+,\s*(\w+)"""
)

_S3_PUT_CONST = re.compile(
    r"""put_object\s*\([^)]*Key\s*=\s*(\w+)"""
)

_S3_GET_CONST = re.compile(
    r"""get_object\s*\([^)]*Key\s*=\s*(\w+)"""
)


def _extract_builder_to_save_mapping(content: str, constants: dict[str, str] = None) -> dict[str, list[str]]:
    """Extract builder_function -> S3 key mappings from the pattern:
        var = build_X(...)
        _save_json(var, CONSTANT)
    Returns: {build_X: [s3_key, ...]}
    """
    if constants is None:
        constants = {}
    result = {}

    # Find all: var = build_X(...) patterns
    build_calls = re.finditer(
        r'(\w+)\s*=\s*(build_\w+)\s*\(', content
    )
    var_to_builder = {}
    for m in build_calls:
        var_name, builder_name = m.group(1), m.group(2)
        var_to_builder[var_name] = builder_name

    # Find all: _save_json(var, CONSTANT, ...) patterns
    save_calls = re.finditer(
        r'_save_json\s*\(\s*(\w+)\s*,\s*(\w+)', content
    )
    for m in save_calls:
        var_name, const_or_key = m.group(1), m.group(2)
        s3_key = constants.get(const_or_key)
        if not s3_key:
            continue
        builder = var_to_builder.get(var_name)
        if builder:
            result.setdefault(builder, []).append(s3_key)

    # Also handle: build_X(..., upload=True) pattern (no _save_json, writes internally)
    direct_builders = re.finditer(
        r'(build_\w+)\s*\([^)]*upload\s*=\s*(?:True|not\s+dry_run)', content
    )
    for m in direct_builders:
        builder = m.group(1)
        # Try to find the S3 key from the function definition
        if builder not in result:
            result.setdefault(builder, [])

    return result


def _extract_functions_with_s3(content: str, constants: dict[str, str] = None) -> dict[str, list[str]]:
    """Map function names to S3 keys they write. Best-effort: assigns S3 keys
    to the nearest preceding function def."""
    functions = list(_PYTHON_DEF.finditer(content))
    if not functions:
        return {}

    if constants is None:
        constants = {}

    result = {}
    for i, func_match in enumerate(functions):
        func_name = func_match.group(1)
        start = func_match.start()
        end = functions[i + 1].start() if i + 1 < len(functions) else len(content)
        chunk = content[start:end]

        keys = set()
        # String literal patterns
        for pattern in (_S3_PUT_OBJECT, _S3_UPLOAD, _S3_HELPER_WRITE, _S3_FSTRING_KEY):
            for m in pattern.finditer(chunk):
                key = m.group(1) or (m.group(2) if m.lastindex >= 2 else None)
                if key and '/' in key and not key.startswith('{'):
                    ck = _clean_s3_key(key)
                    if _is_valid_s3_key(ck):
                        keys.add(ck)

        for m in _S3_KEY_LITERAL.finditer(chunk):
            raw = m.group(0).strip("'\"")
            if '/' in raw:
                ck = _clean_s3_key(raw)
                if _is_valid_s3_key(ck):
                    keys.add(ck)

        # Constant-based patterns: _save_json(data, TIMESERIES_CHART, ...)
        for pattern in (_S3_HELPER_CONST, _S3_PUT_CONST):
            for m in pattern.finditer(chunk):
                const_name = m.group(1)
                if const_name in constants:
                    keys.add(constants[const_name])

        if keys:
            result[func_name] = sorted(keys)

    return result


def _clean_s3_key(key: str) -> str:
    """Clean up f-string artifacts from S3 keys."""
    # Remove f-string braces: gold/artifacts/{name}.json -> gold/artifacts/*.json
    key = re.sub(r'\{[^}]+\}', '*', key)
    # Remove surrounding quotes
    key = key.strip("'\"")
    return key


# A real S3 key path: word chars + / _ - . * = : % + only (after _clean_s3_key
# replaces {...} with *). NFRA_GRAPHS D5: the broad ['"]([^'"]+)['"] capture
# patterns (re.DOTALL) can pair a quote inside a code expression with the next
# string literal far below, over-capturing a code fragment + comment as a fake
# key (e.g. "].read()))\n\n# Transaction types ...") that slips through the bare
# '/' in key filter when the spanned text contains a slash. This validator
# rejects any candidate carrying whitespace, quotes, or Python-syntax chars, so
# only plausible key paths become S3_ARTIFACT nodes (kills the comp-trace
# junk-node class the GLOBGRPH stitch 0-dangling check surfaced 2026-06-11).
_VALID_S3_KEY = re.compile(r'[\w/.*=:%+-]+\Z')


def _is_valid_s3_key(key: str) -> bool:
    """True only for plausible S3 key paths (post-_clean_s3_key)."""
    return bool(key) and '/' in key and bool(_VALID_S3_KEY.match(key))


def _extract_s3_reads(content: str, constants: dict[str, str] = None) -> set[str]:
    """Extract all S3 keys read by a file."""
    if constants is None:
        constants = {}
    keys = set()
    for pattern in (_S3_GET_OBJECT, _S3_HELPER_READ):
        for m in pattern.finditer(content):
            key = m.group(1) or (m.group(2) if m.lastindex >= 2 else None)
            if key and '/' in key and not key.startswith('{'):
                ck = _clean_s3_key(key)
                if _is_valid_s3_key(ck):
                    keys.add(ck)

    for m in _S3_READ_PARQUET.finditer(content):
        key = m.group(1)
        if '/' in key:
            ck = _clean_s3_key(key)
            if _is_valid_s3_key(ck):
                keys.add(ck)

    # Constant-based reads: s3.get_object(Key=CONSTANT)
    for m in _S3_GET_CONST.finditer(content):
        const_name = m.group(1)
        if const_name in constants:
            keys.add(constants[const_name])

    return keys


# ---------------------------------------------------------------------------
# Main extraction
# ---------------------------------------------------------------------------

def extract_s3_edges(graph: TraceGraph, workspace_root: Path):
    """Extract S3 read/write edges from gold scripts and Lambda source."""

    # --- Gold scripts (writers) ---
    gold_dir = workspace_root / "data" / "black_diamond" / "scripts" / "gold"
    if gold_dir.exists():
        # Resolve constants from lib/s3_layout.py
        constants = _resolve_constants(gold_dir)

        for py_file in sorted(gold_dir.glob("*.py")):
            if py_file.name.startswith("__"):
                continue
            try:
                content = py_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            order = _run_order(py_file.stem)
            rel_path = str(py_file.relative_to(workspace_root)).replace("\\", "/")

            # File-level node
            script_node_id = f"gold:{py_file.stem}"
            graph.add_node(Node(
                id=script_node_id,
                node_type="GOLD_SCRIPT",
                label=py_file.stem,
                file_path=rel_path,
                run_order=order,
            ))

            # Function-level nodes + local call graph.
            function_names, call_map = _extract_function_graph(content)
            for func_name in function_names:
                func_node_id = f"gold:{py_file.stem}:{func_name}"
                graph.add_node(Node(
                    id=func_node_id,
                    node_type="GOLD_SCRIPT",
                    label=f"{py_file.stem}:{func_name}",
                    file_path=rel_path,
                    function_name=func_name,
                    run_order=order,
                ))

            for caller, callees in call_map.items():
                caller_node_id = f"gold:{py_file.stem}:{caller}"
                for callee in sorted(callees):
                    callee_node_id = f"gold:{py_file.stem}:{callee}"
                    graph.add_edge(Edge(
                        source=caller_node_id,
                        target=callee_node_id,
                        edge_type="CALLS",
                    ))
                    # ADHC_ROUTER.T1 fix: previously also added a reverse
                    # CALLED_BY edge here so `comp-blast helper` could walk
                    # toward callers. That polluted `downstream()` (which
                    # indexes by source regardless of edge_type), making the
                    # blast radius of any function explode to every function
                    # in the same script via alternating forward+reverse
                    # traversal. Caller chain now surfaces via `upstream()`
                    # invoked from cmd_blast when the query resolves to a
                    # function-grain node (see cli.cmd_blast).

            # Builder-to-save mapping: build_X() -> _save_json(var, CONSTANT)
            builder_writes = _extract_builder_to_save_mapping(content, constants)
            for builder_name, s3_keys in builder_writes.items():
                builder_node_id = f"gold:{py_file.stem}:{builder_name}"
                graph.add_node(Node(
                    id=builder_node_id,
                    node_type="GOLD_SCRIPT",
                    label=f"{py_file.stem}:{builder_name}",
                    file_path=rel_path,
                    function_name=builder_name,
                    run_order=order,
                ))
                for s3_key in s3_keys:
                    s3_node_id = f"s3:{s3_key}"
                    graph.add_node(Node(
                        id=s3_node_id, node_type="S3_ARTIFACT",
                        label=s3_key,
                    ))
                    graph.add_edge(Edge(
                        source=builder_node_id, target=s3_node_id,
                        edge_type="WRITES_S3",
                    ))

            # Function-level S3 writes (direct put_object patterns, not builder->save)
            func_writes = _extract_functions_with_s3(content, constants)
            for func_name, s3_keys in func_writes.items():
                # Skip if already covered by builder mapping
                if func_name in builder_writes:
                    continue
                func_node_id = f"gold:{py_file.stem}:{func_name}"
                graph.add_node(Node(
                    id=func_node_id,
                    node_type="GOLD_SCRIPT",
                    label=f"{py_file.stem}:{func_name}",
                    file_path=rel_path,
                    function_name=func_name,
                    run_order=order,
                ))
                for s3_key in s3_keys:
                    s3_node_id = f"s3:{s3_key}"
                    graph.add_node(Node(
                        id=s3_node_id, node_type="S3_ARTIFACT",
                        label=s3_key,
                    ))
                    graph.add_edge(Edge(
                        source=func_node_id, target=s3_node_id,
                        edge_type="WRITES_S3",
                    ))

            # File-level S3 reads (gold scripts reading from other scripts' output)
            for s3_key in _extract_s3_reads(content, constants):
                s3_node_id = f"s3:{s3_key}"
                graph.add_node(Node(
                    id=s3_node_id, node_type="S3_ARTIFACT", label=s3_key,
                ))
                graph.add_edge(Edge(
                    source=s3_node_id, target=script_node_id,
                    edge_type="READS_S3",
                ))

    # --- INF gold scripts (writers) ---
    # ADHC_COMPIL_V4.020: extends comp-trace + comp-blast to Tier A by
    # registering INF gold function-level nodes alongside BD. INF gold lives
    # at data/inf/scripts/gold/INF_*.py and uses hardcoded path strings
    # (no s3_layout.py constants), so we run the same loop with constants={}.
    inf_gold_dir = workspace_root / "data" / "inf" / "scripts" / "gold"
    if inf_gold_dir.exists():
        inf_constants: dict[str, str] = {}
        for py_file in sorted(inf_gold_dir.glob("INF_*.py")):
            if py_file.name.startswith("__"):
                continue
            try:
                content = py_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            order = _run_order(py_file.stem.replace("INF_", ""))
            rel_path = str(py_file.relative_to(workspace_root)).replace("\\", "/")

            script_node_id = f"gold:{py_file.stem}"
            graph.add_node(Node(
                id=script_node_id,
                node_type="GOLD_SCRIPT",
                label=py_file.stem,
                file_path=rel_path,
                run_order=order,
            ))

            function_names, call_map = _extract_function_graph(content)
            for func_name in function_names:
                func_node_id = f"gold:{py_file.stem}:{func_name}"
                graph.add_node(Node(
                    id=func_node_id,
                    node_type="GOLD_SCRIPT",
                    label=f"{py_file.stem}:{func_name}",
                    file_path=rel_path,
                    function_name=func_name,
                    run_order=order,
                ))

            for caller, callees in call_map.items():
                caller_node_id = f"gold:{py_file.stem}:{caller}"
                for callee in sorted(callees):
                    callee_node_id = f"gold:{py_file.stem}:{callee}"
                    graph.add_edge(Edge(
                        source=caller_node_id,
                        target=callee_node_id,
                        edge_type="CALLS",
                    ))

            builder_writes = _extract_builder_to_save_mapping(content, inf_constants)
            for builder_name, s3_keys in builder_writes.items():
                builder_node_id = f"gold:{py_file.stem}:{builder_name}"
                graph.add_node(Node(
                    id=builder_node_id,
                    node_type="GOLD_SCRIPT",
                    label=f"{py_file.stem}:{builder_name}",
                    file_path=rel_path,
                    function_name=builder_name,
                    run_order=order,
                ))
                for s3_key in s3_keys:
                    s3_node_id = f"s3:{s3_key}"
                    graph.add_node(Node(
                        id=s3_node_id, node_type="S3_ARTIFACT", label=s3_key,
                    ))
                    graph.add_edge(Edge(
                        source=builder_node_id, target=s3_node_id,
                        edge_type="WRITES_S3",
                    ))

            func_writes = _extract_functions_with_s3(content, inf_constants)
            for func_name, s3_keys in func_writes.items():
                if func_name in builder_writes:
                    continue
                func_node_id = f"gold:{py_file.stem}:{func_name}"
                graph.add_node(Node(
                    id=func_node_id,
                    node_type="GOLD_SCRIPT",
                    label=f"{py_file.stem}:{func_name}",
                    file_path=rel_path,
                    function_name=func_name,
                    run_order=order,
                ))
                for s3_key in s3_keys:
                    s3_node_id = f"s3:{s3_key}"
                    graph.add_node(Node(
                        id=s3_node_id, node_type="S3_ARTIFACT", label=s3_key,
                    ))
                    graph.add_edge(Edge(
                        source=func_node_id, target=s3_node_id,
                        edge_type="WRITES_S3",
                    ))

            for s3_key in _extract_s3_reads(content, inf_constants):
                s3_node_id = f"s3:{s3_key}"
                graph.add_node(Node(
                    id=s3_node_id, node_type="S3_ARTIFACT", label=s3_key,
                ))
                graph.add_edge(Edge(
                    source=s3_node_id, target=script_node_id,
                    edge_type="READS_S3",
                ))

    # --- Lambda source (readers) ---
    lambda_dir = workspace_root / "infra" / "aws" / "lambda"

    # ADHC_COMPIL_V5 TO-VAL AC-VAL-Y.5 -- build source_dir → TF-canonical-name
    # reverse-map once for alias resolution (used by supplemental scan below).
    # Cached in module-private global to avoid re-parse per Lambda file.
    global _lambda_source_map_cache
    if _lambda_source_map_cache is None:
        _lambda_source_map_cache = {}
        sm_file = workspace_root / "infra" / "aws" / "lambda" / "ci" / "lambda-source-map.json"
        if sm_file.exists():
            try:
                import json as _json
                sm_data = _json.loads(sm_file.read_text(encoding="utf-8"))
                if isinstance(sm_data.get("functions"), dict):
                    sm_data = sm_data["functions"]
                for fn_name, entry in sm_data.items():
                    if isinstance(entry, dict):
                        src = entry.get("source_dir") or entry.get("source")
                        if src:
                            src_norm = src.replace("\\", "/").rstrip("/")
                            _lambda_source_map_cache[src_norm] = fn_name
            except Exception:
                pass  # malformed source-map; alias resolution skipped

    if lambda_dir.exists():
        for py_file in lambda_dir.rglob("*.py"):
            if py_file.name.startswith("__") or "layer" in str(py_file).lower():
                continue
            try:
                content = py_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            rel_path = str(py_file.relative_to(workspace_root)).replace("\\", "/")

            # Determine Lambda name from directory structure
            # e.g., infra/aws/lambda/bd-pipeline/opal-partners-data/handler.py
            parts = py_file.relative_to(lambda_dir).parts
            lambda_name = parts[-2] if len(parts) >= 2 else py_file.stem

            # Yang pipeline: directory names don't always match TF canonical
            # function names. TF always adds 'yang-' prefix; directories like
            # 'generate-manifest', 'generate-latest', 'generate-volatility',
            # and other orchestration/outputs dirs omit it. Correct here so
            # WRITES_S3 edges land on the canonical node, not a duplicate.
            # Special case: 'trigger' directory -> 'yang-pipeline-trigger'.
            if 'yang_pipeline' in parts and not lambda_name.startswith('yang'):
                lambda_name = ('yang-pipeline-trigger' if lambda_name == 'trigger'
                               else 'yang-' + lambda_name)

            lambda_node_id = f"lambda:{lambda_name}"
            graph.add_node(Node(
                id=lambda_node_id, node_type="LAMBDA",
                label=lambda_name, file_path=rel_path,
            ))

            # Build per-file constant map for Lambda constant resolution.
            # Yang generators define OUTPUT_KEY = 'json/.../foo.json' at module
            # level and pass the constant name to upload_json(bucket, OUTPUT_KEY,
            # data); the base write loop discards the captured variable name
            # because '/' not in 'OUTPUT_KEY'. Collecting module-level string
            # constants whose values contain '/' lets _S3_HELPER_CONST /
            # _S3_PUT_CONST resolve them to the actual S3 key.
            file_constants: dict[str, str] = {}
            for _cm in _CONST_ASSIGNMENT.finditer(content):
                _cname, _cvalue = _cm.group(1), _cm.group(2)
                if '/' in _cvalue:
                    file_constants[_cname] = _cvalue
            # Resolve single-hop prefix concatenations after simple literals are
            # collected: TIER1_KEY = OUTPUT_PREFIX + 'tier1-snapshot.json'
            for _cm in _CONST_CONCAT.finditer(content):
                _cname, _prefix_name, _suffix = _cm.group(1), _cm.group(2), _cm.group(3)
                if _prefix_name in file_constants and _cname not in file_constants:
                    _cvalue = file_constants[_prefix_name] + _suffix
                    if '/' in _cvalue:
                        file_constants[_cname] = _cvalue

            # S3 reads
            for s3_key in _extract_s3_reads(content, file_constants):
                s3_node_id = f"s3:{s3_key}"
                graph.add_node(Node(
                    id=s3_node_id, node_type="S3_ARTIFACT", label=s3_key,
                ))
                graph.add_edge(Edge(
                    source=s3_node_id, target=lambda_node_id,
                    edge_type="READS_S3",
                ))

            # S3 writes (some Lambdas also write)
            for pattern in (_S3_PUT_OBJECT, _S3_UPLOAD, _S3_HELPER_WRITE, _S3_FSTRING_KEY):
                for m in pattern.finditer(content):
                    key = m.group(1) or (m.group(2) if m.lastindex >= 2 else None)
                    if key and '/' in key and not key.startswith('{'):
                        s3_key = _clean_s3_key(key)
                        if not _is_valid_s3_key(s3_key):
                            continue
                        s3_node_id = f"s3:{s3_key}"
                        graph.add_node(Node(
                            id=s3_node_id, node_type="S3_ARTIFACT", label=s3_key,
                        ))
                        graph.add_edge(Edge(
                            source=lambda_node_id, target=s3_node_id,
                            edge_type="WRITES_S3",
                        ))

            # Constant-based writes: upload_json(bucket, CONSTANT, data) and
            # put_object(Key=CONSTANT). Resolves the yang-generator pattern where
            # the module-level key constant is passed by name to a helper.
            for pattern in (_S3_HELPER_CONST, _S3_PUT_CONST):
                for m in pattern.finditer(content):
                    const_name = m.group(1)
                    if const_name in file_constants:
                        s3_key = file_constants[const_name]
                        s3_node_id = f"s3:{s3_key}"
                        graph.add_node(Node(
                            id=s3_node_id, node_type="S3_ARTIFACT", label=s3_key,
                        ))
                        graph.add_edge(Edge(
                            source=lambda_node_id, target=s3_node_id,
                            edge_type="WRITES_S3",
                        ))

            # ADHC_COMPIL_V5 TO-VAL AC-VAL-Y -- supplemental scan via the
            # `scan_lambda_io` AST-based helper that catches Lambda patterns
            # the regex above misses (helper-fn call-graph + per-FunctionDef
            # intermediate-var DFA + f-string component-wise resolution).
            # Anchor: DS 0.1.0 YALP_MKTOVR.001 brief §11 -- market-overview-
            # tiered-generator's `save_to_s3(SUMMARY_KEY, ...)` + intermediate
            # `key = f"{DETAILS_PREFIX}{ticker}.json"` patterns previously
            # missed by the regex-only path; supplemental scan adds these
            # READS_S3/WRITES_S3 edges to make comp-trace + comp-blast
            # cross-stack traversal Lambda-aware.
            #
            # AC-VAL-Y.5 alias resolution: lambda-source-map.json maps the
            # TF-canonical function name (e.g. opal-market-overview-tiered-
            # generator) to source_dir; we lookup the TF-canonical via the
            # source_dir of this py_file and ALSO add edges under the
            # TF-canonical Lambda Node so comp-trace works for both name
            # variants (directory vs TF/AWS-canonical).
            if py_file.name == "lambda_function.py":
                try:
                    from org.modules.graph.pipeline_cli import scan_lambda_io
                    io = scan_lambda_io(content)

                    # AC-VAL-Y.5 alias lookup: TF-canonical from source-map
                    tf_canonical_name = None
                    if _lambda_source_map_cache is not None:
                        py_parent = str(py_file.parent.relative_to(workspace_root)).replace("\\", "/")
                        tf_canonical_name = _lambda_source_map_cache.get(py_parent)

                    lambda_ids = {lambda_node_id}
                    if tf_canonical_name and tf_canonical_name != lambda_name:
                        tf_node_id = f"lambda:{tf_canonical_name}"
                        graph.add_node(Node(
                            id=tf_node_id, node_type="LAMBDA",
                            label=tf_canonical_name, file_path=rel_path,
                        ))
                        lambda_ids.add(tf_node_id)

                    for s3_key in io.get("s3_reads", set()):
                        if not _is_valid_s3_key(s3_key):
                            continue
                        s3_node_id = f"s3:{s3_key}"
                        graph.add_node(Node(
                            id=s3_node_id, node_type="S3_ARTIFACT", label=s3_key,
                        ))
                        for lid in lambda_ids:
                            graph.add_edge(Edge(
                                source=s3_node_id, target=lid,
                                edge_type="READS_S3",
                            ))
                    for s3_key in io.get("s3_writes", set()):
                        if not _is_valid_s3_key(s3_key):
                            continue
                        s3_node_id = f"s3:{s3_key}"
                        graph.add_node(Node(
                            id=s3_node_id, node_type="S3_ARTIFACT", label=s3_key,
                        ))
                        for lid in lambda_ids:
                            graph.add_edge(Edge(
                                source=lid, target=s3_node_id,
                                edge_type="WRITES_S3",
                            ))
                except (ImportError, Exception):
                    pass  # supplemental scan failure must not break the build
