#!/usr/bin/env python
"""R29 acceptance for the four READ cells of MDPF_SECCLASS round 29 (READ-ONLY). One mode per cell; each recomputes what it can from the served objects.

Usage (repo root):
  python check_r29_reads.py selftest
  python check_r29_reads.py e18-line  [--file <E18_FIRE_LINE.json>]      SC-e-112  (worker ~101)
  python check_r29_reads.py calendar  [--file <D1016_ABSENCE.json>]      SC-e-113  (worker ~102)
  python check_r29_reads.py s48-range [--file <S48_RANGE_RECON.json>]    SC-e-114  (worker ~103)
  python check_r29_reads.py partners  [--file <PARTNERS_MAP.json>]       SC-e-115  (worker ~104)
Prints `R29-<MODE> ok=<bool> problems=<list>`; exit 0 ok, 1 not ok. A missing file is a failed check, never a pass.
"""
import datetime as dt
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, *(['..'] * 6)))
DELIV = os.path.join(ROOT, 'org', 'missions', 'D8', 'MDPF', 'MDPF_SECCLASS', 'deliverables')
DEFAULTS = {
    'e18-line': os.path.join(DELIV, '0.9.0_WK_MDPF_SECCLASS~101', 'E18_FIRE_LINE.json'),
    'calendar': os.path.join(DELIV, '0.9.0_WK_MDPF_SECCLASS~102', 'D1016_ABSENCE.json'),
    's48-range': os.path.join(DELIV, '0.9.0_WK_MDPF_SECCLASS~103', 'S48_RANGE_RECON.json'),
    'partners': os.path.join(DELIV, '0.9.0_WK_MDPF_SECCLASS~104', 'PARTNERS_MAP.json'),
}
GOLD = os.path.join(ROOT, 'data', 'black_diamond', 'scripts', 'gold')
MIX_KEY = 'advi/49financial/platinum/views/mix_daily_summary.json'
TOL = 0.01
UTC = dt.timezone.utc


def _need(doc, keys, p):
    if not isinstance(doc, dict):
        p.append('document is not an object')
        return False
    for k in keys:
        if k not in doc:
            p.append('missing key %s' % k)
    return not any(x.startswith('missing key') for x in p)


def grade_e18_line(doc, io_):
    """io_.log_text(src)->(text, last_modified_utc)."""
    p = []
    if not _need(doc, ('source', 'line', 'candidates', 'already_resolved', 'written', 'refused'), p):
        return p
    try:
        text, lm = io_.log_text(doc['source'])
    except Exception as e:
        return ['source read failed: %s' % str(e)[:120]]
    lo = dt.datetime(2026, 10, 18, 0, 4, 0, tzinfo=UTC)
    hi = dt.datetime(2026, 10, 18, 3, 0, 0, tzinfo=UTC)
    if not lo <= lm <= hi:
        p.append('source time %s is outside the 23:00Z fire window (%s to %s)' % (lm.isoformat(), lo.isoformat(), hi.isoformat()))
    if not (isinstance(doc['line'], str) and doc['line'].strip() and doc['line'] in text):
        p.append('line is not found in the source')
    m = re.search(r'candidates:\s*([\d,]+)', doc['line'] if isinstance(doc['line'], str) else '')
    if not m:
        p.append("line carries no 'candidates: <n>' figure")
    elif int(m.group(1).replace(',', '')) != int(doc['candidates']):
        p.append('candidates %s does not equal the figure in the line' % doc['candidates'])
    return p


