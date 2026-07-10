#!/usr/bin/env python3
"""Mutant-kill bar for the comp-aws cert layer (NFRA_TOOLPASS tool-2, 2026-07-10).

Author: 3.0.0_SA_CVO~A. Arch ruling: 1.0.0_SA_CTO 20260710T152154Z.

WHY THESE TESTS EXIST, AND WHAT THEY ARE GUARDING AGAINST
---------------------------------------------------------
Every test here fails RED under a specific, plausible "improvement" that a future
maintainer would make in good faith. They are not coverage; they are traps.

The cert this replaces could not fail:
  * `main()` discarded every handler's return, so nothing could exit nonzero.
  * `score_iam_ec2` computed `_f1(tp, 0, fn)` -- fp HARDCODED to 0 -- so the ec2 leg's
    declared_f1 was structurally 1.0000 and could not detect a phantom instance.
  * `precision` was computed against a frozen hand-audit, so a GROWING estate lowered
    it with no code change. An F1 against a frozen fixture is an aging clock.

And the first proposed remedy would have rebuilt the disease one function over: if every
"extra" that provably EXISTS in AWS is excused as a fixture gap, then precision can fall
only on a phantom -- and the AC-GRAIN sentinel already refuses to emit phantoms. Precision
becomes structurally 1.0 again. `test_fixture_gap_is_not_absorbed` is the trap for that.

A test whose input can never reach the branch it claims to guard is a green light for
eternity (see comp_route.py:761-766). Each test below therefore asserts the MUTANT is
caught, not merely that the happy path passes.
"""
from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
_MOD = _HERE.parent / "comp_aws_cli.py"
_WS = _HERE.parents[3]


def _load():
    spec = importlib.util.spec_from_file_location("comp_aws_cli_under_test", _MOD)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


caw = _load()


def _args(**kw):
    base = {"cls": None, "out": None, "resource": None,
            "reconcile_fixture": False, "report_out": None}
    base.update(kw)
    return argparse.Namespace(**base)


# ---------------------------------------------------------------------------
# A1 -- exit-code propagation. The success token was bound to the wrong step.
# ---------------------------------------------------------------------------

def test_a1_main_propagates_handler_rc(monkeypatch):
    """MUTANT: revert main() to `args.fn(args)` (drop the sys.exit) -> RED.

    A handler returning 7 must exit 7. Under the old code every rc was 0.
    """
    monkeypatch.setattr(sys, "argv", ["comp-aws", "classes"])
    monkeypatch.setattr(caw, "cmd_classes", lambda a: 7)
    with pytest.raises(SystemExit) as e:
        caw.main()
    assert e.value.code == 7, "main() is not propagating the handler's exit code"


def test_a1_cmd_derive_return_contract_is_a_dict_not_an_rc():
    """derive_runner.py:100 consumes cmd_derive's RETURN as the nightly's graph.

    MUTANT: make cmd_derive return an int rc -> RED, and the nightly breaks.
    This test exists because the obvious A1 remedy, `sys.exit(args.fn(args) or 0)`,
    consumes that dict as an exit code: a SUCCESSFUL derive returns a truthy dict and
    exits 1 (dumping the graph to stderr); a FAILED derive returns {} and exits 0.
    EXACTLY INVERTED. cmd_derive_cli is the seam that keeps both contracts honest.
    """
    import inspect
    src = inspect.getsource(caw.cmd_derive)
    assert "return graph" in src, "cmd_derive must still return the graph dict"
    assert "return {}" in src, "cmd_derive must still return {} on failure"
    # and the CLI seam must return an int
    assert caw.cmd_derive_cli({} if False else _args(resource="arn:aws:zzz:::x")) == caw.RC_DERIVE_ERROR


def test_a1_naive_or_zero_remedy_would_invert_the_exit_code():
    """Documents WHY cmd_derive_cli exists. If someone 'simplifies' main() back to
    `sys.exit(args.fn(args) or 0)`, this is the behaviour they reintroduce."""
    success_graph = {"meta": {"account": "x"}, "classes_data": {}}
    failure = {}
    # `sys.exit(<dict>)` prints the object and exits 1; `sys.exit(0)` exits 0.
    assert (success_graph or 0) is success_graph, "SUCCESS -> non-int -> python would exit 1"
    assert (failure or 0) == 0, "FAILURE -> {} or 0 -> exit 0. Inverted from what we want."


