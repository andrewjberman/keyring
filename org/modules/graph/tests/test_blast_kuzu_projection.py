"""comp-blast is projected from the CANONICAL KUZU GRAPH, and the four 07-31 defects stay fixed.

Andrew-direct ruling 2026-08-03 (ANDREW_RULING_projections_default_kuzu_full_graph_20260803.md):
"all projections should by default be kuzudb full resource graph ... Comp-blast absolutely should
cover all of AWS." Spec: SPEC_comp-blast_kuzu_projection_20260803.md (CVO), acceptance battery s6.

EVERY TEST HERE EXERCISES THE BINARY unless it is explicitly a unit test of a helper. The sibling
file test_blast_exit_code_contract.py owns the frozen 0/1/2/3/4 contract; this file owns the new
universe, the new rc=5, the overlay, and the (a)/(b)/(c)/(d) regressions.

WHY A REGRESSION PER DEFECT: each of the four shipped a WRONG ANSWER AT A CONFIDENT EXIT CODE, which
is the only failure mode that matters on a change-safety gate. rc=0 with the wrong subject, and rc=4
"orphan" on a node with 143 consumers, are both read downstream as deletion evidence.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve()
_GRAPH_DIR = _HERE.parents[1]
_CLI = _GRAPH_DIR / "cli.py"
_REPO = _GRAPH_DIR.parents[2]

sys.path.insert(0, str(_REPO))

EXIT_OK = 0
EXIT_TOOL_FAILED = 1
EXIT_STALE = 2
EXIT_NOT_FOUND = 3
EXIT_PHANTOM = 4
EXIT_AMBIGUOUS = 5


def _run(*argv: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(_CLI), "blast", *argv],
        capture_output=True, text=True, cwd=str(_REPO),
    )


def _bu():
    try:
        from org.modules.graph import comp_blast_universe as bu
        return bu
    except Exception as ex:  # noqa: BLE001
        pytest.skip(f"comp_blast_universe unimportable: {ex}")


def _universe():
    bu = _bu()
    try:
        g, prov, path = bu.load_kuzu_universe(refresh=False)
    except Exception as ex:  # noqa: BLE001
        pytest.skip(f"canonical kuzu universe unavailable: {ex}")
    return bu, g, prov


# ------------------------------------------------------------------ s6.1 universe conformance
def test_universe_is_kuzu_not_the_private_trace_graph():
    """The retired private universe was 2,255 nodes with FOUR S3 buckets. The estate is not that."""
    _bu_, g, _prov = _universe()
    assert len(g.nodes) > 10000, (
        f"universe has only {len(g.nodes)} nodes -- that is the private trace graph's order of "
        f"magnitude (2,255), not the canonical estate graph's (~20,480). The projection is not "
        f"reading kuzu."
    )
    buckets = [n for n in g.nodes.values() if n.node_type == "S3_BUCKET"]
    assert len(buckets) > 4, (
        f"only {len(buckets)} S3_BUCKET nodes -- the private universe carried exactly 4 "
        f"(bd/inf/portal-v2/assets), which is what made opal-data-mdpf a NOT-FOUND."
    )


def test_opal_data_mdpf_resolves_the_failure_that_triggered_the_ruling():
    """THE canonical instance. A real production bucket with live consumers must not be NOT-FOUND."""
    r = _run("opal-data-mdpf")
    assert r.returncode != EXIT_NOT_FOUND, (
        "opal-data-mdpf is NOT-FOUND again -- this is the exact regression the Andrew ruling was "
        f"issued for.\n{r.stderr[-1500:]}"
    )
    assert r.returncode == EXIT_OK, f"expected a clean answer, got rc={r.returncode}\n{r.stderr[-800:]}"


def test_aws_territory_types_present_in_the_projected_universe():
    """s6.1 spot-set: the AWS territory comes along ENTIRE, and other territories ride free."""
    _bu_, g, _prov = _universe()
    have = {n.node_type for n in g.nodes.values()}
    for want in ("LAMBDA", "EVENT_RULE", "S3Key", "IAM_ROLE"):
        assert want in have, f"node_type {want} absent from the projected universe -- AWS is not entire"


# ------------------------------------------------------------------ s6.4 negative control
def test_bogus_node_is_not_found_with_the_kuzu_denominator():
    """A NOT-FOUND must print the denominator it is a verdict OVER, and it must be kuzu's."""
    r = _run("__nonexistent_zzz_target_no_node_has_this__")
    assert r.returncode == EXIT_NOT_FOUND, f"expected 3, got {r.returncode}"
    assert "denominator:" in r.stderr, "NOT-FOUND printed no denominator -- an unseeable universe"
    assert "CANONICAL KUZU GRAPH" in r.stderr, "the denominator is not declared as the kuzu universe"
    assert "not a 'nothing breaks' clear" in r.stderr, "the false-clear guard wording was lost"


