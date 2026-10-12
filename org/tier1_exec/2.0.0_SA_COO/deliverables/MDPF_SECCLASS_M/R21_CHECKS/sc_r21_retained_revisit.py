#!/usr/bin/env python3
"""sc_r21_retained_revisit.py -- MDPF_SECCLASS round 21 cell SC-e-91 (row D1-S30): does C_06's retained-date pass revisit a retained
date's `unclassified` holdings, so that a classifier improvement (SC-e-79 / SC-e-87's ticker-no-row -> NAME:: branch) reaches a date C_06
already wrote?   Run from the repo root being graded.

Usage:  python sc_r21_retained_revisit.py <revisit|wiring>

revisit : drives the module's OWN `reclassify_retained(existing_mix, existing_conc, rebuilt_dates, moved=None)` on one retained date with
          the table stubbed (no AWS call). Four holdings, one table:
            TARGET   ticker with NO row, name has a NAME:: row, held as `unclassified`  -> equity / 'Name Row' / etf-classifications,
                     its pct moves from `unclassified` to `equity` inside that date's mix
            STAYS    ticker with no row and no NAME:: row, held as `unclassified`      -> stays `unclassified` (listed, never guessed)
            CONTROL  a holding already inside the six (VOO equity)                     -> byte-identical
            a second call moves 0 holdings and changes nothing (idempotent).
          `moved`, when passed a list, receives one tuple per holding moved: (date, old_class, new_class, dollars) with
          dollars = pct * the date's total_mv, so the caller can adjust the firm and advisor daily snapshots.
          Prints  RETAINED-REVISIT ok=<bool> moved=<n> stays_unclassified=<bool> control_identical=<bool> idempotent=<bool> deltas=<n> mix_ok=<bool>
wiring  : AST read of `build()`: the `if not keys_to_process:` branch (no new partition) must reach the retained pass instead of returning
          first, and `build()` must hand `reclassify_retained` a `moved` accumulator.
          Prints  RETAINED-WIRING ok=<bool> early_return_runs_pass=<bool> moved_passed=<bool>
"""
import ast
import copy
import importlib.util
import os
import sys
from pathlib import Path

ROOT = Path.cwd()
GOLD = ROOT / "data/black_diamond/scripts/gold"
FILE = Path(os.environ.get("R21_C06_FILE") or (GOLD / "C_06.client_mix_timeseries.py"))  # the override is for the issuer's positive control only


class _Stub:
    ROWS = {
        "VOO": {"asset_class": "equity", "sub_asset_class": "US Large Cap"},
        "NAME::COLUMBIA DIVIDEND INCOME A": {"asset_class": "equity", "sub_asset_class": "Name Row"},
    }

    def get_classification(self, key):
        return self.ROWS.get(key)


def _holding(name, ticker, cls, pct, mv, canon, sub, src):
    return {"asset_name": name, "ticker": ticker, "asset_class": cls, "asset_class_canonical": canon,
            "sub_asset_class_canonical": sub, "class_source": src, "market_value": mv, "pct": pct}


