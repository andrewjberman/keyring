"""
Tests for comp-route -- the NFRA_COMPROUTE core posterior decision engine (Stage-1 L3).

Locks the load-bearing invariants (PRD docs/architecture/NFRA_COMPROUTE_PRD.md sections 2/3/9 +
CTO rulings 2/3/4) so a later weight/scorer change cannot silently break them:

  - PRIOR-not-FILTER: the prior biases, never excludes (a strong query on a non-ctx surface still routes).
  - never-silent-argmax: within eps => disambiguation surfacing BOTH with their concern.
  - capability-map-AGNOSTIC (section 9c): the SAME engine routes a non-tool smoke provider unchanged.
  - Goodhart-honest (ruling 4): history_affinity is OUTCOME-weighted, never invocation count.
  - graceful cold-start: no affinity provider => score = query + prior + margin, still routes.

Author: 0.8.0_AE_CloudComp~E (NFRA_COMPROUTE Stage-1 L3). 2026-07-01.
"""

from __future__ import annotations

import sys
from pathlib import Path

_WORKSPACE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.comp_route import (  # noqa: E402
    Capability,
    DictAffinityProvider,
    DictCapabilityProvider,
    build_fixture_caps,
    RouteContext,
    Weights,
    _self_test,
    build_fixture_provider,
    build_smoke_provider,
    outcome_weighted_affinity,
    route,
)


def test_self_test_all_pass():
    """The in-module self-test IS the PRD section-9c smoke + the 2 grounded section-2 cases. All pass."""
    ok, checks = _self_test()
    failed = [c["check"] for c in checks if not c["pass"]]
    assert ok, f"failing checks: {failed}"


def test_within_margin_disambiguates_never_argmax():
    """Two capabilities within eps => a disambiguation surfacing BOTH, each with a concern -- never a
    silent argmax (CTO ruling 3)."""
    prov = build_fixture_provider(role_surface_affinity={"DE": {"graph": 0.6, "portal": 0.7}})
    r = route("similar components", RouteContext(role="DE"), prov)
    assert r.kind == "disambiguation"
    ids = {s.cap.id for s in r.within_margin}
    assert {"comp-cluster", "comp-transform"} <= ids
    assert all(s.cap.concern for s in r.within_margin)


def test_prior_is_additive_not_a_filter():
    """A capability on a surface ABSENT from role_surface_affinity (prior 0.0) with the strongest
    query_match is never excluded -- it wins or lands within-margin (CTO ruling 3, PRIOR-not-FILTER)."""
    prov = build_fixture_provider(role_surface_affinity={"DE": {"graph": 0.9}})   # portal absent -> 0.0
    r = route("component schema field props", RouteContext(role="DE"), prov)
    transform = next(s for s in r.ranked if s.cap.id == "comp-transform")
    assert transform.prior == 0.0
    assert "comp-transform" in {s.cap.id for s in r.within_margin}


def test_same_surface_prior_is_necessary_not_sufficient():
    """Two capabilities on the SAME surface get EQUAL prior => the prior cannot disambiguate them; the
    likelihood (query_match) carries the decision (PRD section-2 case B)."""
    prov = build_fixture_provider(role_surface_affinity={"AE": {"estate": 0.8}})
    r = route("estate drift", RouteContext(role="AE"), prov)
    pri = {s.cap.id: s.prior for s in r.ranked}
    assert abs(pri["comp-drift"] - pri["comp-aws"]) < 1e-9
    # removing the prior entirely leaves the same top-2 contenders -> prior alone did not decide it.
    r_np = route("estate drift", RouteContext(role="AE"), prov, weights=Weights(w_q=0.75, w_s=0.0, w_h=0.25))
    assert {s.cap.id for s in r.ranked[:2]} == {s.cap.id for s in r_np.ranked[:2]} == {"comp-drift", "comp-aws"}


