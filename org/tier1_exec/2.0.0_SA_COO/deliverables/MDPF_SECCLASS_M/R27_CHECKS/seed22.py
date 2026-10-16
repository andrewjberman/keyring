#!/usr/bin/env python
"""R27 SC-e-107: the 22-row canonical seed from the old list (bd-securities -> etf-classifications).

Subcommands (run from anywhere; paths resolve from this file):
  plan --out <file> [--fold-map <file>]
                               READ-ONLY. Plans the 22 baseline tickers through the shared module's
                               plan_rows (legacy-fork input, direct canonical vocabulary match only)
                               and writes the plan file. With --fold-map (CTO fold ruling, amendment 1),
                               the tickers plan_rows cannot plan are seeded from the map's `seed` (ruled
                               class, provenance, fold_* audit) or held out to seed_pending from the map's
                               `held_out` (never planned). Reads: one lots partition, the live
                               etf-classifications table (scan), the bd-securities table (get_item).
  apply --plan <file> --pair <path>
                               WRITES planned rows to etf-classifications. A CloudOps seat runs this
                               only under a signed pair. Refuses (exit 2, nothing written) when --pair
                               is not an existing file, when the plan firm is not 49financial, when a
                               planned row lacks provenance, or when any planned ticker already has a
                               canonical row. Writes by a conditional put (attribute_not_exists(ticker))
                               that carries the two provenance attributes and the fold_* audit attributes;
                               the shared write() drops them. Never writes a seed_pending entry.
  selftest                     NO AWS call. Stub tables only. Prints SEED22-SELFTEST ok=<bool>.

Shared module (imported, never copied): infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py
"""
import argparse
import io
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[6]
SHARED = REPO / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"
if not (SHARED / "etf_classification_scheduled.py").is_file():
    raise SystemExit("BLOCKED: shared module not found at %s" % SHARED)
sys.path.insert(0, str(SHARED))

import boto3  # noqa: E402
import pyarrow.parquet as pq  # noqa: E402
from botocore.exceptions import ClientError  # noqa: E402

from etf_classification_scheduled import (  # noqa: E402
    CLASSIFIED_BY, LEGACY_FORK_INPUT_LABEL, TableVocabulary, _WRITE_FIELDS, default_bd_securities_lookup,
    existing_tickers, plan_rows, ETFClassifier,
)

FIRM = "49financial"
REGION = "us-east-1"
TABLE_NAME = "etf-classifications"        # canonical table (the shared module's own constant)
OLD_TABLE = "bd-securities"               # the old list; the source table of every seeded row
LOTS_BUCKET = "opal-data-bd"
LOTS_KEY = "gold/holdings_lots/2026-10-09.parquet"
BASELINE = HERE / "seed22_candidates_20261016.json"
UPDATED_BY = "mdpf-secclass-seed22"
PROVENANCE_TABLE = OLD_TABLE
COND = "attribute_not_exists(ticker)"
# Amendment 1: a row seeded from the CTO fold map carries this input tag and these audit attributes.
FOLD_MAP_INPUT_LABEL = "fold-map"
FOLD_AUDIT_FIELDS = ("fold_rule", "fold_note", "source_asset_class", "source_sub_asset_class")


def _now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_baseline():
    base = json.load(open(BASELINE, encoding="utf-8"))
    mv = {c["ticker"]: float(c["market_value"]) for c in base["candidates"]}
    return mv, float(base["total_market_value"])


def _lots_names(tickers):
    """One asset_name per ticker: the name with the largest open market value (fallback: all rows)."""
    s3 = boto3.client("s3", region_name=REGION)
    body = s3.get_object(Bucket=LOTS_BUCKET, Key=LOTS_KEY)["Body"].read()
    df = pq.read_table(io.BytesIO(body), columns=["ticker", "asset_name", "market_value", "is_open"]).to_pandas()
    df["_t"] = df["ticker"].astype(str).str.strip().str.upper()
    names, notes = {}, {}
    for t in tickers:
        rows = df[(df["_t"] == t) & df["asset_name"].notna()]
        op = rows[rows["is_open"] == True]  # noqa: E712
        src = op if len(op) else rows
        if not len(src):
            names[t] = t
            notes[t] = "no lots row with an asset_name; ticker used as name"
            continue
        g = src.groupby("asset_name")["market_value"].sum()
        best = sorted(g.items(), key=lambda kv: (-kv[1], str(kv[0])))[0][0]
        names[t] = str(best)
    return names, notes


