#!/usr/bin/env python3
"""SC-e-15 (MDPF_SECCLASS round 6): the MODEL_ROWS reader census.

Every reader of the `etf-classifications` table is exercised through its REAL function on
synthetic `classified_by = "model"` rows built from the real R4 Kimi K3 results
(R4_MODEL_CLASSIFY_CENSUS_20260930.json: every result with a non-null asset_class, 260 rows).
ONLY the table is stubbed (an in-memory DynamoDB double that returns what boto3 returns:
Decimal numbers, bool flags, projected scans, paginated scans, conditional writes). No AWS call
is made and nothing is written anywhere but the census JSON.

A reader is one verdict: TOLERATES (exercised, no crash, no refusal, no contract failure),
CRASHES, REFUSES (raised a refusal for the model row), FAILS-CONTRACT (an output breaks a strict
contract: the published Holdings schema, the MDPF_SECCLASS contract, a closed catalogue schema),
or READ-ONLY (not runnable here; the deciding line is recorded and, where the file is present,
re-verified by this check).

COMPLETENESS GUARD: every tracked code file that names the table (`etf-classifications`,
`classified_by`, `etf_classifications_dynamodb`) outside org/, docs/ and archive/ must be in
READERS or NOT_READERS below (or match a structural rule: test, terraform, shell, json). A file
that is in neither is printed `UNCENSUSED` and withholds MODEL-READER-TOLERATED: a reader added
after this census was cut cannot slip past a fresh run.

Run from the worktree root:  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_model_reader_census.py
Prints `MODEL-READER-CENSUS readers=.. tolerates=.. read_only=.. crashes=.. refuses=.. fails_contract=..`
and, when crashes, refuses, fails_contract and UNCENSUSED are all zero, `MODEL-READER-TOLERATED`.
ASCII only.
"""
from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
import re
import subprocess
import sys
import threading
import traceback
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
assert (ROOT / ".tools").is_dir() and (ROOT / "org").is_dir(), "not run from inside the repo tree: %s" % ROOT

DELIV = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
R4_CENSUS = DELIV / "R4_MODEL_CLASSIFY_CENSUS_20260930.json"
R2_CENSUS = DELIV / "R2_CUSIP_CENSUS_20260930.json"
OUT = DELIV / "R6_MODEL_READER_CENSUS_20260930.json"
CONTRACT_MDPF = ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json"
HOLDINGS_SCHEMA = ROOT / "docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json"
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
YANG = ROOT / "infra/aws/lambda/v2_portal/yang_pipeline"
TABLE = "etf-classifications"
EXERCISE_TIMEOUT_S = 120

# ---------------------------------------------------------------------------------------------
# The model rows: real R4 results, in the shape the planned write puts in the table.
# ---------------------------------------------------------------------------------------------


def build_model_rows() -> list:
    census = json.loads(R4_CENSUS.read_text(encoding="utf-8"))
    rows, n = [], 0
    for r in census["results"]:
        if not r.get("asset_class"):
            continue
        n += 1
        # A name-only entry has no ticker key (it is outside the planned write); it still gets a
        # synthetic ticker here so the readers see every asset class the model produced.
        ticker = r.get("key") or ("MDLX%03d" % n)
        row = {
            "ticker": ticker,
            "name": str(r.get("name") or ticker),
            "asset_class": r["asset_class"],
            "classified_by": "model",
            "classification_confidence": Decimal(str(r["confidence"])),  # boto3 returns Decimal
            "low_confidence": bool(r["low_confidence"]),
            "updated_by": "classify-residual-model",
        }
        if r.get("sub_asset_class"):
            row["sub_asset_class"] = r["sub_asset_class"]
        rows.append(row)
    return rows


CONTROL_ROWS = [
    {"ticker": "SPY", "asset_class": "equity", "sub_asset_class": "US Large Cap", "management_style": "passive",
     "sector": "Broad Market", "name": "SPDR S&P 500 ETF Trust", "classified_by": "seed"},
    {"ticker": "LEGACYX", "asset_class": "fixed_income", "sub_asset_class": "Short Duration",
     "management_style": "active", "name": "Legacy Row With No Label"},  # no classified_by: reads as legacy
    {"ticker": "ALTSEED", "asset_class": "alternatives", "sub_asset_class": "Real Estate", "name": "Alt Seed",
     "classified_by": "seed"},
]


def all_rows() -> list:
    return copy.deepcopy(CONTROL_ROWS) + build_model_rows()


# ---------------------------------------------------------------------------------------------
# The table double and the boto3 patch.
# ---------------------------------------------------------------------------------------------
from botocore.exceptions import ClientError  # noqa: E402
from boto3.dynamodb.types import TypeSerializer  # noqa: E402


def _cond_fail(op):
    return ClientError({"Error": {"Code": "ConditionalCheckFailedException", "Message": "cond"}}, op)


class FakeTable:
    PAGE = 100

    def __init__(self, rows=(), name=TABLE):
        self.name = name
        self.rows = {r["ticker"]: copy.deepcopy(r) for r in rows}
        self.writes = []

    def get_item(self, Key, **kw):
        it = self.rows.get(Key["ticker"])
        return {"Item": copy.deepcopy(it)} if it else {}

    def query(self, IndexName, KeyConditionExpression, ExpressionAttributeValues, **kw):
        attr = {"asset-class-index": "asset_class", "sub-asset-class-index": "sub_asset_class"}[IndexName]
        want = list(ExpressionAttributeValues.values())[0]
        return {"Items": [copy.deepcopy(r) for r in self.rows.values() if r.get(attr) == want]}

    def scan(self, ProjectionExpression=None, Select=None, ExclusiveStartKey=None, **kw):
        keys = sorted(self.rows)
        start = keys.index(ExclusiveStartKey["ticker"]) + 1 if ExclusiveStartKey else 0
        page = keys[start:start + self.PAGE]
        if Select == "COUNT":
            resp = {"Count": len(page)}
        else:
            attrs = [a.strip() for a in ProjectionExpression.split(",")] if ProjectionExpression else None
            items = []
            for k in page:
                row = self.rows[k]
                items.append({a: copy.deepcopy(row[a]) for a in attrs if a in row} if attrs else copy.deepcopy(row))
            resp = {"Items": items}
        if start + self.PAGE < len(keys):
            resp["LastEvaluatedKey"] = {"ticker": page[-1]}
        return resp

    def _check(self, cond, item, op):
        if not cond:
            return
        for attr in re.findall(r"attribute_not_exists\((\w+)\)", cond):
            if item is not None and (attr == "ticker" or attr in item):
                raise _cond_fail(op)

    def put_item(self, Item, ConditionExpression=None, **kw):
        self._check(ConditionExpression, self.rows.get(Item["ticker"]), "PutItem")
        self.rows[Item["ticker"]] = copy.deepcopy(Item)
        self.writes.append(("put", Item["ticker"]))
        return {}

    def update_item(self, Key, UpdateExpression, ConditionExpression=None, ExpressionAttributeValues=None,
                    ExpressionAttributeNames=None, **kw):
        item = self.rows.get(Key["ticker"])
        self._check(ConditionExpression, item, "UpdateItem")
        if item is None:
            item = self.rows[Key["ticker"]] = {"ticker": Key["ticker"]}
        names = ExpressionAttributeNames or {}
        for part in UpdateExpression.split("SET ", 1)[1].split(","):
            lhs, rhs = [x.strip() for x in part.split("=", 1)]
            item[names.get(lhs, lhs)] = (ExpressionAttributeValues or {})[rhs]
        self.writes.append(("update", Key["ticker"]))
        return {}


