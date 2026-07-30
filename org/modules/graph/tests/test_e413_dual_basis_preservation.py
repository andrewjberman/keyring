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
    oc = _load("comp_output_contract_sens", "comp_output_contract.py")

    # The id is lru_cached per process, which is CORRECT and must not be removed to make this
    # test easier: comp_log_auto runs one process per tool call, so it always reads fresh, and the
    # re-baseline computes the id once and labels one run with it. No production path can observe a
    # stale id. But that cache means this test MUST clear it around the mutation, or it would be
    # measuring the cache rather than the derivation -- and it would pass for the wrong reason.
    # (This test caught exactly that when the id was centralized into comp_output_contract.)
    oc.contract_surface_id.cache_clear()
    before = oc.derived_basis_id()

    # Simulate a content-only edit by pointing the id function at a mutated byte stream.
    orig_read_bytes = Path.read_bytes

    def _patched(self):
        data = orig_read_bytes(self)
        if self.name == "comp-output-contracts.yaml":
            return data + b"\n# a content-only edit that does not bump version:\n"
        return data

    monkeypatch.setattr(Path, "read_bytes", _patched)
    oc.contract_surface_id.cache_clear()
    after = oc.derived_basis_id()
    monkeypatch.undo()
    oc.contract_surface_id.cache_clear()
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


# ======================================================================================
# E4.3 ELEMENTS 1 / 4 / 5 -- the FORWARD rebuild (COO GO 20260730T072044Z)
# ======================================================================================

def test_11_element1_basis_id_has_ONE_implementation_not_two():
    """MUTANT: re-inline the basis-id computation in the re-baseline module -> RED.

    The appender stamps the basis at write time and this module labels the re-derived series. If
    those two ever computed the identity differently the discriminator would be worthless -- and
    "two implementations of a denominator's own identity" is the defect this lineage has recorded
    four generations of.
    """
    oc = _load("comp_output_contract_e43", "comp_output_contract.py")
    assert rb.derived_basis_id() == oc.derived_basis_id(), (
        "the re-baseline and the contract helper disagree on the basis id -- there are two "
        "implementations and the discriminator is unsound")
    assert rb._contract_surface_id() == oc.contract_surface_id()


def test_12_element1_appender_stamps_the_basis_on_EVERY_new_row(tmp_path, monkeypatch):
    """MUTANT: make verdict_basis conditional/optional on the run row -> RED.

    A row with NO basis is indistinguishable from a pre-E4.3 row, which is exactly the ambiguity
    element 1 closes. Even the failure path must emit a LOUD sentinel rather than omit the key.
    """
    cla = _load("comp_log_auto_e43", "comp_log_auto.py")
    (tmp_path / "org" / "mcp").mkdir(parents=True)
    (tmp_path / "org" / "mcp" / "comp-tool-runs.jsonl").write_text("", encoding="utf-8")
    monkeypatch.delenv("COMP_SYNTHETIC_FIXTURE", raising=False)
    cla._append_log(tmp_path, "comp-blast", "x", 0, "0.7.0_AE_CloudOps", "(no-TO)")
    row = json.loads((tmp_path / "org" / "mcp" / "comp-tool-runs.jsonl").read_text(encoding="utf-8").strip())
    assert "verdict_basis" in row, "a new row carries no basis -- element 1 is not built"
    assert row["verdict_basis"].startswith("derived@v")

    # and with the derivation unavailable it must still say SOMETHING, loudly
    (tmp_path / "org" / "mcp" / "comp-tool-runs.jsonl").write_text("", encoding="utf-8")
    monkeypatch.setattr(cla, "_OC_OK", False)
    monkeypatch.setattr(cla, "_oc", None)
    cla._append_log(tmp_path, "comp-blast", "x", 0, "0.7.0_AE_CloudOps", "(no-TO)")
    row2 = json.loads((tmp_path / "org" / "mcp" / "comp-tool-runs.jsonl").read_text(encoding="utf-8").strip())
    assert row2["verdict_basis"] == "UNKNOWN-basis-unavailable", (
        "an unavailable derivation omitted the basis instead of saying so")