def _unresolved_reason(old, vocab):
    if not old:
        return "no bd-securities row to read provenance from"
    ac, sac = old.get("asset_class"), old.get("sub_asset_class")
    if sac == "needs_review":
        return ("old-list sub_asset_class 'needs_review' is not a canonical sub-class; "
                "no source resolved it directly; left unresolved, not folded")
    if ac not in vocab.asset_classes:
        return "old-list asset_class '%s' is not a canonical asset_class; not folded" % ac
    if sac not in vocab.sub_asset_classes.get(ac, set()):
        return ("old-list (asset_class, sub_asset_class) = (%s, %s) is not a direct canonical vocabulary "
                "member; no other source resolved it; not folded" % (ac, sac))
    return "no source resolved the ticker directly"


def _fold_row(t, name, old, spec, vocab):
    """Amendment 1: a row seeded from the CTO fold map -- the ruled class, the provenance and the fold_* audit.
    Returns (row, None), or (None, reason) when the ruled class is not canonical or the old row cannot be carried."""
    ac, sac = spec["asset_class"], spec.get("sub_asset_class")
    if ac not in vocab.asset_classes or (sac and sac not in vocab.sub_asset_classes.get(ac, set())):
        return None, "fold-map class (%s, %s) is not a canonical vocabulary member; not seeded" % (ac, sac)
    if not old or not old.get("last_updated"):
        return None, "no bd-securities last_updated to carry as provenance"
    row = {"ticker": t, "asset_class": ac, "classified_by": CLASSIFIED_BY, "updated_by": UPDATED_BY,
           "name": name or t, "input": FOLD_MAP_INPUT_LABEL}
    if sac:
        row["sub_asset_class"] = sac  # a null sub-class is OMITTED (canonical rows without one carry no attribute)
    row["source_table"] = PROVENANCE_TABLE
    row["source_last_updated"] = old["last_updated"]  # copied verbatim from the old-list row
    row["source_asset_class"] = old.get("asset_class")
    if old.get("sub_asset_class") is not None:
        row["source_sub_asset_class"] = old["sub_asset_class"]
    row["fold_rule"] = spec["rule"]
    row["fold_note"] = spec["note"]  # verbatim, including any OVERRIDE text
    return row, None


