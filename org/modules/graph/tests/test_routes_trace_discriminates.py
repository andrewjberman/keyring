#!/usr/bin/env python3
"""comp-routes trace: RESOLVE through the rewrite table, and DISCLOSE a catch-all fall-through.

NFRA_TOOLARCH.ROUTES. The defect, reproduced first-hand before any code was touched: `trace` matched
the CloudFront behavior correctly and then stopped -- it never consulted the rewrite table it already
carried, so it never emitted an S3 key for a behavior-matched URL. Three paths under the SAME behavior
returned BYTE-IDENTICAL output even when DIFFERENT rewrite rules applied:

    /api/general/json/mdpf/global/aggregate-aua-timeseries.json   (rule /api/general/json/ -> json/)
    /api/general/json/zzzz/total/garbage/nonexistent.json          (same rule, junk suffix)
    /api/general/NOT-json-prefix/whatever.txt                      (rule /api/general/ -> json/)

That is the false-authority class, not the obvious kind: the CF/auth/edge half of the answer IS
correct, so the missing S3 resolution reads as considered-and-absent rather than never-attempted. An
instrument that returns the same answer for inputs with different truths is not an instrument.

BIDIRECTIONAL, non-vacuous -- the house rule from test_routes_unresolved_not_none.py. Every limb binds
BOTH directions and names the MUTANT it reddens:
  (1) a covered path -> a NAMED rule + a resolved key (a mutant dropping the resolution REDDENS), and
  (2) an uncovered path -> UNRESOLVED, and a SPECIFIC behavior -> no default-disclosure (the negative
      controls against "always resolve" / "always disclose" -- a blanket mutant REDDENS).
Both directions must redden, else the fix merely MOVED the dishonesty instead of closing it.

Author: 0.8.0_AE_CloudComp~A (NFRA_TOOLARCH.ROUTES, issued 1.0.0_SA_CTO~Z). 2026-07-23.
Hermetic: synthetic in-memory routing tables for the CLI surfaces; the parser tests read the repo's
own committed route config. No network, no AWS, no client data.
"""

from __future__ import annotations

import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

_WORKSPACE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph import routes_cli  # noqa: E402
from org.modules.graph.extract_routes import (  # noqa: E402
    CloudFrontBehavior,
    CloudFrontOrigin,
    EdgeFunction,
    RewriteRule,
    RoutingTable,
    _s3_bucket_from_domain,
    build_routing_table,
)

# The MDPF hop: the concrete URL->key resolution this TO exists to make answerable.
MDPF_URL = "/api/general/json/mdpf/global/aggregate-aua-timeseries.json"
MDPF_KEY = "json/mdpf/global/aggregate-aua-timeseries.json"
MDPF_BUCKET = "opal-data-portal-v2"


# ---------------------------------------------------------------------------
# Synthetic fixture: one specific behavior (with rewrites) + the catch-all default.
# ---------------------------------------------------------------------------

def _rt() -> RoutingTable:
    rt = RoutingTable()
    rt.origins = {
        "S3-data-json": CloudFrontOrigin(
            origin_id="S3-data-json",
            domain_name=f"{MDPF_BUCKET}.s3.us-east-1.amazonaws.com",
            origin_type="api_gateway",   # deliberately the OAC misclassification -- see residual test
            bucket_name=MDPF_BUCKET,
        ),
        "S3-spa": CloudFrontOrigin(
            origin_id="S3-spa",
            domain_name="opalinvest-portal.s3.us-east-1.amazonaws.com",
            origin_type="s3",
            bucket_name="opalinvest-portal",
        ),
    }
    rt.behaviors = [
        # order 0 IS the structural default slot -- the catch-all.
        CloudFrontBehavior(path_pattern="/*", origin_id="S3-spa", order=0, comment="default (SPA)"),
        CloudFrontBehavior(
            path_pattern="/api/general/*", origin_id="S3-data-json", order=18,
            has_auth=True, has_router=True,
            edge_functions=[EdgeFunction(event_type="origin-request", function_name="public-data-router")],
        ),
    ]
    # Most-specific-first, exactly as the Lambda@Edge router's if/else chain evaluates.
    rt.rewrite_rules = [
        RewriteRule(url_prefix="/api/general/json/", s3_prefix="json/", condition="general json passthrough"),
        RewriteRule(url_prefix="/api/general/", s3_prefix="json/", condition="general default fallback"),
    ]
    return rt


