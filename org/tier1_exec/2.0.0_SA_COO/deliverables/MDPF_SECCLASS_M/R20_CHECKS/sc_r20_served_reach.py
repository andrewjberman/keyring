#!/usr/bin/env python3
"""sc_r20_served_reach.py -- MDPF_SECCLASS round 20 cell SC-e-87 (row D1-S26): does BD's SERVED classify site reach the ticker-no-row
NAME:: fallback that SC-e-79 put in the shared lib?

Usage (run from the repo root being graded):  python sc_r20_served_reach.py <D_04|C_06|D_03>

It drives the SITE'S OWN served classify function, never the lib function, with the table client stubbed (no AWS call):
  D_04 -> D_04.client_portal_summary._classify_with_canonical(ticker, name, classifier, cusip)
  C_06 -> C_06.client_mix_timeseries.classify_series(tickers, names)
  D_03 -> D_03.composition_artifacts.classify_series(tickers, names, cusips)
Four positions, one table:
  TARGET   ticker with NO row, name has a NAME:: row            -> the NAME:: row's class (equity / 'Name Row')
  CONTROL1 ticker WITH a row (name also has a NAME:: row)       -> the TICKER row's class, never the name row
  CONTROL2 ticker with no row and no NAME:: row                 -> 'unclassified', class_source 'unclassified'
  CONTROL3 BLANK ticker, name has a NAME:: row                  -> the NAME:: row's class (the path that already worked)
Prints  SERVED-REACH site=<S> ok=<bool> target=<tuple> controls=<k>/3
ok is True when the target resolves and all three controls hold.
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path.cwd()
GOLD = ROOT / "data/black_diamond/scripts/gold"
FILES = {
    "D_04": GOLD / "D_04.client_portal_summary.py",
    "C_06": GOLD / "C_06.client_mix_timeseries.py",
    "D_03": GOLD / "D_03.composition_artifacts.py",
}
ROWS = {
    "VOO": {"asset_class": "equity", "sub_asset_class": "US Large Cap"},
    "NAME::COLUMBIA DIVIDEND INCOME A": {"asset_class": "equity", "sub_asset_class": "Name Row"},
    "NAME::VANGUARD MORNINGSTAR GROWTH ETF": {"asset_class": "equity", "sub_asset_class": "Name Row"},
}


class _Stub:
    def get_classification(self, key):
        return ROWS.get(key)


def _load(site):
    spec = importlib.util.spec_from_file_location("site_" + site, str(FILES[site]))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv):
    if len(argv) != 2 or argv[1] not in FILES:
        print("SERVED-REACH ok=False error=usage (D_04|C_06|D_03)")
        return 2
    site = argv[1]
    sys.path.insert(0, str(GOLD))  # `lib` must resolve to the gold lib, not another `lib` package on the path
    for _m in [m for m in sys.modules if m == "lib" or m.startswith("lib.")]:
        del sys.modules[_m]
    import pandas as pd
    from lib.etf_classifier import ETFClassifier, IdentityResolver

    clf = ETFClassifier(client=_Stub())
    clf.set_identity(IdentityResolver(name_to_ticker={}, name_to_cusips={}, cusip_to_tickers={}, ticker_to_cusips={}))
    ETFClassifier._instance = clf  # the sites read ETFClassifier.instance()
    mod = _load(site)
    ETFClassifier._instance = clf

    def served(ticker, name):
        if site == "D_04":
            ac, canon, sub, src = mod._classify_with_canonical(ticker, name, clf, "")
            return ac, canon, sub, src
        if site == "C_06":
            df = mod.classify_series(pd.Series([ticker]), pd.Series([name]))
        else:
            df = mod.classify_series(pd.Series([ticker]), pd.Series([name]), pd.Series([""]))
        r = df.iloc[0]
        return r["asset_class"], r["asset_class_canonical"], r["sub_asset_class_canonical"], r["class_source"]

    target = served("LBSAX", "Columbia Dividend Income A")
    c1 = served("VOO", "Columbia Dividend Income A")
    c2 = served("ZZZZX", "Unknown Widget Fund")
    c3 = served("", "Vanguard Morningstar Growth ETF")
    t_ok = target == ("equity", "equity", "Name Row", "etf-classifications")
    controls = [
        c1 == ("equity", "equity", "US Large Cap", "etf-classifications"),
        c2[0] == "unclassified" and c2[3] == "unclassified",
        c3 == ("equity", "equity", "Name Row", "etf-classifications"),
    ]
    ok = t_ok and all(controls)
    print(f"SERVED-REACH site={site} ok={ok} target={tuple(target)} controls={sum(controls)}/3")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
