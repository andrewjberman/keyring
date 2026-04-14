#!/usr/bin/env python3
"""
comp-transform -- trace client-side data flow inside React components.

Usage:
    comp-transform trace PartnerAnalytics     # full data flow for one component
    comp-transform trace ClientsTab           # full data flow for Books tab
    comp-transform fields PartnerAnalytics    # which response fields are actually used
    comp-transform chains PartnerAnalytics    # useMemo/useCallback transformation chains
    comp-transform unused PartnerAnalytics    # response fields fetched but never rendered
    comp-transform all                        # summary of all components with data flow
    comp-transform stats                      # statistics

Traces: fetch function -> response type -> useMemo/useCallback chains -> rendered JSX fields.
Answers: "what does this component actually use from the API response, and what does it discard?"
"""

import argparse
import json
import re
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_transforms import (
    build_component_dataflow, build_all_dataflows, ComponentDataFlow,
)


def _find_component(query: str) -> Path | None:
    """Find a component file by name (fuzzy match)."""
    pages_dir = _WORKSPACE / "portal" / "src" / "pages"
    if not pages_dir.exists():
        return None

    query_lower = query.lower()
    matches = []
    for tsx_file in pages_dir.rglob("*.tsx"):
        if query_lower == tsx_file.stem.lower():
            return tsx_file
        if query_lower in tsx_file.stem.lower():
            matches.append(tsx_file)

    if len(matches) == 1:
        return matches[0]
    if matches:
        print(f"Multiple matches for '{query}':")
        for m in matches:
            print(f"  {m.stem} ({m.relative_to(_WORKSPACE)})")
        sys.exit(1)
    return None


def _print_flow(flow: ComponentDataFlow, verbose: bool = True):
    print(f"COMPONENT: {flow.component_name}")
    print(f"  File: {flow.file_path}")
    print()

    if flow.fetches:
        print(f"  FETCHES ({len(flow.fetches)}):")
        for fb in flow.fetches:
            type_str = f" -> {fb.response_type}" if fb.response_type else ""
            qk_str = f" [key: {fb.query_key}]" if fb.query_key else ""
            print(f"    L{fb.line_number}: {fb.fetch_function}(){type_str}")
            print(f"      hook: {fb.hook_type} | data var: {fb.data_variable}{qk_str}")
        print()

    if flow.transforms:
        print(f"  TRANSFORM CHAINS ({len(flow.transforms)}):")
        for tc in flow.transforms:
            ops_str = f" [{', '.join(tc.operations)}]" if tc.operations else ""
            print(f"    L{tc.line_number}: {tc.output_variable} ({tc.hook_type}){ops_str}")
            print(f"      reads: {', '.join(tc.input_variables)}")
            if tc.field_accesses and verbose:
                for fa in tc.field_accesses[:8]:
                    print(f"        .{fa.split('.', 1)[1] if '.' in fa else fa}")
                if len(tc.field_accesses) > 8:
                    print(f"        ... +{len(tc.field_accesses) - 8} more")
            if tc.code_preview and verbose:
                print(f"      preview: {tc.code_preview}")
        print()

    if flow.jsx_refs and verbose:
        # Deduplicate by field_path
        seen = set()
        unique_refs = []
        for r in flow.jsx_refs:
            if r.field_path not in seen:
                seen.add(r.field_path)
                unique_refs.append(r)

        print(f"  JSX REFERENCES ({len(unique_refs)} unique):")
        for r in unique_refs[:20]:
            print(f"    L{r.line_number}: {r.field_path} ({r.context})")
        if len(unique_refs) > 20:
            print(f"    ... +{len(unique_refs) - 20} more")
        print()

    if flow.response_types:
        print(f"  RESPONSE TYPES:")
        for type_name, fields in flow.response_types.items():
            print(f"    {type_name} ({len(fields)} fields):")
            for f in fields[:15]:
                opt = "?" if f.optional else ""
                print(f"      {f.name}{opt}: {f.type_str}")
            if len(fields) > 15:
                print(f"      ... +{len(fields) - 15} more")
        print()