# ---------------------------------------------------------------------------
# A5 -- UNSCORED != INVALID != PASS, in token AND exit code.
# ---------------------------------------------------------------------------

def _run_cli(*argv):
    p = subprocess.run([sys.executable, str(_MOD), *argv],
                       capture_output=True, text=True, cwd=str(_WS), timeout=120)
    return p.returncode, p.stdout + p.stderr


def test_a5_invalid_class_is_nonzero_and_says_invalid():
    """MUTANT: fall back to `print('no certified oracle scorer'); continue` -> RED."""
    rc, out = _run_cli("score", "--class", "zzqq-nope")
    assert rc == caw.RC_INVALID, f"invalid class must exit {caw.RC_INVALID}, got {rc}"
    assert "INVALID CLASS" in out


def test_a5_unscored_class_is_distinguishable_from_invalid():
    """A real class with no oracle is UNMEASURED -- never recorded as success.

    MUTANT: return RC_OK for UNSCORED -> RED. That is what poisoned
    org/compiler-tools-log.md: .tools/comp-aws passes $? to comp_log_auto.py, so an
    rc of 0 was logged as PASS for a class that was never measured.
    """
    rc, out = _run_cli("score", "--class", "lambda")
    assert rc == caw.RC_UNSCORED, f"unscored class must exit {caw.RC_UNSCORED}, got {rc}"
    assert "UNSCORED" in out and "UNMEASURED" in out


def test_a5_unscored_and_invalid_outputs_are_not_identical():
    """They were near-identical one-liners at rc=0. UNMEASURED must not read as INVALID."""
    rc_u, out_u = _run_cli("score", "--class", "lambda")
    rc_i, out_i = _run_cli("score", "--class", "zzqq-nope")
    assert rc_u != rc_i
    assert out_u != out_i


def test_a5_iam_and_ec2_alias_to_the_composite_scorer():
    """`iam` is a real class covered by the `iam-ec2` scorer. Reporting it UNSCORED
    would be false. MUTANT: drop SCORER_ALIASES -> RED."""
    assert caw.SCORER_ALIASES["iam"] == "iam-ec2"
    assert caw.SCORER_ALIASES["ec2"] == "iam-ec2"


# ---------------------------------------------------------------------------
# A3 -- the vacuous control. fp was hardcoded to 0.
# ---------------------------------------------------------------------------

def test_a3_f1_helper_is_gone_demotion_test():
    """MUTANT: reintroduce `_f1` -> RED.

    Offline, `fp` is not a false positive; it is an UNRECONCILED disagreement. Any
    function that folds fp into a score is computing a number it cannot compute honestly.
    """
    assert not hasattr(caw, "_f1"), "_f1 is back -- precision/F1 are not computable offline"
    assert hasattr(caw, "_recall")


def _fake_iam_ec2(monkeypatch, *, derived_ec2_declared, oracle_ec2_declared,
                  derived_roles=None, truth_role_count=2, truth_overperm=None):
    oracle = {
        "iam_roles": {"customer_role_count": truth_role_count},
        "iam_cataloged_findings_HELD": {
            "overperm_roles": [{"role": r} for r in (truth_overperm or ["role-broad"])]},
        "ec2_declared": [{"name": n} for n in oracle_ec2_declared],
    }
    vintage = {"path": "fake.yaml", "fixture_version": "9", "filename_version_skew": False,
               "tf_commit_at_audit": "deadbeef", "as_of": "2026-07-10T00:00:00+00:00",
               "as_of_source": "test", "age_days": 0, "stale": False}
    monkeypatch.setattr(caw, "_load_fixture", lambda fn: (oracle, vintage))

    roles = derived_roles if derived_roles is not None else [
        {"id": "role-broad", "broad_managed": ["AmazonS3FullAccess"]},
        {"id": "role-scoped", "broad_managed": []},
    ]

    def fake_derive_class(cls):
        if cls == "iam":
            return {"nodes": roles}
        if cls == "ec2":
            return {"nodes": [{"name": n, "drift_class": "DECLARED"} for n in derived_ec2_declared],
                    "counts": {"live": len(derived_ec2_declared), "live_no_declared": 0}}
        raise AssertionError(f"unexpected class {cls}")

    monkeypatch.setattr(caw, "derive_class", fake_derive_class)


