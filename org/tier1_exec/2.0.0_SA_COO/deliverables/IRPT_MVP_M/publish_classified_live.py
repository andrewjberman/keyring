"""Republish a firm's CLASSIFIED Holdings candidate (served revision + the v0.6 members) over its index, under a CTO GO.

Usage (worktree root): python .runtime/holdings-journey-20260923/publish_classified_live.py <firm> <expected_rev> <expected_etag> <expected_index_version> <prior_rev> <go_ref> [check|publish]
The sibling of publish_firm_cas_live.py for prepare_classified_candidate.py's output (prepared_<tag>_classified/). Every
expected value is passed on the command line and re-read at execution; any drift REFUSES with zero writes. `check`
writes nothing. `publish` executes, reads back every returned version, runs the reader matrix on the firm's first two
accounts and their pair plus one refused date, and writes HOLDINGS_<TAG>_CLASSIFIED_PUBLICATION_RECEIPT_20260924.json.
"""
import datetime as dt
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path('lib').resolve()))
sys.path.insert(0, str(Path('data/assets/scripts/gold/investor_reporting').resolve()))
sys.path.insert(0, str(Path('infra/aws/lambda/investor-reporting/holdings').resolve()))
import holdings_snapshot as hs  # noqa: E402
from publication import HoldingsPublication, PublicationRefused, canonical_bytes, digest, _platinum_plan, MAX_JSON_BYTES  # noqa: E402
import boto3  # noqa: E402

firm, EXPECTED_REV, EXPECTED_ETAG, EXPECTED_INDEX_VERSION, PRIOR_REV, GO = sys.argv[1:7]
MODE = sys.argv[7] if len(sys.argv) > 7 else 'check'
tag = {'49financial': '49f', 'inflection': 'inf', 'cottonwood': 'cot'}[firm]
root = Path('.runtime/holdings-journey-20260923/prepared_%s_classified' % tag)
s = json.loads((root / 'candidate_summary.json').read_text())
raw = (root / 'candidate.json').read_bytes()
gold = (root / 'gold.parquet').read_bytes()
receipts = json.loads((root / 'source_receipts.json').read_text())
body = json.loads(raw)
rev = digest(canonical_bytes(body))
BUSINESS_DATE = s['base']['business_date']
plan = _platinum_plan(body, rev) if len(raw) > MAX_JSON_BYTES else None
parts = len(plan[1]) if plan else 0
entry = next((e for e in body['source_set_revision'] if e['source'] == 'irpt-source-objects'), None)
s3 = boto3.client('s3', region_name='us-east-1')
store = HoldingsPublication(s3, firm)
expected = store.begin()
ref = expected.get('reference') or {}
row = (expected.get('document') or {}).get('dates', {}).get(BUSINESS_DATE, {})
src = []
for rr in receipts or []:
    h = s3.head_object(Bucket=rr['bucket'], Key=rr['key'], VersionId=rr['version_id'])
    src.append({'key': rr['key'], 'version_ok': h.get('VersionId') == rr['version_id'],
                'length_ok': h['ContentLength'] == rr['byte_length']})
index_key = store.location('platinum', 'current', 'manifest.json')
recon = hs.reconcile_before_after({**body, '_manifest': {'total_market_value': body['custody_totals']['total_market_value']['value']}})
checks = {
    'go': GO, 'firm': firm, 'candidate_revision': rev,
    'candidate_revision_match': rev == EXPECTED_REV == s['candidate_revision'],
    'gold_sha256_match': digest(gold) == s['gold']['sha256'],
    'receipts_bound_to_body': entry is not None and receipts is not None and digest(canonical_bytes(receipts)) == entry['revision'],
    'receipts_at_pinned_versions': bool(src) and all(x['version_ok'] and x['length_ok'] for x in src), 'receipts_checked': len(src),
    'index_location': index_key, 'index_etag': expected.get('etag'), 'index_version': ref.get('version_id'),
    'index_etag_match': expected.get('etag') == EXPECTED_ETAG, 'index_version_match': ref.get('version_id') == EXPECTED_INDEX_VERSION,
    'index_row_is_prior_revision': row.get('revision') == PRIOR_REV == s['base']['served_revision'],
    'measured_plan': {'multipart': plan is not None, 'parts': parts, 'immutable_creates': (2 + parts + 1) if plan else 3,
                      'index_writes': 1, 'index_precondition': 'IfMatch ' + str(expected.get('etag'))},
    'validate': hs.validate_snapshot(body)[0] is True, 'reconcile': recon[0],
}
hs.assert_bases_not_spliced(body['nodes'])
ok = all(checks[k] for k in ('candidate_revision_match', 'gold_sha256_match', 'receipts_bound_to_body',
                              'receipts_at_pinned_versions', 'index_etag_match', 'index_version_match',
                              'index_row_is_prior_revision', 'validate', 'reconcile'))