def build_plan(candidates, mv, names, *, vocab, existing, old_item, bd_lookup, read_at, notes=None, fold_map=None):
    """Pure planner (no AWS): every candidate ends in exactly one of planned / unresolved / seed_pending.
    fold_map (amendment 1): {"seed": {ticker: {rule, asset_class, sub_asset_class, note}}, "held_out": {ticker: {rule, reason}}}.
    A held_out ticker is seed_pending and never planned; a seed ticker that plan_rows cannot plan is planned with the
    ruled class; a ticker in neither stays unresolved (the check refuses it)."""
    fold_seed = (fold_map or {}).get("seed", {})
    fold_held = (fold_map or {}).get("held_out", {})
    stray = sorted((set(fold_seed) | set(fold_held)) - set(candidates))
    if stray:
        raise SystemExit("SEED22-PLAN REFUSED fold map names tickers outside the candidate set: %s" % stray)
    both = sorted(set(fold_seed) & set(fold_held))
    if both:
        raise SystemExit("SEED22-PLAN REFUSED fold map lists tickers as both seed and held_out: %s" % both)
    planned, unresolved, seed_pending = [], [], []
    mv_by_class = {}
    for t in candidates:
        m = mv[t]
        if t in existing:
            unresolved.append({"ticker": t, "market_value": m,
                               "reason": "REFUSED: an etf-classifications row already exists for this ticker"})
            continue
        if t in fold_held:
            seed_pending.append({"ticker": t, "market_value": m, "reason": fold_held[t]["reason"],
                                 "fold_rule": fold_held[t]["rule"]})
            continue
        old = old_item(t)
        rows, un, sp = plan_rows([(t, names[t])], vocab=vocab, existing_tickers=existing,
                                 bd_securities_lookup=bd_lookup, updated_by=UPDATED_BY)
        if sp:
            seed_pending.append({"ticker": t, "market_value": m,
                                 "reason": "carried by the seed source (etf_classification.py); the seed path writes it"})
            continue
        if rows and t in fold_seed:
            unresolved.append({"ticker": t, "market_value": m,
                               "reason": "fold map names a ticker plan_rows plans directly; the map does not override a direct match"})
            continue
        if not rows and t in fold_seed:
            row, why = _fold_row(t, names[t], old, fold_seed[t], vocab)
            if row is None:
                unresolved.append({"ticker": t, "market_value": m, "reason": why})
            else:
                planned.append({"ticker": t, "market_value": m, "row": row})
                mv_by_class[row["asset_class"]] = mv_by_class.get(row["asset_class"], 0.0) + m
            continue
        if not rows:
            unresolved.append({"ticker": t, "market_value": m, "reason": _unresolved_reason(old, vocab)})
            continue
        row = rows[0]
        if row.get("input") != LEGACY_FORK_INPUT_LABEL:
            unresolved.append({"ticker": t, "market_value": m,
                               "reason": "resolved by a non-bd-securities input (%s); not a seed of this cell" % row.get("input")})
            continue
        if not row.get("sub_asset_class"):
            unresolved.append({"ticker": t, "market_value": m,
                               "reason": "no sub_asset_class: a direct canonical sub-class match is required"})
            continue
        if not old or not old.get("last_updated"):
            unresolved.append({"ticker": t, "market_value": m, "reason": "no bd-securities last_updated to carry as provenance"})
            continue
        row["source_table"] = PROVENANCE_TABLE
        row["source_last_updated"] = old["last_updated"]  # copied verbatim from the old row
        planned.append({"ticker": t, "market_value": m, "row": row})
        mv_by_class[row["asset_class"]] = mv_by_class.get(row["asset_class"], 0.0) + m
    return {
        "firm": FIRM,
        "read_at": read_at,
        "candidates": list(candidates),
        "planned": planned,
        "unresolved": unresolved,
        "seed_pending": seed_pending,
        "mv_by_class": {k: round(v, 2) for k, v in sorted(mv_by_class.items())},
    }


def cmd_plan(out_path, fold_path=None):
    mv, total = _load_baseline()
    tickers = sorted(mv)
    fold_map = None
    if fold_path:
        if not os.path.isfile(fold_path):
            print("SEED22-PLAN REFUSED fold map=ABSENT path=%s" % fold_path)
            return 2
        fold_map = json.load(open(fold_path, encoding="utf-8"))
    names, notes = _lots_names(tickers)
    classifier = ETFClassifier()
    vocab = TableVocabulary.from_live_table(classifier)
    existing = existing_tickers(classifier)
    old_table = boto3.resource("dynamodb", region_name=REGION).Table(OLD_TABLE)

    def old_item(t):
        return old_table.get_item(Key={"ticker": t}).get("Item")

    plan = build_plan(tickers, mv, names, vocab=vocab, existing=existing, old_item=old_item,
                      bd_lookup=default_bd_securities_lookup(OLD_TABLE), read_at=_now_utc(), fold_map=fold_map)
    plan["source_partition"] = "s3://%s/%s" % (LOTS_BUCKET, LOTS_KEY)
    plan["total_market_value"] = total
    if fold_map is not None:
        plan["fold_map"] = os.path.basename(fold_path)
    if notes:
        plan["name_notes"] = notes
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(plan, fh, indent=2, sort_keys=False)
        fh.write("\n")
    dollars = sum(e["market_value"] for k in ("planned", "unresolved", "seed_pending") for e in plan[k])
    print("SEED22-PLAN-BUILT planned=%d unresolved=%d seed_pending=%d dollars=%.2f out=%s" % (
        len(plan["planned"]), len(plan["unresolved"]), len(plan["seed_pending"]), dollars, out_path))
    for e in plan["unresolved"]:
        print("  unresolved %s mv=%.2f reason=%s" % (e["ticker"], e["market_value"], e["reason"]))
    for e in plan["seed_pending"]:
        print("  seed_pending %s mv=%.2f" % (e["ticker"], e["market_value"]))
    print("  mv_by_class %s" % json.dumps(plan["mv_by_class"], sort_keys=True))
    return 0


