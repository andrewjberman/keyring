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
import re
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_routes import build_routing_table, parse_edge_versions, EndpointFunction  # noqa: E402

try:  # header-only dependency: a missing helper must not break the tool, only its header
    from org.modules.graph import comp_output_contract as _oc  # noqa: E402
except Exception:  # pragma: no cover - defensive
    _oc = None


def _build_rt():
    return build_routing_table(_WORKSPACE)


# ---------------------------------------------------------------------------
# OUTPUT-CONTRACT header (R1R3) -- coverage + plane/vintage, to stderr so stdout stays parseable
# ---------------------------------------------------------------------------

def _emit_contract(sub: str) -> None:
    if _oc is None:
        print("COVERAGE: UNKNOWN (output-contract helper unavailable); coverage NOT asserted",
              file=sys.stderr)
        print("PLANE: desired | VINTAGE: parsed Terraform + Lambda@Edge routers at working-tree HEAD",
              file=sys.stderr)
        return
    print(_oc.coverage_line("comp-routes", sub), file=sys.stderr)
    print(_oc.plane_header("comp-routes", sub), file=sys.stderr)


# ---------------------------------------------------------------------------
# Git-Bash/MSYS argument repair
# ---------------------------------------------------------------------------

_MSYS_MANGLED_RE = re.compile(r'^[A-Za-z]:[\\/](?:.*[\\/])?Git[\\/](.*)$')