class FakeResource:
    def __init__(self, tables):
        self.tables = tables

    def Table(self, name):  # noqa: N802 -- boto3's own spelling
        return self.tables.setdefault(name, FakeTable([], name))


class _Dead:
    """Any non-DynamoDB boto3 client: no network, any call raises."""

    def __init__(self, service):
        self._service = service

    def __getattr__(self, name):
        def _refuse(*a, **k):
            raise RuntimeError("UNSTUBBED boto3.client(%r).%s called" % (self._service, name))
        return _refuse


class FakeDdbClient:
    """boto3.client('dynamodb').scan: DynamoDB-typed items, paginated."""

    def __init__(self, tables):
        self.tables = tables
        self._ser = TypeSerializer()

    def scan(self, TableName, ExclusiveStartKey=None, **kw):
        t = self.tables.get(TableName) or FakeTable([], TableName)
        resp = t.scan(ExclusiveStartKey={"ticker": ExclusiveStartKey["ticker"]["S"]} if ExclusiveStartKey else None)
        out = {"Items": [{k: self._ser.serialize(v) for k, v in it.items()} for it in resp["Items"]]}
        if "LastEvaluatedKey" in resp:
            out["LastEvaluatedKey"] = {"ticker": {"S": resp["LastEvaluatedKey"]["ticker"]}}
        return out


class World:
    """One exercise's private table world; patches the real boto3 module for its duration."""

    def __init__(self, rows=None):
        self.tables = {TABLE: FakeTable(all_rows() if rows is None else rows)}
        self.main = self.tables[TABLE]

    def __enter__(self):
        import boto3
        self._saved = (boto3.resource, boto3.client)
        boto3.resource = lambda service="dynamodb", *a, **k: FakeResource(self.tables)
        boto3.client = lambda service, *a, **k: (FakeDdbClient(self.tables) if service == "dynamodb" else _Dead(service))
        return self

    def __exit__(self, *exc):
        import boto3
        boto3.resource, boto3.client = self._saved
        return False


# ---------------------------------------------------------------------------------------------
# Module loading: by path, under a private name, leaving sys.path / sys.modules as found.
# ---------------------------------------------------------------------------------------------


@contextlib.contextmanager
def isolated(paths=()):
    before_mods = set(sys.modules)
    before_path = list(sys.path)
    for p in reversed([str(x) for x in paths]):
        sys.path.insert(0, p)
    try:
        yield
    finally:
        doomed = []
        for k in list(sys.modules):
            if k in before_mods:
                continue
            m = sys.modules[k]
            f = getattr(m, "__file__", None) or ""
            try:
                locs = [str(Path(x).resolve()) for x in list(getattr(m, "__path__", None) or [])]
            except Exception:  # noqa: BLE001 -- a namespace path whose parent is already gone: ours, purge it
                locs = [str(ROOT)]
            if (f and str(ROOT) in str(Path(f).resolve())) or any(str(ROOT) in x for x in locs):
                doomed.append(k)
        for k in doomed:
            sys.modules.pop(k, None)
        sys.path[:] = before_path


def load(relpath, name):
    spec = importlib.util.spec_from_file_location(name, str(ROOT / relpath))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


class Verdict(Exception):
    def __init__(self, verdict, evidence):
        super().__init__(evidence)
        self.verdict, self.evidence = verdict, evidence


def fails_contract(msg):
    raise Verdict("FAILS-CONTRACT", msg)


def refuses(msg):
    raise Verdict("REFUSES", msg)


def expect(cond, msg):
    if not cond:
        fails_contract(msg)


MODEL = build_model_rows()
MODEL_BY = {r["ticker"]: r for r in MODEL}
CLASSES = sorted({r["asset_class"] for r in MODEL})


def jdump(obj):
    return json.dumps(obj, sort_keys=True)  # strict: a Decimal / set here is the crash this census hunts


# ---------------------------------------------------------------------------------------------
# The exercises. Each returns an evidence string on TOLERATES, or raises.
# ---------------------------------------------------------------------------------------------


def ex_client_read(relpath):
    with World(), isolated([ROOT / Path(relpath).parent]):
        mod = load(relpath, "ex_client_mod")
        clf = mod.ETFClassifier()
        for r in MODEL:
            t = r["ticker"]
            got = clf.get_classification(t)
            expect(got == r, "%s: get_classification changed the row" % t)
            expect(got["classified_by"] == "model" and got["low_confidence"] is r["low_confidence"]
                   and got["classification_confidence"] == r["classification_confidence"],
                   "%s: model attributes lost" % t)
            expect(clf.get_asset_class(t) == r["asset_class"], "%s: get_asset_class" % t)
            expect(clf.get_sub_asset_class(t) == r.get("sub_asset_class", ""), "%s: get_sub_asset_class" % t)
            expect(clf.get_management_style(t) == "unknown", "%s: get_management_style" % t)
            expect(clf.get_sector(t) == "", "%s: get_sector" % t)
        found = 0
        for ac in CLASSES:
            want = sorted(r["ticker"] for r in MODEL if r["asset_class"] == ac)
            have = sorted(i["ticker"] for i in clf.find_by_asset_class(ac) if i.get("classified_by") == "model")
            expect(want == have, "find_by_asset_class(%s): %d model rows expected, %d returned" % (ac, len(want), len(have)))
            found += len(have)
        subs = sorted({r["sub_asset_class"] for r in MODEL if r.get("sub_asset_class")})
        for sc in subs:
            want = sorted(r["ticker"] for r in MODEL if r.get("sub_asset_class") == sc)
            have = sorted(i["ticker"] for i in clf.find_by_sub_asset_class(sc) if i.get("classified_by") == "model")
            expect(want == have, "find_by_sub_asset_class(%s) mismatch" % sc)
        return ("%d model rows through get_classification/get_asset_class/get_sub_asset_class/get_management_style/"
                "get_sector verbatim (Decimal confidence and bool flag intact); find_by_asset_class over %d classes "
                "returned all %d model rows; find_by_sub_asset_class over %d sub classes matched"
                % (len(MODEL), len(CLASSES), found, len(subs)))


