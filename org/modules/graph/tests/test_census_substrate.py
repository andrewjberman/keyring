#!/usr/bin/env python3
"""census_substrate -- hermetic tests for the 2026-08-05 descriptor extraction.

THE LOAD-BEARING ASSERTIONS, in extraction order:
  1. RE-EXPORT IDENTITY: comp_iam_census's gate names ARE the substrate's objects (not copies)
     -- one gate, one home; a fork here is two gates that will drift.
  2. The PROJECTION shaper builds a stamped census from an injected runner (zero AWS).
  3. A custom-shaper descriptor REFUSES the projection path BY NAME (honesty over uniformity).
  4. The three transport failure classes stay DISTINCT (collapsing them sends a reader hunting
     the wrong cause -- the exact lesson the transport was extracted with).
  5. --query is refused structurally (the per-page pagination trap, banked estate scar).
Hermetic: no AWS, no subprocess -- the runner is injected everywhere.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
_GRAPH = _HERE.parent
sys.path.insert(0, str(_GRAPH))

import census_substrate as cs  # noqa: E402
import comp_iam_census as cic  # noqa: E402


def test_gate_reexport_identity_one_gate_one_home():
    assert cic.census_freshness is cs.census_freshness
    assert cic.parse_generated_utc is cs.parse_generated_utc
    assert cic.FRESH is cs.FRESH and cic.FUTURE is cs.FUTURE
    assert cic.DEFAULT_TTL_HOURS == cs.DEFAULT_TTL_HOURS


def test_projection_shaper_builds_stamped_census_hermetically():
    payload = ('{"Functions": ['
               '{"FunctionName": "f1", "FunctionArn": "arn:aws:lambda:us-east-1:313476888478:function:f1",'
               ' "CodeSha256": "abc", "LastModified": "x", "Runtime": "python3.12",'
               ' "MemorySize": 256, "Timeout": 30, "IGNORED_FIELD": "dropped"}]}')
    snap = cs.build_descriptor_census("aws.lambda", tool="test",
                                      _runner=lambda argv: (0, payload, ""))
    assert snap["summary"]["item_count"] == 1
    assert snap["items"][0]["FunctionName"] == "f1"
    assert "IGNORED_FIELD" not in snap["items"][0], "projection must DROP undeclared fields"
    m = snap["_meta"]
    assert m["account"] == "313476888478", "account derives from the ARN's fixed colon layout"
    assert m["provider"] == "aws" and m["service"] == "lambda"
    verdict, age = cs.census_freshness(snap)
    assert verdict == cs.FRESH, "a just-stamped census must read FRESH through the moved gate"


def test_custom_shaper_refuses_projection_path_by_name():
    with pytest.raises(ValueError) as e:
        cs.build_descriptor_census("aws.iam", tool="test", _runner=lambda argv: (0, "{}", ""))
    assert "custom" in str(e.value) and "aws.iam" in str(e.value)


def test_unknown_descriptor_names_the_known_rows():
    with pytest.raises(KeyError) as e:
        cs.build_descriptor_census("aws.zz-nope", tool="test", _runner=lambda argv: (0, "{}", ""))
    assert "aws.iam" in str(e.value) and "aws.lambda" in str(e.value)


def test_three_transport_failure_classes_stay_distinct():
    with pytest.raises(cs.CliCallFailed):
        cs.run_cli_json(["x"], _runner=lambda argv: (1, "", "denied"))
    with pytest.raises(cs.CliEmptyStdout):
        cs.run_cli_json(["x"], _runner=lambda argv: (0, "   ", ""))
    assert not issubclass(cs.CliCallFailed, cs.CliEmptyStdout)
    assert not issubclass(cs.CliEmptyStdout, cs.CliCallFailed)
    assert issubclass(cs.CliNotFound, RuntimeError), "back-compat: callers catching RuntimeError still work"


def test_query_flag_refused_structurally():
    with pytest.raises(ValueError) as e:
        cs.run_cli_json(["lambda", "list-functions", "--query", "length(Functions)"],
                        _runner=lambda argv: (0, "{}", ""))
    assert "page" in str(e.value).lower()
