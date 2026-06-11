"""
Pipeline DAG extractor -- authoritative input/output mapping for gold scripts.

Unlike extract_s3.py (regex heuristics), this module uses two authoritative sources:
  1. lib/s3_layout.py -- every S3 key as a named Python constant
  2. gold_dispatch.sh -- execution order, chain membership, catalog

For each gold script, it AST-parses the `from lib.s3_layout import (...)` block
to get the exact list of constants, then classifies each as INPUT or OUTPUT by
scanning the script body for read vs write usage patterns.

The result is a complete pipeline DAG:
  script -[READS]-> S3_key -[WRITTEN_BY]-> script

Zero API calls. Deterministic.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path
from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class S3Key:
    """An S3 key or prefix from s3_layout.py."""
    constant_name: str        # Python constant name (e.g., ACCOUNTS_DIMENSION)
    s3_path: str              # Resolved S3 key (e.g., gold/dimensions/accounts_dimension_latest.parquet)
    is_prefix: bool = False   # True if this is a prefix (ends with /) not a single file
    is_function: bool = False # True if this is a key-generating function, not a constant


@dataclass
class ScriptIO:
    """Input/output manifest for one gold script."""
    script_id: str            # e.g., D_00
    filename: str             # e.g., D_00.portal_aggregates.py
    file_path: str            # relative path from workspace root
    group: str = ""           # A, B, C, D
    run_order: int = -1       # position in chain
    reads: list[str] = field(default_factory=list)   # constant names this script reads
    writes: list[str] = field(default_factory=list)  # constant names this script writes
    read_keys: list[str] = field(default_factory=list)   # resolved S3 keys read
    write_keys: list[str] = field(default_factory=list)  # resolved S3 keys written
    # FUNC keys that appear in both reads and writes: likely rolling-window prior-run reads.
    # Removed from read_keys/reads to avoid false circular-dep edges; surfaced as warnings.
    rolling_window_candidates: list[str] = field(default_factory=list)
    # Pipeline label: [bd-gold], [inf-gold], [bd-silver], [inf-silver], [bronze]
    pipeline: str = "bd-gold"


@dataclass
class PipelineDAG:
    """The complete pipeline dependency graph."""
    pipeline: str = "bd-gold"                                     # which firm/tier this DAG is
    scripts: dict[str, ScriptIO] = field(default_factory=dict)    # script_id -> ScriptIO
    s3_keys: dict[str, S3Key] = field(default_factory=dict)       # constant_name -> S3Key
    chains: dict[str, list[str]] = field(default_factory=dict)    # chain_name -> [script_ids]
    groups: dict[str, list[str]] = field(default_factory=dict)    # group_letter -> [script_ids]
    catalog: dict[str, str] = field(default_factory=dict)         # script_id -> filename

    # Derived: which script writes each S3 key
    _writers: dict[str, list[str]] = field(default_factory=dict)  # s3_key -> [script_ids]
    _readers: dict[str, list[str]] = field(default_factory=dict)  # s3_key -> [script_ids]
    # Implicit edges: FUNC-write resolved prefix -> [script_ids that write to it via FUNC key]
    # These cross-reference PREFIX reads against FUNC writes (GAP 2 fix).
    _implicit_writers: dict[str, list[str]] = field(default_factory=dict)

    def build_index(self):
        """Build writer/reader indexes from script manifests."""
        self._writers.clear()
        self._readers.clear()
        self._implicit_writers.clear()
        for sid, sio in self.scripts.items():
            for key in sio.write_keys:
                self._writers.setdefault(key, []).append(sid)
            for key in sio.read_keys:
                self._readers.setdefault(key, []).append(sid)

        # GAP 2: cross-reference FUNC-write resolved prefixes against PREFIX reads.
        # When script A writes positions_cube_key -> 'gold/.../positions_cube/{*}.parquet'
        # and script B reads POSITIONS_CUBE_PREFIX -> 'gold/.../positions_cube/',
        # the literal prefix of the FUNC template matches the PREFIX constant.
        # Emit an implicit edge: A -> B.
        for writer_sid, writer_sio in self.scripts.items():
            for const in writer_sio.writes:
                sk = self.s3_keys.get(const)
                if not (sk and sk.is_function and '{*}' in sk.s3_path):
                    continue
                literal_prefix = sk.s3_path.split('{*}')[0]
                if not literal_prefix.endswith('/'):
                    continue
                for reader_sid, reader_sio in self.scripts.items():
                    if reader_sid == writer_sid:
                        continue
                    for r_const in reader_sio.reads:
                        r_sk = self.s3_keys.get(r_const)
                        if r_sk and r_sk.is_prefix and r_sk.s3_path == literal_prefix:
                            writers_list = self._implicit_writers.setdefault(literal_prefix, [])
                            if writer_sid not in writers_list:
                                writers_list.append(writer_sid)

    def feeds(self, script_id: str) -> list[tuple[str, str, str]]:
        """What scripts feed this one? Returns [(upstream_script, s3_key, constant)]."""
        sio = self.scripts.get(script_id)
        if not sio:
            return []
        result = []
        for key in sio.read_keys:
            for writer in self._writers.get(key, []):
                if writer != script_id:
                    # Find constant name for this key
                    const = next((c for c, sk in self.s3_keys.items()
                                  if sk.s3_path == key), key)
                    result.append((writer, key, const))
        return sorted(set(result))

    def consumers(self, script_id: str) -> list[tuple[str, str, str]]:
        """What scripts consume this one's output? Returns [(downstream_script, s3_key, constant)]."""
        sio = self.scripts.get(script_id)
        if not sio:
            return []
        result = []
        for key in sio.write_keys:
            for reader in self._readers.get(key, []):
                if reader != script_id:
                    const = next((c for c, sk in self.s3_keys.items()
                                  if sk.s3_path == key), key)
                    result.append((reader, key, const))
        return sorted(set(result))

    def overlap(self, script_a: str, script_b: str) -> dict[str, list[str]]:
        """Shared S3 artifacts between two scripts. Returns {relationship: [keys]}."""
        a = self.scripts.get(script_a)
        b = self.scripts.get(script_b)
        if not a or not b:
            return {}
        result = {}
        shared_reads = set(a.read_keys) & set(b.read_keys)
        if shared_reads:
            result['both_read'] = sorted(shared_reads)
        a_writes_b_reads = set(a.write_keys) & set(b.read_keys)
        if a_writes_b_reads:
            result[f'{script_a}_writes_{script_b}_reads'] = sorted(a_writes_b_reads)
        b_writes_a_reads = set(b.write_keys) & set(a.read_keys)
        if b_writes_a_reads:
            result[f'{script_b}_writes_{script_a}_reads'] = sorted(b_writes_a_reads)
        return result


# ---------------------------------------------------------------------------
# Step 1: Parse s3_layout.py into constant->key map
# ---------------------------------------------------------------------------

