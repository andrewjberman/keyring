#!/usr/bin/env python3
"""
comp-platinum -- full-stack trace from portal page to gold script.

Chains together comp-transform + comp-routes + comp-pipescript to answer:
"For a given portal page/tab, what platinum/gold files does it need,
what fields does it render, and what gold scripts produce those files?"

Usage:
    comp-platinum page PartnerAnalytics     # full-stack trace for one component
    comp-platinum page ClientsTab           # full-stack trace for Books tab
    comp-platinum reverse gold/artifacts/employee_leaderboard.json  # S3 key -> routes -> components
    comp-platinum tab-audit                 # audit every ADVI tab (Phase 2 shortcut)
    comp-platinum summary                   # one-line summary per component
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_transforms import build_component_dataflow, build_all_dataflows  # noqa: E402
from org.modules.graph.extract_routes import build_routing_table  # noqa: E402
from org.modules.graph.extract_pipeline import build_pipeline_dag  # noqa: E402

_FIELD_QUERY_ARTIFACT_SUFFIXES = ('.json', '.parquet', '.csv')
_FIELD_QUERY_SKIP_PARTS = {
    'map', 'filter', 'find', 'some', 'every', 'reduce', 'forEach', 'flatMap',
    'sort', 'slice', 'length', 'includes', 'indexOf', 'keys', 'values',
    'entries', 'push', 'pop', 'concat', 'join', 'toString', 'toFixed',
    'toLocaleString', 'trim', 'toLowerCase', 'toUpperCase', 'startsWith',
    'endsWith', 'replace', 'split', 'match', 'search', 'charAt', 'substring',
}


def _find_component(query: str) -> Path | None:
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


def cmd_page(args):
    path = _find_component(args.component)
    if not path:
        print(f"Component not found: {args.component}")
        sys.exit(1)

    flow = build_component_dataflow(path, _WORKSPACE)
    if not flow:
        print(f"Could not parse: {path}")
        sys.exit(1)

    rt = build_routing_table(_WORKSPACE)
    dag = build_pipeline_dag(_WORKSPACE)
    dag.build_index()

    print(f"FULL-STACK TRACE: {flow.component_name}")
    print(f"  File: {flow.file_path}")
    print()

    if not flow.fetches:
        print("  No fetches detected in this component.")
        return

    for fb in flow.fetches:
        print(f"  FETCH: {fb.fetch_function}()")
        if fb.response_type:
            print(f"    response type: {fb.response_type}")
        if fb.query_key:
            print(f"    cache key: [{fb.query_key}]")
        print(f"    hook: {fb.hook_type} -> {fb.data_variable or '(destructured)'}")

        # Find route for this endpoint
        route = next((r for r in rt.routes if r.endpoint_function == fb.fetch_function), None)
        if route:
            print(f"    url: {route.url_pattern}")
            print(f"    cloudfront: {route.cf_behavior} -> {route.cf_origin} ({route.cf_origin_type})")
            auth_parts = []
            if route.auth_edge:
                auth_parts.append("edge JWT")
            if route.auth_api_gw:
                auth_parts.append("API GW authorizer")
            if not auth_parts:
                auth_parts.append("NONE")
            print(f"    auth: {' + '.join(auth_parts)}")
            if route.edge_router:
                print(f"    router: {route.edge_router}")
            if route.s3_key:
                print(f"    s3 key: {route.s3_key}")
                _print_gold_source(dag, route.s3_key, indent=4)
            elif route.lambda_handler:
                print(f"    lambda: {route.lambda_handler}")
                if route.api_gw_route:
                    print(f"    api gw route: {route.api_gw_route}")
        else:
            # Try matching by endpoint name in routes
            ep = rt.endpoints.get(fb.fetch_function)
            if ep and ep.url_template:
                print(f"    url: {ep.url_template}")
                behavior = rt.match_behavior(ep.url_template)
                if behavior:
                    print(f"    cloudfront: {behavior.path_pattern} -> {behavior.origin_id}")
                else:
                    print("    cloudfront: (no behavior match)")
            else:
                print("    url: (not resolved)")

        # Show transform chains that use this fetch's data
        related_chains = [tc for tc in flow.transforms
                          if fb.data_variable and fb.data_variable in tc.input_variables]
        if related_chains:
            print(f"    transforms ({len(related_chains)}):")
            for tc in related_chains:
                ops = f" [{', '.join(tc.operations)}]" if tc.operations else ""
                print(f"      -> {tc.output_variable}{ops}")
                if tc.field_accesses:
                    for fa in tc.field_accesses[:5]:
                        print(f"           {fa}")
                    if len(tc.field_accesses) > 5:
                        print(f"           ... +{len(tc.field_accesses) - 5} more")

        # Show JSX references for this fetch's data or its transforms
        related_vars = {fb.data_variable} if fb.data_variable else set()
        related_vars.update(tc.output_variable for tc in related_chains)
        related_jsx = [r for r in flow.jsx_refs if r.variable in related_vars]
        if related_jsx:
            seen = set()
            unique = []
            for r in related_jsx:
                if r.field_path not in seen:
                    seen.add(r.field_path)
                    unique.append(r)
            print(f"    rendered ({len(unique)} fields):")
            for r in unique[:10]:
                print(f"      L{r.line_number}: {r.field_path} ({r.context})")
            if len(unique) > 10:
                print(f"      ... +{len(unique) - 10} more")

        print()

    # Response type field summary
    if flow.response_types:
        import re
        used_names = set()
        for u in flow.fields_used():
            normalized = re.sub(r'\?\.|[\[\]?]', '.', u)
            parts = [p for p in normalized.split('.') if p and p.isidentifier()]
            used_names.update(parts)

        for type_name, fields in flow.response_types.items():
            used_fields = [f for f in fields if f.name in used_names]
            unused_fields = [f for f in fields if f.name not in used_names]
            print(f"  RESPONSE TYPE: {type_name} ({len(used_fields)}/{len(fields)} fields used)")
            if unused_fields:
                print(f"    unused: {', '.join(f.name for f in unused_fields)}")
        print()


def _print_gold_source(dag, s3_key: str, indent: int = 4):
    """Print which gold script writes this S3 key and what feeds it."""
    import re
    pad = " " * indent

    # Normalize s3_key: remove {param} wildcards for matching
    normalized = re.sub(r'\{[^}]+\}', '*', s3_key)

    # Find writers and the specific write-constant that matched
    writer_info: list[tuple[str, str]] = []  # [(script_id, write_key)]
    for sid, sio in dag.scripts.items():
        for wk in sio.write_keys:
            if wk == s3_key or wk == normalized or s3_key.startswith(wk.rstrip('*')):
                writer_info.append((sid, wk))
                break

    if writer_info:
        for w, wk in writer_info:
            # Find the function name from the script that produces this key
            sio = dag.scripts[w]
            fn_name = _find_producer_function(sio, wk)
            fn_str = f" :: {fn_name}()" if fn_name else ""
            print(f"{pad}gold script: {w}{fn_str}")
            upstream = dag.feeds(w)
            if upstream:
                scripts = sorted(set(u for u, _, _ in upstream))
                print(f"{pad}  fed by: {', '.join(scripts)}")
    else:
        # Try prefix match for entity/partitioned keys
        prefix_writers: list[tuple[str, str]] = []
        for sid, sio in dag.scripts.items():
            for wk in sio.write_keys:
                if '*' in wk and s3_key.startswith(wk.split('*')[0]):
                    prefix_writers.append((sid, wk))
                    break
        if prefix_writers:
            for w, wk in sorted(set(prefix_writers)):
                sio = dag.scripts[w]
                fn_name = _find_producer_function(sio, wk)
                fn_str = f" :: {fn_name}()" if fn_name else ""
                print(f"{pad}gold script: {w}{fn_str} (prefix match)")


def _find_producer_function(sio, write_key: str) -> str:
    """Heuristically find the function name in a gold script that writes a given key.
    Scans the script file for function defs that co-occur with the key string."""
    import re
    try:
        from pathlib import Path
        content = Path(sio.file_path).read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""

    # Extract just the filename stem from write_key for matching
    # e.g., platinum/firm/mix_summary.json -> mix_summary
    key_stem = re.sub(r'[{*}]', '', write_key.split('/')[-1].replace('.json', '').replace('.parquet', ''))

    # Find function defs near usage of this key
    fn_pattern = re.compile(r'def\s+(\w+)\s*\(')
    lines = content.splitlines()
    last_fn = ""
    for i, line in enumerate(lines):
        m = fn_pattern.match(line.strip())
        if m:
            last_fn = m.group(1)
        if key_stem and key_stem.replace('-', '_') in line.replace('-', '_'):
            if last_fn and not last_fn.startswith('_') and last_fn != 'main':
                return last_fn
    return ""


def _normalize_field_path(path: str) -> str:
    normalized = re.sub(r'\?\.|[\[\]?]', '.', path)
    parts = [p for p in normalized.split('.') if p and p.isidentifier() and p not in _FIELD_QUERY_SKIP_PARTS]
    return '.'.join(parts)


def _has_wildcard_segments(path: str) -> bool:
    """Return True if path contains * or {name} wildcard segments."""
    return '*' in path or bool(re.search(r'\{[^}]+\}', path))


def _normalize_field_path_wildcard(path: str) -> str:
    """Like _normalize_field_path but preserves segments containing * or {name}."""
    normalized = re.sub(r'\?\.|[\[\]?]', '.', path)
    parts = []
    for p in normalized.split('.'):
        if not p:
            continue
        if '*' in p or re.search(r'\{[^}]+\}', p):
            parts.append(p)  # wildcard/dynamic segments preserved as-is
        elif p.isidentifier() and p not in _FIELD_QUERY_SKIP_PARTS:
            parts.append(p)
    return '.'.join(parts)


def _wildcard_to_regex(pattern: str) -> re.Pattern:
    """Convert a normalized wildcard path pattern to a compiled regex.

    A bare * segment matches any single non-dot segment.
    A glob segment like decomposition_* matches strings starting with that prefix.
    A {name} segment matches any single non-dot segment (dynamic key).
    Pattern matches the full index key OR as a trailing suffix (.pattern).
    """
    regex_parts = []
    for seg in pattern.split('.'):
        if re.fullmatch(r'\{[^}]+\}', seg):
            regex_parts.append(r'[^.]+')
        elif '*' in seg:
            regex_parts.append(re.escape(seg).replace(r'\*', r'[^.]*'))
        else:
            regex_parts.append(re.escape(seg))
    inner = r'\.'.join(regex_parts)
    return re.compile(r'(?:(?:^|\.)' + inner + r')$')


def _looks_like_artifact_query(query: str) -> bool:
    if '/' in query:
        return True
    return query.endswith(_FIELD_QUERY_ARTIFACT_SUFFIXES)


def _build_field_reverse_index(rt) -> dict[str, list[dict]]:
    route_by_endpoint = {r.endpoint_function: r for r in rt.routes}
    index: dict[str, list[dict]] = {}

    for flow in build_all_dataflows(_WORKSPACE):
        all_fields = {_normalize_field_path(f) for f in flow.fields_used()}
        all_fields.discard("")

        for fb in flow.fetches:
            if not fb.data_variable:
                continue

            route = route_by_endpoint.get(fb.fetch_function)
            if not route:
                continue

            data_var = fb.data_variable
            prefix = f"{data_var}."
            matched_fields = []
            for field in all_fields:
                if field == data_var:
                    continue
                if field.startswith(prefix):
                    matched_fields.append(field[len(prefix):])
                    continue
                parts = field.split('.')
                if data_var in parts:
                    suffix = '.'.join(parts[parts.index(data_var) + 1:])
                    if suffix:
                        matched_fields.append(suffix)

            for field_path in sorted(set(f for f in matched_fields if f)):
                entry = {
                    "component": flow.component_name,
                    "endpoint_function": fb.fetch_function,
                    "url_pattern": route.url_pattern,
                    "cf_behavior": route.cf_behavior,
                    "cf_origin": route.cf_origin,
                    "cf_origin_type": route.cf_origin_type,
                    "auth_edge": route.auth_edge,
                    "auth_api_gw": route.auth_api_gw,
                    "s3_key": route.s3_key,
                    "lambda_handler": route.lambda_handler,
                }
                index.setdefault(field_path, []).append(entry)

    return index


def _artifact_stems_matching(dag, query: str) -> list[str]:
    """Return DAG write-keys whose basename stem contains `query`.
    Used for empty-vs-broken disambiguation on reverse lookups."""
    if not query:
        return []
    hits = []
    seen = set()
    for sio in dag.scripts.values():
        for wk in sio.write_keys:
            stem = wk.rsplit('/', 1)[-1]
            stem = stem.replace('.json', '').replace('.parquet', '').replace('.csv', '')
            stem = re.sub(r'[{*}]', '', stem).strip('_-')
            if query in stem and wk not in seen:
                hits.append(wk)
                seen.add(wk)
    return hits


def _portal_grep_hits(query: str, limit: int = 3) -> list[str]:
    """Best-effort raw-text search of portal/src for the query string.
    Returns up to `limit` 'file:line:snippet' hits. Used to detect extractor gaps:
    if the field appears in portal source but the dataflow index missed it."""
    if not query or len(query) < 3:
        return []
    portal_src = _WORKSPACE / "portal" / "src"
    if not portal_src.exists():
        return []
    hits = []
    for p in portal_src.rglob("*.ts*"):
        try:
            for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if query in line:
                    rel = p.relative_to(_WORKSPACE)
                    snippet = line.strip()[:80]
                    hits.append(f"{rel}:{i}: {snippet}")
                    if len(hits) >= limit:
                        return hits
                    break
        except Exception:
            continue
    return hits


def _print_field_reverse(query: str, rt, dag):
    index = _build_field_reverse_index(rt)
    is_wildcard = _has_wildcard_segments(query)
    has_dynamic = bool(re.search(r'\{[^}]+\}', query))

    if is_wildcard:
        query_normalized = _normalize_field_path_wildcard(query)
        _pat = _wildcard_to_regex(query_normalized)
        matches = sorted({fp for fp in index if _pat.search(fp)})
    else:
        query_normalized = _normalize_field_path(query)
        # ADHC_ROUTER.T1 fix: original matcher included
        # `query_normalized.endswith(f".{field_path}")` and
        # `query_normalized in field_path`, producing false positives by
        # matching on trailing segments. For query `rfs.decomposition_max.nna`,
        # this falsely surfaced artifacts carrying a plain `nna` field (e.g.
        # timeseries_overview.json) because `"rfs.decomposition_max.nna"
        # .endswith(".nna")` is True. Strict matching: exact hit OR query is a
        # suffix of an indexed path (`field_path.endswith(f".{query}")`). An
        # honest empty result is strictly better than a confident wrong one.
        matches = sorted({
            field_path for field_path in index
            if field_path == query_normalized
            or field_path.endswith(f".{query_normalized}")
        })

    print(f"REVERSE LOOKUP: {query}")
    if is_wildcard:
        wc_type = "WILDCARD/DYNAMIC" if has_dynamic else "WILDCARD"
        print(f"  [routed as: FIELD query ({wc_type}); pattern='{query_normalized}'; index size: {len(index)} field paths]")
    else:
        print(f"  [routed as: FIELD query; normalized='{query_normalized}'; index size: {len(index)} field paths]")
    if has_dynamic:
        dyn_keys = re.findall(r'\{([^}]+)\}', query)
        print(f"  NOTE: dynamic segment(s) {', '.join('{' + k + '}' for k in dyn_keys)} treated as wildcards "
              f"-- matches any value at that key position in the JSON path.")
    print()

    if not matches:
        # Empty-vs-broken disambiguation (ADHC_ROUTER.T3 2026-04-15):
        # print a diagnostic footer so agents can tell "tool searched and found
        # nothing" apart from "tool didn't route the query correctly".
        artifact_stem_hits = _artifact_stems_matching(dag, query_normalized)
        portal_text_hits = _portal_grep_hits(query_normalized, limit=3)
        print("  PRODUCER:")
        print("    (no payload-path matches found in portal dataflow index)")
        print()
        print("  SERVED VIA:")
        print("    (no matching routes found)")
        print()
        print("  CONSUMED BY:")
        print("    (no components found in dataflow index)")
        print()
        print("  ---- DIAGNOSTIC (empty result, 0/{} fields matched) ----".format(len(index)))
        print("  Distinguish empty-vs-broken:")
        print("    [a] genuine empty: no portal component reads this field (new canonical, not-yet-wired field, or consumer-less artifact).")
        print("    [b] query mis-routed: query may name an artifact, not a field.")
        print("    [c] index stale: dataflow extractor may not have picked up recent portal changes (re-run comp-build).")
        print("    [d] extractor gap: field is in portal source but indexer does not capture this access pattern (m.foo in iteration scopes, destructuring after cast, etc.).")
        if artifact_stem_hits:
            print(f"  HINT: {len(artifact_stem_hits)} DAG artifact(s) have basename stem containing '{query_normalized}':")
            for key in artifact_stem_hits[:5]:
                print(f"    comp-platinum reverse {key}")
        if portal_text_hits:
            print(f"  HINT: {len(portal_text_hits)} raw portal source hit(s) on '{query_normalized}' (may indicate indexer gap):")
            for hit in portal_text_hits:
                print(f"    {hit}")
        if not artifact_stem_hits and not portal_text_hits:
            print(f"  Query '{query_normalized}' not found anywhere in DAG artifacts or portal source -- likely genuinely absent (case [a]).")
        return

    entries = []
    for field_path in matches:
        for entry in index[field_path]:
            entries.append((field_path, entry))

    print("  PRODUCER:")
    seen_s3 = set()
    printed_producer = False
    for _, entry in entries:
        s3_key = entry.get("s3_key", "")
        if not s3_key or s3_key in seen_s3:
            continue
        seen_s3.add(s3_key)
        print(f"    field path: {query_normalized} -> {s3_key}")
        _print_gold_source(dag, s3_key, indent=6)
        printed_producer = True
    if not printed_producer:
        print("    (no S3-backed producer resolved)")

    print()
    print("  SERVED VIA:")
    seen_routes = set()
    for field_path, entry in entries:
        route_key = (entry["endpoint_function"], entry["url_pattern"], field_path)
        if route_key in seen_routes:
            continue
        seen_routes.add(route_key)
        auth_tag = []
        if entry.get("auth_edge"):
            auth_tag.append("edge")
        if entry.get("auth_api_gw"):
            auth_tag.append("apigw")
        auth_str = "+".join(auth_tag) if auth_tag else "none"
        print(f"    {entry['endpoint_function']}: {entry['url_pattern']}")
        print(f"      field: {field_path}")
        print(f"      CF: {entry['cf_behavior']} -> {entry['cf_origin']} ({entry['cf_origin_type']}, auth={auth_str})")
        if entry.get("lambda_handler"):
            print(f"      lambda: {entry['lambda_handler']}")
        if entry.get("s3_key"):
            print(f"      s3 key: {entry['s3_key']}")

    print()
    print("  CONSUMED BY:")
    seen_components = set()
    for field_path, entry in entries:
        comp_key = (entry["component"], field_path, entry["endpoint_function"])
        if comp_key in seen_components:
            continue
        seen_components.add(comp_key)
        print(f"    {entry['component']} via {entry['endpoint_function']} ({field_path})")


def _print_artifact_reverse(s3_key: str, rt, dag):
    print(f"REVERSE LOOKUP: {s3_key}")
    print()

    # Find gold script that writes this key
    print("  PRODUCER:")
    _print_gold_source(dag, s3_key, indent=4)

    # Find routes that resolve to this S3 key
    print()
    print("  SERVED VIA:")
    matching_routes = []
    for route in rt.routes:
        if route.s3_key and (route.s3_key == s3_key or
            s3_key.startswith(route.s3_key.split('{')[0].split('*')[0])):
            matching_routes.append(route)

    reconstructed_url = ""
    if matching_routes:
        for r in matching_routes:
            auth_tag = ""
            if r.auth_edge:
                auth_tag = " [AUTH:edge"
                if r.auth_api_gw:
                    auth_tag += "+apigw"
                auth_tag += "]"
            print(f"    {r.endpoint_function}: {r.url_pattern}")
            print(f"      CF: {r.cf_behavior} -> {r.cf_origin}{auth_tag}")
            if r.components:
                print(f"      components: {', '.join(r.components)}")
    else:
        # Try matching via rewrite rules (reverse: S3 key -> URL)
        for rule in rt.rewrite_rules:
            if s3_key.startswith(rule.s3_prefix):
                suffix = s3_key[len(rule.s3_prefix):]
                reconstructed_url = rule.url_prefix + suffix
                print(f"    URL (reconstructed): {reconstructed_url}")
                behavior = rt.match_behavior(reconstructed_url)
                if behavior:
                    auth_tag = " [AUTH]" if behavior.has_auth else ""
                    print(f"      CF: {behavior.path_pattern} -> {behavior.origin_id}{auth_tag}")
                break
        else:
            print("    (no matching routes found)")

    # Find components that render data from this key's route
    print()
    print("  CONSUMED BY:")
    component_names = set()
    for r in matching_routes:
        component_names.update(r.components)

    # Fallback 1: search by endpoint function URLs matching the reconstructed URL
    # Handles platinum paths that route via API GW (s3_key not set on route objects)
    if not component_names and reconstructed_url:
        url_prefix = reconstructed_url.split('{')[0]
        for fn_name, ep in rt.endpoints.items():
            if not ep.url_template:
                continue
            ep_prefix = ep.url_template.split('{')[0]
            if ep_prefix and (ep_prefix == url_prefix or
                              url_prefix.startswith(ep_prefix) or
                              ep_prefix.startswith(url_prefix)):
                for comp in rt.components:
                    if fn_name in comp.endpoint_calls:
                        component_names.add(comp.name)

    # Fallback 2: directory-prefix match
    # Some keys (e.g. platinum/firm/fee_efficiency.json) are sub-fields of a larger
    # aggregate response (e.g. platinum/firm/dashboard.json fetched by getPlatinumFirmDashboard).
    # Search for endpoints whose URL shares the same directory prefix.
    if not component_names and s3_key:
        key_dir = s3_key.rsplit('/', 1)[0]  # e.g. platinum/firm
        sibling_fns: list[str] = []
        for fn_name, ep in rt.endpoints.items():
            if not ep.url_template:
                continue
            # Resolve URL to S3 key via rewrite rules
            resolved = rt.resolve_s3_key(ep.url_template.split('{')[0])
            if not resolved:
                # Try stripping query params
                resolved = rt.resolve_s3_key(ep.url_template.split('?')[0])
            if resolved:
                ep_dir = resolved.rsplit('/', 1)[0]
                if ep_dir == key_dir:
                    sibling_fns.append(fn_name)
        if sibling_fns:
            # ADHC_ROUTER.T3: this fallback is speculative (directory-prefix
            # match, not actual key match). Flag explicitly so agents do not
            # treat it as ground-truth consumer attribution.
            print("    WARN: SPECULATIVE MATCH (directory-prefix fallback, not a verified consumer).")
            print("    WARN: These endpoints live in the same S3 directory but may not read this specific key.")
            for fn_name in sorted(sibling_fns):
                ep = rt.endpoints[fn_name]
                for comp in rt.components:
                    if fn_name in comp.endpoint_calls:
                        component_names.add(comp.name)
                        print(f"    via {fn_name} ({ep.url_template}) -> {comp.name}")

    if component_names:
        for cn in sorted(component_names):
            if cn not in s3_key:  # avoid double-printing from fallback 2
                print(f"    {cn}")
    elif not (s3_key and any(
        rt.resolve_s3_key(ep.url_template.split('{')[0]).rsplit('/', 1)[0] ==
        s3_key.rsplit('/', 1)[0]
        for ep in rt.endpoints.values()
        if ep.url_template and rt.resolve_s3_key(ep.url_template.split('{')[0])
    )):
        print("    (no components found -- check Lambda@Edge handlers for this key)")


def cmd_reverse(args):
    """Reverse lookup: S3 key OR payload field path -> routes -> components.

    Routing:
      - If query contains '/' or ends with .json/.parquet/.csv -> artifact reverse.
      - Else: check if query matches a DAG artifact filename stem; if so,
        try artifact reverse against the matched key(s) first, then fall through
        to field reverse. This disambiguates queries like 'advisor_fee_efficiency'
        which previously routed as FIELD and returned empty because the index
        only holds sub-fields of fetch data variables.
    """
    query = args.s3_key
    rt = build_routing_table(_WORKSPACE)
    dag = build_pipeline_dag(_WORKSPACE)
    dag.build_index()

    if _looks_like_artifact_query(query):
        _print_artifact_reverse(query, rt, dag)
        return

    # ADHC_ROUTER.T3: auto-probe artifact-stem match before field reverse.
    stem_hits = _artifact_stems_matching(dag, _normalize_field_path(query))
    if stem_hits:
        # Exact basename match(es) -- run artifact reverse, not field.
        exact = [k for k in stem_hits
                 if re.sub(r'[{*}]', '', k.rsplit('/', 1)[-1].split('.')[0]).strip('_-')
                    == _normalize_field_path(query)]
        target_keys = exact or stem_hits[:1]
        print(f"  [routed as: ARTIFACT (stem match); query='{query}' -> {target_keys[0]}]")
        print()
        _print_artifact_reverse(target_keys[0], rt, dag)
        if len(target_keys) > 1 or (len(stem_hits) > len(target_keys)):
            print()
            print(f"  (additional {len(stem_hits) - 1} stem matches; re-run with full S3 key to disambiguate)")
        return

    _print_field_reverse(query, rt, dag)


def cmd_tab_audit(args):
    """Run full-stack trace for every ADVI tab component."""
    advi_components = [
        "PartnerAnalytics",
        "DistributionTab",
        "AdvisorsTab",
        "ClientsTab",
        "AssetIntelligenceTab",
        "ClientDetailPage",
        "MixTimeseriesPanel",
        "ConcentrationPanel",
        "FeeEfficiencyPanel",
        "FeeRoleBreakdownPanel",
        "FeeSummaryPanel",
    ]

    rt = build_routing_table(_WORKSPACE)
    dag = build_pipeline_dag(_WORKSPACE)
    dag.build_index()

    for comp_name in advi_components:
        path = _find_component(comp_name)
        if not path:
            print(f"SKIP: {comp_name} (not found)")
            print()
            continue

        flow = build_component_dataflow(path, _WORKSPACE)
        if not flow or not flow.fetches:
            print(f"SKIP: {comp_name} (no fetches)")
            print()
            continue

        print(f"{'=' * 70}")
        print(f"TAB: {comp_name}")
        print(f"{'=' * 70}")

        for fb in flow.fetches:
            route = next((r for r in rt.routes if r.endpoint_function == fb.fetch_function), None)

            origin_type = route.cf_origin_type if route else "?"
            s3_key = route.s3_key if route else ""
            auth = "edge" if route and route.auth_edge else ""
            if route and route.auth_api_gw:
                auth += "+apigw" if auth else "apigw"
            auth = auth or "none"

            # Find gold source
            gold_source = ""
            if s3_key:
                import re
                normalized = re.sub(r'\{[^}]+\}', '*', s3_key)
                for sid, sio in dag.scripts.items():
                    for wk in sio.write_keys:
                        if wk == s3_key or wk == normalized or s3_key.startswith(wk.rstrip('*')):
                            gold_source = sid
                            break
                    if gold_source:
                        break

            # Count transforms
            chain_count = len([tc for tc in flow.transforms
                              if fb.data_variable and fb.data_variable in tc.input_variables])

            print(f"  {fb.fetch_function}()")
            print(f"    origin: {origin_type} | auth: {auth} | transforms: {chain_count}")
            if s3_key:
                print(f"    s3: {s3_key}")
            if gold_source:
                print(f"    gold: {gold_source}")
            if route and route.lambda_handler:
                print(f"    lambda: {route.lambda_handler}")

        print()


def cmd_summary(args):
    """One-line summary per component."""
    flows = build_all_dataflows(_WORKSPACE)
    rt = build_routing_table(_WORKSPACE)

    print(f"FULL-STACK SUMMARY ({len(flows)} components)")
    print()
    print(f"  {'Component':<25} {'Fetches':<8} {'Chains':<8} {'S3 Direct':<10} {'API GW':<8} {'Auth'}")
    print(f"  {'-'*25} {'-'*7} {'-'*7} {'-'*9} {'-'*7} {'-'*10}")

    for flow in sorted(flows, key=lambda f: f.component_name):
        fetch_count = len(flow.fetches)
        chain_count = len(flow.transforms)

        s3_count = 0
        apigw_count = 0
        auth_count = 0
        for fb in flow.fetches:
            route = next((r for r in rt.routes if r.endpoint_function == fb.fetch_function), None)
            if route:
                if route.cf_origin_type == "s3":
                    s3_count += 1
                elif route.cf_origin_type == "api_gateway":
                    apigw_count += 1
                if route.auth_edge:
                    auth_count += 1

        print(f"  {flow.component_name:<25} {fetch_count:<8} {chain_count:<8} {s3_count:<10} {apigw_count:<8} {auth_count}/{fetch_count}")


def main():
    parser = argparse.ArgumentParser(
        prog='comp-platinum',
        description='Full-stack trace from portal page to gold script.',
    )
    sub = parser.add_subparsers(dest='command')

    p_page = sub.add_parser('page', help='Full-stack trace for one component')
    p_page.add_argument('component', help='Component name')
    p_page.add_argument('--json', action='store_true')

    p_rev = sub.add_parser('reverse', help='S3 key -> routes -> components')
    p_rev.add_argument('s3_key', help='S3 key (e.g., gold/artifacts/employee_leaderboard.json)')

    sub.add_parser('tab-audit', help='Audit every ADVI tab')
    sub.add_parser('summary', help='One-line summary per component')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        'page': cmd_page,
        'reverse': cmd_reverse,
        'tab-audit': cmd_tab_audit,
        'summary': cmd_summary,
    }
    commands[args.command](args)


if __name__ == '__main__':
    main()