def grade_calendar(doc, io_):
    """io_.served_dates(bucket,key,vid)->(sorted dates, last_modified_utc); io_.frontier(lm)->date str; io_.script_exists(name)."""
    p = []
    if not _need(doc, ('served', 'tail_date', 'missing_date', 'frontier_date', 'producer_step', 'reason'), p):
        return p
    s = doc['served']
    try:
        dates, lm = io_.served_dates(s['bucket'], s['key'], s['version_id'])
        if dates[-1] != doc['tail_date']:
            p.append('tail_date %s != recomputed %s' % (doc['tail_date'], dates[-1]))
        if doc['missing_date'] in dates:
            p.append('missing_date %s is present in the served version' % doc['missing_date'])
        fr = io_.frontier(lm)
        if fr != doc['frontier_date']:
            p.append('frontier_date %s != trading_calendar %s' % (doc['frontier_date'], fr))
        if doc['missing_date'] > fr:
            p.append('missing_date is after the frontier: it is not expected to exist')
    except Exception as e:
        p.append('served read failed: %s' % str(e)[:120])
    if not (isinstance(doc['producer_step'], str) and io_.script_exists(doc['producer_step'])):
        p.append('producer_step %r is not a file under the gold scripts folder' % (doc['producer_step'],))
    if not (isinstance(doc['reason'], str) and len(doc['reason'].strip()) >= 40):
        p.append('reason is under 40 characters')
    return p


def grade_s48_range(doc, io_):
    """io_.served_total(bucket,key,vid,date)->float; io_.canonical_total(bucket,key,vid)->float."""
    p = []
    if not _need(doc, ('served', 'canonical', 'rows', 'summary'), p):
        return p
    sv = doc['served']
    cn = doc['canonical']
    rows = {r.get('date'): r for r in doc['rows'] if isinstance(r, dict)}
    expect = ['2026-10-%02d' % d for d in range(1, 15)]
    for d in expect:
        r = rows.get(d)
        if r is None:
            p.append('date %s has no row' % d)
            continue
        try:
            sd = io_.served_total(sv['bucket'], sv['key'], sv['post_version_id'], d) - io_.served_total(sv['bucket'], sv['key'], sv['pre_version_id'], d)
            c = cn['dates'][d]
            cd = io_.canonical_total(cn['bucket'], c['key'], c['after_version_id']) - io_.canonical_total(cn['bucket'], c['key'], c['before_version_id'])
            if abs(sd - float(r['served_delta'])) > TOL:
                p.append('%s served_delta %s != recomputed %.2f' % (d, r['served_delta'], sd))
            if abs(cd - float(r['canonical_delta'])) > TOL:
                p.append('%s canonical_delta %s != recomputed %.2f' % (d, r['canonical_delta'], cd))
            if abs((sd - cd) - float(r['residue'])) > TOL:
                p.append('%s residue %s != served minus canonical %.2f' % (d, r['residue'], sd - cd))
        except Exception as e:
            p.append('%s read failed: %s' % (d, str(e)[:100]))
    if not (isinstance(doc['summary'], str) and len(doc['summary'].strip()) >= 40):
        p.append('summary is under 40 characters')
    return p


def grade_partners(doc, io_):
    """io_.path_exists(rel)->bool; io_.line_text(rel,line)->str; io_.lambda_sha(name,region)->str."""
    p = []
    if not _need(doc, ('lambda', 'repo_paths', 'classifier_path', 'call_sites', 'class_handling', 'contract'), p):
        return p
    lam = doc['lambda']
    try:
        sha = io_.lambda_sha(lam['name'], lam.get('region', 'us-east-1'))
        if sha != lam.get('code_sha256'):
            p.append('lambda code_sha256 %s != live %s' % (lam.get('code_sha256'), sha))
    except Exception as e:
        p.append('lambda read failed: %s' % str(e)[:120])
    if not (isinstance(doc['repo_paths'], list) and doc['repo_paths']):
        p.append('repo_paths is empty: the code is not located')
    else:
        for r in doc['repo_paths']:
            if not io_.path_exists(r):
                p.append('repo path %s does not exist at HEAD' % r)
    if not io_.path_exists(doc['classifier_path']):
        p.append('classifier_path %s does not exist at HEAD' % doc['classifier_path'])
    if not (isinstance(doc['call_sites'], list) and doc['call_sites']):
        p.append('call_sites is empty')
    else:
        for c in doc['call_sites']:
            try:
                if c['text'].strip() not in io_.line_text(c['path'], int(c['line'])):
                    p.append('call site %s:%s does not hold the quoted text' % (c['path'], c['line']))
            except Exception as e:
                p.append('call site read failed: %s' % str(e)[:100])
    if not (isinstance(doc['class_handling'], str) and len(doc['class_handling'].strip()) >= 60):
        p.append('class_handling is under 60 characters')
    if not (isinstance(doc['contract'], dict) and doc['contract'].get('returns')):
        p.append('contract.returns is empty')
    return p


