"""
Tests for ADHC_COMPIL.005: nested/wildcard/dynamic key support in comp-platinum reverse.

AC5 requirement: >= 3 fixtures all FAIL against pre-005 implementation, PASS after.

FAILS BEFORE (pre-005):
  - _has_wildcard_segments, _normalize_field_path_wildcard, _wildcard_to_regex
    did not exist -- ImportError / AttributeError.
  - Wildcard query "rfs.decomposition_*.nna": _normalize_field_path stripped the
    '*' segment (not an identifier) -> normalized to "rfs.nna" -> wrong/empty match.
  - Dynamic query "role_aua.{role}.total": '{role}' stripped -> "role_aua.total"
    -> matched wrong paths or nothing.

PASSES AFTER (post-005):
  - All three helper functions exist and return correct values.
  - Wildcard regex matches correct paths in a mock index and rejects non-matching paths.
  - Dynamic key regex matches parameterized paths and prints a NOTE in output.
"""

from __future__ import annotations

import contextlib
import sys
from io import StringIO
from pathlib import Path
from unittest.mock import patch

_WORKSPACE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_WORKSPACE))

import org.modules.graph.platinum_cli as _cli  # noqa: E402


# ---------------------------------------------------------------------------
# Fixture 1 (AC5-a, AC2): Wildcard normalization preserves * segment
#
# FAILS BEFORE: _normalize_field_path_wildcard did not exist (AttributeError).
#   Old _normalize_field_path("rfs.decomposition_*.nna") -> "rfs.nna"
#   because "decomposition_*" is not a valid Python identifier.
# PASSES AFTER: new function returns "rfs.decomposition_*.nna" intact.
# ---------------------------------------------------------------------------

def test_wildcard_normalization_preserves_star():  # FAILS_BEFORE_FIX
    result = _cli._normalize_field_path_wildcard("rfs.decomposition_*.nna")
    assert result == "rfs.decomposition_*.nna", (
        f"Expected 'rfs.decomposition_*.nna', got '{result}'"
    )


def test_wildcard_normalization_strips_jspath_noise():  # FAILS_BEFORE_FIX
    # ?. is collapsed to .; * preserved within a segment
    result = _cli._normalize_field_path_wildcard("rfs?.decomposition_*?.nna")
    assert result == "rfs.decomposition_*.nna", (
        f"Expected 'rfs.decomposition_*.nna', got '{result}'"
    )


# ---------------------------------------------------------------------------
# Fixture 2 (AC5-b, AC3): Dynamic key normalization preserves {name} segments
#
# FAILS BEFORE: _normalize_field_path_wildcard did not exist (AttributeError).
#   Old _normalize_field_path("role_aua.{role}.total") -> "role_aua.total"
#   because "{role}" is not a valid Python identifier.
# PASSES AFTER: new function returns "role_aua.{role}.total".
# ---------------------------------------------------------------------------

def test_dynamic_key_normalization_preserves_braces():  # FAILS_BEFORE_FIX
    result = _cli._normalize_field_path_wildcard("role_aua.{role}.total")
    assert result == "role_aua.{role}.total", (
        f"Expected 'role_aua.{{role}}.total', got '{result}'"
    )


# ---------------------------------------------------------------------------
# Fixture 3 (AC5-a): _wildcard_to_regex matches wildcard paths correctly
#
# FAILS BEFORE: _wildcard_to_regex did not exist (AttributeError).
# PASSES AFTER: regex matches expected paths, rejects non-matching ones.
# ---------------------------------------------------------------------------

def test_wildcard_regex_star_segment():  # FAILS_BEFORE_FIX
    pat = _cli._wildcard_to_regex("rfs.decomposition_*.nna")
    # Should match exact and as suffix
    assert pat.search("rfs.decomposition_max.nna"), "should match decomposition_max"
    assert pat.search("rfs.decomposition_ytd.nna"), "should match decomposition_ytd"
    assert pat.search("data.rfs.decomposition_q1.nna"), "should match as suffix"
    # Should NOT match paths where wildcard segment is missing or has extra dots
    assert not pat.search("rfs.nna"), "should not match when middle segment absent"
    assert not pat.search("rfs.decomposition_max.aua"), "should not match different leaf"
    assert not pat.search("rfs.decomposition_max.nna.sub"), "should not match as prefix"