def cmd_trace(args):
    path = _find_component(args.component)
    if not path:
        print(f"Component not found: {args.component}")
        sys.exit(1)

    flow = build_component_dataflow(path, _WORKSPACE)
    if not flow:
        print(f"Could not parse: {path}")
        sys.exit(1)

    if args.json:
        print(json.dumps({
            "component": flow.component_name,
            "file": flow.file_path,
            "fetches": [{"fn": f.fetch_function, "var": f.data_variable,
                         "type": f.response_type, "hook": f.hook_type,
                         "line": f.line_number, "query_key": f.query_key}
                        for f in flow.fetches],
            "transforms": [{"output": t.output_variable, "hook": t.hook_type,
                           "line": t.line_number, "inputs": t.input_variables,
                           "fields": t.field_accesses, "ops": t.operations}
                          for t in flow.transforms],
            "jsx_refs": [{"var": r.variable, "field": r.field_path,
                         "line": r.line_number, "context": r.context}
                        for r in flow.jsx_refs],
            "response_types": {k: [{"name": f.name, "type": f.type_str, "optional": f.optional}
                                   for f in v]
                              for k, v in flow.response_types.items()},
        }, indent=2))
    else:
        _print_flow(flow)


_JS_BUILTINS = {
    'map', 'filter', 'find', 'some', 'every', 'reduce', 'forEach',
    'flatMap', 'sort', 'slice', 'length', 'includes', 'indexOf',
    'keys', 'values', 'entries', 'push', 'pop', 'concat', 'join',
    'toString', 'toFixed', 'toLocaleString', 'trim', 'toLowerCase',
    'toUpperCase', 'startsWith', 'endsWith', 'replace', 'split',
    'match', 'search', 'charAt', 'substring', 'then', 'catch',
    'flat', 'reverse', 'fill', 'findIndex', 'at',
}


def cmd_fields(args):
    path = _find_component(args.component)
    if not path:
        print(f"Component not found: {args.component}")
        sys.exit(1)

    flow = build_component_dataflow(path, _WORKSPACE)
    if not flow:
        print(f"Could not parse: {path}")
        sys.exit(1)

    fields = flow.fields_used()

    # Filter out JS built-in method names that leak from array/string method calls
    # e.g. advisors.map(...) produces 'advisors.map' as a "field" -- not a real data field
    def _is_data_field(field_path: str) -> bool:
        parts = field_path.replace('?.', '.').split('.')
        return all(p not in _JS_BUILTINS for p in parts if p)

    fields = {f for f in fields if _is_data_field(f)}

    print(f"FIELDS USED by {flow.component_name} ({len(fields)}):")
    print()

    # Group by root variable
    by_root: dict[str, list[str]] = {}
    for f in sorted(fields):
        root = f.split('.')[0]
        by_root.setdefault(root, []).append(f)

    for root, paths in sorted(by_root.items()):
        # Find which fetch provides this root
        source_fetch = next((fb for fb in flow.fetches if fb.data_variable == root), None)
        source_str = f" (from {source_fetch.fetch_function})" if source_fetch else ""
        print(f"  {root}{source_str}:")
        for p in paths:
            suffix = p[len(root):] if p.startswith(root) else p
            print(f"    {suffix or '(root)'}")
        print()


def cmd_chains(args):
    path = _find_component(args.component)
    if not path:
        print(f"Component not found: {args.component}")
        sys.exit(1)

    flow = build_component_dataflow(path, _WORKSPACE)
    if not flow:
        print(f"Could not parse: {path}")
        sys.exit(1)

    if not flow.transforms:
        print(f"No transform chains found in {flow.component_name}")
        return

    print(f"TRANSFORM CHAINS in {flow.component_name} ({len(flow.transforms)}):")
    print()

    for tc in flow.transforms:
        ops_str = f"  ops: {', '.join(tc.operations)}" if tc.operations else ""
        print(f"  {tc.output_variable} (L{tc.line_number}, {tc.hook_type})")
        print(f"    reads: {', '.join(tc.input_variables)}")
        if ops_str:
            print(f"   {ops_str}")
        if tc.field_accesses:
            print(f"    fields accessed:")
            for fa in tc.field_accesses:
                print(f"      {fa}")
        if tc.code_preview:
            print(f"    code: {tc.code_preview}")
        print()