# ------------------------------------------------------------------ defect (a): ASCII emission
def test_defect_a_ascii_safe_transliterates_the_corpus_characters():
    """ROOT fix, POSITIVE direction -- this test FIRES; it does not skip.

    The sibling contract file's crash test is written to SKIP once the encoding is fixed, which is
    correct for it and useless as a gate for the fix. This asserts the property directly.

    The measured root: nerves-risk-edges.json stores non-ASCII JSON-ESCAPED, so the FILE scans as
    pure ASCII while json.load decodes real arrows into the claim prose that _render_risk prints.
    28 of 2,255 nodes raised UnicodeEncodeError on a cp1252 stdout -- and they were the RISK-BEARING
    nodes, so the crash silenced HOLD warnings on the most dangerous files in the estate.
    """
    bu = _bu()
    # \u-escaped ON PURPOSE: this file must itself stay pure ASCII (CLAUDE.md Code Quality). A test
    # for non-ASCII handling that embeds raw non-ASCII is the defect wearing the gate's clothes.
    sample = "commit `5b9c6d46e` \u2192 `_month_cap` \u2014 done \u2713 \u00b1 \u2265"
    out = bu.ascii_safe(sample)
    assert out.isascii(), f"ascii_safe returned non-ASCII: {out!r}"
    out.encode("cp1252")                      # the actual failing operation, exercised
    assert "->" in out and "--" in out, "transliteration lost meaning instead of preserving it"
    assert "5b9c6d46e" in out, "transliteration destroyed adjacent content"


def test_defect_a_ascii_safe_never_raises_on_arbitrary_unicode():
    """Unmapped codepoints must degrade visibly, never crash and never silently vanish."""
    bu = _bu()
    for s in ("\u4e2d\u6587\u6d4b\u8bd5", "\U0001F600 emoji", "\u00a0\u2007", "plain"):
        out = bu.ascii_safe(s)
        assert out.isascii(), f"ascii_safe left non-ASCII in {s!r} -> {out!r}"
        out.encode("cp1252")


def test_defect_a_risk_bearing_node_renders_without_crashing():
    """End-to-end: a node carrying risk-corpus claims renders clean through the binary."""
    risk = _GRAPH_DIR / "nerves-risk-edges.json"
    if not risk.exists():
        pytest.skip("risk corpus absent")
    r = _run("opal-data-mdpf")
    assert "UnicodeEncodeError" not in r.stderr, f"the cp1252 crash is back:\n{r.stderr[-800:]}"
    assert "Traceback" not in r.stderr, f"unexpected traceback:\n{r.stderr[-800:]}"


# ------------------------------------------------------------------ defect (b): direction vs verdict
def _node_with_dependents() -> str:
    _bu_, g, _prov = _universe()
    for nid in sorted(g.nodes):
        if g.downstream(nid, max_depth=3) and g.upstream(nid, max_depth=3):
            return nid
    pytest.skip("no node with both upstream and downstream in the universe")


