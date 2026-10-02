"""MDPF_SECCLASS BD per-ticker first act (CTO rulings batches 139, 145): 16 seed rows, each in its peer's class and sub class.

Run: python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R8_CHECKS/test_seed_bd_first_act_rows.py -q -p no:cacheprovider
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parents[5] / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))
import etf_classification as m  # noqa: E402

_spec = importlib.util.spec_from_file_location("add_rows", str(_HERE / "add_first_act_seed_rows.py"))
A = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(A)


@pytest.mark.parametrize("ticker", sorted(A.ROWS))
def test_row_takes_its_peers_class_and_sub_class(ticker):
    peer = A.ROWS[ticker][0]
    assert m.ETF_CLASSIFICATIONS[ticker] == m.ETF_CLASSIFICATIONS[peer]
    assert m.ETF_SUB_ASSET_CLASS[ticker] == m.ETF_SUB_ASSET_CLASS[peer]
    assert m.ETF_INSTRUMENT_KIND[ticker] == A.ROWS[ticker][2]
    assert m.ETF_NAME_OVERRIDES[ticker] == A.ROWS[ticker][1]


def test_the_ruled_groups():
    for t in ("BMAR", "QMAR", "FMAR", "JANW", "DECZ", "SIXO", "JHQTX"):   # batch 145 B
        assert (m.ETF_CLASSIFICATIONS[t], m.ETF_SUB_ASSET_CLASS[t]) == ("structured", "Hedge")
    assert (m.ETF_CLASSIFICATIONS["QQH"], m.ETF_SUB_ASSET_CLASS["QQH"]) == (m.ETF_CLASSIFICATIONS["QQQ"], m.ETF_SUB_ASSET_CLASS["QQQ"])
    assert (m.ETF_CLASSIFICATIONS["GLDM"], m.ETF_SUB_ASSET_CLASS["GLDM"]) == ("commodities", "Metals")  # CUSIP 98149E303
    assert m.ETF_INSTRUMENT_KIND["SMA"] == "single_security"


def test_not_written_by_ruling():
    for t in ("IBIT", "XCAPX", "NICHX", "AAETX", "FBALX", "VMFXX", "GOFXX"):   # batch 145 C and D, batch 139 cash
        assert t not in m.ETF_CLASSIFICATIONS
