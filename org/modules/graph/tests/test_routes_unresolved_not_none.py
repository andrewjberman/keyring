#!/usr/bin/env python3
"""comp-routes / comp-pii honesty guard: a CLIENT-COMPOSED URL reports UNRESOLVED, never a false auth:NONE.

Same honesty class as the comp-pii cleartext-vs-"hashed" fix (2094d30c9), INVERTED: a tool must not
assert a posture it cannot determine. comp-routes could not statically resolve a client-composed URL
(a base built at runtime from a local template literal -> leading "{param}"), so the route fell through
to all-False auth flags + blank origin, which comp-pii then printed as `auth: NONE | NO PSEUDONYMIZER
(S3 direct)`. auth:NONE reads as a PROVEN-OPEN gate; the truth is UNRESOLVED (auth UNDETERMINED). The
gate whose auth is actually SOUND (getPlatinumAdvisorSummary, anon->401 exercised @499cb50ef) was
libeled as no-auth. Worse, a REAL open PII gate would read identically -- so the false NONE is
non-discriminating and cannot be trusted either way.

BIDIRECTIONAL, non-vacuous (COO exit criterion, fixTO 005efdc9e). Every test binds BOTH directions and
each names the MUTANT it reddens:
  (1) a client-composed URL  -> UNRESOLVED (a mutant regressing it to NONE REDDENS), and
  (2) a genuinely statically-resolvable OPEN route -> NONE (the negative control against
      "always say UNRESOLVED" -- a mutant that blanket-relabels REDDENS).
Both mutants must redden, else the fix merely MOVED the dishonesty.

Author: comp-routes honesty-fix worker (reports to 1.0.0_SA_CTO). 2026-07-11.
Hermetic: synthetic in-memory routes/flows for the consumer surfaces; the classifier tests parse the
repo's own portal route config (no bd/data/held path, no network, no vendor API).
"""

from __future__ import annotations

import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

_WORKSPACE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph import pii_cli, routes_cli  # noqa: E402
from org.modules.graph.extract_routes import (  # noqa: E402
    Route,
    RoutingTable,
    _url_is_statically_resolvable,
    build_routing_table,
)
from org.modules.graph.extract_transforms import (  # noqa: E402
    ComponentDataFlow,
    FetchBinding,
    TypeField,
)


# ---------------------------------------------------------------------------
# Synthetic fixtures: one client-composed (unresolvable) + one genuinely-open resolvable route.
# ---------------------------------------------------------------------------

def _composed_route() -> Route:
    """A CLIENT-COMPOSED route: base built at runtime -> leading '{param}', auth UNDETERMINED."""
    return Route(
        url_pattern="{param}/book.json{param}",
        endpoint_function="getPlatinumAdvisorSummary",
        url_resolvable=False,
        resolve_reason="client-composed URL (runtime-templated base, no static literal)",
        # auth flags all False -- but they are UNDETERMINED, NOT proven-absent:
        auth_edge=False,
        auth_api_gw=False,
    )


def _open_resolvable_route() -> Route:
    """A GENUINELY statically-resolvable OPEN route (absolute URL, matched a no-auth behavior).
    This is the negative control: it must STILL report NONE, never UNRESOLVED."""
    return Route(
        url_pattern="/api/general/public/thing.json",
        endpoint_function="getPublicThing",
        url_resolvable=True,
        cf_behavior="/*",
        cf_origin="S3-opalinvest-portal",
        cf_origin_type="s3",
        auth_edge=False,
        auth_api_gw=False,
    )


# ---------------------------------------------------------------------------
# LAYER 1 -- the classifier (extract_routes._url_is_statically_resolvable + build_routing_table gate).
# Mutant target: `_url_is_statically_resolvable` (return True / return False) and the build gate.
# ---------------------------------------------------------------------------

def test_classifier_discriminates_composed_from_resolvable():
    """The discriminator itself. A leading '{param}' (client-composed base) is UNRESOLVABLE; a mid-path
    '{param}' in an absolute URL is RESOLVABLE. MUTANT `return True`  -> line 1 REDDENS (composed passes);
    MUTANT `return False` -> line 2 REDDENS (resolvable fails). Neither blanket answer survives."""
    assert _url_is_statically_resolvable("{param}/book.json{param}") is False
    assert _url_is_statically_resolvable(
        "/api/scoped/advisor-intelligence/platinum/advisors/{param}/book.json"
    ) is True


