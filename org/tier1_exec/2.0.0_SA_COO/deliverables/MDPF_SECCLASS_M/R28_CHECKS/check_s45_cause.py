#!/usr/bin/env python
"""R28 SC-e-110 acceptance (READ-ONLY): does S45_CAUSE.json name why the 13-row seed is not visible where leg G reads it, on numbers
the checker recomputes from S3?

Usage (repo root):
  python check_s45_cause.py selftest
  python check_s45_cause.py read [--file <S45_CAUSE.json>]

The worker writes S45_CAUSE.json (default path below). Required keys:
  first_divergence   one of instrument-expectation | table-read | classify-call | identity-join | aggregate | other
  canonical          {bucket, key, version_id}: the canonical-holdings object of 2026-10-02 the C_06 fire read (a version, not "latest")
  tickers            one entry per SEEDED ticker of SEED22_PLAN.json `planned` (13): {ticker, canonical_rows, canonical_mv, class_in_table, note}
                     canonical_rows / canonical_mv are what that object holds for the ticker (upper-cased match), recomputed by the checker within 0.01
  served             {bucket, key, pre_version_id, post_version_id, date, uncl_other_pre, uncl_other_post}: `unclassified`+`other` of the firm on that
                     date in two versions of the served mix_daily_summary.json, recomputed within 0.01
  conclusion         at least 40 characters: where the seeded dollars stop, in one place
  fix                at least 20 characters: what would make leg G read true (an instrument change or a code change), stated, not done
Prints `S45-CAUSE ok=<bool> problems=<list>`; exit 0 ok, 1 not ok.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, *(['..'] * 6)))
DEFAULT = os.path.join(ROOT, 'org', 'missions', 'D8', 'MDPF', 'MDPF_SECCLASS', 'deliverables', '0.9.0_WK_MDPF_SECCLASS~100', 'S45_CAUSE.json')
PLAN = os.path.join(ROOT, 'org', 'missions', 'D8', 'MDPF', 'MDPF_SECCLASS', 'deliverables', '0.9.0_WK_MDPF_SECCLASS~97', 'SEED22_PLAN.json')
ENUM = ('instrument-expectation', 'table-read', 'classify-call', 'identity-join', 'aggregate', 'other')
TOL = 0.01


def grade(doc, plan_tickers, io_):
    """io_.ticker_mv(bucket,key,vid)->{TICKER: (rows, mv)}; io_.uncl_other(bucket,key,vid,date)->float."""
    p = []
    if not isinstance(doc, dict):
        return ['document is not an object']
    for k in ('first_divergence', 'canonical', 'tickers', 'served', 'conclusion', 'fix'):
        if k not in doc:
            p.append('missing key %s' % k)
    if p:
        return p
    if doc['first_divergence'] not in ENUM:
        p.append('first_divergence %r is not one of %s' % (doc['first_divergence'], ENUM))
    c = doc['canonical']
    try:
        have = io_.ticker_mv(c['bucket'], c['key'], c['version_id'])
        got = {str(e.get('ticker', '')).upper(): e for e in doc['tickers'] if isinstance(e, dict)}
        for t in sorted(plan_tickers):
            e = got.get(t)
            if e is None:
                p.append('ticker %s has no entry' % t)
                continue
            rows, mv = have.get(t, (0, 0.0))
            if int(e.get('canonical_rows', -1)) != int(rows):
                p.append('%s canonical_rows %s != recomputed %s' % (t, e.get('canonical_rows'), rows))
            if abs(float(e.get('canonical_mv', -1e18)) - float(mv)) > TOL:
                p.append('%s canonical_mv %s != recomputed %.2f' % (t, e.get('canonical_mv'), mv))
            if not (isinstance(e.get('class_in_table'), str) and e['class_in_table'].strip()):
                p.append('%s has no class_in_table' % t)
    except Exception as ex:
        p.append('canonical read failed: %s' % str(ex)[:120])
    s = doc['served']
    try:
        pre = io_.uncl_other(s['bucket'], s['key'], s['pre_version_id'], s['date'])
        post = io_.uncl_other(s['bucket'], s['key'], s['post_version_id'], s['date'])
        if abs(float(s['uncl_other_pre']) - pre) > TOL:
            p.append('uncl_other_pre %s != recomputed %.2f' % (s['uncl_other_pre'], pre))
        if abs(float(s['uncl_other_post']) - post) > TOL:
            p.append('uncl_other_post %s != recomputed %.2f' % (s['uncl_other_post'], post))
    except Exception as ex:
        p.append('served read failed: %s' % str(ex)[:120])
    if not (isinstance(doc['conclusion'], str) and len(doc['conclusion'].strip()) >= 40):
        p.append('conclusion is under 40 characters')
    if not (isinstance(doc['fix'], str) and len(doc['fix'].strip()) >= 20):
        p.append('fix is under 20 characters')
    return p


class Live(object):
    def __init__(self):
        import boto3
        self.s3 = boto3.client('s3', region_name='us-east-1')

    def ticker_mv(self, b, k, v):
        import pandas as pd
        raw = self.s3.get_object(Bucket=b, Key=k, VersionId=v)['Body'].read()
        df = pd.read_parquet(io.BytesIO(raw), columns=['ticker', 'market_value'])
        df = df.assign(T=df['ticker'].astype(str).str.upper())
        g = df.groupby('T')['market_value'].agg(['count', 'sum'])
        return {t: (int(r['count']), float(r['sum'])) for t, r in g.iterrows()}

    def uncl_other(self, b, k, v, date):
        d = json.loads(self.s3.get_object(Bucket=b, Key=k, VersionId=v)['Body'].read())['firm'][date]
        return float(d.get('unclassified', 0.0)) + float(d.get('other', 0.0))


class Stub(object):
    def __init__(self, tm, uo):
        self.tm, self.uo = tm, uo

    def ticker_mv(self, b, k, v):
        return self.tm

    def uncl_other(self, b, k, v, date):
        return self.uo[v]


def selftest():
    tm = {'AAA': (2, 10.5), 'BBB': (1, 3.0)}
    st = Stub(tm, {'p0': 500.0, 'p1': 505.0})
    good = {'first_divergence': 'instrument-expectation', 'canonical': {'bucket': 'b', 'key': 'k', 'version_id': 'v'},
            'tickers': [{'ticker': 'AAA', 'canonical_rows': 2, 'canonical_mv': 10.5, 'class_in_table': 'equity', 'note': ''},
                        {'ticker': 'BBB', 'canonical_rows': 1, 'canonical_mv': 3.0, 'class_in_table': 'fixed_income', 'note': ''}],
            'served': {'bucket': 'b', 'key': 'm', 'pre_version_id': 'p0', 'post_version_id': 'p1', 'date': '2026-10-02', 'uncl_other_pre': 500.0, 'uncl_other_post': 505.0},
            'conclusion': 'c' * 45, 'fix': 'f' * 25}
    ok = True
    pg = grade(good, {'AAA', 'BBB'}, st)
    print('S45-CAUSE-SELFTEST green:', not pg, pg)
    ok &= not pg
    cases = []
    d = json.loads(json.dumps(good))
    d['tickers'].pop()
    cases.append(('a seeded ticker has no entry', d))
    d = json.loads(json.dumps(good))
    d['tickers'][0]['canonical_mv'] = 11.0
    cases.append(('canonical_mv does not reconcile', d))
    d = json.loads(json.dumps(good))
    d['served']['uncl_other_post'] = 9.0
    cases.append(('served number does not reconcile', d))
    d = json.loads(json.dumps(good))
    d['first_divergence'] = 'guess'
    cases.append(('divergence not in the enum', d))
    d = json.loads(json.dumps(good))
    d['fix'] = 'no'
    cases.append(('fix too short', d))
    for name, doc in cases:
        pn = grade(doc, {'AAA', 'BBB'}, st)
        print('S45-CAUSE-SELFTEST negative (%s): %s' % (name, bool(pn)))
        ok &= bool(pn)
    print('S45-CAUSE-SELFTEST ok=%s' % ok)
    return 0 if ok else 1


def read(path):
    if not os.path.isfile(path):
        print('S45-CAUSE ok=False problems=%s' % ['no file at %s' % path])
        return 1
    plan = json.load(open(PLAN, encoding='utf-8'))
    tickers = {e['ticker'].upper() for e in plan['planned']}
    doc = json.load(open(path, encoding='utf-8'))
    pr = grade(doc, tickers, Live())
    print('S45-CAUSE ok=%s problems=%s' % (not pr, pr))
    return 0 if not pr else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['selftest']:
        sys.exit(selftest())
    if a[:1] == ['read']:
        sys.exit(read(a[a.index('--file') + 1] if '--file' in a else DEFAULT))
    raise SystemExit('usage: check_s45_cause.py selftest | read [--file <S45_CAUSE.json>]')
