#!/usr/bin/env python3
"""old_list_reclassify_write.py -- MDPF_SECCLASS round 8, cell SC-e-32 (FWD-17, FWD-15): the writer of the old list's
reclassification set (OLD_LIST_RECLASSIFY_SET_20261007.tsv, built by old_list_reclassify_set.py).

DEFAULT IS A DRY RUN: it reads the set and the live etf-classifications table (consistent paginated scan, keys and classes
only), plans exactly what a write would do, and prints
  RECLASSIFY-DRY-RUN direct=<n> to_ai=<n> unplaced_key=<n> present=<n> puts=0 model_calls=0
(n = the set's rows by route). The table handle and the model transport are wrapped with counters: any put / update /
delete / batch-write is counted AND refused, the transport counts every call and refuses it; the run exits non-zero
(RECLASSIFY-DRY-RUN-BAD) if either counter is not zero. It reads no secret and writes no file.

  --write --half <path> --snapshot <path>   THE ISSUER'S ACT, never a worker's. Refuses unless BOTH halves read SIGNED in
        <half> (headings `## COO half -- SIGNED` and `## CTO half -- SIGNED`), and unless <snapshot> does not exist yet.
        Order: (1) snapshot the table's key set to <snapshot> BEFORE any put; (2) DIRECT rows, held first, through
        etf_classification_scheduled.write() -- a conditional put on an absent key, so a present key is never touched;
        (3) AI rows, held first, through SC-e-31's runner (yang_pipeline/classify-residual-model.py run()) with its model
        enabled, in chunks of --chunk keys (each chunk is classified, bounded, put conditionally, and the AI listing
        rewritten, so a stop loses at most one chunk). A key two old rows both map to is written ONCE: the DIRECT row wins
        over an AI row, otherwise the earlier row in the set's order.
  --rollback --half <path> --snapshot <path>   per key: a conditional delete of a key this run put -- the key is a
        DIRECT/AI shared_key of the set that is NOT in the snapshot, and the condition is attribute_exists(ticker) AND
        updated_by IN (the run's two values). A key another writer put, or one that already existed, is never deleted.

Row values. DIRECT: classified_by `scheduled`, updated_by RUN_UPDATED_BY, name = the set's clean_name, identifier_namespace
NAME for a NAME:: key and CUSIP for a CUSIP: key (absent for a ticker, which reads TICKER). AI rows are the runner's own
(classified_by `model`, updated_by `mdpf-secclass-model`); the runner builds no identifier_namespace, so the table handed to it
adds NAME / CUSIP on a put by key prefix (surprise row MDPF_SECCLASS-W26-S5).
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SET = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_RECLASSIFY_SET_20261007.tsv"
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
RUNNER = ROOT / "infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py"
COLS = ["old_key", "shared_key", "held", "route", "asset_class", "sub_asset_class", "clean_name"]
SIX = frozenset({"cash", "fixed_income", "equity", "structured", "alternatives", "commodities"})
ROUTES = ("PRESENT", "DIRECT", "AI", "UNPLACED-KEY")
CONTRACT = ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json"
# Andrew-direct 2026-10-06 00:03Z: up to 8,495 old-table rows to the model; the run refuses a larger AI key set.
VENDOR_KEY_CEILING = 8495
REGION = "us-east-1"
TABLE = "etf-classifications"
RUN_UPDATED_BY = "mdpf-secclass-old-list-reclassify"
MODEL_UPDATED_BY = "mdpf-secclass-model"
BLOCKED = ("put_item", "update_item", "delete_item", "batch_write_item", "batch_writer")
HALF_RE = {"COO": re.compile(r"^## COO half -- SIGNED\b", re.MULTILINE), "CTO": re.compile(r"^## CTO half -- SIGNED\b", re.MULTILINE)}


class GuardedTable:
    """Delegates reads; counts and refuses every write."""

    def __init__(self, inner):
        self._inner = inner
        self.write_attempts = 0

    def __getattr__(self, name):
        if name in BLOCKED:
            def refuse(*_a, **_k):
                self.write_attempts += 1
                raise RuntimeError(f"REFUSED: the dry run attempted {name}")
            return refuse
        return getattr(self._inner, name)


class CountingSend:
    """The dry-run model transport: counts and refuses every call."""

    def __init__(self):
        self.calls = 0

    def __call__(self, payload, **_kw):
        self.calls += 1
        raise RuntimeError("REFUSED: the dry run called the model transport")


class NamespaceTable:
    """Hands the AI runner a table whose put_item adds identifier_namespace by key prefix (the runner builds none)."""

    def __init__(self, inner):
        self._inner = inner

    def put_item(self, **kw):
        item = kw.get("Item") or {}
        key = str(item.get("ticker", ""))
        if "identifier_namespace" not in item:
            if key.startswith("NAME::"):
                item["identifier_namespace"] = "NAME"
            elif key.startswith("CUSIP:"):
                item["identifier_namespace"] = "CUSIP"
        return self._inner.put_item(**kw)

    def __getattr__(self, name):
        return getattr(self._inner, name)


def load_runner():
    sys.path.insert(0, str(SHARED))
    spec = importlib.util.spec_from_file_location("classify_residual_model_for_reclassify", str(RUNNER))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_set(path: Path):
    with path.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh, delimiter="\t")
        if rd.fieldnames != COLS:
            raise SystemExit(f"ERROR: set header is {rd.fieldnames!r}, expected {COLS!r}")
        rows = list(rd)
    bad = [r["old_key"] for r in rows if r["route"] not in ROUTES]
    if bad:
        raise SystemExit(f"ERROR: {len(bad)} rows carry a route outside {ROUTES!r} (first {bad[0]!r})")
    return rows


def half_signed(path):
    """True only when the file holds BOTH signed-half headings."""
    text = Path(path).read_text(encoding="utf-8")
    return {who: bool(rx.search(text)) for who, rx in HALF_RE.items()}


def scan_live(table):
    items, kw = [], {"ConsistentRead": True, "ProjectionExpression": "ticker, asset_class, sub_asset_class"}
    while True:
        resp = table.scan(**kw)
        items.extend(resp.get("Items", []))
        if "LastEvaluatedKey" not in resp:
            return items
        kw["ExclusiveStartKey"] = resp["LastEvaluatedKey"]


def six_vocab(items, TableVocabulary):
    ac, subs = set(), {}
    for it in items:
        c, s = it.get("asset_class"), it.get("sub_asset_class")
        if c in SIX:
            ac.add(c)
            if s:
                subs.setdefault(c, set()).add(s)
    return TableVocabulary(asset_classes=ac, sub_asset_classes=subs)


def contract_vocab(TableVocabulary):
    """The bound (ruling 2.5, R12): the contract's closed sub_asset_class list per class, the six classes only -- not the values
    the live table happens to hold (the table still carries legacy fixed_income/Cash rows)."""
    c = json.loads(CONTRACT.read_text(encoding="utf-8"))
    closed = {k: set(v) for k, v in c["fields"]["sub_asset_class"]["values_by_class"].items() if k in SIX}
    return TableVocabulary(asset_classes=set(closed), sub_asset_classes=closed), c.get("contract_version")


def outside(vocab, ac, sac):
    return ac not in vocab.asset_classes or not sac or sac not in vocab.sub_asset_classes.get(ac, set())


def plan(rows, existing, vocab):
    """Split the set into what a write would do. Returns a dict of ordered lists (held first, as the set is ordered)."""
    present = [r for r in rows if r["route"] == "PRESENT"]
    unplaced = [r for r in rows if r["route"] == "UNPLACED-KEY"]
    group = {}
    for r in rows:
        if r["route"] in ("DIRECT", "AI"):
            group.setdefault(r["shared_key"], []).append(r)
    direct, ai, now_present, off_vocab = [], [], [], []
    for key, members in group.items():
        if key in existing:
            now_present.append(key)
            continue
        dr = next((m for m in members if m["route"] == "DIRECT"), None)
        if dr is not None:
            ac, sac = dr["asset_class"], dr["sub_asset_class"]
            if ac not in SIX or outside(vocab, ac, sac):
                off_vocab.append(key)
                continue
            direct.append(dr)
        else:
            ai.append(members[0])
    # the set is held-first, so the groups' first members are; a group is held if ANY of its rows is
    held_key = {k for k, ms in group.items() if any(m["held"] == "true" for m in ms)}
    ai.sort(key=lambda r: (0 if r["shared_key"] in held_key else 1))
    direct.sort(key=lambda r: (0 if r["shared_key"] in held_key else 1))
    return {"present": present, "unplaced": unplaced, "direct": direct, "ai": ai, "now_present": now_present,
            "off_vocab": off_vocab, "group": group}


def direct_item(r):
    key = r["shared_key"]
    item = {"ticker": key, "asset_class": r["asset_class"], "classified_by": "scheduled",
            "updated_by": RUN_UPDATED_BY, "name": r["clean_name"] or key}
    if r["sub_asset_class"]:
        item["sub_asset_class"] = r["sub_asset_class"]
    if key.startswith("NAME::"):
        item["identifier_namespace"] = "NAME"
    elif key.startswith("CUSIP:"):
        item["identifier_namespace"] = "CUSIP"
    return item


def summary(rows):
    by = {k: 0 for k in ROUTES}
    for r in rows:
        by[r["route"]] += 1
    return by


def do_dry_run(rows, table):
    runner = load_runner()
    from etf_classification_scheduled import TableVocabulary
    guard = GuardedTable(table)
    send = CountingSend()
    items = scan_live(guard)
    existing = {str(i["ticker"]) for i in items}
    vocab, cver = contract_vocab(TableVocabulary)
    p = plan(rows, existing, vocab)
    pairs = [(r["shared_key"], r["clean_name"] or None) for r in p["ai"]]
    rep = runner.run(pairs, vocab=vocab, existing=existing, table=None, s3=None, send=send, api_key=None,
                     use_model=False, do_write=False)
    by = summary(rows)
    collapsed = sum(len(m) - 1 for m in p["group"].values())
    print(f"INFO set_rows={len(rows)} live_rows={len(existing)} direct_keys={len(p['direct'])} ai_keys={len(p['ai'])} "
          f"collapsed_duplicate_keys={collapsed} now_present={len(p['now_present'])} off_vocab={len(p['off_vocab'])} "
          f"bound=contract {cver} vendor_ceiling={VENDOR_KEY_CEILING}")
    print("INFO " + runner.summary_line(rep))
    bad = []
    if send.calls != 0 or rep["model_calls"] != 0:
        bad.append(f"model_calls={send.calls}/{rep['model_calls']}")
    if guard.write_attempts != 0:
        bad.append(f"puts={guard.write_attempts}")
    if rep["would_land"] != 0:
        bad.append(f"would_land={rep['would_land']}")
    if p["off_vocab"]:
        bad.append(f"off_vocab={len(p['off_vocab'])}:{p['off_vocab'][:5]}")
    if len(p["ai"]) > VENDOR_KEY_CEILING:
        bad.append(f"ai_keys={len(p['ai'])}>ceiling")
    if rep["to_model"] != len(p["ai"]):
        bad.append(f"to_model={rep['to_model']}!=ai_keys={len(p['ai'])}")
    if bad:
        print("RECLASSIFY-DRY-RUN-BAD " + " ".join(bad))
        return 1
    print(f"RECLASSIFY-DRY-RUN direct={by['DIRECT']} to_ai={by['AI']} unplaced_key={by['UNPLACED-KEY']} "
          f"present={by['PRESENT']} puts={guard.write_attempts} model_calls={send.calls}")
    return 0


def require_halves(half):
    state = half_signed(half)
    if not all(state.values()):
        raise SystemExit(f"BLOCKED: halves not both SIGNED in {half}: {state}")


def do_write(rows, table, s3, half, snapshot, chunk, workers, send=None, api_key=None):
    require_halves(half)
    snap = Path(snapshot)
    if snap.exists():
        raise SystemExit(f"BLOCKED: snapshot {snap} already exists")
    runner = load_runner()
    from etf_classification_scheduled import TableVocabulary, write
    items = scan_live(table)
    existing = {str(i["ticker"]) for i in items}
    vocab, _cver = contract_vocab(TableVocabulary)
    pre = plan(rows, existing, vocab)
    if pre["off_vocab"] or len(pre["ai"]) > VENDOR_KEY_CEILING:
        raise SystemExit(f"BLOCKED: off_vocab={len(pre['off_vocab'])} ai_keys={len(pre['ai'])} (ceiling {VENDOR_KEY_CEILING})")
    snap.write_text(json.dumps({"taken_at": datetime.now(timezone.utc).isoformat(), "table": TABLE,
                                "run_updated_by": [RUN_UPDATED_BY, MODEL_UPDATED_BY],
                                "rows": len(existing), "keys": sorted(existing)}), encoding="utf-8")
    p = plan(rows, existing, vocab)
    written = refused = 0
    for outcome in write([direct_item(r) for r in p["direct"]], table=table):
        if outcome[1] == "written":
            written += 1
        else:
            refused += 1
    print(f"DIRECT planned={len(p['direct'])} written={written} refused={refused}")
    existing |= {r["shared_key"] for r in p["direct"]}
    if api_key is None:
        api_key = runner.get_kimi_key()
    use_table = NamespaceTable(table)
    tot = {"to_model": 0, "would_land": 0, "written": 0, "refused": 0, "calls": 0}
    pairs = [(r["shared_key"], r["clean_name"] or None) for r in p["ai"]]
    for i in range(0, len(pairs), chunk):
        rep = runner.run(pairs[i:i + chunk], vocab=vocab, existing=existing, table=use_table, s3=s3,
                         send=send or runner.default_send, api_key=api_key, use_model=True, do_write=True,
                         workers=workers)
        for ticker, why in rep["left_unresolved"]:
            print(f"UNRESOLVED {ticker}: {why}")
        tot["to_model"] += rep["to_model"]
        tot["would_land"] += rep["would_land"]
        tot["written"] += rep["written"]
        tot["refused"] += rep["refused_by_put"]
        tot["calls"] += rep["model_calls"]
        existing |= {r["ticker"] for r in rep["rows"]}
        sent = len(pairs[i:i + chunk])
        landed_outside = [r["ticker"] for r in rep["rows"] if outside(vocab, r.get("asset_class"), r.get("sub_asset_class"))]
        print(f"AI chunk {i}-{i + chunk}: keys_sent={sent} model_calls={rep['model_calls']} "
              f"landed_outside_contract={len(landed_outside)} " + runner.summary_line(rep), flush=True)
        if landed_outside:
            raise SystemExit(f"STOPPED: chunk {i} landed {len(landed_outside)} rows outside the contract: {landed_outside[:5]}; "
                             f"roll back this run with --rollback")
    print(f"RECLASSIFY-WRITE direct_written={written} ai_to_model={tot['to_model']} ai_written={tot['written']} "
          f"ai_refused={tot['refused']} model_calls={tot['calls']} snapshot={snap}")
    return 0


def do_rollback(rows, table, s3, half, snapshot):
    require_halves(half)
    snap = json.loads(Path(snapshot).read_text(encoding="utf-8"))
    before = set(snap["keys"])
    values = snap["run_updated_by"]
    runner = load_runner()
    keys = sorted({r["shared_key"] for r in rows if r["route"] in ("DIRECT", "AI") and r["shared_key"]} - before)
    deleted = skipped = 0
    for key in keys:
        try:
            table.delete_item(Key={"ticker": key},
                              ConditionExpression="attribute_exists(ticker) AND updated_by IN (:a, :b)",
                              ExpressionAttributeValues={":a": values[0], ":b": values[1]})
            deleted += 1
        except Exception as e:  # only ConditionalCheckFailed is expected; anything else is re-raised
            if getattr(e, "response", {}).get("Error", {}).get("Code") == "ConditionalCheckFailedException":
                skipped += 1
            else:
                raise
    index = runner._load_index_writer()
    address, count = index.write_listing(table, s3, now=datetime.now(timezone.utc),
                                         address=index.index_address(index.run_day_of(datetime.now(timezone.utc))))
    print(f"RECLASSIFY-ROLLBACK candidates={len(keys)} deleted={deleted} skipped_not_this_run={skipped} "
          f"index={address} count={count}")
    return 0


def main(argv=None, table=None, s3=None, send=None, api_key=None) -> int:
    ap = argparse.ArgumentParser(description="Old-list reclassification writer; dry run unless --write / --rollback.")
    ap.add_argument("--set", default=str(SET))
    ap.add_argument("--write", action="store_true", help="the issuer's act; needs --half and --snapshot")
    ap.add_argument("--rollback", action="store_true", help="conditional delete of the keys a run put; needs --half, --snapshot")
    ap.add_argument("--half", default=None, help="the half-request file; BOTH halves must read SIGNED")
    ap.add_argument("--snapshot", default=None, help="the pre-write key snapshot (written by --write, read by --rollback)")
    ap.add_argument("--chunk", type=int, default=250, help="AI keys per classify-put-index chunk")
    ap.add_argument("--workers", type=int, default=1)
    a = ap.parse_args(argv)
    if a.write and a.rollback:
        raise SystemExit("ERROR: --write and --rollback are separate acts")
    rows = read_set(Path(a.set))
    if table is None:
        table = boto3.resource("dynamodb", region_name=REGION).Table(TABLE)
    if a.write or a.rollback:
        if not a.half or not a.snapshot:
            raise SystemExit("BLOCKED: --write/--rollback require --half <path> and --snapshot <path>")
        if s3 is None:
            s3 = boto3.client("s3", region_name=REGION)
        if a.write:
            return do_write(rows, table, s3, a.half, a.snapshot, a.chunk, a.workers, send=send, api_key=api_key)
        return do_rollback(rows, table, s3, a.half, a.snapshot)
    return do_dry_run(rows, table)


if __name__ == "__main__":
    sys.exit(main())
