"""Bounded offline re-1 review. Does not edit originals, invoke AWS or move portal."""
import collections
import contextlib
import datetime
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import socket
import subprocess
import sys
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
sys.path.insert(0, str(ROOT))
PROJECT = 'org/missions/D5/AMGT/AMGT_RESAPP'
WORKER = PROJECT + '/deliverables/0.9.0_WK_AMGT_RESAPP~10/'
PORTAL_PIN = 'c67281460a2651430798c9a4c3e68233d81a6e96'


def run(args):
    p = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return {'args': args, 'rc': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}


def main():
    spec = importlib.util.spec_from_file_location('surprise_gate', ROOT / '.tools/surprise-row-gate.py')
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    evidence = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'head': run(['git', 'rev-parse', 'HEAD']),
                'orders': {p: gate._open_tos_for_project(str(ROOT), p)
                           for p in ['AMGT_RESAPP', 'POSN_ASTTAX', 'ZZZZ_NOSUCH']},
                'dispositions_before': gate._latest_dispositions(str(ROOT), 'AMGT_RESAPP'),
                'limits': 'Offline source and controlled function reads only. No AWS, deployed authentication, browser layout, live Print, task-order mutation, portal checkout or promote.'}
    proof_path = WORKER + 'AMGT_RESAPP.TO-AMGT-re-1.lead-panel-recut.proof_of_spec.json'
    evidence['proof_path'] = proof_path
    evidence['proof_commit'] = run(['git', 'log', '-1', '--format=%H', '--', proof_path])
    evidence['proof_structure'] = run([sys.executable, '.tools/proof-of-spec-check.py', proof_path, 'AC1,AC2,AC3,AC4,AC5,AC6'])
    evidence['portal_object'] = run(['git', '-C', 'portal', 'cat-file', '-t', PORTAL_PIN])
    evidence['portal_object_negative'] = run(['git', '-C', 'portal', 'cat-file', '-t', '0000000000000000000000000000000000000000'])
    evidence['portal_state'] = run(['git', 'ls-tree', 'HEAD', 'portal'])
    proof = json.loads((ROOT / proof_path).read_text(encoding='utf-8'))
    evidence['instrument_correction'] = 'First audit attempt stopped before tests on wrong CVO key artifacts; corrected to actual artifacts_produced. No criterion result was inferred from that failed attempt.'
    evidence['worker_artifacts'] = proof['artifacts_produced']
    with patch.object(socket.socket, 'connect', side_effect=RuntimeError('CVO offline socket guard')), patch.object(socket, 'create_connection', side_effect=RuntimeError('CVO offline socket guard')):
        import pytest
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
            rc = pytest.main(['lib/research/api/tests/test_scoped_amgt.py', '-q', '-p', 'no:cacheprovider'])
        evidence['adapter_tests'] = {'rc': int(rc), 'output': capture.getvalue(), 'socket_guard': 'connect and create_connection denied for the full suite'}
        from lib.research.api import scoped_amgt as api
        from lib.research.api.tests.test_scoped_amgt import FakeResource
        evidence['cross_resolutions'] = [api.resolve_axis(m, s) for m in api.MOVEMENTS for s in api.SUBJECTS]
        row = {'axis_date': 'CHATTER#2026-09-11', 'ticker': 'BABA US', 'rank': 1, 'rank_sort': '00001', 'score': 82, 'as_of_date': '2026-09-11'}
        good = FakeResource([row])
        with patch.object(api, '_dynamodb', return_value=good):
            evidence['series_processed_control'] = api.read_rank_series('trending', 'chatter', ['BABA US'], as_of_date='2026-09-11', days=1)
        class DeferredResource:
            def __init__(self):
                self.calls = 0
            def batch_get_item(self, RequestItems):
                self.calls += 1
                return {'Responses': {}, 'UnprocessedKeys': RequestItems}
        deferred = DeferredResource()
        with patch.object(api, '_dynamodb', return_value=deferred):
            evidence['series_unprocessed_control'] = api.read_rank_series('trending', 'chatter', ['BABA US'], as_of_date='2026-09-11', days=1)
        evidence['series_unprocessed_call_count'] = deferred.calls
        raw = api.read_model_block('BABA_US_Equity')
        evidence['model_scopes'] = dict(collections.Counter(f.get('scope') for f in raw.get('figures', [])))
        evidence['thesis_response'] = api.read_thesis_bundle('BABA_US_Equity')
        from lib.research.print.render_pack import load_model_block
        corrected = load_model_block('BABA_US_Equity')
        evidence['raw_fiscal_prices'] = [f for f in raw.get('figures', []) if f.get('mnemonic') == 'PX_LAST' and f.get('scope') != 'header']
        evidence['consumer_fiscal_prices'] = [f for f in corrected.get('figures', []) if f.get('mnemonic') == 'PX_LAST' and f.get('scope') != 'header']
    evidence['instrument_correction'] += ' First successful audit used field instead of mnemonic for the price-only diagnostic; empty lists were not proof of absent price rows. This rerun corrects that diagnostic.'
    sources = ['lib/research/api/scoped_amgt.py', 'lib/research/api/tests/test_scoped_amgt.py',
               'infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf']
    evidence['source_sha256'] = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in sources}
    evidence['source_matches_worker_pin'] = {}
    for p in sources[:2]:
        blob = subprocess.check_output(['git', 'show', 'e83bdbe7c1fd076f94e87ba6749836bd0eca5cf6:' + p], cwd=ROOT)
        evidence['source_matches_worker_pin'][p] = blob.replace(b'\r\n', b'\n') == (ROOT / p).read_bytes().replace(b'\r\n', b'\n')
    portal_files = run(['git', '-C', 'portal', 'ls-tree', '-r', '--name-only', PORTAL_PIN, 'src/pages/SecurityAnalysis', 'src/api/endpoints/amgt-lead-panel.ts'])['stdout'].splitlines()
    unicode_files = {}
    for p in portal_files:
        text = subprocess.check_output(['git', '-C', 'portal', 'show', PORTAL_PIN + ':' + p], cwd=ROOT).decode('utf-8')
        chars = [{'line': n, 'codepoints': [f'U+{ord(c):04X}' for c in line if ord(c) > 127]} for n, line in enumerate(text.splitlines(), 1) if any(ord(c) > 127 for c in line)]
        if chars:
            unicode_files[p] = chars
    evidence['portal_unicode'] = {'files_scanned': len(portal_files), 'affected_files': unicode_files}
    evidence['worker_render_report'] = json.loads((ROOT / WORKER / 'rendercheck_report.json').read_text(encoding='utf-8'))
    evidence['iam_recheck'] = {'commands': ['comp-iam service scoped_amgt', 'comp-iam service amgt-resapp'],
      'observed': 'No scoped_amgt match in 188 services and 212 roles; amgt-resapp role view still lists old opal-amgt-articles Query ARNs. This is a mapping miss for the new adapter, not a green IAM verdict. No applied-plane simulation or deployed route measurement.'}
    evidence['head_end'] = run(['git', 'rev-parse', 'HEAD'])
    out = HOME / 'AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json'
    out.write_text(json.dumps(evidence, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')
    print(json.dumps({'path': str(out), 'tests': evidence['adapter_tests'], 'model_scopes': evidence['model_scopes'], 'thesis_keys': list(evidence['thesis_response']),
                      'fiscal_count': len(evidence['thesis_response'].get('fiscal_year_figures', [])),
                      'price_counts': [len(evidence['raw_fiscal_prices']), len(evidence['consumer_fiscal_prices'])],
                      'open_orders': evidence['orders']['AMGT_RESAPP'],
                      'unresolved': [k for k, v in evidence['dispositions_before'][0].items() if v == 'UNDER_INVESTIGATION']}))


if __name__ == '__main__':
    main()
