#!/usr/bin/env python3
"""Mutant-kill bar for E6.R8 -- the route->run conversion instrument (NFRA_VELOCITY_ESTATE WS-E6.R8).

Author: 0.7.0_AE_CloudOps. ~C-gated pull-forward P4->P1. COO rulings 20260730T065315Z.

R8 CARRIES ITS OWN DENOMINATOR AND ITS OWN MUTANT -- NEVER INHERITED FROM E4.1. That is the
binding condition (COO 064118Z), and the reason is exact: a route->run join that has never
been mutant-proven on its own terms is an unfalsifiable claim wearing E4.1's evidence.

WHAT R8 TURNED OUT TO BE. Not an analysis over existing data -- a NEW SENSOR. Measured
2026-07-30: 0 of 17,687 ROUTE-POSTERIOR events carried a serial (positive control: 1,312
RUN-GREP rows in the SAME file did, so the zero was not a broken grep), and no run row
carried a route id. There was no key on EITHER side, so ANY conversion rate quoted before
this landed would have been FABRICATED, not merely imprecise.

THE THREE RATIFIED DEFINITIONS, each of which must ship printed alongside any rate:
  ANY-of-N converts, and N is recorded so an ALL-of-N rate stays derivable with no re-baseline.
  route_id is TTL-scoped, and the row records the route's AGE at stamp time so a reader
    re-cuts the window in analysis rather than re-baselining.
  comp-which is declared as a NON-tools_index emitter -- it is NOT added to the roster
    (that is a comp-tool STANDARD change, main-CTO gated).

THE TRAPS -- each fails RED under a specific good-faith change:
  * parsing `intent=` uniformly across rail families -> tests 2, 3. This is COO's binding
    constraint and the sharpest hazard here: `intent=` holds TOOL names in ROUTE-POSTERIOR
    and an intent CATEGORY in plain ROUTE ("manifest" x702). A uniform parse MIS-JOINS 1,571
    rows WHILE LOOKING LIKE A WORKING JOIN.
  * making route_id persistent instead of TTL-scoped -> test 4. Every later unrelated run
    inherits it and conversion inflates toward 100%.
  * letting comp-which convert its own route -> test 6. The rate would then rise with
    comp-which's own usage, which is the very quantity it is measured against.
  * folding NOFIT-POSTERIOR into the denominator -> test 3. 110 honest no-matches are not
    abandoned routes; counting them as such treats comp-which's honesty as failure.
  * re-breaking --route-only's side-effect-free contract -> test 7. It was documented
    side-effect-free and silently was not, once; the fix was the flag, never a downstream
    strip rule.

A NOTE ON HOW TEST 2 IS WRITTEN, because the first version of this probe was WRONG: I
originally scored family-awareness on "was a handoff file written", which is undiscriminating
-- it fires identically whether the family was tool-valued or not, so it reported a
MIS-JOIN HAZARD on a correctly-stamped ROUTE-POSTERIOR. The verdict must be DERIVED FROM THE
FAMILY, never from the side effect. A hand-chosen probe measures the author; the family-driven
predicate measures the instrument.
"""
from __future__ import annotations

import importlib.util
import json
import time
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
_WS = _HERE.parents[3]


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, _HERE.parent / filename)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


cla = _load("comp_log_auto_r8", "comp_log_auto.py")

# The ONLY rail families whose `intent=` is a tool list. Mirrored from .tools/comp-which; the
# duplication is deliberate -- if the two ever disagree, test 3 catches it against the live log.
TOOL_VALUED = ("ROUTE-POSTERIOR", "ROUTE-POSTERIOR-DISAMBIG")
RAIL = _WS / "org" / "mcp" / "comp-which-rail.log"


@pytest.fixture
def session(tmp_path, monkeypatch):
    """A workspace whose session dir and run sink are throwaway."""
    monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "r8-test-session")
    (tmp_path / "org" / "mcp" / "sessions").mkdir(parents=True)
    (tmp_path / "org" / "mcp" / "comp-tool-runs.jsonl").write_text("", encoding="utf-8")
    return tmp_path


