#!/usr/bin/env python3
"""SC-e-16 (MDPF_SECCLASS round 7): the BLOOMBERG-namespace reader census.

FWD-9 puts every Rival Funds stock into DynamoDB `etf-classifications`. The 516 non-US securities
carry no ISIN or CUSIP, so 1.0.0_SA_CTO RULINGS batch 257 Q1 keys them in a third namespace:
`ticker` = `BBG:<ticker>:<exch>` (no whitespace), `identifier_namespace` = `BLOOMBERG`,
`security_bloomberg` = the Bloomberg id verbatim. The census comes FIRST: every reader of the
table is exercised through its REAL function on a synthetic BLOOMBERG row, ONLY the table
stubbed (the in-memory DynamoDB double and boto3 patch of the round-6 census, imported from
R6_CHECKS/r6_model_reader_census.py, never copied). No AWS call is made; nothing is written.

The synthetic row (the order's) is run twice per reader:
  A: the full row                                 (sub_asset_class "Developed", low_confidence false)
  B: sub_asset_class ABSENT, low_confidence true
Beside it the table holds control rows, among them a US row keyed `REL` (the bare ticker of
`REL LN Equity`) with a DIFFERENT class: a reader that strips the BBG key to a bare US ticker, or
matches it to a holding by ticker text, returns the control's class and is graded MISKEYS.

One verdict per reader:
  TOLERATES      exercised; no crash, no refusal of the row, no mis-key, no contract failure
  CRASHES        raised, or hung
  REFUSES        the reader drops or declines the BLOOMBERG row
  MISKEYS        treats the key as a bare US ticker, or matches it to a holding by `ticker` text
  FAILS-CONTRACT a served output breaks a strict contract (the Holdings schema is additionalProperties:false)
  READ-ONLY      not runnable here (a portal TypeScript mapping, a delegate, a PRD); the deciding
                 line is recorded and re-verified by this check where the file is present

COMPLETENESS GUARD: every tracked code file outside org/, docs/ and archive/ that names the table
(`etf-classifications`, `etf_classifications_dynamodb`), the namespace (`identifier_namespace`), the
provenance field (`classified_by`) or the BD/COT library (`lib.etf_classifier`) must be a reader
below, a declared NOT_READER, or a test. A file in none of the three prints UNCENSUSED and withholds
BBG-READER-TOLERATED. The portal submodule is not in `git ls-files`: its readers are listed by hand.

Run from the worktree root:  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_bbg_reader_census.py
Prints `BBG-READER-CENSUS readers=.. tolerates=.. read_only=.. crashes=.. refuses=.. miskeys=.. fails_contract=..`
and, when crashes, refuses, miskeys, fails_contract and UNCENSUSED are all zero, `BBG-READER-TOLERATED`.
Writes R7_BBG_READER_CENSUS_20261005.json beside the R6/R7 censuses. ASCII only.
"""
from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[6]
assert (ROOT / ".tools").is_dir() and (ROOT / "org").is_dir(), "not run from inside the repo tree: %s" % ROOT

DELIV = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
R6_PATH = DELIV / "R6_CHECKS/r6_model_reader_census.py"
OUT = DELIV / "R7_BBG_READER_CENSUS_20261005.json"
R6_CENSUS = DELIV / "R6_MODEL_READER_CENSUS_20260930.json"
CONTRACT_MDPF = ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json"
HOLDINGS_SCHEMA = ROOT / "docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json"
CATALOGUE_SCHEMA = ROOT / "infra/aws/lambda/investor-reporting/_contracts/ComparisonCatalogue.schema.json"
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
YANG = ROOT / "infra/aws/lambda/v2_portal/yang_pipeline"
IRPT = ROOT / "infra/aws/lambda/investor-reporting"
GEN = IRPT / "ycharts/generate"
TABLE = "etf-classifications"


def _load_r6():
    """The round-6 census as a LIBRARY: its table double, boto3 patch, loader and isolation are reused."""
    spec = importlib.util.spec_from_file_location("r6_lib_for_r7", str(R6_PATH))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["r6_lib_for_r7"] = mod
    spec.loader.exec_module(mod)
    return mod


r6 = _load_r6()
World, FakeTable, FakeDdbClient, isolated, load = r6.World, r6.FakeTable, r6.FakeDdbClient, r6.isolated, r6.load
Verdict, jdump = r6.Verdict, r6.jdump

# ---------------------------------------------------------------------------------------------
# The synthetic BLOOMBERG row (the task order's), its second shape, and the controls.
# ---------------------------------------------------------------------------------------------
KEY = "BBG:REL:LN"
ROW_A = {"ticker": KEY, "identifier_namespace": "BLOOMBERG", "security_bloomberg": "REL LN Equity",
         "asset_class": "equity", "sub_asset_class": "Developed", "instrument_kind": "single_security",
         "classified_by": "scheduled", "listing_country": "GB", "low_confidence": False}
ROW_B = {k: v for k, v in ROW_A.items() if k != "sub_asset_class"}
ROW_B["low_confidence"] = True
VARIANTS = [("A", ROW_A), ("B", ROW_B)]
NEW_ATTRS = ("identifier_namespace", "security_bloomberg", "listing_country", "instrument_kind",
             "classified_by", "low_confidence")

# A US row keyed by the BARE ticker of `REL LN Equity`, in a DIFFERENT class: the mis-key detector.
CONTROL_REL = {"ticker": "REL", "asset_class": "fixed_income", "sub_asset_class": "Short Duration",
               "management_style": "active", "sector": "Control Sector", "name": "Control US REL Fund",
               "classified_by": "seed"}
CONTROLS = [
    {"ticker": "SPY", "asset_class": "equity", "sub_asset_class": "US Large Cap", "management_style": "passive",
     "sector": "Broad Market", "name": "SPDR S&P 500 ETF Trust", "classified_by": "seed"},
    CONTROL_REL,
    {"ticker": "CUSIP:037833100", "asset_class": "equity", "identifier_namespace": "CUSIP",
     "classified_by": "scheduled", "name": "Control CUSIP row"},
    {"ticker": "LEGACYX", "asset_class": "fixed_income", "sub_asset_class": "Short Duration",
     "management_style": "active", "name": "Legacy Row With No Label"},
]


def rows_for(row):
    return copy.deepcopy(CONTROLS) + [copy.deepcopy(row)]


def world(row):
    return World(rows_for(row))


def expect(cond, msg, verdict="FAILS-CONTRACT"):
    if not cond:
        raise Verdict(verdict, msg)


def class_verdict(got):
    """The verdict for a wrong class read back for the BBG key: the bare-US control's class is a mis-key, an empty
    or unclassified answer for a present row is a refusal of it, anything else breaks the reader's contract."""
    if got == CONTROL_REL["asset_class"]:
        return "MISKEYS"
    if got in (None, "", "unknown", "unclassified"):
        return "REFUSES"
    return "FAILS-CONTRACT"


def miskey_free(got_class, row, what):
    """The reader returned the BLOOMBERG row's class, not the bare-US control's, and not an empty answer."""
    expect(got_class not in (None, "", "unknown", "unclassified"),
           "%s answered %r for the present row %s" % (what, got_class, KEY), "REFUSES")
    expect(got_class != CONTROL_REL["asset_class"] or row["asset_class"] == CONTROL_REL["asset_class"],
           "%s returned the bare US `REL` control's class %r for %s" % (what, got_class, KEY), "MISKEYS")


def both(fn):
    """Run an exercise on both shapes of the row; a verdict names the shape that produced it."""
    def run():
        parts = []
        for label, row in VARIANTS:
            try:
                parts.append("[%s] %s" % (label, fn(copy.deepcopy(row))))
            except Verdict as v:
                raise Verdict(v.verdict, "[%s] %s" % (label, v.evidence))
        return " || ".join(parts)
    return run


# ---------------------------------------------------------------------------------------------
# The exercises. Each returns an evidence string on TOLERATES, or raises.
# ---------------------------------------------------------------------------------------------