def _trace(url: str, rt: RoutingTable | None = None) -> str:
    """Capture `comp-routes trace <url>` stdout against a synthetic table."""
    class _Args:
        json = False

    args = _Args()
    args.query = url
    orig = routes_cli._build_rt
    routes_cli._build_rt = lambda rt=(rt or _rt()): rt
    try:
        buf = io.StringIO()
        with redirect_stdout(buf):
            routes_cli.cmd_trace(args)
        return buf.getvalue()
    finally:
        routes_cli._build_rt = orig


# ---------------------------------------------------------------------------
# LAYER 1 -- the matcher (RoutingTable.match_rewrite_rule / resolve_s3_key).
# Mutant target: the prefix loop -- `return self.rewrite_rules[0]` or `return None`.
# ---------------------------------------------------------------------------

def test_rewrite_matcher_picks_the_MOST_SPECIFIC_rule_not_merely_a_rule():
    """The discriminator itself, at the source. Two URLs under one behavior select DIFFERENT rules.
    MUTANT (return the first rule unconditionally) collapses both onto /api/general/json/ -> the
    second assert REDDENS. MUTANT (return None) -> the first assert REDDENS. Neither blanket survives."""
    rt = _rt()
    assert rt.match_rewrite_rule(MDPF_URL).url_prefix == "/api/general/json/"
    assert rt.match_rewrite_rule("/api/general/NOT-json/x.txt").url_prefix == "/api/general/"


def test_rewrite_matcher_returns_none_for_an_uncovered_prefix():
    """NEGATIVE CONTROL at the source: an uncovered prefix must NOT be forced onto some rule.
    MUTANT (fall back to the last rule when nothing matches) -> REDDENS. Missing coverage must stay
    missing, never be dressed up as a resolution."""
    assert _rt().match_rewrite_rule("/zzz/nothing/here.json") is None
    assert _rt().resolve_s3_key("/zzz/nothing/here.json") == ""


def test_resolve_s3_key_delegates_to_the_one_matcher():
    """Single-derivation guard. resolve_s3_key must agree with match_rewrite_rule by construction --
    the whole point of routing both through one matcher is that the rule NAMED in the output and the
    key EMITTED can never disagree. MUTANT (re-implement the prefix loop separately in resolve_s3_key,
    e.g. iterating in a different order) -> REDDENS here."""
    rt = _rt()
    for url in (MDPF_URL, "/api/general/NOT-json/x.txt"):
        rule = rt.match_rewrite_rule(url)
        assert rt.resolve_s3_key(url) == rule.s3_prefix + url[len(rule.url_prefix):]


# ---------------------------------------------------------------------------
# LAYER 2 -- LIMB A: trace emits a NAMED rule + a resolved key.
# Mutant target: the _print_rewrite_resolution call in cmd_trace's behavior branch.
# ---------------------------------------------------------------------------

def test_trace_resolves_the_mdpf_url_to_its_real_s3_key():
    """DIRECTION 1, and the concrete acceptance: the MDPF URL resolves to its real key, names the rule
    that fired, and renders a complete bucket-qualified location. MUTANT (delete the
    _print_rewrite_resolution call) drops all three lines -> REDDENS. This key was confirmed to exist
    live under s3://opal-data-portal-v2/ at 2026-07-23T21:18:53Z (comp-keys)."""
    out = _trace(MDPF_URL)
    assert f"S3 key:  {MDPF_KEY}" in out
    assert "Rewrite: /api/general/json/ -> json/" in out, "the rule that fired must be NAMED, not just applied"
    assert f"s3://{MDPF_BUCKET}/{MDPF_KEY}" in out, "a key without its bucket is under-specified"


def test_trace_does_not_blanket_emit_a_key_for_an_uncovered_path():
    """NEGATIVE CONTROL for limb A: an uncovered path must say UNRESOLVED, never invent a key.
    MUTANT (resolve by stripping the leading slash whenever no rule matches -- the tempting guess)
    emits a key -> the 'UNRESOLVED' assert REDDENS. Proves the fix did not learn 'always resolve'."""
    out = _trace("/zzz/no/behavior/at/all.json")
    assert "S3 key:  UNRESOLVED" in out
    assert "Rewrite: NONE" in out
    assert "not a proof that no key exists" in out, "missing coverage must be labelled as coverage, not as absence"