def _parse_s3_layout(gold_dir: Path) -> dict[str, S3Key]:
    """Parse lib/s3_layout.py using AST to extract all constant assignments and
    key-generating functions."""
    layout_file = gold_dir / "lib" / "s3_layout.py"
    if not layout_file.exists():
        return {}

    content = layout_file.read_text(encoding="utf-8", errors="replace")
    keys: dict[str, S3Key] = {}

    try:
        tree = ast.parse(content)
    except SyntaxError:
        return {}

    for node in ast.walk(tree):
        # Constants: ACCOUNTS_DIMENSION = 'gold/dimensions/accounts_dimension_latest.parquet'
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and isinstance(node.value, ast.Constant):
                    name = target.id
                    value = node.value.value
                    if isinstance(value, str) and '/' in value and name.isupper():
                        is_prefix = value.endswith('/')
                        keys[name] = S3Key(
                            constant_name=name,
                            s3_path=value,
                            is_prefix=is_prefix,
                        )

        # Functions: def advisor_book_key(advisor_id: str) -> str:
        #                return f'gold/entities/advisors/{advisor_id}/book.json'
        if isinstance(node, ast.FunctionDef):
            fname = node.name
            # Skip legacy_ functions and internal helpers
            if fname.startswith('legacy_') or fname.startswith('_'):
                continue
            # Extract the f-string template from the return statement
            for child in ast.walk(node):
                if isinstance(child, ast.Return) and child.value:
                    template = _extract_fstring_template(child.value)
                    if template and '/' in template:
                        keys[fname] = S3Key(
                            constant_name=fname,
                            s3_path=template,
                            is_prefix=False,
                            is_function=True,
                        )
                        break

    return keys