GRADERS = {'e18-line': grade_e18_line, 'calendar': grade_calendar, 's48-range': grade_s48_range, 'partners': grade_partners}


class Live(object):
    def __init__(self):
        import boto3
        self.s3 = boto3.client('s3', region_name='us-east-1')
        self.boto3 = boto3

    def log_text(self, src):
        if src.get('type') == 's3':
            kw = {'Bucket': src['bucket'], 'Key': src['key']}
            if src.get('version_id'):
                kw['VersionId'] = src['version_id']
            o = self.s3.get_object(**kw)
            return o['Body'].read().decode('utf-8', 'replace'), o['LastModified']
        logs = self.boto3.client('logs', region_name='us-east-1')
        msgs, last = [], None
        kw = {'logGroupName': src['log_group'], 'startTime': int(src['start_ms']), 'endTime': int(src['end_ms'])}
        if src.get('log_stream'):
            kw['logStreamNames'] = [src['log_stream']]
        for pg in logs.get_paginator('filter_log_events').paginate(**kw):
            for ev in pg['events']:
                msgs.append(ev['message'])
                last = dt.datetime.fromtimestamp(ev['timestamp'] / 1000.0, UTC)
        if last is None:
            raise RuntimeError('no log events in the window')
        return '\n'.join(msgs), last

    def served_dates(self, b, k, v):
        o = self.s3.get_object(Bucket=b, Key=k, VersionId=v)
        return sorted(json.loads(o['Body'].read())['firm']), o['LastModified']

    def frontier(self, lm):
        sys.path.insert(0, ROOT)
        from lib import trading_calendar as tc
        return str(tc.expected_last_trading_day(lm.astimezone(UTC).replace(tzinfo=None)))

    def served_total(self, b, k, v, d):
        if not hasattr(self, '_cache'):
            self._cache = {}
        if (b, k, v) not in self._cache:
            self._cache[(b, k, v)] = json.loads(self.s3.get_object(Bucket=b, Key=k, VersionId=v)['Body'].read())['firm']
        return float(self._cache[(b, k, v)][d]['total'])

    def canonical_total(self, b, k, v):
        import pandas as pd
        raw = self.s3.get_object(Bucket=b, Key=k, VersionId=v)['Body'].read()
        return float(pd.read_parquet(io.BytesIO(raw), columns=['market_value'])['market_value'].sum())

    def script_exists(self, name):
        return os.path.isfile(os.path.join(GOLD, os.path.basename(name)))

    def path_exists(self, rel):
        return os.path.exists(os.path.join(ROOT, rel))

    def line_text(self, rel, line):
        return open(os.path.join(ROOT, rel), encoding='utf-8', errors='replace').read().split('\n')[line - 1]

    def lambda_sha(self, name, region):
        return self.boto3.client('lambda', region_name=region).get_function_configuration(FunctionName=name)['CodeSha256']


class Stub(object):
    def log_text(self, src):
        return 'x Scheduled-classification candidates:      0 y', dt.datetime(2026, 10, 18, 0, 5, 9, tzinfo=UTC)

    def served_dates(self, b, k, v):
        return ['2026-10-14', '2026-10-15'], dt.datetime(2026, 10, 18, 0, 24, 42, tzinfo=UTC)

    def frontier(self, lm):
        return '2026-10-16'

    def served_total(self, b, k, v, d):
        return {'a': 100.0, 'b': 160.0}[v]

    def canonical_total(self, b, k, v):
        return {'c': 10.0, 'd': 70.0}[v]

    def script_exists(self, n):
        return n == 'B_00.canonical_holdings.py'

    def path_exists(self, rel):
        return rel.startswith('ok/')

    def line_text(self, rel, line):
        return '    classifier = ETFClassifier()'

    def lambda_sha(self, name, region):
        return 'SHA1'


