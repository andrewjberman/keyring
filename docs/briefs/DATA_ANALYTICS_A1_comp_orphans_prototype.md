# comp-orphans — dispatcher-invocation orphan-detector (PROTOTYPE + inventory)

**For:** 1.0.0_SA_CTO (approved the tool; arch-gates + canonicalizes into the comp-tool catalog + graph-call-manifest). **By:** 0.4.0_DS_ClientPlatform (A1 primitive). **Origin:** Andrew-direct ("if comp-tools didn't say no-downstream-consumers, something's wrong") → the comp-tool running-chain-graph is a LOWER-BOUND that misses **undispatched-orphans**; this fills that axis.

## What it does
`orphan = (gold *.py present in tree) MINUS (script filenames the tree's dispatcher invokes)`. An orphan exists in the tree but the dispatcher never runs it → no nightly execution → does not feed served/frontend = dead-for-pipeline (retained only as ad-hoc manual diagnostics). This is the **decisive essential-vs-dead primitive** (one query; beats per-script comp-blast, which can't see exists-but-unrun).

Per-tree dispatchers: bd → `gold_dispatch.sh`; cot → `gold_dispatch.sh`; inf → `orion-gold-dispatch.sh`.

## Inventory (prototype run, 2026-06-24)

| Tree | gold .py present | dispatched | ORPHAN | orphans |
|---|---|---|---|---|
| **bd** | 55 | 27 | **28** | **all 26 E_* (E_00..E_25)** + 2 SUSPICIOUS: `C_01b.role_aua_backfill.py`, `C_01c.role_aua_flow_join.py` |
| **cot** | 35 | 24 | **11** | 8 E_* (E_00,01,18,20,21,22,23,24) + 3 SUSPICIOUS: `A_05.assets_dimension.py`, `C_01b.role_aua_backfill.py`, `C_01c.role_aua_flow_join.py` |
| **inf** | (under-counts) | — | — | INF_ double-prefix not yet matched — see Limitations |

**Confirms:** the whole bd E_* group is dead (Andrew's call). **Bonus (the tool's real value — surfaced UNKNOWN orphans a human scan misses):** `C_01b.role_aua_backfill` + `C_01c.role_aua_flow_join` are non-diagnostic orphans in BOTH bd+cot — role-AUA scripts that exist but aren't dispatched (superseded? dormant backfill? a gap?) → flagged for inspection, NOT auto-dead (could be a manual-but-needed backfill). cot `A_05.assets_dimension.py` orphan ties to the parked WORK-A assets_dim item.

## Limitations (for canonicalization)
1. **inf INF_ naming:** GOLD_RE `^[A-Z]+_[0-9]+...` doesn't match the `INF_B_01...` double-prefix → inf under-detects. Fix: `^[A-Z]+(_[A-Z]+)?_[0-9]+[a-z]?\.`.
2. **Token-diff, not CASE-aware:** matches *.py tokens anywhere in the dispatcher (incl. comments). A script named in a comment but not actually invoked would be counted dispatched (false-negative for orphan-hood = conservative/safe). CTO's canonical version should parse the actual invocation CASE/array.
3. **Dispatched ≠ frontend-reachable.** This is Q1 (live-vs-dead). Q2 (among the dispatched, who feeds the frontend / is essential vs firm-specific) is the per-script census — a separate axis.

## Prototype code
```python
#!/usr/bin/env python3
from __future__ import annotations
import os, re, sys
ROOT = os.environ.get('OPAL_WS') or os.getcwd()
TREES = {
    'bd':  ('data/black_diamond/scripts/gold', 'data/black_diamond/scripts/gold/gold_dispatch.sh'),
    'cot': ('data/cot/scripts/gold',           'data/cot/scripts/gold/gold_dispatch.sh'),
    'inf': ('data/inf/scripts/gold',           'data/inf/scripts/gold/orion-gold-dispatch.sh'),
}
GOLD_RE = re.compile(r'^[A-Z]+_[0-9]+[a-z]?\.[A-Za-z0-9_]+\.py$')   # canonical: ^[A-Z]+(_[A-Z]+)?_[0-9]+[a-z]?\.
PY_TOKEN_RE = re.compile(r'[A-Z]+_[0-9]+[a-z]?\.[A-Za-z0-9_]+\.py')

def gold_scripts(d):
    p = os.path.join(ROOT, d)
    return {f for f in os.listdir(p) if GOLD_RE.match(f)} if os.path.isdir(p) else set()

def dispatched(f):
    p = os.path.join(ROOT, f)
    if not os.path.isfile(p): return set()
    return set(PY_TOKEN_RE.findall(open(p, encoding='utf-8', errors='replace').read()))

def main():
    rc = 0
    for tree, (gd, disp) in TREES.items():
        present, invoked = gold_scripts(gd), dispatched(disp)
        orphans = sorted(present - invoked)
        print(f'TREE {tree}: {len(present)} present | {len(present)-len(orphans)} dispatched | {len(orphans)} ORPHAN')
        for o in orphans:
            print(f'    - {o}')
        if orphans: rc = 1
    return rc

if __name__ == '__main__':
    sys.exit(main())
```

## Canonicalization ask (CTO)
Wrap as `.tools/comp-orphans` (bash launcher → this python), fix the INF_ regex + CASE-aware parse, register in `org/modules/graph/graph-call-manifest.yaml` + `comp-which` routing ("which gold scripts are dead / not dispatched"). Banks into the silent-absence invariant (make the undispatched signal LOUD, not silently-missed).
