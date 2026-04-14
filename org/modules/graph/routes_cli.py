#!/usr/bin/env python3
"""
comp-routes -- trace the full serving path from S3 artifact to frontend component.

Usage:
    comp-routes trace /api/scoped/advisor-intelligence/artifacts/employee_leaderboard.json
    comp-routes trace getEmployeeLeaderboard
    comp-routes trace PartnerAnalytics
    comp-routes behaviors                    # list all CloudFront behaviors
    comp-routes origins                      # list all CloudFront origins
    comp-routes rewrites                     # list all URL->S3 rewrite rules
    comp-routes api-routes                   # list all API Gateway routes
    comp-routes endpoints                    # list all frontend endpoint functions with URLs
    comp-routes components                   # list all components with their endpoint calls
    comp-routes auth-map                     # which paths have which auth layers
    comp-routes edge-versions                # Lambda@Edge version pinning scanner
    comp-routes stats                        # routing table statistics

Authoritative sources:
    cloudfront-distribution.tf  -- behaviors, origins, Lambda@Edge
    shared-advisor-router/index.mjs -- URL rewrite rules
    api-gateway.tf files -- API GW routes
    portal/src/api/endpoints/*.ts -- frontend fetch functions
    portal/src/pages/**/*.tsx -- component -> endpoint calls
"""

import argparse
import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_routes import build_routing_table, parse_edge_versions


def _build_rt():
    return build_routing_table(_WORKSPACE)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_trace(args):
    rt = _build_rt()
    query = args.query

    # Determine what was queried: URL, endpoint function, or component
    matched_routes = []

    if query.startswith('/'):
        # URL query -- find routes whose url_pattern matches
        matched_routes = [r for r in rt.routes if query in r.url_pattern or r.url_pattern in query]
        if not matched_routes:
            # Try CloudFront behavior match
            behavior = rt.match_behavior(query)
            if behavior:
                print(f"URL matches CloudFront behavior: {behavior.path_pattern}")
                print(f"  Origin: {behavior.origin_id}")
                print(f"  Auth: {'yes' if behavior.has_auth else 'no'}")
                print(f"  Router: {'yes' if behavior.has_router else 'no'}")
                for ef in behavior.edge_functions:
                    print(f"  Edge: {ef.event_type} -> {ef.function_name}")
                return
            else:
                print(f"No route found for URL: {query}")
                return
    else:
        # Function name or component name
        # Check endpoints first
        if query in rt.endpoints:
            matched_routes = [r for r in rt.routes if r.endpoint_function == query]
        else:
            # Check components
            comp_matches = [c for c in rt.components if query.lower() in c.name.lower()]
            if comp_matches:
                for comp in comp_matches:
                    print(f"COMPONENT: {comp.name}")
                    print(f"  File: {comp.file_path}")
                    print(f"  Calls: {', '.join(comp.endpoint_calls)}")
                    print()
                    for fn in comp.endpoint_calls:
                        fn_routes = [r for r in rt.routes if r.endpoint_function == fn]
                        for r in fn_routes:
                            _print_route(r, indent=2)
                return
            else:
                # Fuzzy match on endpoint names
                matches = [fn for fn in rt.endpoints if query.lower() in fn.lower()]
                if matches:
                    for fn in matches:
                        fn_routes = [r for r in rt.routes if r.endpoint_function == fn]
                        for r in fn_routes:
                            _print_route(r)
                    return
                print(f"No match for: {query}")
                print(f"Try a URL (/api/...), endpoint function name, or component name.")
                return

    if args.json:
        print(json.dumps([{
            "url": r.url_pattern,
            "cf_behavior": r.cf_behavior,
            "cf_origin": r.cf_origin,
            "cf_origin_type": r.cf_origin_type,
            "auth_edge": r.auth_edge,
            "auth_api_gw": r.auth_api_gw,
            "edge_router": r.edge_router,
            "s3_key": r.s3_key,
            "api_gw_route": r.api_gw_route,
            "lambda_handler": r.lambda_handler,
            "endpoint_function": r.endpoint_function,
            "components": r.components,
        } for r in matched_routes], indent=2))
    else:
        for r in matched_routes:
            _print_route(r)


