#!/usr/bin/env python
"""R28 leg G RE-READ of the 13-row seed (READ-ONLY), on the object C_06 actually reads.

Why: seed22_legg_read.py expects the seeded dollars to leave `unclassified`+`other`, computed from gold/holdings_lots. Cell SC-e-110 (S45_CAUSE.json)
found that expectation wrong: the served `unclassified`+`other` on 2026-10-02 held 1,924.34 before and after. This re-read asks the question the
data can answer: between the pre-seed served version and the first fire after the seed, did the firm's class dollars move by exactly the
dollars of the seeded name that was classified differently, taken from the canonical holdings the fire read?

Result of the first run (2026-10-17): the `cash` and `fixed_income` deltas equal minus and plus the LCFYX (Lord Abbett Convertible I) dollars in
the canonical holdings on every one of 15 dates, within a few dollars.

Usage (repo root):
  python seed_legg_reread_lcfyx.py selftest
  python seed_legg_reread_lcfyx.py read [--tol 5]
Prints `SEED-LEGG-REREAD date=... lcfyx=... cash_delta=... fi_delta=... ok=...` and `SEED-LEGG-REREAD ok=<bool> dates=<n> bad=<k>`.
"""
import io
import json
import sys

BUCKET_BD = 'opal-data-bd'
BUCKET_SERVED = 'opal-data-49financial'
KEY_MDS = 'advi/49financial/platinum/views/mix_daily_summary.json'
PRE_VID = '3BY8Etw3LetRaRFcOofjaAT98PSfp4Z3'
POST_VID = '87CvfcFpbyM7ZRAb0P6AztqK1X74W6cQ'
FIRE1_PREFIX = '2026-10-16T23'


def grade(pre, post, lcfyx_by_date, tol):
    """pre/post: the `firm` maps of two mix_daily_summary versions; lcfyx_by_date: {date: dollars}. Returns (lines, ok, n, bad)."""
    lines, bad, n = [], 0, 0
    for d in sorted(lcfyx_by_date):
        if d not in pre or d not in post:
            continue
        n += 1
        mv = lcfyx_by_date[d]
        dc = float(post[d].get('cash', 0.0)) - float(pre[d].get('cash', 0.0))
        dfi = float(post[d].get('fixed_income', 0.0)) - float(pre[d].get('fixed_income', 0.0))
        good = abs(dc + mv) <= tol and abs(dfi - mv) <= tol
        bad += int(not good)
        lines.append('SEED-LEGG-REREAD date=%s lcfyx=%.2f cash_delta=%.2f fi_delta=%.2f ok=%s' % (d, mv, dc, dfi, good))
    return lines, bad == 0 and n > 0, n, bad


def selftest():
    pre = {'2026-10-01': {'cash': 100.0, 'fixed_income': 10.0}}
    post = {'2026-10-01': {'cash': 60.0, 'fixed_income': 50.0}}
    ok = True
    _, g, n, b = grade(pre, post, {'2026-10-01': 40.0}, 1.0)
    print('SEED-LEGG-REREAD-SELFTEST green:', g and n == 1 and b == 0)
    ok &= g and n == 1 and b == 0
    _, g, _, _ = grade(pre, post, {'2026-10-01': 30.0}, 1.0)
    print('SEED-LEGG-REREAD-SELFTEST negative (dollars differ):', not g)
    ok &= not g
    _, g, n, _ = grade(pre, post, {'2026-10-09': 40.0}, 1.0)
    print('SEED-LEGG-REREAD-SELFTEST negative (no common date):', not g and n == 0)
    ok &= (not g) and n == 0
    print('SEED-LEGG-REREAD-SELFTEST ok=%s' % ok)
    return 0 if ok else 1


def read(tol):
    import boto3
    import pandas as pd
    s3 = boto3.client('s3', region_name='us-east-1')
    pre = json.loads(s3.get_object(Bucket=BUCKET_SERVED, Key=KEY_MDS, VersionId=PRE_VID)['Body'].read())['firm']
    post = json.loads(s3.get_object(Bucket=BUCKET_SERVED, Key=KEY_MDS, VersionId=POST_VID)['Body'].read())['firm']
    # the canonical-holdings version each date had when the 23:00Z fire read it (written 2026-10-16T23:15Z)
    vers = {}
    for pg in s3.get_paginator('list_object_versions').paginate(Bucket=BUCKET_BD, Prefix='gold/canonical/holdings/'):
        for v in pg.get('Versions', []):
            if v['LastModified'].strftime('%Y-%m-%dT%H').startswith(FIRE1_PREFIX):
                vers[v['Key'].rsplit('/', 1)[1][:10]] = (v['Key'], v['VersionId'])
    mv = {}
    for d, (k, vid) in sorted(vers.items()):
        df = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET_BD, Key=k, VersionId=vid)['Body'].read()), columns=['asset_name', 'ticker', 'market_value'])
        hit = df['asset_name'].astype(str).str.upper().str.contains('LORD ABBETT CONVERTIBLE') | (df['ticker'].astype(str).str.upper() == 'LCFYX')
        mv[d] = float(df.loc[hit, 'market_value'].sum())
    print('SEED-LEGG-REREAD pre=%s post=%s canonical_versions=%d' % (PRE_VID, POST_VID, len(vers)))
    lines, ok, n, bad = grade(pre, post, mv, tol)
    for ln in lines:
        print(ln)
    print('SEED-LEGG-REREAD ok=%s dates=%d bad=%d tol=%.0f' % (ok, n, bad, tol))
    return 0 if ok else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['selftest']:
        sys.exit(selftest())
    if a[:1] == ['read']:
        sys.exit(read(float(a[a.index('--tol') + 1]) if '--tol' in a else 5.0))
    raise SystemExit('usage: seed_legg_reread_lcfyx.py selftest | read [--tol 5]')
