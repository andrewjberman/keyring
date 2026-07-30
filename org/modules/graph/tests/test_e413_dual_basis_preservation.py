#!/usr/bin/env python3
"""Mutant-kill bar for E4.1 CONDITION 3 -- dual-basis preservation (NFRA_VELOCITY_ESTATE WS-E4.1).

Author: 0.7.0_AE_CloudOps. Dispatch 2.0.0_SA_COO 20260730T053344Z + refinement
20260730T053709Z: "E4.1.3 is not satisfied by a `verdict_basis` column existing. It is
satisfied by a query that returns the ORIGINAL series and a query that returns the
RE-BASELINED series, both run, both disagreeing where you expect them to disagree."

WHAT CONDITION 3 IS ACTUALLY FOR
--------------------------------
A re-baselined series and an original series differ by an unknown mixture of two causes:
"the verdict logic changed" and "the estate changed". Both move the series IDENTICALLY.
The only thing that separates them is the BASIS IDENTITY, and it is unrecoverable if it
is not captured at the moment of the re-baseline -- which is why preservation must happen
IN the same motion, not after.

The 2026-07-23 shape preserved the VALUE (`result_prior`) but not the LOGIC. With 51
tools still pending declaration the contract surface WILL move again, and
`rebaselined: true` cannot separate a v1 re-baseline from a v2 one.

THE TRAPS -- each fails RED under a specific good-faith change:
  * making the basis id a bare version string ("the hash is noise") -> test 2. A hand edit
    that does not bump `version:` still changes the derivation; a basis id blind to that
    is a lie with a version number on it.
  * recomputing the as-written verdict "for consistency" -> test 4. That destroys the very
    residue the condition exists to keep, and it would look like a cleanup.
  * reporting IDENTICAL series as a PASS -> test 6. This is the failure mode COO named
    explicitly: identical output means either the re-baseline changed nothing OR the basis
    switch is not wired, and those two need different responses.
  * dropping the corpus span from the report -> test 7. C5's four-month trend is not
    derivable on this 16-day corpus, and only the span disclosure surfaces that.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, _HERE.parent / filename)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


rb = _load("comp_msbeff_rebaseline_under_test", "comp_msbeff_rebaseline.py")


# A fixture corpus. comp-blast is a DECLARED verdict tool (rc1/rc2 verdict, rc3 refuse), so
# a frozen-era "FAIL" on rc3 must re-verdict to REFUSE. comp-zzz-undeclared is absent from
# the contract surface, so its nonzero must land UNKNOWN.
_FIXTURE = [
    {"ts_epoch": 1784000000.0, "tool": "comp-blast", "rc": 3, "result": "FAIL", "serial": "s"},
    {"ts_epoch": 1784000100.0, "tool": "comp-blast", "rc": 0, "result": "PASS", "serial": "s"},
    {"ts_epoch": 1784000200.0, "tool": "comp-blast", "rc": 2, "result": "FAIL", "serial": "s"},
    {"ts_epoch": 1784000300.0, "tool": "comp-zzz-undeclared", "rc": 1, "result": "FAIL", "serial": "s"},
]

# A corpus where the two bases AGREE (every row already correct), used to prove the
# "identical is not a pass" branch is reachable.
_AGREEING = [
    {"ts_epoch": 1784000000.0, "tool": "comp-blast", "rc": 0, "result": "PASS", "serial": "s"},
    {"ts_epoch": 1784000100.0, "tool": "comp-blast", "rc": 0, "result": "PASS", "serial": "s"},
]


@pytest.fixture
def corpus(tmp_path, monkeypatch):
    def _install(rows):
        p = tmp_path / "runs.jsonl"
        p.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
        monkeypatch.setattr(rb, "_RUNS", p)
        monkeypatch.setattr(rb, "_OUT", tmp_path / "rebaselined.jsonl")
        return p
    return _install


# ---------------------------------------------------------------------------
# BASIS IDENTITY
# ---------------------------------------------------------------------------

def test_1_positive_control_basis_ids_are_distinct_and_well_formed():
    assert rb.BASIS_AS_WRITTEN == "as-written"
    d = rb.derived_basis_id()
    assert d.startswith("derived@v"), d
    assert d != rb.BASIS_AS_WRITTEN
    assert "+" in d, "the basis id must carry a content hash, not only a version"


def test_2_basis_id_is_sensitive_to_the_CONTENT_of_the_contract_surface(monkeypatch):
    """MUTANT: build the basis id from `version:` alone -> RED.

    A hand edit to a contract that does not bump `version:` still changes every derived
    verdict. A basis id that cannot see that change cannot discriminate the two
    re-baselines it exists to distinguish.
    """
    before = rb.derived_basis_id()
    real = rb._contract_surface_id.__wrapped__ if hasattr(rb._contract_surface_id, "__wrapped__") else None
    assert real is None or callable(real)

    # Simulate a content-only edit by pointing the id function at a mutated byte stream.
    orig_read_bytes = Path.read_bytes

    def _patched(self):
        data = orig_read_bytes(self)
        if self.name == "comp-output-contracts.yaml":
            return data + b"\n# a content-only edit that does not bump version:\n"
        return data

    monkeypatch.setattr(Path, "read_bytes", _patched)
    after = rb.derived_basis_id()
    assert after != before, (
        "the basis id did not move on a content-only contract edit -- it is version-only, "
        "so two materially different derivations would share one id")
    assert after.split("+")[0] == before.split("+")[0], (
        "the version half should be unchanged; only the hash half should move")


# ---------------------------------------------------------------------------
# ROWS ALONGSIDE ROWS, AND THE ORIGINAL IS NEVER RECOMPUTED
# ---------------------------------------------------------------------------

def test_3_dual_basis_emits_two_rows_per_source_row(corpus):
    corpus(_FIXTURE)
    pairs = list(rb.dual_basis_rows())
    assert len(pairs) == 2 * len(_FIXTURE)
    bases = {b for b, _ in pairs}
    assert bases == {rb.BASIS_AS_WRITTEN, rb.derived_basis_id()}
    for _b, row in pairs:
        assert "verdict_basis" in row, "every emitted row must be self-identifying"


def test_4_as_written_verdict_is_PRESERVED_VERBATIM_never_recomputed(corpus):
    """MUTANT: recompute the as-written row's result "for consistency" -> RED.

    The as-written row IS the historical record of what the appender concluded. If it is
    recomputed, both rows carry the derived verdict and the residue is gone -- the exact
    irreversible loss ~C's finding 3 protects against.
    """
    corpus(_FIXTURE)
    as_written = [r for b, r in rb.dual_basis_rows() if b == rb.BASIS_AS_WRITTEN]
    assert [r["result"] for r in as_written] == ["FAIL", "PASS", "FAIL", "FAIL"], (
        "the as-written series was recomputed -- preservation is broken")
    derived = [r for b, r in rb.dual_basis_rows() if b != rb.BASIS_AS_WRITTEN]
    assert [r["result"] for r in derived] == ["REFUSE", "PASS", "VERDICT", "UNKNOWN"], (
        "the derived series is not re-classifying from rc under the current contracts")
    for r in derived:
        assert "result_as_written" in r, (
            "a derived row must carry the prior value too, so a single row is auditable "
            "without a join back to the other basis")


def test_5_the_two_bases_DISAGREE_on_a_corpus_where_they_should(corpus):
    """The exercise itself: not the column's presence, the query's answer."""
    corpus(_FIXTURE)
    rep = rb.dual_basis_compare()
    assert rep["group_disagreements"] >= 1, (
        "the two bases returned the same series on a corpus built to make them differ -- "
        "the basis switch is not wired")
    assert "EXERCISED" in rep["VERDICT"]
    tools = {t["tool"] for t in rep["per_tool_disagreements"]}
    assert "comp-blast" in tools


def test_6_IDENTICAL_series_is_reported_as_NOT_A_PASS(corpus):
    """MUTANT: return a pass when the two bases agree -> RED.

    COO's refinement, verbatim: if they come back identical, either the re-baseline
    changed nothing or the basis switch is not wired -- find out which. A tool that calls
    that a pass has removed the only signal that distinguishes them.
    """
    corpus(_AGREEING)
    rep = rb.dual_basis_compare()
    assert rep["group_disagreements"] == 0 and not rep["per_tool_disagreements"]
    assert "IDENTICAL" in rep["VERDICT"]
    assert "NOT a pass" in rep["VERDICT"], (
        "an identical dual-basis result was reported as a pass")
    assert "not wired" in rep["VERDICT"], (
        "the report must name BOTH possible causes, or the reader picks the flattering one")


# ---------------------------------------------------------------------------
# THE CORPUS DISCLOSURE -- what the number is OF
# ---------------------------------------------------------------------------

def test_7_corpus_profile_prints_span_months_and_device_scope(corpus):
    """MUTANT: drop span/months from the profile -> RED.

    C5's headline is a four-month trend. The rc-bearing corpus spans 16 days and one
    month, so that trend is not re-derivable here at all. Only the span disclosure turns
    that from an invisible mismatch into a stated limit.
    """
    corpus(_FIXTURE)
    cp = rb.corpus_profile()
    for k in ("rows", "earliest", "latest", "span_days", "months_present",
              "DEVICE_LOCAL", "TREND_CAPABILITY"):
        assert k in cp, "corpus_profile lost its %s disclosure" % k
    assert cp["rows"] == len(_FIXTURE)
    assert isinstance(cp["months_present"], dict) and cp["months_present"]
    assert "DEVICE-LOCAL" in cp["DEVICE_LOCAL"]


def test_8_every_series_carries_its_denominator_AND_its_predicate(corpus):
    """A rate without its denominator is not a measurement, and two honest predicates
    sharing one word moved this population by 3 rows (C5 April 221 vs 224: the
    `FAIL->FIXED` token). So the predicate ships with the number, always.
    """
    corpus(_FIXTURE)
    s = rb.series(rb.BASIS_AS_WRITTEN)
    assert "fail_predicate" in s and "FAIL->FIXED" in s["fail_predicate"], (
        "the FAIL predicate must be stated, naming the tokens it EXCLUDES")
    for _g, row in s["by_month"].items():
        assert "n" in row and "FAIL" in row and "rate_pct" in row
    assert s["by_tool"], "per-series decomposition is mandatory, never optional"


def test_9_no_aggregate_without_per_series_decomposition(corpus):
    """WS-E4.3's standing form, enforced structurally rather than by convention.

    An aggregate that moves because the mix moved is a rigorous instrument on the wrong
    axis. MUTANT: make by_tool optional/empty -> RED.
    """
    corpus(_FIXTURE)
    rep = rb.dual_basis_compare()
    assert "per_tool_disagreements" in rep
    s = rb.series(rb.derived_basis_id())
    assert len(s["by_tool"]) >= 2, (
        "the decomposition collapsed -- an aggregate would ship unaccompanied")


def test_10_sidecar_round_trips_one_basis_at_a_time(corpus, tmp_path):
    """The consumer contract: filter ONE column, get a complete clean series in `result`.

    MUTANT: store the two verdicts as two FIELDS on one row -> RED, because a consumer
    then needs per-basis field-selection logic, which is the shape that silently reads the
    wrong field.
    """
    corpus(_FIXTURE)
    info = rb.write_dual_basis_sidecar()
    rows = [json.loads(x) for x in Path(info["sidecar"]).read_text(encoding="utf-8").splitlines() if x.strip()]
    assert len(rows) == 2 * len(_FIXTURE)
    for basis in (rb.BASIS_AS_WRITTEN, rb.derived_basis_id()):
        sub = [r for r in rows if r["verdict_basis"] == basis]
        assert len(sub) == len(_FIXTURE), "a basis filter did not return a COMPLETE series"
        assert all("result" in r for r in sub), "the series is not readable from one field"
    meta = json.loads(Path(info["meta"]).read_text(encoding="utf-8"))
    assert meta["supersession_history"], "condition 3 also requires the history recorded"
    assert len(meta["supersession_history"]) >= 5
    assert "corpus_profile" in meta and "fail_predicate" in meta


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
