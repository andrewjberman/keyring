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
    DictAffinityProvider,
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


def test_affinity_provider_moves_the_score():
    """A wired AffinityProvider contributes the w_h learned term (and clears cold_start)."""
    prov = build_fixture_provider(role_surface_affinity={"AE": {"estate": 0.8}})
    aff = DictAffinityProvider({("estate", "AE"): 0.9})
    r = route("estate drift", RouteContext(role="AE"), prov, affinity_provider=aff)
    drift = next(s for s in r.ranked if s.cap.id == "comp-drift")
    assert drift.affinity == 0.9
    assert r.cold_start is False


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
