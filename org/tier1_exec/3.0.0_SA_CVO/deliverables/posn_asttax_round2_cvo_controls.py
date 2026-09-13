"""Read-only CVO source controls; fake registry and AWS, no deployment or data writes."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import types
from unittest.mock import MagicMock

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / 'infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py'
OUT = Path(__file__).with_name('POSN_ASTTAX_ROUND2_CVO_SOURCE_CONTROLS_20260911_Z.json')

def main():
    registry = {
        'SPY': {'asset_class': 'equity', 'management_style': 'passive'},
        'AGG': {'asset_class': 'fixed_income', 'management_style': 'passive'},
        'GLD': {'asset_class': 'Commodities', 'management_style': 'passive'},
        'VXX': {'asset_class': 'Structured', 'management_style': 'overlay'},
    }
    class StubClassifier:
        def get_classification(self, ticker):
            return registry.get(ticker)
    stub = types.ModuleType('etf_classifications_dynamodb')
    stub.ETFClassifier = StubClassifier
    sys.modules['etf_classifications_dynamodb'] = stub
    sys.modules['boto3'] = MagicMock()
    mod = types.ModuleType('cvo_positioning_readonly')
    mod.__file__ = str(SOURCE)
    source = SOURCE.read_bytes()
    exec(compile(source, str(SOURCE), 'exec'), mod.__dict__)
    import pandas as pd
    capture = io.StringIO()
    findings = {}
    with contextlib.redirect_stdout(capture):
        guards = []
        for val in ['unknown', ' UNKNOWN ', '', None, 'active', 'overlay']:
            registry['PROBE'] = {'management_style': val}
            result = mod.classify_management_style('PROBE')
            guards.append({'input': val, 'output': result})
            assert result == ('passive' if val in ['unknown', ' UNKNOWN ', '', None] else val)
        findings['placeholder_controls'] = guards
        holdings = [{'ticker': t, 'weight': .2} for t in ['SPY', 'AGG', 'GLD', 'VXX', 'ABSENT']]
        asset, style = mod.calculate_allocations(holdings)
        assert sum(asset.values()) == 100 and sum(style.values()) == 100
        assert asset['Commodities'] == asset['Structured'] == asset['unclassified'] == 20
        assert style['overlay'] == 20
        findings['allocation_own_key_conservation'] = {'asset': asset, 'style': style}
        served = mod.calculate_aggregated_holdings({'ST': holdings}, {'ST': 1000}, {})
        records = {r['ticker']: r for r in json.loads(json.dumps(served))}
        assert records['SPY']['asset_class'] == 'Equity' and records['SPY']['asset_class_recognized'] is True
        assert records['ABSENT']['asset_class'] == 'Unknown' and records['ABSENT']['asset_class_recognized'] is False
        for ticker in ['GLD', 'VXX']:
            assert records[ticker]['asset_class'] == 'Unknown' and records[ticker]['asset_class_recognized'] is True
        findings['serialized_served_records'] = records
        df = pd.DataFrame([dict(h, model='ST') for h in holdings])
        benchmark = mod.calculate_benchmark_allocations_from_holdings(df)
        assert sum(benchmark['ST'].values()) == 100
        assert benchmark['ST']['Commodities'] == benchmark['ST']['Structured'] == 20
        findings['latest_benchmark_conserves_new_classes'] = benchmark
    findings['stdout'] = capture.getvalue()
    findings['source_sha256'] = hashlib.sha256(source).hexdigest()
    findings['head'] = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    findings['scope'] = 'Actual current generator functions; fake registry, fake AWS. Serialized generated records, not deployed bytes or frontend behavior. Historical S7 3/14/0 is not asserted for current source: S1 subsequently repairs the benchmark hop.'
    OUT.write_text(json.dumps(findings, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in findings.items() if k != 'stdout'}, indent=2))

if __name__ == '__main__':
    main()
