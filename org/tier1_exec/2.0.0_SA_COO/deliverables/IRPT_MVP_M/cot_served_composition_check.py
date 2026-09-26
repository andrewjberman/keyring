"""Served COT composition check (CTO 101616 condition (2); CRO 101629). Read-only.

Reads every SERVED D_03 composition in s3://opal-data-cot (firm: gold/views/firm_composition.json; relationships:
gold/entities/clients/*_composition.json) and prints the denominator, the data_as_of spread, the count whose mix pct
sums above 100% (tolerance 0.05pp), and z09305653's cash slice. Run it before the cash-line deploy (baseline) and
after the first scheduled run that carries it; the bar after is 0 over 100%.

Usage: python cot_served_composition_check.py [--out <json>]
"""
import argparse
import json
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import boto3

BUCKET = 'opal-data-cot'
FIRM = 'gold/views/firm_composition.json'
PREFIX = 'gold/entities/clients/'
WATCH = 'z09305653'
TOL = 0.0005

s3 = boto3.client('s3')


def get(key):
    obj = s3.get_object(Bucket=BUCKET, Key=key)
    return key, obj['LastModified'].isoformat(), json.loads(obj['Body'].read())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out')
    a = ap.parse_args()
    keys = []
    for page in s3.get_paginator('list_objects_v2').paginate(Bucket=BUCKET, Prefix=PREFIX):
        keys += [o['Key'] for o in page.get('Contents', []) if o['Key'].endswith('_composition.json')]
    with ThreadPoolExecutor(16) as ex:
        docs = list(ex.map(get, [FIRM] + keys))
    over, asof, watch = [], Counter(), None
    for key, lm, doc in docs:
        s = sum(float(m.get('pct') or 0) for m in doc.get('mix', []))
        asof[doc.get('data_as_of')] += 1
        if s > 1.0 + TOL:
            over.append({'key': key, 'pct_sum': round(s, 6), 'last_modified': lm})
        if key == f'{PREFIX}{WATCH}_composition.json':
            watch = {m['asset_class']: round(float(m.get('pct') or 0), 6) for m in doc.get('mix', [])}
            watch['_last_modified'] = lm
    res = {'bucket': BUCKET, 'scopes_read': len(docs), 'relationships': len(keys), 'data_as_of': dict(asof),
           'over_100pct': len(over), 'over_detail': over, WATCH: watch}
    text = json.dumps(res, indent=1, default=str)
    print(text)
    if a.out:
        Path(a.out).write_text(text + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    sys.exit(main())