def _print_route(route, indent=0):
    pad = " " * indent
    print(f"{pad}ROUTE: {route.endpoint_function}")
    print(f"{pad}  URL: {route.url_pattern}")
    print(f"{pad}  CloudFront:")
    print(f"{pad}    behavior: {route.cf_behavior}")
    print(f"{pad}    origin:   {route.cf_origin} ({route.cf_origin_type})")
    print(f"{pad}  Auth:")
    print(f"{pad}    edge JWT: {'YES' if route.auth_edge else 'no'}")
    print(f"{pad}    API GW:   {'YES' if route.auth_api_gw else 'no'}")
    if route.edge_router:
        print(f"{pad}  Router: {route.edge_router}")
    if route.s3_key:
        print(f"{pad}  S3 key: {route.s3_key}")
    if route.api_gw_route:
        print(f"{pad}  API GW route: {route.api_gw_route}")
    if route.lambda_handler:
        print(f"{pad}  Lambda: {route.lambda_handler}")
    if route.components:
        print(f"{pad}  Components: {', '.join(route.components)}")
    print()


def cmd_behaviors(args):
    rt = _build_rt()
    print(f"CLOUDFRONT BEHAVIORS ({len(rt.behaviors)})")
    print()
    for b in rt.behaviors:
        origin = rt.origins.get(b.origin_id)
        origin_type = origin.origin_type if origin else "?"
        auth_tag = " [AUTH]" if b.has_auth else ""
        router_tag = " [ROUTER]" if b.has_router else ""
        comment = f" -- {b.comment}" if b.comment else ""
        print(f"  {b.order:2d}. {b.path_pattern}")
        print(f"      -> {b.origin_id} ({origin_type}){auth_tag}{router_tag}{comment}")
        for ef in b.edge_functions:
            print(f"         {ef.event_type}: {ef.function_name}")
        print()

    # Custom error responses -- these intercept status codes before they reach the browser
    if rt.custom_error_responses:
        print()
        print(f"CUSTOM ERROR RESPONSES ({len(rt.custom_error_responses)}):")
        print("  !! These intercept HTTP status codes -- Lambda/S3 errors may be hidden from browser")
        print()
        for cer in sorted(rt.custom_error_responses, key=lambda c: c.error_code):
            warn = ""
            if cer.error_code == 403:
                warn = "  !! WARN: Lambda 403 auth-denials will be swallowed -- browser gets {} {} not the Lambda error".format(
                    cer.response_code, cer.response_page_path)
            elif cer.error_code == 404:
                warn = "  !! WARN: S3 missing-key 404s will be swallowed -- SPA routing assumed"
            print(f"  HTTP {cer.error_code} -> {cer.response_code} {cer.response_page_path}  (ttl: {cer.ttl_seconds}s)")
            if warn:
                print(warn)
        print()


def cmd_origins(args):
    rt = _build_rt()
    print(f"CLOUDFRONT ORIGINS ({len(rt.origins)})")
    print()
    for oid, o in rt.origins.items():
        print(f"  {oid}")
        print(f"    domain: {o.domain_name}")
        print(f"    type:   {o.origin_type}")
        if o.bucket_name:
            print(f"    bucket: {o.bucket_name}")
        if o.origin_path:
            print(f"    path:   {o.origin_path}")
        if o.oai_or_oac:
            print(f"    access: {o.oai_or_oac}")
        print()


def cmd_rewrites(args):
    rt = _build_rt()
    print(f"URL -> S3 REWRITE RULES ({len(rt.rewrite_rules)})")
    print()
    for r in rt.rewrite_rules:
        print(f"  {r.url_prefix}")
        print(f"    -> {r.s3_prefix}")
        if r.condition:
            print(f"       ({r.condition})")
        print()