def cmd_unused(args):
    path = _find_component(args.component)
    if not path:
        print(f"Component not found: {args.component}")
        sys.exit(1)

    flow = build_component_dataflow(path, _WORKSPACE)
    if not flow:
        print(f"Could not parse: {path}")
        sys.exit(1)

    used = flow.fields_used()

    print(f"WASTE ANALYSIS for {flow.component_name}:")
    print()

    for type_name, fields in flow.response_types.items():
        used_names = set()
        for u in used:
            # Normalize: remove ?. optional chaining, bracket access, etc.
            normalized = re.sub(r'\?\.|[\[\]?]', '.', u)
            parts = [p for p in normalized.split('.') if p and p.isidentifier()]
            for p in parts:
                used_names.add(p)

        unused = [f for f in fields if f.name not in used_names]
        used_list = [f for f in fields if f.name in used_names]

        print(f"  {type_name}:")
        print(f"    total fields: {len(fields)}")
        print(f"    used:         {len(used_list)}")
        print(f"    unused:       {len(unused)}")
        if unused:
            print(f"    potentially unused fields:")
            for f in unused:
                opt = "?" if f.optional else ""
                print(f"      {f.name}{opt}: {f.type_str}")
        print()

    if not flow.response_types:
        print("  No response types resolved -- cannot compute unused fields.")
        print("  (Response type must be specified in useQuery<Type> or endpoint return type)")


