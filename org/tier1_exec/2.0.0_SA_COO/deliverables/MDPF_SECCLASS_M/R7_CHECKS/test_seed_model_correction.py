"""MDPF_SECCLASS row W12-S1: a seed correction of a model row drops the two model-only attributes.

org/standards/MDPF_SECCLASS_CONTRACT.json: `classification_confidence` and `low_confidence` are present ONLY on a
row a model classified, and "a later seed correction of a model row replaces classified_by = seed and drops
low_confidence entirely, same as classification_confidence". Before this fix `merge_item` carried both onto the
seed row through its carry-forward loop.

Pure: no table read, no AWS call.
It lives beside the round's other checks because the seat's grant covers the script, not the shared tests folder.
Run from the repo (or worktree) root:
  python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/test_seed_model_correction.py -q -p no:cacheprovider
"""
from __future__ import annotations

import importlib.util
import json
import sys
from decimal import Decimal
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[6]  # .../org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS
_SHARED = _ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"
_YANG = _SHARED.parent / "yang_pipeline"
_CONTRACT = _ROOT / "org" / "standards" / "MDPF_SECCLASS_CONTRACT.json"

sys.path.insert(0, str(_SHARED))
import etf_classification as ec  # noqa: E402


@pytest.fixture(scope="module")
def seed():
    spec = importlib.util.spec_from_file_location("seed_etf_classifications",
                                                  str(_YANG / "seed-etf-classifications.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def ticker():
    return sorted(ec.ETF_CLASSIFICATIONS)[0]


def _model_row(ticker):
    return {"ticker": ticker, "asset_class": ec.ETF_CLASSIFICATIONS[ticker], "classified_by": "model",
            "classification_confidence": Decimal("0.62"), "low_confidence": True,
            "curator_note": "kept by a person"}


def test_a_seed_correction_of_a_model_row_drops_both_model_only_attributes(seed, ticker):
    item, _preserved, _conflicts = seed.merge_item(ticker, _model_row(ticker), "2026-10-01T00:00:00Z")
    assert item["classified_by"] == "seed"
    assert "classification_confidence" not in item
    assert "low_confidence" not in item


def test_the_drop_is_narrow_a_curators_attribute_is_still_carried(seed, ticker):
    item, preserved, _conflicts = seed.merge_item(ticker, _model_row(ticker), "2026-10-01T00:00:00Z")
    assert item["curator_note"] == "kept by a person"
    assert "curator_note" in preserved
    assert not set(seed.MODEL_ONLY_FIELDS) & set(preserved)


def test_a_row_with_no_model_attributes_merges_as_before(seed, ticker):
    row = {"ticker": ticker, "asset_class": ec.ETF_CLASSIFICATIONS[ticker], "classified_by": "legacy",
           "curator_note": "kept by a person"}
    item, _preserved, _conflicts = seed.merge_item(ticker, row, "2026-10-01T00:00:00Z")
    assert item["classified_by"] == "seed" and item["curator_note"] == "kept by a person"


def test_the_two_names_are_the_contracts_own_fields(seed):
    with open(_CONTRACT, encoding="utf-8") as fh:
        fields = json.load(fh)["fields"]
    assert set(seed.MODEL_ONLY_FIELDS) <= set(fields)
    assert set(seed.MODEL_ONLY_FIELDS) == {"classification_confidence", "low_confidence"}