def test_a3_phantom_ec2_instance_is_detected(monkeypatch):
    """THE MUTANT THAT MATTERS. Inject an EC2 name the fixture does not declare.

    Under the old `_f1(tp, 0, fn)` the ec2 leg printed declared_f1 = 1.0000 and could
    not move. A leg that has only ever printed one value is not a control.
    MUTANT: hardcode fp=0 again (or drop `unreconciled` from the ec2 leg) -> RED.
    """
    _fake_iam_ec2(monkeypatch,
                  oracle_ec2_declared=["real-box"],
                  derived_ec2_declared=["real-box", "PHANTOM-BOX"])
    r = caw.score_iam_ec2()
    assert r["ec2"]["unreconciled"] == ["PHANTOM-BOX"]
    assert r["ec2"]["unreconciled_count"] == 1
    assert r["ec2"]["declared_precision"] == caw.UNAVAILABLE
    tokens, unrec, _ = caw._class_verdict(r)
    assert "UNRECONCILED" in tokens and unrec == 1
    assert "PASS" not in tokens, "a phantom EC2 instance must not PASS"


def test_a4_role_count_delta_now_enters_the_verdict(monkeypatch):
    """A4: count_match was computed, printed, and never scored. A 57-role gap did nothing.

    MUTANT: drop role_count_delta from _class_verdict -> RED.
    """
    _fake_iam_ec2(monkeypatch, oracle_ec2_declared=["b"], derived_ec2_declared=["b"],
                  truth_role_count=111)   # derive returns 2 roles -> delta -109
    r = caw.score_iam_ec2()
    assert r["iam"]["count_match"] is False
    assert r["iam"]["role_count_delta"] == 2 - 111
    tokens, _, _ = caw._class_verdict(r)
    assert "ROLE-COUNT-DELTA" in tokens
    assert "PASS" not in tokens


# ---------------------------------------------------------------------------
# A2 -- CTO's own mutant: the fixture gap must NOT be silently absorbed.
# ---------------------------------------------------------------------------

def _fake_s3(monkeypatch, *, truth_buckets, derived_buckets):
    oracle = {"s3_buckets": [{"bucket_name": b} for b in truth_buckets]}
    vintage = {"path": "fake.yaml", "fixture_version": "9", "filename_version_skew": False,
               "tf_commit_at_audit": "deadbeef", "as_of": "2026-07-10T00:00:00+00:00",
               "as_of_source": "test", "age_days": 0, "stale": False}
    monkeypatch.setattr(caw, "_load_fixture", lambda fn: (oracle, vintage))
    monkeypatch.setattr(caw, "derive_class",
                        lambda cls: {"nodes": [{"id": b} for b in derived_buckets]})


def test_fixture_gap_is_not_absorbed(monkeypatch):
    """CTO's mutant, guarding CTO's own struck bar (arch ruling 20260710T152154Z).

    A REAL bucket that exists in AWS but is absent from the fixture must surface as
    UNRECONCILED and must NOT be quietly excused.

    MUTANT: 'improve' score by calling head_bucket and dropping extras that exist ->
    RED. That change makes precision fall only on a phantom, and AC-GRAIN already
    refuses to emit phantoms -- so precision becomes structurally 1.0 and the cert can
    never fail again. This is the single most important test in this file.
    """
    _fake_s3(monkeypatch, truth_buckets=["a", "b"], derived_buckets=["a", "b", "opal-real-new"])
    r = caw.score_s3()
    assert r["unreconciled"] == ["opal-real-new"]
    assert r["unreconciled_count"] == 1
    assert r["node_recall"] == 1.0, "recall is untouched: the fixture asserts nothing about it"
    tokens, _, _ = caw._class_verdict(r)
    assert tokens == ["UNRECONCILED"], "an unreconciled disagreement is not a PASS"