def ex_client_classify_holdings(relpath):
    """ETFClassifier.classify_holdings (static): result[asset_class] += weight over a fixed 4-key dict."""
    with World(), isolated([ROOT / Path(relpath).parent]):
        mod = load(relpath, "ex_client_ch_mod")
        ok_classes = {"fixed_income", "equity"}
        safe = [{"ticker": r["ticker"], "weight": 0.01} for r in MODEL if r["asset_class"] in ok_classes]
        mod.ETFClassifier.classify_holdings(safe)
        bad = next(r for r in MODEL if r["asset_class"] not in ok_classes)
        control_err = None
        try:
            mod.ETFClassifier.classify_holdings([{"ticker": "ALTSEED", "weight": 0.01}])
        except KeyError as exc:
            control_err = repr(exc)
        try:
            mod.ETFClassifier.classify_holdings([{"ticker": bad["ticker"], "weight": 0.01}])
        except KeyError as exc:
            raise Verdict("CRASHES", "%r on model row %s (asset_class=%s): result[asset_class] += weight over a dict "
                          "seeded with fixed_income/equity/hedge/unknown only. PRE-EXISTING, not caused by the model "
                          "row: the control seed row ALTSEED (alternatives, classified_by=seed) raises %s the same way, "
                          "and a live read of the table at build (2026-09-30, 2657 rows) already holds alternatives 4, "
                          "commodities 8, structured 5. Zero functional call sites (comp-find 'classify_holdings(' regex' "
                          "= 8 hits at build: 7 definitions plus one unrelated INF function)."
                          % (exc, bad["ticker"], bad["asset_class"], control_err))
        return "classify_holdings tolerated every class"


def _positioning_holdings():
    rows = MODEL[:]
    w = 1.0 / len(rows)
    return [{"ticker": r["ticker"], "weight": w} for r in rows]


def ex_positioning_lambda(dirrel):
    d = ROOT / dirrel
    with World(), isolated([d]):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            mod = load(dirrel + "/lambda_function.py", "ex_yang_positioning")
            for r in MODEL:
                t = r["ticker"]
                nm = mod.resolve_display_name(t, "FALLBACK")
                expect(nm == (r["name"] if r["name"] != t else "FALLBACK"), "%s: resolve_display_name %r" % (t, nm))
                expect(mod.classify_etf(t) == r["asset_class"], "%s: classify_etf" % t)
                expect(mod.classify_management_style(t) == "passive", "%s: management style default" % t)
            hold = _positioning_holdings()
            assets, mgmt = mod.calculate_allocations(hold)
            expect(abs(sum(assets.values()) - 100.0) < 1.0, "allocations do not sum to 100: %s" % sum(assets.values()))
            for c in CLASSES:
                expect(assets.get(c, 0) > 0, "class %s vanished from the served allocation" % c)
            seg = mod.calculate_segment_breakdown(hold)
            jdump({"assets": assets, "mgmt": mgmt, "seg": seg})
        return ("%d model rows through resolve_display_name/classify_etf/classify_management_style; "
                "calculate_allocations over all %d classes summed to %.1f with every class present; "
                "calculate_segment_breakdown ok; served dicts json.dumps strictly"
                % (len(MODEL), len(CLASSES), sum(assets.values())))