checks['preconditions'] = 'PASS' if ok else 'REFUSED'
print(json.dumps(checks, indent=2, default=str), flush=True)
if not ok:
    print('REFUSED: drift against GO ' + GO + '; zero writes executed')
    sys.exit(2)
if MODE != 'publish':
    print('CHECK ONLY: zero writes executed')
    sys.exit(0)

started = dt.datetime.now(dt.timezone.utc).isoformat()
result = store.publish(body, gold, business_date=BUSINESS_DATE, expected=expected,
                       validate=lambda d: hs.validate_snapshot(d)[0], source_objects=receipts)
finished = dt.datetime.now(dt.timezone.utc).isoformat()
assert result['revision'] == EXPECTED_REV
manifest = json.loads(store.read_exact(result['manifest'], expected_location=(result['manifest']['bucket'], result['manifest']['key']),
                                       max_bytes=4 * 1024 * 1024))
writes = [manifest['gold']] + ([manifest['platinum_header']] + [p['object'] for p in manifest['partitions']]
                               if 'partitions' in manifest else [manifest['platinum']]) + [result['manifest']]
for w in writes:
    store.read_exact(w, expected_location=(w['bucket'], w['key']), max_bytes=64 * 1024 * 1024)
index_ref = result['acceptance_receipt']['index']
store.read_exact(index_ref, expected_location=(index_ref['bucket'], index_ref['key']), max_bytes=1024 * 1024)
accounts_all = sorted(n['node_id'] for n in body['nodes'] if n['node_kind'] == 'ACCOUNT')
probe = accounts_all[:2]
matrix = []
for accounts in [{probe[0]}, {probe[1]}, set(probe)]:
    for date in [None, BUSINESS_DATE, '2026-09-23']:
        try:
            loaded, mf = store.load(as_of=date, account_ids=accounts)
            secs = [n for n in loaded['nodes'] if n['node_kind'] == 'SECURITY']
            matrix.append({'accounts': sorted(accounts), 'as_of': date, 'status': 'READ_OK', 'revision': mf['revision'],
                           'nodes': len(loaded['nodes']), 'securities_with_asset_class': sum(1 for n in secs if n.get('asset_class')),
                           'securities': len(secs),
                           'model_leaves_with_code': sum(1 for n in loaded['nodes'] if n['node_kind'] == 'MODEL_LEAF' and n.get('model_code'))})
            assert date != '2026-09-23'
        except PublicationRefused as e:
            assert date == '2026-09-23', str(e)
            matrix.append({'accounts': sorted(accounts), 'as_of': date, 'status': 'EXPECTED_REFUSAL', 'reason': str(e)})
receipt = {'status': 'PUBLISHED_VERIFIED', 'go': GO, 'executed_by': '2.0.0_SA_COO~M', 'started_utc': started, 'finished_utc': finished,
           'firm_id': firm, 'business_date': BUSINESS_DATE, 'revision': result['revision'], 'prior_revision': PRIOR_REV,
           'change': s['change'], 'index_location': index_key, 'index_version': result['index_version'], 'index_sha256': result['index_sha256'],
           'index_precondition': 'IfMatch ' + EXPECTED_ETAG + ' (version ' + EXPECTED_INDEX_VERSION + ')',
           'immutable_write_count': len(writes) - 1, 'index_writes': 1, 'classification_census': s['classification_census'],
           'reader_matrix': matrix, 'reader_matrix_proof_class': 'LIBRARY_UNDER_USER (the function reads under its role)',
           'rollback': 're-point the date row %s to %s under a fresh IfMatch; its objects and index version are retained' % (BUSINESS_DATE, PRIOR_REV)}
out = Path('org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/HOLDINGS_%s_CLASSIFIED_PUBLICATION_RECEIPT_20260924.json' % tag.upper())
out.write_text(json.dumps(receipt, indent=1, default=str) + '\n', encoding='utf-8')
print('PUBLISHED_VERIFIED', result['revision'], 'index', result['index_version'], '->', out)