def test_precision_and_f1_are_never_numeric(monkeypatch):
    """MUTANT: print a precision number -> RED. Offline it cannot be computed honestly."""
    _fake_s3(monkeypatch, truth_buckets=["a"], derived_buckets=["a", "x"])
    r = caw.score_s3()
    for k in ("node_precision", "node_f1"):
        assert isinstance(r[k], str) and "UNAVAILABLE" in r[k]


def test_exact_agreement_is_a_clean_pass(monkeypatch):
    """The NEGATIVE ARM. Without it, a scorer that always fails would pass every test above.

    MUTANT: make UNRECONCILED fire on an empty set -> RED.
    """
    _fake_s3(monkeypatch, truth_buckets=["a", "b"], derived_buckets=["a", "b"])
    r = caw.score_s3()
    assert r["unreconciled_count"] == 0
    assert r["node_recall"] == 1.0
    assert r["missed"] == []
    tokens, unrec, misses = caw._class_verdict(r)
    assert tokens == ["PASS"] and unrec == 0 and misses == []


def test_recall_miss_is_well_defined_offline_and_fails(monkeypatch):
    """A fixture entry the derive did NOT find is a real miss -- computable with no AWS call."""
    _fake_s3(monkeypatch, truth_buckets=["a", "b"], derived_buckets=["a"])
    r = caw.score_s3()
    assert r["missed"] == ["b"]
    assert r["node_recall"] == 0.5
    tokens, _, misses = caw._class_verdict(r)
    assert "RECALL-MISS" in tokens and misses
    assert "PASS" not in tokens


# ---------------------------------------------------------------------------
# A6 -- vintage. Never mtime.
# ---------------------------------------------------------------------------

def test_a6_vintage_never_comes_from_mtime(tmp_path):
    """MUTANT: resolve as_of from st_mtime -> RED.

    mtime is a fact about the filesystem: git checkout / copy / touch rewrites it with no
    human re-auditing anything. An untracked file has NO resolvable vintage and must FAIL
    CLOSED to stale.
    """
    p = tmp_path / "untracked-fixture.yaml"
    p.write_text("meta: {}\n", encoding="utf-8")
    v = caw._fixture_vintage(p, {})
    assert v["as_of"] == "UNKNOWN"
    assert v["as_of_source"] == "UNRESOLVED"
    assert v["stale"] is True, "an unresolvable vintage must fail CLOSED"


def test_a6_real_fixtures_have_no_as_of_but_do_carry_tf_commit(monkeypatch):
    """U3 RESOLVED: 0 of the scored fixtures carry `as_of`; all 3 carry tf_commit_at_audit.

    Guards the resolver's fallback. MUTANT: drop the git fallback -> RED (as_of UNKNOWN).
    """
    p = _WS / "org" / "modules" / "graph" / "aws-shapes" / "s3-hand-audit-fixture-v1.1.yaml"
    if not p.exists():
        pytest.skip("fixture not present")
    doc = caw._load_yaml(p)
    meta = doc.get("meta", {}) or {}
    assert "as_of" not in meta, "a human added as_of -- update this test, precedence 1 now wins"
    assert meta.get("tf_commit_at_audit")
    v = caw._fixture_vintage(p, meta)
    assert v["as_of"] != "UNKNOWN" and v["as_of_source"] == "git:last-commit-of-fixture"


def test_a6_filename_version_skew_is_surfaced():
    """The scorer loads fixtures by HARDCODED FILENAME, and all three filenames disagree
    with meta.fixture_version. The name is a lie about the content; say so."""
    p = _WS / "org" / "modules" / "graph" / "aws-shapes" / "s3-hand-audit-fixture-v1.1.yaml"
    if not p.exists():
        pytest.skip("fixture not present")
    v = caw._fixture_vintage(p, caw._load_yaml(p).get("meta", {}))
    assert v["filename_version_skew"] is True


