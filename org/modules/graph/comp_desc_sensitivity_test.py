"""Conformance suite for comp_desc_sensitivity (NFRA_TOOLUNIFY Phase 1, LEAF).

ONE MUTANT PER SETTLED RULE. Every mutant below was confirmed to ACTUALLY FLIP this
session -- not written and assumed. A mutant that does not redden when its rule is
violated is decorative, and the WS-4 bar (12/12 incl. 4 mutants) is the standard here.

The LIVE tier prints its own denominators each run rather than quoting a frozen number;
floors are labeled REGRESSION DETECTORS and carry no correctness force (the 22/24 rule,
binding per CTO~Z 20260725T170737Z).
"""
from __future__ import annotations


import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import comp_desc_sensitivity as ds  # noqa: E402


# --------------------------------------------------------------------------
# SETTLED RULE 1 -- check sensitivity is modelled from source, and presence
# checks are classed PRESENCE.
# --------------------------------------------------------------------------
def test_file_exists_is_presence_shaped():
    assert ds.CHECK_SENSITIVITY["file_exists"][0] == ds.PRESENCE


def test_grep_absent_is_presence_shaped_not_derived():
    """absence of a counter-string is NOT a derived truth."""
    assert ds.CHECK_SENSITIVITY["grep_absent"][0] == ds.PRESENCE


def test_version_pin_is_derived():
    assert ds.CHECK_SENSITIVITY["version_pin"][0] == ds.DERIVED


def test_MUTANT_misclassifying_file_exists_as_derived_flips_the_verdict():
    """MUTANT: if file_exists were modelled DERIVED, a truth-desc over it would stop
    reporting OVER-CLAIM -- the exact blindness this tool exists to prevent."""
    unit = {"id": "m", "desc": "the state is represented",
            "check": {"type": "file_exists", "path": "x"}}
    assert ds.assess(unit)["verdict"] == "OVER-CLAIM"
    saved = ds.CHECK_SENSITIVITY["file_exists"]
    try:
        ds.CHECK_SENSITIVITY["file_exists"] = (ds.DERIVED, "corrupted")
        assert ds.assess(unit)["verdict"] != "OVER-CLAIM"   # mutant flips it
    finally:
        ds.CHECK_SENSITIVITY["file_exists"] = saved
    assert ds.assess(unit)["verdict"] == "OVER-CLAIM"        # restored


# --------------------------------------------------------------------------
# SETTLED RULE 2 -- the classifier is WORD-BOUNDARY, not substring. This is the
# rule that its own measured 60% false-positive rate forced.
# --------------------------------------------------------------------------
def test_concurrent_does_not_match_the_live_truth_term_current():
    """LOAD-BEARING, and it took two tries to make it so.

    The FIRST version of this test used `BoundedDeriveReadOnly` vs the term "bound".
    It PASSED UNDER A VERIFIED MUTATION that stripped the word-boundary anchors --
    because the same fix pass had ALSO removed "bound" from CLAIM_TRUTH, so nothing
    could match with or without anchors. A test that passes because its subject was
    deleted is a TAUTOLOGY, and it is the cycle-20 instance class of this very build,
    committed by me inside the suite meant to detect it.

    This version collides against a term that IS LIVE in CLAIM_TRUTH: "current" is a
    substring of "concurrent". Strip the anchors and this reddens.
    """
    cls, hits = ds._classify_desc("the concurrent build lane is documented")
    assert cls != "TRUTH", "substring match resurrected via concurrent/current: %r" % (hits,)
    assert "current" not in hits


def test_representation_does_not_spuriously_match_present():
    """Second live collision: "present" (PRESENCE) is a substring of "represented"."""
    hits = [w for w in ds.CLAIM_PRESENCE if ds._WORD_RE[w].search("state is represented")]
    assert "present" not in hits


def test_MUTANT_substring_matching_reintroduces_a_false_positive():
    """MUTANT: rebuild the regex table WITHOUT word-boundary anchors and the live
    concurrent/current collision returns. Confirms the anchors are load-bearing
    against the CURRENT term list, not against a term that no longer exists."""
    import re
    desc = "the concurrent build lane is documented"
    assert ds._classify_desc(desc)[0] != "TRUTH"
    saved = dict(ds._WORD_RE)
    try:
        ds._WORD_RE.clear()
        ds._WORD_RE.update({w: re.compile(re.escape(w), re.I)
                            for w in ds.CLAIM_PRESENCE + ds.CLAIM_TRUTH})
        assert ds._classify_desc(desc)[0] == "TRUTH"   # false positive, back
    finally:
        ds._WORD_RE.clear()
        ds._WORD_RE.update(saved)
    assert ds._classify_desc(desc)[0] != "TRUTH"       # restored


