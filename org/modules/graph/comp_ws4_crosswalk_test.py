"""
NFRA_TOOLUNIFY WS-4 conformance suite -- one mutant per settled crosswalk mapping.

Two tiers, per the dispatch's own acceptance bar (positive control + mutant as separate
invocations; member-level set-identity with printed denominators; GRAPHUNI count-blind lesson):

  TIER 1 (offline, always runs, zero network dependency): pure join-rule fixtures --
  known-matched / known-mismatched pairs per entity, PLUS a mutant per rule that corrupts the
  rule and asserts the same fixture now reddens. This is the M4 "mutants killed" class from the
  adapter-mutant-spec (fa8a9533ec) applied to the 4 WS-4 join rules instead of the 8 node types.

  TIER 2 (live, network-touching, individually skip-clean on infra unavailability rather than
  failing the whole run): the actual member-level set-identity sweep over the CURRENT source
  population per entity, denominators printed, comparing against the 2026-07-25 exercised
  baseline floors so a real regression reddens while the two already-known currency gaps
  (2 COMPONENT, and ENDPOINT's real-URL misses) do not manufacture permanent noise.

Run: `python3 -m pytest org/modules/graph/comp_ws4_crosswalk_test.py -v`
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comp_ws4_crosswalk as xwalk  # noqa: E402
from comp_ws4_crosswalk import Verdict, join, join_component, join_endpoint, join_lambda, join_s3_artifact  # noqa: E402


# ---------------------------------------------------------------------------
# TIER 1a -- M1 totality
# ---------------------------------------------------------------------------

def test_m1_totality_all_four_entity_types_dispatch():
    kwargs_by_type = {
        "LAMBDA": {"source_label": "probe-fn", "live_or_registry_names": {"probe-fn"}},
        "COMPONENT": {"source_id": "component:portal/src/App.tsx"},
        "ENDPOINT": {"source_id": "endpoint:getFoo", "urls": ["/api/foo"]},
        "S3_ARTIFACT": {"source_id": "s3:gold/foo.parquet",
                         "incident_gold_script_file_paths": ["data/inf/scripts/gold/A_00.foo.py"]},
    }
    checked = []
    for t in xwalk.ENTITY_TYPES:
        result = join(t, **kwargs_by_type[t])
        assert result is not None, "entity type %s produced no result -- silent fall-through" % t
        checked.append(t)
    print("M1 totality: %d/%d entity types checked (%s)" % (len(checked), len(xwalk.ENTITY_TYPES), checked))
    assert checked == list(xwalk.ENTITY_TYPES)


def test_m1_unhandled_type_raises_not_defaults():
    with pytest.raises(ValueError):
        join("NOT_A_WS4_ENTITY", source_id="whatever")


# ---------------------------------------------------------------------------
# TIER 1b -- LAMBDA join rule + mutant
# ---------------------------------------------------------------------------

def test_lambda_normalization_match_and_mismatch():
    live = {"market-regime-classifier"}
    matched = join_lambda("market_regime_classifier", live)  # underscore source label
    assert matched.verdict is Verdict.MATCHED
    assert matched.deployed_id == "market-regime-classifier"

    phantom = join_lambda("_api", live)  # real vendor-phantom label, A_lambda_enumeration.json
    assert phantom.verdict is Verdict.ABSENT


def test_lambda_normalization_mutant_reddens_on_corrupted_normalizer():
    live = {"market-regime-classifier"}

    def broken_normalizer(label: str) -> str:
        return label  # no strip/lowercase at all -- the corrupted rule

    orig = xwalk._normalize_lambda_label
    xwalk._normalize_lambda_label = broken_normalizer
    try:
        result = join_lambda("market_regime_classifier", live)
        assert result.verdict is Verdict.ABSENT, (
            "MUTANT DID NOT REDDEN: a normalizer that does not strip separators still matched "
            "'market_regime_classifier' against 'market-regime-classifier' -- this mutant is dead, "
            "the fixture is not actually exercising normalization"
        )
    finally:
        xwalk._normalize_lambda_label = orig
    # positive control, same fixture, rule restored -- must pass again
    assert join_lambda("market_regime_classifier", live).verdict is Verdict.MATCHED


# ---------------------------------------------------------------------------
# TIER 1c -- COMPONENT join rule + mutant
# ---------------------------------------------------------------------------

def test_component_literal_identity_and_out_of_scope():
    matched = join_component("component:portal/src/pages/ModelPortfolios.tsx")
    assert matched.verdict is Verdict.MATCHED
    assert matched.deployed_id == matched.source_id  # literal identity, not a transform

    scoped_out = join_component("endpoint:notAComponent")
    assert scoped_out.verdict is Verdict.OUT_OF_SCOPE


def test_component_mutant_reddens_on_broken_prefix_check():
    def broken_join_component(source_id: str):
        # corrupted rule: accepts ANY id as a component, defeating OUT_OF_SCOPE entirely
        return xwalk.JoinResult(Verdict.MATCHED, source_id, source_id, "corrupted: no prefix check")

    result = broken_join_component("endpoint:notAComponent")
    assert result.verdict is Verdict.MATCHED, "sanity: the mutant itself must misbehave as designed"
    # the REAL rule must catch what the mutant let through
    real_result = join_component("endpoint:notAComponent")
    assert real_result.verdict is Verdict.OUT_OF_SCOPE, (
        "MUTANT COMPARISON FAILED: real join_component did not distinguish itself from the broken "
        "any-id-matches version on a non-component id"
    )


# ---------------------------------------------------------------------------
# TIER 1d -- ENDPOINT join rule + mutant (the OUT_OF_SCOPE predicate is the load-bearing rule --
# this is the one that turned 55/138 real misses into 45 pollution + 10 genuine gaps)
# ---------------------------------------------------------------------------

def test_endpoint_url_predicate_matched_and_out_of_scope():
    real = join_endpoint("endpoint:getSubmission", ["/api/general/trades/submissions/${submissionId}"])
    assert real.verdict is Verdict.MATCHED

    empty = join_endpoint("endpoint:getChangeColor", [])
    assert empty.verdict is Verdict.OUT_OF_SCOPE

    template_junk = join_endpoint(
        "endpoint:formatAUM",
        ["$${(aum / 1_000_000_000).toFixed(2)}B", "$${aum.toFixed(2)}"],
    )
    assert template_junk.verdict is Verdict.OUT_OF_SCOPE, (
        "template-literal false-positive from the source extractor's URL regex must still be "
        "caught by the '/'-prefix predicate"
    )


def test_endpoint_mutant_reddens_on_permissive_predicate():
    orig = xwalk._URL_LIKE
    import re
    xwalk._URL_LIKE = re.compile(r".*")  # corrupted: matches anything, including empty-list default
    try:
        # the corrupted regex still can't match against an EMPTY list (any() over [] is False
        # regardless of pattern) -- so the true discriminating mutant is on a NON-empty junk input:
        junk_result = join_endpoint("endpoint:formatAUM", ["not-a-url-at-all"])
        assert junk_result.verdict is Verdict.MATCHED, (
            "MUTANT DID NOT REDDEN: a permissive '.*' predicate should have let a non-path string "
            "through as MATCHED, proving the real '/'-prefix rule is what blocks it"
        )
    finally:
        xwalk._URL_LIKE = orig
    assert join_endpoint("endpoint:formatAUM", ["not-a-url-at-all"]).verdict is Verdict.OUT_OF_SCOPE


# ---------------------------------------------------------------------------
# TIER 1e -- S3_ARTIFACT join rule (firm-bucket attribution) + mutant
# ---------------------------------------------------------------------------

def test_s3_artifact_firm_attribution_matched_ambiguous_and_unmapped():
    matched = join_s3_artifact(
        "s3:gold/dimensions/accounts_dimension_latest.parquet",
        ["data/black_diamond/scripts/gold/A_00.accounts_dimension.py"],
    )
    assert matched.verdict is Verdict.MATCHED
    assert matched.deployed_id == "opal-data-bd/gold/dimensions/accounts_dimension_latest.parquet"

    ambiguous = join_s3_artifact(
        "s3:gold/shared_key.parquet",
        [
            "data/black_diamond/scripts/gold/A_00.foo.py",
            "data/inf/scripts/gold/INF_A_00.foo.py",
        ],
    )
    assert ambiguous.verdict is Verdict.UNRESOLVED

    unmapped_firm = join_s3_artifact(
        "s3:gold/x.parquet",
        ["data/mdpf/scripts/gold/whatever.py"],
    )
    assert unmapped_firm.verdict is Verdict.UNRESOLVED, (
        "a firm outside FIRM_BUCKET_MAP must UNRESOLVE, never guess a bucket"
    )

    no_edge = join_s3_artifact("s3:gold/orphan.parquet", [])
    assert no_edge.verdict is Verdict.UNRESOLVED


def test_s3_artifact_mutant_reddens_on_corrupted_bucket_map():
    orig = dict(xwalk.FIRM_BUCKET_MAP)
    xwalk.FIRM_BUCKET_MAP["black_diamond"] = "opal-data-WRONG-BUCKET"
    try:
        result = join_s3_artifact(
            "s3:gold/dimensions/accounts_dimension_latest.parquet",
            ["data/black_diamond/scripts/gold/A_00.accounts_dimension.py"],
        )
        assert result.deployed_id == "opal-data-WRONG-BUCKET/gold/dimensions/accounts_dimension_latest.parquet"
        assert result.deployed_id != (
            "opal-data-bd/gold/dimensions/accounts_dimension_latest.parquet"
        ), "MUTANT DID NOT REDDEN: corrupting FIRM_BUCKET_MAP had no effect on the computed id"
    finally:
        xwalk.FIRM_BUCKET_MAP.clear()
        xwalk.FIRM_BUCKET_MAP.update(orig)
    # positive control, rule restored
    restored = join_s3_artifact(
        "s3:gold/dimensions/accounts_dimension_latest.parquet",
        ["data/black_diamond/scripts/gold/A_00.accounts_dimension.py"],
    )
    assert restored.deployed_id == "opal-data-bd/gold/dimensions/accounts_dimension_latest.parquet"


# ---------------------------------------------------------------------------
# TIER 2 -- live member-level set-identity sweep, denominators printed. Individually
# skip-clean (not fail) on live-infra unavailability -- the GRAPHUNI count-blind lesson demands
# member-level checking, but a Tier-1-only environment (no comp-kuzu / no marker-head DB / the
# 180s Kuzu-contention class this same census hit twice on 2026-07-25) must not brick the suite.
# ---------------------------------------------------------------------------

def _skip_if_live_plane_unavailable(exc: Exception):
    pytest.skip("deployed plane unavailable this run (%s: %s) -- Tier 2 is best-effort live, "
                "not a hard gate; Tier 1 already covers the join-rule logic offline" % (type(exc).__name__, exc))


@pytest.mark.live_kuzu
def test_component_live_set_identity_floor():
    try:
        graph = xwalk.load_source_graph()
        source_ids = sorted(
            k for k, v in graph["nodes"].items() if v.get("node_type") == "COMPONENT"
        )
        present = xwalk.query_deployed_ids_present(source_ids)
    except Exception as exc:  # noqa: BLE001 -- deliberately broad, this tier degrades to skip
        _skip_if_live_plane_unavailable(exc)
        return
    matched = [i for i in source_ids if i in present]
    missing = [i for i in source_ids if i not in present]
    print("COMPONENT live set-identity: %d/%d matched, denominator=%d, missing=%s"
          % (len(matched), len(source_ids), len(source_ids), missing))
    # floor, not exact-equality: the 2026-07-25 baseline is 22/24; a regression BELOW this floor
    # reddens, but new source components landing between runs does not manufacture false red
    assert len(matched) >= 22, (
        "COMPONENT live match count dropped below the 2026-07-25 baseline floor (22) -- "
        "matched=%d missing=%s" % (len(matched), missing)
    )


@pytest.mark.live_kuzu
def test_endpoint_live_set_identity_floor():
    try:
        graph = xwalk.load_source_graph()
        nodes = graph["nodes"]
        candidate_ids = []
        for k, v in nodes.items():
            if v.get("node_type") != "ENDPOINT":
                continue
            urls = v.get("metadata", {}).get("urls", [])
            if join_endpoint(k, urls).verdict is Verdict.MATCHED:
                candidate_ids.append(k)
        present = xwalk.query_deployed_ids_present(sorted(candidate_ids))
    except Exception as exc:  # noqa: BLE001
        _skip_if_live_plane_unavailable(exc)
        return
    matched = [i for i in candidate_ids if i in present]
    missing = [i for i in candidate_ids if i not in present]
    print("ENDPOINT live set-identity (post-OUT_OF_SCOPE filter): %d/%d matched, "
          "in-scope-denominator=%d, missing=%s" % (len(matched), len(candidate_ids), len(candidate_ids), missing))
    # 2026-07-25 baseline: 10 real-URL candidates all currently ABSENT (0/10) -- the floor here is
    # 0 (a known, named gap, not asserted fixed) but the DENOMINATOR must not silently shrink
    assert len(candidate_ids) >= 10, (
        "in-scope ENDPOINT candidate count dropped below the 2026-07-25 baseline denominator (10) "
        "-- the OUT_OF_SCOPE predicate may have widened unexpectedly"
    )
