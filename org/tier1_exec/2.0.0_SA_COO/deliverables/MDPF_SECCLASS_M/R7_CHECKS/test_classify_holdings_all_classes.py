"""MDPF_SECCLASS row W12-S2: `ETFClassifier.classify_holdings` no longer raises KeyError on a class beyond the four
it seeds. The live table holds alternatives, commodities and structured rows, and a model row can carry any of the
five contract classes; the method summed weights into a dict seeded with fixed_income / equity / hedge / unknown only.

Covers the one client and its two byte-identical copies. Pure: the table lookup is stubbed; no AWS call.
Run from the repo (or worktree) root:
  python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/test_classify_holdings_all_classes.py -q -p no:cacheprovider
"""
from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[6]
_V2 = _ROOT / "infra" / "aws" / "lambda" / "v2_portal"
COPIES = [
    _V2 / "_shared" / "etf_classifications_dynamodb.py",
    _V2 / "yang_pipeline" / "positioning" / "yang-generate-positioning" / "etf_classifications_dynamodb.py",
    _V2 / "yang_pipeline" / "positioning" / "yang-generate-holdings-attribution" / "etf_classifications_dynamodb.py",
]
CLASS_OF = {"AAA": "equity", "BND": "fixed_income", "GLD": "commodities", "VXX": "structured", "ALT": "alternatives",
            "ZZZ": "unknown"}


def _load(path, index):
    spec = importlib.util.spec_from_file_location("etf_client_copy_%d" % index, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(params=range(len(COPIES)), ids=["_shared", "positioning", "holdings-attribution"])
def client(request, monkeypatch):
    mod = _load(COPIES[request.param], request.param)
    monkeypatch.setattr(mod.ETFClassifier, "__init__", lambda self, *a, **k: None)
    monkeypatch.setattr(mod.ETFClassifier, "get_asset_class", lambda self, ticker: CLASS_OF[ticker])
    return mod


def test_every_class_the_table_can_hold_is_summed_and_none_raises(client):
    holdings = [{"ticker": t, "weight": w} for t, w in
                (("AAA", 0.4), ("BND", 0.2), ("GLD", 0.15), ("VXX", 0.1), ("ALT", 0.1), ("ZZZ", 0.05))]
    out = client.ETFClassifier.classify_holdings(holdings)
    assert out["equity"] == pytest.approx(0.4) and out["fixed_income"] == pytest.approx(0.2)
    assert out["commodities"] == pytest.approx(0.15)
    assert out["structured"] == pytest.approx(0.1)
    assert out["alternatives"] == pytest.approx(0.1)
    assert out["unknown"] == pytest.approx(0.05) and out["unknown_tickers"] == ["ZZZ"]
    assert sum(v for k, v in out.items() if k != "unknown_tickers") == pytest.approx(1.0)


def test_the_four_seeded_keys_stay_present_at_zero_for_old_readers(client):
    out = client.ETFClassifier.classify_holdings([{"ticker": "GLD", "weight": 1.0}])
    assert {"fixed_income", "equity", "hedge", "unknown", "unknown_tickers"} <= set(out)
    assert (out["fixed_income"], out["equity"], out["hedge"], out["unknown"]) == (0.0, 0.0, 0.0, 0.0)
    assert out["commodities"] == 1.0


def test_the_three_copies_are_byte_identical():
    digests = {hashlib.md5(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest() for p in COPIES}
    assert len(digests) == 1, digests
