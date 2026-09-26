"""The CTO's added condition on the ACCOUNT own-mask publication (SIGNOFF_HOLDINGS_ACCOUNT_OWN_MASK_20260926.md
@45bafa24a1, msg 101333): each firm publishes at its SERVED as_of, and BEFORE latest moves a structural diff against
the served revision shows only level-0 ACCOUNT display.label changes, and 0 changes in amounts, ids, drill_refs,
classes or coverage. Anything else is a STOP.

  dry     No write. Reads the served revision (HoldingsPublication.load), rebuilds the firm at the served business
          date with run_firm(upload=False, local_out=<dir>), and diffs the candidate against the served document.
          Prints the candidate revision digest. Exit 0 only on a labels-only diff.
  check   After an upload: the newly served revision must equal the dry candidate's digest, so the published
          document IS the one the dry diff read.

Usage (from the repo root):
  python org/.../IRPT_MVP_M/account_mask_publication_diff.py dry --firm 49financial --out <dir>
  python org/.../IRPT_MVP_M/account_mask_publication_diff.py check --firm 49financial --expect <revision>
"""
import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
sys.path.insert(0, str(ROOT / 'data/assets/scripts/gold/investor_reporting'))
sys.path.insert(0, str(ROOT / 'lib'))
sys.path.insert(0, str(ROOT / 'infra/aws/lambda/investor-reporting/holdings'))

# Top-level members compared whole. Clocks and source_set_revision carry build identity, so they are printed, never gated.
GATED_TOP = ('scope', 'custody_totals', 'coverage', 'attribution_holdouts')


def _get(s3, ref):
    kw = {'Bucket': ref['bucket'], 'Key': ref['key']}
    if ref.get('version_id'):
        kw['VersionId'] = ref['version_id']
    return s3.get_object(**kw)['Body'].read()


def _served(s3, firm):
    """The served document, assembled whole: HoldingsPublication.load() refuses a whole-firm read by design (bounded
    response), so the nodes come from the accepted Gold Parquet (node_json, which the publisher verifies equals the
    Platinum nodes) and the other members from the Platinum document or its header."""
    import io
    import pyarrow.parquet as pq
    from publication import HoldingsPublication
    idx = HoldingsPublication(s3, firm, qa=False).begin()['document']
    manifest = json.loads(_get(s3, idx['dates'][idx['latest_date']]['manifest']))
    top = json.loads(_get(s3, manifest.get('platinum') or manifest['platinum_header']))
    rows = pq.read_table(io.BytesIO(_get(s3, manifest['gold'])), columns=['node_json']).to_pylist()
    top['nodes'] = [json.loads(r['node_json']) for r in rows]
    return top


def _served_revision(s3, firm):
    """The index's own record of the served revision (the pointer the publication moves)."""
    from publication import HoldingsPublication
    doc = HoldingsPublication(s3, firm, qa=False).begin()["document"]
    return doc["dates"][doc["latest_date"]]["revision"], doc["latest_date"]


def _next_trading_day(tcal, iso):
    day = dt.date.fromisoformat(iso) + dt.timedelta(days=1)
    while not tcal.is_trading_day(day):
        day += dt.timedelta(days=1)
    return day.isoformat()


def structural_diff(served, cand):
    """(label_changes, other_changes) over nodes keyed by node_id plus the gated top-level members."""
    s_nodes = {n['node_id']: n for n in served['nodes']}
    c_nodes = {n['node_id']: n for n in cand['nodes']}
    other = []
    if set(s_nodes) != set(c_nodes):
        other.append({'kind': 'node_set', 'only_served': len(set(s_nodes) - set(c_nodes)),
                      'only_candidate': len(set(c_nodes) - set(s_nodes))})
    labels = []
    for nid in sorted(set(s_nodes) & set(c_nodes)):
        a, b = dict(s_nodes[nid]), dict(c_nodes[nid])
        da, db = a.pop('display', None), b.pop('display', None)
        if a != b:
            keys = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
            other.append({'kind': 'node', 'node_id': nid, 'fields': keys})
        if da != db:
            if a.get('node_kind') == 'ACCOUNT' and a.get('level') == 0 and \
                    {k: v for k, v in (da or {}).items() if k != 'label'} == {k: v for k, v in (db or {}).items() if k != 'label'}:
                labels.append({'node_id': nid, 'served': (da or {}).get('label'), 'candidate': (db or {}).get('label')})
            else:
                other.append({'kind': 'display', 'node_id': nid, 'node_kind': a.get('node_kind')})
    for k in GATED_TOP:
        if served.get(k) != cand.get(k):
            other.append({'kind': 'top', 'member': k})
    return labels, other


def dry(firm, out):
    import boto3
    import holdings_snapshot as hs
    s3 = boto3.client('s3', region_name='us-east-1')
    served = _served(s3, firm)
    as_of = served['clocks']['business_date']
    # The CUTOFF that rebuilds the served business date: INF values at the prior trading day of its custody key, so
    # its served 09-22 comes from a 09-23 cutoff. Try the date itself, then the next trading day; keep the build whose
    # own business date equals the served one.
    for cutoff in (as_of, _next_trading_day(hs.tcal, as_of)):
        result = hs.run_firm(firm, s3, qa=False, upload=False, local_out=out, as_of=cutoff)
        if result['business_date'] == as_of:
            break
    else:
        raise SystemExit('STOP: no cutoff rebuilds served business date %s' % as_of)
    cands = sorted(Path(out).rglob('*.json'))
    cand_path = next(p for p in cands if 'platinum' in str(p) and 'date=%s' % as_of in str(p)
                     and not p.name.endswith(('.manifest.json', '.header.json')))
    cand = json.loads(cand_path.read_text(encoding='utf-8'))
    labels, other = structural_diff(served, cand)
    served_rev, latest = _served_revision(s3, firm)
    report = {'firm': firm, 'cutoff': cutoff, 'served_business_date': as_of, 'index_latest_date': latest, 'served_revision': served_rev,
              'candidate_revision': cand_path.stem, 'candidate_path': str(cand_path),
              'account_label_changes': len(labels), 'other_changes': len(other),
              'other': other[:50], 'label_examples': labels[:8], 'schema_valid': result['schema_valid'],
              'reconcile_ok': result['reconcile_ok'],
              'verdict': 'LABELS-ONLY' if not other and result['schema_valid'] and result['reconcile_ok'] else 'STOP'}
    print(json.dumps(report, indent=1))
    return 0 if report['verdict'] == 'LABELS-ONLY' else 1


def check(firm, expect):
    import boto3
    got, _ = _served_revision(boto3.client('s3', region_name='us-east-1'), firm)
    print(json.dumps({'firm': firm, 'served_revision': got, 'expected': expect, 'match': got == expect}))
    return 0 if got == expect else 1


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='mode', required=True)
    d = sub.add_parser('dry')
    d.add_argument('--firm', required=True)
    d.add_argument('--out', required=True)
    c = sub.add_parser('check')
    c.add_argument('--firm', required=True)
    c.add_argument('--expect', required=True)
    a = ap.parse_args()
    return dry(a.firm, a.out) if a.mode == 'dry' else check(a.firm, a.expect)


if __name__ == '__main__':
    sys.exit(main())