def test_wildcard_regex_dynamic_key():  # FAILS_BEFORE_FIX
    pat = _cli._wildcard_to_regex("role_aua.{role}.total")
    assert pat.search("role_aua.advisor.total"), "should match advisor"
    assert pat.search("role_aua.rep.total"), "should match rep"
    assert pat.search("role_aua.consultant.total"), "should match consultant"
    assert not pat.search("role_aua.total"), "should not match missing middle segment"
    assert not pat.search("role_aua.advisor.nna"), "should not match different leaf"


# ---------------------------------------------------------------------------
# Fixture 4 (AC5-b, AC2): End-to-end match selection with mock index
#
# FAILS BEFORE: _print_field_reverse used _normalize_field_path which stripped *,
#   yielding normalized="rfs.nna"; no index key ends with ".rfs.nna" -> 0 matches.
# PASSES AFTER: wildcard branch matches decomposition_max and decomposition_ytd,
#   not rfs.other.aua.
# ---------------------------------------------------------------------------

_MOCK_ENTRY = {
    "component": "PartnerAnalytics",
    "endpoint_function": "getPartnerData",
    "url_pattern": "/api/partner",
    "cf_behavior": "default",
    "cf_origin": "apigw",
    "cf_origin_type": "api_gateway",
    "auth_edge": True,
    "auth_api_gw": False,
    "s3_key": "platinum/firm/partner_analytics.json",
    "lambda_handler": "handler",
}

_MOCK_INDEX = {
    "rfs.decomposition_max.nna": [_MOCK_ENTRY],
    "rfs.decomposition_ytd.nna": [_MOCK_ENTRY],
    "rfs.other.aua": [_MOCK_ENTRY],
}


def _mock_print_field_reverse(query: str, index_override: dict) -> str:
    """Run _print_field_reverse with a controlled index, capture stdout."""
    with patch.object(_cli, '_build_field_reverse_index', return_value=index_override), \
         patch.object(_cli, '_print_gold_source', return_value=None), \
         patch.object(_cli, '_artifact_stems_matching', return_value=[]), \
         patch.object(_cli, '_portal_grep_hits', return_value=[]):
        out = StringIO()
        with contextlib.redirect_stdout(out):
            _cli._print_field_reverse(query, rt=None, dag=None)
        return out.getvalue()


def test_wildcard_match_selects_union_not_unrelated():  # FAILS_BEFORE_FIX
    output = _mock_print_field_reverse("rfs.decomposition_*.nna", _MOCK_INDEX)
    assert "decomposition_max.nna" in output, "should surface decomposition_max path"
    assert "decomposition_ytd.nna" in output, "should surface decomposition_ytd path"
    assert "rfs.other.aua" not in output, "should not surface unrelated rfs.other.aua"
    assert "WILDCARD" in output, "header should show WILDCARD routing"


def test_dynamic_key_emits_note():  # FAILS_BEFORE_FIX
    mock_index = {
        "role_aua.advisor.total": [_MOCK_ENTRY],
        "role_aua.rep.total": [_MOCK_ENTRY],
    }
    output = _mock_print_field_reverse("role_aua.{role}.total", mock_index)
    assert "NOTE:" in output, "dynamic key should emit semantics note"
    assert "{role}" in output, "note should name the dynamic segment"
    assert "DYNAMIC" in output, "header should show DYNAMIC routing"
    assert "role_aua.advisor.total" in output or "role_aua.rep.total" in output, \
        "should surface at least one matched path"


# ---------------------------------------------------------------------------
# AC4 regression: flat-key behavior unchanged
# ---------------------------------------------------------------------------

def test_flat_key_unchanged():
    mock_index = {
        "total_aua": [_MOCK_ENTRY],
        "unrelated_field": [_MOCK_ENTRY],
    }
    output = _mock_print_field_reverse("total_aua", mock_index)
    assert "total_aua" in output
    assert "unrelated_field" not in output
    # Should NOT show WILDCARD header
    assert "WILDCARD" not in output
    assert "NOTE:" not in output