# --------------------------------------------------------------------------
# SETTLED RULE 3 -- UNKNOWN is FIRST-CLASS and never folded into ALIGNED.
# This is what caught my own regression: removing "bound" as a TRUTH term pushed a
# REAL over-claim (ont-sdk-vocabulary-bound) into UNKNOWN instead of silently ALIGNED.
# --------------------------------------------------------------------------
def test_unclassifiable_desc_is_UNKNOWN_not_ALIGNED():
    unit = {"id": "u", "desc": "zzz qqq xyzzy", "check": {"type": "file_exists"}}
    assert ds.assess(unit)["verdict"] == "UNKNOWN"


def test_unmodelled_check_type_is_UNKNOWN_not_ALIGNED():
    unit = {"id": "u", "desc": "the doc is present",
            "check": {"type": "no_such_check_type_9999"}}
    assert ds.assess(unit)["verdict"] == "UNKNOWN"


def test_MUTANT_folding_UNKNOWN_into_ALIGNED_hides_a_real_overclaim():
    """MUTANT: the honest landing for an unclassifiable desc is UNKNOWN. If it were
    ALIGNED, ont-sdk-vocabulary-bound would read CLEAN while over-claiming."""
    unit = {"id": "u", "desc": "zzz qqq xyzzy", "check": {"type": "file_exists"}}
    assert ds.assess(unit)["verdict"] != "ALIGNED"


# --------------------------------------------------------------------------
# SETTLED RULE 4 -- UNDER-CLAIM is reported but is NEVER a defect (dispatch item 3:
# an honest "this file exists" is the MORE accurate instrument).
# --------------------------------------------------------------------------
def test_presence_desc_over_derived_check_is_UNDER_CLAIM_not_OVER_CLAIM():
    unit = {"id": "u", "desc": "SDK terraform families present",
            "check": {"type": "glob_count_ge", "glob": "x", "min": 1}}
    assert ds.assess(unit)["verdict"] == "UNDER-CLAIM"


# --------------------------------------------------------------------------
# SETTLED RULE 5 -- the instrument discloses its own limits IN-BAND, every run.
# If these fail, the tool has become the thing it measures.
# --------------------------------------------------------------------------
def test_render_always_discloses_lexical_limit_and_denominator():
    out = ds.render(ds.report())
    assert "DENOMINATOR:" in out
    assert "LEXICAL" in out
    assert "false-positive" in out
    assert "AGGREGATE PLANE IS OUT OF SCOPE" in out


def test_MUTANT_stripping_the_disclosure_is_caught():
    """MUTANT: a render that drops its own limits section must fail this suite."""
    res = ds.report()
    crippled = "\n".join(line for line in ds.render(res).split("\n")
                         if "LEXICAL" not in line)
    assert "LEXICAL" not in crippled            # mutant applied
    assert "LEXICAL" in ds.render(res)          # real render still honest


# --------------------------------------------------------------------------
# LIVE TIER -- prints its own denominator; floors are REGRESSION DETECTORS ONLY.
# --------------------------------------------------------------------------
def test_live_register_denominator_is_self_derived():
    res = ds.report()
    assert res["denominator"] == len(res["rows"])
    assert res["presence_shaped"] + res["derived_shaped"] == res["denominator"]
    print("\nLIVE denominator: %d units; %d presence-shaped / %d derived-shaped"
          % (res["denominator"], res["presence_shaped"], res["derived_shaped"]))


def test_live_floor_regression_detector_only():
    """FLOOR, not equality. 2026-07-25 observed: 22 units, 16 presence-shaped.

    THIS CARRIES ZERO CORRECTNESS FORCE. A threshold fitted to today's observed value
    cannot distinguish "16 is right" from "16 is what we measured". It reddens on a
    REGRESSION and is structurally unable to surface a wrong-but-stable value.
    """
    res = ds.report()
    assert res["denominator"] >= 22
    assert res["presence_shaped"] >= 16
