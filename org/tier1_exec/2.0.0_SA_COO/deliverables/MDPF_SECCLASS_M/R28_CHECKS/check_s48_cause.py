#!/usr/bin/env python
"""R28 SC-e-109 acceptance (READ-ONLY): does S48_CAUSE.json name the input that moved between the 23:00Z and 04:00Z 2026-10 fires, its writer, and
does the named delta reconcile to the served objects?

Usage (repo root):
  python check_s48_cause.py selftest
  python check_s48_cause.py read [--file <S48_CAUSE.json>]

The worker writes S48_CAUSE.json (default path below). Required keys:
  writer               a gold script file name that exists under data/black_diamond/scripts/gold/ (for example B_00.canonical_holdings.py)
  moved_key            {bucket, key, date, before_version_id, after_version_id}: ONE canonical-holdings object, two versions
  delta_total          after minus before of sum(market_value) for that object (the checker recomputes it)
  upstream             non-empty list of {bucket, key, version_before, version_after}: the writer's input objects that changed
  why                  at least 40 characters
  verdict              RIGHT | WRONG (the TOTAL rise on 2026-10-01..10-14 is the intended behaviour, or it is not)
Every claim the checker can recompute it recomputes from S3; the rest it checks for presence and type.
Prints `S48-CAUSE ok=<bool> problems=<list>`; exit 0 ok, 1 not ok.
"""
import datetime as dt
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, *(['..'] * 6)))
DEFAULT = os.path.join(ROOT, 'org', 'missions', 'D8', 'MDPF', 'MDPF_SECCLASS', 'deliverables', '0.9.0_WK_MDPF_SECCLASS~99', 'S48_CAUSE.json')
GOLD = os.path.join(ROOT, 'data', 'black_diamond', 'scripts', 'gold')
FIRE1 = dt.datetime(2026, 10, 16, 23, 15, 29, tzinfo=dt.timezone.utc)   # the 23:00Z fire's canonical-holdings rewrite
FIRE2 = dt.datetime(2026, 10, 17, 4, 16, 5, tzinfo=dt.timezone.utc)     # the 04:00Z fire's canonical-holdings rewrite
TOL = 0.01


def grade(doc, io_):
    """doc: parsed S48_CAUSE.json. io_: object with head(bucket,key,vid)->aware datetime, total(bucket,key,vid)->float, script_exists(name)->bool."""
    p = []
    if not isinstance(doc, dict):
        return ['document is not an object']
    for k in ('writer', 'moved_key', 'delta_total', 'upstream', 'why', 'verdict'):
        if k not in doc:
            p.append('missing key %s' % k)
    if p:
        return p
    if not (isinstance(doc['writer'], str) and io_.script_exists(doc['writer'])):
        p.append('writer %r is not a file under the gold scripts folder' % (doc['writer'],))
    mk = doc['moved_key']
    for k in ('bucket', 'key', 'date', 'before_version_id', 'after_version_id'):
        if not (isinstance(mk, dict) and mk.get(k)):
            p.append('moved_key.%s missing' % k)
    if not p:
        try:
            tb = io_.head(mk['bucket'], mk['key'], mk['before_version_id'])
            ta = io_.head(mk['bucket'], mk['key'], mk['after_version_id'])
            if not tb < FIRE1 + dt.timedelta(minutes=5):
                p.append('before version %s is not from the 23:00Z fire or earlier' % tb.isoformat())
            if not ta > FIRE2 - dt.timedelta(minutes=30):
                p.append('after version %s is not from the 04:00Z fire' % ta.isoformat())
            d = io_.total(mk['bucket'], mk['key'], mk['after_version_id']) - io_.total(mk['bucket'], mk['key'], mk['before_version_id'])
            if abs(d - float(doc['delta_total'])) > TOL:
                p.append('delta_total %.2f does not equal the recomputed %.2f' % (float(doc['delta_total']), d))
            if d <= 0:
                p.append('recomputed delta %.2f is not a rise' % d)
        except Exception as e:  # a read that fails is a failed check, never a pass
            p.append('moved_key read failed: %s' % str(e)[:120])
    up = doc['upstream']
    if not (isinstance(up, list) and up):
        p.append('upstream is empty: the writer input that changed is not named')
    else:
        for i, u in enumerate(up):
            try:
                vb = io_.head(u['bucket'], u['key'], u['version_before'])
                va = io_.head(u['bucket'], u['key'], u['version_after'])
                if not (vb <= FIRE1 and FIRE1 < va <= FIRE2):
                    p.append('upstream[%d] %s: before %s / after %s do not straddle the window (%s, %s]' % (i, u['key'], vb.isoformat(), va.isoformat(), FIRE1.isoformat(), FIRE2.isoformat()))
            except Exception as e:
                p.append('upstream[%d] read failed: %s' % (i, str(e)[:120]))
    if not (isinstance(doc['why'], str) and len(doc['why'].strip()) >= 40):
        p.append('why is under 40 characters')
    if doc['verdict'] not in ('RIGHT', 'WRONG'):
        p.append('verdict must be RIGHT or WRONG, got %r' % (doc['verdict'],))
    return p