def _extract_fstring_template(node: ast.expr) -> str | None:
    """Extract a path template from an AST expression (f-string or string)."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        # f-string: reconstruct with {*} placeholders
        parts = []
        for val in node.values:
            if isinstance(val, ast.Constant):
                parts.append(str(val.value))
            else:
                parts.append('{*}')
        return ''.join(parts)
    return None


# ---------------------------------------------------------------------------
# Step 2: Parse gold_dispatch.sh for chains, groups, catalog
# ---------------------------------------------------------------------------

def _parse_dispatch(gold_dir: Path) -> tuple[dict[str, list[str]], dict[str, list[str]], dict[str, str]]:
    """Parse gold_dispatch.sh for chain definitions, groups, and catalog.
    Returns (chains, groups, catalog)."""
    dispatch_file = gold_dir / "gold_dispatch.sh"
    if not dispatch_file.exists():
        return {}, {}, {}

    content = dispatch_file.read_text(encoding="utf-8", errors="replace")

    chains: dict[str, list[str]] = {}
    groups: dict[str, list[str]] = {}
    catalog: dict[str, str] = {}

    # Parse CHAIN_* definitions: CHAIN_FOUNDATION="A_00 A_01 A_02 ..."
    for m in re.finditer(r'CHAIN_(\w+)="([^"]*)"', content):
        chain_name = m.group(1).lower()
        script_ids = m.group(2).strip().split()
        # Resolve variable references like $CHAIN_FOUNDATION
        resolved = []
        for sid in script_ids:
            if sid.startswith('$CHAIN_'):
                ref_name = sid.replace('$', '').replace('CHAIN_', '').lower()
                resolved.extend(chains.get(ref_name, []))
            else:
                resolved.append(sid)
        chains[chain_name] = resolved

    # Parse GROUP_* definitions: GROUP_A="A_00 A_01 ..."
    for m in re.finditer(r'GROUP_(\w)="([^"]*)"', content):
        groups[m.group(1)] = m.group(2).strip().split()

    # Parse CATALOG (heredoc block)
    catalog_match = re.search(
        r"read -r -d '' CATALOG << 'CATALOG_END'(.*?)CATALOG_END",
        content, re.DOTALL
    )
    if catalog_match:
        for line in catalog_match.group(1).strip().splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('|')
            if len(parts) >= 2:
                catalog[parts[0]] = parts[1]

    return chains, groups, catalog


# ---------------------------------------------------------------------------
# Step 3: For each script, parse s3_layout imports + classify as read/write
# ---------------------------------------------------------------------------

# Approach: scan each line for direct usage patterns. A constant on a line
# with a write-style call is a write; with a read-style call is a read.
# This avoids cross-function regex bleed that plagued the old approach.

# Write-side function/method names (constant appears as argument)
_WRITE_CALLEES = {
    'put_object', 'upload_file', '_save_json', 'upload_json', 'save_to_s3',
    '_upload_artifact', '_save_parquet', '_write', 'save_dimension',
    '_upload_parquet', '_put_json', '_put_parquet',
}

# Read-side function/method names
_READ_CALLEES = {
    'get_object', '_load_parquet', '_read_parquet_from_s3', '_read_s3',
    'load_json', '_load_json', 'read_from_s3', '_download_artifact',
    'get_json', 'read_parquet', '_load', '_read',
}


def _find_aliases(const_name: str, content: str) -> set[str]:
    """Find local variable aliases for a constant.
    Matches patterns like: output_key = CONSTANT  or  key = CONSTANT"""
    aliases = {const_name}
    esc = re.escape(const_name)
    for m in re.finditer(rf'(\w+)\s*=\s*{esc}\b', content):
        alias = m.group(1)
        # Skip self-assignment and non-variable patterns
        if alias != const_name and alias.islower() and not alias.startswith('_'):
            aliases.add(alias)
    return aliases


_COLLAPSE_FUNC_RE = re.compile(
    r'(?:put_object|get_object|upload_file|_write|_save_json|items\.append|batch\.append|writes\.append)\s*\('
)


def _collapse_multiline_calls(content: str) -> str:
    """Collapse multi-line function calls into single lines for pattern matching.

    Handles both forms:
        s3.put_object(                              # open paren at end of line
            Bucket=S3_BUCKET, Key=CONSTANT, ...
        )
        s3.put_object(Bucket=S3_BUCKET,            # args start on same line (GAP 1 fix)
                      Key=func_call(date_str), ...
        )

    Uses paren-depth tracking so the call is collapsed regardless of where args start.
    """
    lines = content.splitlines()
    collapsed = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if _COLLAPSE_FUNC_RE.search(line):
            depth = line.count('(') - line.count(')')
            if depth > 0:
                merged = line.rstrip()
                j = i + 1
                while j < len(lines) and depth > 0:
                    cont = lines[j].strip()
                    depth += cont.count('(') - cont.count(')')
                    merged += ' ' + cont
                    j += 1
                collapsed.append(merged)
                i = j
                continue
        collapsed.append(line)
        i += 1
    return '\n'.join(collapsed)


def _classify_constant(const_name: str, content: str) -> str:
    """Classify a constant as 'read', 'write', or 'both' based on line-level
    co-occurrence with known read/write function calls."""
    is_read = False
    is_write = False

    # Pre-process: collapse multi-line s3 calls into single lines
    content_collapsed = _collapse_multiline_calls(content)

    # Find aliases (e.g., output_key = ACCOUNTS_DIMENSION)
    aliases = _find_aliases(const_name, content_collapsed)

    for line in content_collapsed.splitlines():
        # Check if any alias appears on this line
        if not any(a in line for a in aliases):
            continue
        # Skip import lines and comments
        stripped = line.strip()
        if stripped.startswith(('#', 'from ', 'import ')):
            continue

        # Check write callees on this line (for any alias)
        for callee in _WRITE_CALLEES:
            if callee in line and re.search(rf'{callee}\s*\(', line):
                is_write = True
                break

        # Check read callees on this line
        for callee in _READ_CALLEES:
            if callee in line and re.search(rf'{callee}\s*\(', line):
                is_read = True
                break

        # pool.submit(_load_parquet, CONSTANT, ...) -- read via executor
        for alias in aliases:
            a_esc = re.escape(alias)
            if re.search(rf'submit\s*\(\s*_load_parquet\b.*{a_esc}', line):
                is_read = True
            if re.search(r'submit\s*\(\s*_read', line) and alias in line:
                is_read = True

            # pool.submit(_save_json, ..., CONSTANT) or submit(_upload, ..., CONSTANT)
            if re.search(r'submit\s*\(\s*(?:_save_json|_upload|upload_json|_write)', line) and alias in line:
                is_write = True

            # Key= in put_object context on same line
            if 'put_object' in line and re.search(rf'Key\s*=\s*{a_esc}\b', line):
                is_write = True
            if 'upload_file' in line and alias in line:
                is_write = True
            # Key= in get_object context on same line
            if 'get_object' in line and re.search(rf'Key\s*=\s*{a_esc}\b', line):
                is_read = True

            # Prefix= in paginator context (listing objects = read)
            if 'Prefix' in line and re.search(rf'Prefix\s*=\s*{a_esc}\b', line):
                is_read = True

            # f-string key construction
            if 'put_object' in line and f'{{{alias}}}' in line:
                is_write = True
            if 'get_object' in line and f'{{{alias}}}' in line:
                is_read = True

    # PREFIX constants that weren't matched are almost always reads
    # (used in list_objects pagination)
    if const_name.endswith('_PREFIX') and not is_write and not is_read:
        is_read = True

    if is_read and is_write:
        return 'both'
    if is_write:
        return 'write'
    if is_read:
        return 'read'
    return 'unknown'


def _classify_function_usage(func_name: str, content: str) -> str:
    """Classify a key-generating function as 'read', 'write', or 'both'.
    Handles both direct usage (put_object(Key=func_name(...))) and
    aliased usage (key = func_name(...); put_object(Key=key))."""
    is_read = False
    is_write = False
    esc = re.escape(func_name)
    call_pattern = rf'{esc}\s*\('

    # Pre-process: collapse multiline calls
    content_collapsed = _collapse_multiline_calls(content)

    # Find aliases: var = func_name(...) -> track var as write/read proxy
    func_aliases: set[str] = set()
    for m in re.finditer(rf'(\w+)\s*=\s*{esc}\s*\(', content_collapsed):
        alias = m.group(1)
        if alias.islower() and len(alias) < 20:
            func_aliases.add(alias)

    for line in content_collapsed.splitlines():
        stripped = line.strip()
        if stripped.startswith(('#', 'from ', 'import ', 'def ')):
            continue

        # Direct usage: func_name(...) on a line with a write/read call
        if func_name in line and re.search(call_pattern, line):
            if 'put_object' in line:
                is_write = True
            if 'get_object' in line:
                is_read = True
            for callee in _WRITE_CALLEES:
                if callee in line and re.search(rf'{callee}\s*\(', line):
                    is_write = True
                    break
            for callee in _READ_CALLEES:
                if callee in line and re.search(rf'{callee}\s*\(', line):
                    is_read = True
                    break
            if re.search(r'submit\s*\(\s*(?:_save|_upload|upload|_write)', line):
                is_write = True
            if re.search(r'submit\s*\(\s*(?:_load|_read|read)', line):
                is_read = True

        # Aliased usage: var was assigned from func_name(), now used in Key=var
        for alias in func_aliases:
            if alias not in line:
                continue
            a_esc = re.escape(alias)
            if 'put_object' in line and re.search(rf'Key\s*=\s*{a_esc}\b', line):
                is_write = True
            if 'upload_file' in line and alias in line:
                is_write = True
            if 'get_object' in line and re.search(rf'Key\s*=\s*{a_esc}\b', line):
                is_read = True

    if is_read and is_write:
        return 'both'
    if is_write:
        return 'write'
    if is_read:
        return 'read'
    return 'unknown'


# Known S3 path prefixes that indicate a hardcoded S3 key
_S3_PATH_PREFIXES = ('platinum/', 'gold/', 'silver/', 'bronze/')

# Write context: functions/patterns that indicate a string is being written to S3.
# Covers both BD-style (put_object, _write_batch) and INF-style (_write_json_s3, _write_s3).
_HARDCODED_WRITE_CONTEXT = re.compile(
    r'_write_batch|put_object|upload_file|_save_json|upload_json|'
    r'items\.append|batch\.append|writes\.append|'
    r'_write_json_s3|_write_s3|_write_parquet_s3|_put_object'
)

# Read context: functions/patterns that indicate a string is being read from S3.
# Covers both BD-style and INF-style (_read_s3, _read_s3_parquet).
_HARDCODED_READ_CONTEXT = re.compile(
    r'get_object|_load_parquet|_read_parquet|load_json|_load_json|'
    r'read_parquet|_download|_read_s3|Prefix\s*='
)


def _extract_module_s3_constants(content: str) -> dict[str, str]:
    """Scan module-level uppercase constant assignments for S3 path strings.

    Detects patterns like:
        CLIENT_PERF_KEY = 'gold/timeseries/client_performance.parquet'
        TIMESERIES_CHART_KEY = 'gold/artifacts/timeseries_chart.json'

    Returns {CONSTANT_NAME: s3_path} for all module-level uppercase S3 constants.
    Used to resolve INF-style scripts where keys are assigned once then passed
    as variables to _write_json_s3(obj, KEY_CONST) or _read_s3(KEY_CONST) calls.
    """
    constants: dict[str, str] = {}
    # Match: UPPERCASE_NAME = 'gold/...' or "gold/..."  (only top-level, indented=0)
    const_re = re.compile(
        r'^([A-Z][A-Z0-9_]+)\s*=\s*[\'"]((platinum|gold|silver|bronze)/[^\'"]+\.(?:json|parquet|csv))[\'"]',
        re.MULTILINE,
    )
    for m in const_re.finditer(content):
        constants[m.group(1)] = m.group(2)
    return constants


def _extract_s3_calls_with_constants(
    content: str,
    module_constants: dict[str, str],
) -> tuple[list[str], list[str]]:
    """Detect S3 reads/writes where the key is a module-level constant variable
    (not a string literal on the call line).

    Handles:
        _write_json_s3(obj, TIMESERIES_CHART_KEY)
        _read_s3(CLIENT_PERF_KEY)
        s3.put_object(Bucket=S3_BUCKET, Key=CANONICAL_NNA_PREFIX, ...)
        resp = s3.get_object(Bucket=S3_BUCKET, Key=SOME_KEY)

    Returns (read_paths, write_paths).
    """
    reads: list[str] = []
    writes: list[str] = []

    # Pattern: _write_json_s3(anything, CONST) or _write_s3(anything, CONST)
    write_var_re = re.compile(
        r'(?:_write_json_s3|_write_s3|_write_parquet_s3|_put_object)\s*\([^)]*?([A-Z][A-Z0-9_]+)\s*[,)]'
    )
    # Pattern: _read_s3(CONST) or _read_s3_parquet(CONST) or _read_s3_json(CONST)
    read_var_re = re.compile(
        r'(?:_read_s3|_read_s3_parquet|_read_s3_json|_load_s3)\s*\(\s*([A-Z][A-Z0-9_]+)\s*[,)]'
    )
    # Pattern: Key=CONST in put_object / get_object
    put_key_re = re.compile(r'put_object\s*\([^)]*Key\s*=\s*([A-Z][A-Z0-9_]+)')
    get_key_re = re.compile(r'get_object\s*\([^)]*Key\s*=\s*([A-Z][A-Z0-9_]+)')
    # Pattern: Prefix=CONST in list_objects
    prefix_re = re.compile(r'Prefix\s*=\s*([A-Z][A-Z0-9_]+)')

    content_collapsed = _collapse_multiline_calls(content)

    for line in content_collapsed.splitlines():
        stripped = line.strip()
        if stripped.startswith(('#', 'def ', 'class ', '"""', "'''")):
            continue
        for m in write_var_re.finditer(line):
            const = m.group(1)
            if const in module_constants:
                path = module_constants[const]
                if path not in writes:
                    writes.append(path)
        for m in put_key_re.finditer(line):
            const = m.group(1)
            if const in module_constants:
                path = module_constants[const]
                if path not in writes:
                    writes.append(path)
        for m in read_var_re.finditer(line):
            const = m.group(1)
            if const in module_constants:
                path = module_constants[const]
                if path not in reads:
                    reads.append(path)
        for m in get_key_re.finditer(line):
            const = m.group(1)
            if const in module_constants:
                path = module_constants[const]
                if path not in reads:
                    reads.append(path)
        for m in prefix_re.finditer(line):
            const = m.group(1)
            if const in module_constants:
                path = module_constants[const]
                if path not in reads:
                    reads.append(path)

    return sorted(reads), sorted(writes)


