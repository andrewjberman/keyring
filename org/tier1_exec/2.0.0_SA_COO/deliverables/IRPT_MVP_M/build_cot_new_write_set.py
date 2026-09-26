"""Build the bd-securities write set for the COT-new classification plus the re-cut batch B, under Andrew's rules of
2026-09-26 ~02:3xZ (ANDREW_DIRECT_20260926_023xZ_ESTABLISHED_EQUITIES_STAY_AND_OTHER_IS_PERSONAL_ONLY.md @c3dde578b9).
No write: it reads the table, the ONE run's results and COT's 2026-09-22 holdings, and prints the per-client delta.

Rules, in order, per key:
  R2a  `other` only for a personal or held-away asset: an "Investor Manual Asset - ..." row, or one of the held-away
       accounts ~M decided on its REC under the self-drive arm (@ce6aa15a17): Voya, Gilder Gagnon Howe, Leader Bank
       IRA. A personal asset the model placed elsewhere is set to `other`.
  R2b  A security the model called `other` is EXCLUDED: it keeps what C_06 gives it today.
  R1   A key C_06 already classifies `equity` FROM THE TABLE (ETFClassifier layer 1 ticker or layer 2 name) never
       moves: EXCLUDED.
  R3   (~M on its REC, self-drive arm @ce6aa15a17) A key the model calls `equity` that C_06 today places in
       fixed_income or alternatives is EXCLUDED. The model's "ETF -> equity" line outranked C_06's own bond and
       treasury name patterns (a 1-3 month T-bill ETF, a 25-year zero-coupon Treasury fund), so none of these moves.
The outcome is read from C_06's own rule: classify_holding over every 09-22 row with the new items added to a
loader built from the live table, never predicted from the class column.

  python org/.../IRPT_MVP_M/build_cot_new_write_set.py --out <write_set.json>
"""
import argparse
import collections
import hashlib
import importlib.util
import json
import subprocess
import sys
from io import BytesIO
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
GOLD = ROOT / 'data/cot/scripts/gold'
sys.path.insert(0, str(GOLD))
M = ROOT / 'org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M'
RESULTS = M / 'CLASSIFY_COT_NEW_RESULTS_20260926.json'
BATCH_B = M / 'BD_SECURITIES_WRITE_SET_20260925.json'
SERVED_DATE = '2026-09-22'
HELD_AWAY = ('VOYA', 'GILDER GAGNON HOWE', 'LEADER BANK IRA')