class Live(object):
    def __init__(self):
        import boto3
        self.s3 = boto3.client('s3', region_name='us-east-1')

    def head(self, b, k, v):
        return self.s3.head_object(Bucket=b, Key=k, VersionId=v)['LastModified']

    def total(self, b, k, v):
        import pandas as pd
        raw = self.s3.get_object(Bucket=b, Key=k, VersionId=v)['Body'].read()
        return float(pd.read_parquet(io.BytesIO(raw), columns=['market_value'])['market_value'].sum())

    def script_exists(self, name):
        return os.path.isfile(os.path.join(GOLD, os.path.basename(name)))


class Stub(object):
    def __init__(self, heads, totals, scripts):
        self.h, self.t, self.s = heads, totals, scripts

    def head(self, b, k, v):
        return self.h[(b, k, v)]

    def total(self, b, k, v):
        return self.t[(b, k, v)]

    def script_exists(self, n):
        return n in self.s


def selftest():
    u = dt.timezone.utc
    heads = {('b', 'k', 'v0'): dt.datetime(2026, 10, 16, 23, 15, 29, tzinfo=u), ('b', 'k', 'v1'): dt.datetime(2026, 10, 17, 4, 16, 5, tzinfo=u),
             ('b', 'up', 'u0'): dt.datetime(2026, 10, 10, 1, 0, 0, tzinfo=u), ('b', 'up', 'u1'): dt.datetime(2026, 10, 17, 3, 30, 0, tzinfo=u),
             ('b', 'up', 'u2'): dt.datetime(2026, 10, 10, 2, 0, 0, tzinfo=u)}
    totals = {('b', 'k', 'v0'): 100.0, ('b', 'k', 'v1'): 150.5}
    st = Stub(heads, totals, {'B_00.canonical_holdings.py'})
    good = {'writer': 'B_00.canonical_holdings.py', 'moved_key': {'bucket': 'b', 'key': 'k', 'date': '2026-10-02', 'before_version_id': 'v0', 'after_version_id': 'v1'},
            'delta_total': 50.5, 'upstream': [{'bucket': 'b', 'key': 'up', 'version_before': 'u0', 'version_after': 'u1'}],
            'why': 'x' * 45, 'verdict': 'RIGHT'}
    ok = True
    pg = grade(good, st)
    print('S48-CAUSE-SELFTEST green:', not pg, pg)
    ok &= not pg
    neg = []
    d = json.loads(json.dumps(good))
    d['upstream'] = []
    neg.append(('empty upstream', d))
    d = json.loads(json.dumps(good))
    d['delta_total'] = 51.0
    neg.append(('delta does not reconcile', d))
    d = json.loads(json.dumps(good))
    d['upstream'][0]['version_before'] = 'u2'
    d['upstream'][0]['version_after'] = 'u0'
    neg.append(('upstream does not straddle the window', d))
    d = json.loads(json.dumps(good))
    d['writer'] = 'NOPE.py'
    neg.append(('writer is not a gold script', d))
    d = json.loads(json.dumps(good))
    d['verdict'] = 'UNDETERMINED'
    neg.append(('verdict undetermined', d))
    d = json.loads(json.dumps(good))
    del d['why']
    neg.append(('why missing', d))
    for name, doc in neg:
        pn = grade(doc, st)
        print('S48-CAUSE-SELFTEST negative (%s): %s' % (name, bool(pn)))
        ok &= bool(pn)
    print('S48-CAUSE-SELFTEST ok=%s' % ok)
    return 0 if ok else 1


def read(path):
    if not os.path.isfile(path):
        print('S48-CAUSE ok=False problems=%s' % ['no file at %s' % path])
        return 1
    doc = json.load(open(path, encoding='utf-8'))
    pr = grade(doc, Live())
    print('S48-CAUSE ok=%s problems=%s' % (not pr, pr))
    return 0 if not pr else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['selftest']:
        sys.exit(selftest())
    if a[:1] == ['read']:
        sys.exit(read(a[a.index('--file') + 1] if '--file' in a else DEFAULT))
    raise SystemExit('usage: check_s48_cause.py selftest | read [--file <S48_CAUSE.json>]')