def cmd_apply(plan, pair_path, table=None, now=None):
    """Returns the exit code. 0 written all, 2 refused (nothing written, or a race refusal)."""
    if not pair_path or not os.path.isfile(pair_path):
        print("SEED22-APPLY REFUSED pair=ABSENT path=%s" % pair_path)
        return 2
    if plan.get("firm") != FIRM:
        print("SEED22-APPLY REFUSED firm=%s (expected %s)" % (plan.get("firm"), FIRM))
        return 2
    planned = plan.get("planned", [])
    for e in planned:
        row = e.get("row") or {}
        if row.get("source_table") != PROVENANCE_TABLE or not row.get("source_last_updated"):
            print("SEED22-APPLY REFUSED provenance missing for %s" % e.get("ticker"))
            return 2
    if table is None:
        table = boto3.resource("dynamodb", region_name=REGION).Table(TABLE_NAME)
    present = [e["ticker"] for e in planned if "Item" in table.get_item(Key={"ticker": e["ticker"]})]
    if present:
        print("SEED22-APPLY written=0 refused=%d" % len(present))
        for t in present:
            print("SEED22-APPLY refused %s reason=canonical row already exists" % t)
        return 2
    stamp = now or _now_utc()
    written, refused = 0, []
    for e in planned:
        row = e["row"]
        item = {k: row[k] for k in _WRITE_FIELDS if row.get(k) is not None}
        item["last_updated"] = stamp
        item["source_table"] = row["source_table"]
        item["source_last_updated"] = row["source_last_updated"]
        for k in FOLD_AUDIT_FIELDS:  # amendment 1: fold_rule, fold_note, source_asset_class, source_sub_asset_class
            if row.get(k) is not None:
                item[k] = row[k]
        try:
            table.put_item(Item=item, ConditionExpression=COND)
            written += 1
        except ClientError as err:
            if err.response.get("Error", {}).get("Code") == "ConditionalCheckFailedException":
                refused.append(e["ticker"])
                print("SEED22-APPLY refused %s reason=conditional put failed (row appeared after the pre-check)" % e["ticker"])
            else:
                raise
    print("SEED22-APPLY written=%d refused=%d" % (written, len(refused)))
    return 0 if not refused else 2


class _StubTable:
    def __init__(self, items=None):
        self.items = {k: dict(v) for k, v in (items or {}).items()}
        self.attempts = []

    def get_item(self, Key):
        t = Key["ticker"]
        return {"Item": dict(self.items[t])} if t in self.items else {}

    def put_item(self, Item, ConditionExpression):
        self.attempts.append({"ticker": Item["ticker"], "ConditionExpression": ConditionExpression, "Item": dict(Item)})
        if ConditionExpression != COND:
            raise ValueError("selftest stub: unexpected condition %r" % ConditionExpression)
        if Item["ticker"] in self.items:
            raise ClientError({"Error": {"Code": "ConditionalCheckFailedException", "Message": "stub"}}, "PutItem")
        self.items[Item["ticker"]] = dict(Item)