def test_13_element4_a_window_LONGER_than_the_corpus_is_REFUSED_loudly(corpus):
    """MUTANT: narrow silently to the available months, or return a short answer -> RED.

    COO's ruling, verbatim in substance: refuse loudly, never silently narrow. A trend over 90
    days computed from 40 days of retained rows is not a degraded trend -- it is a different
    number wearing the label. It RAISES rather than returns so a caller cannot mistake a short
    answer for the answer it asked for.
    """
    corpus(_FIXTURE)   # a single-month fixture
    with pytest.raises(rb.TrendWindowUnsupported) as e:
        rb.assert_window_supported(4)
    msg = str(e.value)
    assert "REFUSED" in msg
    assert "month(s)" in msg and "span" in msg, (
        "the refusal must carry the numbers -- an unactionable denial trains a bypass")
    assert "NOT recoverable" in msg, (
        "the refusal must say the historical window cannot be recovered, or a reader will go "
        "looking for it")


def test_14_element4_positive_control_a_supported_window_is_ACCEPTED(corpus):
    """Run separately from test_13: a guard that refuses everything is not a guard."""
    corpus(_FIXTURE)
    prof = rb.assert_window_supported(1)
    assert prof["rows"] == len(_FIXTURE)
    assert len(prof["months_present"]) >= 1


def test_15_element5_device_scope_is_a_FIELD_on_every_series_not_a_caveat(corpus):
    """MUTANT: drop device_scope, or demote it to prose in a report -> RED.

    The sink is device-local. The scope line is the only thing stopping a reader promoting a
    per-device number to an estate-wide one, and a caveat a reader may drop is not a control.
    """
    corpus(_FIXTURE)
    s = rb.series(rb.BASIS_AS_WRITTEN)
    assert "device_scope" in s, "a series shipped without its device scope"
    assert "PER-DEVICE" in s["device_scope"]
    assert "BLOCKED" in s["device_scope"], (
        "the scope field must record that a cross-device rollup is BLOCKED, not merely absent -- "
        "otherwise the next agent builds one and fabricates coverage")


def test_16_element2_the_trend_path_is_NOT_reachable_around_the_precondition(corpus):
    """MUTANT: expose a trend entry point that skips assert_window_supported -> RED.

    The precondition existed before this element; nothing FORCED a caller through it, and a
    guard nothing invokes is not a guard. trend_claim() refuses BEFORE computing anything.
    """
    corpus(_FIXTURE)
    with pytest.raises(rb.TrendWindowUnsupported):
        rb.trend_claim(4)


def test_17_element2_a_claim_carries_its_provenance_as_NON_OPTIONAL_fields(corpus):
    """MUTANT: make basis/predicate/device_scope optional on the return -> RED.

    A caller must not be able to FORGET the provenance; it is on the return, not on their
    discipline.
    """
    corpus(_FIXTURE)
    c = rb.trend_claim(1)
    for k in ("claim", "basis", "fail_predicate", "device_scope", "corpus_profile", "series"):
        assert k in c, "a trend claim shipped without %s" % k
    assert c["basis"].startswith("derived@v")
    assert "PROVENANCE_NOTE" in c


def test_18_element3_a_stored_series_REFUSES_a_predicate_or_basis_swap(corpus, tmp_path):
    """MUTANT: recompute silently under the requested predicate, or ignore the mismatch -> RED.

    The measured C5 lesson: 221/12.14% vs 224/12.30% differ by exactly the 3 `FAIL->FIXED`
    rows. An unstated predicate makes two CORRECT numbers look like a discrepancy; a silently
    SWAPPED one makes a WRONG number look correct, which is worse.
    """
    corpus(_FIXTURE)
    p = tmp_path / "series.json"
    rb.store_series(p, rb.trend_claim(1))
    # positive control FIRST and separately: the matching predicate must be accepted
    assert rb.load_series(p, expect_predicate=rb.FAIL_PREDICATE)["basis"].startswith("derived@")
    with pytest.raises(rb.PredicateMismatch):
        rb.load_series(p, expect_predicate="result token startswith FAIL")
    with pytest.raises(rb.PredicateMismatch):
        rb.load_series(p, expect_basis="derived@v1+DIFFERENT")


def test_19_element3_a_series_stored_WITHOUT_a_predicate_is_uninterpretable(corpus, tmp_path):
    """MUTANT: default a predicate-less stored series to today's predicate -> RED.

    That default is the silent substitution the whole element guards: it would read old numbers
    as if they answered today's question.
    """
    corpus(_FIXTURE)
    p = tmp_path / "series.json"
    rb.store_series(p, rb.trend_claim(1))
    doc = json.loads(p.read_text(encoding="utf-8"))
    doc.pop("fail_predicate")
    p.write_text(json.dumps(doc), encoding="utf-8")
    with pytest.raises(rb.PredicateMismatch):
        rb.load_series(p)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
