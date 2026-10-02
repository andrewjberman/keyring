"""MDPF_SECCLASS (CTO rulings batch 113 item 1): the three seed rows for Cottonwood's name-pattern entries with a ticker.

Each row takes its seed peer's class and sub class: ABNFX as AGG/BND (a core bond fund), LBNYX as HYG (a bond-debenture fund,
mostly below investment grade), NYT as WMT's single-stock form with IJH's US Mid Cap. QACDS (a Chase deposit sweep) gets no
row: cash is the caller's rule (batch 93 item 1).

Run: python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R8_CHECKS/test_seed_cot_name_pattern_rows.py -q -p no:cacheprovider
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_SHARED = Path(__file__).resolve().parents[6] / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"
sys.path.insert(0, str(_SHARED))

import etf_classification as m  # noqa: E402

PEERS = {"ABNFX": "AGG", "LBNYX": "HYG", "NYT": "IJH"}


@pytest.mark.parametrize("ticker,peer", sorted(PEERS.items()))
def test_row_takes_its_peers_class_and_sub_class(ticker, peer):
    assert m.ETF_CLASSIFICATIONS[ticker] == m.ETF_CLASSIFICATIONS[peer]
    assert m.ETF_SUB_ASSET_CLASS[ticker] == m.ETF_SUB_ASSET_CLASS[peer]
    assert m.ETF_SECTOR_MAPPING[ticker] == m.ETF_SECTOR_MAPPING[peer]
    assert m.ETF_NAME_OVERRIDES[ticker]


def test_nyt_is_a_single_stock_in_wmts_form():
    assert m.ETF_INSTRUMENT_KIND["NYT"] == m.ETF_INSTRUMENT_KIND["WMT"] == "single_security"
    assert "NYT" not in m.ETF_MANAGEMENT_STYLE and "WMT" not in m.ETF_MANAGEMENT_STYLE
    assert m.ETF_CLASSIFICATIONS["NYT"] == "equity"


def test_the_two_funds_are_active_funds():
    for t in ("ABNFX", "LBNYX"):
        assert m.ETF_INSTRUMENT_KIND[t] == "fund" and m.ETF_MANAGEMENT_STYLE[t] == "active"


def test_no_cash_seed_row():
    for t in ("QACDS", "FCASH", "FIGXX"):
        assert t not in m.ETF_CLASSIFICATIONS