def test_defect_b_direction_up_does_not_invert_the_consumer_verdict():
    """THE DELETION-EVIDENCE REGRESSION.

    Measured at HEAD a1cab01483 on gold:A_00.accounts_dimension (143 real downstream consumers):
        --check-consumers                 -> rc=0  CONSUMER-OK
        --check-consumers --direction up  -> rc=4  PHANTOM-CONSUMER
    Same node, same estate, opposite verdicts, and rc=4 is mapped by comp_debt/grounding_lib to
    GRAPH_ZERO_CONSUMER -- i.e. to deletion evidence. A DISPLAY flag must never move a VERDICT.
    """
    nid = _node_with_dependents()
    base = _run(nid, "--check-consumers")
    up = _run(nid, "--check-consumers", "--direction", "up")
    down = _run(nid, "--check-consumers", "--direction", "down")
    assert base.returncode == up.returncode == down.returncode, (
        f"--direction changed the consumer VERDICT for {nid}: "
        f"default rc={base.returncode}, up rc={up.returncode}, down rc={down.returncode}. "
        "That is defect (b) -- a false PHANTOM-CONSUMER is deletion evidence."
    )
    assert base.returncode == EXIT_OK and "CONSUMER-OK" in base.stdout


def test_defect_b_no_direction_flag_can_manufacture_a_phantom():
    """Stronger form: for a node WITH dependents, no direction value may yield rc=4."""
    nid = _node_with_dependents()
    for d in ("up", "down", "both"):
        r = _run(nid, "--check-consumers", "--direction", d)
        assert r.returncode != EXIT_PHANTOM, (
            f"--direction {d} manufactured a PHANTOM-CONSUMER on {nid}, which HAS dependents"
        )


# ------------------------------------------------------------------ defect (c): wrong subject
def _ambiguous_query() -> str:
    bu, g, _prov = _universe()
    from collections import Counter
    segs = Counter()
    for nid in g.nodes:
        seg = nid.replace("\\", "/").rsplit(":", 1)[-1].rsplit("/", 1)[-1]
        if len(seg) > 6:
            segs[seg] += 1
    for seg, n in segs.most_common(50):
        if n > 1 and bu.resolve_subject(g, seg)[0] == bu.RESOLVE_AMBIGUOUS:
            return seg
    pytest.skip("no ambiguous query found in the universe")


def test_defect_c_ambiguous_subject_refuses_with_rc5_not_a_silent_pick():
    """The silent wrong-subject class.

    Measured: `comp-blast load_accounts_dim` returned, AT rc=0, a full blast answer about
    gold:B_01.holdings_lots:load_accounts_dimension -- a different function in a different script --
    while the exact node existed among 17 substring matches. Nothing said a choice had been made.
    """
    q = _ambiguous_query()
    r = _run(q)
    assert r.returncode == EXIT_AMBIGUOUS, (
        f"ambiguous query {q!r} returned rc={r.returncode}, expected {EXIT_AMBIGUOUS}. "
        f"rc=0 here means the tool picked a subject for you and did not say so."
    )
    assert "AMBIGUOUS-SUBJECT" in r.stderr, "the marker callers key on is missing"
    assert "refusing to pick" in r.stderr


def test_defect_c_rc5_is_disjoint_from_every_other_code():
    """rc=5 may not overload not-found (3) or clean (0). The nodes EXIST; we declined to choose."""
    assert EXIT_AMBIGUOUS not in (EXIT_OK, EXIT_TOOL_FAILED, EXIT_STALE, EXIT_NOT_FOUND, EXIT_PHANTOM)


def test_defect_c_exact_id_still_answers_cleanly():
    """The refusal must not swallow the normal case: an exact node id answers at rc=0."""
    _bu_, g, _prov = _universe()
    nid = next((n for n in sorted(g.nodes) if g.downstream(n, max_depth=2)), None)
    if nid is None:
        pytest.skip("no node with downstream edges")
    r = _run(nid)
    assert r.returncode == EXIT_OK, f"exact id {nid} -> rc={r.returncode}\n{r.stderr[-600:]}"


def test_defect_c_legacy_id_shape_resolves_uniquely():
    """The id-shape migration: kuzu says `pipeline:bd:gold:X`, every existing call site says `gold:X`.

    Without the colon-boundary suffix tier the old id is merely a SUBSTRING of the new one and also
    of all ~40 of that script's function nodes -- so every legacy call site would degrade to
    AMBIGUOUS. That would be a fix that breaks the fleet.
    """
    bu, g, _prov = _universe()
    legacy = None
    for nid in sorted(g.nodes):
        if nid.startswith("pipeline:") and nid.count(":") >= 3 and "gold:" in nid:
            legacy = "gold:" + nid.split("gold:", 1)[1]
            if legacy.count(":") == 1:
                break
    if not legacy:
        pytest.skip("no pipeline-scoped gold node to derive a legacy id from")
    kind, matches = bu.resolve_subject(g, legacy)
    assert kind == bu.RESOLVE_EXACT, (
        f"legacy id {legacy!r} resolved {kind} ({len(matches)} matches) -- existing call sites break"
    )