def test_two_paths_under_the_SAME_behavior_are_not_byte_identical():
    """THE DISCRIMINATION MUTANT -- this is the acceptance criterion, as a test.

    All three paths match the same behavior (/api/general/*) and previously produced byte-identical
    output. T1 and T3 select DIFFERENT rewrite rules; T2 selects T1's rule with a different suffix.
    All three must now differ. MUTANT (any regression that stops consulting the rewrite table)
    collapses them back to identical -> every assert here REDDENS at once."""
    t1 = _trace(MDPF_URL)
    t2 = _trace("/api/general/json/zzzz/total/garbage/nonexistent.json")
    t3 = _trace("/api/general/NOT-json-prefix/whatever.txt")
    assert t1 != t2, "same rule, different suffix -- must resolve to different keys"
    assert t1 != t3, "DIFFERENT rewrite rules -- byte-identical output is the reported defect"
    assert t2 != t3, "different rules AND different suffixes"
    # And the discrimination must be the CORRECT one, not merely any difference.
    assert "json/NOT-json-prefix/whatever.txt" in t3


# ---------------------------------------------------------------------------
# LAYER 3 -- LIMB B: the catch-all fall-through discloses that it is a DEFAULT.
# Mutant target: the `if behavior.order != 0: return` guard in _print_fallthrough_disclosure.
# ---------------------------------------------------------------------------

def test_catchall_match_is_disclosed_as_a_default_not_a_resolution():
    """DIRECTION 1 for limb B. A path no behavior claimed falls to the catch-all, and the output must
    SAY it is a default. MUTANT (delete the disclosure call, restoring the old silent print) -> every
    assert REDDENS. Always-on: there is no suppress flag to test, by design."""
    out = _trace("/zzz/no/behavior/at/all.json")
    assert "catch-all /*" in out
    assert "THIS IS A DEFAULT, NOT A RESOLUTION" in out
    assert "does not" in out and "discriminate" in out
    assert "NOT evidence that the path exists" in out


def test_a_specific_behavior_match_is_NOT_labelled_a_default():
    """NEGATIVE CONTROL for limb B, and the one that matters most: a genuine specific-behavior match
    must NOT carry the disclosure. MUTANT (drop the `behavior.order != 0` guard so EVERY answer is
    disclosed) -> REDDENS. A disclosure printed on every answer conveys nothing -- an always-on
    warning is indistinguishable from no warning, which is the very failure mode being fixed."""
    out = _trace(MDPF_URL)
    assert "THIS IS A DEFAULT" not in out
    assert "catch-all" not in out


def test_disclosure_keys_on_the_default_SLOT_not_the_literal_pattern_string():
    """The guard is structural (behavior.order == 0), not a string match on the pattern text.

    Unit-level discriminator, stated plainly: the parser hardcodes path_pattern="/*" for the default
    slot (extract_routes.py:329), so the two guards agree on every input the real parser can produce.
    They diverge only here -- an ORDERED behavior that happens to carry a "/*" pattern is a genuine
    match, not a fall-through, and must NOT be disclosed as a default.
    MUTANT (`if behavior.path_pattern != "/*": return`) discloses it -> REDDENS. That mutant would
    also mislabel every future default whose pattern text ever changes."""
    rt = _rt()
    rt.behaviors.append(CloudFrontBehavior(path_pattern="/*", origin_id="S3-data-json", order=99))
    rt.behaviors = [b for b in rt.behaviors if b.order != 0]  # remove the real default
    out = _trace("/anything/at/all", rt=rt)
    assert "URL matches CloudFront behavior: /*" in out, "the ordered behavior should still match"
    assert "THIS IS A DEFAULT" not in out, "an ORDERED behavior is a real match, not a fall-through"


# ---------------------------------------------------------------------------
# LAYER 4 -- the MSYS argument repair. Without it an agent in Git Bash gets a FALSE ABSENT
# and cannot exercise limb A at all. Mutant target: _normalize_query_path.
# ---------------------------------------------------------------------------

def test_msys_mangled_leading_slash_argument_is_repaired():
    """DIRECTION 1. Git Bash rewrites `/api/general/...` to `C:/Program Files/Git/api/general/...`
    before the process sees it; the mangled string does not start with "/", so cmd_trace skipped the
    URL branch and printed "No match for" -- an ABSENT verdict manufactured by broken retrieval, not
    by the routing table. MUTANT (return query unchanged) -> REDDENS."""
    assert routes_cli._normalize_query_path(
        "C:/Program Files/Git/api/general/json/mdpf/global/aggregate-aua-timeseries.json"
    ) == MDPF_URL
    # Backslash form of the same mangle.
    assert routes_cli._normalize_query_path(
        r"C:\Program Files\Git\api\general\json\x.json"
    ) == "/api/general/json/x.json"