def ex_attribution_lambda(dirrel):
    import pandas as pd
    d = ROOT / dirrel
    with World() as w, isolated([d]):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            mod = load(dirrel + "/lambda_function.py", "ex_yang_attribution")
            for r in MODEL:
                t = r["ticker"]
                nm = mod.resolve_display_name(t, w.main.rows[t], None)
                expect(nm == (r["name"] if r["name"] != t else t), "%s: resolve_display_name %r" % (t, nm))
            sample = MODEL[:60]
            ncol = 15
            rows = []
            for r in sample:
                rows.append([r["ticker"], None, None, None, None, 0.02, 0.01, 0.008, 0.009, 0.0, 0.0, 0.0, 0.001, 0.001, 0.0])
            rows.append([None, "Total"] + [None] * 3 + [1.0, 0.02, 1.0, 0.02, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
            df = pd.DataFrame(rows, columns=list(range(ncol)))
            res = mod.extract_holdings_for_portfolio(df, 5, 0)
            hold = res["holdings"]
            expect(len(hold) == len(sample), "a model row was silently dropped: %d of %d holdings (the function "
                   "swallows a per-row exception into a warning)" % (len(hold), len(sample)))
            got = {h["ticker"]: h for h in hold}
            for r in sample:
                h = got[r["ticker"]]
                want = {"fixed_income": "Fixed Income", "equity": "Equity", "hedge": "Equity"}.get(r["asset_class"], r["asset_class"])
                expect(h["asset_class"] == want, "%s: asset_class %r, expected %r" % (r["ticker"], h["asset_class"], want))
            jdump(res)
        return ("%d model rows through resolve_display_name; extract_holdings_for_portfolio over a synthetic "
                "attribution sheet of %d model tickers kept %d of %d holdings (none dropped), classes %s, result "
                "json.dumps strictly" % (len(MODEL), len(sample), len(hold), len(sample),
                                          sorted({h["asset_class"] for h in hold})))


def ex_publisher():
    rel = "data/etfs/scripts/gold/etf_positioning_publisher.py"
    with World(), isolated([SHARED, ROOT / "data/etfs/scripts/gold", ROOT / "lib"]):
        mod = load(rel, "ex_etf_positioning_publisher")
        for r in MODEL:
            t = r["ticker"]
            nm = mod._display_name(t, "RAW ISSUER STRING")
            expect(nm == r["name"], "%s: _display_name %r != registry name" % (t, nm))
        return "%d model rows through _display_name (registry name wins, classifier cached per ticker)" % len(MODEL)


def ex_satellites_registry():
    rel = "data/assets/scripts/gold/build_satellites_registry.py"
    with World(), isolated([ROOT / "data/assets/scripts/gold", ROOT / "lib"]):
        mod = load(rel, "ex_build_satellites_registry")
        clf = mod.load_classifier()
        for r in MODEL:
            ac, sac = mod.classify(clf, r["ticker"])
            expect(ac == r["asset_class"] and sac == (r.get("sub_asset_class")), "%s: classify -> %r" % (r["ticker"], (ac, sac)))
            jdump([ac, sac])
        return "%d model rows through load_classifier()+classify() -> (asset_class, sub_asset_class) strings, json-safe" % len(MODEL)


def ex_satellites_characteristics():
    rel = "data/assets/scripts/gold/build_satellites_characteristics.py"
    with World(), isolated([ROOT / "data/assets/scripts/gold", ROOT / "lib"]):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            mod = load(rel, "ex_build_satellites_characteristics")
            tickers = [r["ticker"] for r in MODEL]
            identity, stats = mod.load_identity(tickers)
        for r in MODEL:
            got = identity[r["ticker"]]
            expect(got.get("name") == r["name"] and got.get("management_style") is None,
                   "%s: identity %r" % (r["ticker"], got))
        jdump(identity)
        return ("load_identity over %d model tickers -> name served, management_style None (absent, not guessed), "
                "missing=%s, json-safe" % (len(tickers), stats.get("identity_missing")))


def ex_bd_classifier():
    rel = "data/black_diamond/scripts/gold/lib/etf_classifier.py"
    with World(), isolated([SHARED, ROOT / "data/black_diamond/scripts/gold"]):
        mod = load(rel, "ex_bd_etf_classifier")
        clf = mod.ETFClassifier(table_name=TABLE)
        for r in MODEL:
            t = r["ticker"]
            expect(clf.classify(t, r["name"]) == r["asset_class"], "%s: classify" % t)
            expect(clf.get_sub_asset_class(t, r["name"]) == r.get("sub_asset_class", ""), "%s: sub" % t)
        expect(clf.classify("NOSUCHTKR", "no such") in ("", getattr(clf, "UNKNOWN", "")), "miss did not read as unknown")
        return "%d model rows through classify()/get_sub_asset_class() verbatim; a miss still reads unknown" % len(MODEL)


def _bd_clf():
    from lib.etf_classifier import ETFClassifier  # the BD library, `lib` = gold/lib (gold is first on sys.path)
    return ETFClassifier(table_name=TABLE)


def ex_bd_assets_dim():
    import pandas as pd
    gold = ROOT / "data/black_diamond/scripts/gold"
    silver = ROOT / "data/black_diamond/scripts/silver"
    with World(), isolated([SHARED, gold, silver, ROOT / "lib"]):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            mod = load("data/black_diamond/scripts/silver/build_bd_assets_dim.py", "ex_build_bd_assets_dim")
            clf = _bd_clf()
            coarse = sorted(mod.COARSE_SUPER_CLASSES)[0]
            dim = pd.DataFrame({
                "ticker": [r["ticker"] for r in MODEL],
                "asset_name": [r["name"] for r in MODEL],
                "asset_super_class_bd": [coarse] * len(MODEL),
            })
            res = mod.apply_blend(dim, classifier=clf)
        expect(len(res) == len(MODEL), "apply_blend dropped rows: %d of %d" % (len(res), len(MODEL)))
        cols = [c for c in res.columns if "canonical" in c]
        return ("apply_blend over %d model-row assets (all coarse BD super class) kept every row, canonical columns %s"
                % (len(res), cols))


def ex_bd_d04():
    gold = ROOT / "data/black_diamond/scripts/gold"
    with World(), isolated([SHARED, gold, ROOT / "lib"]):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            mod = load("data/black_diamond/scripts/gold/D_04.client_portal_summary.py", "ex_d04")
            clf = _bd_clf()
            for r in MODEL:
                res = mod._classify_with_canonical(r["ticker"], r["name"], clf)
                expect(res[0] == r["asset_class"] and res[3] == "etf-classifications", "%s: %r" % (r["ticker"], res))
                jdump(res)
        return "_classify_with_canonical over %d model rows -> (class, class, sub, 'etf-classifications'), json-safe" % len(MODEL)


def ex_holdings_snapshot():
    """The IRPT Holdings producer: canonical row -> node members -> the published strict contract."""
    rel = "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py"
    hs_dir = ROOT / "data/assets/scripts/gold/investor_reporting"
    with World(), isolated([hs_dir, ROOT / "lib", SHARED]):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            mod = load(rel, "ex_holdings_snapshot")
            canonical = None
            sys.path.insert(0, str(SHARED))
            import etf_classifications_dynamodb as canonical_mod
            canonical = canonical_mod.ETFClassifier()

            class _Fallback:
                _ticker_map, _name_map = {}, {}

                def classify(self, ticker, name):
                    return ""

                def get_sub_asset_class(self, ticker, name=None):
                    return ""

            ec = mod  # `ec` is only consulted on the fallback path
            clf = mod._NarrowedClassifier(canonical, _Fallback())
            schema = json.loads(HOLDINGS_SCHEMA.read_text(encoding="utf-8"))
            item_schema = schema["properties"]["nodes"]["items"]
            validator = mod.contract_validator_class()(item_schema)
            nodes = []
            for i, r in enumerate(MODEL):
                nodes.append({
                    "node_id": "n%03d" % i, "level": 3, "node_kind": "SECURITY", "basis": "OBSERVED",
                    "amount": {"value": 1000.0, "units": "USD", "denominator": {"kind": "ACCOUNT", "value": 1000000.0}},
                    "percentages": {"of_parent": 0.1, "of_total": 0.1},
                    "provenance": {"producer": "r6_model_reader_census", "join_method": "synthetic",
                                   "join_matched": 1, "join_attempted": 1, "claim": "held"},
                    "display": {"label": r["ticker"], "symbol": r["ticker"], "description": r["name"]},
                })
            base_errs = [e for n in nodes[:1] for e in validator.iter_errors(n)]
            census = mod.annotate_classification(nodes, classifier=(ec, clf))
        errs = []
        for n in nodes:
            errs.extend("%s: %s" % (n["node_id"], e.message) for e in validator.iter_errors(n))
        baseline_note = "baseline node (no members) had %d schema error(s)" % len(base_errs)
        expect(not errs, "served node fails the published HoldingsSnapshot contract: %s | %s" % (errs[:3], baseline_note))
        for n, r in zip(nodes, MODEL):
            expect(n["asset_class"] == r["asset_class"] and n["asset_class_basis"] == "TABLE", "%s: served members %r" % (r["ticker"], n))
            leaked = sorted(set(n) & {"classified_by", "classification_confidence", "low_confidence", "class_source"})
            expect(not leaked, "%s: model attribute leaked onto the served node: %s" % (r["ticker"], leaked))
        # Negative control: the validator would refuse a leaked attribute (the closed schema is real).
        probe = dict(nodes[0], classification_confidence=0.62)
        control_refused = any(True for _ in validator.iter_errors(probe))
        expect(control_refused, "negative control failed: a leaked classification_confidence was accepted")
        jdump(nodes)
        return ("annotate_classification over %d SECURITY nodes from model rows (classify_security -> canonical row -> "
                "asset_class/sub_asset_class, basis TABLE, by_class_source %s); every served node validates against "
                "%s (additionalProperties false); no model attribute reaches a node; negative control (a leaked "
                "classification_confidence) IS refused by the same validator"
                % (len(nodes), census.get("by_class_source"), HOLDINGS_SCHEMA.relative_to(ROOT)))


def ex_scheduled():
    with World() as w, isolated([SHARED]):
        mod = load("infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py", "ex_scheduled")
        import etf_classifications_dynamodb as cm
        clf = cm.ETFClassifier()
        vocab = mod.TableVocabulary.from_live_table(clf)
        existing = mod.existing_tickers(clf)
        for c in CLASSES:
            expect(c in vocab.asset_classes, "vocabulary lost class %s" % c)
        expect(all(r["ticker"] in existing for r in MODEL), "existing_tickers missed a model row")
        held = [(r["ticker"], r["name"]) for r in MODEL] + [("ZZNEWX", "Some New Fund")]
        plan, unresolved, seed_pending = mod.plan_rows(
            held, vocab=vocab, existing_tickers=existing, seed_source_tickers=set(),
            bd_securities_lookup=lambda t: {"asset_class": "equity", "sub_asset_class": None} if t == "ZZNEWX" else None,
            gics_lookup=lambda t: None, schwab_lookup=lambda t: None)
        planned = {p["ticker"] for p in plan}
        expect(not (planned & set(MODEL_BY)), "plan_rows re-planned a model ticker: %s" % sorted(planned & set(MODEL_BY))[:5])
        return ("TableVocabulary.from_live_table saw all %d model classes (paginated projected scan of %d rows); "
                "existing_tickers held all %d model tickers; plan_rows over %d held securities planned only the %d new "
                "one(s) and never a model ticker (the conditional-absence half). E_18 bd/cot call exactly this "
                "sequence." % (len(CLASSES), len(w.main.rows), len(MODEL), len(held), len(planned)))


def ex_label_legacy():
    with World() as w, isolated([YANG]):
        mod = load("infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py", "ex_label_legacy")
        items = mod.scan_all(w.main)
        unl = mod.plan_unlabelled(items)
        expect(unl == ["LEGACYX"], "plan_unlabelled %r (expected only the unlabelled control row)" % unl[:5])
        try:
            mod.label_row_if_unlabelled(w.main, MODEL[0]["ticker"])
            fails_contract("label update overwrote a model row's classified_by")
        except mod.RowAlreadyLabelled:
            pass
        expect(mod.label_row_if_unlabelled(w.main, "LEGACYX") == "labelled", "control label failed")
        expect(w.main.rows[MODEL[0]["ticker"]]["classified_by"] == "model", "model label changed")
        return ("scan_all paginated %d rows; plan_unlabelled excluded all %d model rows (classified_by present) and "
                "kept only the unlabelled control; label_row_if_unlabelled on a model row raises RowAlreadyLabelled "
                "(additive-only, designed) and leaves classified_by=model" % (len(items), len(MODEL)))


def ex_set_kind():
    with World() as w, isolated([YANG]):
        mod = load("infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py", "ex_set_kind")
        items = mod.scan_all(w.main)
        absent = mod.plan_absent_kind(items)
        expect(all(r["ticker"] in absent for r in MODEL), "a model row was not offered to the kind-only plan")
        t = MODEL[0]["ticker"]
        before = copy.deepcopy(w.main.rows[t])
        expect(mod.set_kind_if_absent(w.main, t, "fund", {"fund", "single_security"}) == "set", "kind not set")
        after = w.main.rows[t]
        expect({k: v for k, v in after.items() if k != "instrument_kind"} == before, "kind-only update touched another attribute")
        try:
            mod.set_kind_if_absent(w.main, t, "fund", {"fund", "single_security"})
            fails_contract("second kind write overwrote")
        except mod.KindAlreadySet:
            pass
        return ("scan_all+plan_absent_kind offered all %d model rows (no instrument_kind yet); set_kind_if_absent set "
                "instrument_kind on one and touched no other attribute (classified_by/confidence/low_confidence "
                "unchanged); a repeat raises KindAlreadySet (designed)" % len(MODEL))


def ex_seed_classifications():
    with World() as w, isolated([YANG, SHARED]):
        mod = load("infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py", "ex_seed_classifications")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            existing = mod.read_existing(w.main)
        expect(all(r["ticker"] in existing for r in MODEL), "read_existing missed a model row")
        import etf_classification as seedsrc
        overlap = sorted(set(seedsrc.ETF_CLASSIFICATIONS) & set(MODEL_BY))
        # The contract's correction path: add a model ticker to the seed source and re-seed.
        t = sorted(seedsrc.ETF_CLASSIFICATIONS)[0]
        seed_vals = mod.module_values(t)
        mrow = {"ticker": t, "name": seed_vals["name"] or t, "asset_class": seed_vals["asset_class"],
                "classified_by": "model", "classification_confidence": Decimal("0.62"), "low_confidence": True}
        if seed_vals["sub_asset_class"]:
            mrow["sub_asset_class"] = seed_vals["sub_asset_class"]
        item, preserved, conflicts = mod.merge_item(t, mrow, "2026-09-30T00:00:00Z")
        carried = sorted(k for k in ("classification_confidence", "low_confidence") if k in item)
        if item.get("classified_by") == "seed" and carried:
            contract = json.loads(CONTRACT_MDPF.read_text(encoding="utf-8"))["fields"]
            promise = "a later seed correction of a model row replaces classified_by = seed and drops low_confidence entirely"
            expect(promise in contract["low_confidence"]["rule24_record"]["state_coherence"], "contract sentence moved")
            raise Verdict("FAILS-CONTRACT",
                          "no crash and no refusal (read_existing paged %d rows; the %d model tickers overlap the seed "
                          "source by %d, so today's population is unaffected), BUT the seed CORRECTION path carries model "
                          "attributes onto a seed row: merge_item(%s, <model row>) returns classified_by='seed' WITH %s "
                          "(the 'carry forward any attribute a curator added' loop, seed-etf-classifications.py:113-117, "
                          "keeps every attribute the module does not derive and PROVENANCE_FIELDS omits both). "
                          "MDPF_SECCLASS_CONTRACT 0.3.0 low_confidence.state_coherence says: '%s'; both fields' `absent` "
                          "rule: present ONLY on a model row."
                          % (len(existing), len(MODEL_BY), len(overlap), t, carried, promise))
        return "merge_item dropped the model attributes on a seed correction"


def ex_seed_constituents():
    with World() as w, isolated([YANG]):
        mod = load("infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py", "ex_seed_constituents")
        t = MODEL[0]["ticker"]
        consts = {t: {"name": "X", "asset_class": "Equity", "sub_asset_class": "US"},
                  "ZZNEWX": {"name": "New X", "asset_class": "Equity", "sub_asset_class": "US"}}
        mod.load_constituents = lambda: consts
        outs = []
        for argv in (["x", "--dry-run"], ["x", "--dry-run", "--kind-only"]):
            buf = io.StringIO()
            sys.argv = argv
            with contextlib.redirect_stdout(buf):
                rc = mod.main()
            expect(rc == 0, "main %s returned %s" % (argv[1:], rc))
            outs.append(buf.getvalue())
        expect("EXISTING rows in %s: %d" % (TABLE, len(w.main.rows)) in outs[0], "existing scan denominator missing")
        expect(("KEEP   %-12s" % t) in outs[0], "model ticker not preserved (KEEP) in the plan")
        row = mod.build_row(t, "X", "Equity", "US", "2026-09-30T00:00:00Z")
        try:
            mod.put_row_if_unclassified(w.main, row)
            fails_contract("constituents put overwrote a model row")
        except mod.RowProtected:
            pass
        expect(w.main.rows[t]["classified_by"] == "model", "model row changed")
        return ("paginated scan of %d rows read; --dry-run plan KEEPs the model ticker (preserve-existing) and plans "
                "CREATE for the new one; --kind-only dry-run ok; put_row_if_unclassified on a model row raises "
                "RowProtected (attribute_not_exists(classified_by), designed) and leaves the row" % len(w.main.rows))


def ex_seed_canonical():
    with World() as w, isolated([ROOT / "data/black_diamond/scripts/classification"]):
        mod = load("data/black_diamond/scripts/classification/seed_canonical_securities.py", "ex_seed_canonical")
        differing = conflicts_n = 0
        for r in MODEL[:80]:
            sec = {"ticker": r["ticker"], "name": r["name"] + " CANON", "asset_class": "equity",
                   "sub_asset_class": "US Large Cap"}
            c = mod._yang_conflicts(w.main, sec)
            conflicts_n += len(c)
            differing += 1
        absent = mod._yang_conflicts(w.main, {"ticker": "NOSUCH", "name": "n", "asset_class": "equity", "sub_asset_class": "x"})
        expect(absent == [], "first mint reported a conflict")
        return ("_yang_conflicts over %d model rows read the row via get_item and returned %d field conflict(s) "
                "(table wins, PRESERVED; designed guard), no crash; an absent ticker is still a clean first mint"
                % (differing, conflicts_n))


def ex_seed_bd():
    with World() as w, isolated([ROOT / "data/black_diamond/scripts/classification"]):
        w.tables["bd-securities"] = FakeTable([], "bd-securities")
        mod = load("data/black_diamond/scripts/classification/seed_bd_securities.py", "ex_seed_bd")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            mod.seed(dry_run=False)
        bd = w.tables["bd-securities"].rows
        for r in MODEL:
            expect(r["ticker"] in bd, "%s not copied" % r["ticker"])
        t = MODEL[0]["ticker"]
        copied = bd[t]
        return ("one-time seed scanned %d rows and copied all %d model rows into bd-securities without error. NOTE "
                "(recorded, not graded): the copy overwrites classified_by ('model' -> %r), stamps confidence=%s and "
                "needs_review=%s, and passes classification_confidence/low_confidence through, so model provenance "
                "does not survive into the retiring per-firm table; the script is a documented one-time seed, not "
                "scheduled." % (len(w.main.rows), len(MODEL), copied.get("classified_by"), copied.get("confidence"),
                                copied.get("needs_review")))


def ex_classify_residual():
    with World() as w, isolated([YANG, SHARED]):
        mod = load("infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py", "ex_classify_residual")
        import etf_classifications_dynamodb as cm
        clf = cm.ETFClassifier()
        n = mod.table_rows_at_build(clf)
        expect(n == len(w.main.rows), "table_rows_at_build %d != %d" % (n, len(w.main.rows)))
        live = mod.existing_tickers(clf, region="us-east-1")
        expect(all(r["ticker"] in live for r in MODEL), "existing_tickers missed a model row")
        return ("table_rows_at_build counted %d (Select=COUNT, paginated) and existing_tickers returned all %d model "
                "tickers: the runner's own census sees a model row as a live row, so it is never re-planned" % (n, len(MODEL)))


def ex_scoped_amgt():
    rel = "lib/research/api/scoped_amgt.py"
    with World() as w, isolated([ROOT]):
        mod = load(rel, "ex_scoped_amgt")
        mod._dynamodb = lambda: FakeResource(w.tables)
        rows_in = [{"ticker": r["ticker"] + " US", "x": 1} for r in MODEL]
        joined = mod._join_classification(rows_in)
        for src, got in zip(MODEL, joined):
            expect(got["name_state"] == "SERVED" and got["classification"]["asset_class"] == src["asset_class"],
                   "%s: %r" % (src["ticker"], got))
        jdump(joined)
        return ("_join_classification over %d model tickers (GetItem by bare ticker) -> name SERVED, classification "
                "{asset_class, sub_asset_class, sector} from the row, json.dumps strictly (only three named fields "
                "leave the reader)" % len(joined))


def ex_positioning_chain():
    rel = "lib/research/identity/positioning_chain.py"
    with World() as w, isolated([ROOT]):
        mod = load(rel, "ex_positioning_chain")
        cmap, denom = mod.read_etf_classifications()
        expect(denom["rows"] == len(w.main.rows) and all(r["ticker"].upper() in cmap for r in MODEL),
               "read_etf_classifications denominator %r" % (denom,))
        for r in MODEL:
            ident = mod.resolve_one(r["ticker"], None, "US", None, cmap[r["ticker"].upper()], None)
            jdump(ident)
            expect(ident["classifier_asset_class"] == r["asset_class"], "%s: classifier_asset_class" % r["ticker"])
        return ("read_etf_classifications (client scan + TypeDeserializer, paginated) returned %d rows incl. all %d "
                "model rows; resolve_one carried classifier_asset_class/sub/name, json.dumps strictly"
                % (denom["rows"], len(MODEL)))


def ex_comparison_catalogue():
    base = ROOT / "infra/aws/lambda/investor-reporting/ycharts/generate"
    with World(), isolated([base]):
        mod = load("infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py", "ex_comparison_catalogue")
        port = lambda: {r["ticker"]: dict(r) for r in MODEL}  # noqa: E731 -- the injected read_classifications port
        cat = mod.build_catalogue(tenant="t1", read_classifications=port)
        names = {e["ticker"]: e for e in cat["entries"] if e.get("ticker")}
        expect(all(r["ticker"] in names for r in MODEL), "a model ticker missing from the catalogue")
        import jsonschema
        schema = json.loads((ROOT / "infra/aws/lambda/investor-reporting/_contracts/ComparisonCatalogue.schema.json").read_text(encoding="utf-8"))
        errs = list(jsonschema.Draft202012Validator(schema).iter_errors(cat))
        expect(not errs, "catalogue fails its closed schema: %s" % [e.message for e in errs[:3]])
        extra = sorted({k for e in cat["entries"] for k in e} - {"key", "label", "ticker", "name_source"})
        expect(not extra, "model attributes leaked into catalogue entries: %s" % extra)
        return ("build_catalogue with the injected port returning %d model rows -> %d entries, all model tickers named "
                "(name_source etf_classifications), validates against ComparisonCatalogue.schema.json (closed), entry "
                "keys limited to key/label/ticker/name_source. The port is UNWIRED in the deployed function "
                "(entry.py:165 passes read_classifications through; ENTRY installs none), so no row reaches it today"
                % (len(MODEL), len(cat["entries"])))


# ---------------------------------------------------------------------------------------------
# READ-ONLY readers: the deciding line is recorded and re-verified where the file is present.
# ---------------------------------------------------------------------------------------------
PORTAL_PIN = None


def portal_pin():
    try:
        return subprocess.run(["git", "ls-tree", "HEAD", "portal"], cwd=str(ROOT), capture_output=True, text=True,
                              timeout=30).stdout.split()[2]
    except Exception:  # noqa: BLE001
        return None


def read_only_portal_composition():
    decide = "export const CANONICAL_CLASSES = ['equity', 'fixed_income', 'alternatives', 'structured', 'commodities'] as const"
    path = ROOT / "portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts"
    classes = {"equity", "fixed_income", "alternatives", "structured", "commodities"}
    miss = sorted(set(CLASSES) - classes)
    if miss:
        fails_contract("model asset_class values outside the portal's CANONICAL_CLASSES: %s" % miss)
    if path.exists():
        expect(decide in path.read_text(encoding="utf-8"), "deciding line not present in %s" % path)
        verified = "re-verified in the checked-out portal"
    else:
        verified = ("portal submodule not checked out here; deciding line read at the gitlink pin %s via git show "
                    "<pin>:src/pages/AdvisorIntelligence/_shared/lib/composition.ts:38 (build-time read, not re-run)" % portal_pin())
    return ("READ-ONLY (TypeScript). Deciding line composition.ts:38: `%s`; normalizeMixTo4Class keeps an item only "
            "when `classes.includes(item.asset_class)`. All %d model asset classes %s are members. The portal never "
            "reads classified_by/classification_confidence/low_confidence from the table (it reads served artifacts); "
            "a git grep of those tokens in portal/src at the pin returns only an unrelated sentiment enum. %s."
            % (decide, len(CLASSES), CLASSES, verified))


def read_only_portal_wire():
    decide = ("readonly asset_class?: 'equity' | 'fixed_income' | 'alternatives' | 'structured' | 'commodities' | 'cash' "
              "| 'other' | 'unclassified'")
    path = ROOT / "portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts"
    if path.exists():
        expect(decide in path.read_text(encoding="utf-8"), "deciding line not present in %s" % path)
        verified = "re-verified in the checked-out portal"
    else:
        verified = "read at the gitlink pin %s via git show <pin>:src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts:104 (build-time read)" % portal_pin()
    return ("READ-ONLY (TypeScript). Deciding line HoldingsSnapshot.ts:104 `%s`: the model's five classes are members and "
            "the wire type carries no classified_by/confidence member, matching the Python contract. %s." % (decide, verified))


def read_only_dashbd_classes():
    path = ROOT / "org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md"
    text = path.read_text(encoding="utf-8")
    line = next(row for row in text.split("\n") if row.startswith("| C-CLASSES"))
    expect("fixed_income, equity, commodities, structured, alternatives" in line, "C-CLASSES vocabulary line changed")
    n_code = 0
    for p in (ROOT / "org/missions/D9/IRPT/IRPT_DASHBD").rglob("*.py"):
        n_code += 1 if re.search(r"etf-classifications|etf_classifications|asset_class", p.read_text(encoding="utf-8", errors="ignore")) else 0
    return ("READ-ONLY (no consumer code exists in the tree). Deciding line IRPT_DASHBD_PRD.md C-CLASSES row: 'Each "
            "holding maps through `etf-classifications` (DynamoDB, key `ticker`): fixed_income, equity, commodities, "
            "structured, alternatives; the portal adds cash, unclassified, other. No row means UNCLASSIFIED' -- the "
            "model's %d classes %s are all inside that vocabulary; it names no classified_by or confidence field. "
            "Code under org/missions/D9/IRPT/IRPT_DASHBD naming the table or asset_class: %d of the .py files there "
            "(class_return_daily has no code hit anywhere in the tracked tree)." % (len(CLASSES), CLASSES, n_code))


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

READERS = [
    (CLIENT, "ETFClassifier.get_*/find_by_* (the one client)", lambda: ex_client_read(CLIENT)),
    (CLIENT_POS, "ETFClassifier.get_*/find_by_* (Lambda copy, yang-generate-positioning)", lambda: ex_client_read(CLIENT_POS)),
    (CLIENT_ATT, "ETFClassifier.get_*/find_by_* (Lambda copy, yang-generate-holdings-attribution)", lambda: ex_client_read(CLIENT_ATT)),
    (CLIENT, "ETFClassifier.classify_holdings (static, no call site)", lambda: ex_client_classify_holdings(CLIENT)),
    (CLIENT_POS, "ETFClassifier.classify_holdings (static, no call site; Lambda copy)", lambda: ex_client_classify_holdings(CLIENT_POS)),
    (CLIENT_ATT, "ETFClassifier.classify_holdings (static, no call site; Lambda copy)", lambda: ex_client_classify_holdings(CLIENT_ATT)),
    (POS_DIR + "/lambda_function.py", "resolve_display_name/classify_etf/calculate_allocations/calculate_segment_breakdown", lambda: ex_positioning_lambda(POS_DIR)),
    (ATT_DIR + "/lambda_function.py", "resolve_display_name/extract_holdings_for_portfolio", lambda: ex_attribution_lambda(ATT_DIR)),
    ("data/etfs/scripts/gold/etf_positioning_publisher.py", "_display_name", ex_publisher),
    ("data/assets/scripts/gold/build_satellites_registry.py", "load_classifier/classify", ex_satellites_registry),
    ("data/assets/scripts/gold/build_satellites_characteristics.py", "load_identity", ex_satellites_characteristics),
    ("data/black_diamond/scripts/gold/lib/etf_classifier.py", "ETFClassifier.classify/get_sub_asset_class (BD library)", ex_bd_classifier),
    ("data/black_diamond/scripts/silver/build_bd_assets_dim.py", "apply_blend (BD assets dim)", ex_bd_assets_dim),
    ("data/black_diamond/scripts/gold/D_04.client_portal_summary.py", "_classify_with_canonical", ex_bd_d04),
    ("data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py", "BD library consumer (classify/get_sub_asset_class)",
     lambda: read_only_delegate("data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py",
                                "Consumes only the two strings the BD library returns (exercised above).",
                                ["canonical_class = classifier.classify(ticker, name)",
                                 "canonical_subs.append(classifier.get_sub_asset_class(ticker, name))"])),
    ("data/black_diamond/scripts/gold/D_03.composition_artifacts.py", "BD library consumer (classify/get_sub_asset_class)",
     lambda: read_only_delegate("data/black_diamond/scripts/gold/D_03.composition_artifacts.py",
                                "Consumes only the two strings the BD library returns (exercised above).",
                                ["canonical_class = classifier.classify(ticker, asset_name)",
                                 "canonical_sub = classifier.get_sub_asset_class(ticker, asset_name)"])),
    ("data/assets/scripts/gold/investor_reporting/holdings_snapshot.py", "annotate_classification/classify_security -> HoldingsSnapshot contract", ex_holdings_snapshot),
    ("infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py", "TableVocabulary.from_live_table/existing_tickers/plan_rows", ex_scheduled),
    ("data/black_diamond/scripts/gold/E_18.detect_new_securities.py", "E_18 scheduled caller (BD)",
     lambda: read_only_delegate("data/black_diamond/scripts/gold/E_18.detect_new_securities.py",
                                "Calls only TableVocabulary.from_live_table, existing_tickers and plan_rows, exercised in etf_classification_scheduled.py in this order.",
                                ["vocab = TableVocabulary.from_live_table(classifier)", "existing = existing_tickers(classifier)"])),
    ("data/cot/scripts/gold/E_18.detect_new_securities.py", "E_18 scheduled caller (COT)",
     lambda: read_only_delegate("data/cot/scripts/gold/E_18.detect_new_securities.py",
                                "Calls only TableVocabulary.from_live_table, existing_tickers and plan_rows, exercised in etf_classification_scheduled.py in this order.",
                                ["vocab = TableVocabulary.from_live_table(classifier)", "existing = existing_tickers(classifier)"])),
    ("infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py", "scan_all/plan_unlabelled/label_row_if_unlabelled", ex_label_legacy),
    ("infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py", "scan_all/plan_absent_kind/set_kind_if_absent", ex_set_kind),
    ("infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py", "read_existing/merge_item (seed correction of a model row)", ex_seed_classifications),
    ("infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py", "main (--dry-run, --kind-only)/put_row_if_unclassified", ex_seed_constituents),
    ("data/black_diamond/scripts/classification/seed_canonical_securities.py", "_yang_conflicts", ex_seed_canonical),
    ("data/black_diamond/scripts/classification/seed_bd_securities.py", "seed (one-time copy into bd-securities)", ex_seed_bd),
    ("infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py", "table_rows_at_build/existing_tickers", ex_classify_residual),
    ("lib/research/api/scoped_amgt.py", "_join_classification/_classification_for_ticker", ex_scoped_amgt),
    ("lib/research/identity/positioning_chain.py", "read_etf_classifications/resolve_one", ex_positioning_chain),
    ("infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py", "build_catalogue (injected port, unwired)", ex_comparison_catalogue),
    ("infra/aws/lambda/investor-reporting/ycharts/generate/entry.py", "read_comparison_catalogue (delegates to build_catalogue)",
     lambda: read_only_delegate("infra/aws/lambda/investor-reporting/ycharts/generate/entry.py",
                                "Delegates to comparison_catalogue.build_catalogue (exercised above); no classifications port is installed on ENTRY.",
                                ["return _catalogue.build_catalogue(tenant=ctx.tenant, read_classifications=read_classifications)"])),
    ("portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts", "CANONICAL_CLASSES / normalizeMixTo4Class (portal asset-class mapping)", read_only_portal_composition),
    ("portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts", "asset_class wire type", read_only_portal_wire),
    ("org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md", "IRPT_DASHBD C-CLASSES consumer (PRD only, no code yet)", read_only_dashbd_classes),
]

# Code files that name the table and are NOT readers of it, each with the reason (verified by reading).
NOT_READERS = {
    "infra/aws/lambda/v2_portal/_shared/etf_classification.py": "the static seed SOURCE module (dicts), not a table reader; the seeders above read it",
    "data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py": "reads the LEGACY per-firm table (LEGACY_TABLE = _legacy_table_name()), not etf-classifications",
    "data/black_diamond/scripts/classification/classify_bd_securities.py": "WRITES classified_by to bd-securities (gpt-4o-mini); not a reader of the table",
    "data/black_diamond/scripts/gold/B_01b.classify_new_securities.py": "WRITES classified_by to bd-securities; not a reader of the table",
    "data/cot/scripts/gold/B_01b.classify_new_securities.py": "WRITES classified_by to the cot securities table; not a reader of the table",
    "data/inf/scripts/classification/classify_assets.py": "reads/writes the INF assets table (BD_SECURITIES_TABLE = 'bd-securities'), not etf-classifications",
    "data/black_diamond/scripts/gold/tests/thread_trace.py": "a LOCAL trace harness that drives apply_blend/BD library (both exercised above), not itself a reader",
    ".tools/safe_deploy_core.py": "deploy tool: names the client file in a package member list",
    "infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py": "docstring mention only; its derivation is build_satellites_registry (exercised above)",
    "infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/build_package.py": "packaging member list",
    "infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/build_package.py": "packaging member list",
    "infra/aws/lambda/etfs-pipeline/etf-positioning-producer/build_package.py": "packaging member list",
}
# Files covered by a sibling entry above (same module counted once by path).
COVERED_PATHS = {p for p, _f, _fn in READERS} | set(NOT_READERS)
STRUCTURAL = (".tf", ".sh", ".json")
SEARCH_PATTERNS = ["etf-classifications", "classified_by", "etf_classifications_dynamodb"]
CODE_EXT = (".py", ".ts", ".tsx", ".js", ".mjs", ".cjs")


def tracked_files():
    out = subprocess.run(["git", "ls-files"], cwd=str(ROOT), capture_output=True, text=True, timeout=120).stdout
    return [f for f in out.split("\n") if f]


def search_census(files):
    search, universe = [], {}
    texts = {}
    for f in files:
        if f.endswith(STRUCTURAL + CODE_EXT + (".md", ".yaml", ".yml", ".txt")):
            try:
                texts[f] = (ROOT / f).read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
    for pat in SEARCH_PATTERNS:
        hits = files_n = 0
        for f, t in texts.items():
            c = t.count(pat)
            if c:
                hits += c
                files_n += 1
                if f.endswith(CODE_EXT) and not f.startswith(("org/", "docs/", "archive/", ".scratch")):
                    universe.setdefault(f, []).append(pat)
        search.append({"pattern": pat, "hits": hits, "files": files_n})
    return search, universe


def is_test_path(f):
    b = f.rsplit("/", 1)[-1]
    return "/tests/" in f or b.startswith("test_") or b.endswith("_test.py")


def uncensused(universe):
    bad = []
    for f in sorted(universe):
        if f in COVERED_PATHS or is_test_path(f):
            continue
        bad.append(f)
    return bad


def run_one(fn):
    box = {}

    def target():
        try:
            box["evidence"] = fn()
            box["verdict"] = "TOLERATES"
        except Verdict as v:
            box["verdict"], box["evidence"] = v.verdict, v.evidence
        except Exception as exc:  # noqa: BLE001 -- a crash IS the verdict
            tb = traceback.extract_tb(exc.__traceback__)
            where = "%s:%s" % (Path(tb[-1].filename).name, tb[-1].lineno) if tb else "?"
            box["verdict"], box["evidence"] = "CRASHES", "%s: %s at %s" % (type(exc).__name__, exc, where)

    th = threading.Thread(target=target, daemon=True)
    th.start()
    th.join(EXERCISE_TIMEOUT_S)
    if th.is_alive():
        return "CRASHES", "no result in %ds (hung exercise, abandoned)" % EXERCISE_TIMEOUT_S
    return box["verdict"], box["evidence"]


def main() -> int:
    files = tracked_files()
    search, universe = search_census(files)
    readers = []
    for path, func, fn in READERS:
        verdict, evidence = run_one(fn)
        if evidence.startswith("READ-ONLY") and verdict == "TOLERATES":
            verdict = "READ-ONLY"
        readers.append({"path": path, "function": func, "verdict": verdict, "evidence": evidence})
    missing = uncensused(universe)
    r2 = json.loads(R2_CENSUS.read_text(encoding="utf-8"))
    counts = {k: sum(1 for r in readers if r["verdict"] == k) for k in
              ("TOLERATES", "READ-ONLY", "CRASHES", "REFUSES", "FAILS-CONTRACT")}
    doc = {
        "what": "SC-e-15 model-row reader census: every reader of etf-classifications exercised on classified_by=model rows",
        "model_rows": {"source": str(R4_CENSUS.relative_to(ROOT)).replace("\\", "/"), "count": len(MODEL),
                       "by_asset_class": {c: sum(1 for r in MODEL if r["asset_class"] == c) for c in CLASSES},
                       "low_confidence_true": sum(1 for r in MODEL if r["low_confidence"]),
                       "keyed_tickers": sum(1 for r in MODEL if not r["ticker"].startswith("MDLX")),
                       "confidence_type": "Decimal (what boto3 returns for a DynamoDB number)"},
        "readers": readers,
        "denominator": {"readers_exercised_or_read": len(readers),
                        "round3_reader_census_entries": r2.get("reader_denominator"),
                        "code_files_naming_the_table_outside_org_docs_archive": len(universe),
                        "of_which_tests": sum(1 for f in universe if is_test_path(f)),
                        "of_which_declared_not_readers": sum(1 for f in universe if f in NOT_READERS),
                        "uncensused": missing},
        "search": search,
        "not_readers": NOT_READERS,
    }
    OUT.write_text(json.dumps(doc, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    for r in readers:
        print("READER %-15s %s :: %s" % (r["verdict"], r["path"], r["function"]))
    for f in missing:
        print("UNCENSUSED %s" % f)
    print("MODEL-READER-CENSUS readers=%d tolerates=%d read_only=%d crashes=%d refuses=%d fails_contract=%d"
          % (len(readers), counts["TOLERATES"], counts["READ-ONLY"], counts["CRASHES"], counts["REFUSES"],
             counts["FAILS-CONTRACT"]))
    if not (counts["CRASHES"] or counts["REFUSES"] or counts["FAILS-CONTRACT"] or missing):
        print("MODEL-READER-TOLERATED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