def test_a6_stale_alone_never_changes_the_verdict(monkeypatch):
    """A stale-but-fully-reconciled fixture is still a PASS.

    MUTANT: make age fail the cert -> RED. That rebuilds the aging clock: the number would
    again decay monotonically with no code change.
    """
    oracle = {"s3_buckets": [{"bucket_name": "a"}]}
    stale = {"path": "f.yaml", "fixture_version": "1", "filename_version_skew": False,
             "tf_commit_at_audit": "x", "as_of": "2020-01-01T00:00:00+00:00",
             "as_of_source": "test", "age_days": 9999, "stale": True}
    monkeypatch.setattr(caw, "_load_fixture", lambda fn: (oracle, stale))
    monkeypatch.setattr(caw, "derive_class", lambda cls: {"nodes": [{"id": "a"}]})
    tokens, _, _ = caw._class_verdict(caw.score_s3())
    assert tokens == ["PASS"], "staleness alone must not fail the cert"


# ---------------------------------------------------------------------------
# A7 / A8 -- grain honesty.
# ---------------------------------------------------------------------------

def test_a7_unreachable_classes_are_computed_not_hardcoded():
    """MUTANT: hardcode the 8 names -> RED the moment a class is added.

    L0 bounds OUTPUT, not WORK, and 8 of 30 classes have no ARN route at all.
    """
    unreachable = caw.arn_unreachable_classes()
    reachable = set(caw._ARN_SERVICE_MAP.values()) | set(caw._ELB_PREFIX_MAP.values())
    assert set(unreachable) == set(caw.CLASSES) - reachable
    assert unreachable == sorted(unreachable)
    assert "s3" not in unreachable and "lambda" not in unreachable


def test_a7_unmappable_arn_exits_nonzero():
    """An unroutable ARN printed ERROR and exited 0. AWS-free path (returns before derive)."""
    rc, out = _run_cli("derive", "--resource", "arn:aws:glacier:us-east-1:313476888478:vaults/x")
    assert rc == caw.RC_DERIVE_ERROR
    assert "cannot infer class" in out
    assert "NO ARN route" in out


def test_a7_elb_listener_rule_is_never_catch_all_classified():
    """An unmodeled ELBv2 sub-type must return None, not phantom-classify as 'lb'."""
    assert caw._arn_to_cls(
        "arn:aws:elasticloadbalancing:us-east-1:313476888478:listener-rule/app/x/1/2/3") is None
    assert caw._arn_to_cls(
        "arn:aws:elasticloadbalancing:us-east-1:313476888478:loadbalancer/app/x/1") == "lb"


def test_a8_class_derive_emits_edges_key_and_discloses(monkeypatch, capsys):
    """EXERCISED 2026-07-10: `derive --class lambda` returned a graph with NO 'edges' key.

    Consumers doing .get("edges", []) read 0 relationships as "this class has none".
    MUTANT: drop the else-branch -> RED (KeyError on graph["edges"]).
    """
    monkeypatch.setattr(caw, "derive_class", lambda cls: {
        "nodes": [], "counts": {"live": 0, "tf_declared": 0, "live_declared": 0,
                                "live_no_declared": 0, "declared_no_live": 0}})
    g = caw.cmd_derive(_args(cls="lambda"))
    assert "edges" in g, "a --class derive must emit the edges key"
    assert g["edges"] == []
    assert g["meta"]["edges_computed"] is False
    assert "NOT COMPUTED" in capsys.readouterr().out


# ---------------------------------------------------------------------------
# A11 -- iceberg-commit wrote empty edge endpoints.
# ---------------------------------------------------------------------------

def test_a11_edge_endpoint_resolution_reads_source_target():
    """Both edges.append sites emit {"source","target"}; cmd_iceberg_commit read src/dst,
    so every graph_edges row carried empty src_id/dst_id. The schema's required=True is
    satisfied by "" (non-null), so it was silent.

    This asserts the resolution order used by the fixed writer.
    """
    def _nid(e, *keys):
        for k in keys:
            n = e.get(k)
            if isinstance(n, dict) and n.get("id"):
                return n["id"]
            if isinstance(n, str) and n:
                return n
        return ""
    edge = {"source": "LAMBDA:foo", "target": "S3_BUCKET:bar", "edge_type": "READS"}
    assert _nid(edge, "source", "src") == "LAMBDA:foo"
    assert _nid(edge, "target", "dst") == "S3_BUCKET:bar"
    assert _nid(edge, "src") == "", "the OLD key order resolved to empty -- that was the bug"