def test_repair_does_not_touch_a_legitimate_query():
    """NEGATIVE CONTROL: endpoint function names, component names and already-correct URLs pass through
    untouched. MUTANT (over-broad regex, e.g. stripping any drive-letter prefix or rewriting anything
    containing 'Git') -> REDDENS. A repair that mangles good input is worse than the mangle it fixes."""
    for q in (MDPF_URL, "getEmployeeLeaderboard", "PartnerAnalytics", "/api/scoped/x.json"):
        assert routes_cli._normalize_query_path(q) == q


def test_mangled_argument_reaches_the_same_answer_as_the_clean_one():
    """End-to-end: the repaired mangled form and the clean form produce identical stdout -- i.e. the
    Git Bash caller now gets the real resolution rather than 'No match for: C:/Program Files/Git/...'.
    MUTANT (drop the _normalize_query_path call in cmd_trace) -> REDDENS."""
    mangled = _trace("C:/Program Files/Git/api/general/json/mdpf/global/aggregate-aua-timeseries.json")
    assert mangled == _trace(MDPF_URL)
    assert MDPF_KEY in mangled


# ---------------------------------------------------------------------------
# LAYER 5 -- bucket derivation. A resolved key without its bucket is under-specified.
# Mutant target: _s3_bucket_from_domain / its call site in the origin parser.
# ---------------------------------------------------------------------------

def test_s3_bucket_derived_from_domain_regardless_of_OAI_or_OAC():
    """DIRECTION 1. The bucket is a property of the DOMAIN. It was previously keyed on the presence of
    a legacy `s3_origin_config` block, so every OAC-fronted S3 origin -- including the MDPF one --
    carried an EMPTY bucket. MUTANT (revert to the s3_origin_config test) -> the real-config assert
    below REDDENS."""
    assert _s3_bucket_from_domain("opal-data-portal-v2.s3.us-east-1.amazonaws.com") == "opal-data-portal-v2"
    assert _s3_bucket_from_domain("opal-data-bd.s3.amazonaws.com") == "opal-data-bd"


def test_non_s3_domain_yields_no_bucket():
    """NEGATIVE CONTROL: an API Gateway domain must NOT produce a bucket name. MUTANT (blanket
    `domain.split('.')[0]`) invents 'f61h681z9g' as a bucket -> REDDENS."""
    assert _s3_bucket_from_domain("f61h681z9g.execute-api.us-east-1.amazonaws.com") == ""
    assert _s3_bucket_from_domain("") == ""


# ---------------------------------------------------------------------------
# LAYER 5b -- R1: the FALSE-SECURE auth-map reading (NFRA_TOOLARCH.MACHINEFLAG, ruled P1).
#
# cmd_auth_map groups by origin_type, and origin_type was derived from the presence of a LEGACY
# `s3_origin_config` block. An OAC-fronted S3 origin declares only origin_access_control_id, so both
# OAC origins were typed api_gateway and /api/general/* + /api/general/json-tiered/* were reported
# under "EDGE JWT + API GW AUTHORIZER" -- an authorizer guarding a path no authorizer guards.
#
# The failure direction is what makes it P1: the wrongness pointed toward SAFETY. An agent asking what
# protects an origin got a reassuring answer, and reassuring answers do not get re-checked.
#
# BOTH DIRECTIONS ARE BOUND, per the ruling. The second is the one nobody would think to write and the
# one that would hide a real exposure: if the fix over-corrects and types everything s3, a genuinely
# authorizer-protected origin silently loses its authorizer in the map.
# ---------------------------------------------------------------------------

def _auth_map(rt: RoutingTable) -> str:
    orig = routes_cli._build_rt
    routes_cli._build_rt = lambda rt=rt: rt
    try:
        buf = io.StringIO()
        with redirect_stdout(buf):
            routes_cli.cmd_auth_map(None)
        return buf.getvalue()
    finally:
        routes_cli._build_rt = orig


def _auth_section(out: str, header: str) -> str:
    """The lines under one auth-map section header (sections are separated by a blank line)."""
    after = out.split(header, 1)[1] if header in out else ""
    return after.split("\n\n", 1)[0]