def test_cold_start_routes_without_affinity():
    """No affinity provider => cold_start flagged, still returns a valid decision/disambiguation."""
    prov = build_fixture_provider(role_surface_affinity={"AE": {"estate": 0.8}})
    r = route("estate drift", RouteContext(role="AE"), prov)
    assert r.cold_start is True
    assert r.kind in ("decision", "disambiguation")


def test_generalization_interface_is_real_smoke_provider():
    """PRD section 9c: a NON-tool capability map (a library) routes through the SAME route() with zero
    engine change. This is the systems-alpha property -- the engine does not assume comp-tools."""
    smoke = build_smoke_provider(role_surface_affinity={"patron": {"reference-hall": 0.7}})
    r = route("look up a fact in the encyclopedia", RouteContext(role="patron"), smoke)
    assert r.ranked and r.ranked[0].cap.id == "reference-desk"


def test_affinity_is_outcome_weighted_not_count():
    """CTO ruling 4 / Goodhart: a capability with FEW high-outcome rows beats one with MANY low-outcome
    (FAIL/DENY) rows. Raw invocation count must never win."""
    rows = (
        [{"tool": "good", "role": "DE", "result": "PASS", "gap_text": "found a gap"}] * 4
        + [{"tool": "spammy", "role": "DE", "result": "DENY"}] * 40
        + [{"tool": "spammy", "role": "DE", "result": "FAIL"}] * 40
    )
    a_good = outcome_weighted_affinity(rows, "good", "DE")
    a_spam = outcome_weighted_affinity(rows, "spammy", "DE")
    assert a_good is not None and a_spam is not None
    assert a_good > a_spam
    assert outcome_weighted_affinity(rows, "unseen-tool", "DE") is None   # no rows -> cold-start (None)


def test_affinity_provider_is_per_cap_id_and_disambiguates_same_surface():
    """CTO ruling 2026-07-01: the learned term keys PER-CAP-ID, so it disambiguates two same-surface
    tools (comp-drift vs comp-aws, both 'estate') -- the one job a surface-grain term could not do. A
    cold cap backs off to its surface_prior (the m-estimate prior; the (c) hybrid subsumed)."""
    prov = build_fixture_provider(role_surface_affinity={"AE": {"estate": 0.8}})
    tie = route("estate", RouteContext(role="AE"), prov)
    assert {"comp-drift", "comp-aws"} <= {s.cap.id for s in tie.within_margin}   # tie without affinity
    aff = DictAffinityProvider({("comp-drift", "AE"): 0.95, ("comp-aws", "AE"): 0.2})
    dis = route("estate", RouteContext(role="AE"), prov, affinity_provider=aff)
    assert dis.decision is not None and dis.decision.cap.id == "comp-drift"      # affinity breaks the tie
    assert next(s for s in dis.ranked if s.cap.id == "comp-drift").affinity == 0.95
    aff2 = DictAffinityProvider({("comp-drift", "AE"): 0.95})                    # comp-aws now cold
    dis2 = route("estate", RouteContext(role="AE"), prov, affinity_provider=aff2)
    aw = next(s for s in dis2.ranked if s.cap.id == "comp-aws")
    assert aw.affinity == aw.prior == 0.8                                        # cold cap -> surface_prior


def _curated_ex(intent, ctx_d):
    return [{"cap_id": "comp-drift", "confidence": 1.0, "vetted": True}] if "parity" in intent else []


def _surface_first_ex(intent, ctx_d):
    return [{"cap_id": "comp-aws", "confidence": 0.8, "vetted": True}] if "estate" in intent else []


def test_default_router_vetted_signal_dominates_structurally():
    """DR1 (CTO ruling 2026-07-01): a curated hit on a PARAPHRASE the bare posterior would misroute wins
    as a confident DECISION -- the vetted band [1.0,2.0) dominates by construction (the 4-paraphrase
    regression fix). curated (1.0->2.0) beats surface-first (0.8->1.8) by confidence-ordering."""
    prov = build_fixture_provider(role_surface_affinity={"AE": {"estate": 0.8}})
    r = route("run the parity check", RouteContext(role="AE"), prov, extractors=[_curated_ex, _surface_first_ex])
    assert r.kind == "decision" and r.decision.cap.id == "comp-drift"
    assert r.decision.vetted and r.decision.score >= 1.0
    # both vetted, curated (2.0) > surface-first (1.8), structurally
    r2 = route("estate parity", RouteContext(role="AE"), prov, extractors=[_curated_ex, _surface_first_ex])
    aws = next(s for s in r2.ranked if s.cap.id == "comp-aws")
    assert r2.decision.cap.id == "comp-drift" and aws.vetted and aws.score < r2.decision.score


