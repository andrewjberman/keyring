"""e49_ai_write.py -- MDPF_SECCLASS SC-e-49, the AI leg: the existing runner over the re-planned missing-list AI keys.

Runs AFTER the e32 V3 AI leg (CTO e32 V3 half condition 2), at a head carrying R12c (clean_name ASCII) and TO-SC-e65 amendment 3.
Input: R12_CHECKS/e49_replan/FWD15_AI_PLAN_<firm>_20261007.json, route AI, held-first (amount largest first), one pair per distinct
shared key: (shared_key, plan name). Keys already in etf-classifications at run time are skipped by the runner (the e32 act lands
the 157 old-table ones). Bound: the contract 0.8.0 closed list (old_list_reclassify_write.contract_vocab), checked again per chunk.
Vendor: kimi-k3 via the runner, name and key only; laptop 1.0.0_SA_CTO msg 106533 ruled the keys covered; at most 1,172 keys.

  python e49_ai_write.py                                         # dry run: no model call, no put
  python e49_ai_write.py --write --half <e49 request.md> --cto-half <CTO half.md> --snapshot <new path> [--chunk 250]
  python e49_ai_write.py --rollback --snapshot <path>            # deletes this act's model rows (updated_by guard)
"""
import argparse
import glob
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("old_list_writer", str(HERE.parent / "R10_CHECKS/old_list_reclassify_write.py"))
W = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(W)

PLAN_GLOB = str(HERE / "e49_replan" / "FWD15_AI_PLAN_*_20261007.json")
KEY_CEILING = 1172


def ai_pairs():
    entries = []
    for f in sorted(glob.glob(PLAN_GLOB)):
        p = json.loads(Path(f).read_text(encoding="utf-8"))
        entries += [e for e in p["entries"] if e["route"] == "AI"]
    entries.sort(key=lambda e: -(e.get("amount") or 0.0))
    pairs, seen = [], set()
    for e in entries:
        k = e.get("shared_key") or e["key"]
        if k not in seen:
            seen.add(k)
            pairs.append((k, e.get("name") or None))
    return len(entries), pairs


def excluded_keys(path):
    """Keys the issuer ruled FINAL (refused twice under the model, the second time under the SC-e-78 prompt; TO amendment
    ~20:2xZ). Accepts a JSON list of keys, a list of {"key"|"ticker"|"shared_key": ...} objects, or {"keys": [...]}."""
    if not path:
        return set()
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("keys") or data.get("model_refused_in_run2_and_run3") or data.get("entries") or []
    out = set()
    for x in data:
        out.add(str(x if isinstance(x, str) else (x.get("key") or x.get("ticker") or x.get("shared_key"))))
    return out