def cmd_api_routes(args):
    rt = _build_rt()
    print(f"API GATEWAY ROUTES ({len(rt.api_gw_routes)})")
    print()
    # Group by pipeline
    by_pipeline: dict[str, list] = {}
    for r in rt.api_gw_routes:
        by_pipeline.setdefault(r.pipeline, []).append(r)

    for pipeline, routes in sorted(by_pipeline.items()):
        print(f"  {pipeline}:")
        for r in routes:
            lambda_str = f" -> {r.lambda_name}" if r.lambda_name else ""
            print(f"    {r.route_key}{lambda_str}")
        print()


def cmd_endpoints(args):
    rt = _build_rt()
    # Filter to only endpoints with URLs
    with_urls = {k: v for k, v in rt.endpoints.items() if v.url_template}
    without_urls = {k: v for k, v in rt.endpoints.items() if not v.url_template}

    print(f"FRONTEND ENDPOINTS ({len(with_urls)} with URLs, {len(without_urls)} without)")
    print()

    # Group by source file
    by_file: dict[str, list[EndpointFunction]] = {}
    for ep in with_urls.values():
        by_file.setdefault(ep.source_file, []).append(ep)

    from org.modules.graph.extract_routes import EndpointFunction
    for src_file, eps in sorted(by_file.items()):
        print(f"  {src_file}:")
        for ep in sorted(eps, key=lambda e: e.name):
            print(f"    {ep.name}: {ep.url_template}")
        print()


def cmd_components(args):
    rt = _build_rt()
    print(f"COMPONENT -> ENDPOINT BINDINGS ({len(rt.components)})")
    print()
    for comp in sorted(rt.components, key=lambda c: c.name):
        print(f"  {comp.name} ({comp.file_path})")
        for fn in comp.endpoint_calls:
            ep = rt.endpoints.get(fn)
            url = ep.url_template if ep else "?"
            print(f"    -> {fn}: {url}")
        print()


def cmd_auth_map(args):
    rt = _build_rt()
    print("AUTH MAP: which paths go through which auth layers")
    print()

    print("  NO AUTH:")
    for b in rt.behaviors:
        if not b.has_auth:
            print(f"    {b.path_pattern} -> {b.origin_id}")
    print()

    print("  EDGE JWT ONLY (no API GW authorizer):")
    for b in rt.behaviors:
        origin = rt.origins.get(b.origin_id)
        if b.has_auth and origin and origin.origin_type == "s3":
            print(f"    {b.path_pattern} -> {b.origin_id}")
    print()

    print("  EDGE JWT + API GW AUTHORIZER:")
    for b in rt.behaviors:
        origin = rt.origins.get(b.origin_id)
        if b.has_auth and origin and origin.origin_type == "api_gateway":
            print(f"    {b.path_pattern} -> {b.origin_id}")
    print()

    # Warn about custom error responses that affect auth debugging
    auth_codes_intercepted = [c for c in rt.custom_error_responses if c.error_code in (401, 403)]
    if auth_codes_intercepted:
        print()
        print("WARN -- custom_error_response intercepts:")
        for cer in auth_codes_intercepted:
            print(f"  HTTP {cer.error_code} -> {cer.response_code} {cer.response_page_path}")
            print(f"  Lambda auth denials ({cer.error_code}) will reach browser as {cer.response_code} HTML, not JSON.")
            print(f"  To pass auth errors through: return HTTP 401 instead of 403 from Lambda.")


def cmd_stats(args):
    rt = _build_rt()
    print("ROUTING TABLE STATISTICS")
    print(f"  CloudFront origins:   {len(rt.origins)}")
    print(f"  CloudFront behaviors: {len(rt.behaviors)}")
    print(f"  Custom error responses: {len(rt.custom_error_responses)}")
    print(f"  Rewrite rules:        {len(rt.rewrite_rules)}")
    print(f"  API Gateway routes:   {len(rt.api_gw_routes)}")
    print(f"  Frontend endpoints:   {len(rt.endpoints)} ({sum(1 for e in rt.endpoints.values() if e.url_template)} with URLs)")
    print(f"  Component bindings:   {len(rt.components)}")
    print(f"  Resolved routes:      {len(rt.routes)}")
    print()

    # Routes by origin type
    s3_routes = [r for r in rt.routes if r.cf_origin_type == "s3"]
    apigw_routes = [r for r in rt.routes if r.cf_origin_type == "api_gateway"]
    unmatched = [r for r in rt.routes if not r.cf_origin_type]
    print(f"  Routes via S3 direct:     {len(s3_routes)}")
    print(f"  Routes via API Gateway:   {len(apigw_routes)}")
    print(f"  Routes unmatched to CF:   {len(unmatched)}")
    print()

    # Auth coverage
    auth_routes = [r for r in rt.routes if r.auth_edge]
    print(f"  Routes with edge auth:    {len(auth_routes)} / {len(rt.routes)}")
    api_auth_routes = [r for r in rt.routes if r.auth_api_gw]
    print(f"  Routes with API GW auth:  {len(api_auth_routes)} / {len(rt.routes)}")