def cmd_selftest():
    fails = []

    def check(label, cond, detail=""):
        print("  %s %s %s" % ("PASS" if cond else "FAIL", label, detail))
        if not cond:
            fails.append(label)

    vocab = TableVocabulary.from_mapping({"equity": ["US Large Cap"], "fixed_income": ["Investment Grade"]})
    old = {
        "AAAX": {"ticker": "AAAX", "asset_class": "equity", "sub_asset_class": "US Large Cap",
                 "last_updated": "2026-04-08T23:40:19.275200+00:00Z"},
        "BBBX": {"ticker": "BBBX", "asset_class": "fixed_income", "sub_asset_class": "needs_review",
                 "last_updated": "2026-03-20T20:03:54.223843Z"},
        "CCCX": {"ticker": "CCCX", "asset_class": "equity", "sub_asset_class": "US Large Cap",
                 "last_updated": "2026-04-09T19:04:35.648812+00:00Z"},
    }
    canon_stub = {"CCCX": {"ticker": "CCCX", "asset_class": "equity", "sub_asset_class": "US Large Cap"}}
    mv = {"AAAX": 100.0, "BBBX": 50.0, "CCCX": 25.0}
    names = {"AAAX": "FIXTURE A", "BBBX": "FIXTURE B", "CCCX": "FIXTURE C"}

    print("SEED22-SELFTEST (i) plan on the three-ticker fixture")
    plan = build_plan(["AAAX", "BBBX", "CCCX"], mv, names, vocab=vocab, existing={"CCCX"},
                      old_item=lambda t: old.get(t), bd_lookup=lambda t: old.get(t), read_at=_now_utc())
    pl = {e["ticker"]: e for e in plan["planned"]}
    un = {e["ticker"]: e for e in plan["unresolved"]}
    check("planned AAAX", "AAAX" in pl, json.dumps(pl.get("AAAX", {}).get("row"), sort_keys=True))
    check("AAAX carries source_table", pl.get("AAAX", {}).get("row", {}).get("source_table") == "bd-securities")
    check("AAAX carries source_last_updated",
          pl.get("AAAX", {}).get("row", {}).get("source_last_updated") == old["AAAX"]["last_updated"])
    check("AAAX input is legacy-fork", pl.get("AAAX", {}).get("row", {}).get("input") == LEGACY_FORK_INPUT_LABEL)
    check("BBBX (needs_review) unresolved", "BBBX" in un and "BBBX" not in pl, un.get("BBBX", {}).get("reason", ""))
    check("CCCX (canonical stub) refused, not planned", "CCCX" in un and "CCCX" not in pl,
          un.get("CCCX", {}).get("reason", ""))
    check("partition exact", sorted(list(pl) + list(un) + [e["ticker"] for e in plan["seed_pending"]])
          == ["AAAX", "BBBX", "CCCX"])

    pair_ok = str(BASELINE)  # an existing file stands in for the signed pair (read only)
    print("SEED22-SELFTEST (ii) apply writes the planned row with provenance and a conditional put")
    stub = _StubTable(canon_stub)
    rc = cmd_apply(plan, pair_ok, table=stub, now="2026-10-16T00:00:00Z")
    last = stub.attempts[-1] if stub.attempts else {}
    check("apply rc 0", rc == 0, "rc=%d" % rc)
    check("conditional put issued", last.get("ConditionExpression") == COND, last.get("ConditionExpression", ""))
    check("item has source_table", last.get("Item", {}).get("source_table") == "bd-securities")
    check("item has source_last_updated",
          last.get("Item", {}).get("source_last_updated") == old["AAAX"]["last_updated"])
    check("only AAAX attempted", [a["ticker"] for a in stub.attempts] == ["AAAX"],
          str([a["ticker"] for a in stub.attempts]))
    check("input tag not persisted", "input" not in last.get("Item", {}))

    print("SEED22-SELFTEST (iii) difference control: missing pair writes nothing and exits 2")
    stub3 = _StubTable(canon_stub)
    rc3 = cmd_apply(plan, str(HERE / "NO_SUCH_PAIR.json"), table=stub3, now="2026-10-16T00:00:00Z")
    check("missing pair rc 2", rc3 == 2, "rc=%d" % rc3)
    check("missing pair writes nothing", stub3.attempts == [] and set(stub3.items) == {"CCCX"})

    print("SEED22-SELFTEST (iv) planned ticker already canonical: nothing written for it")
    stub4 = _StubTable(dict(canon_stub, AAAX={"ticker": "AAAX", "asset_class": "equity",
                                               "sub_asset_class": "US Large Cap"}))
    before = json.dumps(stub4.items, sort_keys=True)
    rc4 = cmd_apply(plan, pair_ok, table=stub4, now="2026-10-16T00:00:00Z")
    check("existing planned ticker rc 2", rc4 == 2, "rc=%d" % rc4)
    check("existing planned ticker not written", stub4.attempts == [] and json.dumps(stub4.items, sort_keys=True) == before)

    print("SEED22-SELFTEST (v) firm other than 49financial refuses")
    bad = dict(plan, firm="other")
    stub5 = _StubTable(canon_stub)
    rc5 = cmd_apply(bad, pair_ok, table=stub5, now="2026-10-16T00:00:00Z")
    check("firm mismatch rc 2 and nothing written", rc5 == 2 and stub5.attempts == [])

    fx_old = {
        "DDDX": {"ticker": "DDDX", "asset_class": "alternatives", "sub_asset_class": "Volatility",
                 "last_updated": "2026-04-01T00:00:00+00:00Z"},
        "EEEX": {"ticker": "EEEX", "asset_class": "fixed_income", "sub_asset_class": "needs_review",
                 "last_updated": "2026-04-02T00:00:00Z"},
        "FFFX": {"ticker": "FFFX", "asset_class": "fixed_income", "sub_asset_class": "Investment Grade",
                 "last_updated": "2026-04-03T00:00:00Z"},
        "GGGX": {"ticker": "GGGX", "asset_class": "alternatives", "sub_asset_class": "Volatility",
                 "last_updated": "2026-04-04T00:00:00Z"},
    }
    fx_map = {
        "seed": {
            "DDDX": {"rule": "F1", "asset_class": "alternatives", "sub_asset_class": "Real Estate",
                     "note": "fixture: REIT convention"},
            "EEEX": {"rule": "F2", "asset_class": "fixed_income", "sub_asset_class": None,
                     "note": "fixture: old-list class kept, no sub-class"},
            "GGGX": {"rule": "F5", "asset_class": "commodities", "sub_asset_class": "Commodities",
                     "note": "OVERRIDE of the old-list class (alternatives / Volatility): fixture"},
        },
        "held_out": {"FFFX": {"rule": "F2", "reason": "fixture: held out"}},
    }
    fx_vocab = TableVocabulary.from_mapping({"alternatives": ["Real Estate"], "fixed_income": ["Investment Grade"],
                                              "commodities": ["Commodities"], "equity": ["US Large Cap"]})
    fx_mv = {"DDDX": 10.0, "EEEX": 20.0, "FFFX": 30.0, "GGGX": 40.0}
    fx_names = {"DDDX": "FIXTURE D", "EEEX": "FIXTURE E", "FFFX": "FIXTURE F", "GGGX": "FIXTURE G"}
    fx_cands = ["DDDX", "EEEX", "FFFX", "GGGX"]

    print("SEED22-SELFTEST (vi) fold map: seeded tickers take the map's classes, provenance and fold_* audit; held-out never planned or written")
    fplan = build_plan(fx_cands, fx_mv, fx_names, vocab=fx_vocab, existing=set(),
                       old_item=lambda t: fx_old.get(t), bd_lookup=lambda t: fx_old.get(t),
                       read_at=_now_utc(), fold_map=fx_map)
    fpl = {e["ticker"]: e for e in fplan["planned"]}
    fsp = {e["ticker"]: e for e in fplan["seed_pending"]}
    drow = fpl.get("DDDX", {}).get("row", {})
    check("DDDX planned from the map", "DDDX" in fpl, json.dumps(drow, sort_keys=True))
    check("DDDX takes the map's classes", drow.get("asset_class") == "alternatives"
          and drow.get("sub_asset_class") == "Real Estate")
    check("DDDX provenance source_table", drow.get("source_table") == "bd-securities")
    check("DDDX provenance source_last_updated", drow.get("source_last_updated") == fx_old["DDDX"]["last_updated"])
    check("DDDX fold_rule and fold_note", drow.get("fold_rule") == "F1" and drow.get("fold_note") == "fixture: REIT convention")
    check("DDDX input is fold-map", drow.get("input") == FOLD_MAP_INPUT_LABEL)
    check("DDDX source_sub_asset_class audit", drow.get("source_sub_asset_class") == "Volatility"
          and drow.get("source_asset_class") == "alternatives")
    erow = fpl.get("EEEX", {}).get("row", {})
    check("EEEX planned, null sub-class omitted", "EEEX" in fpl and erow.get("asset_class") == "fixed_income"
          and "sub_asset_class" not in erow, json.dumps(erow, sort_keys=True))
    check("FFFX held out to seed_pending, not planned", "FFFX" in fsp and "FFFX" not in fpl
          and fsp["FFFX"].get("reason") == "fixture: held out", json.dumps(fsp.get("FFFX", {}), sort_keys=True))
    check("fixture partition exact", sorted(list(fpl) + list(fsp) + [e["ticker"] for e in fplan["unresolved"]])
          == sorted(fx_cands) and not fplan["unresolved"])
    fstub = _StubTable({})
    frc = cmd_apply(fplan, pair_ok, table=fstub, now="2026-10-16T00:00:00Z")
    attempted = [a["ticker"] for a in fstub.attempts]
    check("fold apply rc 0", frc == 0, "rc=%d attempted=%s" % (frc, attempted))
    check("fold apply never attempts held-out FFFX", "FFFX" not in attempted and "FFFX" not in fstub.items)
    eitem = fstub.items.get("EEEX", {})
    check("fold apply writes no sub_asset_class for EEEX", "sub_asset_class" not in eitem and eitem.get("asset_class") == "fixed_income")
    ditem = fstub.items.get("DDDX", {})
    check("fold apply writes fold_rule, source_asset_class, source_sub_asset_class",
          ditem.get("fold_rule") == "F1" and ditem.get("source_asset_class") == "alternatives"
          and ditem.get("source_sub_asset_class") == "Volatility", json.dumps(ditem, sort_keys=True))

    print("SEED22-SELFTEST (vii) OVERRIDE case: a seeded note starting OVERRIDE is kept verbatim in fold_note")
    grow = fpl.get("GGGX", {}).get("row", {})
    check("GGGX planned with the map's commodities class", grow.get("asset_class") == "commodities"
          and grow.get("sub_asset_class") == "Commodities", json.dumps(grow, sort_keys=True))
    check("GGGX fold_note keeps the OVERRIDE text", str(grow.get("fold_note", "")).startswith("OVERRIDE"),
          str(grow.get("fold_note", "")))
    check("GGGX written with the OVERRIDE note", fstub.items.get("GGGX", {}).get("fold_note") == grow.get("fold_note"))

    ok = not fails
    print("SEED22-SELFTEST ok=%s fails=%s" % (ok, fails))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="R27 SC-e-107 seed22 plan / apply / selftest")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_plan = sub.add_parser("plan", help="READ-ONLY plan file")
    p_plan.add_argument("--out", required=True)
    p_plan.add_argument("--fold-map", default=None, help="CTO fold ruling map (amendment 1), read only")
    p_apply = sub.add_parser("apply", help="WRITE planned rows under a signed pair (CloudOps seat only)")
    p_apply.add_argument("--plan", required=True)
    p_apply.add_argument("--pair", required=True)
    sub.add_parser("selftest", help="stub tables only, no AWS")
    args = ap.parse_args(argv)
    if args.cmd == "plan":
        return cmd_plan(args.out, args.fold_map)
    if args.cmd == "apply":
        plan = json.load(open(args.plan, encoding="utf-8")) if os.path.isfile(args.plan) else None
        if plan is None:
            print("SEED22-APPLY REFUSED plan=ABSENT path=%s" % args.plan)
            return 2
        return cmd_apply(plan, args.pair)
    return cmd_selftest()


if __name__ == "__main__":
    sys.exit(main())
