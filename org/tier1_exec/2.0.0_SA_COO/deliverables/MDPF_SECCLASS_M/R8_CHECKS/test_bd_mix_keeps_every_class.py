"""MDPF_SECCLASS, Black Diamond forward fix (CTO rulings batch 99 item 4, batch 117 item 4): no ticker leaves the mix.

The 2026-10-02 04:00Z fire served a 49 Financial firm mix of 1,397.4 M against a 1,843.1 M total: a position classed
commodities, structured, cash or unclassified fell out of the three-class mix while staying in the total. Each check
below fails on that code and passes on the fix:
  - every class C_06 can return is a mix class, and a relationship's mix sums to 100 percent;
  - the period views publish commodities and structured as themselves, with `unclassified` the only residual;
  - D_03's composition has a line for every class held and its lines sum to the total;
  - D_04's firm snapshot carries every class C_06 publishes and sums to the total.

Run: python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R8_CHECKS/test_bd_mix_keeps_every_class.py -q -p no:cacheprovider
Stdlib + pandas + a stub client only; no AWS call is made by this file.
"""
from __future__ import annotations

import importlib.util
import os
import sys

import pandas as pd
import pytest

# this file lives in the seat's folder (R8_CHECKS); the code under test is Black Diamond's gold tree
_GOLD = os.path.abspath(os.path.join(os.path.dirname(__file__), *(['..'] * 6), 'data', 'black_diamond', 'scripts', 'gold'))
if _GOLD not in sys.path:
    sys.path.insert(0, _GOLD)

from lib.etf_classifier import ETFClassifier  # noqa: E402
from lib import mix_views  # noqa: E402