def _extract_hardcoded_paths(content: str) -> tuple[list[str], list[str]]:
    """Scan for hardcoded S3 paths in string literals and f-strings.

    Returns (read_paths, write_paths) with parameterized f-string vars
    replaced by {*} (e.g., f'platinum/clients/{rid}/summary.json' -> 'platinum/clients/{*}/summary.json').
    """
    reads: set[str] = set()
    writes: set[str] = set()

    content_collapsed = _collapse_multiline_calls(content)

    for line in content_collapsed.splitlines():
        stripped = line.strip()
        if stripped.startswith(('#', 'from ', 'import ', 'def ', '"""', "'''")):
            continue

        # Find string literals: 'platinum/...' or "platinum/..."
        for m in re.finditer(r"""['"]((platinum|gold|silver|bronze)/[^'"]+\.(?:json|parquet|csv))['"]""", line):
            path = m.group(1)
            if _HARDCODED_WRITE_CONTEXT.search(line):
                writes.add(path)
            elif _HARDCODED_READ_CONTEXT.search(line):
                reads.add(path)

        # Find f-string literals: f'platinum/clients/{rid}/summary.json'
        for m in re.finditer(r"""f['"]((platinum|gold|silver|bronze)/[^'"]+\.(?:json|parquet|csv))['"]""", line):
            raw_path = m.group(1)
            # Replace {variable} with {*} for parameterized paths
            normalized = re.sub(r'\{[^}]+\}', '{*}', raw_path)
            if _HARDCODED_WRITE_CONTEXT.search(line):
                writes.add(normalized)
            elif _HARDCODED_READ_CONTEXT.search(line):
                reads.add(normalized)

    # Pass 2 (firm-trace fix 2026-06-11): VARIABLE-mediated writes/reads. The inf D-tier
    # portal scripts assign a path literal to a var (`KEY = 'platinum/...'` / `key = f'platinum/
    # advisors/{id}/book.json'`) then write it via a helper on a LATER line (`_write_json_s3(obj,
    # KEY)`) -- literal and verb on different lines, so the single-line check above misses them.
    # Build var->path, then attribute by where the var is used in a write/read context. Additive
    # only (never removes); bd is unaffected (it resolves via s3_layout imports, not this path).
    _assign_re = re.compile(
        r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*f?['\"]"
        r"((?:platinum|gold|silver|bronze)/[^'\"]+\.(?:json|parquet|csv))['\"]")
    _ident_re = re.compile(r'\b([A-Za-z_][A-Za-z0-9_]*)\b')
    # Pass 2b (prefix-var fix 2026-06-11): the inf D-tier portal scripts compose write keys from a
    # tier-rooted PREFIX var concatenated to a suffix via f-string -- the prefix itself comes from
    # `OUTPUT_PREFIX = os.environ.get('OUTPUT_PREFIX', 'platinum/')...` (env-default) or a plain
    # literal `CANONICAL_NNA_PREFIX = 'gold/canonical/'`, then `KEY = f'{OUTPUT_PREFIX}firm/x.json'`
    # or a direct `_write_json_s3(o, f'{OUTPUT_PREFIX}firm/x.json')`. The f-string STARTS with the
    # `{PREFIX_VAR}` interpolation (not a literal tier), so the single-line + Pass-2 literal scans
    # both miss it. Resolve PREFIX_VAR -> its tier value, substitute, and the full key falls out.
    # This is what surfaces INF_D_04's platinum/firm/timeseries_overview.json + the gold/artifacts/
    # summary/header_metrics.json writes (and also closes the comp-platinum --firm inf producer gap).
    _prefix_env_re = re.compile(
        r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*os\.environ\.get\([^,]+,\s*['\"]"
        r"((?:platinum|gold|silver|bronze)/[^'\"]*)['\"]")
    _prefix_lit_re = re.compile(
        r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*['\"]"
        r"((?:platinum|gold|silver|bronze)/[^'\"]*/)['\"]\s*(?:#.*)?$")
    _fstr_prefixed_assign_re = re.compile(
        r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*f['\"]\{([A-Za-z_][A-Za-z0-9_]*)\}"
        r"([^'\"]+\.(?:json|parquet|csv))['\"]")
    _fstr_prefixed_re = re.compile(
        r"f['\"]\{([A-Za-z_][A-Za-z0-9_]*)\}([^'\"]+\.(?:json|parquet|csv))['\"]")
    # Sequential walk: track each var's CURRENT path value as assignments happen, so a reused var
    # (e.g. `key` set to book.json then later detail.json) attributes the value live at each use.
    cur: dict[str, str] = {}
    prefixes: dict[str, str] = {}

    def _resolve_prefixed(pvar: str, suffix: str):
        base = prefixes.get(pvar)
        if base is None:
            return None
        return re.sub(r'\{[^}]+\}', '{*}', base + suffix)

    for line in content_collapsed.splitlines():
        pe = _prefix_env_re.match(line)
        if pe:
            prefixes[pe.group(1)] = pe.group(2).rstrip('/') + '/'
            continue
        pl = _prefix_lit_re.match(line)
        if pl:
            prefixes[pl.group(1)] = pl.group(2)
            continue
        pf = _fstr_prefixed_assign_re.match(line)
        if pf:
            resolved = _resolve_prefixed(pf.group(2), pf.group(3))
            if resolved:
                cur[pf.group(1)] = resolved
                continue
        am = _assign_re.match(line)
        if am:
            cur[am.group(1)] = re.sub(r'\{[^}]+\}', '{*}', am.group(2))
            continue
        wc = _HARDCODED_WRITE_CONTEXT.search(line)
        rc = _HARDCODED_READ_CONTEXT.search(line)
        if not (wc or rc):
            continue
        # direct prefixed f-string on the verb line: _write_json_s3(o, f'{OUTPUT_PREFIX}firm/x.json')
        for dm in _fstr_prefixed_re.finditer(line):
            resolved = _resolve_prefixed(dm.group(1), dm.group(2))
            if resolved:
                (writes if wc else reads).add(resolved)
        for um in _ident_re.finditer(line):
            p = cur.get(um.group(1))
            if not p:
                continue
            if wc:
                writes.add(p)
            elif rc:
                reads.add(p)

    # Deduplicate: if we have both 'platinum/clients/{*}/summary.json' (from f-string)
    # and the same path from a plain string, keep only the {*} version.
    # Also remove any path that is a subset of a {*} parameterized path.
    def _dedup_paths(paths: set[str]) -> set[str]:
        parameterized = {p for p in paths if '{*}' in p}
        result = set(parameterized)
        for p in paths:
            if '{*}' in p:
                continue
            # Check if this literal path matches any parameterized pattern
            matched = False
            for pp in parameterized:
                pattern = re.escape(pp).replace(r'\{\*\}', '[^/]+')
                if re.fullmatch(pattern, p):
                    matched = True
                    break
            if not matched:
                result.add(p)
        return result

    reads = _dedup_paths(reads)
    writes = _dedup_paths(writes)

    return sorted(reads), sorted(writes)


def _extract_dynamic_refs(content: str) -> list[str]:
    """Scan for non-constant S3 read patterns that aren't tracked via s3_layout.py.

    Detects:
    - pandas read_parquet/read_csv with s3:// URIs
    - s3.get_object / s3_client.get_object with f-string keys containing variables
    - Direct s3:// URI strings in any context

    Returns list of path templates (variables replaced with {*}).
    These are emitted as S3-DYNAMIC annotations in comp-pipescript io output.
    """
    dynamic: set[str] = set()

    content_collapsed = _collapse_multiline_calls(content)

    for line in content_collapsed.splitlines():
        stripped = line.strip()
        if stripped.startswith(('#', 'from ', 'import ')):
            continue

        # pandas: pd.read_parquet('s3://bucket/path') or pd.read_csv(f's3://...')
        for m in re.finditer(r"""(?:read_parquet|read_csv|read_json)\s*\(\s*f?['"]s3://[^/'"]+/([^'"]+)['"]""", line):
            path = m.group(1)
            normalized = re.sub(r'\{[^}]+\}', '{*}', path)
            dynamic.add(normalized)

        # s3.get_object with f-string Key containing variables
        # e.g.: s3.get_object(Bucket='opal-data-bd', Key=f'gold/dimensions/{name}.csv')
        for m in re.finditer(r"""get_object\s*\([^)]*Key\s*=\s*f['"]((platinum|gold|silver|bronze)/[^'"]+)['"]""", line):
            path = m.group(1)
            normalized = re.sub(r'\{[^}]+\}', '{*}', path)
            # Only include if it has a variable (otherwise extract_hardcoded_paths handles it)
            if '{*}' in normalized:
                dynamic.add(normalized)

        # Any s3:// URI with gold/silver/bronze/platinum prefix in any context
        for m in re.finditer(r"""s3://[^/'"]+/((platinum|gold|silver|bronze)/[^/'"*\s]+(?:/[^/'"*\s]+)*)""", line):
            path = m.group(1)
            if not path.endswith(('.json', '.parquet', '.csv', '/')):
                continue
            normalized = re.sub(r'\{[^}]+\}', '{*}', path)
            dynamic.add(normalized)

    return sorted(dynamic)


def _extract_script_io(
    py_file: Path,
    workspace_root: Path,
    s3_keys: dict[str, S3Key],
    script_id_override: str | None = None,
    pipeline: str = "bd-gold",
    run_order_override: int = -1,
) -> ScriptIO | None:
    """Parse a gold script's s3_layout imports and classify each as read/write.

    script_id_override: use this ID instead of deriving from filename (for INF/silver scripts
    whose naming doesn't match the BD [A-Z]_NN pattern).
    pipeline: label for this script's pipeline ([bd-gold], [inf-gold], [bd-silver], etc.).
    run_order_override: explicit run order when chain position is known (e.g. INF dispatch order).
    """
    try:
        content = py_file.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None

    rel_path = str(py_file.relative_to(workspace_root)).replace("\\", "/")

    if script_id_override is not None:
        script_id = script_id_override
        # Derive group from first letter if it looks like [A-Z]_NN, else use pipeline prefix
        g_match = re.match(r'^([A-Z])_', script_id)
        group = g_match.group(1) if g_match else script_id[0].upper() if script_id else ""
        run_order = run_order_override
    else:
        # Extract script ID from filename: D_00.portal_aggregates.py -> D_00
        stem = py_file.stem
        match = re.match(r'^([A-Z]_\d{2}[a-z]?)', stem)
        if not match:
            return None
        script_id = match.group(1)
        group = script_id[0]
        order_letter = (ord(group) - ord('A')) * 100
        order_num = int(re.search(r'_(\d{2})', script_id).group(1))
        run_order = order_letter + order_num

    sio = ScriptIO(
        script_id=script_id,
        filename=py_file.name,
        file_path=rel_path,
        group=group,
        run_order=run_order,
        pipeline=pipeline,
    )

    # AST-parse imports from lib.s3_layout
    try:
        tree = ast.parse(content)
    except SyntaxError:
        return sio

    imported_names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module and 's3_layout' in node.module:
                for alias in node.names:
                    imported_names.append(alias.name)

    # Classify each imported name
    for name in imported_names:
        # Skip LEGACY dict and non-key imports
        if name == 'LEGACY':
            continue

        s3_key_info = s3_keys.get(name)
        if not s3_key_info:
            continue

        if s3_key_info.is_function:
            classification = _classify_function_usage(name, content)
        else:
            classification = _classify_constant(name, content)

        if classification in ('read', 'both'):
            sio.reads.append(name)
            sio.read_keys.append(s3_key_info.s3_path)
        if classification in ('write', 'both'):
            sio.writes.append(name)
            sio.write_keys.append(s3_key_info.s3_path)
        if classification == 'unknown':
            # Default: if it's a PREFIX, assume read; otherwise assume read
            # (safer to over-report reads than miss them)
            sio.reads.append(name)
            sio.read_keys.append(s3_key_info.s3_path)

    # Step 2: Scan for hardcoded string S3 paths (not from s3_layout)
    # Catches writes like: _write_batch([(data, 'platinum/firm/dashboard.json')], ...)
    # and: items.append((data, f'platinum/clients/{rid}/summary.json'))
    hardcoded_reads, hardcoded_writes = _extract_hardcoded_paths(content)
    for path in hardcoded_writes:
        hc_name = f"[hardcoded] {path}"
        if hc_name not in sio.writes:
            sio.writes.append(hc_name)
        if path not in sio.write_keys:
            sio.write_keys.append(path)
    for path in hardcoded_reads:
        hc_name = f"[hardcoded] {path}"
        if hc_name not in sio.reads:
            sio.reads.append(hc_name)
        if path not in sio.read_keys:
            sio.read_keys.append(path)

    # Step 3: For non-s3_layout scripts (e.g. INF gold, silver), resolve module-level
    # S3 constant variables passed to read/write functions.
    # Catches: _write_json_s3(obj, TIMESERIES_CHART_KEY) where key is a module constant.
    if not imported_names:
        module_consts = _extract_module_s3_constants(content)
        if module_consts:
            const_reads, const_writes = _extract_s3_calls_with_constants(content, module_consts)
            for path in const_writes:
                hc_name = f"[hardcoded] {path}"
                if hc_name not in sio.writes:
                    sio.writes.append(hc_name)
                if path not in sio.write_keys:
                    sio.write_keys.append(path)
            for path in const_reads:
                hc_name = f"[hardcoded] {path}"
                if hc_name not in sio.reads:
                    sio.reads.append(hc_name)
                if path not in sio.read_keys:
                    sio.read_keys.append(path)

    # Deduplicate
    sio.reads = sorted(set(sio.reads))
    sio.writes = sorted(set(sio.writes))
    sio.read_keys = sorted(set(sio.read_keys))
    sio.write_keys = sorted(set(sio.write_keys))

    # GAP 3: Rolling-window candidate detection.
    # If a FUNC key appears in BOTH reads and writes for the same script, surface it
    # as a rolling_window_candidate so cmd_io can emit a WARNING.
    # The key is NOT removed from reads here — that would break the _readers index
    # (e.g., D_04 genuinely reads partner_analytics_key but also has a false-write due
    # to alias collision; removing from reads would drop D_04 from D_01's consumer list).
    # Rolling-window detection is display-only: the graph edges remain intact so that
    # comp-pipescript consumers/feeds commands still show the correct downstream scripts.
    writes_set = set(sio.writes)
    sio.rolling_window_candidates = [
        c for c in sio.reads
        if c in writes_set and s3_keys.get(c) and s3_keys[c].is_function
    ]

    return sio


# ---------------------------------------------------------------------------
# Column gap detection: _load_parquet columns= allowlist vs actual access
# ---------------------------------------------------------------------------

def _extract_column_gaps(py_file: Path) -> list[dict]:
    """Detect cases where a script accesses a DataFrame column that was not
    included in the _load_parquet(..., columns=[...]) call that produced it.

    Returns list of dicts:
      {var, key_const, loaded_cols, accessed_col, load_line, access_line}

    Only fires for _load_parquet calls with an explicit columns=[...] list
    (not variables like columns=SOME_LIST). Dynamic column lists are skipped.
    """
    import ast as _ast

    try:
        content = py_file.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    # DataFrame method/attribute names to exclude from column access detection
    _DF_METHODS = {
        'columns', 'index', 'shape', 'dtypes', 'empty', 'values', 'T',
        'iterrows', 'itertuples', 'to_dict', 'to_json', 'to_parquet', 'to_csv',
        'groupby', 'sort_values', 'sort_index', 'reset_index', 'set_index',
        'rename', 'merge', 'join', 'concat', 'drop', 'fillna', 'dropna',
        'copy', 'head', 'tail', 'loc', 'iloc', 'at', 'iat', 'apply', 'map',
        'astype', 'describe', 'info', 'count', 'sum', 'mean', 'max', 'min',
        'nunique', 'unique', 'value_counts', 'isnull', 'notnull', 'notna',
        'isna', 'any', 'all', 'pipe', 'assign', 'query', 'filter', 'sample',
        'nlargest', 'nsmallest', 'pivot', 'melt', 'explode', 'str', 'dt',
        'cat', 'plot', 'hist', 'items', 'keys', 'get', 'pop', 'update',
    }

    gaps = []

    # Match: varname = ..._load_parquet(..., columns=['col1', 'col2', ...])
    # Also: varname = pool_result (where pool_result came from _load_parquet via submit)
    # Focus on the simplest and most common pattern first.
    load_re = re.compile(
        r'^(\s*)(\w+)\s*(?:[:,]\s*\w[\w\[\],\s]*?)?\s*=\s*'
        r'(?:\w+\.)?_load_parquet\s*\(\s*(\w+)\s*,\s*columns\s*=\s*\[([^\]]*)\]',
        re.MULTILINE,
    )

    # Also handle: fut_X = pool.submit(_load_parquet, KEY, ..., columns=[...])
    # then: varname = fut_X.result()
    submit_re = re.compile(
        r'(\w+)\s*=\s*\w+\.submit\s*\(\s*_load_parquet\s*,\s*(\w+)\s*,[^)]*columns\s*=\s*\[([^\]]*)\]',
        re.MULTILINE,
    )
    result_re = re.compile(r'(\w+)\s*=\s*(\w+)\.result\(\)')

    loads = []  # list of (var_name, key_const, loaded_cols_set, load_line)

    for m in load_re.finditer(content):
        var_name = m.group(2)
        key_const = m.group(3)
        cols_raw = m.group(4)
        load_line = content[:m.start()].count('\n') + 1
        try:
            loaded_cols = set(_ast.literal_eval(f'[{cols_raw}]'))
        except Exception:
            continue
        if loaded_cols:
            loads.append((var_name, key_const, loaded_cols, load_line))

    # Handle pool.submit pattern: fut = pool.submit(_load_parquet, KEY, columns=[...])
    # then later: var = fut.result()
    fut_to_load: dict[str, tuple] = {}
    for m in submit_re.finditer(content):
        fut_name = m.group(1)
        key_const = m.group(2)
        cols_raw = m.group(3)
        load_line = content[:m.start()].count('\n') + 1
        try:
            loaded_cols = set(_ast.literal_eval(f'[{cols_raw}]'))
        except Exception:
            continue
        if loaded_cols:
            fut_to_load[fut_name] = (key_const, loaded_cols, load_line)

    for m in result_re.finditer(content):
        var_name = m.group(1)
        fut_name = m.group(2)
        if fut_name in fut_to_load:
            key_const, loaded_cols, load_line = fut_to_load[fut_name]
            loads.append((var_name, key_const, loaded_cols, load_line))

    if not loads:
        return []

    # For each loaded variable, find column accesses
    for var_name, key_const, loaded_cols, load_line in loads:
        # Patterns for column access:
        # 1. var['col']  or  var["col"]
        bracket_re = re.compile(
            rf'\b{re.escape(var_name)}\s*\[\s*[\'"](\w+)[\'"]\s*\]'
        )
        # 2. var.col  (attribute access -- common with adim.col_name)
        attr_re = re.compile(
            rf'\b{re.escape(var_name)}\s*\.\s*([a-z]\w*)\b'
        )
        # 3. var.get('col')
        get_re = re.compile(
            rf'\b{re.escape(var_name)}\s*\.get\s*\(\s*[\'"](\w+)[\'"]'
        )

        accessed: dict[str, int] = {}  # col_name -> first access line

        for pat in (bracket_re, attr_re, get_re):
            for m in pat.finditer(content):
                col = m.group(1)
                if col in _DF_METHODS:
                    continue
                if col.startswith('_') or col[0].isupper():
                    continue  # skip private/constant names
                line = content[:m.start()].count('\n') + 1
                if line == load_line:
                    continue  # skip the load line itself
                if col not in accessed:
                    accessed[col] = line

        for col, access_line in accessed.items():
            if col not in loaded_cols:
                gaps.append({
                    'var': var_name,
                    'key_const': key_const,
                    'col': col,
                    'loaded_cols': sorted(loaded_cols),
                    'load_line': load_line,
                    'access_line': access_line,
                })

    return gaps


# ---------------------------------------------------------------------------
# Main: build the full pipeline DAG
# ---------------------------------------------------------------------------

def build_pipeline_dag(workspace_root: Path, gold_dir: Path = None,
                       pipeline: str = "bd-gold") -> PipelineDAG:
    """Build a gold pipeline DAG from authoritative sources (s3_layout.py + gold_dispatch.sh).
    Defaults to the BD-gold tree (backward-compatible). `gold_dir` override lets the same
    parser serve any firm tree that uses the s3_layout.py + gold_dispatch.sh shape (bd, cot)."""
    if gold_dir is None:
        gold_dir = workspace_root / "data" / "black_diamond" / "scripts" / "gold"
    if not gold_dir.exists():
        return PipelineDAG()

    dag = PipelineDAG()
    dag.pipeline = pipeline

    # Step 1: Parse s3_layout.py
    dag.s3_keys = _parse_s3_layout(gold_dir)

    # Step 2: Parse gold_dispatch.sh
    dag.chains, dag.groups, dag.catalog = _parse_dispatch(gold_dir)

    # Step 3: Parse each gold script
    for py_file in sorted(gold_dir.glob("[A-D]_*.py")):
        if py_file.name.startswith("__"):
            continue
        sio = _extract_script_io(py_file, workspace_root, dag.s3_keys, pipeline=pipeline)
        if sio:
            dag.scripts[sio.script_id] = sio

    # Step 4: Build indexes
    dag.build_index()

    return dag


# Firm <-> gold-tree map. Source of truth for the firm->bucket leg is the Lambda@Edge
# firm-config.mjs (FIRM_BUCKET_MAP); mirrored here for the static trace graph. Accepts both
# firm-id aliases (49financial/inflection/cottonwood) and pipeline slugs (bd/inf/cot).
FIRM_ALIAS = {"49financial": "bd", "bd": "bd", "inflection": "inf", "inf": "inf",
              "cottonwood": "cot", "cot": "cot"}
FIRM_BUCKET = {"bd": "opal-data-bd", "inf": "opal-data-inf", "cot": "opal-data-cot"}

def build_firm_gold_dag(workspace_root: Path, firm: str = "bd") -> PipelineDAG:
    """Build the gold DAG for ONE firm. The ADVI serving tree is firm-isolated: 49F->bd
    (Black Diamond), Inflection->inf (Orion API), Cottonwood->cot -- DIFFERENT gold scripts +
    buckets per firm. comp-platinum historically built only bd, silently mis-attributing inf/cot
    ADVI traces to the bd tree (firm-blind). This routes to the correct per-firm tree."""
    f = FIRM_ALIAS.get((firm or "bd").lower(), "bd")
    if f == "inf":
        return build_inf_gold_dag(workspace_root)
    if f == "cot":
        return build_pipeline_dag(workspace_root,
                                  workspace_root / "data" / "cot" / "scripts" / "gold",
                                  pipeline="cot-gold")
    return build_pipeline_dag(workspace_root)   # bd (default)


# ---------------------------------------------------------------------------
# Multi-pipeline support: INF gold, BD silver, INF silver, bronze
# ---------------------------------------------------------------------------

def _parse_orion_dispatch(gold_dir: Path) -> tuple[dict[str, list[str]], dict[str, list[str]], dict[str, str]]:
    """Parse orion-gold-dispatch.sh for chains, groups, and catalog.
    Uses the same CATALOG heredoc + CHAIN_ variable format as BD's gold_dispatch.sh.
    Returns (chains, groups, catalog)."""
    dispatch_file = gold_dir / "orion-gold-dispatch.sh"
    if not dispatch_file.exists():
        return {}, {}, {}

    content = dispatch_file.read_text(encoding="utf-8", errors="replace")

    chains: dict[str, list[str]] = {}
    groups: dict[str, list[str]] = {}
    catalog: dict[str, str] = {}

    # CHAIN_ definitions (same regex as BD)
    for m in re.finditer(r'CHAIN_(\w+)="([^"]*)"', content):
        chain_name = m.group(1).lower()
        script_ids = m.group(2).strip().split()
        resolved = []
        for sid in script_ids:
            if sid.startswith('$CHAIN_'):
                ref_name = sid.replace('$', '').replace('CHAIN_', '').lower()
                resolved.extend(chains.get(ref_name, []))
            else:
                resolved.append(sid)
        chains[chain_name] = resolved

    # CATALOG heredoc (same format: ID|filename|flags)
    catalog_match = re.search(
        r"read -r -d '' CATALOG << 'CATALOG_END'(.*?)CATALOG_END",
        content, re.DOTALL
    )
    if catalog_match:
        for line in catalog_match.group(1).strip().splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('|')
            if len(parts) >= 2:
                catalog[parts[0]] = parts[1]

    return chains, groups, catalog


def build_inf_gold_dag(workspace_root: Path) -> PipelineDAG:
    """Build the Inflection gold pipeline DAG.

    INF scripts use hardcoded S3_BUCKET = 'opal-data-inf' instead of lib.s3_layout imports.
    The dispatch catalog (orion-gold-dispatch.sh) is the authoritative source for script IDs.
    Hardcoded path detection (_extract_hardcoded_paths) covers all S3 I/O.
    """
    gold_dir = workspace_root / "data" / "inf" / "scripts" / "gold"
    if not gold_dir.exists():
        return PipelineDAG()

    dag = PipelineDAG()
    dag.pipeline = "inf-gold"
    # No s3_layout.py for INF -- hardcoded paths only
    dag.s3_keys = {}

    chains, groups, catalog = _parse_orion_dispatch(gold_dir)
    dag.chains = chains
    dag.groups = groups
    dag.catalog = catalog

    # Determine run_order from chain_full position
    full_chain = chains.get('full', [])
    order_map = {sid: idx * 10 for idx, sid in enumerate(full_chain)}

    for script_id, filename in catalog.items():
        py_file = gold_dir / filename
        if not py_file.exists():
            continue
        run_order = order_map.get(script_id, -1)
        sio = _extract_script_io(
            py_file, workspace_root, dag.s3_keys,
            script_id_override=script_id,
            pipeline="inf-gold",
            run_order_override=run_order,
        )
        if sio:
            dag.scripts[script_id] = sio

    dag.build_index()
    return dag


def build_silver_dag(
    workspace_root: Path,
    pipeline_label: str,
    script_dir_rel: str,
) -> PipelineDAG:
    """Build a silver-layer pipeline DAG by walking a script directory.

    No dispatch catalog and no s3_layout.py -- script IDs are filename stems,
    and S3 I/O is detected entirely via _extract_hardcoded_paths.

    pipeline_label: "bd-silver" or "inf-silver"
    script_dir_rel: relative path from workspace root (e.g. "data/black_diamond/scripts/silver")
    """
    script_dir = workspace_root / Path(script_dir_rel)
    if not script_dir.exists():
        return PipelineDAG()

    dag = PipelineDAG()
    dag.s3_keys = {}

    for idx, py_file in enumerate(sorted(script_dir.glob("*.py"))):
        if py_file.name.startswith("__"):
            continue
        script_id = py_file.stem
        sio = _extract_script_io(
            py_file, workspace_root, dag.s3_keys,
            script_id_override=script_id,
            pipeline=pipeline_label,
            run_order_override=idx * 10,
        )
        if sio:
            dag.scripts[script_id] = sio
            dag.catalog[script_id] = py_file.name

    dag.build_index()
    return dag


def build_inf_manual_api_dag(workspace_root: Path) -> PipelineDAG:
    """Build a DAG for Inflection manual_api scripts (Orion REST pull scripts).

    Path: data/inf/manual_api/*.py (non-recursive)
    These scripts pull from Orion REST API and write to S3 bronze; classified as
    pipeline label "inf-manual-api". I/O detection via _extract_hardcoded_paths
    (same pattern as silver scripts; no dispatch catalog).

    ADHC_COMPIL_V4.008: closes the manual_api graph-coverage gap (anchor: 12+
    NOT-INDEXED FAILs in 2-week compiler-tools-log including pull_inflection_billing_dim,
    orion_billing_dim, pull_inflection_performance_dim).
    """
    return build_silver_dag(workspace_root, "inf-manual-api", "data/inf/manual_api")


def build_multi_pipeline_dag(workspace_root: Path) -> PipelineDAG:
    """Build a combined multi-pipeline DAG covering all indexed layers:
      - bd-gold        (BD gold scripts, s3_layout-authoritative)
      - inf-gold       (INF gold scripts, hardcoded-path detection)
      - bd-silver      (BD silver scripts, hardcoded-path detection)
      - inf-silver     (INF silver scripts, hardcoded-path detection)
      - inf-manual-api (INF manual_api Orion REST pull scripts; ADHC_COMPIL_V4.008)

    Script IDs in the combined DAG are namespaced:
      bd-gold:D_04, inf-gold:D_04, bd-silver:convert_assets_to_silver,
      inf-manual-api:pull_inflection_billing_dim, etc.

    Cross-pipeline edges are built: a silver script's write_keys that overlap with
    a gold script's read_keys produce an implicit cross-layer dependency.
    """
    bd_gold = build_pipeline_dag(workspace_root)
    inf_gold = build_inf_gold_dag(workspace_root)
    bd_silver = build_silver_dag(workspace_root, "bd-silver", "data/black_diamond/scripts/silver")
    inf_silver = build_silver_dag(workspace_root, "inf-silver", "data/inf/scripts/silver")
    inf_manual_api = build_inf_manual_api_dag(workspace_root)

    merged = PipelineDAG()

    # Merge all s3_keys (BD gold has the authoritative named keys)
    merged.s3_keys.update(bd_gold.s3_keys)

    def _ns(pipeline: str, script_id: str) -> str:
        return f"{pipeline}:{script_id}"

    # Merge scripts with namespaced IDs
    for sub_dag in (bd_gold, inf_gold, bd_silver, inf_silver, inf_manual_api):
        for sid, sio in sub_dag.scripts.items():
            ns_id = _ns(sio.pipeline, sid)
            # Clone sio with namespaced script_id
            ns_sio = ScriptIO(
                script_id=ns_id,
                filename=sio.filename,
                file_path=sio.file_path,
                group=sio.group,
                run_order=sio.run_order,
                reads=list(sio.reads),
                writes=list(sio.writes),
                read_keys=list(sio.read_keys),
                write_keys=list(sio.write_keys),
                rolling_window_candidates=list(sio.rolling_window_candidates),
                pipeline=sio.pipeline,
            )
            merged.scripts[ns_id] = ns_sio

        # Merge chains with pipeline prefix
        for chain_name, members in sub_dag.chains.items():
            merged.chains[f"{sub_dag.scripts[members[0]].pipeline if members and members[0] in sub_dag.scripts else sub_dag.catalog.get(members[0], '')}:{chain_name}" if members else chain_name] = [
                _ns(sub_dag.scripts[m].pipeline if m in sub_dag.scripts else sio.pipeline, m)
                for m in members
            ]

    merged.build_index()
    return merged


# ---------------------------------------------------------------------------
# Bridge: inject pipeline edges into the trace graph
# ---------------------------------------------------------------------------

def inject_pipeline_edges(dag: PipelineDAG, workspace_root: Path, _graph=None):
    """Inject pipeline DAG edges into the comp-trace graph cache.
    This lets comp-trace walk through pipeline dependencies during
    cross-layer traces.

    ADHC_COMPIL_V4.020: when called with `_graph` (in-process TraceGraph),
    operates on that graph directly without saving to file. Used by
    `trace_graph.build_graph` to bake BD + INF gold pipeline edges into
    fresh comp-build output. Returns int (edges_added) or None if no cache.
    Backwards-compatible: omitting `_graph` preserves the original cache-load + save flow.
    """
    from .trace_graph import TraceGraph, Node, Edge

    if _graph is not None:
        g = _graph
        cache_file = None
    else:
        cache_file = workspace_root / ".comp-graph" / "graph.json"
        if not cache_file.exists():
            return
        g = TraceGraph.load(cache_file)

    edges_added = 0
    for sid, sio in dag.scripts.items():
        script_node_id = f"gold:{sio.filename.replace('.py', '')}"

        # Ensure script node exists
        if script_node_id not in g.nodes:
            g.add_node(Node(
                id=script_node_id,
                node_type="GOLD_SCRIPT",
                label=sio.filename.replace('.py', ''),
                file_path=sio.file_path,
                run_order=sio.run_order,
            ))

        # Add READS_S3 edges: s3_key -> script (pipeline-sourced)
        for key in sio.read_keys:
            s3_node_id = f"s3:{key}"
            if s3_node_id not in g.nodes:
                g.add_node(Node(
                    id=s3_node_id, node_type="S3_ARTIFACT", label=key,
                ))
            # Check if this edge already exists
            edge_exists = any(
                e.source == s3_node_id and e.target == script_node_id
                and e.edge_type == "READS_S3"
                for e in g.edges
            )
            if not edge_exists:
                g.add_edge(Edge(
                    source=s3_node_id, target=script_node_id,
                    edge_type="READS_S3",
                    metadata={"source": "pipeline_dag"},
                ))
                edges_added += 1

        # Add WRITES_S3 edges: script -> s3_key (pipeline-sourced)
        for key in sio.write_keys:
            s3_node_id = f"s3:{key}"
            if s3_node_id not in g.nodes:
                g.add_node(Node(
                    id=s3_node_id, node_type="S3_ARTIFACT", label=key,
                ))
            edge_exists = any(
                e.source == script_node_id and e.target == s3_node_id
                and e.edge_type == "WRITES_S3"
                for e in g.edges
            )
            if not edge_exists:
                g.add_edge(Edge(
                    source=script_node_id, target=s3_node_id,
                    edge_type="WRITES_S3",
                    metadata={"source": "pipeline_dag"},
                ))
                edges_added += 1

    if cache_file is not None:
        g.save(cache_file)
    return edges_added