def test_real_build_client_composed_is_unresolvable_not_open():
    """DIRECTION 1 on the REAL repo route config: getPlatinumAdvisorSummary resolves to a client-composed
    '{param}/...' URL -> url_resolvable False. MUTANT (drop the build_routing_table resolvability gate, or
    `_url_is_statically_resolvable`->True) leaves it url_resolvable True == a false proven-open -> REDDENS."""
    rt = build_routing_table(_WORKSPACE)
    r = next((x for x in rt.routes if x.endpoint_function == "getPlatinumAdvisorSummary"), None)
    assert r is not None, "getPlatinumAdvisorSummary route missing -- parser/path drift"
    assert r.url_resolvable is False, (
        f"client-composed URL {r.url_pattern!r} must be UNRESOLVED, got url_resolvable={r.url_resolvable}"
    )
    assert r.resolve_reason, "an unresolvable route must carry its reason (never a silent flag)"


def test_real_build_does_not_blanket_relabel_everything_unresolved():
    """NEGATIVE CONTROL on the REAL config: statically-resolvable absolute URLs stay RESOLVABLE. If the
    fix just learned 'always UNRESOLVED', these flip. MUTANT `_url_is_statically_resolvable`->False makes
    EVERY route unresolvable -> REDDENS. Proves the fix discriminates, it did not move the dishonesty."""
    rt = build_routing_table(_WORKSPACE)
    resolvable = [x for x in rt.routes if x.url_resolvable]
    unresolvable = [x for x in rt.routes if not x.url_resolvable]
    assert resolvable, "no route resolved -- the fix blanket-relabelled everything UNRESOLVED"
    # The known resolvable firm dashboard (absolute '/api/scoped/...json') must keep its real posture.
    dash = next((x for x in rt.routes if x.endpoint_function == "getPlatinumFirmDashboard"), None)
    assert dash is not None and dash.url_resolvable is True
    # And the known client-composed ones ARE the unresolvable set (discrimination is real, not empty).
    composed = {x.endpoint_function for x in unresolvable}
    assert "getPlatinumAdvisorSummary" in composed


# ---------------------------------------------------------------------------
# LAYER 2 -- comp-routes consumer (routes_cli._print_route + trace --json auth_status).
# Mutant target: the `if not route.url_resolvable:` branch in _print_route / the JSON auth_status expr.
# ---------------------------------------------------------------------------

def _capture(fn, *a, **k) -> str:
    buf = io.StringIO()
    with redirect_stdout(buf):
        fn(*a, **k)
    return buf.getvalue()


def test_comp_routes_print_composed_says_unresolved_not_no_auth():
    """DIRECTION 1 (comp-routes human). A client-composed route prints UNRESOLVED and NOT 'edge JWT: no'.
    MUTANT (delete the `if not route.url_resolvable` branch) prints 'edge JWT: no / API GW:   no' -- a
    false proven-open -> the 'UNRESOLVED in out' assert AND the 'edge JWT: no' NOT-in assert both REDDEN."""
    out = _capture(routes_cli._print_route, _composed_route())
    assert "UNRESOLVED" in out
    assert "edge JWT: no" not in out and "API GW:   no" not in out, (
        "a client-composed route must NOT emit a determinate no-auth verdict"
    )


def test_comp_routes_print_open_says_no_auth_not_unresolved():
    """NEGATIVE CONTROL (comp-routes human). A genuinely-resolvable OPEN route STILL prints the concrete
    'edge JWT: no / API GW:   no' and NOT 'UNRESOLVED'. MUTANT (blanket-print UNRESOLVED) -> REDDENS."""
    out = _capture(routes_cli._print_route, _open_resolvable_route())
    assert "edge JWT: no" in out and "API GW:   no" in out
    assert "UNRESOLVED" not in out, "a genuinely-resolvable open route must NOT be relabelled UNRESOLVED"


