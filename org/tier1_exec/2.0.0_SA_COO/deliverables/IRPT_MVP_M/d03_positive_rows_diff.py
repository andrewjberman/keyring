"""COT D_03 composition, served code vs the cash-line branch (CTO 101616 ruling (a); CRO 101619). Read-only; writes nothing
to S3.

Runs D_03's own steps (canonical holdings, open filter, [branch: positive rows], ghost exclusion, classify, architect
merge, canonical AUA) for BOTH code versions, then calls each version's _build_composition at the firm, advisor and
relationship grains and lists every scope whose total or mix moves, before and after, with counts printed.

Usage: python d03_positive_rows_diff.py --before <gold dir, served code> --after <gold dir, branch> [--out <json>]
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path


def load(gold, tag):
    sys.path.insert(0, str(gold))
    for k in [k for k in sys.modules if k == 'lib' or k.startswith('lib.')]:
        del sys.modules[k]
    spec = importlib.util.spec_from_file_location(f'd03_{tag}', str(Path(gold) / 'D_03.composition_artifacts.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    from lib.exclusions import load_ghost_account_ids, apply_ghost_exclusion
    sys.path.remove(str(gold))
    return m, load_ghost_account_ids, apply_ghost_exclusion


def build(gold, tag):
    m, ghosts, excl = load(gold, tag)
    key = m._find_latest_canonical_holdings()
    lots = m._load_holdings_from_canonical(key)
    lots = lots[lots['is_open'].fillna(False)].copy()
    if hasattr(m, 'positive_rows'):
        lots = m.positive_rows(lots)
    lots = excl(lots, ghosts(), label=tag)
    lots['asset_class'] = m.classify_series(lots['ticker'], lots['asset_name'])
    try:  # D_03 Step 3: rel_architect_lookup, else client_dimension.primary_architect
        rl = m._read_parquet(m.REL_ARCHITECT_LOOKUP, columns=['relationship_id', 'architect'])
    except Exception:
        rl = m._read_parquet(m.CLIENT_DIMENSION, columns=['relationship_id', 'primary_architect'])
        rl = rl.rename(columns={'primary_architect': 'architect'})
    lots = lots.merge(rl, on='relationship_id', how='left')
    lots['architect'] = lots['architect'].fillna('Unassigned')
    rel_aua, firm_aua = m._load_canonical_aua_lookup()
    adv_aua = {}
    if rel_aua is not None:
        for _, r in lots[['relationship_id', 'architect']].drop_duplicates().iterrows():
            adv_aua[r['architect']] = adv_aua.get(r['architect'], 0) + rel_aua.get(r['relationship_id'], 0)
    out = {('firm', 'cot'): m._build_composition(lots, {'firm_id': 'cot'}, key, canonical_aua=firm_aua)}
    for a, g in lots.groupby('architect'):
        if str(a).strip().lower() in ('', 'nan', 'none', 'unassigned'):
            continue
        out[('advisor', str(a))] = m._build_composition(g, {'firm_id': 'cot'}, key, canonical_aua=adv_aua.get(a))
    for r, g in lots.groupby('relationship_id'):
        if str(r).strip().lower() in ('', 'nan', 'none'):
            continue
        out[('relationship', str(r))] = m._build_composition(
            g, {'firm_id': 'cot'}, key, canonical_aua=rel_aua.get(r) if rel_aua else None)
    return key, out


def shape(c):
    if c is None:
        return None
    mix = {x['asset_class']: (round(x['market_value'], 2), round(x['pct'], 6)) for x in c['mix']}
    return {'total': round(c['total_market_value'], 2), 'mix': mix,
            'pct_sum': round(sum(p for _, p in mix.values()), 6)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--before', required=True)
    ap.add_argument('--after', required=True)
    ap.add_argument('--out')
    a = ap.parse_args()
    kb, before = build(Path(a.before).resolve(), 'before')
    ka, after = build(Path(a.after).resolve(), 'after')
    assert kb == ka, (kb, ka)
    moved, over = [], {'before': [], 'after': []}
    counts = {}
    for scope in sorted(set(before) | set(after)):
        b, f = shape(before.get(scope)), shape(after.get(scope))
        counts[scope[0]] = counts.get(scope[0], 0) + 1
        for side, v in (('before', b), ('after', f)):
            if v and v['pct_sum'] > 1.0005:
                over[side].append([scope[0], scope[1], v['pct_sum']])
        if b != f:
            moved.append({'grain': scope[0], 'id': scope[1], 'before': b, 'after': f})
    res = {
        'input': kb, 'scopes': counts,
        'moved': {g: sum(1 for x in moved if x['grain'] == g) for g in counts},
        'over_100pct': {k: len(v) for k, v in over.items()},
        'over_100pct_detail': over, 'moved_detail': moved,
    }
    text = json.dumps(res, indent=1, default=str)
    if a.out:
        Path(a.out).write_text(text + '\n', encoding='utf-8')
    print(json.dumps({k: res[k] for k in ('input', 'scopes', 'moved', 'over_100pct')}, indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