def test_R1_direction_1_an_OAC_s3_origin_is_never_reported_as_authorizer_protected():
    """DIRECTION 1 -- the reported defect. An OAC-fronted S3 origin behind an edge JWT belongs under
    EDGE JWT ONLY, never under EDGE JWT + API GW AUTHORIZER. MUTANT (revert is_s3 to the
    `s3_origin_config`-only test) puts it back in the authorizer section -> REDDENS."""
    rt = _rt()
    rt.behaviors = [CloudFrontBehavior(path_pattern="/api/general/*", origin_id="S3-data-json",
                                       order=18, has_auth=True, has_router=True)]
    rt.origins["S3-data-json"].origin_type = "s3"   # what the corrected parser now yields
    out = _auth_map(rt)
    assert "/api/general/*" in _auth_section(out, "EDGE JWT ONLY (no API GW authorizer):")
    assert "/api/general/*" not in _auth_section(out, "EDGE JWT + API GW AUTHORIZER:"), (
        "FALSE-SECURE: an OAC S3 origin must never be reported as guarded by an API GW authorizer"
    )


def test_R1_direction_2_a_real_api_gateway_origin_never_loses_its_authorizer():
    """DIRECTION 2 -- THE ONE THAT WOULD HIDE A REAL EXPOSURE. A genuine API Gateway origin behind an
    edge JWT must STILL report the authorizer. MUTANT (over-correct: type every origin s3, e.g.
    `is_s3 = True`) silently moves it into EDGE JWT ONLY -> REDDENS. Without this direction, a fix for
    direction 1 could strip a real authorizer from the map and nothing would notice."""
    rt = _rt()
    rt.origins["APIGW"] = CloudFrontOrigin(
        origin_id="APIGW", domain_name="7k3ed8px20.execute-api.us-east-1.amazonaws.com",
        origin_type="api_gateway",
    )
    rt.behaviors = [CloudFrontBehavior(path_pattern="/api/private/*", origin_id="APIGW",
                                       order=20, has_auth=True)]
    out = _auth_map(rt)
    assert "/api/private/*" in _auth_section(out, "EDGE JWT + API GW AUTHORIZER:")
    assert "/api/private/*" not in _auth_section(out, "EDGE JWT ONLY (no API GW authorizer):"), (
        "an authorizer-protected origin must never be relabelled as edge-JWT-only"
    )


def test_R1_the_classifier_itself_discriminates_both_ways():
    """The discriminator at the source, independent of the renderer. An S3 domain is s3 whether it is
    fronted by OAI or OAC; an execute-api domain is never s3. MUTANT (`is_s3 = True` / `= False`)
    reddens one line or the other -- no blanket answer survives."""
    assert _s3_bucket_from_domain("opal-data-portal-v2.s3.us-east-1.amazonaws.com")  # OAC S3 -> s3
    assert _s3_bucket_from_domain("opal-data-bd.s3.us-east-1.amazonaws.com")         # OAI S3 -> s3
    assert not _s3_bucket_from_domain("7k3ed8px20.execute-api.us-east-1.amazonaws.com")
    assert not _s3_bucket_from_domain("f61h681z9g.execute-api.us-east-1.amazonaws.com")


def test_R1_real_config_the_PARSER_types_every_origin_by_its_domain():
    """THE TEST THAT ACTUALLY GUARDS DIRECTION 2 -- and the one I initially failed to write.

    My first direction-2 test built a fixture with origin_type="api_gateway" HARDCODED, so it exercised
    the RENDERER and never the CLASSIFIER: the mutant `is_s3 = True` sailed through it. A hand-set
    fixture field measures the author's expectation, not the parser. This runs the REAL parser over the
    REAL config and asserts the classification itself, in both directions:
      MUTANT `is_s3 = True`                    -> execute-api origins become "s3"  -> REDDENS (line 2)
      MUTANT `is_s3 = 's3_origin_config' in b` -> OAC S3 origins become api_gateway -> REDDENS (line 1)
    """
    rt = build_routing_table(_WORKSPACE)
    for oid, o in rt.origins.items():
        if ".s3." in o.domain_name or o.domain_name.endswith(".s3.amazonaws.com"):
            assert o.origin_type == "s3", f"{oid} ({o.domain_name}) is an S3 domain typed {o.origin_type!r}"
            assert o.bucket_name, f"{oid} is an S3 origin with no bucket"
        elif "execute-api" in o.domain_name:
            assert o.origin_type == "api_gateway", (
                f"{oid} ({o.domain_name}) is an API Gateway typed {o.origin_type!r} -- an over-correction "
                f"that would strip a real authorizer from the auth map"
            )
            assert not o.bucket_name, f"{oid} is an API Gateway origin carrying a bucket name"


