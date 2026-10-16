#!/usr/bin/env python
"""R27 SC-e-107 ship check (Branch 1 of the seed pair): the live `etf-classifications` holds exactly what the ruling seeds.

Read-only (boto3 get_item, us-east-1). Run from the repo root:  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/e107_seeded_check.py
Reads the committed plan and fold map. Expects: every `planned` ticker of
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~97/SEED22_PLAN.json exists with the planned asset_class and
sub_asset_class (absent where the plan has none), `source_table` == 'bd-securities' and `source_last_updated` equal to the plan's; every
`seed_pending` ticker is still ABSENT. Prints `E107-SEEDED ok=<bool> present=<n>/<want> absent_ok=<m>/<want> problems=[...]`; exit 0 ok, 1 not ok.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, *(['..'] * 6)))
PLAN = os.path.join(ROOT, 'org', 'missions', 'D8', 'MDPF', 'MDPF_SECCLASS', 'deliverables', '0.9.0_WK_MDPF_SECCLASS~97', 'SEED22_PLAN.json')


def check(plan, get):
    problems, present, absent_ok = [], 0, 0
    for e in plan['planned']:
        t, want = e['ticker'], e['row']
        got = get(t)
        if not got:
            problems.append('%s absent' % t)
            continue
        ok = True
        for k in ('asset_class', 'source_table', 'source_last_updated'):
            if got.get(k) != want.get(k):
                problems.append('%s %s=%r want %r' % (t, k, got.get(k), want.get(k)))
                ok = False
        if (got.get('sub_asset_class') or None) != (want.get('sub_asset_class') or None):
            problems.append('%s sub_asset_class=%r want %r' % (t, got.get('sub_asset_class'), want.get('sub_asset_class')))
            ok = False
        present += int(ok)
    for e in plan['seed_pending']:
        if get(e['ticker']):
            problems.append('%s held out but PRESENT' % e['ticker'])
        else:
            absent_ok += 1
    return present, absent_ok, problems


def main():
    import boto3
    table = boto3.resource('dynamodb', region_name='us-east-1').Table('etf-classifications')
    plan = json.load(open(PLAN, encoding='utf-8'))
    present, absent_ok, problems = check(plan, lambda t: table.get_item(Key={'ticker': t}).get('Item'))
    print('E107-SEEDED ok=%s present=%d/%d absent_ok=%d/%d problems=%s' % (
        not problems, present, len(plan['planned']), absent_ok, len(plan['seed_pending']), problems[:6]))
    return 0 if not problems else 1


if __name__ == '__main__':
    sys.exit(main())