def test_comp_routes_json_auth_status_discriminates():
    """comp-routes trace --json: auth_status == 'UNRESOLVED' for composed, a concrete verdict for open.
    Exercises cmd_trace's JSON emitter with a synthetic rt. MUTANT (drop the url_resolvable arm of the
    auth_status ternary) -> composed emits 'none' -> the composed assert REDDENS; a blanket 'UNRESOLVED'
    -> the open assert REDDENS."""
    composed, open_route = _composed_route(), _open_resolvable_route()
    rt = RoutingTable()
    rt.routes = [composed, open_route]
    # cmd_trace takes the --json exact-match path only when the query is a known endpoint key;
    # the values are unused by the JSON emitter (it filters rt.routes by endpoint_function).
    rt.endpoints = {"getPlatinumAdvisorSummary": None, "getPublicThing": None}

    class _Args:
        json = True

    for fn_name, expected in (("getPlatinumAdvisorSummary", "UNRESOLVED"), ("getPublicThing", "none")):
        # cmd_trace fuzzy-matches endpoint names; feed the exact function name as the query.
        args = _Args()
        args.query = fn_name
        # Route the CLI through our synthetic table.
        orig = routes_cli._build_rt
        routes_cli._build_rt = lambda rt=rt: rt
        try:
            out = _capture(routes_cli.cmd_trace, args)
        finally:
            routes_cli._build_rt = orig
        import json as _json

        payload = _json.loads(out)
        assert payload, f"no JSON emitted for {fn_name}"
        assert payload[0]["auth_status"] == expected, (
            f"{fn_name}: auth_status={payload[0]['auth_status']!r}, expected {expected!r}"
        )
        assert payload[0]["url_resolvable"] is (expected != "UNRESOLVED")


# ---------------------------------------------------------------------------
# LAYER 3 -- comp-pii consumer (pii_cli.cmd_routes): the surface that PRINTED the false `auth: NONE`.
# Mutant target: the `if not route.url_resolvable:` UNRESOLVED branch in cmd_routes.
# ---------------------------------------------------------------------------

def _flow(component_name: str, fetch_fn: str, type_name: str) -> ComponentDataFlow:
    """A minimal component flow that fetches `fetch_fn` and whose response type carries a PII field
    (client_name) -- so cmd_routes prints a PII-route line for it."""
    return ComponentDataFlow(
        component_name=component_name,
        file_path=f"portal/src/pages/{component_name}.tsx",
        fetches=[FetchBinding(fetch_function=fetch_fn, data_variable="d", response_type=type_name)],
        response_types={type_name: [TypeField(name="client_name", type_str="string")]},
    )


def _run_pii_routes(routes, flows) -> str:
    rt = RoutingTable()
    rt.routes = routes
    orig_rt, orig_flows = pii_cli.build_routing_table, pii_cli.build_all_dataflows
    pii_cli.build_routing_table = lambda *_a, **_k: rt
    pii_cli.build_all_dataflows = lambda *_a, **_k: flows
    try:
        return _capture(pii_cli.cmd_routes, None)
    finally:
        pii_cli.build_routing_table = orig_rt
        pii_cli.build_all_dataflows = orig_flows


def test_comp_pii_routes_composed_surfaces_unresolved_not_none():
    """DIRECTION 1 (comp-pii, the reported surface). The client-composed route surfaces `auth: UNRESOLVED`
    and NEVER `auth: NONE`. This is the exact string the finding named ('auth: NONE | NO PSEUDONYMIZER
    (S3 direct)'). MUTANT (delete the cmd_routes `if not route.url_resolvable` branch) prints `auth: NONE`
    -> the 'auth: NONE' NOT-in assert AND the 'UNRESOLVED' in assert both REDDEN."""
    out = _run_pii_routes(
        [_composed_route()],
        [_flow("SynthComposed", "getPlatinumAdvisorSummary", "PlatinumAdvisorSummary")],
    )
    assert "getPlatinumAdvisorSummary" in out
    assert "auth: UNRESOLVED" in out
    assert "auth: NONE" not in out, "comp-pii must NOT print a false auth: NONE for a client-composed URL"
    # The false 'S3 direct / NO PSEUDONYMIZER' determinate posture must also be gone for the composed route.
    assert "UNRESOLVED: client-composed" in out


def test_comp_pii_routes_open_still_says_none():
    """NEGATIVE CONTROL (comp-pii). A genuinely-resolvable OPEN route STILL prints `auth: NONE` -- the
    honest verdict for a real open route. MUTANT (blanket UNRESOLVED) makes the open route print
    UNRESOLVED -> the 'auth: NONE' assert REDDENS. Proves comp-pii didn't just learn 'always UNRESOLVED'."""
    out = _run_pii_routes(
        [_open_resolvable_route()],
        [_flow("SynthOpen", "getPublicThing", "PublicThing")],
    )
    assert "getPublicThing" in out
    assert "auth: NONE" in out, "a genuinely-open resolvable route must keep the honest auth: NONE verdict"
    assert "auth: UNRESOLVED" not in out