def ex_client_read(relpath):
    def ex(row):
        with world(row), isolated([ROOT / Path(relpath).parent]):
            mod = load(relpath, "r7_client_mod")
            clf = mod.ETFClassifier()
            got = clf.get_classification(KEY)
            expect(got is not None, "get_classification(%s) returned None for a present row" % KEY, "REFUSES")
            expect(got == row, "get_classification changed the row: %r" % (got,))
            ac = clf.get_asset_class(KEY)
            miskey_free(ac, row, "get_asset_class")
            expect(ac == "equity", "get_asset_class %r" % ac)
            expect(clf.get_sub_asset_class(KEY) == row.get("sub_asset_class", ""), "get_sub_asset_class")
            expect(clf.get_management_style(KEY) == "unknown" and clf.get_sector(KEY) == "", "style/sector defaults")
            bare = clf.get_classification("REL")
            expect(bare is not None and bare["ticker"] == "REL" and bare["asset_class"] == "fixed_income",
                   "the bare REL lookup no longer answers its own row", "MISKEYS")
            expect(clf.get_classification("REL LN Equity") is None and clf.get_classification("BBG:REL") is None,
                   "a partial / verbatim Bloomberg id matched a row", "MISKEYS")
            eq = [i["ticker"] for i in clf.find_by_asset_class("equity")]
            expect(KEY in eq and "CUSIP:037833100" not in eq, "find_by_asset_class(equity) %r" % eq)
            sub = [i["ticker"] for i in clf.find_by_sub_asset_class("Developed")]
            expect((KEY in sub) == ("sub_asset_class" in row), "find_by_sub_asset_class(Developed) %r" % sub)
            return ("get_classification/get_asset_class/get_sub_asset_class/get_management_style/get_sector read the row "
                    "verbatim (bool low_confidence intact), the bare REL lookup still answers the US control, a verbatim "
                    "`REL LN Equity` matches nothing; find_by_asset_class lists the row (only CUSIP rows are dropped by "
                    "_drop_cusip_rows, a BLOOMBERG row is listed) and find_by_sub_asset_class lists it only when "
                    "sub_asset_class is present. find_by_* has ZERO functional call sites in the repo (tests only)")
    return both(ex)


def ex_client_classify_holdings(relpath):
    def ex(row):
        with world(row), isolated([ROOT / Path(relpath).parent]):
            mod = load(relpath, "r7_client_ch_mod")
            res = mod.ETFClassifier.classify_holdings([{"ticker": KEY, "weight": 0.4}, {"ticker": "SPY", "weight": 0.6},
                                                       {"ticker": "REL", "weight": 0.1}])
            expect(abs(res["equity"] - 1.0) < 1e-9, "equity weight %r (the BBG row + SPY should be 1.0)" % res["equity"],
                   "MISKEYS")
            expect(abs(res["fixed_income"] - 0.1) < 1e-9, "bare REL control weight %r" % res["fixed_income"], "MISKEYS")
            expect(res["unknown"] == 0.0 and res["unknown_tickers"] == [], "the BBG row read as unknown: %r" % res)
            return "classify_holdings over [BBG key 0.4, SPY 0.6, bare REL 0.1] -> equity 1.0, fixed_income 0.1, unknown 0"
    return both(ex)


def ex_positioning_lambda(dirrel):
    def ex(row):
        d = ROOT / dirrel
        with world(row), isolated([d]):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                mod = load(dirrel + "/lambda_function.py", "r7_yang_positioning")
                nm = mod.resolve_display_name(KEY, "FALLBACK")
                expect(nm == "FALLBACK", "resolve_display_name %r" % nm)
                ac = mod.classify_etf(KEY)
                miskey_free(ac, row, "classify_etf")
                expect(ac == "equity", "classify_etf %r" % ac)
                expect(mod.classify_management_style(KEY) == "passive", "management style default")
                assets, mgmt = mod.calculate_allocations([{"ticker": KEY, "weight": 0.5}, {"ticker": "SPY", "weight": 0.5}])
                expect(abs(assets.get("equity", 0) - 100.0) < 0.2, "allocations %r" % assets, "MISKEYS")
                a2, _ = mod.calculate_allocations([{"ticker": "REL", "weight": 1.0}])
                expect(a2.get("fixed_income") == 100.0, "bare REL control allocations %r" % a2, "MISKEYS")
                seg = mod.calculate_segment_breakdown([{"ticker": KEY, "weight": 1.0}])
                jdump({"assets": assets, "mgmt": mgmt, "seg": seg})
            return ("resolve_display_name falls to the fallback (no name on the row), classify_etf equity, management "
                    "style defaults passive, calculate_allocations puts the row's weight in equity (the bare REL control "
                    "stays fixed_income), calculate_segment_breakdown sector %r geography %r; served dicts json.dumps strictly"
                    % (sorted(seg["sector"]), sorted(seg["geography"])))
    return both(ex)