def cmd_schema_check(args):
    """Cross-reference rendered fields against the response type schema.
    Flags:
    - MISSING: field rendered in JSX but not in response type (will break at runtime)
    - UNUSED: field in response type but never rendered (over-fetching / waste)
    """
    from org.modules.graph.extract_transforms import parse_type_deep

    path = _find_component(args.component)
    if not path:
        print(f"Component not found: {args.component}")
        sys.exit(1)

    flow = build_component_dataflow(path, _WORKSPACE)
    if not flow:
        print(f"Could not parse: {path}")
        sys.exit(1)

    # Find types.ts
    types_file = path.parent / "types.ts"
    if not types_file.exists():
        types_file = path.parent.parent / "types.ts"
    if not types_file.exists():
        print(f"No types.ts found near {path}")
        sys.exit(1)
    types_content = types_file.read_text(encoding="utf-8", errors="replace")

    # Also scan the endpoint files for return type annotations
    api_dir = _WORKSPACE / "portal" / "src" / "api" / "endpoints"
    api_types: dict[str, str] = {}  # fn_name -> return type
    if api_dir.exists():
        for ts_file in api_dir.glob("*.ts"):
            try:
                api_content = ts_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            for m in re.finditer(
                r'export\s+(?:async\s+)?function\s+(\w+)\s*\([^)]*\)\s*:\s*Promise<(\w+)>',
                api_content
            ):
                api_types[m.group(1)] = m.group(2)

    print(f"SCHEMA CHECK: {flow.component_name}")
    print(f"  File: {flow.file_path}")
    print()

    has_issues = False

    for fb in flow.fetches:
        # Resolve response type: from useQuery<Type> or from endpoint return type
        fetch_type = fb.response_type
        if not fetch_type and fb.fetch_function in api_types:
            fetch_type = api_types[fb.fetch_function]

        # Check if state variable has a different type (adapter pattern)
        data_var = fb.data_variable
        state_type = flow.state_types.get(data_var, "") if data_var else ""
        # Clean state type for matching
        state_type_clean = re.sub(r'\s*\|\s*(?:null|undefined)', '', state_type).strip() if state_type else ""

        # Determine which type to check JSX fields against:
        # If state type exists and differs from fetch type, JSX reads the state type
        has_adapter = False
        check_type = fetch_type or ""
        if state_type_clean and fetch_type and state_type_clean != fetch_type:
            has_adapter = True
            check_type = state_type_clean  # JSX reads the state type, not fetch type

        if not check_type:
            continue

        # Parse the type deeply (recursive into nested interfaces)
        type_fields = parse_type_deep(types_content, check_type)
        if not type_fields:
            print(f"  {fb.fetch_function}() -> {check_type}: type not found in types.ts")
            continue

        type_root_fields = set()
        for field_path in type_fields:
            parts = field_path.split('.')
            type_root_fields.add(parts[0])
            for i in range(1, len(parts) + 1):
                type_root_fields.add('.'.join(parts[:i]))

        # Collect rendered fields for this fetch's data variable
        data_var = fb.data_variable
        rendered_fields: set[str] = set()

        # From transform chains
        for tc in flow.transforms:
            if data_var and data_var in tc.input_variables:
                for fa in tc.field_accesses:
                    # Strip the variable prefix: timeseriesData?.aua -> aua
                    normalized = re.sub(r'\?\.|[\[\]?]', '.', fa)
                    parts = [p for p in normalized.split('.') if p and p.isidentifier()]
                    if parts and parts[0] == data_var:
                        field_path = '.'.join(parts[1:])
                        if field_path:
                            rendered_fields.add(field_path)
                    elif parts:
                        rendered_fields.add('.'.join(parts))

        # From JSX refs
        for ref in flow.jsx_refs:
            if ref.variable == data_var or (data_var and data_var in ref.field_path):
                normalized = re.sub(r'\?\.|[\[\]?]', '.', ref.field_path)
                parts = [p for p in normalized.split('.') if p and p.isidentifier()]
                if parts and parts[0] == data_var:
                    field_path = '.'.join(parts[1:])
                    if field_path:
                        rendered_fields.add(field_path)

        if not rendered_fields:
            continue

        # Cross-reference: rendered vs type schema
        rendered_roots = set()
        for rf in rendered_fields:
            root = rf.split('.')[0]
            rendered_roots.add(root)

        type_roots = set()
        for tf in type_fields:
            root = tf.split('.')[0]
            type_roots.add(root)

        # Filter out JS built-in methods that aren't real field names
        js_builtins = {'map', 'filter', 'find', 'some', 'every', 'reduce', 'forEach',
                       'flatMap', 'sort', 'slice', 'length', 'includes', 'indexOf',
                       'keys', 'values', 'entries', 'item', 'push', 'pop', 'concat',
                       'join', 'toString', 'toFixed', 'toLocaleString', 'trim',
                       'toLowerCase', 'toUpperCase', 'startsWith', 'endsWith',
                       'replace', 'split', 'match', 'search', 'charAt', 'substring'}

        missing = rendered_roots - type_roots - js_builtins
        unused = type_roots - rendered_roots
        # Filter unused: skip metadata fields
        metadata_fields = {'generated_at', 'data_as_of', 'firm_id', 'relationship_id',
                           'advisor_id', 'account_id'}
        unused_non_meta = unused - metadata_fields

        print(f"  {fb.fetch_function}() -> {check_type}")
        if has_adapter:
            print(f"    ADAPTER: fetch returns {fetch_type}, state var '{data_var}' is {state_type_clean}")
            print(f"    checking JSX against: {check_type} (state type, not fetch type)")
        print(f"    type fields:     {len(type_roots)}")
        print(f"    rendered fields: {len(rendered_roots)}")

        # Detect runtime destructure aliases: const { X } = parentVar
        # These appear as "missing" fields but are actually flattened from the parent type.
        component_source = path.read_text(encoding="utf-8", errors="replace")
        alias_map: dict[str, str] = {}  # alias_name -> parent_var
        for dm in re.finditer(
            r'const\s*\{([^}]+)\}\s*=\s*(\w+)',
            component_source
        ):
            parent = dm.group(2)
            for name in re.split(r'[,\s]+', dm.group(1)):
                clean = name.strip().split(':')[0].strip()  # handle renaming: { x: y }
                if clean and clean.isidentifier():
                    alias_map[clean] = parent

        # Partition missing into true-missing vs alias
        true_missing = set()
        aliases_found: dict[str, str] = {}
        for m in missing:
            if m in alias_map:
                aliases_found[m] = alias_map[m]
            else:
                true_missing.add(m)

        if true_missing:
            has_issues = True
            print(f"    !! MISSING FROM TYPE ({len(true_missing)}):")
            for m in sorted(true_missing):
                # Find where it's rendered
                locations = []
                for ref in flow.jsx_refs:
                    if m in ref.field_path:
                        locations.append(f"L{ref.line_number}")
                for tc in flow.transforms:
                    if any(m in fa for fa in tc.field_accesses):
                        locations.append(f"L{tc.line_number} ({tc.output_variable})")
                loc_str = f" at {', '.join(locations[:3])}" if locations else ""
                print(f"       {m}{loc_str}")
                print(f"         Component renders this but {check_type} does not define it.")
                print(f"         This will be undefined at runtime unless aliased or injected.")

        if aliases_found:
            print(f"    NOTE (runtime aliases, {len(aliases_found)} -- not type violations):")
            for name, parent in sorted(aliases_found.items()):
                print(f"       {name}  <- destructured from '{parent}' (const {{ {name} }} = {parent})")
                print(f"         Check that '{parent}.{name}' exists in the type. Not flagged as MISSING.")

        if unused_non_meta:
            feature_token = (args.feature or "").lower().strip()
            feature_hits = {u for u in unused_non_meta if feature_token and feature_token in u.lower()}
            plain_unused = unused_non_meta - feature_hits

            if feature_hits:
                print(f"    !! WARN — feature-relevant UNUSED ({len(feature_hits)}, token: '{feature_token}'):")
                for u in sorted(feature_hits):
                    print(f"       {u}: {type_fields.get(u, '?')}")
                    print(f"         This field is typed but NEVER rendered.")
                    print(f"         You're building '{feature_token}' support — most likely cause: a routing")
                    print(f"         ternary (e.g. cohort === 'geo' ? ... : ...) is missing the '{feature_token}'")
                    print(f"         branch. Run: comp-transform ternary-audit {flow.component_name}")
                has_issues = True

            if plain_unused:
                print(f"    UNUSED ({len(plain_unused)}):")
                for u in sorted(plain_unused):
                    print(f"       {u}: {type_fields.get(u, '?')}")

        if not missing and not unused_non_meta:
            print(f"    OK: all rendered fields exist in type, no waste")

        print()

    if has_issues:
        print("  SCHEMA MISMATCH DETECTED: component renders fields not defined in the response type.")
        print("  This causes undefined values at runtime. Fix the type or the component.")
    else:
        print("  All rendered fields match their response types.")


