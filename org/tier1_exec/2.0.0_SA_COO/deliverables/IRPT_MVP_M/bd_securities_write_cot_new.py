"""The signed bd-securities write from the ONE COT classification run (1.0.0_SA_CTO sign-off
org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_BD_SECURITIES_COT_NEW_20260926.md @ab4a2e41bb).

  census --part 1|2   No write. Reads the part's rows from COT_NEW_WRITE_SET_20260926.json, re-reads bd-securities on
                      a fresh scan, and prints the sha256 of the sorted key list (the sign-off's) and any key that
                      now exists. Part 1 is signed at c96398886f143f54..., Part 2 at 389f0e6674545567...
  write --part N      Requires --expect-sha. Re-runs the census and refuses on any difference or any present key.
                      Then one conditional PutItem per key (attribute_not_exists(ticker)): B_01b's item shape plus
                      classified_run. It reads every key back (get_item, consistent) and through a fresh loader
                      (classify by the key's own ticker and name), and writes the receipt. No overwrite, no delete.

Part 2 lands only on its two conditions (the act-1 read-back, and ~D's mapping on origin DEV); this script does
not check them, so the ledger does.

Usage (from the repo root):
  python org/.../IRPT_MVP_M/bd_securities_write_cot_new.py census --part 1
  python org/.../IRPT_MVP_M/bd_securities_write_cot_new.py write --part 1 --expect-sha <sha> --receipt <json>
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
WRITE_SET = ROOT / 'org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/COT_NEW_WRITE_SET_20260926.json'
TABLE, REGION, RUN = 'bd-securities', 'us-east-1', 'irpt-m-cot-new-20260926'
SIGNED = {'1': ('c96398886f143f54', 941), '2': ('389f0e6674545567', 26)}


def census(part: str):
    import boto3
    rows = [r for r in json.loads(WRITE_SET.read_text(encoding='utf-8'))['rows']
            if (r['asset_class'] == 'other') == (part == '2')]
    rows.sort(key=lambda r: r['pk'])
    keys = [r['pk'] for r in rows]
    table = boto3.resource('dynamodb', region_name=REGION).Table(TABLE)
    existing = set()
    for page in table.meta.client.get_paginator('scan').paginate(TableName=TABLE, ProjectionExpression='ticker'):
        existing.update(i['ticker'] for i in page.get('Items', []))
    present = [k for k in keys if k in existing]
    sha = hashlib.sha256(json.dumps(keys).encode('utf-8')).hexdigest()
    return rows, sha, present, len(existing)


def write(part: str, expect_sha: str, receipt: Path):
    import boto3
    from boto3.dynamodb.conditions import Attr
    rows, sha, present, scanned = census(part)
    prefix, count = SIGNED[part]
    if sha != expect_sha or not sha.startswith(prefix) or len(rows) != count or present:
        raise SystemExit('REFUSED: census differs -- %d key(s), sha %s, %d already present' % (len(rows), sha, len(present)))
    if receipt.exists():
        raise SystemExit('REFUSED: %s exists' % receipt)
    table = boto3.resource('dynamodb', region_name=REGION).Table(TABLE)
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    written, refused = [], []
    for r in rows:
        item = {'ticker': r['pk'], 'asset_class': r['asset_class'], 'sub_asset_class': r['sub_asset_class'] or '',
                'confidence': Decimal(str(round(float(r['confidence'] or 0.0), 4))), 'needs_review': bool(r['needs_review']),
                'classified_by': 'gpt-5.4-mini', 'rationale': r['rationale'] or '', 'asset_name_raw': r['asset_name'],
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
    expected = {r['pk']: r['asset_class'] for r in rows}
    loader = {r['pk']: clf.classify('' if r['pk'].startswith('NAME::') else r['pk'], r['asset_name'])
              for r in rows if r['pk'] in written}
    doc = {'act': 'bd-securities COT-new conditional PutItem, part %s' % part,
           'signoff': 'SIGNOFF_BD_SECURITIES_COT_NEW_20260926.md @ab4a2e41bb',
           'started_utc': started, 'finished_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
           'census': {'keys': len(rows), 'sha256_sorted_keys': sha, 'present_before': present, 'table_items_scanned': scanned},
           'written': len(written), 'condition_refused': refused,
           'read_back_matches': sum(1 for k in written if back[k] == (expected[k], RUN)),
           'loader_matches': sum(1 for k, v in loader.items() if v == expected[k]),
           'loader_mismatches': {k: [v, expected[k]] for k, v in loader.items() if v != expected[k]},
           'rollback': 'DeleteItem per written key with condition classified_run = %s (human confirmation)' % RUN,
           'written_keys': written}
    receipt.write_text(json.dumps(doc, indent=1) + '\n', encoding='utf-8')
    print('OK: wrote %d of %d; %d condition-refused; read-back %d; loader %d (%d mismatch) -> %s' % (
        len(written), len(rows), len(refused), doc['read_back_matches'], doc['loader_matches'],
        len(doc['loader_mismatches']), receipt))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='mode', required=True)
    c = sub.add_parser('census')
    c.add_argument('--part', choices=('1', '2'), required=True)
    w = sub.add_parser('write')
    w.add_argument('--part', choices=('1', '2'), required=True)
    w.add_argument('--expect-sha', required=True)
    w.add_argument('--receipt', required=True)
    args = ap.parse_args()
    if args.mode == 'census':
        rows, sha, present, scanned = census(args.part)
        print('census part %s: %d key(s) (signed %d); sha256 %s; %d already present; %d table items scanned'
              % (args.part, len(rows), SIGNED[args.part][1], sha, len(present), scanned))
    else:
        write(args.part, args.expect_sha, Path(args.receipt))


if __name__ == '__main__':
    main()
