"""The signed bd-securities write, batch A: 204 net-new NAME:: keys (1.0.0_SA_CTO sign-off
org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_BD_SECURITIES_BATCH_A_20260925.md @8214723353).

  census   No write. Reads the write set's A_NOW rows, drops the three struck preferreds, re-reads bd-securities on a
           fresh scan, and prints the sha256 of the ordered 204-key list plus any key that now exists. It REFUSES
           on anything but 204 keys with none present.
  write    Requires --expect-sha. Re-runs the census and refuses on any difference. Then one conditional PutItem per
           key (attribute_not_exists(ticker)): B_01b's item shape (B_01b.classify_new_securities.py:330-340) plus
           classified_run. It reads every key back (get_item) and through a fresh loader (classify by name), and
           writes the receipt. No overwrite, no delete.

Usage (from the worktree root):
  python org/.../IRPT_MVP_M/bd_securities_write_batch_a.py census
  python org/.../IRPT_MVP_M/bd_securities_write_batch_a.py write --expect-sha <sha> --receipt <json>
"""
import argparse
import datetime as dt
import hashlib
import json
import subprocess
import sys
from decimal import Decimal
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
sys.path.insert(0, str(ROOT / 'data/black_diamond/scripts/gold'))
WRITE_SET = ROOT / 'org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/BD_SECURITIES_WRITE_SET_20260925.json'
TABLE, REGION, RUN = 'bd-securities', 'us-east-1', 'irpt-m-once-20260925'
STRUCK = ('GLADSTONE CAP 6.25% PFD PFD SER A', 'MORGAN STANLE 4.25% PFD PFD SER O', 'VORNADO REALTY 5.4% PFD PFD SER L')
SIGNED_COUNT = 204


def census():
    import boto3
    rows = [r for r in json.loads(WRITE_SET.read_text(encoding='utf-8'))['rows']
            if r['batch'] == 'A_NOW' and r['asset_name_raw'] not in STRUCK]
    rows.sort(key=lambda r: r['pk'])
    keys = [r['pk'] for r in rows]
    table = boto3.resource('dynamodb', region_name=REGION).Table(TABLE)
    existing = set()
    for page in table.meta.client.get_paginator('scan').paginate(TableName=TABLE, ProjectionExpression='ticker'):
        existing.update(i['ticker'] for i in page.get('Items', []))
    present = [k for k in keys if k in existing]
    sha = hashlib.sha256(json.dumps(keys).encode('utf-8')).hexdigest()
    return rows, sha, present, len(existing)


def write(expect_sha: str, receipt: Path):
    import boto3
    from boto3.dynamodb.conditions import Attr
    rows, sha, present, scanned = census()
    if sha != expect_sha or len(rows) != SIGNED_COUNT or present:
        raise SystemExit('REFUSED: census differs -- %d key(s), sha %s, %d already present' % (len(rows), sha, len(present)))
    table = boto3.resource('dynamodb', region_name=REGION).Table(TABLE)
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    written, refused = [], []
    for r in rows:
        item = {'ticker': r['pk'], 'asset_class': r['asset_class'], 'sub_asset_class': r['sub_asset_class'] or '',
                'confidence': Decimal(str(round(float(r['confidence']), 4))), 'needs_review': bool(r['needs_review']),
                'classified_by': 'gpt-5.4-mini', 'rationale': r['rationale'] or '', 'asset_name_raw': r['asset_name_raw'],
                'last_updated': dt.datetime.now(dt.timezone.utc).isoformat(), 'classified_run': RUN}
        try:
            table.put_item(Item=item, ConditionExpression=Attr('ticker').not_exists())
            written.append(r['pk'])
        except table.meta.client.exceptions.ConditionalCheckFailedException:
            refused.append(r['pk'])
    back = {}
    for k in written:
        got = table.get_item(Key={'ticker': k}, ConsistentRead=True).get('Item') or {}
        back[k] = (got.get('asset_class'), got.get('classified_run'))
    from lib.etf_classifier import ETFClassifier
    clf = ETFClassifier()
    by_name = {r['pk']: clf.classify('', r['asset_name_raw']) for r in rows if r['pk'] in written}
    expected = {r['pk']: r['asset_class'] for r in rows}
    doc = {'act': 'bd-securities batch A conditional PutItem', 'signoff': 'SIGNOFF_BD_SECURITIES_BATCH_A_20260925.md @8214723353',
           'started_utc': started, 'finished_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
           'census': {'keys': len(rows), 'sha256_ordered_keys': sha, 'present_before': present, 'table_items_scanned': scanned},
           'written': len(written), 'condition_refused': refused,
           'read_back_matches': sum(1 for k in written if back[k] == (expected[k], RUN)),
           'loader_by_name_matches': sum(1 for k, v in by_name.items() if v == expected[k]),
           'loader_by_name_mismatches': {k: [v, expected[k]] for k, v in by_name.items() if v != expected[k]},
           'rollback': 'DeleteItem per written key with condition classified_run = %s (human confirmation)' % RUN,
           'written_keys': written}
    receipt.write_text(json.dumps(doc, indent=1) + '\n', encoding='utf-8')
    print('OK: wrote %d of %d; %d condition-refused; read-back %d; loader-by-name %d -> %s' % (
        len(written), len(rows), len(refused), doc['read_back_matches'], doc['loader_by_name_matches'], receipt))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='mode', required=True)
    sub.add_parser('census')
    w = sub.add_parser('write')
    w.add_argument('--expect-sha', required=True)
    w.add_argument('--receipt', required=True)
    args = ap.parse_args()
    if args.mode == 'census':
        rows, sha, present, scanned = census()
        print('census: %d key(s) (signed %d); sha256 %s; %d already present; %d table items scanned'
              % (len(rows), SIGNED_COUNT, sha, len(present), scanned))
    else:
        write(args.expect_sha, Path(args.receipt))


if __name__ == '__main__':
    main()