def cmd_ternary_audit(args):
    """Scan a component for ternary chains on union-typed variables that don't
    handle all union members.

    Finds:
    1. String-literal union type aliases: type CohortOption = 'geo' | 'adv' | 'ofc'
    2. Variables using those types: const [cohort, setCohort] = useState<CohortOption>(...)
    3. Ternary chains on those variables: cohort === 'geo' ? X : Y
    4. Reports which union members are not handled on each line

    Example output:
      L1956: cohort ternary — handles ['geo', 'adv'] — MISSING: ['ofc']
             ofc falls through to adv path (last else branch)
    """
    path = _find_component(args.component)
    if not path:
        print(f"Component not found: {args.component}")
        sys.exit(1)

    try:
        source = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"Could not read {path}: {e}")
        sys.exit(1)

    lines = source.splitlines()

    print(f"TERNARY AUDIT: {path.name}")
    print(f"  File: {path.relative_to(_WORKSPACE)}")
    print()

    # -----------------------------------------------------------------------
    # Step 1: Extract union type aliases from the file and types.ts
    # -----------------------------------------------------------------------
    union_types: dict[str, list[str]] = {}  # TypeName -> ['lit1', 'lit2', ...]

    def _extract_unions(text: str) -> None:
        for m in re.finditer(
            r'type\s+(\w+)\s*=\s*((?:\'[^\']+\'|"[^"]+")(?:\s*\|\s*(?:\'[^\']+\'|"[^"]+"))+)',
            text,
        ):
            type_name = m.group(1)
            members = re.findall(r'[\'"]([^\'"]+)[\'"]', m.group(2))
            if len(members) >= 2:
                union_types[type_name] = members

    _extract_unions(source)
    types_file = path.parent / "types.ts"
    if not types_file.exists():
        types_file = path.parent.parent / "types.ts"
    if types_file.exists():
        _extract_unions(types_file.read_text(encoding="utf-8", errors="replace"))

    if not union_types:
        print("  No string-literal union types found in file or types.ts.")
        print("  Nothing to audit.")
        return

    # -----------------------------------------------------------------------
    # Step 2: Find variables bound to those union types
    # -----------------------------------------------------------------------
    # Patterns: useState<Type>, param: Type, : Type =, function arg: Type
    var_to_union: dict[str, str] = {}  # varName -> TypeName

    for type_name in union_types:
        esc = re.escape(type_name)
        # useState<CohortOption>
        for m in re.finditer(rf'const\s*\[(\w+)[,\s].*?\]\s*=\s*useState\s*<{esc}>', source):
            var_to_union[m.group(1)] = type_name
        # param: CohortOption or variable: CohortOption
        for m in re.finditer(rf'(\w+)\s*:\s*{esc}\b', source):
            var_to_union[m.group(1)] = type_name
        # function arg without destructuring
        for m in re.finditer(rf'function\s+\w+[^{{]*?(\w+)\s*:\s*{esc}', source):
            var_to_union[m.group(1)] = type_name

    if not var_to_union and not args.var:
        print("  No variables found with union types.")
        print(f"  Union types found: {', '.join(union_types.keys())}")
        print("  Use --var <name> to audit a specific variable manually.")
        return

    # Override: explicit --var flag
    if args.var:
        for v in args.var:
            # Try to match to a known union type, else use --members if provided
            if v not in var_to_union:
                var_to_union[v] = "(manual)"

    # -----------------------------------------------------------------------
    # Step 3: Scan every line for ternary chains on each tracked variable
    # -----------------------------------------------------------------------
    # For each line containing `varname ===`, collect all checked string literals
    # in that logical expression (handles chained ternaries on one line).
    # We also look ahead up to 4 lines for continuation patterns.

    gaps_found = 0
    exhaustive_count = 0

    # Generic variable names that are commonly used as loop iterators/keys — skip by default
    _GENERIC_VARS = {'key', 'val', 'value', 'item', 'entry', 'elem', 'node',
                     'i', 'j', 'k', 'idx', 'index', 'seg', 'segment'}

    for var_name, type_name in sorted(var_to_union.items()):
        members = union_types.get(type_name, [])
        if not members and not args.var:
            continue

        # Skip generic variable names unless explicitly requested via --var
        if var_name in _GENERIC_VARS and not (args.var and var_name in args.var):
            continue

        # Skip large unions by default (TimePeriodKey has 10+ members — these
        # are almost always handled via dynamic accessor `view[period]` not ternaries).
        # Use --all-unions to include them.
        if len(members) > 6 and not getattr(args, 'all_unions', False):
            continue

        var_esc = re.escape(var_name)
        checked_pattern = re.compile(
            rf'\b{var_esc}\s*(?:===|==|!==|!=)\s*[\'"]([^\'"]+)[\'"]'
            rf'|[\'"]([^\'"]+)[\'"]\s*(?:===|==|!==|!=)\s*\b{var_esc}\b'
        )

        # Scan lines
        visited_regions: set[int] = set()  # avoid double-reporting nearby lines

        for lineno, line in enumerate(lines, 1):
            if var_name not in line:
                continue
            if '?' not in line and '===' not in line:
                continue

            # Skip pure comment lines
            stripped = line.strip()
            if stripped.startswith('//') or stripped.startswith('*'):
                continue

            # Collect the full logical region (this line + continuations)
            region_start = lineno
            if region_start in visited_regions:
                continue

            region_lines = [line]
            # Look ahead for continuation: lines that are part of same ternary
            for offset in range(1, 5):
                if lineno + offset - 1 >= len(lines):
                    break
                next_line = lines[lineno + offset - 1]
                # Continue if next line has more comparisons on same var or ? :
                if var_name in next_line or (next_line.strip().startswith(':') and offset <= 2):
                    region_lines.append(next_line)
                else:
                    break

            region_text = ' '.join(region_lines)

            # Skip if no ternary operator in the region
            if '?' not in region_text:
                continue

            # Collect all values compared against var_name in this region
            checked_values = set()
            for m in checked_pattern.finditer(region_text):
                val = m.group(1) or m.group(2)
                if val:
                    checked_values.add(val)

            if not checked_values:
                continue

            # Mark this region as visited
            for offset in range(len(region_lines)):
                visited_regions.add(region_start + offset)

            if not members:
                # Manual var with no known type — just report what was checked
                print(f"  L{lineno}: {var_name} ternary — checks: {sorted(checked_values)}")
                print(f"           (no union type found — use --members to specify expected values)")
                continue

            missing_members = [m for m in members if m not in checked_values]

            if not missing_members:
                exhaustive_count += 1
                if args.verbose:
                    print(f"  L{lineno}: {var_name} ({type_name}) — OK: all members handled {sorted(checked_values)}")
                continue

            # Signal quality filter:
            # A 2-branch ternary on a 3-member union (N checked = total-1) is
            # usually intentional: the last else is the catch-all for the one
            # remaining member (e.g. geo=A adv=B else=C is fine for 'ofc' as
            # the fallthrough if the else value is correct for ofc).
            #
            # The REAL bug pattern is N checked < total-1: TWO OR MORE members
            # share the same unintended fallthrough value (e.g. the W3 bug where
            # cohort==='geo' ? nna_geo : nna_adv meant both adv AND ofc fell to
            # nna_adv, silently routing ofc to wrong data).
            #
            # Only flag when at least 2 members are unhandled, UNLESS --strict.
            implicit_count = len(missing_members)
            is_suspicious = implicit_count >= 2 or getattr(args, 'strict', False)

            if not is_suspicious:
                # Single implicit fallthrough — acceptable pattern, skip unless verbose
                if args.verbose:
                    print(f"  L{lineno}: {var_name} ({type_name}) — NOTE (1 implicit fallthrough, likely intentional):")
                    print(f"    handles:  {sorted(checked_values)}")
                    print(f"    implicit: {missing_members}  (routes to else branch)")
                    display = stripped[:100] + ('...' if len(stripped) > 100 else '')
                    print(f"    code: {display}")
                    print()
                continue

            # Additional filter: skip dynamic-accessor patterns where the else
            # branch clearly uses the variable as a dynamic key.
            # e.g. period === 'current' ? view.current : view[period]
            # The `[period]` in the else branch means all values are handled.
            region_lower = region_text.lower()
            dynamic_accessor = f'[{var_name.lower()}]'
            if dynamic_accessor in region_lower:
                if args.verbose:
                    print(f"  L{lineno}: {var_name} ({type_name}) — SKIP (dynamic accessor [{var_name}] in else branch)")
                continue

            # True gap: 2+ members unhandled → likely wrong data routing
            gaps_found += 1
            print(f"  L{lineno}: {var_name} ({type_name})")
            print(f"    handles:  {sorted(checked_values)}")
            print(f"    MISSING:  {missing_members}  ({implicit_count} members fall to else branch)")
            print(f"    These {implicit_count} values silently share the else branch value —")
            print(f"    if that value is correct for one but not the others, this is a routing bug.")

            # Show the line for context
            display = stripped[:120] + ('...' if len(stripped) > 120 else '')
            print(f"    code: {display}")
            print()

    # -----------------------------------------------------------------------
    # Step 4: Summary
    # -----------------------------------------------------------------------
    print()
    if gaps_found == 0:
        print(f"  All ternaries on union-typed variables are exhaustive.")
        if exhaustive_count > 0:
            print(f"  {exhaustive_count} ternary sites checked, 0 gaps found.")
    else:
        print(f"  {gaps_found} ternary gap(s) found across {len(var_to_union)} variable(s).")
        print(f"  Each gap means unhandled union members silently route to the else branch.")
        print()
        print(f"  Run: comp-transform schema-check {args.component} --feature <token>")
        print(f"  to see which typed fields are UNUSED for each missing branch.")