def test_R1_bucket_derivation_is_not_split_on_first_dot():
    """A dotted bucket name is where the domain-derived bucket and the old `split('.')[0]` expression
    diverge. Over TODAY's origin set the two agree exactly (verified: 8/8 identical), which makes the
    old expression an EQUIVALENT mutant rather than a caught one -- so this pins the difference
    directly instead of relying on a mutant that cannot express it.
    MUTANT (`domain.split('.')[0]`) returns "my" -> REDDENS."""
    assert _s3_bucket_from_domain("my.dotted.bucket.s3.us-east-1.amazonaws.com") == "my.dotted.bucket"


def test_R1_real_config_no_s3_origin_is_grouped_as_authorizer_protected():
    """The REAL committed CloudFront config, which is where the false-secure reading actually lived.
    Every path in the authorizer section must resolve to a non-S3 origin. This is the assertion that
    fails if anyone reintroduces the OAI-only typing, and it is grain-correct: it checks the PROPERTY
    (no S3 origin claims an authorizer) rather than pinning today's specific path list."""
    rt = build_routing_table(_WORKSPACE)
    out = _auth_map(rt)
    section = _auth_section(out, "EDGE JWT + API GW AUTHORIZER:")
    offenders = [oid for oid, o in rt.origins.items()
                 if o.bucket_name and f"-> {oid}" in section]
    assert not offenders, (
        f"FALSE-SECURE: S3 origin(s) {offenders} reported under 'EDGE JWT + API GW AUTHORIZER' "
        f"in the real config -- an authorizer claimed for a path no authorizer guards"
    )


# ---------------------------------------------------------------------------
# LAYER 6 -- `trace --json <url>`: the outcome CLASS as a first-class enum.
# Before this, the behavior branch returned before the JSON emitter, so --json silently produced
# PROSE for every URL query -- a flag promising machine-readable output and returning human text.
# Requested by 0.8.0_AE_CloudComp~B (TOOLBHVR.ROUTE) so a router cannot collapse the three outcomes.
# Mutant target: the `if args.json` arm in cmd_trace / the outcome branches in _url_trace_payload.
# ---------------------------------------------------------------------------

def _trace_json(url: str, rt: RoutingTable | None = None) -> dict:
    import json as _json
    return _json.loads(_trace_raw_json(url, rt))


def _trace_raw_json(url: str, rt: RoutingTable | None = None) -> str:
    class _Args:
        json = True

    args = _Args()
    args.query = url
    orig = routes_cli._build_rt
    routes_cli._build_rt = lambda rt=(rt or _rt()): rt
    try:
        buf = io.StringIO()
        with redirect_stdout(buf):
            routes_cli.cmd_trace(args)
        return buf.getvalue()
    finally:
        routes_cli._build_rt = orig


def test_json_flag_emits_json_not_prose():
    """DIRECTION 1, and the defect this layer fixes: --json on a URL must PARSE. MUTANT (remove the
    `if args.json` arm from the behavior branch, restoring the fall-through to prose) -> json.loads
    raises -> REDDENS. A flag that silently ignores itself is the honesty class, not a UX nit."""
    for url in (MDPF_URL, "/zzz/nothing.json"):
        raw = _trace_raw_json(url)
        assert raw.lstrip().startswith("{"), f"--json returned prose for {url}: {raw[:60]!r}"
        assert isinstance(_trace_json(url), dict)


def test_outcome_enum_discriminates_all_four_classes():
    """The enum is the whole point: a consumer must not have to recover the class by string-matching
    "UNRESOLVED" or "!!" out of prose. MUTANT (collapse any two branches in _url_trace_payload, e.g.
    return RESOLVED whenever a behavior matched) -> REDDENS, because two classes become equal."""
    no_default = _rt()
    no_default.behaviors = [b for b in no_default.behaviors if b.order != 0]

    assert _trace_json(MDPF_URL)["outcome"] == "RESOLVED"
    assert _trace_json("/api/general/")["outcome"] == "RESOLVED"
    assert _trace_json("/zzz/nothing.json")["outcome"] == "CATCHALL_DEFAULT"
    assert _trace_json("/zzz/nothing.json", rt=no_default)["outcome"] == "NO_MATCH"

    outcomes = {
        _trace_json(MDPF_URL)["outcome"],
        _trace_json("/zzz/nothing.json")["outcome"],
        _trace_json("/zzz/nothing.json", rt=no_default)["outcome"],
    }
    assert len(outcomes) == 3, f"outcome classes collapsed: {outcomes}"