def ex_attribution_lambda(dirrel):
    def ex(row):
        import pandas as pd
        d = ROOT / dirrel
        with world(row) as w, isolated([d]):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                mod = load(dirrel + "/lambda_function.py", "r7_yang_attribution")
                nm = mod.resolve_display_name(KEY, w.main.rows[KEY], None)
                expect(nm == KEY, "resolve_display_name %r (no name on the row: the ticker verbatim)" % nm)
                ncol = 15
                rows = []
                for t in (KEY, "SPY", "REL"):
                    rows.append([t, None, None, None, None, 0.02, 0.01, 0.008, 0.009, 0.0, 0.0, 0.0, 0.001, 0.001, 0.0])
                rows.append([None, "Total"] + [None] * 3 + [1.0, 0.02, 1.0, 0.02, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
                df = pd.DataFrame(rows, columns=list(range(ncol)))
                res = mod.extract_holdings_for_portfolio(df, 5, 0)
                hold = {h["ticker"]: h for h in res["holdings"]}
                expect(KEY in hold, "the BLOOMBERG holding was silently dropped (kept %s)" % sorted(hold), "REFUSES")
                expect(hold[KEY]["asset_class"] == "Equity", "asset_class %r" % hold[KEY]["asset_class"])
                expect(hold["REL"]["asset_class"] == "Fixed Income", "bare REL control %r" % hold["REL"]["asset_class"],
                       "MISKEYS")
                jdump(res)
            return ("resolve_display_name answers the ticker verbatim (the row has no name); extract_holdings_for_portfolio "
                    "over a 3-holding attribution sheet kept all 3, the BBG holding 'Equity', the bare REL control "
                    "'Fixed Income'; result json.dumps strictly")
    return both(ex)


def ex_publisher():
    def ex(row):
        rel = "data/etfs/scripts/gold/etf_positioning_publisher.py"
        with world(row), isolated([SHARED, ROOT / "data/etfs/scripts/gold", ROOT / "lib"]):
            mod = load(rel, "r7_etf_positioning_publisher")
            nm = mod._display_name(KEY, "RAW ISSUER STRING")
            expect(isinstance(nm, str) and nm and nm != CONTROL_REL["name"], "_display_name %r" % (nm,), "MISKEYS")
            nm_rel = mod._display_name("REL", "RAW")
            expect(nm_rel == CONTROL_REL["name"], "bare REL _display_name %r" % (nm_rel,), "MISKEYS")
            return "_display_name(BBG key, raw) -> %r (no registry name: the un-shouted raw string); bare REL still answers its own registry name" % nm
    return both(ex)


def ex_satellites_registry():
    def ex(row):
        rel = "data/assets/scripts/gold/build_satellites_registry.py"
        with world(row), isolated([ROOT / "data/assets/scripts/gold", ROOT / "lib"]):
            mod = load(rel, "r7_build_satellites_registry")
            clf = mod.load_classifier()
            ac, sac = mod.classify(clf, KEY)
            expect(ac == "equity" and sac == row.get("sub_asset_class"), "classify -> %r" % ((ac, sac),),
                   class_verdict(ac))
            jdump([ac, sac])
            return "load_classifier()+classify() -> (%r, %r) strings, json-safe (absent sub_asset_class -> None)" % (ac, sac)
    return both(ex)


def ex_satellites_characteristics():
    def ex(row):
        rel = "data/assets/scripts/gold/build_satellites_characteristics.py"
        with world(row), isolated([ROOT / "data/assets/scripts/gold", ROOT / "lib"]):
            out = io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
                mod = load(rel, "r7_build_satellites_characteristics")
                identity, stats = mod.load_identity([KEY, "REL"])
            got = identity.get(KEY)
            expect(got is not None, "load_identity dropped the BLOOMBERG ticker", "REFUSES")
            expect(got.get("name") != CONTROL_REL["name"], "BBG identity carries the REL control's name %r" % got, "MISKEYS")
            expect(identity["REL"].get("name") == CONTROL_REL["name"], "bare REL identity %r" % identity["REL"], "MISKEYS")
            jdump(identity)
            return "load_identity([BBG key, REL]) -> BBG identity %r (no name, no style: absent not guessed), bare REL keeps its own name, json-safe, missing=%s" % (got, stats.get("identity_missing"))
    return both(ex)


def _bd_clf():
    from lib.etf_classifier import ETFClassifier  # the BD library, `lib` = gold/lib (gold is first on sys.path)
    return ETFClassifier(table_name=TABLE)


def ex_bd_classifier():
    def ex(row):
        rel = "data/black_diamond/scripts/gold/lib/etf_classifier.py"
        with world(row), isolated([SHARED, ROOT / "data/black_diamond/scripts/gold"]):
            mod = load(rel, "r7_bd_etf_classifier")
            clf = mod.ETFClassifier(table_name=TABLE)
            ac = clf.classify(KEY, "RELX PLC")
            miskey_free(ac, row, "classify")
            expect(ac == "equity", "classify %r" % ac)
            expect(clf.get_sub_asset_class(KEY, "RELX PLC") == row.get("sub_asset_class", ""), "get_sub_asset_class")
            hop = clf.classify_with_identity(KEY, "RELX PLC")
            expect(hop == ("equity", row.get("sub_asset_class", ""), "etf-classifications", "ticker"), "classify_with_identity %r" % (hop,))
            expect(clf.classify("REL", "x") == "fixed_income", "bare REL", "MISKEYS")
            expect(clf.classify("NOSUCHTKR", "x") == clf.UNKNOWN, "miss did not read unknown")
            return "classify/get_sub_asset_class/classify_with_identity read the BBG key verbatim -> %r; bare REL and a miss unchanged" % (hop,)
    return both(ex)


def ex_cot_classifier():
    def ex(row):
        rel = "data/cot/scripts/gold/lib/etf_classifier.py"
        with world(row), isolated([SHARED, ROOT / "data/cot/scripts/gold"]):
            mod = load(rel, "r7_cot_etf_classifier")
            clf = mod.ETFClassifier(table_name=TABLE)
            ac = clf.classify(KEY, "RELX PLC")
            miskey_free(ac, row, "classify")
            expect(ac == "equity", "classify %r" % ac)
            expect(clf.get_sub_asset_class(KEY) == row.get("sub_asset_class", ""), "get_sub_asset_class")
            pos = clf.classify_position(KEY, None, False)
            expect(pos == ("equity", "table ticker"), "classify_position %r" % (pos,))
            pos2 = clf.classify_position("", "037833100", False)
            expect(pos2 == ("equity", "table cusip"), "CUSIP rung %r" % (pos2,))
            expect(clf.classify_position("REL", None, False) == ("fixed_income", "table ticker"), "bare REL", "MISKEYS")
            return "classify/get_sub_asset_class/classify_position read the BBG key by ticker -> %r; the CUSIP rung and bare REL unchanged" % (pos,)
    return both(ex)


def ex_bd_assets_dim():
    def ex(row):
        import pandas as pd
        gold = ROOT / "data/black_diamond/scripts/gold"
        silver = ROOT / "data/black_diamond/scripts/silver"
        with world(row), isolated([SHARED, gold, silver, ROOT / "lib"]):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                mod = load("data/black_diamond/scripts/silver/build_bd_assets_dim.py", "r7_build_bd_assets_dim")
                clf = _bd_clf()
                coarse = sorted(mod.COARSE_SUPER_CLASSES)[0]
                dim = pd.DataFrame({"ticker": [KEY, "REL"], "asset_name": ["RELX PLC", "Control US REL Fund"],
                                    "asset_super_class_bd": [coarse, coarse]})
                res = mod.apply_blend(dim, classifier=clf)
            expect(len(res) == 2, "apply_blend dropped rows: %d of 2" % len(res), "REFUSES")
            cols = [c for c in res.columns if "canonical" in c]
            by = res.set_index("ticker")
            cls_col = next((c for c in cols if "sub" not in c and "class" in c), None)
            expect(cls_col is not None, "no canonical class column in %s" % list(res.columns))
            expect(by.loc[KEY, cls_col] == "equity", "canonical class %r" % by.loc[KEY, cls_col],
                   class_verdict(by.loc[KEY, cls_col]))
            expect(by.loc["REL", cls_col] == "fixed_income", "bare REL canonical %r" % by.loc["REL", cls_col], "MISKEYS")
            return "apply_blend over [BBG key, REL] kept both rows; %s: BBG equity, REL fixed_income (columns %s)" % (cls_col, cols)
    return both(ex)


def _series(*vals):
    import pandas as pd
    return pd.Series(list(vals), dtype="object")


def ex_bd_d04():
    def ex(row):
        gold = ROOT / "data/black_diamond/scripts/gold"
        with world(row), isolated([SHARED, gold, ROOT / "lib"]):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                mod = load("data/black_diamond/scripts/gold/D_04.client_portal_summary.py", "r7_d04")
                clf = _bd_clf()
                res = mod._classify_with_canonical(KEY, "RELX PLC", clf)
                ctl = mod._classify_with_canonical("REL", "Control", clf)
            expect(res[0] == "equity" and res[3] == "etf-classifications", "%r" % (res,),
                   class_verdict(res[0]))
            expect(ctl[0] == "fixed_income", "bare REL %r" % (ctl,), "MISKEYS")
            jdump(res)
            return "_classify_with_canonical(BBG key) -> %r, json-safe; bare REL -> %r" % (res, ctl[:2])
    return both(ex)


def ex_bd_series(rel, name, gold_rel):
    """BD C_06 / D_03 classify_series over a ticker series holding the BBG key, bare REL and a blank ticker."""
    def ex(row):
        gold = ROOT / gold_rel
        with world(row), isolated([SHARED, gold, ROOT / "lib"]):
            out = io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
                mod = load(rel, name)
                clf = mod.ETFClassifier.instance()
                clf.set_identity(None)  # a blank ticker reads 'identity-unavailable', no S3
                df = mod.classify_series(_series(KEY, "REL"), _series("RELX PLC", "Control US REL Fund"))
            r0, r1 = df.iloc[0], df.iloc[1]
            expect(r0["asset_class_canonical"] == "equity" and r0["class_source"] == "etf-classifications",
                   "BBG row %r" % r0.to_dict(), class_verdict(r0["asset_class_canonical"]))
            expect(r0["sub_asset_class_canonical"] == row.get("sub_asset_class", ""), "sub %r" % r0.to_dict())
            expect(r1["asset_class_canonical"] == "fixed_income", "bare REL %r" % r1.to_dict(), "MISKEYS")
            jdump(df.to_dict("records"))
            return "classify_series over [BBG key, REL] -> BBG %s / %r from 'etf-classifications', REL fixed_income; json-safe" % (
                r0["asset_class_canonical"], r0["sub_asset_class_canonical"])
    return both(ex)


def ex_cot_series(rel, name, gold_rel):
    def ex(row):
        gold = ROOT / gold_rel
        with world(row), isolated([SHARED, gold, ROOT / "lib"]):
            out = io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
                mod = load(rel, name)
                res = mod.classify_series(_series(KEY, "REL", ""), _series("RELX PLC", "Control", "Blank"))
            vals = list(res)
            expect(vals[0] == "equity", "BBG row %r" % vals, class_verdict(vals[0]))
            expect(vals[1] == "fixed_income", "bare REL %r" % vals, "MISKEYS")
            expect(vals[2] == "unclassified", "blank ticker %r" % vals)
            jdump(vals)
            return "classify_series over [BBG key, REL, blank] -> %r (classify_position, the ruled rule); json-safe" % vals
    return both(ex)


def ex_bd_e25():
    def ex(row):
        import pandas as pd
        gold = ROOT / "data/black_diamond/scripts/gold"
        with world(row), isolated([SHARED, gold, ROOT / "lib"]):
            out = io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
                mod = load("data/black_diamond/scripts/gold/E_25.aua_decomposition_audit.py", "r7_e25")
                h = pd.DataFrame({"ticker": [KEY, "REL"], "asset_name": ["RELX PLC", "Control"], "market_value": [100.0, 50.0]})
                res = mod.classification_drift_audit(h)
            expect(isinstance(res, dict) and "error" not in res, "drift audit returned %r" % (res,))
            unknown_n = next((v for k, v in res.items() if "unknown" in k and isinstance(v, (int, float))), None)
            expect(unknown_n in (0, None), "the BBG row read as unknown: %r" % (res,), "REFUSES")
            return "classification_drift_audit over [BBG key, REL] ran; keys %s; the BBG row is not counted unknown" % sorted(res)
    return both(ex)


def ex_holdings_snapshot():
    def ex(row):
        rel = "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py"
        hs_dir = ROOT / "data/assets/scripts/gold/investor_reporting"
        with world(row), isolated([hs_dir, ROOT / "lib", SHARED]):
            out = io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
                mod = load(rel, "r7_holdings_snapshot")
                sys.path.insert(0, str(SHARED))
                import etf_classifications_dynamodb as canonical_mod
                canonical = canonical_mod.ETFClassifier()

                class _Fallback:
                    _ticker_map, _name_map = {}, {}

                    def classify(self, ticker, name):
                        return ""

                    def get_sub_asset_class(self, ticker, name=None):
                        return ""

                clf = mod._NarrowedClassifier(canonical, _Fallback())
                schema = json.loads(HOLDINGS_SCHEMA.read_text(encoding="utf-8"))
                validator = mod.contract_validator_class()(schema["properties"]["nodes"]["items"])
                nodes = []
                for i, (sym, desc) in enumerate(((KEY, "RELX PLC"), ("REL", "Control US REL Fund"))):
                    nodes.append({
                        "node_id": "n%03d" % i, "level": 3, "node_kind": "SECURITY", "basis": "OBSERVED",
                        "amount": {"value": 1000.0, "units": "USD", "denominator": {"kind": "ACCOUNT", "value": 1000000.0}},
                        "percentages": {"of_parent": 0.1, "of_total": 0.1},
                        "provenance": {"producer": "r7_bbg_reader_census", "join_method": "synthetic",
                                       "join_matched": 1, "join_attempted": 1, "claim": "held"},
                        "display": {"label": sym, "symbol": sym, "description": desc},
                    })
                census = mod.annotate_classification(nodes, classifier=(mod, clf))
            errs = []
            for n in nodes:
                errs.extend("%s: %s" % (n["node_id"], e.message) for e in validator.iter_errors(n))
            expect(not errs, "served node fails the published HoldingsSnapshot contract: %s" % errs[:3])
            bbg, ctl = nodes
            expect(bbg["asset_class"] == "equity" and bbg["asset_class_basis"] == "TABLE", "BBG node %r" % bbg,
                   class_verdict(bbg["asset_class"]))
            expect(bbg.get("sub_asset_class") == row.get("sub_asset_class"), "BBG sub %r" % bbg.get("sub_asset_class"))
            expect(ctl["asset_class"] == "fixed_income", "bare REL node %r" % ctl, "MISKEYS")
            leaked = sorted(set(bbg) & set(NEW_ATTRS))
            expect(not leaked, "table attribute leaked onto the served node: %s" % leaked)
            probe = dict(bbg, security_bloomberg="REL LN Equity")
            expect(any(True for _ in validator.iter_errors(probe)),
                   "negative control failed: a leaked security_bloomberg was accepted")
            jdump(nodes)
            return ("annotate_classification over a BBG SECURITY node + a REL control: both validate against %s "
                    "(additionalProperties false); BBG node asset_class equity basis TABLE sub %r; none of %s reaches "
                    "a node; negative control (a leaked security_bloomberg) IS refused by the same validator; "
                    "by_class_source %s" % (HOLDINGS_SCHEMA.relative_to(ROOT), bbg.get("sub_asset_class"), list(NEW_ATTRS),
                                            census.get("by_class_source")))
    return both(ex)


def ex_scheduled():
    def ex(row):
        with world(row), isolated([SHARED]):
            mod = load("infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py", "r7_scheduled")
            import etf_classifications_dynamodb as cm
            clf = cm.ETFClassifier()
            vocab = mod.TableVocabulary.from_live_table(clf)
            existing = mod.existing_tickers(clf)
            expect("equity" in vocab.asset_classes, "vocabulary lost equity")
            expect(("Developed" in vocab.sub_asset_classes.get("equity", set())) == ("sub_asset_class" in row),
                   "vocabulary sub classes %r" % sorted(vocab.sub_asset_classes.get("equity", set())))
            expect(KEY in existing, "existing_tickers missed the BLOOMBERG row", "REFUSES")
            plan, unresolved, seed_pending = mod.plan_rows(
                [(KEY, "RELX PLC"), ("REL", "x"), ("ZZNEWX", "Some New Fund")],
                vocab=vocab, existing_tickers=existing, seed_source_tickers=set(),
                bd_securities_lookup=lambda t: {"asset_class": "equity", "sub_asset_class": None} if t == "ZZNEWX" else None,
                gics_lookup=lambda t: None, schwab_lookup=lambda t: None)
            planned = {p["ticker"] for p in plan}
            expect(KEY not in planned and "REL" not in planned, "plan_rows re-planned an existing key: %s" % sorted(planned),
                   "MISKEYS")
            return ("TableVocabulary.from_live_table and existing_tickers read the table with the BLOOMBERG row in it "
                    "(row held in existing_tickers, sub_asset_class joins the vocabulary only when present); plan_rows over "
                    "[BBG key, REL, ZZNEWX] planned only %s (never the BBG key, never the bare REL). E_18 bd/cot call exactly "
                    "this sequence" % sorted(planned))
    return both(ex)


def ex_label_legacy():
    def ex(row):
        with world(row) as w, isolated([YANG]):
            mod = load("infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py", "r7_label_legacy")
            items = mod.scan_all(w.main)
            unl = mod.plan_unlabelled(items)
            expect(unl == ["LEGACYX"], "plan_unlabelled %r (expected only the unlabelled control)" % unl[:5])
            try:
                mod.label_row_if_unlabelled(w.main, KEY)
                raise Verdict("FAILS-CONTRACT", "label update overwrote the BBG row's classified_by")
            except mod.RowAlreadyLabelled:
                pass
            expect(w.main.rows[KEY]["classified_by"] == "scheduled", "classified_by changed")
            return "scan_all paginated %d rows; plan_unlabelled excluded the BBG row (classified_by present); label_row_if_unlabelled raises RowAlreadyLabelled (designed, additive-only) and leaves it" % len(items)
    return both(ex)


def ex_set_kind():
    def ex(row):
        with world(row) as w, isolated([YANG]):
            mod = load("infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py", "r7_set_kind")
            items = mod.scan_all(w.main)
            absent = mod.plan_absent_kind(items)
            expect(KEY not in absent, "the BBG row (it carries instrument_kind) was offered to the kind-only plan")
            try:
                mod.set_kind_if_absent(w.main, KEY, "fund", {"fund", "single_security"})
                raise Verdict("FAILS-CONTRACT", "kind update overwrote the BBG row's instrument_kind")
            except mod.KindAlreadySet:
                pass
            expect(w.main.rows[KEY]["instrument_kind"] == "single_security", "instrument_kind changed")
            return "scan_all+plan_absent_kind did not offer the BBG row (instrument_kind present); set_kind_if_absent raises KindAlreadySet (designed) and leaves it"
    return both(ex)


def ex_seed_classifications():
    def ex(row):
        with world(row) as w, isolated([YANG, SHARED]):
            mod = load("infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py", "r7_seed_classifications")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                existing = mod.read_existing(w.main)
            expect(KEY in existing, "read_existing missed the BLOOMBERG row", "REFUSES")
            import etf_classification as seedsrc
            expect(KEY not in seedsrc.ETF_CLASSIFICATIONS, "the seed source carries the BBG key: merge_item would touch the row", "MISKEYS")
            return "read_existing paged %d rows incl. the BBG row; the seed source (ETF_CLASSIFICATIONS, %d keys) does not carry the BBG key, so no seed merge_item ever runs on it" % (
                len(existing), len(seedsrc.ETF_CLASSIFICATIONS))
    return both(ex)


def ex_seed_constituents():
    def ex(row):
        with world(row) as w, isolated([YANG]):
            mod = load("infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py", "r7_seed_constituents")
            consts = {KEY: {"name": "X", "asset_class": "Equity", "sub_asset_class": "US"},
                      "ZZNEWX": {"name": "New X", "asset_class": "Equity", "sub_asset_class": "US"}}
            mod.load_constituents = lambda: consts
            outs = []
            for argv in (["x", "--dry-run"], ["x", "--dry-run", "--kind-only"]):
                buf = io.StringIO()
                sys.argv = argv
                with contextlib.redirect_stdout(buf):
                    rc = mod.main()
                expect(rc == 0, "main %s returned %s" % (argv[1:], rc), "CRASHES")
                outs.append(buf.getvalue())
            expect(("KEEP   %-12s" % KEY) in outs[0], "the BBG ticker not preserved (KEEP) in the plan")
            built = mod.build_row(KEY, "X", "Equity", "US", "2026-10-05T00:00:00Z")
            try:
                mod.put_row_if_unclassified(w.main, built)
                raise Verdict("FAILS-CONTRACT", "constituents put overwrote the BBG row")
            except mod.RowProtected:
                pass
            expect(w.main.rows[KEY]["classified_by"] == "scheduled", "BBG row changed")
            return "paginated scan of %d rows; --dry-run plan KEEPs the BBG key, --kind-only dry-run ok; put_row_if_unclassified on it raises RowProtected (designed) and leaves the row" % len(w.main.rows)
    return both(ex)


def ex_seed_canonical():
    def ex(row):
        with world(row) as w, isolated([ROOT / "data/black_diamond/scripts/classification"]):
            mod = load("data/black_diamond/scripts/classification/seed_canonical_securities.py", "r7_seed_canonical")
            sec = {"ticker": KEY, "name": "RELX PLC", "asset_class": "equity", "sub_asset_class": "US Large Cap"}
            conflicts = mod._yang_conflicts(w.main, sec)
            same = {k: CONTROL_REL[k] for k in ("ticker", "name", "asset_class", "sub_asset_class")}
            ctl = mod._yang_conflicts(w.main, same)
            absent = mod._yang_conflicts(w.main, {"ticker": "BBG:NOSUCH:LN", "name": "n", "asset_class": "equity", "sub_asset_class": "x"})
            expect(absent == [], "first mint of an absent BBG key reported a conflict")
            expect(ctl == [], "the bare REL control, identical to its own row, reported %r" % (ctl,), "MISKEYS")
            expect(all(c[1] == row.get(c[0]) for c in conflicts),
                   "a conflict's table-side value is not the BBG row's own: %r" % (conflicts,), "MISKEYS")
            return ("_yang_conflicts read the BBG row via get_item by its full key -> %s (the table's own values, which win: "
                    "designed guard); an absent BBG key is a clean first mint; the bare REL control identical to its row reports none"
                    % (conflicts,))
    return both(ex)


def ex_seed_bd():
    def ex(row):
        with world(row) as w, isolated([ROOT / "data/black_diamond/scripts/classification"]):
            w.tables["bd-securities"] = FakeTable([], "bd-securities")
            mod = load("data/black_diamond/scripts/classification/seed_bd_securities.py", "r7_seed_bd")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                mod.seed(dry_run=False)
            bd = w.tables["bd-securities"].rows
            expect(KEY in bd, "the BBG row was not copied", "REFUSES")
            copied = bd[KEY]
            return ("one-time seed scanned %d rows and copied the BBG row into bd-securities without error. NOTE (recorded, "
                    "not graded): the copy overwrites classified_by ('scheduled' -> %r) and carries identifier_namespace=%r "
                    "and security_bloomberg onto the retiring per-firm table; a documented one-time seed, not scheduled; "
                    "CUSIP: rows are skipped by prefix, a BBG: row is not" % (
                        len(w.main.rows), copied.get("classified_by"), copied.get("identifier_namespace")))
    return both(ex)


def ex_classify_residual():
    def ex(row):
        with world(row) as w, isolated([YANG, SHARED]):
            mod = load("infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py", "r7_classify_residual")
            import etf_classifications_dynamodb as cm
            clf = cm.ETFClassifier()
            n = mod.table_rows_at_build(clf)
            expect(n == len(w.main.rows), "table_rows_at_build %d != %d" % (n, len(w.main.rows)))
            live = mod.existing_tickers(clf, region="us-east-1")
            expect(KEY in live, "existing_tickers missed the BLOOMBERG row", "REFUSES")
            return "table_rows_at_build counted %d (Select=COUNT, paginated) and existing_tickers returned the BBG key: the runner's own census sees it as a live row" % n
    return both(ex)


def ex_write_model_rows():
    def ex(row):
        with world(row), isolated([YANG, SHARED]):
            mod = load("infra/aws/lambda/v2_portal/yang_pipeline/write-model-rows.py", "r7_write_model_rows")
            import etf_classifications_dynamodb as cm
            clf = cm.ETFClassifier()
            vocab = mod.TableVocabulary.from_live_table(clf)
            live = mod.existing_tickers(clf)
            expect(KEY in live, "existing_tickers missed the BLOOMBERG row", "REFUSES")
            cands = {KEY: {"key": KEY, "asset_class": "equity", "sub_asset_class": row.get("sub_asset_class"),
                           "name": "RELX PLC", "confidence": 0.9, "low_confidence": False}}
            rows, refused, present = mod.plan_rows([KEY], cands, vocab, live)
            expect(rows == [] and refused == [] and present == [KEY], "plan_rows %r %r %r" % (rows, refused, present))
            return "from_live_table and existing_tickers read the table with the BBG row in it; plan_rows over the BBG key planned 0, refused 0, reported it PRESENT (left as it is)"
    return both(ex)


def ex_scoped_amgt():
    def ex(row):
        with world(row) as w, isolated([ROOT]):
            mod = load("lib/research/api/scoped_amgt.py", "r7_scoped_amgt")
            mod._dynamodb = lambda: r6.FakeResource(w.tables)
            joined = mod._join_classification([{"ticker": KEY, "x": 1}, {"ticker": "REL LN", "x": 2}, {"ticker": "REL US", "x": 3}])
            direct, london, us = joined
            expect(direct["name_state"] in ("SERVED", "ABSENT") and direct["classification"] is not None
                   and direct["classification"]["asset_class"] == "equity", "BBG key joined %r" % direct, "REFUSES")
            expect(us["classification"]["asset_class"] == "fixed_income", "REL US joined %r" % us, "MISKEYS")
            jdump(joined)
            note = ""
            if london["classification"] is not None and london["classification"]["asset_class"] == "fixed_income":
                note = (" NOTE (pre-existing, recorded not graded): a Bloomberg ticker 'REL LN' is read by its first "
                        "space-separated token 'REL' (bare-ticker rule, AMGT-ww-2), so a London ranking row joins the US "
                        "`REL` row, never the BBG row; the BBG row neither causes nor cures that")
            return ("_join_classification GetItem by the first token: the BBG key as a ticker joins the BBG row (equity), "
                    "'REL US' joins the US control; json.dumps strictly.%s" % note)
    return both(ex)


def ex_positioning_chain():
    def ex(row):
        with world(row) as w, isolated([ROOT]):
            mod = load("lib/research/identity/positioning_chain.py", "r7_positioning_chain")
            cmap, denom = mod.read_etf_classifications()
            expect(denom["rows"] == len(w.main.rows) and KEY in cmap, "read_etf_classifications denominator %r" % (denom,), "REFUSES")
            ident = mod.resolve_one(KEY, None, "GB", None, cmap[KEY], None)
            jdump(ident)
            expect(ident["classifier_asset_class"] == "equity", "classifier_asset_class %r" % ident["classifier_asset_class"],
                   class_verdict(ident["classifier_asset_class"]))
            ctl = mod.resolve_one("REL", None, "US", None, cmap["REL"], None)
            expect(ctl["classifier_asset_class"] == "fixed_income", "bare REL %r" % ctl["classifier_asset_class"], "MISKEYS")
            return "read_etf_classifications (client scan + TypeDeserializer, paginated) returned %d rows incl. the BBG key (projected to asset_class/sub_asset_class/name); resolve_one carried classifier_asset_class equity; json.dumps strictly" % denom["rows"]
    return both(ex)


def _catalogue_world(row, named=False):
    r = copy.deepcopy(row)
    if named:
        r["name"] = "RELX PLC"
    return World(rows_for(r))


def ex_comparison_catalogue():
    import jsonschema

    def run_catalogue(row, named):
        with _catalogue_world(row, named) as w, isolated([GEN]):
            mod = load("infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py", "r7_comparison_catalogue")
            reader = mod.classifications_reader(FakeDdbClient(w.tables))
            rows = reader()
            expect(KEY in rows, "the real reader dropped the BLOOMBERG row", "REFUSES")
            cat = mod.build_catalogue(tenant="t1", read_classifications=reader)
            schema = json.loads(CATALOGUE_SCHEMA.read_text(encoding="utf-8"))
            errs = list(jsonschema.Draft202012Validator(schema).iter_errors(cat))
            listed = [e for e in cat["entries"] if e.get("ticker") == KEY]
            verbatim = mod.entry_for_ticker(KEY, tenant="t1", read_classifications=reader)
            verr = list(jsonschema.Draft202012Validator(schema).iter_errors({"catalogue_version": "v1", "entries": [verbatim]}))
            return cat, errs, listed, verbatim, verr

    def ex(row):
        cat, errs, listed, verbatim, verr = run_catalogue(row, False)
        expect(not errs, "catalogue fails its closed schema: %s" % [e.message for e in errs[:3]])
        expect(not listed, "the unnamed BBG row is listed in the picker list: %r" % listed)
        expect(verbatim["name_source"] == "ticker_verbatim" and verbatim["ticker"] == KEY, "entry_for_ticker %r" % (verbatim,))
        expect(not verr, "the verbatim BBG entry fails the closed schema: %s" % [e.message for e in verr[:3]])
        note = ""
        try:
            cat2, errs2, listed2, _v, _e = run_catalogue(row, True)
            note = (" NAMED PROBE (not graded; the order's row carries no name): a BBG row WITH a name %s the picker list "
                    "(%d entr%s for %s) and the list %s its closed schema" % (
                        "IS offered in" if listed2 else "is not offered in", len(listed2), "y" if len(listed2) == 1 else "ies", KEY,
                        "passes" if not errs2 else "FAILS (%s)" % [e.message for e in errs2[:2]]))
        except Verdict as v:
            note = " NAMED PROBE (not graded): %s" % v.evidence
        return ("classifications_reader (real paginated Scan over the double) read the BBG row; build_catalogue lists "
                "it NOT (an unnamed row is never listed, CTO batch 61) and validates against ComparisonCatalogue.schema.json "
                "(closed); entry_for_ticker answers the BBG key verbatim (name_source ticker_verbatim), schema-valid.%s" % note)
    return both(ex)


def ex_maintained_sources():
    def ex(row):
        paths = [GEN, IRPT, IRPT / "_scope", IRPT / "reports"]
        with world(row) as w, isolated(paths):
            out = io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
                cat = load("infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py", "r7_cc_for_ms")
                ms = load("infra/aws/lambda/investor-reporting/_scope/maintained_sources.py", "r7_maintained_sources")
            reader = cat.classifications_reader(FakeDdbClient(w.tables))
            got = ms._classified_etf(KEY, reader)
            ctl = ms._classified_etf("REL", reader)
            expect(ctl is not None and ctl["vendor_id"] == "REL", "the bare REL control (named) is no longer admitted: %r" % (ctl,), "MISKEYS")
            expect(got is None or got["vendor_id"] != "REL", "the BBG key was admitted under the bare vendor id REL: %r" % (got,), "MISKEYS")
            fullmatch = bool(ms.CLASSIFIED_ETF_TICKER.fullmatch(KEY))
            named = copy.deepcopy(row)
            named["name"] = "RELX PLC"
            w.main.rows[KEY] = named
            named_got = ms._classified_etf(KEY, cat.classifications_reader(FakeDdbClient(w.tables), ttl_seconds=0))
            return ("_classified_etf(BBG key): %s (CLASSIFIED_ETF_TICKER %r %s the key; the YCharts comparison grammar is a bare "
                    "ticker). The BBG key is never admitted as a comparison key and never reduced to the bare vendor id REL; "
                    "bare REL, named, is still admitted. This is a designed non-admission of a key outside the grammar "
                    "(the row has no name either), not a read failure. NAMED PROBE (not graded): with a name on the row "
                    "_classified_etf still returns %s, while comparison_catalogue.build_catalogue WOULD list that named row "
                    "(see its entry): the list could offer a key the resolver refuses" % (
                        "None (not admitted)" if got is None else "admitted %r" % (got,), ms.CLASSIFIED_ETF_TICKER.pattern,
                        "matches" if fullmatch else "does not match", named_got))
    return both(ex)


# ---------------------------------------------------------------------------------------------
# READ-ONLY readers: the deciding line is recorded and re-verified where the file is present.
# ---------------------------------------------------------------------------------------------
PORTAL_SRC = ROOT / "portal/src"


def portal_pin():
    try:
        return subprocess.run(["git", "ls-tree", "HEAD", "portal"], cwd=str(ROOT), capture_output=True, text=True,
                              timeout=30).stdout.split()[2]
    except Exception:  # noqa: BLE001
        return None


def read_only_portal(rel, decide, what):
    path = PORTAL_SRC / rel
    if path.exists():
        expect(decide in path.read_text(encoding="utf-8"), "deciding line not present in %s" % path)
        verified = "re-verified in the checked-out portal"
    else:
        verified = ("portal submodule not checked out in this worktree; deciding line read from the portal working copy "
                    "on 2026-10-05 (gitlink pin %s), a build-time read not re-run here" % portal_pin())
    return "READ-ONLY (TypeScript). Deciding line `%s`. %s %s." % (decide, what, verified)


def read_only_composition():
    return read_only_portal(
        "pages/AdvisorIntelligence/_shared/lib/composition.ts",
        "export const CANONICAL_CLASSES = ['equity', 'fixed_income', 'alternatives', 'structured', 'commodities', 'multi_asset', 'unclassified'] as const",
        "normalizeMixTo4Class keeps an item only when `classes.includes(item.asset_class)` (composition.ts:126); the BBG row's "
        "asset_class 'equity' is a member. The portal reads served artifacts, never a table row, so identifier_namespace / "
        "security_bloomberg / listing_country never reach it")


def read_only_wire_holdings():
    return read_only_portal(
        "pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts",
        "readonly asset_class?: 'equity' | 'fixed_income' | 'alternatives' | 'structured' | 'commodities' | 'multi_asset' | 'cash' | 'other' | 'unclassified'",
        "The wire type carries asset_class and sub_asset_class only (matching the Python contract, exercised in "
        "holdings_snapshot.py above); no BLOOMBERG attribute is a member")


def read_only_wire_catalogue():
    return read_only_portal(
        "pages/InvestorReporting/contracts/wire/ComparisonCatalogue.ts",
        "readonly name_source: 'model_catalogue' | 'etf_classifications' | 'ticker_verbatim'",
        "readCatalogue (contracts/comparison-catalogue.ts) accepts any non-empty string `key` and `ticker`, so a served "
        "verbatim 'BBG:REL:LN' entry is read; the Python producer is exercised above (comparison_catalogue.py)")


def read_only_dashbd():
    path = ROOT / "org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md"
    text = path.read_text(encoding="utf-8")
    line = next(row for row in text.split("\n") if row.startswith("| C-CLASSES"))
    expect("fixed_income, equity, commodities, structured, alternatives" in line, "C-CLASSES vocabulary line changed")
    expect("No row means UNCLASSIFIED" in line, "C-CLASSES miss rule changed")
    return ("READ-ONLY (no consumer code exists in the tree). Deciding line IRPT_DASHBD_PRD.md C-CLASSES row: 'Each holding maps "
            "through `etf-classifications` (DynamoDB, key `ticker`) ... No row means UNCLASSIFIED' -- the BBG row's class "
            "'equity' is inside the vocabulary; the row maps by key, names no identifier_namespace member")


def read_only_delegate(relpath, what, lines):
    text = (ROOT / relpath).read_text(encoding="utf-8", errors="ignore")
    for ln in lines:
        expect(ln in text, "deciding line missing in %s: %s" % (relpath, ln))
    return "READ-ONLY (runs only inside a live pipeline run). %s Deciding line(s): %s" % (what, " | ".join("`%s`" % ln for ln in lines))


# ---------------------------------------------------------------------------------------------
# The reader set.
# ---------------------------------------------------------------------------------------------
CLIENT = "infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py"
CLIENT_POS = "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classifications_dynamodb.py"
CLIENT_ATT = "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/etf_classifications_dynamodb.py"
POS_DIR = "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning"
ATT_DIR = "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution"
BD_GOLD = "data/black_diamond/scripts/gold"
COT_GOLD = "data/cot/scripts/gold"
E18_LINES = ["vocab = TableVocabulary.from_live_table(classifier)", "existing = existing_tickers(classifier)"]
E18_WHAT = ("Calls only TableVocabulary.from_live_table, existing_tickers and plan_rows, exercised in "
            "etf_classification_scheduled.py in this order.")

READERS = [
    (CLIENT, "ETFClassifier.get_*/find_by_* (the one client)", ex_client_read(CLIENT)),
    (CLIENT_POS, "ETFClassifier.get_*/find_by_* (Lambda copy, yang-generate-positioning)", ex_client_read(CLIENT_POS)),
    (CLIENT_ATT, "ETFClassifier.get_*/find_by_* (Lambda copy, yang-generate-holdings-attribution)", ex_client_read(CLIENT_ATT)),
    (CLIENT, "ETFClassifier.classify_holdings (static, no call site)", ex_client_classify_holdings(CLIENT)),
    (CLIENT_POS, "ETFClassifier.classify_holdings (static, no call site; Lambda copy)", ex_client_classify_holdings(CLIENT_POS)),
    (CLIENT_ATT, "ETFClassifier.classify_holdings (static, no call site; Lambda copy)", ex_client_classify_holdings(CLIENT_ATT)),
    (POS_DIR + "/lambda_function.py", "resolve_display_name/classify_etf/calculate_allocations/calculate_segment_breakdown", ex_positioning_lambda(POS_DIR)),
    (ATT_DIR + "/lambda_function.py", "resolve_display_name/extract_holdings_for_portfolio", ex_attribution_lambda(ATT_DIR)),
    ("data/etfs/scripts/gold/etf_positioning_publisher.py", "_display_name", ex_publisher()),
    ("data/assets/scripts/gold/build_satellites_registry.py", "load_classifier/classify", ex_satellites_registry()),
    ("data/assets/scripts/gold/build_satellites_characteristics.py", "load_identity", ex_satellites_characteristics()),
    (BD_GOLD + "/lib/etf_classifier.py", "ETFClassifier.classify/get_sub_asset_class/classify_with_identity (BD library)", ex_bd_classifier()),
    (COT_GOLD + "/lib/etf_classifier.py", "ETFClassifier.classify/get_sub_asset_class/classify_position (Cottonwood library)", ex_cot_classifier()),
    ("data/black_diamond/scripts/silver/build_bd_assets_dim.py", "apply_blend (BD assets dim)", ex_bd_assets_dim()),
    (BD_GOLD + "/D_04.client_portal_summary.py", "_classify_with_canonical", ex_bd_d04()),
    (BD_GOLD + "/C_06.client_mix_timeseries.py", "classify_series (BD mix timeseries)",
     ex_bd_series(BD_GOLD + "/C_06.client_mix_timeseries.py", "r7_bd_c06", BD_GOLD)),
    (BD_GOLD + "/D_03.composition_artifacts.py", "classify_series (BD composition artifacts)",
     ex_bd_series(BD_GOLD + "/D_03.composition_artifacts.py", "r7_bd_d03", BD_GOLD)),
    (BD_GOLD + "/E_25.aua_decomposition_audit.py", "classification_drift_audit (BD)", ex_bd_e25()),
    (COT_GOLD + "/C_06.client_mix_timeseries.py", "classify_series/classify_holding (Cottonwood mix timeseries)",
     ex_cot_series(COT_GOLD + "/C_06.client_mix_timeseries.py", "r7_cot_c06", COT_GOLD)),
    (COT_GOLD + "/D_03.composition_artifacts.py", "classify_series (Cottonwood composition artifacts)",
     ex_cot_series(COT_GOLD + "/D_03.composition_artifacts.py", "r7_cot_d03", COT_GOLD)),
    (COT_GOLD + "/D_04.client_portal_summary.py", "classify sites (Cottonwood client portal summary)",
     lambda: read_only_delegate(COT_GOLD + "/D_04.client_portal_summary.py",
                                "Calls only ETFClassifier.instance().classify(ticker, name), exercised in lib/etf_classifier.py above; a miss reads unknown, a hit is the row's asset_class verbatim.",
                                ["classifier = ETFClassifier.instance()", "result = classifier.classify("])),
    ("data/assets/scripts/gold/investor_reporting/holdings_snapshot.py", "annotate_classification/classify_security -> HoldingsSnapshot contract", ex_holdings_snapshot()),
    ("infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py", "TableVocabulary.from_live_table/existing_tickers/plan_rows", ex_scheduled()),
    (BD_GOLD + "/E_18.detect_new_securities.py", "E_18 scheduled caller (BD)",
     lambda: read_only_delegate(BD_GOLD + "/E_18.detect_new_securities.py", E18_WHAT, E18_LINES)),
    (COT_GOLD + "/E_18.detect_new_securities.py", "E_18 scheduled caller (COT)",
     lambda: read_only_delegate(COT_GOLD + "/E_18.detect_new_securities.py", E18_WHAT, E18_LINES)),
    ("infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py", "scan_all/plan_unlabelled/label_row_if_unlabelled", ex_label_legacy()),
    ("infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py", "scan_all/plan_absent_kind/set_kind_if_absent", ex_set_kind()),
    ("infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py", "read_existing/merge_item (seed source does not carry the BBG key)", ex_seed_classifications()),
    ("infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py", "main (--dry-run, --kind-only)/put_row_if_unclassified", ex_seed_constituents()),
    ("data/black_diamond/scripts/classification/seed_canonical_securities.py", "_yang_conflicts", ex_seed_canonical()),
    ("data/black_diamond/scripts/classification/seed_bd_securities.py", "seed (one-time copy into bd-securities)", ex_seed_bd()),
    ("infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py", "table_rows_at_build/existing_tickers", ex_classify_residual()),
    ("infra/aws/lambda/v2_portal/yang_pipeline/write-model-rows.py", "TableVocabulary.from_live_table/existing_tickers/plan_rows (the model path's writer)", ex_write_model_rows()),
    ("lib/research/api/scoped_amgt.py", "_join_classification/_classification_for_ticker", ex_scoped_amgt()),
    ("lib/research/identity/positioning_chain.py", "read_etf_classifications/resolve_one", ex_positioning_chain()),
    ("infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py", "classifications_reader (the real paginated Scan) + build_catalogue + entry_for_ticker", ex_comparison_catalogue()),
    ("infra/aws/lambda/investor-reporting/_scope/maintained_sources.py", "_classified_etf (a named classified ETF as a comparison key)", ex_maintained_sources()),
    ("infra/aws/lambda/investor-reporting/ycharts/generate/entry.py", "read_comparison_catalogue (delegates to build_catalogue)",
     lambda: read_only_delegate("infra/aws/lambda/investor-reporting/ycharts/generate/entry.py",
                                "Delegates to comparison_catalogue.build_catalogue (exercised above).",
                                ["return _catalogue.build_catalogue(tenant=ctx.tenant, read_classifications=read_classifications)"])),
    ("infra/aws/lambda/investor-reporting/reports/generate_installed.py", "compose_ports: wires read_classifications to the real reader",
     lambda: read_only_delegate("infra/aws/lambda/investor-reporting/reports/generate_installed.py",
                                "Composition only: installs comparison_catalogue.classifications_reader (exercised above); it reads no row itself.",
                                ['"read_classifications": comparison_catalogue.classifications_reader(clients["dynamodb"]),'])),
    ("infra/aws/lambda/investor-reporting/reports/request_composition.py", "comparison source authority (a MAINTAINED_RECORD at dynamodb:etf-classifications)",
     lambda: read_only_delegate("infra/aws/lambda/investor-reporting/reports/request_composition.py",
                                "Reads no table row: it checks a comparison item's source descriptor, which maintained_sources._classified_etf builds (exercised above); a BBG key never reaches it as a comparison.",
                                ['source.get("canonical_location") == "dynamodb:etf-classifications"'])),
    ("infra/aws/lambda/investor-reporting/ycharts/generate/prospect_submission.py", "read_classifications port pass-through",
     lambda: read_only_delegate("infra/aws/lambda/investor-reporting/ycharts/generate/prospect_submission.py",
                                "Holds the injected read_classifications port and hands it to resolve_comparison_fields; reads no row itself.",
                                ["self.read_classifications = read_classifications"])),
    ("portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts", "CANONICAL_CLASSES / normalizeMixTo4Class (portal asset-class mapping)", read_only_composition),
    ("portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts", "asset_class wire type", read_only_wire_holdings),
    ("portal/src/pages/InvestorReporting/contracts/wire/ComparisonCatalogue.ts", "comparison catalogue wire type + readCatalogue", read_only_wire_catalogue),
    ("org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md", "IRPT_DASHBD C-CLASSES consumer (PRD only, no code yet)", read_only_dashbd),
]

# Code files that name the table / namespace / library and are NOT readers of the table, each with the reason.
INTAKE_REASON = ("IRPT intake / analysis path: `identifier_namespace` here is the namespace of a SUBMITTED PORTFOLIO "
                 "holding (AnalysisRequest enum TICKER/CUSIP/ISIN/CASH/MODEL/UNMATCHED), not an etf-classifications row; "
                 "the file reads no table row")
NOT_READERS = dict(r6.NOT_READERS)
NOT_READERS.update({
    "infra/aws/lambda/investor-reporting/intake/corrections.py": INTAKE_REASON,
    "infra/aws/lambda/investor-reporting/intake/custody_portfolio.py": INTAKE_REASON,
    "infra/aws/lambda/investor-reporting/intake/parse.py": INTAKE_REASON,
    "infra/aws/lambda/investor-reporting/intake/portfolio.py": INTAKE_REASON,
    "infra/aws/lambda/investor-reporting/ycharts/generate/normalized_input.py": INTAKE_REASON,
    "infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py": INTAKE_REASON,
})
COVERED_PATHS = {p for p, _f, _fn in READERS} | set(NOT_READERS)
SEARCH_PATTERNS = ["etf-classifications", "etf_classifications_dynamodb", "identifier_namespace", "classified_by",
                   "lib.etf_classifier"]
CODE_EXT = (".py", ".ts", ".tsx", ".js", ".mjs", ".cjs")
SEARCH_SCOPE = ("tracked files outside org/, docs/, archive/ with a code, config or shell extension (py ts tsx js mjs cjs tf "
                "sh json yaml yml); the portal submodule is not in git ls-files, its readers are listed by hand")
# The comp-find denominators, measured at build (one-time record, not re-run by this check).
COMP_FIND_AT_BUILD = {
    "measured_by": "comp-find <pattern> --files --all, corpus=all, worktree root wk-secclass-r7-13, 2026-10-05 (a one-time record, not re-run by this check)",
    "etf-classifications": {"hits": 6849, "files_scanned": 53766},
    "etf_classifications_dynamodb": {"hits": 612, "files_scanned": 53767},
    "identifier_namespace": {"hits": 926, "files_scanned": 53768},
}


def tracked_files():
    out = subprocess.run(["git", "ls-files"], cwd=str(ROOT), capture_output=True, text=True, timeout=120).stdout
    return [f for f in out.split("\n") if f]


def search_census(files):
    texts = {}
    for f in files:
        if f.startswith(("org/", "docs/", "archive/", ".scratch")):
            continue
        if f.endswith(r6.STRUCTURAL + CODE_EXT + (".yaml", ".yml")):
            try:
                texts[f] = (ROOT / f).read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
    search, universe = [], {}
    for pat in SEARCH_PATTERNS:
        hits = files_n = 0
        for f, t in texts.items():
            c = t.count(pat)
            if c:
                hits += c
                files_n += 1
                if f.endswith(CODE_EXT):
                    universe.setdefault(f, []).append(pat)
        search.append({"pattern": pat, "hits": hits, "files": files_n})
    return search, universe


def run_one(fn):
    verdict, evidence = r6.run_one(fn)
    if verdict == "TOLERATES" and evidence.startswith("READ-ONLY"):
        verdict = "READ-ONLY"
    return verdict, evidence


def main() -> int:
    files = tracked_files()
    search, universe = search_census(files)
    readers = []
    for path, func, fn in READERS:
        verdict, evidence = run_one(fn)
        readers.append({"path": path, "function": func, "verdict": verdict, "evidence": evidence})
    missing = [f for f in sorted(universe) if f not in COVERED_PATHS and not r6.is_test_path(f)]
    r6_doc = json.loads(R6_CENSUS.read_text(encoding="utf-8"))
    r6_paths = {r["path"] for r in r6_doc["readers"]}
    now_paths = {r["path"] for r in readers}
    verdicts = ("TOLERATES", "READ-ONLY", "CRASHES", "REFUSES", "MISKEYS", "FAILS-CONTRACT")
    counts = {k: sum(1 for r in readers if r["verdict"] == k) for k in verdicts}
    doc = {
        "what": "SC-e-16 BLOOMBERG-namespace reader census: every reader of etf-classifications exercised on a BBG:<ticker>:<exch> row",
        "bbg_rows": {"rows": [ROW_A, ROW_B], "key": KEY,
                     "second_shape": "sub_asset_class absent, low_confidence true",
                     "controls": [c["ticker"] for c in CONTROLS],
                     "ruling": "1.0.0_SA_CTO RULINGS batch 257 Q1 (org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md)"},
        "readers": readers,
        "denominator": {"readers_exercised_or_read": len(readers),
                        "round6_model_reader_census_entries": len(r6_doc["readers"]),
                        "added_since_round6": sorted(now_paths - r6_paths),
                        "dropped_since_round6": sorted(r6_paths - now_paths),
                        "code_files_naming_the_table_outside_org_docs_archive": len(universe),
                        "of_which_tests": sum(1 for f in universe if r6.is_test_path(f)),
                        "of_which_declared_not_readers": sum(1 for f in universe if f in NOT_READERS),
                        "uncensused": missing},
        "search": search,
        "search_scope": SEARCH_SCOPE,
        "comp_find_at_build": COMP_FIND_AT_BUILD,
        "not_readers": NOT_READERS,
    }
    OUT.write_text(json.dumps(doc, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    print("WROTE %s" % OUT.relative_to(ROOT).as_posix())
    for r in readers:
        print("READER %-15s %s :: %s" % (r["verdict"], r["path"], r["function"]))
    for f in missing:
        print("UNCENSUSED %s" % f)
    print("BBG-READER-CENSUS readers=%d tolerates=%d read_only=%d crashes=%d refuses=%d miskeys=%d fails_contract=%d"
          % (len(readers), counts["TOLERATES"], counts["READ-ONLY"], counts["CRASHES"], counts["REFUSES"],
             counts["MISKEYS"], counts["FAILS-CONTRACT"]))
    if not (counts["CRASHES"] or counts["REFUSES"] or counts["MISKEYS"] or counts["FAILS-CONTRACT"] or missing):
        print("BBG-READER-TOLERATED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