def _normalize_query_path(query: str) -> str:
    """Undo the MSYS mangling of a leading-slash URL argument.

    Git Bash rewrites a bare `/api/general/...` argument into `C:/Program Files/Git/api/general/...`
    before the process ever sees it. The mangled string no longer starts with "/", so cmd_trace's URL
    branch is skipped entirely and the query falls through to the function-name branch, ending at
    "No match for: C:/Program Files/Git/api/..." -- an ABSENT verdict manufactured by a broken
    retrieval, not by the routing table. Same class as the `git show <ref>:<path>` mangle.

    MSYS_NO_PATHCONV=1 does NOT fix this at the call site: it leaks into the comp-routes launcher and
    mangles the SCRIPT path instead. So the repair belongs here, and it is announced (stderr) rather
    than silent -- a tool that quietly rewrites its own input teaches the caller nothing.
    """
    m = _MSYS_MANGLED_RE.match(query)
    if not m:
        return query
    repaired = "/" + m.group(1).replace("\\", "/")
    print(f"NOTE: argument was MSYS-mangled by Git Bash; read as {repaired!r} (was {query!r}).",
          file=sys.stderr)
    print("      Git Bash rewrites a leading-slash argument into a Windows path. Quote it or pass an "
          "endpoint function name to avoid this.", file=sys.stderr)
    return repaired


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_trace(args):
    rt = _build_rt()
    query = _normalize_query_path(args.query)

    # Determine what was queried: URL, endpoint function, or component
    matched_routes = []

    if query.startswith('/'):
        # URL query -- find routes whose url_pattern matches
        matched_routes = [r for r in rt.routes if query in r.url_pattern or r.url_pattern in query]
        if not matched_routes:
            # Try CloudFront behavior match
            behavior = rt.match_behavior(query)
            if args.json:
                # A --json flag that falls through to prose is its own honesty defect: the consumer's
                # parser breaks, or it does not break and they string-match their way to a wrong class.
                print(json.dumps(_url_trace_payload(rt, query, behavior), indent=2))
                return
            if behavior:
                origin = rt.origins.get(behavior.origin_id)
                bucket = origin.bucket_name if origin else ""
                origin_line = behavior.origin_id + (f" (bucket {bucket})" if bucket else "")
                print(f"URL matches CloudFront behavior: {behavior.path_pattern}")
                print(f"  Origin: {origin_line}")
                print(f"  Auth: {'yes' if behavior.has_auth else 'no'}")
                print(f"  Router: {'yes' if behavior.has_router else 'no'}")
                for ef in behavior.edge_functions:
                    print(f"  Edge: {ef.event_type} -> {ef.function_name}")
                _print_rewrite_resolution(rt, query, bucket)
                _print_fallthrough_disclosure(behavior)
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
                print("Try a URL (/api/...), endpoint function name, or component name.")
                return

    if args.json:
        print(json.dumps([{
            "url": r.url_pattern,
            "cf_behavior": r.cf_behavior,
            "cf_origin": r.cf_origin,
            "cf_origin_type": r.cf_origin_type,
            # UNRESOLVED when the URL is client-composed (auth is UNDETERMINED, not
            # proven-absent). auth_edge/auth_api_gw are only meaningful when
            # url_resolvable is True -- a consumer must read url_resolvable, never
            # treat false/false as a proven auth:NONE.
            "url_resolvable": r.url_resolvable,
            "resolve_reason": r.resolve_reason,
            "auth_status": "UNRESOLVED" if not r.url_resolvable else (
                "edge+apigw" if (r.auth_edge and r.auth_api_gw) else
                "edge" if r.auth_edge else
                "apigw" if r.auth_api_gw else "none"
            ),
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


# ---------------------------------------------------------------------------
# Machine-readable URL trace (`trace --json <url>`)
# ---------------------------------------------------------------------------

# The outcome CLASS is a first-class field, never something a consumer recovers by string-matching
# "UNRESOLVED" or "!!" out of prose. A textual distinction gets inferred wrong eventually, and that
# failure is silent; an enum makes it structural.
OUTCOME_RESOLVED = "RESOLVED"                      # a rewrite rule matched -> a real S3 key
OUTCOME_UNRESOLVED_NO_RULE = "UNRESOLVED_NO_RULE"  # behavior matched, no rule covers the prefix
OUTCOME_CATCHALL_DEFAULT = "CATCHALL_DEFAULT"      # fell through to the default slot: NOT a resolution
OUTCOME_NO_MATCH = "NO_MATCH"                      # no behavior matched at all, not even the default
OUTCOME_REFUSED = "REFUSED"                        # the router BLOCKS this path (e.g. 401); NO S3 key exists


def _contract_field(field, default):
    """Pull a declared field from comp-routes' output contract, so the JSON payload carries the SAME
    coverage statement the human header does. Read at run time rather than hardcoded: a corrected
    blind spot reaches every consumer without a second edit here."""
    if _oc is None:
        return default
    try:
        c = _oc.contract_for("comp-routes", "trace")
        if isinstance(c, dict) and c.get(field) is not None:
            return c[field]
    except Exception:  # pragma: no cover - a header must never break the answer
        pass
    return default


def _url_trace_payload(rt, url, behavior):
    """The machine-readable answer for a URL trace. `behavior` is None when nothing matched.

    PRECEDENCE, stated here because it is a real decision and not an implementation detail:
    CATCHALL_DEFAULT outranks RESOLVED. If no specific behavior claimed the path, we do not know it is
    served at all, so that caveat beats a key we could nominally compute -- which means s3_key MAY be
    non-null while outcome is CATCHALL_DEFAULT. Consumers key on `outcome` and treat anything that is
    not RESOLVED as not-a-resolution. `catchall` is emitted separately so the two axes never have to be
    recovered from one field.
    """
    payload = {
        "query": url,
        "outcome": OUTCOME_NO_MATCH,
        "catchall": False,
        "behavior": None,
        "origin": None,
        "auth": None,
        "router": None,
        "edge_functions": [],
        "rewrite_rule": None,
        "s3_bucket": None,
        "s3_key": None,
        "s3_uri": None,
        "plane": _contract_field("plane", "desired"),
        "vintage": _contract_field("vintage", "UNKNOWN"),
        "blind_spots": _contract_field("blind_spots", []),
    }
    if behavior is None:
        payload["disclosure"] = (
            "No CloudFront behavior matched this path -- not even the default. Nothing was resolved "
            "and nothing is asserted about whether the path is served."
        )
        return payload

    origin = rt.origins.get(behavior.origin_id)
    behavior_bucket = origin.bucket_name if origin else ""
    rule = rt.match_rewrite_rule(url)
    is_refuse = rule is not None and getattr(rule, "kind", "") == "refuse"
    firm_parametric = rule is not None and getattr(rule, "firm_parametric", False)
    key = rt.resolve_s3_key(url) if rule is not None else ""

    # THE BUCKET IS NOT ALWAYS THE CF ORIGIN'S BUCKET. For a firm-parametric rule the router rebuilds
    # the origin domain per requesting firm (FIRM_BUCKET_MAP), so no single bucket is correct -- the CF
    # origin's bucket is merely one firm's. Emitting it as s3://<that-firm>/... names another firm's
    # bucket with RESOLVED confidence, the exact cross-firm-pointer the firm-sep gates exist to catch
    # downstream. So the bucket REFUSES here (key is fine; the KEY is firm-independent).
    bucket = "" if firm_parametric else behavior_bucket

    payload.update({
        "catchall": behavior.order == 0,
        "behavior": behavior.path_pattern,
        "origin": behavior.origin_id,
        "auth": behavior.has_auth,
        "router": behavior.has_router,
        "edge_functions": [{"event_type": ef.event_type, "function_name": ef.function_name}
                           for ef in behavior.edge_functions],
        "rewrite_rule": (f"{rule.url_prefix} -> {rule.s3_prefix}"
                         if (rule and not is_refuse) else None),
        "s3_bucket": bucket or None,
        "s3_bucket_firm_parametric": firm_parametric,
        "s3_key": (None if is_refuse else (key or None)),
        "s3_uri": f"s3://{bucket}/{key}" if (bucket and key and not is_refuse) else None,
    })

    if behavior.order == 0:
        payload["outcome"] = OUTCOME_CATCHALL_DEFAULT
        payload["disclosure"] = (
            "Matched the catch-all default behavior -- NO specific CloudFront behavior claimed this "
            "path. This is a DEFAULT, not a resolution: the same answer is returned for ANY unmodelled "
            "path, so it is not evidence that the path exists, is served, or lives at this origin."
        )
    elif is_refuse:
        # The router BLOCKS this path -- there is no S3 key. This is the state a prefix-only table could
        # not express, so it used to render as RESOLVED with a concrete key (a PII path the router 401s).
        payload["outcome"] = OUTCOME_REFUSED
        payload["refuse_status"] = getattr(rule, "refuse_status", "") or None
        payload["disclosure"] = (
            f"The router REFUSES this path (HTTP {getattr(rule, 'refuse_status', '?')}): "
            f"{getattr(rule, 'refuse_reason', '') or 'blocked at the edge'}. There is NO S3 key -- it is "
            f"not served S3-direct. Reading a resolution here would be false-secure (the router branch "
            f"exists specifically to stop S3-direct access to this path)."
        )
    elif rule is not None:
        payload["outcome"] = OUTCOME_RESOLVED
        fp_note = (" The BUCKET is firm-parametric (chosen per requesting firm from FIRM_BUCKET_MAP), so "
                   "no single s3:// URI is correct -- the key is firm-independent, the bucket is refused."
                   if firm_parametric else "")
        payload["disclosure"] = (
            "Resolved through the modelled static rewrite table (DESIRED plane -- parsed Terraform + "
            "committed router source, never a live CloudFront read)." + fp_note
        )
    else:
        payload["outcome"] = OUTCOME_UNRESOLVED_NO_RULE
        payload["disclosure"] = (
            "A CloudFront behavior matched, but no rewrite rule covers this prefix, so no S3 key was "
            "derived. This is missing COVERAGE, NOT a proof that no key exists."
        )
    return payload


def _print_rewrite_resolution(rt, url, bucket):
    """LIMB A -- consult the rewrite table this tool ALREADY carries, and name the rule that fired.

    Before this, the behavior branch stopped at the CloudFront layer: it reported the behavior,
    origin, auth and edge functions, and never emitted an S3 key at all. Two URLs under the SAME
    behavior returned byte-identical output even when DIFFERENT rewrite rules applied to them --
    so the tool could not answer the question it was being asked, while looking authoritative on
    the part it did answer.

    The table is not re-derived here: rt.match_rewrite_rule / rt.resolve_s3_key share one matcher,
    parsed from the Lambda@Edge routers. Naming the matched rule is what makes the answer
    discriminating -- the key alone would not show WHY two paths resolve differently.
    """
    rule = rt.match_rewrite_rule(url)
    if rule is None:
        print("  Rewrite: NONE -- no rewrite rule matches this path prefix")
        print("  S3 key:  UNRESOLVED -- the modelled rewrite table does not cover this prefix.")
        print("           This is missing COVERAGE, not a proof that no key exists, and it is the")
        print("           SAME answer given for every uncovered path -- do not read it as a resolution.")
        return
    if getattr(rule, "kind", "") == "refuse":
        # The router BLOCKS this path -- no S3 key. A prefix-only table could not express this, so it
        # used to render as a RESOLVED key (a PII path the router 401s, read as served S3-direct).
        print(f"  REFUSED: the router returns HTTP {rule.refuse_status} for this path"
              + (f" -- {rule.refuse_reason}" if rule.refuse_reason else ""))
        print("  S3 key:  NONE -- this path is NOT served S3-direct; the router blocks it at the edge.")
        print("           Reading a resolution here would be FALSE-SECURE: the block is the whole point.")
        return
    cond = f"  ({rule.condition})" if rule.condition else ""
    key = rt.resolve_s3_key(url)
    print(f"  Rewrite: {rule.url_prefix} -> {rule.s3_prefix}{cond}")
    print(f"  S3 key:  {key}")
    if getattr(rule, "firm_parametric", False):
        # The origin BUCKET is chosen per requesting firm (FIRM_BUCKET_MAP). No single bucket is
        # correct; naming one hands out another firm's bucket with false confidence.
        print("  S3 URI:  REFUSED -- this origin is FIRM-PARAMETRIC: the router picks the bucket per")
        print("           requesting firm (opal-data-{firm}), so no single s3:// URI is correct. The key")
        print("           above is firm-independent; ask for the firm map, not a resolved bucket.")
    elif bucket:
        print(f"  S3 URI:  s3://{bucket}/{key}")
    else:
        print("  S3 URI:  UNRESOLVED -- this origin carries no bucket name; the key above is")
        print("           bucket-relative and is NOT a complete location on its own.")


def _print_fallthrough_disclosure(behavior):
    """LIMB B -- always-on, no suppress flag.

    The catch-all default behavior matches ANY path no other behavior claimed, so it renders the
    same origin for a real unmatched route and for a path that does not exist. Printed through the
    identical code path as a specific match, that reads as a resolution. Keyed on behavior.order == 0
    (the structural default slot), never on the literal "/*" string.
    """
    if behavior.order != 0:
        return
    print()
    print(f"  !! MATCHED: catch-all {behavior.path_pattern} -- NO specific CloudFront behavior matched")
    print("     this path. THIS IS A DEFAULT, NOT A RESOLUTION.")
    print("     CloudFront serves this same origin for ANY unmodelled path, so this answer does not")
    print("     discriminate: it is NOT evidence that the path exists, that it is served, or that")
    print("     this origin holds it. Verify the served edge directly before relying on it.")


def _print_route(route, indent=0):
    pad = " " * indent
    print(f"{pad}ROUTE: {route.endpoint_function}")
    print(f"{pad}  URL: {route.url_pattern}")
    if not route.url_resolvable:
        # The URL is client-composed / statically-unresolvable: we CANNOT map it to a
        # CloudFront behavior, so the auth posture is UNDETERMINED. Report UNRESOLVED,
        # never a false auth:NONE (which reads as a proven-open gate).
        print(f"{pad}  CloudFront: UNRESOLVED ({route.resolve_reason})")
        print(f"{pad}  Auth: UNRESOLVED -- cannot statically map this URL to a CF behavior;")
        print(f"{pad}        auth is UNDETERMINED here, NOT proven absent. Verify the served edge directly.")
        if route.components:
            print(f"{pad}  Components: {', '.join(route.components)}")
        print()
        return
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
            print("  To pass auth errors through: return HTTP 401 instead of 403 from Lambda.")


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
    print("  Source: cloudfront-distribution.tf locals block\n")

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
                print(f"    {b.local_name} = {b.tf_resource}.qualified_arn")
        print()
        print(f"  WARNING: {len(hardcoded)} edge function(s) will silently serve stale code")
        print("  after their next deploy. Same root cause as the ADVI_49PUSH outage")
        print("  (shared-advisor-router was pinned to :10, Terraform published :12).")


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
    # R1R3: every answer carries its coverage denominator + plane/vintage (stderr keeps stdout parseable).
    _emit_contract(args.command)
    commands[args.command](args)


if __name__ == '__main__':
    main()