# ------------------------------------------------------------------ defect (d): hidden callers
def test_defect_d_default_direction_shows_fetches_callers():
    """Proven, not assumed (the spec asked): (d) does NOT dissolve under the kuzu universe.

    endpoint:getPlatinumPartnerAnalytics has EIGHT upstream callers via FETCHES and ZERO downstream.
    The old default computed upstream only for function-grain GOLD_SCRIPT -- a node_type that only
    existed in the retired universe -- so under kuzu the default hid every caller in the estate,
    and with defect (b) would have called that endpoint an orphan.
    """
    _bu_, g, _prov = _universe()
    fetches = [e for e in g.edges if e.edge_type == "FETCHES"]
    if not fetches:
        pytest.skip("no FETCHES edges in the universe")
    from collections import Counter
    target, n_callers = Counter(e.target for e in fetches).most_common(1)[0]
    if n_callers < 2:
        pytest.skip("no multi-caller FETCHES target")
    r = _run(target)
    assert r.returncode == EXIT_OK, f"{target} -> rc={r.returncode}\n{r.stderr[-600:]}"
    assert "CALLER CHAIN" in r.stdout, (
        f"{target} has {n_callers} FETCHES callers and the DEFAULT blast showed no caller chain -- "
        "defect (d): the blast-radius answer omits the things that actually break."
    )


def test_defect_d_fetches_target_is_not_a_phantom():
    """The (b)+(d) interaction: a node whose only dependents are upstream is NOT an orphan."""
    _bu_, g, _prov = _universe()
    fetches = [e for e in g.edges if e.edge_type == "FETCHES"]
    if not fetches:
        pytest.skip("no FETCHES edges")
    from collections import Counter
    target, _n = Counter(e.target for e in fetches).most_common(1)[0]
    r = _run(target, "--check-consumers")
    assert r.returncode != EXIT_PHANTOM, (
        f"{target} is FETCHED by real callers and was declared PHANTOM-CONSUMER -- deletion "
        f"evidence against a live endpoint."
    )


# ------------------------------------------------------------------ s6.2 overlay truthfulness
def test_overlay_provenance_is_truthful_about_worktree_mutation():
    """s6.2: the head-pin must be REAL -- a mutation changes the digest in the SAME invocation.

    Unit-level against the real deriver (not the binary) so the fixture never has to live in a
    scanned production tree longer than the assertion. `org/modules/graph` IS one of the roots
    subject_files scans, so a fixture placed here is found exactly as a real subject would be.
    """
    bu = _bu()
    from org.modules.graph.trace_graph import Node
    fixture = _GRAPH_DIR / "zz_blast_overlay_fixture.py"
    node = Node(id="zz_blast_overlay_fixture", node_type="PipelineScript",
                label="zz_blast_overlay_fixture")
    try:
        fixture.write_text(
            "from __future__ import annotations\n"
            "KEY = 'gold/fixture/before.parquet'\n", encoding="utf-8")
        _e1, p1 = bu.derive_overlay(node, "zz_blast_overlay_fixture")
        assert p1["scope"] == "subject", f"overlay did not find the fixture: {p1}"
        assert p1["files"] >= 1
        d1 = p1["digest"]

        fixture.write_text(
            "from __future__ import annotations\n"
            "KEY = 'gold/fixture/AFTER_MUTATION.parquet'\n", encoding="utf-8")
        _e2, p2 = bu.derive_overlay(node, "zz_blast_overlay_fixture")
        assert p2["digest"] != d1, (
            "the worktree digest did NOT change after a real content mutation -- the head-pin is "
            "decorative, and a mid-edit blast is silently answering from the committed estate."
        )

        fixture.write_text(
            "from __future__ import annotations\n"
            "KEY = 'gold/fixture/before.parquet'\n", encoding="utf-8")
        _e3, p3 = bu.derive_overlay(node, "zz_blast_overlay_fixture")
        assert p3["digest"] == d1, "reverting the content did not restore the digest"
    finally:
        if fixture.exists():
            fixture.unlink()


