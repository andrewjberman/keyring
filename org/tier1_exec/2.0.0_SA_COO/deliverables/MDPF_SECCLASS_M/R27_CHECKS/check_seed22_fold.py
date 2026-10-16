#!/usr/bin/env python
"""R27 SC-e-107 amendment-1 check: the seed plan follows the CTO's fold ruling exactly.

Usage: python check_seed22_fold.py <plan.json>   (run from the repo root; reads the committed fold map and baseline, no AWS call)
Expects: planned = the four equity tickers plan_rows plans directly (AEMGX, CEMVX, FBCVX, FIADX) + the 9 tickers of the fold map's
`seed`; seed_pending = the map's 9 `held_out` tickers; unresolved empty; each map-seeded row's asset_class / sub_asset_class equal the
map's (a null sub-class means the attribute is absent or null); every planned row carries `source_table` == 'bd-securities' and
`source_last_updated`; the HODL row records the override (its `fold_rule` is F5 and `fold_note` contains 'OVERRIDE'); dollars of
planned and of seed_pending equal the baseline's for those tickers within $0.01.
Prints `SEED22-FOLD ok=<bool> ...`; exit 0 ok, 1 not ok, 3 file absent.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EQUITY4 = {'AEMGX', 'CEMVX', 'FBCVX', 'FIADX'}


def main():
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print('SEED22-FOLD ok=False file=ABSENT')
        return 3
    fmap = json.load(open(os.path.join(HERE, 'seed22_fold_map_20261016.json'), encoding='utf-8'))
    base = {c['ticker']: c['market_value'] for c in json.load(open(os.path.join(HERE, 'seed22_candidates_20261016.json'), encoding='utf-8'))['candidates']}
    plan = json.load(open(sys.argv[1], encoding='utf-8'))
    problems = []
    planned = {e['ticker']: e for e in plan.get('planned', [])}
    pending = {e['ticker']: e for e in plan.get('seed_pending', [])}
    want_planned = EQUITY4 | set(fmap['seed'])
    want_pending = set(fmap['held_out'])
    if set(planned) != want_planned:
        problems.append('planned: missing=%s extra=%s' % (sorted(want_planned - set(planned)), sorted(set(planned) - want_planned)))
    if set(pending) != want_pending:
        problems.append('seed_pending: missing=%s extra=%s' % (sorted(want_pending - set(pending)), sorted(set(pending) - want_pending)))
    if plan.get('unresolved'):
        problems.append('unresolved not empty: %s' % [e.get('ticker') for e in plan['unresolved']])
    for t, spec in fmap['seed'].items():
        row = (planned.get(t) or {}).get('row') or {}
        if row.get('asset_class') != spec['asset_class'] or (row.get('sub_asset_class') or None) != spec['sub_asset_class']:
            problems.append('%s class %s/%s != ruled %s/%s' % (t, row.get('asset_class'), row.get('sub_asset_class'), spec['asset_class'], spec['sub_asset_class']))
        if row.get('fold_rule') != spec['rule']:
            problems.append('%s fold_rule %r' % (t, row.get('fold_rule')))
    for t, e in planned.items():
        row = e.get('row') or {}
        if row.get('source_table') != 'bd-securities' or not row.get('source_last_updated'):
            problems.append('%s provenance' % t)
    h = (planned.get('HODL') or {}).get('row') or {}
    if 'OVERRIDE' not in str(h.get('fold_note', '')) or h.get('fold_rule') != 'F5':
        problems.append('HODL override not recorded')
    for t in set(planned) | set(pending):
        mv = float((planned.get(t) or pending.get(t) or {}).get('market_value', -1))
        if abs(mv - base.get(t, -9)) > 0.01:
            problems.append('%s dollars %.2f vs %.2f' % (t, mv, base.get(t, -9)))
    print('SEED22-FOLD ok=%s planned=%d seed_pending=%d unresolved=%d problems=%s' % (
        not problems, len(planned), len(pending), len(plan.get('unresolved', [])), problems[:6]))
    return 0 if not problems else 1


if __name__ == '__main__':
    sys.exit(main())
