"""MDPF_SECCLASS BD re-land (CTO rulings batches 144, 155, 156): the identity read for a blank-ticker position.

Order: the position's own CUSIP row; the exact name through the resolution table; the name's one CUSIP -> its row; that CUSIP's
one ticker (a ticker carrying only that CUSIP) -> its row. Unique at every hop, both ways; every refusal named. classify() is
unchanged (E_25 and the silver builder read it).

Run: python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R8_CHECKS/test_bd_identity_read.py -q -p no:cacheprovider
"""
from __future__ import annotations

import importlib.util
import os
import sys

import pandas as pd
import pytest

_GOLD = os.path.abspath(os.path.join(os.path.dirname(__file__), *(['..'] * 6), 'data', 'black_diamond', 'scripts', 'gold'))
if _GOLD not in sys.path:
    sys.path.insert(0, _GOLD)

from lib.etf_classifier import ETFClassifier, IdentityResolver  # noqa: E402

ROWS = {
    "VUG": {"ticker": "VUG", "asset_class": "equity", "sub_asset_class": "US Large Cap"},
    "IEFA": {"ticker": "IEFA", "asset_class": "equity", "sub_asset_class": "Developed"},
    "GLDM": {"ticker": "GLDM", "asset_class": "commodities", "sub_asset_class": "Metals"},
    "CUSIP:06051X3R1": {"ticker": "CUSIP:06051X3R1", "asset_class": "fixed_income"},
    "CUSIP:46647PAA4": {"ticker": "CUSIP:46647PAA4", "asset_class": "fixed_income"},
}

RESOLUTION = pd.DataFrame({"asset_name_normalized": ["ishares core msci eafe etf", "split name", "split name"],
                           "resolved_ticker": ["IEFA", "AAA", "BBB"]})
LOTS = pd.DataFrame([
    ("VUG", "922908736", "VANGUARD GROWTH ETF"),
    ("", "922908736", "VANGUARD MORNINGSTAR GROWTH ETF"),            # same CUSIP, blank ticker, another name
    ("", "46647PAA4", "JPMORGAN NOTE 2029"),                          # a CUSIP that has its own row
    ("GLDM", "98149E303", "SPDR GOLD MINISHARES TRUST"),
    ("GLDM", "911478105", "US GLOBAL INVESTORS GLD & PREC MTLS"),     # GLDM carries two CUSIPs (row S10)
    ("", "911478105", "GOLD MINERS FUND NO TICKER"),
    ("AAA", "111111111", "TWO TICKER CUSIP"), ("BBB", "111111111", "TWO TICKER CUSIP B"),
    ("", "111111111", "NAME ON TWO TICKER CUSIP"),
    ("", "222222222", "NAME WITH TWO CUSIPS"), ("", "333333333", "NAME WITH TWO CUSIPS"),
    ("ZZZ", "444444444", "NO ROW TICKER"), ("", "444444444", "NAME TO NO ROW TICKER"),
    ("", "555555555", "CUSIP WITH NO TICKER"),
], columns=["ticker", "cusip", "asset_name"])


@pytest.fixture()
def resolver():
    return IdentityResolver.from_frames(RESOLUTION, LOTS)


def _row(k):
    return ROWS.get(k)


@pytest.mark.parametrize("name,cusip,expect", [
    ("whatever", "06051X3R1", ("CUSIP:06051X3R1", "own-cusip-row")),
    ("iShares  Core MSCI EAFE ETF ", None, ("IEFA", "name-resolution-table")),
    ("JPMORGAN NOTE 2029", None, ("CUSIP:46647PAA4", "name-cusip-row")),
    ("VANGUARD MORNINGSTAR GROWTH ETF", None, ("VUG", "name-cusip-ticker")),
])
def test_each_hop_resolves(resolver, name, cusip, expect):
    assert resolver.resolve(name, cusip, _row) == expect


@pytest.mark.parametrize("name,reason", [
    ("GOLD MINERS FUND NO TICKER", "ticker-carries-several-cusips"),   # 911478105 carries GLDM only, but GLDM carries two
    ("NAME ON TWO TICKER CUSIP", "cusip-carries-several-tickers"),
    ("NAME WITH TWO CUSIPS", "name-carries-several-cusips"),
    ("NAME TO NO ROW TICKER", "ticker-has-no-row"),
    ("CUSIP WITH NO TICKER", "cusip-carries-no-ticker"),
    ("NEVER SEEN", "name-not-in-feed"),
    ("", "no-name"),
])
def test_each_refusal_is_named(resolver, name, reason):
    key, hop = resolver.resolve(name, None, _row)
    assert key is None and hop == reason
    assert resolver.refusals()[reason] >= 1


def test_a_ticker_carrying_two_cusips_resolves_nothing():
    # 911478105 carries only GLDM in a feed without the SPDR lot -- still refused while GLDM carries 98149E303 too
    lots = LOTS[~LOTS["asset_name"].isin(["TWO TICKER CUSIP", "TWO TICKER CUSIP B"])]
    r = IdentityResolver.from_frames(RESOLUTION, lots)
    assert r.resolve("GOLD MINERS FUND NO TICKER", None, _row) == (None, "ticker-carries-several-cusips")


def test_an_ambiguous_resolution_table_name_is_not_used(resolver):
    assert "split name" not in resolver.name_to_ticker


class _Client:
    def get_classification(self, k):
        return ROWS.get(k)


def test_classify_is_unchanged_and_classify_with_identity_reads_the_resolved_row(resolver):
    c = ETFClassifier(client=_Client())
    c.set_identity(resolver)
    assert c.classify("", "VANGUARD MORNINGSTAR GROWTH ETF") == ""          # classify() never resolves a name
    assert c.classify_with_identity("", "VANGUARD MORNINGSTAR GROWTH ETF") == ("equity", "US Large Cap", "etf-classifications", "name-cusip-ticker")
    assert c.classify_with_identity("IEFA", "anything") == ("equity", "Developed", "etf-classifications", "ticker")
    assert c.classify_with_identity("ZZZ", "NO ROW TICKER") == ("", "", "unclassified", "ticker-no-row")  # a ticker never falls to names
    assert c.classify_with_identity("", "NEVER SEEN")[2:] == ("unclassified", "name-not-in-feed")


def _load(modname, filename):
    spec = importlib.util.spec_from_file_location(modname, os.path.join(_GOLD, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_c06_d03_d04_take_the_identity_read_for_a_blank_ticker(resolver):
    saved = ETFClassifier._instance
    try:
        ETFClassifier._instance = ETFClassifier(client=_Client())
        ETFClassifier._instance.set_identity(resolver)
        C06 = _load("c06_identity", "C_06.client_mix_timeseries.py")
        D03 = _load("d03_identity", "D_03.composition_artifacts.py")
        D04 = _load("d04_identity", "D_04.client_portal_summary.py")
        t = pd.Series(["", "", "IEFA"])
        n = pd.Series(["VANGUARD MORNINGSTAR GROWTH ETF", "NEVER SEEN", "x"])
        c06 = C06.classify_series(t, n)
        assert list(c06["asset_class"]) == ["equity", "unclassified", "equity"]
        d03 = D03.classify_series(t, pd.Series(["whatever", "NEVER SEEN", "x"]), pd.Series(["06051X3R1", "", ""]))
        assert list(d03["asset_class"]) == ["fixed_income", "unclassified", "equity"]
        assert D04._classify_with_canonical("", "VANGUARD MORNINGSTAR GROWTH ETF", ETFClassifier._instance) == ("equity", "equity", "US Large Cap", "etf-classifications")
    finally:
        ETFClassifier._instance = saved
