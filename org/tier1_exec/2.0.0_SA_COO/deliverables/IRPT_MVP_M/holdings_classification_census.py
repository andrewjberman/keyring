"""Coverage census for the DSGN_IRPTV1 v0.6 members (CTO 100905): asset_class on SECURITY nodes, model_code on MODEL_LEAF.

Read-only. Reads every partition of each firm's SERVED holdings revision through the reader library, classifies each
security through the canonical classifier (ETFClassifier over DynamoDB bd-securities, one scan) and records WHICH layer
answered (TABLE, NAME_ALIAS, NAME_PATTERN, TICKER_SHAPE, NONE), and resolves each model leaf name by the registry rule
the COT build already uses (cot_constituent_taxonomy). Counts by distinct security and by served dollars. Writes one JSON.

Usage (worktree root): python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/holdings_classification_census.py --out <json>
"""
import argparse
import datetime as dt
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
for p in ('lib', 'infra/aws/lambda/investor-reporting/holdings', 'data/black_diamond/scripts/gold/lib',
          'data/assets/scripts/gold/investor_reporting'):
    sys.path.insert(0, str(ROOT / p))
import boto3  # noqa: E402
from publication import HoldingsPublication, MAX_JSON_BYTES  # noqa: E402
import etf_classifier as ec  # noqa: E402

FIRMS = ('49financial', 'inflection', 'cottonwood')


def basis_of(clf, ticker, name):
    """The layer of ETFClassifier.classify that answers, mirrored from its own code (:81-129)."""
    if ticker and str(ticker).upper() == 'CASH_USD':
        return 'TABLE'
    t = str(ticker or '').strip().upper()
    if t and t not in ('NONE', 'NAN') and t in clf._ticker_map:
        return 'TABLE'
    if name and clf._name_map.get(clf.normalize_name(str(name))) in clf._ticker_map:
        return 'NAME_ALIAS'
    up = str(name or '').upper()
    if ec._RE_ALT.search(up) or ec._RE_CASH.search(up) or ec._RE_FI.search(up):
        return 'NAME_PATTERN'
    if t and ec.re.fullmatch(r'[A-Z]{1,5}(\.[A-Z])?', t):
        return 'TICKER_SHAPE'
    return 'NONE'


def served_nodes(s3, firm):
    st = HoldingsPublication(s3, firm)
    obs = st.begin()
    idx = obs['document']
    date = idx['latest_date']
    row = idx['dates'][date]
    rev, part = row['revision'], 'date=' + date
    mf = json.loads(st.read_exact(row['manifest'], expected_location=st.location(
        'platinum', part, rev + '.manifest.json'), max_bytes=MAX_JSON_BYTES))
    nodes = []
    for i, p in enumerate(mf['partitions']):
        body = st.read_exact(p['object'], expected_location=st.location(
            'platinum', part, rev + '.part%05d.json' % i), max_bytes=MAX_JSON_BYTES)
        nodes.extend(json.loads(body)['nodes'])
    return nodes, {'revision': rev, 'business_date': date, 'index_version': obs['reference'].get('version_id')}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    import holdings_snapshot as hs  # the COT registry rule, from its one home
    clf = ec.ETFClassifier('bd-securities')
    s3 = boto3.client('s3', region_name='us-east-1')
    report = {'measured_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
              'source_pin': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
              'classifier': {'table': 'bd-securities', 'tickers': len(clf._ticker_map),
                             'aliases': len(clf._name_map)}, 'firms': {}}
    for firm in FIRMS:
        nodes, ref = served_nodes(s3, firm)
        secs = [n for n in nodes if n['node_kind'] == 'SECURITY']
        leaves = [n for n in nodes if n['node_kind'] == 'MODEL_LEAF']
        by_basis, by_class, usd_basis = Counter(), Counter(), defaultdict(float)
        distinct = {}
        for n in secs:
            disp = n.get('display') or {}
            ticker = disp.get('symbol')
            name = disp.get('description') or disp.get('label')
            sid = n.get('security_id') or {}
            key = (sid.get('namespace'), sid.get('value'), ticker)
            b = basis_of(clf, ticker, name)
            ac = clf.classify(ticker, name) or 'unclassified'
            if key not in distinct:
                distinct[key] = (b, ac)
            usd_basis[b] += float((n.get('amount') or {}).get('value') or 0.0)
        for b, ac in distinct.values():
            by_basis[b] += 1
            by_class[ac] += 1
        names = Counter((leaf.get('display') or {}).get('label') for leaf in leaves)
        coded = {}
        for name in names:
            tx = hs.cot_constituent_taxonomy(name)
            coded[name] = tx.get('registry_key')
        report['firms'][firm] = {
            'served': ref, 'security_nodes': len(secs), 'distinct_securities': len(distinct),
            'distinct_by_basis': dict(by_basis), 'distinct_by_asset_class': dict(by_class),
            'usd_by_basis': {k: round(v, 2) for k, v in usd_basis.items()},
            'model_leaf_nodes': len(leaves), 'distinct_model_names': len(names),
            'model_names_with_registry_key': sum(1 for v in coded.values() if v),
            'model_leaf_nodes_with_registry_key': sum(c for nm, c in names.items() if coded.get(nm)),
            'model_name_to_registry_key': coded,
        }
        f = report['firms'][firm]
        print(firm, json.dumps({k: f[k] for k in ('distinct_securities', 'distinct_by_basis', 'usd_by_basis',
                                                   'distinct_model_names', 'model_names_with_registry_key')}),
              flush=True)
    Path(args.out).write_text(json.dumps(report, indent=1, sort_keys=True) + '\n', encoding='utf-8')
    print('OK: wrote', args.out)


if __name__ == '__main__':
    main()
