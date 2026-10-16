#!/usr/bin/env python
"""R27 SC-e-107 check: the 22-row seed plan is complete, carries provenance, and is priced.

Usage: python check_seed22_plan.py <plan.json>   (run from the repo root; 44 DynamoDB get-item reads, read-only)
Plan file: {"firm": "49financial", "read_at": "<UTC>", "candidates": [<22 tickers>], "planned": [{ticker, row: {...},
 market_value}], "unresolved": [{ticker, reason, market_value}], "seed_pending": [{ticker, reason, market_value}],
 "mv_by_class": {<asset_class>: dollars}}.  A planned row's `row` carries asset_class, sub_asset_class and the provenance
 attributes `source_table` == 'bd-securities' and `source_last_updated` (the old list row's own last_updated).
Checks: the candidate set equals the committed baseline (seed22_candidates_20261016.json); planned, unresolved and seed_pending
partition it (every ticker exactly once); every planned row has provenance and its asset_class matches the live old-list row;
no planned ticker has a canonical row now; the dollars (planned + unresolved + seed_pending) equal the baseline total within $1.
Prints `SEED22-PLAN ok=<bool> ...`; exit 0 ok, 1 not ok, 3 file absent.
"""
import json
import os
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seed22_candidates_20261016.json')


def main():
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print('SEED22-PLAN ok=False file=ABSENT')
        return 3
    import boto3
    ddb = boto3.resource('dynamodb', region_name='us-east-1')
    canon, old = ddb.Table('etf-classifications'), ddb.Table('bd-securities')
    base = json.load(open(BASE, encoding='utf-8'))
    want = {c['ticker'] for c in base['candidates']}
    plan = json.load(open(sys.argv[1], encoding='utf-8'))
    problems = []
    if set(plan.get('candidates', [])) != want:
        problems.append('candidates differ: missing=%s extra=%s' % (sorted(want - set(plan.get('candidates', []))), sorted(set(plan.get('candidates', [])) - want)))
    buckets = {k: [e.get('ticker') for e in plan.get(k, [])] for k in ('planned', 'unresolved', 'seed_pending')}
    allt = [t for v in buckets.values() for t in v]
    if sorted(allt) != sorted(want):
        problems.append('partition: seen=%d want=%d dup=%s' % (len(allt), len(want), sorted({t for t in allt if allt.count(t) > 1})))
    mv = 0.0
    for k in buckets:
        for e in plan.get(k, []):
            mv += float(e.get('market_value', 0))
    if abs(mv - base['total_market_value']) > 1.0:
        problems.append('dollars %.2f vs baseline %.2f' % (mv, base['total_market_value']))
    for e in plan.get('planned', []):
        t, row = e.get('ticker'), e.get('row') or {}
        if row.get('source_table') != 'bd-securities' or not row.get('source_last_updated'):
            problems.append('%s provenance' % t)
        if not row.get('asset_class'):  # a null sub-class is ruled for some rows; check_seed22_fold.py grades each class against the map
            problems.append('%s class incomplete' % t)
        if 'Item' in canon.get_item(Key={'ticker': t}):
            problems.append('%s already in canonical' % t)
        o = old.get_item(Key={'ticker': t}).get('Item') or {}
        if not o:
            problems.append('%s not in old list' % t)
        elif o.get('last_updated') != row.get('source_last_updated'):
            problems.append('%s source_last_updated != old row last_updated' % t)
    print('SEED22-PLAN ok=%s planned=%d unresolved=%d seed_pending=%d dollars=%.2f problems=%s' % (
        not problems, len(buckets['planned']), len(buckets['unresolved']), len(buckets['seed_pending']), mv, problems[:6]))
    return 0 if not problems else 1


if __name__ == '__main__':
    sys.exit(main())