def _load(name, file):
    spec = importlib.util.spec_from_file_location(name, str(GOLD / file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def personal(name) -> bool:
    n = ' '.join(str(name or '').upper().replace('&', ' ').split())
    return n.startswith('INVESTOR MANUAL ASSET') or any(n.startswith(h) for h in HELD_AWAY)


def table_layer(e, ticker, name):
    """'table' when ETFClassifier answers from a table row (layer 1 ticker or layer 2 name), else ''."""
    if ticker:
        t = str(ticker).strip().upper()
        if t not in ('NONE', 'NAN', '') and t in e._ticker_map:
            return 'table'
    if name and e._name_map.get(e.normalize_name(str(name))) in e._ticker_map:
        return 'table'
    return ''


def build(out: Path):
    import boto3
    import pandas as pd
    c06 = _load('c06', 'C_06.client_mix_timeseries.py')
    e = c06.ETFClassifier.instance()
    results = json.loads(RESULTS.read_text(encoding='utf-8'))['results']
    by_pk = {r['pk']: dict(r, source='cot-new-run') for r in results}
    for r in json.loads(BATCH_B.read_text(encoding='utf-8'))['rows']:
        if r['batch'] == 'B_HELD_OTHER' and r['pk'] not in by_pk:
            by_pk[r['pk']] = {'pk': r['pk'], 'ticker': '', 'asset_name': r['asset_name_raw'], 'asset_class': r['asset_class'],
                              'sub_asset_class': r['sub_asset_class'], 'confidence': r['confidence'],
                              'needs_review': r['needs_review'], 'rationale': r['rationale'], 'firm': r['firm'],
                              'source': 'batch-b-run-20260925'}
    rows, excluded = [], []
    for pk in sorted(by_pk):
        r = by_pk[pk]
        ticker = r['ticker'] if r['ticker'] not in ('', 'None') else None
        cur = c06.classify_holding(ticker, r['asset_name'])
        cls, note = r['asset_class'], ''
        if personal(r['asset_name']) and cls != 'other':
            cls, note = 'other', 'R2a: personal/held-away set to other (model said %s)' % cls
        if cls == 'other' and not personal(r['asset_name']):
            excluded.append({'pk': pk, 'model_class': cls, 'c06_today': cur, 'rule': 'R2b: a security is never other'})
            continue
        if cur == 'equity' and cls != 'equity' and table_layer(e, ticker, r['asset_name']):
            excluded.append({'pk': pk, 'model_class': cls, 'c06_today': cur, 'rule': 'R1: established equity stays'})
            continue
        if cls == 'equity' and cur in ('fixed_income', 'alternatives'):
            excluded.append({'pk': pk, 'model_class': cls, 'c06_today': cur,
                             'rule': 'R3: no move to equity off a class C_06 already assigns by name'})
            continue
        rows.append({**{k: r.get(k) for k in ('pk', 'ticker', 'asset_name', 'sub_asset_class', 'confidence',
                                              'needs_review', 'rationale', 'source')},
                     'asset_class': cls, 'c06_today': cur, 'note': note})
    # The outcome, from C_06's own rule: classify every 09-22 row with the live loader (before), add the new items to
    # the loader exactly as a table row would load (ticker map + asset_name_raw), and classify again (after).
    s3 = boto3.client('s3', region_name='us-east-1')
    h = pd.read_parquet(BytesIO(s3.get_object(Bucket='opal-data-cot', Key='gold/canonical/holdings/%s.parquet' % SERVED_DATE)['Body'].read()))
    acct = pd.read_parquet(BytesIO(s3.get_object(Bucket='opal-data-cot', Key='gold/dimensions/accounts_dimension_latest.parquet')['Body'].read()),
                           columns=['account_id', 'relationship_id'])
    h = h.merge(acct, on='account_id', how='left')
    h['mv'] = pd.to_numeric(h['market_value'], errors='coerce').fillna(0.0)
    tick = [str(t) if pd.notna(t) else '' for t in h['ticker']]
    name = [str(a) if pd.notna(a) else '' for a in h['asset_name']]
    before = [c06.classify_holding(t or None, a) for t, a in zip(tick, name)]
    for r in rows:
        e._ticker_map[r['pk']] = {'ticker': r['pk'], 'asset_class': r['asset_class']}
        e._name_map[e.normalize_name(str(r['asset_name']))] = r['pk']
    after = [c06.classify_holding(t or None, a) for t, a in zip(tick, name)]
    moves, per_client = collections.Counter(), collections.defaultdict(collections.Counter)
    moved_rows = 0
    for b0, a0, mv, rel in zip(before, after, h['mv'], h['relationship_id']):
        if b0 != a0:
            moved_rows += 1
            moves[(b0, a0)] += mv
            per_client[str(rel)][(b0, a0)] += mv
    sha = hashlib.sha256(json.dumps([r['pk'] for r in rows]).encode('utf-8')).hexdigest()
    doc = {'rules_record': 'ANDREW_DIRECT_20260926_023xZ_ESTABLISHED_EQUITIES_STAY_AND_OTHER_IS_PERSONAL_ONLY.md @c3dde578b9',
           'results': RESULTS.name, 'served_date': SERVED_DATE, 'keys_sha256': sha,
           'counts': {'rows': len(rows), 'excluded': len(excluded),
                      'by_class': dict(collections.Counter(r['asset_class'] for r in rows)),
                      'excluded_by_rule': dict(collections.Counter(x['rule'][:3] for x in excluded)),
                      'moved_holding_rows_0922': moved_rows, 'clients_moved_0922': len(per_client)},
           'moves_usd_0922': {'%s -> %s' % k: round(v, 2) for k, v in moves.items()},
           'per_client_usd_0922': {rel: {'%s -> %s' % k: round(v, 2) for k, v in c.items()} for rel, c in per_client.items()},
           'rows': rows, 'excluded': excluded}
    out.write_text(json.dumps(doc, indent=1) + '\n', encoding='utf-8')
    print(json.dumps(doc['counts'], indent=1))
    print(json.dumps(doc['moves_usd_0922'], indent=1))
    print('keys sha256 %s -> %s' % (sha, out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    build(Path(ap.parse_args().out))


if __name__ == '__main__':
    main()