def _selftest_cases():
    e18 = {'source': {'type': 's3'}, 'line': 'Scheduled-classification candidates:      0', 'candidates': 0, 'already_resolved': 9, 'written': 0, 'refused': 0}
    cal = {'served': {'bucket': 'b', 'key': 'k', 'version_id': 'v'}, 'tail_date': '2026-10-15', 'missing_date': '2026-10-16', 'frontier_date': '2026-10-16',
           'producer_step': 'B_00.canonical_holdings.py', 'reason': 'r' * 45}
    rows = [{'date': '2026-10-%02d' % d, 'served_delta': 60.0, 'canonical_delta': 60.0, 'residue': 0.0} for d in range(1, 15)]
    cdates = {'2026-10-%02d' % d: {'key': 'k', 'before_version_id': 'c', 'after_version_id': 'd'} for d in range(1, 15)}
    rng = {'served': {'bucket': 'b', 'key': 'm', 'pre_version_id': 'a', 'post_version_id': 'b'}, 'canonical': {'bucket': 'b', 'dates': cdates}, 'rows': rows, 'summary': 's' * 45}
    par = {'lambda': {'name': 'f', 'region': 'us-east-1', 'code_sha256': 'SHA1'}, 'repo_paths': ['ok/a.py'], 'classifier_path': 'ok/a.py',
           'call_sites': [{'path': 'ok/a.py', 'line': 3, 'text': 'classifier = ETFClassifier()'}], 'class_handling': 'c' * 65, 'contract': {'returns': ['equity']}}
    import copy

    def mut(d, f):
        e = copy.deepcopy(d)
        f(e)
        return e
    return [
        ('e18-line', e18, [('line not in the source', mut(e18, lambda e: e.update(line='nope'))), ('candidates differ', mut(e18, lambda e: e.update(candidates=3)))]),
        ('calendar', cal, [('missing date present', mut(cal, lambda e: e.update(missing_date='2026-10-15'))), ('wrong frontier', mut(cal, lambda e: e.update(frontier_date='2026-10-15'))),
                           ('not a gold script', mut(cal, lambda e: e.update(producer_step='X.py')))]),
        ('s48-range', rng, [('a date has no row', mut(rng, lambda e: e['rows'].pop())), ('residue wrong', mut(rng, lambda e: e['rows'][0].update(residue=5.0)))]),
        ('partners', par, [('repo path missing', mut(par, lambda e: e['repo_paths'].append('no/b.py'))), ('wrong sha', mut(par, lambda e: e['lambda'].update(code_sha256='X'))),
                           ('call site text differs', mut(par, lambda e: e['call_sites'][0].update(text='something else')))]),
    ]


def selftest():
    ok = True
    st = Stub()
    for mode, good, negs in _selftest_cases():
        pg = GRADERS[mode](good, st)
        print('R29-%s-SELFTEST green: %s %s' % (mode, not pg, pg))
        ok &= not pg
        for name, doc in negs:
            pn = GRADERS[mode](doc, st)
            print('R29-%s-SELFTEST negative (%s): %s' % (mode, name, bool(pn)))
            ok &= bool(pn)
    print('R29-SELFTEST ok=%s' % ok)
    return 0 if ok else 1


def read(mode, path):
    if not os.path.isfile(path):
        print('R29-%s ok=False problems=%s' % (mode, ['no file at %s' % path]))
        return 1
    doc = json.load(open(path, encoding='utf-8'))
    pr = GRADERS[mode](doc, Live())
    print('R29-%s ok=%s problems=%s' % (mode, not pr, pr))
    return 0 if not pr else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['selftest']:
        sys.exit(selftest())
    if a and a[0] in GRADERS:
        sys.exit(read(a[0], a[a.index('--file') + 1] if '--file' in a else DEFAULTS[a[0]]))
    raise SystemExit('usage: check_r29_reads.py selftest | e18-line|calendar|s48-range|partners [--file <json>]')
