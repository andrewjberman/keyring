#!/usr/bin/env python
"""Leg G of the 13-row seed (READ-ONLY): after the first scheduled fire that follows the seed, did the seeded tickers' dollars move
out of Unclassified into the ruled classes, and nothing else?

Usage (repo root):
  python seed22_legg_read.py selftest
  python seed22_legg_read.py read --pre-version-id <VersionId of mix_daily_summary.json read at the seed's leg P> [--tol 250]

For every firm date in the window the fire re-derived (dates >= the served `restated_through`) where C_06's firm class dollars differ
between the pre-seed version and the latest, the expected move is computed from the open lots of that date (s3://opal-data-bd/gold/holdings_lots/<date>.parquet):
+ the dollars of each SEEDED ticker (SEED22_PLAN.json `planned`) in its ruled class, - the same total out of `unclassified` + `other`. Each class is graded within
--tol dollars (the code's own share-rounding bound is $250; the exact deltas are printed). The 9 held-out tickers must stay inside `unclassified` + `other` (the post
value of those two is at least their dollars). Dates in the window where the lots hold a seeded ticker but the firm values did not move are reported NOT-MOVED.
Prints `SEED22-LEGG date=...` lines and `SEED22-LEGG ok=<bool> window_dates=<n> moved=<m> bad=<k>`; exit 0 ok, 1 not ok.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, *(['..'] * 6)))
PLAN = os.path.join(ROOT, 'org', 'missions', 'D8', 'MDPF', 'MDPF_SECCLASS', 'deliverables', '0.9.0_WK_MDPF_SECCLASS~97', 'SEED22_PLAN.json')
BUCKET_SERVED = 'opal-data-49financial'
KEY_MDS = 'advi/49financial/platinum/views/mix_daily_summary.json'
BUCKET_LOTS = 'opal-data-bd'
UNCL = ('unclassified', 'other')


def grade(pre, post, plan, lots_mv, tol=250.0):
    """pre/post: parsed mix_daily_summary bodies. lots_mv(date) -> {ticker: market_value} for open lots. Returns (lines, ok, window, moved, bad)."""
    target = {e['ticker']: e['row']['asset_class'] for e in plan['planned']}
    held = {e['ticker'] for e in plan['seed_pending']}
    rt = post.get('restated_through') or ''
    classes = sorted({k for d in post['firm'].values() for k in d if k != 'total'})
    lines, bad, moved, window = [], 0, 0, 0
    for d in sorted(post['firm']):
        if d < rt or d not in pre['firm']:
            continue
        window += 1
        mv = lots_mv(d)
        exp = {c: 0.0 for c in classes}
        seeded_total = 0.0
        for t, ac in target.items():
            v = float(mv.get(t, 0.0))
            if v:
                exp[ac] = exp.get(ac, 0.0) + v
                seeded_total += v
        held_total = sum(float(mv.get(t, 0.0)) for t in held)
        delta = {c: float(post['firm'][d].get(c, 0.0)) - float(pre['firm'][d].get(c, 0.0)) for c in classes}
        any_move = any(abs(v) > 0.005 for v in delta.values())
        if seeded_total == 0 and not any_move:
            continue
        if seeded_total > 0 and not any_move:
            lines.append('SEED22-LEGG date=%s NOT-MOVED seeded_dollars=%.2f' % (d, seeded_total))
            bad += 1
            continue
        moved += 1
        problems = []
        for c in classes:
            if c in UNCL:
                continue
            if abs(delta[c] - exp.get(c, 0.0)) > tol:
                problems.append('%s delta=%.2f exp=%.2f' % (c, delta[c], exp.get(c, 0.0)))
        out = delta.get('unclassified', 0.0) + delta.get('other', 0.0)
        if abs(out + seeded_total) > tol:
            problems.append('unclassified+other delta=%.2f exp=%.2f' % (out, -seeded_total))
        left = float(post['firm'][d].get('unclassified', 0.0)) + float(post['firm'][d].get('other', 0.0))
        if left + tol < held_total:
            problems.append('held-out %.2f exceeds unclassified+other %.2f' % (held_total, left))
        lines.append('SEED22-LEGG date=%s ok=%s seeded=%.2f held_out=%.2f %s' % (d, not problems, seeded_total, held_total, problems))
        bad += int(bool(problems))
    return lines, bad == 0 and window > 0, window, moved, bad


def selftest():
    plan = {'planned': [{'ticker': 'AAA', 'row': {'asset_class': 'equity'}}, {'ticker': 'BBB', 'row': {'asset_class': 'commodities'}}],
            'seed_pending': [{'ticker': 'HHH'}]}
    pre = {'restated_through': '2026-10-02', 'firm': {'2026-10-01': {'equity': 10.0, 'commodities': 0.0, 'unclassified': 500.0, 'other': 0.0, 'total': 510.0},
                                                     '2026-10-02': {'equity': 10.0, 'commodities': 0.0, 'unclassified': 500.0, 'other': 0.0, 'total': 510.0}}}
    post = json.loads(json.dumps(pre))
    post['firm']['2026-10-02'].update({'equity': 110.0, 'commodities': 40.0, 'unclassified': 360.0})
    mv = {'AAA': 100.0, 'BBB': 40.0, 'HHH': 300.0}
    ok = True
    lines, good, w, m, b = grade(pre, post, plan, lambda d: mv, tol=1.0)
    print('SEED22-LEGG-SELFTEST green:', good, w, m, b)
    ok &= good and w == 1 and m == 1
    neg = json.loads(json.dumps(post))
    neg['firm']['2026-10-02']['commodities'] = 0.0
    lines, good, *_ = grade(pre, neg, plan, lambda d: mv, tol=1.0)
    print('SEED22-LEGG-SELFTEST negative (a class did not move):', not good)
    ok &= not good
    nm = json.loads(json.dumps(pre))
    lines, good, *_ = grade(pre, nm, plan, lambda d: mv, tol=1.0)
    print('SEED22-LEGG-SELFTEST negative (nothing moved):', not good, lines)
    ok &= (not good) and 'NOT-MOVED' in lines[0]
    hh = json.loads(json.dumps(post))
    hh['firm']['2026-10-02']['unclassified'] = 10.0
    lines, good, *_ = grade(pre, hh, plan, lambda d: mv, tol=1.0)
    print('SEED22-LEGG-SELFTEST negative (held-out dollars gone):', not good)
    ok &= not good
    print('SEED22-LEGG-SELFTEST ok=%s' % ok)
    return 0 if ok else 1


def read(pre_vid, tol):
    import boto3
    import pandas as pd
    s3 = boto3.client('s3', region_name='us-east-1')
    pre = json.loads(s3.get_object(Bucket=BUCKET_SERVED, Key=KEY_MDS, VersionId=pre_vid)['Body'].read())
    post = json.loads(s3.get_object(Bucket=BUCKET_SERVED, Key=KEY_MDS)['Body'].read())
    plan = json.load(open(PLAN, encoding='utf-8'))
    tick = {e['ticker'] for e in plan['planned']} | {e['ticker'] for e in plan['seed_pending']}
    cache = {}

    def lots_mv(d):
        if d not in cache:
            try:
                raw = s3.get_object(Bucket=BUCKET_LOTS, Key='gold/holdings_lots/%s.parquet' % d)['Body'].read()
                df = pd.read_parquet(io.BytesIO(raw), columns=['ticker', 'market_value', 'is_open'])
                df = df[(df['is_open'] == True) & df['ticker'].astype(str).str.upper().isin(tick)]  # noqa: E712
                cache[d] = df.assign(t=df['ticker'].astype(str).str.upper()).groupby('t')['market_value'].sum().to_dict()
            except Exception as e:
                print('SEED22-LEGG date=%s lots-unreadable %s' % (d, str(e)[:80]))
                cache[d] = {}
        return cache[d]

    print('SEED22-LEGG pre=%s post_restated_through=%s pre_dates=%d post_dates=%d' % (pre_vid, post.get('restated_through'), len(pre['firm']), len(post['firm'])))
    lines, ok, window, moved, bad = grade(pre, post, plan, lots_mv, tol)
    for ln in lines:
        print(ln)
    print('SEED22-LEGG ok=%s window_dates=%d moved=%d bad=%d tol=%.0f' % (ok, window, moved, bad, tol))
    return 0 if ok else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['selftest']:
        sys.exit(selftest())
    if a[:1] == ['read'] and '--pre-version-id' in a:
        tol = float(a[a.index('--tol') + 1]) if '--tol' in a else 250.0
        sys.exit(read(a[a.index('--pre-version-id') + 1], tol))
    raise SystemExit('usage: seed22_legg_read.py selftest | read --pre-version-id <VersionId> [--tol 250]')
