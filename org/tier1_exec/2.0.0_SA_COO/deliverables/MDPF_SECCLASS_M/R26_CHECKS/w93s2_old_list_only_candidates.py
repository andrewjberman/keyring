#!/usr/bin/env python
"""Row D1-W93-S2 measurement (READ-ONLY): how many E_18 canonical candidates take their class only from the old list.

E_18's candidates are the open (ticker, asset_name) pairs of the latest holdings_lots partition with a real ticker that
`etf-classifications` does not carry. For each, this reads the old list (`bd-securities`) and reports whether it holds a row
with an asset_class: those are the tickers the lookup at E_18:291 currently feeds, and the ones that would turn unresolved
if the lookup is removed. Prints one summary line `W93S2 ...` and the per-ticker table sorted by market value.
Run from the repo root:  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R26_CHECKS/w93s2_old_list_only_candidates.py
"""
import io
import sys

import boto3
import pandas as pd

BUCKET = 'opal-data-bd'
PREFIX = 'gold/holdings_lots/'


def scan_keys(table, proj):
    out, kw = [], {'ProjectionExpression': proj, 'ExpressionAttributeNames': {'#t': 'ticker'}} if 'ticker' in proj else {}
    return out, kw


def scan_all(table, attrs):
    items, kw = [], {'ProjectionExpression': ', '.join('#%d' % i for i in range(len(attrs))),
                     'ExpressionAttributeNames': {'#%d' % i: a for i, a in enumerate(attrs)}}
    pages = 0
    while True:
        r = table.scan(**kw)
        pages += 1
        items.extend(r.get('Items', []))
        if 'LastEvaluatedKey' not in r:
            return items, pages
        kw['ExclusiveStartKey'] = r['LastEvaluatedKey']


def real_ticker(t):
    t = str(t).strip().upper() if t is not None else ''
    return t if t and t not in ('NONE', 'NAN') and t.isalpha() and 1 <= len(t) <= 5 else None


def main():
    s3 = boto3.client('s3', region_name='us-east-1')
    ddb = boto3.resource('dynamodb', region_name='us-east-1')
    latest = None
    for page in s3.get_paginator('list_objects_v2').paginate(Bucket=BUCKET, Prefix=PREFIX):
        for o in page.get('Contents', []):
            if o['Key'].endswith('.parquet') and (latest is None or o['LastModified'] > latest['LastModified']):
                latest = o
    df = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=latest['Key'])['Body'].read()),
                         columns=['ticker', 'asset_name', 'market_value', 'is_open'])
    df = df[df['is_open'] == True]  # noqa: E712
    df['pk'] = df['ticker'].map(real_ticker)
    df = df[df['pk'].notna()]
    new_items, p1 = scan_all(ddb.Table('etf-classifications'), ['ticker'])
    canon = {i['ticker'] for i in new_items}
    old_items, p2 = scan_all(ddb.Table('bd-securities'), ['ticker', 'asset_class', 'sub_asset_class'])
    old = {i['ticker']: i for i in old_items}
    cand = df[~df['pk'].isin(canon)].groupby('pk', dropna=False)['market_value'].sum().reset_index()
    cand['old_class'] = cand['pk'].map(lambda k: (old.get(k) or {}).get('asset_class'))
    has_old = cand[cand['old_class'].notna() & (cand['old_class'] != '')]
    print('W93S2 partition=%s open_real_ticker_rows=%d etf_classifications_keys=%d (pages %d) bd_securities_keys=%d (pages %d) '
          'candidates_not_in_canonical=%d candidates_mv=%.2f candidates_with_old_list_class=%d old_list_class_mv=%.2f' % (
              latest['Key'], len(df), len(canon), p1, len(old), p2, len(cand), cand['market_value'].sum(),
              len(has_old), has_old['market_value'].sum()))
    for _, r in has_old.sort_values('market_value', ascending=False).head(25).iterrows():
        print('  %-6s mv=%14.2f old_class=%s' % (r['pk'], r['market_value'], r['old_class']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