# ---------------------------------------------------------------------------
# edge-versions: Lambda@Edge version pinning scanner
# ---------------------------------------------------------------------------

def cmd_edge_versions(args):
    bindings = parse_edge_versions(_WORKSPACE)
    if not bindings:
        print("No Lambda@Edge version bindings found.")
        return

    print("LAMBDA@EDGE VERSION BINDINGS")
    print(f"  Source: cloudfront-distribution.tf locals block\n")

    hardcoded = []
    dynamic = []

    for b in bindings:
        if b.is_dynamic:
            dynamic.append(b)
        else:
            hardcoded.append(b)

    if hardcoded:
        print(f"  HARDCODED ({len(hardcoded)})  -- these will NOT update on terraform apply:")
        for b in hardcoded:
            version_str = f":{b.pinned_version}" if b.pinned_version is not None else ":?"
            resource_hint = ""
            if b.tf_resource:
                resource_hint = f"  (resource exists: {b.tf_resource})"
            print(f"    {b.function_name:<30} PINNED {version_str:<6} [STALE RISK]{resource_hint}")
        print()

    if dynamic:
        print(f"  DYNAMIC ({len(dynamic)})  -- these auto-update on terraform apply:")
        for b in dynamic:
            print(f"    {b.function_name:<30} qualified_arn  [OK]")
        print()

    if hardcoded:
        print("  FIX: wire hardcoded ARNs to qualified_arn from the Lambda resource.")
        print("  Example:")
        for b in hardcoded:
            if b.tf_resource:
                # Infer the tf local name format
                res_name = b.tf_resource.split('.')[-1]
                print(f"    {b.local_name} = {b.tf_resource}.qualified_arn")
        print()
        print(f"  WARNING: {len(hardcoded)} edge function(s) will silently serve stale code")
        print(f"  after their next deploy. Same root cause as the ADVI_49PUSH outage")
        print(f"  (shared-advisor-router was pinned to :10, Terraform published :12).")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog='comp-routes',
        description='Trace the full serving path from S3 artifact to frontend component.',
    )
    sub = parser.add_subparsers(dest='command')

    p_trace = sub.add_parser('trace', help='Trace a URL, endpoint function, or component')
    p_trace.add_argument('query', help='URL path, endpoint function name, or component name')
    p_trace.add_argument('--json', action='store_true')

    sub.add_parser('behaviors', help='List all CloudFront behaviors')
    sub.add_parser('origins', help='List all CloudFront origins')
    sub.add_parser('rewrites', help='List all URL->S3 rewrite rules')
    sub.add_parser('api-routes', help='List all API Gateway routes')
    sub.add_parser('endpoints', help='List all frontend endpoints with URLs')
    sub.add_parser('components', help='List component -> endpoint bindings')
    sub.add_parser('auth-map', help='Auth layers per path')
    sub.add_parser('stats', help='Routing table statistics')
    sub.add_parser('edge-versions', help='Lambda@Edge version pinning scanner')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        'trace': cmd_trace,
        'behaviors': cmd_behaviors,
        'origins': cmd_origins,
        'rewrites': cmd_rewrites,
        'api-routes': cmd_api_routes,
        'endpoints': cmd_endpoints,
        'components': cmd_components,
        'auth-map': cmd_auth_map,
        'stats': cmd_stats,
        'edge-versions': cmd_edge_versions,
    }
    commands[args.command](args)


if __name__ == '__main__':
    main()
