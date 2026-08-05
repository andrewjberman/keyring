"""Tests for script_io_ast -- the R-2 generalist I/O derivation.

TEST POSTURE: this module's whole reason to exist is that a WRONG or SILENT answer about script I/O
is worse than no answer (it feeds a deploy-gate obligation). So the battery is weighted toward the
failure directions rather than the happy path:

  - a fabricated target (worse than unknown, because it is actionable and silently wrong)
  - a clean zero that is actually a parse failure / missing file
  - a dropped call site (silence is the defect -- CLAUDE.md Rule 22a, the comp-iam lesson)

Every fixture is inline source, so the tests do not depend on any repo file staying put.
"""
from __future__ import annotations

import importlib.util
import os
import textwrap

_HERE = os.path.dirname(os.path.abspath(__file__))
_MOD = os.path.join(os.path.dirname(_HERE), "script_io_ast.py")
_spec = importlib.util.spec_from_file_location("script_io_ast", _MOD)
sio = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sio)


def _run(tmp_path, src):
    p = tmp_path / "s.py"
    p.write_text(textwrap.dedent(src), encoding="utf-8")
    return sio.derive_script_io(str(p))


# ---------------------------------------------------------------- resolution correctness

def test_folds_module_constant_into_s3_target(tmp_path):
    r = _run(tmp_path, '''
        B = "opal-data-assets"
        K = "gold/thing.json"
        import boto3
        boto3.client("s3").put_object(Bucket=B, Key=K, Body=b"x")
    ''')
    assert len(r["writes"]) == 1
    assert r["writes"][0]["target"] == "s3://opal-data-assets/gold/thing.json"
    assert r["unresolved"] == []


def test_dynamic_key_marks_the_unknown_part_but_keeps_the_bucket(tmp_path):
    """A partly-known target is real evidence (WHICH bucket/prefix is touched) and must not be
    discarded just because the key is dynamic."""
    r = _run(tmp_path, '''
        B = "opal-data-assets"
        import boto3
        for k in keys:
            boto3.client("s3").get_object(Bucket=B, Key=k)
    ''')
    assert len(r["reads"]) == 1
    assert r["reads"][0]["target"] == "s3://opal-data-assets/{?}"


def test_rebound_constant_is_NOT_folded(tmp_path):
    """THE ANTI-FABRICATION CONTROL. A name assigned twice is ambiguous; folding either value
    would invent a target that is wrong half the time and unmarked as a guess."""
    r = _run(tmp_path, '''
        B = "one"
        B = "two"
        import boto3
        boto3.client("s3").put_object(Bucket=B, Key="k")
    ''')
    # Assert on the TARGET FIELDS, not on a substring of the whole repr: the first version of this
    # test searched str(r) for "one", which matches inside 'None' and failed against correct code.
    # A probe that cannot distinguish the property it is testing is the §15 broken-probe class --
    # recorded here rather than quietly fixed, since this file is a battery about false signals.
    targets = [x["target"] for x in r["writes"] + r["reads"] + r["unresolved"]]
    assert all("one" != t and "two" != t for t in targets)
    assert not any(t.endswith("/one") or t.endswith("/two") for t in targets)
    assert r["writes"][0]["target"] == "s3://{?}/k"


def test_direction_split_read_vs_write(tmp_path):
    r = _run(tmp_path, '''
        import pandas as pd
        pd.read_parquet("in.parquet")
        df.to_parquet("out.parquet")
    ''')
    assert [x["target"] for x in r["reads"]] == ["in.parquet"]
    assert [x["target"] for x in r["writes"]] == ["out.parquet"]


def test_open_mode_decides_direction(tmp_path):
    r = _run(tmp_path, '''
        open("r.txt")
        open("w.txt", "w")
        open("a.txt", mode="a")
    ''')
    assert [x["target"] for x in r["reads"]] == ["r.txt"]
    assert sorted(x["target"] for x in r["writes"]) == ["a.txt", "w.txt"]


# ---------------------------------------------------------------- silence-is-the-defect

def test_unresolved_call_is_REPORTED_not_dropped(tmp_path):
    """The load-bearing invariant: an I/O call whose target is unknowable still appears, with its
    line. Dropping it would produce a clean zero -- the exact false-clean this module replaces."""
    r = _run(tmp_path, '''
        import boto3
        boto3.client("s3").get_object(Bucket=cfg.bucket, Key=cfg.key)
    ''')
    assert r["reads"] == [] and r["writes"] == []
    assert len(r["unresolved"]) == 1
    assert r["unresolved"][0]["direction"] == "READS"
    assert r["unresolved"][0]["line"] == 3
    assert r["sites_scanned"] == 1          # the DENOMINATOR still counts it


def test_denominator_is_always_present(tmp_path):
    r = _run(tmp_path, '''
        import boto3
        boto3.client("s3").put_object(Bucket="b", Key="k")
        open("x.txt")
    ''')
    assert r["sites_scanned"] == 2


def test_syntax_error_is_an_ERROR_not_an_empty_io_set(tmp_path):
    """A broken parse must never be indistinguishable from 'this script has no I/O'."""
    r = _run(tmp_path, "def broken(:\n")
    assert r["error"] and "SyntaxError" in r["error"]
    assert "UNPARSEABLE" in sio.render(r)


def test_missing_file_is_an_ERROR(tmp_path):
    r = sio.derive_script_io(str(tmp_path / "nope.py"))
    assert r["error"] and "FileNotFoundError" in r["error"]


def test_genuine_zero_says_it_is_MEASURED(tmp_path):
    """A true zero is allowed -- but it must announce that it is a zero over a recognizer set,
    not a claim that the script is inert."""
    r = _run(tmp_path, "def add(a, b):\n    return a + b\n")
    assert r["sites_scanned"] == 0 and r["error"] is None
    assert "MEASURED zero" in sio.render(r)


def test_s3_uri_literals_are_surfaced_even_outside_call_sites(tmp_path):
    """Config dicts and constants the call-site scan does not reach are still evidence."""
    r = _run(tmp_path, '''
        CFG = {"src": "s3://opal-data-inf/silver/x.parquet"}
    ''')
    assert [x["uri"] for x in r["s3_literals"]] == ["s3://opal-data-inf/silver/x.parquet"]


def test_dynamodb_table_is_named(tmp_path):
    r = _run(tmp_path, '''
        import boto3
        boto3.client("dynamodb").put_item(TableName="opal-users-v2", Item={})
    ''')
    assert r["writes"][0]["target"] == "dynamodb:opal-users-v2"


def test_render_is_ascii_only(tmp_path):
    """CLAUDE.md Code Quality: no non-ASCII in anything that can reach CloudWatch/CI stdout."""
    r = _run(tmp_path, '''
        B = "b"
        import boto3
        boto3.client("s3").put_object(Bucket=B, Key="k")
        boto3.client("s3").get_object(Bucket=cfg.b, Key=cfg.k)
    ''')
    out = sio.render(r)
    assert out.encode("ascii")          # raises if any non-ASCII slipped in
