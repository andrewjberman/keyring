"""The CTO's added precondition (SIGNOFF_BD_SECURITIES_COT_NEW_20260926.md @ab4a2e41bb, msg 101114): dry-build a07
dim_asset_classification's classify with the new items in the loader, with no upload, and state the per-firm delta
(49F, INF, COT; count and $).

a07's own code is imported and nothing is re-implemented except its STEP-A/STEP-B loop, whose body is copied from
build() (a07_dim_asset_classification.py:333-363) so both runs use it verbatim. The two runs share one population
and one table scan; the second adds each write-set row the way _load_ddb loads a table item (ticker map, plus the
name map through asset_name_raw). Dollars come from each firm's own population partition:
market_value_settled_unsettled (49F), current_value (INF) and Market Value (COT).

  python org/.../IRPT_MVP_M/measure_a07_delta_cot_new.py --part 1|2|all --out <json>
"""
import argparse
import collections
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
A07 = ROOT / 'data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py'
WRITE_SET = ROOT / 'org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/COT_NEW_WRITE_SET_20260926.json'
sys.path.insert(0, str(A07.parent))

_SRC_RANK = {"override": 0, "dynamodb-ticker": 0, "dynamodb-alias": 0, "regex-name": 1}
_CLS_RANK = {"alternatives": 0, "cash": 1, "fixed_income": 2, "equity": 3}


def _a07():
    spec = importlib.util.spec_from_file_location('a07', str(A07))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def classify_all(a, rep, variants_by_key, ticker_map, name_map) -> dict:
    """a07 build()'s STEP A / STEP B, per security_key -> asset_class."""
    out = {}
    for _, r in rep.iterrows():
        ac, _src = a.classify(r["ticker"], r["asset_name"], ticker_map, name_map)
        if not ac:
            hits = []
            for vt, vn in variants_by_key.get(r["security_key"], []):
                vac, vsrc = a.classify(vt or None, vn or None, ticker_map, name_map)
                if vac:
                    hits.append((_SRC_RANK.get(vsrc, 9), _CLS_RANK.get(vac, 9), vac, vsrc))
            if hits:
                hits.sort()
                ac = hits[0][2]
        out[r["security_key"]] = ac if ac else "UNCLASSIFIED-LOUD"
    return out


def _num(v) -> float:
    try:
        f = float(v)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if f != f else f  # NaN (a missing market value) counts as 0


