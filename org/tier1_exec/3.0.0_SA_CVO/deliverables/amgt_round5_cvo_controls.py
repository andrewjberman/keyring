"""Offline controls for the round-5 adjudication, with all socket connections denied."""
import contextlib
import datetime
import hashlib
import io
import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
OUT = Path(__file__).with_name('AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json')


def deny(*args, **kwargs):
    raise AssertionError('CVO offline audit forbids socket connections')


def main():
    socket.socket.connect = deny
    socket.socket.connect_ex = deny
    socket.create_connection = deny
    import pytest
    spec = importlib.util.spec_from_file_location('cvo_signoff', ROOT / '.tools/prd_signoff_lib.py')
    signoff = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(signoff)
    from lib.research.metrics import chatter_axis as chatter
    from lib.research.price import axis as price
    project = ROOT / 'org/missions/D5/AMGT/AMGT_RESAPP'
    report = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
              'network': 'socket connect/connect_ex/create_connection denied before tests/imports'}
    text = (project / 'prd/AMGT_RESAPP_PRD.md').read_text(encoding='utf-8')
    docs = {p.name: json.loads(p.read_text(encoding='utf-8')) for p in (project / 'prd/signoff').glob('*.json')}
    report['signoff_current'] = signoff.evaluate(text, docs, coo_lane_of_project='2.0.0_SA_COO~ZZZ')
    only_base = {k: v for k, v in docs.items() if '~' not in k}
    report['signoff_without_lane_files'] = signoff.evaluate(text, only_base, coo_lane_of_project='2.0.0_SA_COO~ZZZ')
    changed_text = text + '\nCVO in-memory byte-change control.\n'
    report['signoff_changed_bytes_with_lane_files'] = signoff.evaluate(changed_text, docs, coo_lane_of_project='2.0.0_SA_COO~ZZZ')
    matched_version_docs = json.loads(json.dumps(only_base))
    for doc in matched_version_docs.values():
        doc['prd_version'] = report['signoff_current']['prd_version']
    report['legacy_same_version_changed_bytes_synthetic'] = signoff.evaluate(changed_text, matched_version_docs, coo_lane_of_project='2.0.0_SA_COO~ZZZ')
    report['universes'] = {}
    for slot in [3, 4]:
        path = project / f'deliverables/0.9.0_WK_AMGT_RESAPP~{slot}/universe.json'
        universe = json.loads(path.read_text(encoding='utf-8'))
        values = [r['bloomberg_ticker']['value'] for r in universe['names'] if r.get('bloomberg_ticker', {}).get('status') == 'MEASURED']
        report['universes'][str(slot)] = {'rows': len(universe['names']), 'measured': len(values),
                                        'distinct': len(set(values)), 'aapl_us': values.count('AAPL US'),
                                        'consumer_tickers': len(chatter.read_universe_tickers(str(path)))}
    report['producer_controls'] = {
        'chatter_zero': chatter.normalize_scores({'B': 0, 'A': 0}),
        'chatter_spread': chatter.normalize_scores({'B': 9, 'A': 1}),
        'chatter_top_n': len(chatter.rank_top_n({str(i): float(i) for i in range(20)}, {})),
        'price_rank': price.rank_scores({'LOW': -10.0, 'HIGH': 20.0}),
    }
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
        report['pytest_rc'] = int(pytest.main([
            '-q', '-p', 'no:cacheprovider',
            'lib/research/metrics/tests', 'lib/research/price/tests',
            'lib/research/watchlist/tests',
            'integrations/bloomberg/research/tests/test_price_axis_pull.py']))
    report['pytest_output'] = capture.getvalue()
    paths = ['.tools/prd_signoff_lib.py', 'lib/research/metrics/chatter_axis.py',
             'lib/research/metrics/chatter_gate.py', 'lib/research/watchlist/store.py',
             'lib/research/watchlist/tests/test_watchlist.py', 'lib/research/price/axis.py',
             'integrations/bloomberg/research/price_axis_pull.py']
    report['source_sha256'] = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths}
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')
    print(json.dumps({'evidence': str(OUT), 'pytest_rc': report['pytest_rc'], 'pytest_output': report['pytest_output'],
                      'current_halves': report['signoff_current']['halves'],
                      'base_only_halves': report['signoff_without_lane_files']['halves'],
                      'synthetic_legacy_halves': report['legacy_same_version_changed_bytes_synthetic']['halves'],
                      'universes': report['universes']}, ensure_ascii=True))


if __name__ == '__main__':
    main()
