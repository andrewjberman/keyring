"""S152 before/after identity on one COT date (CTO 101685 term 2). Read-only; writes nothing to S3.

Builds each scope's one-day mix for the date the way C_06 does: the canonical/holdings partition, ghost exclusion,
positive rows (C_06:462), relationship map, and the branch's classify_series. It then runs compute_period_views with the
list served today (CLOUD lib/mix_views) and with the branch list (irpt-m-s152). For every scope and granularity it
checks, to the cent: the added classes' values plus unclassified_after equal unclassified_before, and total_aua is
unchanged. It prints the denominator and every mismatch.

Usage: python s152_period_view_identity.py --before <gold dir, CLOUD> --after <gold dir, irpt-m-s152>
       [--date 2026-09-22] [--out <json>]
"""
import argparse
import importlib.util
import json
import sys
from io import BytesIO
from pathlib import Path

import boto3
import pandas as pd

BUCKET = 'opal-data-cot'


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--before', required=True)
    ap.add_argument('--after', required=True)
    ap.add_argument('--date', default='2026-09-22')
    ap.add_argument('--out')
    a = ap.parse_args()
    after_dir = Path(a.after).resolve()
    sys.path.insert(0, str(after_dir))
    c06 = load(after_dir / 'C_06.client_mix_timeseries.py', 'c06_after')
    mv_after = load(after_dir / 'lib' / 'mix_views.py', 'mv_after')
    mv_before = load(Path(a.before).resolve() / 'lib' / 'mix_views.py', 'mv_before')
    from lib.exclusions import load_ghost_account_ids

    s3 = boto3.client('s3')

    def rd(key, cols=None):
        return pd.read_parquet(BytesIO(s3.get_object(Bucket=BUCKET, Key=key)['Body'].read()), columns=cols)

    pos = rd(f'gold/canonical/holdings/{a.date}.parquet', ['account_id', 'ticker', 'asset_name', 'market_value'])
    pos['account_id'] = pos['account_id'].astype(str)
    pos = pos[~pos['account_id'].isin(load_ghost_account_ids())]
    dim = rd('gold/dimensions/accounts_dimension_latest.parquet', ['account_id', 'relationship_id'])
    pos['relationship_id'] = pos['account_id'].map(dict(zip(dim['account_id'].astype(str), dim['relationship_id'])))
    pos = pos.dropna(subset=['relationship_id'])
    pos['market_value'] = pd.to_numeric(pos['market_value'], errors='coerce')
    pos = pos[pos['market_value'] > 0].copy()
    pos['asset_class'] = c06.classify_series(pos['ticker'], pos['asset_name'])

    def daily(df):
        d = {ac: float(v) for ac, v in df.groupby('asset_class')['market_value'].sum().items()}
        d['total'] = float(df['market_value'].sum())
        return {a.date: d}

    scopes = {('firm', 'cot'): daily(pos)}
    for r, g in pos.groupby('relationship_id'):
        scopes[('relationship', str(r))] = daily(g)
    added = [c for c in mv_after.MIX_ASSET_CLASSES if c not in mv_before.MIX_ASSET_CLASSES]
    checked, mismatches, moved = 0, [], {}
    for scope, dd in scopes.items():
        vb, va = mv_before.compute_period_views(dd), mv_after.compute_period_views(dd)
        for gran in vb:
            for rb, ra in zip(vb[gran], va[gran]):
                checked += 1
                add = sum(ra[c]['value'] for c in added)
                lhs = round(add + ra['unclassified']['value'], 2)
                rhs = round(rb['unclassified']['value'], 2)
                if abs(lhs - rhs) > 0.01 or ra['total_aua'] != rb['total_aua']:
                    mismatches.append({'scope': scope, 'gran': gran, 'lhs': lhs, 'rhs': rhs,
                                       'total_before': rb['total_aua'], 'total_after': ra['total_aua']})
                if gran == 'quarterly':
                    for c in added:
                        moved[c] = moved.get(c, 0.0) + (ra[c]['value'] if scope[0] == 'firm' else 0.0)
    res = {'date': a.date, 'list_before': mv_before.MIX_ASSET_CLASSES, 'list_after': mv_after.MIX_ASSET_CLASSES,
           'added': added, 'scopes': len(scopes), 'rows_checked': checked, 'mismatches': len(mismatches),
           'mismatch_detail': mismatches[:50], 'firm_quarterly_added_values': {k: round(v, 2) for k, v in moved.items()}}
    text = json.dumps(res, indent=1, default=str)
    print(text)
    if a.out:
        Path(a.out).write_text(text + '\n', encoding='utf-8')
    return 0 if not mismatches else 1


if __name__ == '__main__':
    sys.exit(main())