def firm_dollars(a) -> dict:
    """security_key -> {firm: $} from each firm's own latest population partition, keyed as load_population keys."""
    import re
    usd = collections.defaultdict(lambda: collections.Counter())
    d49 = a._latest_partition("opal-data-assets", "schwab/08335338/silver/dim_position/", r"date=(\d{4}-\d{2}-\d{2})/")
    p49 = a._read_pq("opal-data-assets", f"schwab/08335338/silver/dim_position/date={d49}/data.parquet")
    for t, c, v in zip(p49["ticker_symbol"], p49["cusip"], p49["market_value_settled_unsettled"]):
        key = (str(t).upper().strip() if t not in (None, '') and str(t) not in ('None', 'nan') else str(c))
        usd[key]["49f"] += _num(v)
    dates = []
    for page in a.s3().get_paginator("list_objects_v2").paginate(Bucket="opal-data-inf", Prefix="silver/api_dims/positions_mv/", Delimiter="/"):
        for p in page.get("CommonPrefixes", []):
            m = re.search(r"snapshot_date=(\d{4}-\d{2}-\d{2})/", p["Prefix"])
            if m:
                dates.append(m.group(1))
    pinf = a._read_pq("opal-data-inf", f"silver/api_dims/positions_mv/snapshot_date={sorted(dates)[-1]}/data.parquet")
    for t, n, v in zip(pinf["ticker"], pinf["name"], pinf["current_value"]):
        if t not in (None, '') and str(t) not in ('None', 'nan'):
            key = str(t).upper().strip()
        else:
            key = "NAME:" + a.normalize_name(n)
        usd[key]["inf"] += _num(v)
    dcot = a._latest_partition("opal-data-assets", "blackdiamond/cottonwood/silver/fact_holdings/", r"date=(\d{4}-\d{2}-\d{2})/")
    pcot = a._read_pq("opal-data-assets", f"blackdiamond/cottonwood/silver/fact_holdings/date={dcot}/data.parquet")
    for t, s, cu, n, v in zip(pcot["Ticker"], pcot["Symbol"], pcot["CUSIP"], pcot["Asset Name"], pcot["Market Value"]):
        t = t or s
        if t not in (None, '') and str(t) not in ('None', 'nan'):
            key = str(t).upper().strip()
        elif cu not in (None, '') and str(cu) not in ('None', 'nan'):
            key = str(cu)
        else:
            key = "NAME:" + a.normalize_name(n)
        usd[key]["cot"] += _num(v)
    return usd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', choices=('1', '2', 'all'), default='all')
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    a = _a07()
    rows = json.loads(WRITE_SET.read_text(encoding='utf-8'))['rows']
    if args.part == '1':
        rows = [r for r in rows if r['asset_class'] != 'other']
    elif args.part == '2':
        rows = [r for r in rows if r['asset_class'] == 'other']
    ticker_map, name_map = a._load_ddb()
    pop = a.load_population()
    firms_by_key = pop.groupby("security_key")["firm"].agg(lambda s: "|".join(sorted(set(s))))
    rep = pop.sort_values(["security_key", "firm"]).drop_duplicates(subset=["security_key"], keep="first")
    variants_by_key = (pop.assign(_t=pop["ticker"].fillna(""), _n=pop["asset_name"].fillna(""))
                       .groupby("security_key")[["_t", "_n"]]
                       .apply(lambda g: sorted({(t, n) for t, n in g.itertuples(index=False, name=None)}))
                       .to_dict())
    before = classify_all(a, rep, variants_by_key, ticker_map, name_map)
    t2, n2 = dict(ticker_map), dict(name_map)
    for r in rows:
        t2[r['pk']] = {'ticker': r['pk'], 'asset_class': r['asset_class']}
        n2[a.normalize_name(r['asset_name'])] = r['pk']
    after = classify_all(a, rep, variants_by_key, t2, n2)
    usd = firm_dollars(a)
    written = {r['pk'] for r in rows}
    per_firm = collections.defaultdict(lambda: {'keys': 0, 'usd': 0.0, 'moves': collections.Counter()})
    changed = []
    for key, b0 in before.items():
        a0 = after[key]
        if a0 == b0:
            continue
        # reached through a written key by the same rule? (ticker map hit on the key, or the name map)
        rep_row = rep[rep["security_key"] == key].iloc[0]
        via = (str(rep_row["ticker"] or '').upper().strip() in written) or (
            n2.get(a.normalize_name(rep_row["asset_name"])) in written if rep_row["asset_name"] else False) or any(
            (str(vt or '').upper().strip() in written) or (n2.get(a.normalize_name(vn)) in written if vn else False)
            for vt, vn in variants_by_key.get(key, []))
        firms = firms_by_key.get(key, '').split('|')
        changed.append({'security_key': key, 'firms': firms, 'before': b0, 'after': a0, 'via_written_key': bool(via),
                        'usd': {f: round(usd[key][f], 2) for f in firms}})
        for f in firms:
            pf = per_firm[f]
            pf['keys'] += 1
            pf['usd'] += usd[key][f]
            pf['moves']['%s -> %s' % (b0, a0)] += 1
    doc = {'part': args.part, 'written_keys': len(rows), 'population_keys': len(rep),
           'changed_keys': len(changed), 'changed_not_via_written_key': [c for c in changed if not c['via_written_key']],
           'per_firm': {f: {'keys': v['keys'], 'usd': round(v['usd'], 2), 'moves': dict(v['moves'])} for f, v in per_firm.items()},
           'changed': changed}
    Path(args.out).write_text(json.dumps(doc, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({k: doc[k] for k in ('part', 'written_keys', 'population_keys', 'changed_keys', 'per_firm')}, indent=1))
    print('changed NOT via a written key: %d' % len(doc['changed_not_via_written_key']))


if __name__ == '__main__':
    main()