def revisit() -> int:
    sys.path.insert(0, str(GOLD))
    for _m in [m for m in sys.modules if m == "lib" or m.startswith("lib.")]:
        del sys.modules[_m]
    from lib.etf_classifier import ETFClassifier, IdentityResolver

    clf = ETFClassifier(client=_Stub())
    clf.set_identity(IdentityResolver(name_to_ticker={}, name_to_cusips={}, cusip_to_tickers={}, ticker_to_cusips={}))
    ETFClassifier._instance = clf
    spec = importlib.util.spec_from_file_location("c06_r21_under_test", str(FILE))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ETFClassifier._instance = clf

    ds = "2026-10-09"
    mix = {ds: {"date": ds, "equity": 0.4, "fixed_income": 0.4, "unclassified": 0.2, "total_mv": 1000.0}}
    target = _holding("Columbia Dividend Income A", "LBSAX", "unclassified", 0.1, 100.0, "", "", "unclassified")
    stays = _holding("Unknown Widget Fund", "ZZZZX", "unclassified", 0.1, 100.0, "", "", "unclassified")
    control = _holding("Vanguard S&P 500 ETF", "VOO", "equity", 0.4, 400.0, "equity", "US Large Cap", "etf-classifications")
    conc = {ds: {"date": ds, "holdings": [target, stays, control]}}
    control_before = copy.deepcopy(control)

    def _call(m, c, mv):
        try:
            return mod.reclassify_retained(m, c, set(), mv)
        except TypeError:  # the base signature has no `moved`: behaviour is still graded, deltas read 0
            del mv[:]
            return mod.reclassify_retained(m, c, set())

    moved = []
    counts = _call(mix, conc, moved)
    h = {x["ticker"]: x for x in conc[ds]["holdings"]}
    t_ok = (h["LBSAX"]["asset_class"] == "equity" and h["LBSAX"]["asset_class_canonical"] == "equity"
            and h["LBSAX"]["sub_asset_class_canonical"] == "Name Row" and h["LBSAX"]["class_source"] == "etf-classifications")
    stays_ok = h["ZZZZX"]["asset_class"] == "unclassified" and h["ZZZZX"]["class_source"] == "unclassified"
    control_ok = h["VOO"] == control_before
    m = mix[ds]
    mix_ok = abs(m["equity"] - 0.5) < 1e-9 and abs(m["unclassified"] - 0.1) < 1e-9 and abs(m["fixed_income"] - 0.4) < 1e-9
    deltas = [d for d in moved if tuple(d)[:3] == (ds, "unclassified", "equity") and abs(float(tuple(d)[3]) - 100.0) < 1e-6]
    snap = copy.deepcopy((mix, conc))
    again = _call(mix, conc, [])
    idem = tuple(again)[1] == 0 and (mix, conc) == snap
    ok = bool(t_ok and stays_ok and control_ok and mix_ok and len(deltas) == 1 and idem and tuple(counts)[1] == 1)
    print(f"RETAINED-REVISIT ok={ok} moved={tuple(counts)[1]} stays_unclassified={stays_ok} control_identical={control_ok} "
          f"idempotent={idem} deltas={len(deltas)} mix_ok={mix_ok}")
    return 0 if ok else 1


def wiring() -> int:
    tree = ast.parse(FILE.read_text(encoding="utf-8"))
    build = next((n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "build"), None)
    early_runs_pass = moved_passed = False
    if build is not None:
        for node in ast.walk(build):
            if isinstance(node, ast.If) and isinstance(node.test, ast.UnaryOp) and isinstance(node.test.op, ast.Not) \
                    and isinstance(node.test.operand, ast.Name) and node.test.operand.id == "keys_to_process":
                calls = [c for c in ast.walk(ast.Module(body=node.body, type_ignores=[])) if isinstance(c, ast.Call)]
                names = {getattr(c.func, "id", getattr(c.func, "attr", "")) for c in calls}
                first_return = next((i for i, s in enumerate(node.body) if isinstance(s, ast.Return)), None)
                pass_first = False
                for i, s in enumerate(node.body):
                    src = ast.dump(s)
                    if "retained" in src.lower() or "reclassify" in src.lower():
                        pass_first = first_return is None or i < first_return
                        break
                early_runs_pass = bool(pass_first and any("retained" in n.lower() or "reclassify" in n.lower() for n in names))
        for c in ast.walk(build):
            if isinstance(c, ast.Call) and getattr(c.func, "id", getattr(c.func, "attr", "")) == "reclassify_retained":
                if len(c.args) >= 4 or any(k.arg == "moved" for k in c.keywords):
                    moved_passed = True
    ok = early_runs_pass and moved_passed
    print(f"RETAINED-WIRING ok={ok} early_return_runs_pass={early_runs_pass} moved_passed={moved_passed}")
    return 0 if ok else 1


if __name__ == "__main__":
    fns = {"revisit": revisit, "wiring": wiring}
    if len(sys.argv) != 2 or sys.argv[1] not in fns:
        print("RETAINED ok=False error=usage (revisit|wiring)")
        sys.exit(2)
    sys.exit(fns[sys.argv[1]]())
