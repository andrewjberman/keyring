"""
comp-blast pairwise overlap (Andrew act 3) -- the metric must resist the failure modes that made
naive overlap useless, and the output must stay a QUESTION.

Andrew, verbatim: "if something has highly overlapping blast radius and is doing the same function,
that is very high friction, and needs to be assessed."
  COMPUTE overlap -> PROPOSE candidates -> a HUMAN assesses function-sameness.

WHAT THESE TESTS EXIST TO HOLD, each earned by a measured failure during the build:

1. THE HUB PROBLEM. Over 42 cot gold scripts, SIX consumer nodes were each shared by 19 of 25
   producers. Raw jaccard calls almost every pair a candidate, because a shared hub is what a
   pipeline looks like -- not what a duplicate looks like. Specificity weighting must score a
   hub-only pair BELOW an equally-sized specific-overlap pair.

2. THE THIN-EVIDENCE PROBLEM. The first sweep ranked, at a PERFECT 1.000, pairs of functions whose
   entire blast radius was one shared `log` call. wi/wu is scale-free and cannot tell "identical"
   from "standing on a single edge". Hence shared_mass, an absolute floor, and hence: A RATIO NEEDS
   A MAGNITUDE BESIDE IT.

3. SCOPE-VS-REFERENCE. idf computed inside a 5-node selector made a 112-of-333 hub look rare,
   because everything in view shared it. Specificity is an ESTATE property; the selector chooses
   which pairs are SCORED, never what "common" means.

4. THE PROHIBITION. Name-similarity, path-adjacency and shared-vertical are NOT evidence of
   function-sameness and may never be emitted as such. No such signal is computed; the output must
   never assert sameness.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve()
_GRAPH_DIR = _HERE.parents[1]
_CLI = _GRAPH_DIR / "cli.py"
_REPO = _GRAPH_DIR.parents[2]

if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))
from org.modules.graph import cli as _cli_mod  # noqa: E402  (same absolute form cli.py uses)


def _run(*argv: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(_CLI), "blast", *argv],
        capture_output=True, text=True, cwd=str(_REPO),
    )


#: THE SELECTOR IS DERIVED LIVE, NEVER HARDCODED -- and this is a repair, not a preference.
#:
#: These tests were written against `--population gold:A_`. When comp-blast's universe moved to the
#: canonical kuzu graph (2026-08-03/04) that prefix stopped matching ANYTHING: kuzu addresses the
#: same scripts as `pipeline:bd:gold:A_...` and carries ZERO `gold:`-prefixed ids. MEASURED at the
#: switch: selector `gold:A_` -> N=0, so the sweep scored "0 pair(s) of 0" and FOUR tests here kept
#: passing while exercising nothing --
#:   * the mass-floor test asserted "No pair cleared the threshold", which is TRUE BY CONSTRUCTION
#:     when there are no pairs at all, so it stopped testing the floor it exists to test;
#:   * the framing test asserted banned strings were ABSENT from output that printed no pairs;
#:   * the denominator test's per-pair loop body never executed.
#: All eight stayed green. GREEN WENT GREENER AND THE COVERAGE WENT TO ZERO -- the same class as the
#: skip caught in the sibling exit-code suite, one layer subtler because nothing even skipped.
#:
#: Deriving the selector from the live universe means the fixture cannot silently stop selecting;
#: and `_assert_non_vacuous` below makes any future emptiness FAIL instead of pass.
_SELECTOR_CACHE: list = []


def _selector() -> str:
    """A population prefix that actually selects producers in the CURRENT universe."""
    if _SELECTOR_CACHE:
        return _SELECTOR_CACHE[0]
    import pytest
    try:
        from org.modules.graph import comp_blast_universe as bu
        g, _p, _d = bu.load_kuzu_universe(refresh=False)
    except Exception as ex:  # noqa: BLE001
        pytest.skip(f"canonical universe unavailable: {ex}")
    ids, _def = bu.declared_producer_territory(g, None, "script")
    if len(ids) < 2:
        pytest.skip("fewer than 2 producers in the territory -- no pair to score")
    # Longest common-prefix namespace shared by a workable slice: walk candidate prefixes from the
    # most specific id downward until at least 2 producers match.
    head = ids[0]
    for cut in range(len(head), 0, -1):
        pref = head[:cut]
        if sum(1 for i in ids if i.startswith(pref)) >= 2:
            _SELECTOR_CACHE.append(pref)
            return pref
    _SELECTOR_CACHE.append("")
    return ""


def _assert_non_vacuous(out: str) -> None:
    """A sweep that scored NOTHING cannot support any assertion about scoring.

    Without this, every assertion in this file is satisfiable by an empty population -- which is
    exactly how four of them survived the universe swap. This turns that failure mode from a silent
    pass into a loud one.
    """
    for line in out.splitlines():
        if "CANDIDATES:" in line and "pair(s) of" in line:
            scored = int(line.rsplit("of", 1)[1].strip().split()[0])
            assert scored > 0, (
                "VACUOUS TEST: the sweep scored 0 pairs, so every assertion below passes "
                "trivially. The selector no longer selects anything in this universe."
            )
            return
    raise AssertionError("could not find the CANDIDATES denominator line -- cannot prove non-vacuity")


# ---- metric unit tests: synthetic, so the property is isolated from live-graph drift ----------

def _idf(df: dict, n: int) -> dict:
    import math
    return {c: math.log(n / d) for c, d in df.items()}


def test_hub_overlap_scores_below_specific_overlap():
    """THE CENTRAL PROPERTY. Same-sized intersections; only specificity differs."""
    n = 100
    df = {"hub1": 95, "hub2": 95, "rare1": 2, "rare2": 2}
    idf = _idf(df, n)
    hub_pair = _cli_mod._overlap_metrics(
        {"hub1": {"WRITES_S3"}, "hub2": {"WRITES_S3"}},
        {"hub1": {"WRITES_S3"}, "hub2": {"WRITES_S3"}}, idf)
    rare_pair = _cli_mod._overlap_metrics(
        {"rare1": {"WRITES_S3"}, "rare2": {"WRITES_S3"}},
        {"rare1": {"WRITES_S3"}, "rare2": {"WRITES_S3"}}, idf)
    assert hub_pair["jaccard"] == rare_pair["jaccard"] == 1.0, "raw jaccard cannot tell them apart"
    assert rare_pair["shared_mass"] > hub_pair["shared_mass"] * 10, (
        "specificity weighting failed: a pair sharing only universal hubs carries as much evidence "
        "as a pair sharing rare consumers. That is the false-positive engine this metric exists to "
        "defeat."
    )


def test_ratio_alone_ranks_thin_evidence_at_the_top():
    """Documents WHY shared_mass exists -- the defect is in the RATIO, so the ratio still shows it."""
    idf = _idf({"log": 60, "a": 2, "b": 2, "c": 2}, 100)
    thin = _cli_mod._overlap_metrics({"log": {"CALLS"}}, {"log": {"CALLS"}}, idf)
    thick = _cli_mod._overlap_metrics(
        {"a": {"WRITES_S3"}, "b": {"WRITES_S3"}, "c": {"WRITES_S3"}},
        {"a": {"WRITES_S3"}, "b": {"WRITES_S3"}, "c": {"WRITES_S3"}}, idf)
    assert thin["weighted_jaccard"] == thick["weighted_jaccard"] == 1.0
    assert thin["shared_mass"] < thick["shared_mass"], "mass must separate what the ratio cannot"


def test_write_targets_are_separated_from_reads_and_calls():
    """The verb is kept: 2 producers WRITING one sink is not 2 scripts CALLING one helper."""
    idf = _idf({"sink": 2, "helper": 2}, 100)
    m = _cli_mod._overlap_metrics(
        {"sink": {"WRITES_S3"}, "helper": {"CALLS"}},
        {"sink": {"WRITES_S3"}, "helper": {"CALLS"}}, idf)
    assert m["shared_write_targets"] == ["sink"], "write targets must be surfaced separately"
    assert m["verbs"].get("CALLS") == 1 and m["verbs"].get("WRITES_S3") == 1


def test_disjoint_pair_scores_zero():
    """Negative control: no shared consumer -> no evidence, on every metric."""
    idf = _idf({"x": 2, "y": 2}, 100)
    m = _cli_mod._overlap_metrics({"x": {"WRITES_S3"}}, {"y": {"WRITES_S3"}}, idf)
    assert m["intersection"] == 0
    assert m["jaccard"] == 0.0 and m["weighted_jaccard"] == 0.0 and m["shared_mass"] == 0.0


# ---- CLI behaviour: exercised end to end -----------------------------------------------------

def test_sweep_runs_without_a_query_positional():
    """--overlap-sweep ranges over a population; the positional guard must not block it.

    (`--all-producers` has this same shape and IS still blocked -- a separately reported defect.)
    """
    r = _run("--overlap-sweep", "--population", _selector(), "--min-score", "0.9", "--head", "1")
    assert "required: query" not in (r.stdout + r.stderr), "positional guard blocked the sweep"
    assert r.returncode == 0, f"rc={r.returncode}\n{r.stdout}\n{r.stderr}"


def test_output_is_framed_as_candidates_not_findings():
    """THE PROHIBITION, asserted on the surface a human actually reads."""
    r = _run("--overlap-sweep", "--population", _selector(), "--min-score", "0.4", "--head", "1")
    out = r.stdout
    _assert_non_vacuous(out)
    assert "CANDIDATES FOR HUMAN ASSESSMENT, NOT FINDINGS" in out
    assert "Overlap is NOT sameness" in out
    assert "NO name, path, or vertical signal is used" in out
    for banned in ("DUPLICATE:", "IS A DUPLICATE", "SAFE TO DELETE", "same function"):
        assert banned not in out, f"output asserted sameness/deletion: {banned!r}"


def test_denominators_are_coherent_and_estate_referenced():
    """df is estate-wide, so it may never be printed against the slice size (measured bug)."""
    r = _run("--overlap-sweep", "--population", _selector(), "--min-score", "0.4", "--head", "1")
    out = r.stdout
    _assert_non_vacuous(out)
    assert "idf REFERENCE population" in out, "the reference population must be stated"
    ref = None
    for line in out.splitlines():
        if "idf REFERENCE population:" in line:
            ref = int(line.split("idf REFERENCE population:")[1].strip().split()[0])
    assert ref and ref > 0
    for line in out.splitlines():
        if "producers estate-wide)" in line:
            shown = int(line.rsplit("of", 1)[1].strip().split()[0])
            assert shown == ref, f"df printed against {shown}, reference is {ref}"


def test_suppression_count_is_reported_not_silent():
    """A filter that hides pairs must say how many -- silent truncation reads as 'nothing there'."""
    # POSITIVE CONTROL FIRST: prove the same selector DOES score pairs without the floor.
    # Otherwise "No pair cleared the threshold" is satisfied by an empty population and this test
    # asserts nothing -- which is precisely what happened at the universe switch.
    control = _run("--overlap-sweep", "--population", _selector(), "--min-score", "0.4", "--head", "1")
    _assert_non_vacuous(control.stdout)

    r = _run("--overlap-sweep", "--population", _selector(), "--min-score", "0.4",
             "--min-mass", "9999", "--head", "1")
    assert "SUPPRESSED BY THE MASS FLOOR:" in r.stdout
    assert "No pair cleared the threshold" in r.stdout
    assert "not evidence that the estate has no duplication" in r.stdout, (
        "an empty result must not read as an all-clear"
    )