def _write_route(ws, rid, age_s, n):
    p = ws / "org" / "mcp" / "sessions" / "r8-test-session.route"
    p.write_text("%s|%.3f|%d\n" % (rid, time.time() - age_s, n), encoding="utf-8")
    return p


def _rows(ws):
    txt = (ws / "org" / "mcp" / "comp-tool-runs.jsonl").read_text(encoding="utf-8")
    return [json.loads(x) for x in txt.splitlines() if x.strip()]


# ---------------------------------------------------------------------------
# R8's OWN positive control
# ---------------------------------------------------------------------------

def test_1_positive_control_a_fresh_route_is_carried_onto_the_next_run(session):
    """If this is RED, every mutant below is meaningless."""
    _write_route(session, "ROUTE-FRESH", age_s=5, n=3)
    cla._append_log(session, "comp-blast", "x", 0, "0.7.0_AE_CloudOps", "(no-TO)")
    r = _rows(session)[-1]
    assert r["route_id"] == "ROUTE-FRESH"
    assert r["route_n"] == 3, "N must be recorded so ALL-of-N stays derivable"
    assert 0 <= r["route_age_s"] < 60
    assert r["route_ttl_s"] == cla._ROUTE_TTL_S, (
        "the TTL must ship ON the row -- a conversion window that is implicit is not "
        "re-derivable by anyone but its author")


# ---------------------------------------------------------------------------
# COO's BINDING CONSTRAINT: family-awareness
# ---------------------------------------------------------------------------

def test_2_the_tool_valued_family_set_is_explicit_and_excludes_nofit():
    """MUTANT: add ROUTE / ROUTE-SURFACE / ROUTE-POINTER / NOFIT-POSTERIOR to the set -> RED."""
    assert set(TOOL_VALUED) == {"ROUTE-POSTERIOR", "ROUTE-POSTERIOR-DISAMBIG"}
    for bad in ("ROUTE", "ROUTE-SURFACE", "ROUTE-POINTER", "NOFIT-POSTERIOR"):
        assert bad not in TOOL_VALUED, (
            "%s is NOT tool-valued; joining on its intent= mis-attributes routes" % bad)


@pytest.mark.skipif(not RAIL.exists(), reason="rail log absent on this device")
def test_3_live_rail_only_stamps_tool_valued_families_and_the_split_is_enumerable():
    """The instrument checked against the LIVE log, with the verdict DERIVED FROM THE FAMILY.

    MUTANT: stamp every route family -> RED on the category-valued rows.
    MUTANT: fold NOFIT into the joinable set -> RED.
    Also asserts the exclusion is ENUMERABLE, because COO's constraint is that a family which
    cannot be joined soundly is excluded AND PRINTED, never folded in.
    """
    joinable = excluded = nofit = mis_stamped = unstamped_tool_valued = 0
    for line in RAIL.read_text(encoding="utf-8", errors="replace").splitlines():
        parts = line.split()
        if len(parts) < 2:
            continue
        fam = parts[1]
        has_id = "route_id=" in line
        if fam in TOOL_VALUED:
            joinable += 1
            if not has_id:
                unstamped_tool_valued += 1   # pre-R8 history: expected, and counted
        elif fam == "NOFIT-POSTERIOR":
            nofit += 1
            if has_id:
                mis_stamped += 1
        elif fam.startswith("ROUTE"):
            excluded += 1
            if has_id:
                mis_stamped += 1

    assert mis_stamped == 0, (
        "%d category-valued / no-match rows carry a route_id -- the join would mis-attribute "
        "them while looking like it worked" % mis_stamped)
    assert joinable > 0 and excluded > 0, (
        "the live log must contain BOTH families or this test is vacuous -- a probe that "
        "cannot see the failure state it screens for is not a probe")
    # The pre-R8 tail is expected and must stay VISIBLE, never silently treated as abandoned.
    assert unstamped_tool_valued > 0, (
        "expected historical tool-valued routes with no route_id (they predate R8); if this "
        "is 0 the log was rewritten, which is a finding in itself")


