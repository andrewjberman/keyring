"""The CTO's requirement for the R4 enable half (msg 1.0.0_SA_CTO 20260926T170847Z, answering 101341): the first scheduled
Holdings publication's per-firm structural diff against the SERVED revision, split by class (labels, classification,
amounts, node set, clocks, and whatever else moves), each class traced to the half that authorised it; a class no
signed half covers is named with its cause before the schedule turns on.

No build, no write. It reads a candidate Platinum JSON already built locally (account_mask_publication_diff.py dry, or
run_firm --local-out) and the served revision (assembled from the accepted manifest), then classifies every change:

  node_added / node_removed     node set (by node_id), with node_kind and the added/removed dollars
  label_account                 display.label on a level-0 ACCOUNT node only
  display_other                 display on any other node
  classification                classification / asset_class_basis / sub_asset_class members, named per field
  amount                        amount.value moved (dollars netted per node_kind)
  percentages                   percentages only (a consequence of amount or node-set moves)
  clocks                        clocks only
  provenance / other            anything else, by field name
  top:<member>                  a gated top-level member (scope, custody_totals, coverage, attribution_holdouts)

  python org/.../IRPT_MVP_M/holdings_publication_diff_classes.py --firm 49financial --candidate <platinum.json> --out <json>
"""
import argparse
import collections
import importlib.util
import json
import subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
_spec = importlib.util.spec_from_file_location(
    'amd', str(ROOT / 'org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/account_mask_publication_diff.py'))
amd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(amd)

CLASS_FIELDS = {'classification', 'asset_class_basis', 'sub_asset_class', 'asset_class'}


def _amount(n):
    return float(((n or {}).get('amount') or {}).get('value') or 0.0)


def classify(served, cand):
    s = {n['node_id']: n for n in served['nodes']}
    c = {n['node_id']: n for n in cand['nodes']}
    counts = collections.Counter()
    dollars = collections.defaultdict(float)
    examples = collections.defaultdict(list)

    def note(cls, nid, detail=None):
        counts[cls] += 1
        if len(examples[cls]) < 5:
            examples[cls].append({'node_id': nid, **(detail or {})})

    for nid in sorted(set(c) - set(s)):
        k = c[nid].get('node_kind')
        note('node_added', nid, {'node_kind': k, 'amount': _amount(c[nid])})
        dollars['node_added:%s' % k] += _amount(c[nid])
    for nid in sorted(set(s) - set(c)):
        k = s[nid].get('node_kind')
        note('node_removed', nid, {'node_kind': k, 'amount': _amount(s[nid])})
        dollars['node_removed:%s' % k] += _amount(s[nid])
    for nid in sorted(set(s) & set(c)):
        a, b = s[nid], c[nid]
        kind = a.get('node_kind')
        fields = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
        if not fields:
            continue
        rest = set(fields)
        if 'display' in rest:
            rest.discard('display')
            if kind == 'ACCOUNT' and a.get('level') == 0:
                note('label_account', nid, {'served': (a.get('display') or {}).get('label'),
                                            'candidate': (b.get('display') or {}).get('label')})
            else:
                note('display_other', nid, {'node_kind': kind})
        cls_moved = rest & CLASS_FIELDS
        if cls_moved:
            rest -= cls_moved
            note('classification', nid, {'node_kind': kind, 'fields': sorted(cls_moved)})
        if 'amount' in rest:
            rest.discard('amount')
            delta = _amount(b) - _amount(a)
            note('amount', nid, {'node_kind': kind, 'delta': round(delta, 2)})
            dollars['amount:%s' % kind] += delta
        if 'percentages' in rest:
            rest.discard('percentages')
            note('percentages', nid, {'node_kind': kind})
        if 'clocks' in rest:
            rest.discard('clocks')
            note('clocks', nid, {'node_kind': kind})
        for f in sorted(rest):
            note('field:%s' % f, nid, {'node_kind': kind})
    for m in amd.GATED_TOP:
        if served.get(m) != cand.get(m):
            note('top:%s' % m, m)
    return {'counts': dict(counts), 'dollars': {k: round(v, 2) for k, v in dollars.items()},
            'examples': {k: v for k, v in examples.items()}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--firm', required=True)
    ap.add_argument('--candidate', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    import boto3
    s3 = boto3.client('s3', region_name='us-east-1')
    served = amd._served(s3, a.firm)
    rev, latest = amd._served_revision(s3, a.firm)
    cand = json.loads(Path(a.candidate).read_text(encoding='utf-8'))
    doc = {'firm': a.firm, 'served_revision': rev, 'served_latest_date': latest,
           'candidate': a.candidate, 'candidate_business_date': (cand.get('clocks') or {}).get('business_date'),
           **classify(served, cand)}
    Path(a.out).write_text(json.dumps(doc, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({k: doc[k] for k in ('firm', 'candidate_business_date', 'counts', 'dollars')}, indent=1))


if __name__ == '__main__':
    main()
