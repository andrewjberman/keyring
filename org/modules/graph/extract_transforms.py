"""
Transform extractor -- traces client-side data flow inside React components.

For each component, maps:
  fetch function -> response variable -> useMemo/useCallback chains -> rendered fields

Answers: "what fields from the API response does this component actually use,
and what client-side transformations does it apply?"

Authoritative sources:
  1. portal/src/pages/**/*.tsx -- component source (hooks, JSX)
  2. portal/src/pages/**/types.ts -- response type definitions
  3. portal/src/api/endpoints/*.ts -- fetch function return types

Zero API calls. Regex + heuristic extraction.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class FetchBinding:
    """A data-fetch hook in a component."""
    fetch_function: str        # e.g., getPartnerAnalytics
    data_variable: str         # e.g., analyticsData, data
    response_type: str = ""    # e.g., PartnerAnalyticsResponse
    hook_type: str = ""        # useQuery, useEffect+setState, direct call
    line_number: int = 0
    query_key: str = ""        # React Query cache key (if useQuery)


@dataclass
class TransformChain:
    """A useMemo/useCallback that transforms fetched data."""
    output_variable: str       # e.g., aggregatedAuaData
    hook_type: str             # useMemo, useCallback, inline
    line_number: int = 0
    input_variables: list[str] = field(default_factory=list)  # deps that reference fetch data
    field_accesses: list[str] = field(default_factory=list)   # e.g., data.aua.quarterly.data
    operations: list[str] = field(default_factory=list)       # filter, map, reduce, sort, slice
    code_preview: str = ""     # first ~120 chars of the chain body


@dataclass
class JsxReference:
    """A reference to data in JSX rendering."""
    variable: str              # what variable is used
    field_path: str            # e.g., aggregatedAuaData.length, item.period
    line_number: int = 0
    context: str = ""          # e.g., "map callback", "conditional", "text content"


@dataclass
class TypeField:
    """A field in a TypeScript interface."""
    name: str
    type_str: str
    optional: bool = False
    nested_fields: list['TypeField'] = field(default_factory=list)


@dataclass
class ComponentDataFlow:
    """Complete data flow for one component."""
    component_name: str
    file_path: str
    fetches: list[FetchBinding] = field(default_factory=list)
    transforms: list[TransformChain] = field(default_factory=list)
    jsx_refs: list[JsxReference] = field(default_factory=list)
    response_types: dict[str, list[TypeField]] = field(default_factory=dict)  # type_name -> fields
    state_types: dict[str, str] = field(default_factory=dict)  # state_var -> TypeName (from useState<Type>)

    def fields_used(self) -> set[str]:
        """All field paths actually accessed (from transforms + JSX)."""
        fields = set()
        for t in self.transforms:
            fields.update(t.field_accesses)
        for r in self.jsx_refs:
            if r.field_path:
                fields.add(r.field_path)
        return fields


# ---------------------------------------------------------------------------
# Step 1: Extract fetch bindings from component
# ---------------------------------------------------------------------------

# useQuery pattern: const { data: varName } = useQuery({ queryFn: () => fetchFn(...) })
_USE_QUERY = re.compile(
    r'(?:const\s+\{[^}]*data\s*(?::\s*(\w+))?\s*[^}]*\}|'
    r'const\s+(\w+))\s*=\s*useQuery'
    r'(?:<(\w+)>)?\s*\(\s*\{[^}]*queryFn\s*:\s*\(\)\s*=>\s*(\w+)\s*\(',
    re.DOTALL
)

# useQuery with queryKey
_QUERY_KEY = re.compile(
    r"queryKey\s*:\s*\[([^\]]+)\]"
)

# Direct: const data = await fetchFn(...)
_AWAIT_FETCH = re.compile(
    r'(?:const|let)\s+(\w+)\s*=\s*await\s+(\w+)\s*\(',
)

# Promise.all pattern: Promise.all([fetchA(...), fetchB(...)]).then(([a, b]) => ...)
_PROMISE_ALL = re.compile(
    r'Promise\.all\s*\(\s*\[([^\]]+)\]',
)

# Known endpoint import sources (files that export fetch functions)
_API_IMPORT_PATTERN = re.compile(
    r"import\s*\{([^}]+)\}\s*from\s*['\"]([^'\"]*(?:api|endpoints)[^'\"]*)['\"]"
)


def _get_imported_fetch_fns(content: str) -> set[str]:
    """Get all function names imported from API endpoint files."""
    fns = set()
    for m in _API_IMPORT_PATTERN.finditer(content):
        names = [n.strip().split(' as ')[0].strip() for n in m.group(1).split(',')]
        fns.update(n for n in names if n)
    return fns


def _extract_fetch_bindings(content: str, lines: list[str]) -> list[FetchBinding]:
    """Extract all data-fetch hooks from component source."""
    bindings: list[FetchBinding] = []
    seen_fns: set[str] = set()  # avoid duplicates

    # Get all imported API functions for validation
    api_fns = _get_imported_fetch_fns(content)

    # useQuery pattern
    for m in _USE_QUERY.finditer(content):
        data_var = m.group(1) or m.group(2) or 'data'
        resp_type = m.group(3) or ''
        fetch_fn = m.group(4)
        line_no = content[:m.start()].count('\n') + 1

        # Find queryKey
        nearby = content[m.start():m.start() + 500]
        qk_m = _QUERY_KEY.search(nearby)
        query_key = qk_m.group(1).strip() if qk_m else ""

        bindings.append(FetchBinding(
            fetch_function=fetch_fn,
            data_variable=data_var,
            response_type=resp_type,
            hook_type="useQuery",
            line_number=line_no,
            query_key=query_key,
        ))
        seen_fns.add(fetch_fn)

    # useEffect blocks: find fetch calls inside useEffect(() => { ... }, [...])
    # Skip functions that are inside a Promise.all (those are handled below).
    for ue_m in re.finditer(r'useEffect\s*\(\s*\(\)\s*=>\s*\{', content):
        ue_start = ue_m.end()
        depth = 1
        i = ue_start
        while i < len(content) and depth > 0:
            if content[i] == '{':
                depth += 1
            elif content[i] == '}':
                depth -= 1
            i += 1
        ue_body = content[ue_start:i]
        ue_line = content[:ue_m.start()].count('\n') + 1

        # Identify functions inside Promise.all in this useEffect (defer to Promise.all handler)
        promise_all_fns: set[str] = set()
        for pa_m in _PROMISE_ALL.finditer(ue_body):
            for fn_m in re.finditer(r'(\w+)\s*\(', pa_m.group(1)):
                promise_all_fns.add(fn_m.group(1))

        # Find standalone API function calls (NOT in Promise.all)
        for fn_name in api_fns:
            if fn_name in seen_fns or fn_name in promise_all_fns:
                continue
            if re.search(rf'\b{re.escape(fn_name)}\s*\(', ue_body):
                # Find the setState target: fetchFn().then((res) => { ... setXxx(res) ... })
                data_var = ""
                set_m = re.search(
                    rf'{re.escape(fn_name)}\s*\([^)]*\).*?\.then\s*\([^)]*\)\s*=>\s*\{{?'
                    r'[^}}]*?set(\w+)',
                    ue_body, re.DOTALL
                )
                if set_m:
                    state_name = set_m.group(1)
                    data_var = state_name[0].lower() + state_name[1:] if state_name else ""

                bindings.append(FetchBinding(
                    fetch_function=fn_name,
                    data_variable=data_var,
                    hook_type="useEffect+setState",
                    line_number=ue_line,
                ))
                seen_fns.add(fn_name)

    # Promise.all pattern: find the fetch functions AND trace destructured vars to setState
    for m in _PROMISE_ALL.finditer(content):
        calls_str = m.group(1)
        line_no = content[:m.start()].count('\n') + 1

        # Extract function names from the Promise.all array
        call_fns = []
        for fn_m in re.finditer(r'(\w+)\s*\(', calls_str):
            fn_name = fn_m.group(1)
            if fn_name in ('catch', 'then', 'null', 'Promise') or fn_name in seen_fns:
                continue
            if fn_name in api_fns or fn_name.startswith('get') or fn_name.startswith('fetch'):
                call_fns.append(fn_name)

        # Find .then(([var1, var2]) => { ... }) destructuring
        then_region = content[m.end():m.end() + 3000]
        then_m = re.search(r'\.then\s*\(\s*\(\s*\[([^\]]+)\]\s*\)\s*=>\s*\{', then_region)
        destructured_vars = []
        if then_m:
            destructured_vars = [v.strip() for v in then_m.group(1).split(',') if v.strip()]

            # For each destructured var, find ALL setState targets in the .then body
            then_body = then_region[then_m.end():then_m.end() + 2000]
            var_to_states: dict[str, list[str]] = {}  # dvar -> [state_var1, state_var2, ...]
            for dvar in destructured_vars:
                states: list[str] = []
                # Direct: set*(dvar) or set*(dvar.field)
                for sm in re.finditer(rf'set(\w+)\s*\(\s*{re.escape(dvar)}\b', then_body):
                    state_name = sm.group(1)
                    states.append(state_name[0].lower() + state_name[1:])
                # Aliased: const lb = dvar.field; ... set*(lb)
                for am in re.finditer(rf'(?:const|let)\s+(\w+)\s*=\s*{re.escape(dvar)}\.', then_body):
                    alias = am.group(1)
                    for sm in re.finditer(rf'set(\w+)\s*\(\s*{re.escape(alias)}\b', then_body):
                        state_name = sm.group(1)
                        states.append(state_name[0].lower() + state_name[1:])
                var_to_states[dvar] = states

        # Create bindings -- pair fetch functions with destructured vars
        for idx, fn_name in enumerate(call_fns):
            data_var = ""
            if idx < len(destructured_vars):
                dvar = destructured_vars[idx]
                states = var_to_states.get(dvar, [])
                if states:
                    # Use the destructured var name as primary (it's the response object)
                    # but record all setState targets for context
                    data_var = dvar
                else:
                    data_var = dvar

            bindings.append(FetchBinding(
                fetch_function=fn_name,
                data_variable=data_var,
                hook_type="Promise.all",
                line_number=line_no,
            ))
            seen_fns.add(fn_name)

    return bindings


# ---------------------------------------------------------------------------
# Step 2: Extract transform chains (useMemo/useCallback)
# ---------------------------------------------------------------------------

_USE_MEMO = re.compile(
    r'const\s+(\w+)\s*(?::\s*[\w<>\[\]|]+\s*)?=\s*useMemo\s*\(\s*\(\)\s*=>\s*\{?',
)

_USE_CALLBACK = re.compile(
    r'const\s+(\w+)\s*=\s*useCallback\s*\(',
)

# Operations that indicate data transformation
_TRANSFORM_OPS = {
    '.map(': 'map',
    '.filter(': 'filter',
    '.reduce(': 'reduce',
    '.sort(': 'sort',
    '.slice(': 'slice',
    '.find(': 'find',
    '.some(': 'some',
    '.every(': 'every',
    '.flatMap(': 'flatMap',
    '.forEach(': 'forEach',
    'Math.': 'math',
    '.toFixed(': 'format',
    'new Date(': 'date_parse',
}

# Field access pattern: variable.field or variable?.field or variable.field.subfield
# Handles optional chaining (?.) throughout the path
_FIELD_ACCESS = re.compile(r'(\w+)((?:\??\.(?:\w+|\[\w+\]))+)')


def _extract_transform_chains(content: str, lines: list[str], fetch_vars: set[str]) -> list[TransformChain]:
    """Extract useMemo/useCallback chains that reference fetched data."""
    chains: list[TransformChain] = []

    for pattern, hook_type in [(_USE_MEMO, 'useMemo'), (_USE_CALLBACK, 'useCallback')]:
        for m in pattern.finditer(content):
            output_var = m.group(1)
            start = m.start()
            line_no = content[:start].count('\n') + 1

            # Extract the hook body (find matching deps array)
            # Look for }, [deps]) pattern
            body_start = m.end()
            # Find the deps array: }, [dep1, dep2])
            deps_m = re.search(r'\}\s*,\s*\[([^\]]*)\]', content[body_start:body_start + 3000])
            if deps_m:
                body_end = body_start + deps_m.start()
                deps_str = deps_m.group(1)
            else:
                body_end = min(body_start + 1000, len(content))
                deps_str = ""

            body = content[body_start:body_end]
            deps = [d.strip() for d in deps_str.split(',') if d.strip()]

            # Check if any dep references fetch data
            input_vars = [d for d in deps if d in fetch_vars or any(fv in d for fv in fetch_vars)]
            if not input_vars:
                # Also check body for direct references
                body_refs = [fv for fv in fetch_vars if fv in body]
                if not body_refs:
                    continue
                input_vars = body_refs

            # Extract field accesses from body
            field_accesses = set()
            for fa_m in _FIELD_ACCESS.finditer(body):
                root_var = fa_m.group(1)
                field_path = fa_m.group(2)
                if root_var in fetch_vars or root_var in [iv for iv in input_vars]:
                    field_accesses.add(root_var + field_path)

            # Detect operations
            ops = []
            for op_str, op_name in _TRANSFORM_OPS.items():
                if op_str in body:
                    ops.append(op_name)

            # Code preview
            preview = body.strip()[:120].replace('\n', ' ')

            chains.append(TransformChain(
                output_variable=output_var,
                hook_type=hook_type,
                line_number=line_no,
                input_variables=input_vars,
                field_accesses=sorted(field_accesses),
                operations=ops,
                code_preview=preview,
            ))

    return chains


# ---------------------------------------------------------------------------
# Step 3: Extract JSX references
# ---------------------------------------------------------------------------

def _extract_jsx_refs(content: str, lines: list[str], all_data_vars: set[str]) -> list[JsxReference]:
    """Extract references to data variables in JSX rendering.
    Covers both direct variable access ({var.field}) and inline render
    callbacks ({var.map((item) => ... item.field ...)})."""
    refs: list[JsxReference] = []

    # Find JSX region (after the return statement)
    return_m = re.search(r'\breturn\s*\(', content)
    if not return_m:
        return refs

    jsx_content = content[return_m.start():]
    jsx_start_line = content[:return_m.start()].count('\n') + 1

    # Find variable references in JSX expressions: {variable.field} or {variable?.field}
    for m in re.finditer(r'\{([^}]+)\}', jsx_content):
        expr = m.group(1).strip()
        line_no = jsx_start_line + jsx_content[:m.start()].count('\n')

        for var in all_data_vars:
            if var in expr:
                # Extract field path
                fa_m = re.search(rf'{re.escape(var)}((?:\??\.\w+)*)', expr)
                field_path = fa_m.group(0) if fa_m else var

                # Determine context
                context = "expression"
                if '.map(' in expr:
                    context = "map iterator"
                elif '.length' in expr:
                    context = "conditional/length"
                elif '?' in expr and ':' in expr:
                    context = "ternary"
                elif 'format' in expr.lower():
                    context = "formatted display"

                refs.append(JsxReference(
                    variable=var,
                    field_path=field_path,
                    line_number=line_no,
                    context=context,
                ))

    # --- Inline render callback detection ---
    # Pattern: data.map((item) => ... ) or data.map((item, idx) => ... )
    # Find which data vars are iterated in JSX, and what callback params access
    for var in all_data_vars:
        # Find .map( callbacks on this variable in JSX
        map_pattern = re.compile(
            rf'{re.escape(var)}(?:\??)\.map\s*\(\s*'
            rf'(?:\(\s*(\w+)(?:\s*,\s*\w+)?\s*\)|(\w+))\s*=>'
        )
        for mm in map_pattern.finditer(jsx_content):
            callback_param = mm.group(1) or mm.group(2)
            if not callback_param:
                continue

            # Find the callback body (approximate: from => to the next unmatched ))
            cb_start = mm.end()
            # Scan forward for field accesses on the callback param
            # Look in the next ~2000 chars for param.field patterns
            cb_region = jsx_content[cb_start:cb_start + 2000]

            for fa_m in _FIELD_ACCESS.finditer(cb_region):
                if fa_m.group(1) == callback_param:
                    field_path = f"{var}[].{fa_m.group(1)}{fa_m.group(2)}"
                    cb_line = jsx_start_line + jsx_content[:cb_start + fa_m.start()].count('\n')
                    refs.append(JsxReference(
                        variable=var,
                        field_path=field_path,
                        line_number=cb_line,
                        context="inline render callback",
                    ))

    # --- Inline function data access (not in useMemo) ---
    # Pattern: function/const that accesses fetch data directly in the component body
    # (before JSX return), not captured as a useMemo chain
    pre_jsx = content[:return_m.start()] if return_m else content
    # Find inline arrow functions or regular functions that access data vars
    inline_fn_pattern = re.compile(
        r'(?:const\s+(\w+)\s*=\s*(?:\([^)]*\)|[^=])\s*=>|function\s+(\w+)\s*\([^)]*\))\s*\{?'
    )
    for ifm in inline_fn_pattern.finditer(pre_jsx):
        fn_name = ifm.group(1) or ifm.group(2)
        if not fn_name:
            continue
        # Get function body (next ~1000 chars)
        fn_body = pre_jsx[ifm.end():ifm.end() + 1000]
        for var in all_data_vars:
            if var in fn_body:
                for fa_m in _FIELD_ACCESS.finditer(fn_body):
                    if fa_m.group(1) == var:
                        fn_line = content[:ifm.start()].count('\n') + 1
                        refs.append(JsxReference(
                            variable=var,
                            field_path=f"{fa_m.group(1)}{fa_m.group(2)}",
                            line_number=fn_line,
                            context=f"inline function ({fn_name})",
                        ))

    return refs


# ---------------------------------------------------------------------------
# Step 4: Extract response type fields from types.ts
# ---------------------------------------------------------------------------

def _parse_interface_fields(content: str, type_name: str) -> list[TypeField]:
    """Extract fields from a TypeScript interface definition."""
    m = re.search(rf'(?:export\s+)?interface\s+{re.escape(type_name)}\s*\{{', content)
    if not m:
        return []

    start = m.end()
    depth = 1
    i = start
    while i < len(content) and depth > 0:
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
        i += 1
    block = content[start:i - 1]

    fields: list[TypeField] = []
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith('//') or line.startswith('/*'):
            continue
        fm = re.match(r'(\w+)(\??):\s*(.+?)(?:\s*//.*)?$', line.rstrip(';'))
        if fm:
            fields.append(TypeField(
                name=fm.group(1),
                type_str=fm.group(3).strip(),
                optional=bool(fm.group(2)),
            ))
    return fields


def parse_type_deep(content: str, type_name: str, max_depth: int = 3) -> dict[str, str]:
    """Recursively parse a TypeScript interface into a flat field map.
    Returns {dotted.path: type_string} for all fields up to max_depth.
    Handles inline objects ({ field: type }) and named type references."""
    result: dict[str, str] = {}
    _parse_type_recursive(content, type_name, "", result, max_depth, set())
    return result


def _parse_type_recursive(content: str, type_name: str, prefix: str,
                           result: dict[str, str], depth: int, visited: set[str]):
    """Recursive helper for parse_type_deep."""
    if depth <= 0 or type_name in visited:
        return
    visited.add(type_name)

    fields = _parse_interface_fields(content, type_name)
    for f in fields:
        path = f"{prefix}.{f.name}" if prefix else f.name
        result[path] = f.type_str

        # If type is a named interface, recurse into it
        type_clean = f.type_str.rstrip('[]').strip()
        type_clean = re.sub(r'\s*\|\s*null$', '', type_clean).strip()
        if re.match(r'^[A-Z]\w+$', type_clean) and type_clean not in ('Record', 'Partial', 'Omit'):
            _parse_type_recursive(content, type_clean, path, result, depth - 1, visited)

        # If type is an inline object { field: type; ... }, parse it
        if f.type_str.strip().startswith('{'):
            inline_fields = _parse_inline_object(f.type_str)
            for if_name, if_type in inline_fields.items():
                result[f"{path}.{if_name}"] = if_type


def _parse_inline_object(type_str: str) -> dict[str, str]:
    """Parse an inline TypeScript object type: { name: string; count: number }."""
    result: dict[str, str] = {}
    # Strip outer braces
    inner = type_str.strip()
    if inner.startswith('{'):
        inner = inner[1:]
    if inner.endswith('}'):
        inner = inner[:-1]

    for part in re.split(r';\s*', inner):
        part = part.strip()
        if not part:
            continue
        fm = re.match(r'(\w+)\??\s*:\s*(.+)', part)
        if fm:
            result[fm.group(1)] = fm.group(2).strip()
    return result


# ---------------------------------------------------------------------------
# Accessor helper pattern detector
# ---------------------------------------------------------------------------

def _extract_accessor_refs(content: str, fetch_vars: set[str]) -> list[tuple[str, str]]:
    """Detect accessor helper functions of the form:
        const r = (a: any) => ({ field1: a.field1, field2: a.field2 ?? a.alt ?? 0 })
    and trace which data variables they're called with, expanding
    r(dataVar).field -> dataVar.sourceField for downstream analysis.

    Handles two call patterns:
      1. Direct:   r(feeData).name   -- called_var is a fetch var
      2. Callback: feeData.map((a) => r(a).name)  -- called_var is a map param

    Returns list of (data_var, source_field) pairs (deduplicated).
    """
    refs: list[tuple[str, str]] = []

    # Pattern: const NAME = (PARAM: any) => ({
    accessor_pattern = re.compile(
        r'const\s+(\w+)\s*=\s*\(\s*(\w+)(?:\s*:\s*[^)]+)?\s*\)\s*(?::\s*\w+\s*)?=>\s*\(\s*\{'
    )

    accessor_map: dict[str, dict[str, str]] = {}  # accessor_name -> {output_field: source_field}
    for am in accessor_pattern.finditer(content):
        accessor_name = am.group(1)
        param_name = am.group(2)

        # Extract the object body: find matching } after ({
        brace_start = content.find('{', am.end() - 1)
        if brace_start == -1:
            continue
        depth = 1
        i = brace_start + 1
        while i < len(content) and depth > 0:
            if content[i] == '{':
                depth += 1
            elif content[i] == '}':
                depth -= 1
            i += 1
        body = content[brace_start:i]

        # Extract field mappings: output_field: param.source_field (first hit in ?? chains)
        fields: dict[str, str] = {}
        for fm in re.finditer(
            rf'(\w+)\s*:\s*{re.escape(param_name)}\??\.(\w+)',
            body
        ):
            if fm.group(1) not in fields:  # first mapping wins (??-chain: prefer first)
                fields[fm.group(1)] = fm.group(2)

        if fields:
            accessor_map[accessor_name] = fields

    if not accessor_map:
        return refs

    # Build the set of candidate data variables to search against.
    # Primary: known fetch vars. Fallback: any component-level var used in .map()/.filter() etc.
    # This handles prop-based components (no useQuery) where data arrives as a prop.
    candidate_vars: set[str] = set(fetch_vars)
    if not candidate_vars:
        # Scan for any var.map/filter/find/forEach call in the component body
        for mm in re.finditer(
            r'(\w+)\??\.(?:map|filter|find|forEach|flatMap|reduce)\s*\(',
            content
        ):
            var = mm.group(1)
            # Skip obvious non-data identifiers
            if var not in ('Object', 'Array', 'Math', 'JSON', 'console', 'window',
                           'document', 'Promise', 'undefined', 'null'):
                candidate_vars.add(var)

    seen: set[tuple[str, str]] = set()

    for accessor_name, field_map in accessor_map.items():

        # --- Pattern 1: Direct call r(dataVar).field ---
        direct_pattern = re.compile(
            rf'{re.escape(accessor_name)}\s*\(\s*(\w+)\s*\)\??\.(\w+)'
        )
        for cm in direct_pattern.finditer(content):
            called_var = cm.group(1)
            output_field = cm.group(2)
            if called_var in candidate_vars:
                source_field = field_map.get(output_field, output_field)
                key = (called_var, source_field)
                if key not in seen:
                    seen.add(key)
                    refs.append(key)

        # --- Pattern 2: Map callback - dataVar.map((param) => r(param).field) ---
        for data_var in candidate_vars:
            map_pattern = re.compile(
                rf'{re.escape(data_var)}\??\.(?:map|forEach|filter|find|flatMap|reduce)\s*\(\s*'
                rf'(?:\(\s*(\w+)(?:\s*,\s*\w+)?\s*\)|(\w+))\s*=>'
            )
            for mm in map_pattern.finditer(content):
                callback_param = mm.group(1) or mm.group(2)
                if not callback_param:
                    continue
                # Scan callback body (~2000 chars) for accessor(callback_param).field
                cb_region = content[mm.end():mm.end() + 2000]
                cb_pattern = re.compile(
                    rf'{re.escape(accessor_name)}\s*\(\s*{re.escape(callback_param)}\s*\)\??\.(\w+)'
                )
                for cm in cb_pattern.finditer(cb_region):
                    output_field = cm.group(1)
                    source_field = field_map.get(output_field, output_field)
                    key = (data_var, source_field)
                    if key not in seen:
                        seen.add(key)
                        refs.append(key)

        # --- Pattern 3: Assigned result - const row = r(param); row.field ---
        for data_var in candidate_vars:
            map_pattern = re.compile(
                rf'{re.escape(data_var)}\??\.(?:map|forEach|filter|find|flatMap|reduce)\s*\(\s*'
                rf'(?:\(\s*(\w+)(?:\s*,\s*\w+)?\s*\)|(\w+))\s*=>'
            )
            for mm in map_pattern.finditer(content):
                callback_param = mm.group(1) or mm.group(2)
                if not callback_param:
                    continue
                cb_region = content[mm.end():mm.end() + 2000]
                assign_pattern = re.compile(
                    rf'(?:const|let)\s+(\w+)\s*=\s*{re.escape(accessor_name)}\s*\(\s*'
                    rf'{re.escape(callback_param)}\s*\)'
                )
                for asn in assign_pattern.finditer(cb_region):
                    assigned_var = asn.group(1)
                    after = cb_region[asn.end():asn.end() + 1500]
                    field_access = re.compile(rf'{re.escape(assigned_var)}\??\.(\w+)')
                    for fa in field_access.finditer(after):
                        output_field = fa.group(1)
                        source_field = field_map.get(output_field, output_field)
                        key = (data_var, source_field)
                        if key not in seen:
                            seen.add(key)
                            refs.append(key)

        # --- Pattern 4: Prop-based access - accessor called on a prop var (no map) ---
        # Handles: const rows = useMemo(() => { return r(data).advisors.map(...) }, [data])
        # or: r(data).advisors used directly in JSX
        prop_direct = re.compile(
            rf'{re.escape(accessor_name)}\s*\(\s*(\w+)\??(?:\.\w+)?\s*\)\??\.(\w+)'
        )
        for cm in prop_direct.finditer(content):
            called_var = cm.group(1)
            output_field = cm.group(2)
            if called_var in candidate_vars and (called_var, output_field) not in seen:
                source_field = field_map.get(output_field, output_field)
                key = (called_var, source_field)
                if key not in seen:
                    seen.add(key)
                    refs.append(key)

    return refs


# ---------------------------------------------------------------------------
# Main: build data flow for a component
# ---------------------------------------------------------------------------

def build_component_dataflow(component_path: Path, workspace_root: Path) -> ComponentDataFlow | None:
    """Build the complete data flow map for a single component."""
    try:
        content = component_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None

    rel_path = str(component_path.relative_to(workspace_root)).replace("\\", "/")
    lines = content.splitlines()

    flow = ComponentDataFlow(
        component_name=component_path.stem,
        file_path=rel_path,
    )

    # Step 1: Find fetch bindings
    flow.fetches = _extract_fetch_bindings(content, lines)

    # Collect all data variables from fetches
    fetch_vars: set[str] = set()
    for fb in flow.fetches:
        if fb.data_variable:
            fetch_vars.add(fb.data_variable)

    # Step 2: Find transform chains
    flow.transforms = _extract_transform_chains(content, lines, fetch_vars)

    # Collect all output variables from transforms (they become data vars for JSX)
    all_data_vars = set(fetch_vars)
    for tc in flow.transforms:
        all_data_vars.add(tc.output_variable)

    # Step 2b: Detect accessor helpers (e.g. const r = (a: any) => ({ field: a.field }))
    # These proxy field access through a helper call r(dataVar).field instead of dataVar.field
    # We expand them so the rest of the analysis treats the fields as direct data var accesses.
    accessor_refs = _extract_accessor_refs(content, fetch_vars)
    all_data_vars.update(v for v, _ in accessor_refs)

    # Step 3: Find JSX references
    flow.jsx_refs = _extract_jsx_refs(content, lines, all_data_vars)

    # Merge accessor refs into jsx_refs so schema-check and fields commands see them
    for data_var, field_path in accessor_refs:
        flow.jsx_refs.append(JsxReference(
            variable=data_var,
            field_path=f"{data_var}.{field_path}",
            line_number=0,
            context="accessor helper",
        ))

    # Step 4: Extract useState type annotations: useState<Type>() -> state_var -> Type
    # Pattern: const [varName, setVarName] = useState<TypeName | null>(...)
    for m in re.finditer(
        r'const\s+\[(\w+)\s*,\s*set\w+\]\s*=\s*useState<([^>]+)>',
        content
    ):
        state_var = m.group(1)
        state_type = m.group(2).strip()
        # Clean: remove | null, | undefined
        state_type = re.sub(r'\s*\|\s*(?:null|undefined)\s*', '', state_type).strip()
        # Handle import('...').TypeName
        state_type = re.sub(r"import\([^)]+\)\.", '', state_type).strip()
        if state_type:
            flow.state_types[state_var] = state_type

    # Step 5: Parse response types (from fetch + state type annotations)
    types_file = component_path.parent / "types.ts"
    if not types_file.exists():
        types_file = component_path.parent.parent / "types.ts"
    if types_file.exists():
        types_content = types_file.read_text(encoding="utf-8", errors="replace")
        # Parse fetch response types
        for fb in flow.fetches:
            if fb.response_type and fb.response_type not in flow.response_types:
                fields = _parse_interface_fields(types_content, fb.response_type)
                if fields:
                    flow.response_types[fb.response_type] = fields
        # Parse state variable types (may differ from fetch response types due to adapters)
        for state_var, state_type in flow.state_types.items():
            if state_type not in flow.response_types:
                fields = _parse_interface_fields(types_content, state_type)
                if fields:
                    flow.response_types[state_type] = fields

    return flow


def build_all_dataflows(workspace_root: Path) -> list[ComponentDataFlow]:
    """Build data flows for all components in the portal."""
    pages_dir = workspace_root / "portal" / "src" / "pages"
    if not pages_dir.exists():
        return []

    flows = []
    for tsx_file in sorted(pages_dir.rglob("*.tsx")):
        flow = build_component_dataflow(tsx_file, workspace_root)
        if flow and (flow.fetches or flow.transforms):
            flows.append(flow)
    return flows
