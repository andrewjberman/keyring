"""Negative-cash census for the COT cash-line half (CRO msg 101595). Read-only.

Asks: of the relationships whose Black Diamond cash line (ticker CASH, asset name CASH) moves equity -> cash, how many
net negative in cash, and does each reader render a negative cash slice. Inputs are the served COT inputs the readers
use: the latest canonical/holdings partition (C_06, D_03 fallback) and the latest holdings_lots (D_04 account step,
D_03 when present), each with the ghost exclusion applied.

Usage: python cot_cash_line_negative_census.py [--out <json>]
"""
import argparse
import json
import sys
from io import BytesIO
from pathlib import Path

import boto3
import pandas as pd

BUCKET = 'opal-data-cot'
CANONICAL = 'gold/canonical/holdings/'
LOTS = 'gold/timeseries/holdings_lots/'
ACCOUNTS_DIMENSION = 'gold/dimensions/accounts_dimension_latest.parquet'
GOLD = Path(__file__).resolve().parents[5] / 'data' / 'cot' / 'scripts' / 'gold'

s3 = boto3.client('s3')


def latest(prefix):
    keys = []
    for page in s3.get_paginator('list_objects_v2').paginate(Bucket=BUCKET, Prefix=prefix):
        keys += [o['Key'] for o in page.get('Contents', []) if o['Key'].endswith('.parquet')
                 and 'backfill' not in o['Key'].rsplit('/', 1)[-1]]
    return (sorted(keys)[-1] if keys else None), len(keys)


def read(key, cols=None):
    return pd.read_parquet(BytesIO(s3.get_object(Bucket=BUCKET, Key=key)['Body'].read()), columns=cols)


def cash_line(df):
    t = df['ticker'].fillna('').astype(str).str.strip().str.upper()
    n = df['asset_name'].fillna('').astype(str).str.split().str.join(' ').str.upper()
    return (t == 'CASH') & (n == 'CASH')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out')
    a = ap.parse_args()
    cfg = json.loads((GOLD / 'aua_overrides.json').read_text(encoding='utf-8'))
    ghosts = {e['account_id'] for e in cfg.get('ghost_accounts', {}).get('accounts', [])}
    out = {'ghost_accounts': len(ghosts)}

    ckey, cn = latest(CANONICAL)
    pos = read(ckey, ['account_id', 'ticker', 'asset_name', 'market_value'])
    pos['account_id'] = pos['account_id'].astype(str)
    dim = read(ACCOUNTS_DIMENSION, ['account_id', 'relationship_id'])
    rel = dict(zip(dim['account_id'].astype(str), dim['relationship_id']))
    pos = pos[~pos['account_id'].isin(ghosts)].copy()
    pos['relationship_id'] = pos['account_id'].map(rel)
    pos = pos.dropna(subset=['relationship_id'])
    cl = pos[cash_line(pos)]
    nz = cl[cl['market_value'].notna() & (cl['market_value'] != 0)]  # NaN != 0 is True; drop NaN first
    by_rel = nz.groupby('relationship_id')['market_value'].agg(['sum', 'count', lambda s: int((s < 0).sum())])
    by_rel.columns = ['net', 'rows', 'neg_rows']
    neg_rel = by_rel[by_rel['net'] < 0]
    c06 = cl[cl['market_value'] > 0]  # C_06 :462 drops market_value <= 0 before classifying
    out['canonical'] = {
        'key': ckey, 'partitions': cn,
        'cash_line_rows': int(len(cl)), 'nonzero_rows': int(len(nz)),
        'negative_rows': int((nz['market_value'] < 0).sum()),
        'negative_rows_sum': round(float(nz.loc[nz['market_value'] < 0, 'market_value'].sum()), 2),
        'relationships_nonzero': int(len(by_rel)),
        'relationships_net_negative': int(len(neg_rel)),
        'net_negative_detail': {str(k): round(float(v), 2) for k, v in neg_rel['net'].items()},
        'relationships_with_any_negative_row': int((by_rel['neg_rows'] > 0).sum()),
        'net_all': round(float(nz['market_value'].sum()), 2),
        'c06_moves_positive_only': round(float(c06['market_value'].sum()), 2),
        'c06_relationships': int(c06['relationship_id'].nunique()),
    }

    lkey, ln = latest(LOTS)
    if lkey:
        lots = read(lkey, ['account_id', 'ticker', 'asset_name', 'market_value', 'is_open'])
        lots = lots[lots['is_open'].fillna(False)].copy()
        lots['account_id'] = lots['account_id'].astype(str)
        lots = lots[~lots['account_id'].isin(ghosts)]
        lots['market_value'] = pd.to_numeric(lots['market_value'], errors='coerce').fillna(0.0)
        ll = lots[cash_line(lots) & (lots['market_value'] != 0)]
        acct = ll.groupby('account_id')['market_value'].sum()
        totals = lots.groupby('account_id')['market_value'].sum()
        neg = acct[acct < 0]
        out['holdings_lots'] = {
            'key': lkey, 'partitions': ln, 'open_rows': int(len(lots)),
            'cash_line_nonzero_rows': int(len(ll)), 'accounts': int(len(acct)),
            'accounts_net_negative_cash_line': int(len(neg)),
            'of_which_account_total_positive': int((totals.reindex(neg.index) > 0).sum()),
            'net_negative_detail': {k: round(float(v), 2) for k, v in neg.items()},
        }
    else:
        out['holdings_lots'] = {'key': None, 'partitions': ln}
    text = json.dumps(out, indent=2)
    print(text)
    if a.out:
        Path(a.out).write_text(text + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    sys.exit(main())