def signed(half, cto_half):
    a = bool(re.search(r"^## COO half -- SIGNED\b", Path(half).read_text(encoding="utf-8"), re.MULTILINE))
    b = bool(re.search(r"^## VERDICT: SIGNED\b", Path(cto_half).read_text(encoding="utf-8"), re.MULTILINE))
    return a and b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--rollback", action="store_true")
    ap.add_argument("--half")
    ap.add_argument("--cto-half")
    ap.add_argument("--snapshot")
    ap.add_argument("--chunk", type=int, default=250)
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--exclude", help="JSON of keys ruled FINAL; dropped from the plan (never from rollback)")
    a = ap.parse_args()
    runner = W.load_runner()
    from etf_classification_scheduled import TableVocabulary
    table = boto3.resource("dynamodb", region_name=W.REGION).Table(W.TABLE)
    s3 = boto3.client("s3", region_name=W.REGION)
    n_entries, pairs = ai_pairs()

    if a.rollback:
        snap = json.loads(Path(a.snapshot).read_text(encoding="utf-8"))
        before = set(snap["keys"])
        deleted = skipped = 0
        for k, _n in pairs:
            if k in before or not a.write:
                continue
            try:
                table.delete_item(Key={"ticker": k}, ConditionExpression="attribute_exists(ticker) AND updated_by = :b",
                                  ExpressionAttributeValues={":b": W.MODEL_UPDATED_BY})
                deleted += 1
            except Exception as e:  # only ConditionalCheckFailed is expected
                if getattr(e, "response", {}).get("Error", {}).get("Code") == "ConditionalCheckFailedException":
                    skipped += 1
                else:
                    raise
        index = runner._load_index_writer()
        now = datetime.now(timezone.utc)
        address, count = (index.write_listing(table, s3, now=now, address=index.index_address(index.run_day_of(now)))
                          if a.write else (None, None))
        print(f"E49-AI-ROLLBACK write={a.write} deleted={deleted} skipped_not_this_run={skipped} index={address} count={count}")
        return 0

    items = W.scan_live(table)
    existing = {str(i["ticker"]) for i in items}
    vocab, cver = W.contract_vocab(TableVocabulary)
    final = excluded_keys(a.exclude)
    todo = [(k, n) for k, n in pairs if k not in existing and k not in final]
    n_final = sum(1 for k, _n in pairs if k not in existing and k in final)
    bad = []
    if len(pairs) > KEY_CEILING:
        bad.append(f"keys={len(pairs)}>ceiling {KEY_CEILING}")
    if not a.write:
        send = W.CountingSend()
        rep = runner.run(todo, vocab=vocab, existing=existing, table=None, s3=None, send=send, api_key=None,
                         use_model=False, do_write=False)
        if send.calls or rep["model_calls"]:
            bad.append("model_calls")
        if rep["direct"]:
            bad.append(f"runner_direct={rep['direct']} (S63: the run head must carry TO-SC-e65 amendment 3)")
        print(f"E49-AI-DRY-RUN entries={n_entries} keys={len(pairs)} present_now={len(pairs) - len(todo) - n_final} "
              f"excluded_final={n_final} to_model={rep['to_model']} "
              f"runner_direct={rep['direct']} bound=contract {cver} ok={not bad} problems={bad}")
        return 0 if not bad else 1
    if bad or not (a.half and a.cto_half and a.snapshot) or not signed(a.half, a.cto_half):
        raise SystemExit(f"BLOCKED: needs --half (COO SIGNED), --cto-half (VERDICT: SIGNED), --snapshot; problems={bad}")
    snap = Path(a.snapshot)
    if snap.exists():
        raise SystemExit(f"BLOCKED: snapshot {snap} already exists")
    snap.write_text(json.dumps({"taken_at": datetime.now(timezone.utc).isoformat(), "table": W.TABLE, "rows": len(existing),
                                "updated_by": W.MODEL_UPDATED_BY, "keys": sorted(existing)}), encoding="utf-8")
    api_key = runner.get_kimi_key()
    use_table = W.NamespaceTable(table)
    tot = {"sent": 0, "calls": 0, "written": 0, "refused": 0, "unresolved": 0}
    for i in range(0, len(todo), a.chunk):
        chunk = todo[i:i + a.chunk]
        rep = runner.run(chunk, vocab=vocab, existing=existing, table=use_table, s3=s3, send=runner.default_send,
                         api_key=api_key, use_model=True, do_write=True, workers=a.workers)
        for ticker, why in rep["left_unresolved"]:
            print(f"UNRESOLVED {ticker}: {why}")
        outside = [r["ticker"] for r in rep["rows"] if W.outside(vocab, r.get("asset_class"), r.get("sub_asset_class"))]
        tot["sent"] += len(chunk)
        tot["calls"] += rep["model_calls"]
        tot["written"] += rep["written"]
        tot["refused"] += rep["refused_by_put"]
        tot["unresolved"] += len(rep["left_unresolved"])
        existing |= {r["ticker"] for r in rep["rows"]}
        print(f"E49 AI chunk {i}-{i + len(chunk)}: keys_sent={len(chunk)} model_calls={rep['model_calls']} "
              f"landed_outside_contract={len(outside)} " + runner.summary_line(rep), flush=True)
        if outside:
            raise SystemExit(f"STOPPED: chunk {i} landed {len(outside)} rows outside the contract: {outside[:5]}; run --rollback")
    print(f"E49-AI-WRITE keys_sent={tot['sent']} model_calls={tot['calls']} written={tot['written']} refused={tot['refused']} "
          f"unresolved={tot['unresolved']} snapshot={snap}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
