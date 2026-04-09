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

import argparse
import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_transforms import build_component_dataflow, build_all_dataflows
from org.modules.graph.extract_routes import build_routing_table
from org.modules.graph.extract_pipeline import build_pipeline_dag


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
                    print(f"    cloudfront: (no behavior match)")
            else:
                print(f"    url: (not resolved)")

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
    pad = " " * indent

    # Normalize s3_key: remove {param} wildcards for matching
    import re
    normalized = re.sub(r'\{[^}]+\}', '*', s3_key)

    # Find writers
    writers = []
    for sid, sio in dag.scripts.items():
        for wk in sio.write_keys:
            # Match exact or wildcard
            if wk == s3_key or wk == normalized or s3_key.startswith(wk.rstrip('*')):
                writers.append(sid)
                break

    if writers:
        for w in writers:
            print(f"{pad}gold script: {w}")
            upstream = dag.feeds(w)
            if upstream:
                scripts = sorted(set(u for u, _, _ in upstream))
                print(f"{pad}  fed by: {', '.join(scripts)}")
    else:
        # Try prefix match for entity/partitioned keys
        for sid, sio in dag.scripts.items():
            for wk in sio.write_keys:
                if '*' in wk and s3_key.startswith(wk.split('*')[0]):
                    writers.append(sid)
                    break
        if writers:
            for w in sorted(set(writers)):
                print(f"{pad}gold script: {w} (prefix match)")


def cmd_reverse(args):
    """Reverse lookup: S3 key -> routes -> components."""
    s3_key = args.s3_key
    rt = build_routing_table(_WORKSPACE)
    dag = build_pipeline_dag(_WORKSPACE)
    dag.build_index()

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
        # Try matching via rewrite rules
        for rule in rt.rewrite_rules:
            if s3_key.startswith(rule.s3_prefix):
                suffix = s3_key[len(rule.s3_prefix):]
                url = rule.url_prefix + suffix
                print(f"    URL (reconstructed): {url}")
                behavior = rt.match_behavior(url)
                if behavior:
                    print(f"      CF: {behavior.path_pattern} -> {behavior.origin_id}")
                break
        else:
            print("    (no matching routes found)")

    # Find components that render data from this key's route
    print()
    print("  CONSUMED BY:")
    component_names = set()
    for r in matching_routes:
        component_names.update(r.components)
    if component_names:
        for cn in sorted(component_names):
            print(f"    {cn}")
    else:
        print("    (no components found)")


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