def test_default_router_read_excludes_write_path_keeps_recompute():
    """DR1 Stage-A (E1/DR3): a read intent hard-excludes write_path=True tools (a read must never trigger
    an 8-min derive) but KEEPS read-recompute tools (recompute on read, ANSWER reads, no mutation --
    excluding by the conflated mode:rebuild would wrongly drop them). Compute/legacy => no filter."""
    caps = build_fixture_caps() + [
        Capability("comp-aws-derive", ("aws", "estate", "derive"), surface="estate", grain="resource",
                   concern="REBUILD (8-min)", affinity_key="estate", write_path=True),
        Capability("comp-iam-read", ("iam", "policy", "estate", "aws"), surface="estate", grain="iam-policy",
                   concern="IAM read (recompute, no mutation)", affinity_key="estate", mode="recompute")]
    prov = DictCapabilityProvider(caps, role_surface_affinity={"AE": {"estate": 0.9}})
    read = {s.cap.id for s in route("aws iam estate", RouteContext(role="AE", intent_class="read"), prov).ranked}
    assert "comp-aws-derive" not in read and "comp-iam-read" in read
    compute = {s.cap.id for s in route("aws iam estate", RouteContext(role="AE"), prov).ranked}
    assert "comp-aws-derive" in compute   # no intent_class -> no filter


def test_default_router_relevance_floor_falls_back_not_prior_rescued():
    """DR1 Stage-C: an intent with ~0 relevance (no vetted, ~0 query) FALLS BACK to grep/glob even when a
    surface_prior is high -- the floor measures relevance, not the prior bias (a high prior never rescues
    a zero-relevance intent). Never a forced misroute / dead-end."""
    prov = build_fixture_provider(role_surface_affinity={"AE": {"estate": 0.8}})
    r = route("xyzzy nonsense unmatched", RouteContext(role="AE"), prov, extractors=[_curated_ex])
    assert r.kind == "fallback" and r.fallback in ("comp-grep", "comp-glob")


def test_default_router_is_backward_compatible_backstop():
    """DR1: with no extractors + no intent_class, route() is EXACTLY the legacy posterior backstop (no
    vetted band, no mode filter, no fallback) -- comp-which stays on it until the shadow cert flips DR2."""
    prov = build_fixture_provider(role_surface_affinity={"DE": {"graph": 0.6, "portal": 0.7}})
    r = route("similar components", RouteContext(role="DE"), prov)
    assert r.kind == "disambiguation" and all(not s.vetted for s in r.ranked) and r.fallback is None


def test_engine_consumes_a_foreign_capability_object_duck_typed():
    """The engine duck-types the capability fields, so ~C's real L2 Capability (same 6 binding fields)
    is consumed with zero engine edit. A minimal ad-hoc capability object routes fine."""

    class ForeignCap:
        id = "x-tool"
        keywords = ("alpha", "beta")
        surface = "somewhere"
        grain = "thing"
        concern = "does a thing"
        affinity_key = "somewhere"
        routable = True

    class ForeignProvider:
        def capabilities(self):
            return [ForeignCap()]

        def surface_prior(self, affinity_key, ctx):
            return 0.5 if affinity_key == "somewhere" else 0.0

        def affinity_key(self, cap):
            return cap.affinity_key

    r = route("alpha beta", RouteContext(role="anyone"), ForeignProvider())
    assert r.ranked and r.ranked[0].cap.id == "x-tool"
    assert r.ranked[0].prior == 0.5