def cmd_all(args):
    flows = build_all_dataflows(_WORKSPACE)
    if not flows:
        print("No components with data flow found.")
        return

    print(f"ALL COMPONENT DATA FLOWS ({len(flows)} components)")
    print()
    for flow in flows:
        fetch_count = len(flow.fetches)
        chain_count = len(flow.transforms)
        jsx_count = len(set(r.field_path for r in flow.jsx_refs))
        fns = ', '.join(f.fetch_function for f in flow.fetches)
        print(f"  {flow.component_name}")
        print(f"    fetches: {fetch_count} | chains: {chain_count} | jsx refs: {jsx_count}")
        if fns:
            print(f"    calls: {fns}")
        print()


def cmd_stats(args):
    flows = build_all_dataflows(_WORKSPACE)
    print("TRANSFORM STATISTICS")
    print(f"  Components with data flow: {len(flows)}")
    print(f"  Total fetch bindings:      {sum(len(f.fetches) for f in flows)}")
    print(f"  Total transform chains:    {sum(len(f.transforms) for f in flows)}")
    print(f"  Total JSX references:      {sum(len(f.jsx_refs) for f in flows)}")
    print()

    # Components with most transforms
    if flows:
        by_chains = sorted(flows, key=lambda f: len(f.transforms), reverse=True)
        print("  Most transform chains:")
        for f in by_chains[:5]:
            if f.transforms:
                print(f"    {f.component_name}: {len(f.transforms)} chains")

    # Most common operations
    all_ops: dict[str, int] = {}
    for f in flows:
        for tc in f.transforms:
            for op in tc.operations:
                all_ops[op] = all_ops.get(op, 0) + 1
    if all_ops:
        print()
        print("  Most common operations:")
        for op, count in sorted(all_ops.items(), key=lambda x: -x[1])[:8]:
            print(f"    {op}: {count}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog='comp-transform',
        description='Trace client-side data flow inside React components.',
    )
    sub = parser.add_subparsers(dest='command')

    p_trace = sub.add_parser('trace', help='Full data flow for one component')
    p_trace.add_argument('component', help='Component name (fuzzy match)')
    p_trace.add_argument('--json', action='store_true')

    p_fields = sub.add_parser('fields', help='Which response fields are actually used')
    p_fields.add_argument('component')

    p_chains = sub.add_parser('chains', help='useMemo/useCallback transformation chains')
    p_chains.add_argument('component')

    p_unused = sub.add_parser('unused', help='Response fields fetched but never rendered')
    p_unused.add_argument('component')

    p_schema = sub.add_parser('schema-check', help='Cross-reference rendered fields against response type schema')
    p_schema.add_argument('component')
    p_schema.add_argument(
        '--feature', default='', metavar='TOKEN',
        help='Escalate UNUSED fields containing TOKEN to WARN with routing ternary hint. '
             'Use when building a new cohort/mode. Example: --feature ofc'
    )

    p_ternary = sub.add_parser(
        'ternary-audit',
        help='Find ternary chains on union-typed variables missing branches (e.g. cohort === "geo" but no "ofc" branch)'
    )
    p_ternary.add_argument('component', help='Component name (fuzzy match)')
    p_ternary.add_argument(
        '--var', nargs='+', metavar='VAR',
        help='Manually specify variable names to audit (in addition to auto-detected ones)'
    )
    p_ternary.add_argument(
        '--verbose', action='store_true',
        help='Also print exhaustive ternaries (ones that handle all union members correctly)'
    )
    p_ternary.add_argument(
        '--all-unions', action='store_true', dest='all_unions',
        help='Include large unions (>6 members, e.g. TimePeriodKey) — may be noisy'
    )
    p_ternary.add_argument(
        '--strict', action='store_true',
        help='Flag single-implicit-fallthrough ternaries too (catches intentional patterns)'
    )

    sub.add_parser('all', help='Summary of all components with data flow')
    sub.add_parser('stats', help='Statistics')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        'trace': cmd_trace,
        'fields': cmd_fields,
        'chains': cmd_chains,
        'unused': cmd_unused,
        'schema-check': cmd_schema_check,
        'ternary-audit': cmd_ternary_audit,
        'all': cmd_all,
        'stats': cmd_stats,
    }
    commands[args.command](args)


if __name__ == '__main__':
    main()