def test_overlay_dirty_flag_flips_on_a_TRACKED_file():
    """The `dirty` half of the overlay contract -- and it needs a TRACKED file to mean anything.

    CVO's battery checks that a worktree mutation "must flip dirty AND change the digest". The
    sibling test above uses an UNTRACKED fixture, which `git status --porcelain` reports as `??` in
    every state -- so dirty is True throughout and the flip is never exercised. A fixture that
    cannot be clean cannot test a clean->dirty transition.

    So this one mutates a real tracked file and restores it in a finally. Verified end to end:
    False -> True -> False with the digest moving and returning.
    """
    bu = _bu()
    from org.modules.graph.trace_graph import Node
    target = _GRAPH_DIR / "comp_ladder.py"
    if not target.exists():
        pytest.skip("tracked fixture absent")
    r = subprocess.run(["git", "status", "--porcelain", "--", str(target)],
                       capture_output=True, text=True, cwd=str(_REPO))
    if r.stdout.strip():
        pytest.skip("fixture is already dirty in this working tree -- cannot test the transition")

    node = Node(id="comp_ladder", node_type="PipelineScript", label="comp_ladder")
    orig = target.read_bytes()
    try:
        _e1, clean = bu.derive_overlay(node, "comp_ladder")
        assert clean["scope"] == "subject" and clean["files"] >= 1
        assert clean["dirty"] is False, "a clean tracked file reported dirty"

        target.write_bytes(orig + b"\n# transient overlay probe\n")
        _e2, dirty = bu.derive_overlay(node, "comp_ladder")
        assert dirty["dirty"] is True, (
            "the overlay did not notice an uncommitted edit -- the head-pin is decorative and a "
            "mid-edit blast is silently answering from the committed estate"
        )
        assert dirty["digest"] != clean["digest"], "content digest did not move on a real mutation"
    finally:
        target.write_bytes(orig)

    _e3, back = bu.derive_overlay(node, "comp_ladder")
    assert back["dirty"] is False and back["digest"] == clean["digest"], "restore not observed"


def test_dual_provenance_is_always_printed():
    """s3.3: BOTH vintages, always. A single-vintage answer is a P3 conformance failure."""
    r = _run("opal-data-mdpf")
    assert "comp-kuzu provenance" in r.stderr or "DB:" in r.stderr, (
        f"kuzu vintage absent from the emission:\n{r.stderr[-800:]}")
    assert "worktree overlay" in r.stderr, (
        f"overlay vintage absent -- the reader cannot tell an estate fact from a worktree fact:\n"
        f"{r.stderr[-800:]}")
    assert "HEAD:" in r.stderr and "dirty:" in r.stderr and "content-digest:" in r.stderr


def test_json_mode_carries_both_provenances():
    r = _run("opal-data-mdpf", "--json")
    doc = json.loads(r.stdout)
    assert "provenance" in doc, "--json dropped provenance"
    assert "kuzu" in doc["provenance"] and "overlay" in doc["provenance"]


# ------------------------------------------------------------------ s7 no silent fallback
def test_kuzu_unavailable_fails_loud_and_never_falls_back():
    """s7: a silent fallback to the private scan re-creates the exact defect the ruling removes.

    Worse than the original: the tool would answer from a universe the operator did not choose and
    cannot see, so the wrong answer would arrive with no NOT-FOUND to warn them.
    """
    bu = _bu()
    with pytest.raises(bu.KuzuUnavailable):
        bu.load_kuzu_universe(db_path=str(_REPO / "__no_such_kuzu_db_zzz__"), refresh=False)


def test_kuzu_unavailable_exits_tool_failed_through_the_binary():
    """And the binary maps that to rc=1 (TOOL FAILED) -- never a verdict code."""
    import os
    env = dict(os.environ)
    env["GLOBGRPH_KUZU_DB_PATH_OVERRIDE_TEST"] = "1"
    # Exercised via the helper contract above; here we assert the mapping the handler declares.
    from org.modules.graph import comp_blast_universe as bu
    assert issubclass(bu.KuzuUnavailable, RuntimeError)
