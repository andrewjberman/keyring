#!/usr/bin/env python
"""R27 SC-e-107: the 22-row canonical seed from the old list (bd-securities -> etf-classifications).

Subcommands (run from anywhere; paths resolve from this file):
  plan --out <file>            READ-ONLY. Plans the 22 baseline tickers through the shared module's
                               plan_rows (legacy-fork input, direct canonical vocabulary match only,
                               no fold) and writes the plan file. Reads: one lots partition, the live
                               etf-classifications table (scan), the bd-securities table (get_item).
  apply --plan <file> --pair <path>
                               WRITES planned rows to etf-classifications. A CloudOps seat runs this
                               only under a signed pair. Refuses (exit 2, nothing written) when --pair
                               is not an existing file, when the plan firm is not 49financial, when a
                               planned row lacks provenance, or when any planned ticker already has a
                               canonical row. Writes by a conditional put (attribute_not_exists(ticker))
                               that carries the two provenance attributes; the shared write() drops them.
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
    LEGACY_FORK_INPUT_LABEL, TableVocabulary, _WRITE_FIELDS, default_bd_securities_lookup,
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


def build_plan(candidates, mv, names, *, vocab, existing, old_item, bd_lookup, read_at, notes=None):
    """Pure planner (no AWS): every candidate ends in exactly one of planned / unresolved / seed_pending."""
    planned, unresolved, seed_pending = [], [], []
    mv_by_class = {}
    for t in candidates:
        m = mv[t]
        if t in existing:
            unresolved.append({"ticker": t, "market_value": m,
                               "reason": "REFUSED: an etf-classifications row already exists for this ticker"})
            continue
        old = old_item(t)
        rows, un, sp = plan_rows([(t, names[t])], vocab=vocab, existing_tickers=existing,
                                 bd_securities_lookup=bd_lookup, updated_by=UPDATED_BY)
        if sp:
            seed_pending.append({"ticker": t, "market_value": m,
                                 "reason": "carried by the seed source (etf_classification.py); the seed path writes it"})
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


def cmd_plan(out_path):
    mv, total = _load_baseline()
    tickers = sorted(mv)
    names, notes = _lots_names(tickers)
    classifier = ETFClassifier()
    vocab = TableVocabulary.from_live_table(classifier)
    existing = existing_tickers(classifier)
    old_table = boto3.resource("dynamodb", region_name=REGION).Table(OLD_TABLE)

    def old_item(t):
        return old_table.get_item(Key={"ticker": t}).get("Item")

    plan = build_plan(tickers, mv, names, vocab=vocab, existing=existing, old_item=old_item,
                      bd_lookup=default_bd_securities_lookup(OLD_TABLE), read_at=_now_utc())
    plan["source_partition"] = "s3://%s/%s" % (LOTS_BUCKET, LOTS_KEY)
    plan["total_market_value"] = total
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

    ok = not fails
    print("SEED22-SELFTEST ok=%s fails=%s" % (ok, fails))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="R27 SC-e-107 seed22 plan / apply / selftest")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_plan = sub.add_parser("plan", help="READ-ONLY plan file")
    p_plan.add_argument("--out", required=True)
    p_apply = sub.add_parser("apply", help="WRITE planned rows under a signed pair (CloudOps seat only)")
    p_apply.add_argument("--plan", required=True)
    p_apply.add_argument("--pair", required=True)
    sub.add_parser("selftest", help="stub tables only, no AWS")
    args = ap.parse_args(argv)
    if args.cmd == "plan":
        return cmd_plan(args.out)
    if args.cmd == "apply":
        plan = json.load(open(args.plan, encoding="utf-8")) if os.path.isfile(args.plan) else None
        if plan is None:
            print("SEED22-APPLY REFUSED plan=ABSENT path=%s" % args.plan)
            return 2
        return cmd_apply(plan, args.pair)
    return cmd_selftest()


if __name__ == "__main__":
    sys.exit(main())
