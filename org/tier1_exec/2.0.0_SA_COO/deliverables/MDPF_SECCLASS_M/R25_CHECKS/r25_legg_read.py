#!/usr/bin/env python
"""Leg G of the SC-e-102 sorted-keys ship (read-only).

Compares every leg P key (E102_LEGP_20261014.json, the pre-ship VersionIds) with the current served object:
  - per family: keys, VersionId moved, canonical-JSON equal (json.dumps sort_keys, compact)
  - per date-keyed object: the dates whose canonical content differs (the fire's re-derived set)
  - key order: the served mix_daily_summary body equals its own sorted dump
  - D_04 mix_summary: sum of class market values in file order vs composition.total_market_value, pre and post

Usage: python r25_legg_read.py read [--out DIR]
Prints LEGG-* lines; the verdict is the reader's, against the clauses in the COO half item 4.
"""
import json
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), *(['..'] * 6)))
LEGP = os.path.join(ROOT, 'org', 'tier2_senior', '0.7.0_AE_CloudOps~SC1', 'deliverables', 'E102_LEGP_20261014.json')
AWS = os.path.join(ROOT, '.tools', 'aws')


def canon(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'))


def fetch(bucket_key, vid, path):
    b, k = bucket_key.split('/', 1)
    a = [AWS, 's3api', 'get-object', '--bucket', b, '--key', k, path]
    if vid:
        a += ['--version-id', vid]
    r = subprocess.run(a, capture_output=True, text=True, shell=(sys.platform == 'win32'))
    if r.returncode != 0:
        raise SystemExit('ERROR: get-object %s rc=%s %s' % (k, r.returncode, r.stderr[-300:]))
    meta = json.loads(r.stdout)
    with open(path, 'rb') as f:
        raw = f.read()
    return meta, raw


def dated_diff(a, b):
    """Dates (top-level keys) whose canonical content differs."""
    return sorted(k for k in set(a) | set(b) if canon(a.get(k)) != canon(b.get(k)))


def main():
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.join(os.environ.get('TMP', '/tmp'), 'legg')
    os.makedirs(out, exist_ok=True)
    keys = json.load(open(LEGP, encoding='utf-8'))['keys']
    fam = {}
    bodies = {}
    rows = []
    for k, v in sorted(keys.items()):
        pre_meta, pre = fetch(k, v['VersionId'], os.path.join(out, 'pre.bin'))
        post_meta, post = fetch(k, None, os.path.join(out, 'post.bin'))
        moved = post_meta.get('VersionId') != v['VersionId']
        pj, qj = json.loads(pre), json.loads(post)
        eq = canon(pj) == canon(qj)
        f = fam.setdefault(v['family'], {'keys': 0, 'moved': 0, 'canon_equal': 0, 'sorted_now': 0})
        f['keys'] += 1
        f['moved'] += int(moved)
        f['canon_equal'] += int(eq)
        f['sorted_now'] += int(post == json.dumps(qj, sort_keys=True, separators=(',', ':')).encode('utf-8'))
        rows.append((k, v['family'], moved, eq, pj, qj))
        if v['family'] in ('mix_daily_summary', 'firm_mix_summary', 'firm_mix_views_daily'):
            bodies[v['family']] = (pj, qj)
    for name, f in sorted(fam.items()):
        print('LEGG-FAMILY %s keys=%d moved=%d canon_equal=%d sorted_bytes_now=%d' % (name, f['keys'], f['moved'], f['canon_equal'], f['sorted_now']))

    pj, qj = bodies['mix_daily_summary']
    fd = dated_diff(pj['firm'], qj['firm'])
    ad = {}
    for i in sorted(set(pj['advisors']) | set(qj['advisors'])):
        x, y = pj['advisors'].get(i) or {}, qj['advisors'].get(i) or {}
        d = dated_diff(x, y) if isinstance(x, dict) and isinstance(y, dict) else ['<non-dict>']
        if d:
            ad[i] = d
    print('LEGG-DATES firm n=%d of %d differing=%s' % (len(fd), len(qj['firm']), fd))
    print('LEGG-DATES mix_daily_summary advisors differing=%d of %d, union of dates=%s' % (len(ad), len(qj['advisors']), sorted({d for v in ad.values() for d in v})))
    print('LEGG-DATES restated_through pre=%s post=%s' % (pj.get('restated_through'), qj.get('restated_through')))
    pf, qf = bodies['firm_mix_views_daily']
    print('LEGG-DATES firm_mix_views_daily n=%d of %d differing=%s' % (len(dated_diff(pf, qf)), len(qf), dated_diff(pf, qf)))
    for name, label in (('advisor_mix_daily', 'advisor mix_daily'),):
        mv = [(k, d) for (k, fam_, m, eq, a, b) in rows if fam_ == name and not eq
              for d in [dated_diff(a, b) if isinstance(a, dict) and isinstance(b, dict) else ['<non-dict>']]]
        print('LEGG-DATES %s files not canon-equal=%d, union of dates=%s' % (label, len(mv), sorted({x for _, d in mv for x in d})))

    unmoved = sorted(k.split('/')[-2] for (k, fam_, m, eq, a, b) in rows if fam_ == 'advisor_mix_daily' and not m)
    in_summary = set(qj['advisors'])
    print('LEGG-STALE advisor mix_daily files with no new VersionId=%d: %s; of these absent from the served summary: %s' % (
        len(unmoved), unmoved, [i for i in unmoved if i not in in_summary]))

    # D_04 (lines 544-561): composition.total_market_value = round(sum of C_06's classes at max(firm date), file order, 2).
    # The recompute below sums the SAME dict in the SAME (file) order. pre = insertion order, post = sorted order.
    ps, qs = bodies['firm_mix_summary']
    for tag, body, mds in (('pre', ps, pj), ('post', qs, qj)):
        latest = max(mds['firm'])
        snap = mds['firm'][latest]
        s = 0.0
        for k2, v2 in snap.items():
            if k2 != 'total' and v2 is not None:
                s += v2
        tot = body['composition']['total_market_value']
        print('LEGG-D04 %s generated_at=%s c06_date=%s key_order=%s recompute=%.6f round2=%.2f served_total=%.2f diff=%.6f ok=%s' % (
            tag, body['generated_at'], latest, list(snap), s, round(s, 2), tot, round(s, 2) - tot, abs(round(s, 2) - tot) <= 0.000001))


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] != 'read':
        raise SystemExit('usage: r25_legg_read.py read [--out DIR]')
    main()