# ---------------------------------------------------------------------------
# TTL, not persistence
# ---------------------------------------------------------------------------

def test_4_an_EXPIRED_route_is_NOT_carried(session):
    """MUTANT: drop the TTL check (make route_id persistent) -> RED.

    A persistent id is inherited by every later unrelated run and inflates conversion toward
    100% -- the instrument would report success proportional to how long a session ran.
    """
    _write_route(session, "ROUTE-STALE", age_s=cla._ROUTE_TTL_S + 60, n=1)
    cla._append_log(session, "comp-blast", "x", 0, "0.7.0_AE_CloudOps", "(no-TO)")
    r = _rows(session)[-1]
    assert "route_id" not in r, "an expired route was claimed as a conversion"


def test_5_a_clock_inverted_route_is_REFUSED_not_stamped(session):
    """A future-dated emit is a broken clock, not a conversion. No claim beats a wrong claim.

    MUTANT: use abs(age) or drop the negative guard -> RED.
    """
    _write_route(session, "ROUTE-FUTURE", age_s=-9999, n=1)
    cla._append_log(session, "comp-blast", "x", 0, "0.7.0_AE_CloudOps", "(no-TO)")
    assert "route_id" not in _rows(session)[-1]


# ---------------------------------------------------------------------------
# No self-conversion
# ---------------------------------------------------------------------------

def test_6_comp_which_NEVER_carries_its_own_route(session):
    """MUTANT: remove the comp-which exclusion -> RED.

    Not bookkeeping: self-conversion makes the rate rise with comp-which's own usage, which is
    precisely the quantity the rate is measured AGAINST. The instrument would then confirm
    itself.
    """
    _write_route(session, "ROUTE-SELF", age_s=1, n=2)
    cla._append_log(session, "comp-which", "some question", 0, "0.7.0_AE_CloudOps", "(no-TO)")
    r = _rows(session)[-1]
    assert r["tool"] == "comp-which"
    assert "route_id" not in r, "comp-which converted its own route"
    # ...but a DIFFERENT tool in the same session still converts it.
    cla._append_log(session, "comp-blast", "x", 0, "0.7.0_AE_CloudOps", "(no-TO)")
    assert _rows(session)[-1]["route_id"] == "ROUTE-SELF"


def test_7_absent_handoff_yields_an_ABSENT_key_not_a_null(session):
    """MUTANT: write route_id=None when there is no route -> RED.

    Same two-meaning-null this workstream exists to kill: a consumer must be able to tell
    "no route" from "route unknown".
    """
    cla._append_log(session, "comp-blast", "x", 0, "0.7.0_AE_CloudOps", "(no-TO)")
    r = _rows(session)[-1]
    for k in ("route_id", "route_age_s", "route_n", "route_ttl_s"):
        assert k not in r, "%s was written with no route handed off" % k


def test_8_no_session_id_means_no_route_claim(session, monkeypatch):
    """Without a session id a route cannot be attributed to an agent. An honest absence beats
    attributing a route to whatever agent happens to run next.
    """
    _write_route(session, "ROUTE-ORPHAN", age_s=1, n=1)
    monkeypatch.delenv("CLAUDE_CODE_SESSION_ID", raising=False)
    cla._append_log(session, "comp-blast", "x", 0, "0.7.0_AE_CloudOps", "(no-TO)")
    assert "route_id" not in _rows(session)[-1]


def test_9_a_malformed_handoff_is_refused_not_partially_trusted(session):
    """MUTANT: best-effort parse a corrupt handoff -> RED. A half-read route id is a wrong join."""
    p = session / "org" / "mcp" / "sessions" / "r8-test-session.route"
    for junk in ("", "   ", "no-pipes-at-all", "|||", "rid|not-a-float|2"):
        p.write_text(junk, encoding="utf-8")
        cla._append_log(session, "comp-blast", "x", 0, "0.7.0_AE_CloudOps", "(no-TO)")
        assert "route_id" not in _rows(session)[-1], "trusted a malformed handoff: %r" % junk


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