def test_unresolved_no_rule_is_its_own_class_not_folded_into_catchall():
    """A SPECIFIC behavior matched but no rewrite rule covers the prefix -- missing coverage, which is
    NOT the same as a catch-all fall-through. MUTANT (fold UNRESOLVED_NO_RULE into CATCHALL_DEFAULT,
    or into RESOLVED with a null key) -> REDDENS."""
    rt = _rt()
    rt.behaviors.append(CloudFrontBehavior(path_pattern="/v1/*", origin_id="S3-data-json", order=21))
    payload = _trace_json("/v1/anything", rt=rt)
    assert payload["outcome"] == "UNRESOLVED_NO_RULE"
    assert payload["catchall"] is False
    assert payload["s3_key"] is None
    assert "NOT a proof that no key exists" in payload["disclosure"]


def test_catchall_outranks_resolved_and_catchall_is_its_own_axis():
    """THE PRECEDENCE RULE, bound so it cannot drift silently. A catch-all match and a rewrite match are
    independent axes. If no specific behavior claimed the path we do not know it is served at all, so
    CATCHALL_DEFAULT outranks RESOLVED even when a key is derivable -- the conservative direction.
    MUTANT (check `rule is not None` before `behavior.order == 0`) returns RESOLVED -> REDDENS, and a
    consumer would read a real resolution out of a path nothing claimed."""
    rt = _rt()
    # Make the DEFAULT slot the thing that matches a URL a rewrite rule also covers.
    rt.behaviors = [CloudFrontBehavior(path_pattern="/*", origin_id="S3-data-json", order=0)]
    payload = _trace_json(MDPF_URL, rt=rt)
    assert payload["outcome"] == "CATCHALL_DEFAULT", "catch-all must outrank a derivable key"
    assert payload["catchall"] is True
    # The key is still reported -- the caveat rides on `outcome`, and `catchall` stays a separate axis
    # so neither has to be recovered from the other.
    assert payload["s3_key"] == MDPF_KEY


def test_json_payload_carries_plane_and_blind_spots_from_the_contract():
    """`plane`/`vintage`/`blind_spots` are read from comp-routes' output contract at run time, not
    hardcoded here -- so a corrected blind spot reaches every consumer without a second edit, and a
    rail cannot drift from the declaration. MUTANT (hardcode the strings) survives this test but is
    caught by the contract being the single source; MUTANT (drop the fields) -> REDDENS."""
    payload = _trace_json(MDPF_URL)
    assert payload["plane"] == "desired"
    assert isinstance(payload["blind_spots"], list) and payload["blind_spots"], "blind spots must ride along"
    assert any("TRANSCRIBED" in b for b in payload["blind_spots"]), (
        "the transcribed-not-parsed blind spot must reach machine consumers, not just human readers"
    )
    assert payload["vintage"] and payload["vintage"] != "UNKNOWN"


def test_real_config_the_mdpf_origin_now_carries_its_bucket():
    """The real committed CloudFront config, not a fixture: the OAC-fronted MDPF origin resolves its
    bucket. This is the assertion that would have caught the original defect on the live estate."""
    rt = build_routing_table(_WORKSPACE)
    origin = rt.origins.get("S3-opal-data-portal-v2-json")
    assert origin is not None, "MDPF origin missing -- Terraform parser/path drift"
    assert origin.bucket_name == MDPF_BUCKET


def test_real_config_the_mdpf_url_resolves_end_to_end():
    """The full acceptance on the REAL routing table: the MDPF URL resolves through the real committed
    rewrite table to its real key. Guards against a fixture that passes while the estate does not."""
    rt = build_routing_table(_WORKSPACE)
    assert rt.resolve_s3_key(MDPF_URL) == MDPF_KEY
    assert rt.match_rewrite_rule(MDPF_URL).url_prefix == "/api/general/json/"