def _load(modname, filename):
    spec = importlib.util.spec_from_file_location(modname, os.path.join(_GOLD, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C_06 = _load('c06_every_class', 'C_06.client_mix_timeseries.py')
D_03 = _load('d03_every_class', 'D_03.composition_artifacts.py')
D_04 = _load('d04_every_class', 'D_04.client_portal_summary.py')


class _StubSharedClient:
    def __init__(self, rows):
        self._rows = dict(rows)

    def get_classification(self, ticker):
        return self._rows.get(ticker)


_ROWS = {
    'IVV':  {'ticker': 'IVV',  'asset_class': 'equity',       'sub_asset_class': 'US Large Cap'},
    'AGG':  {'ticker': 'AGG',  'asset_class': 'fixed_income', 'sub_asset_class': 'Intermediate'},
    'GLD':  {'ticker': 'GLD',  'asset_class': 'commodities',  'sub_asset_class': 'Metals'},
    'VXX':  {'ticker': 'VXX',  'asset_class': 'structured',   'sub_asset_class': 'Hedge'},
    'QAI':  {'ticker': 'QAI',  'asset_class': 'alternatives', 'sub_asset_class': 'Multi-Strategy'},
}

# One relationship's holdings: one of each canonical class, a cash line, and a ticker the table has no row for.
_HOLDINGS = pd.DataFrame({
    'ticker':       ['IVV', 'AGG', 'GLD', 'VXX', 'QAI', 'CASH', 'IYR'],
    'asset_name':   ['ISHARES CORE S&P 500', 'ISHARES CORE US AGG', 'SPDR GOLD SHARES', 'IPATH VIX SHORT-TERM',
                     'IQ HEDGE MULTI-STRAT', 'CASH SWEEP', 'ISHARES US REAL ESTATE'],
    'market_value': [500.0, 200.0, 50.0, 40.0, 30.0, 20.0, 160.0],
})
_TOTAL = float(_HOLDINGS['market_value'].sum())


@pytest.fixture(autouse=True)
def _stub_instance():
    saved = ETFClassifier._instance
    ETFClassifier._instance = ETFClassifier(client=_StubSharedClient(_ROWS))
    yield
    ETFClassifier._instance = saved


def test_c06_every_returned_class_is_a_mix_class_and_the_mix_sums_to_one():
    cls = C_06.classify_series(_HOLDINGS['ticker'], _HOLDINGS['asset_name'])
    returned = set(cls['asset_class'])
    assert returned == {'equity', 'fixed_income', 'commodities', 'structured', 'alternatives', 'cash', 'unclassified'}
    assert returned <= set(C_06.MIX_ASSET_CLASSES), returned - set(C_06.MIX_ASSET_CLASSES)
    # the relationship mix exactly as process_date builds it: class dollars over the total, every mix class
    agg = _HOLDINGS.assign(asset_class=cls['asset_class']).groupby('asset_class')['market_value'].sum()
    mix = {ac: round(float(agg.get(ac, 0.0)) / _TOTAL, 6) for ac in C_06.MIX_ASSET_CLASSES}
    assert abs(sum(mix.values()) - 1.0) < 1e-6
    assert mix['unclassified'] == round(160.0 / _TOTAL, 6)   # IYR stays in the mix as unclassified
    assert mix['structured'] == round(40.0 / _TOTAL, 6)      # VXX
    assert mix['commodities'] == round(50.0 / _TOTAL, 6)     # GLD


def test_period_views_publish_commodities_and_structured_with_unclassified_as_the_only_residual():
    day = {'equity': 500.0, 'fixed_income': 200.0, 'alternatives': 30.0, 'commodities': 50.0, 'structured': 40.0,
           'cash': 20.0, 'unclassified': 160.0, 'other': 0.0, 'total': _TOTAL}
    views = mix_views.compute_period_views({'2026-09-30': day})
    row = views['quarterly'][-1]
    assert row['commodities']['value'] == 50.0 and row['structured']['value'] == 40.0 and row['cash']['value'] == 20.0
    assert row['unclassified']['value'] == 160.0
    assert 'unclassified' in mix_views.MIX_ASSET_CLASSES        # the same eight classes as C_06's daily dict
    published = sum(row[ac]['value'] for ac in mix_views.MIX_ASSET_CLASSES)
    assert abs(published - row['total_aua']) < 0.05


def test_d03_composition_has_a_line_for_every_class_held_and_sums_to_the_total():
    df = _HOLDINGS.copy()
    cls = D_03.classify_series(df['ticker'], df['asset_name'])
    for col in cls.columns:
        df[col] = cls[col]
    comp = D_03._build_composition(df, {'firm_id': '49financial'}, '2026-09-30')
    lines = {m['asset_class']: m['market_value'] for m in comp['mix']}
    assert set(lines) == {'equity', 'fixed_income', 'commodities', 'structured', 'alternatives', 'cash', 'unclassified'}
    assert abs(sum(lines.values()) - comp['total_market_value']) < 0.01
    assert comp['unclassified']['market_value'] == 160.0


def test_d04_firm_snapshot_carries_every_class_c06_publishes(monkeypatch):
    snap = {'equity': 500.0, 'fixed_income': 200.0, 'alternatives': 30.0, 'commodities': 50.0, 'structured': 40.0,
            'cash': 20.0, 'unclassified': 160.0, 'other': 0.0, 'total': _TOTAL}
    reads = {D_04.MIX_DAILY_SUMMARY: {'firm': {'2026-09-30': snap}}, D_04.FIRM_MIX_VIEWS: None,
             D_04.FIRM_COMPOSITION: None}
    monkeypatch.setattr(D_04, '_read_json', lambda key, *a, **k: reads.get(key))
    written = []
    monkeypatch.setattr(D_04, '_write_batch', lambda items, upload, label='': written.extend(items) or len(items))
    D_04.build_firm_mix_summary(upload=False)
    summary = next(data for data, key in written if key == 'platinum/firm/mix_summary.json')
    assert set(summary['mix']) == {k for k in snap if k != 'total'}
    assert abs(sum(v['market_value'] for v in summary['mix'].values()) - _TOTAL) < 1e-6
    assert abs(sum(v['pct'] for v in summary['mix'].values()) - 1.0) < 1e-6
