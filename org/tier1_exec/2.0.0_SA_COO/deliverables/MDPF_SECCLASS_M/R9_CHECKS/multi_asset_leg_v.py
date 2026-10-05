#!/usr/bin/env python3
"""multi_asset_leg_v.py -- leg V of ledger secclass-multi-asset-rows-and-remint-m-20261004: the first scheduled Holdings
publication after the act (irpt-holdings-snapshot, cron(15 10 ? * MON-FRI *) America/New_York = 14:15Z).

READ-ONLY. Per firm:
  1. the served manifest: the newest date (POST) and the one before it (PRE, published before the act);
  2. every platinum part of both revisions, eight parts in flight, each scanned and dropped: the packet's SECURITY nodes (display symbol or
     security_id in the row set's MOVE/WRITE keys) and their asset_class;
  3. POST's platinum header: the producer's own reconcile (account totals unchanged by the regroup);
  4. the DEPLOYED irpt-holdings bytes (get-function, CodeSha256 printed): load_snapshot -> project -> validate_slice ->
     require_reconciled for the accounts that hold a packet key; class_totals must carry multi_asset.
  5. the FWD-9 HELD CENSUS (the same pass): the 31 US bare-ticker WRITE keys of R7_CHECKS/FWD9_ROW_SET_20261005.tsv, which
     the FWD-9 rows half holds until their served effect is read -- per key, the nodes that hold it and their
     asset_class / sub_asset_class / asset_class_basis today.
Writes MULTI_ASSET_LEG_V_<firm>_20261005.json beside this file and prints one LEG-V line and one FWD9-US-HELD line.

Usage (repo root): python .../R9_CHECKS/multi_asset_leg_v.py <firm> [--max-accounts 25]
"""
from __future__ import annotations

import argparse
import collections
import concurrent.futures
import io
import json
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import remint_served_effect as base  # noqa: E402

PIN_T = "RmruvCeo"
FWD9_SET = HERE.parent / "R7_CHECKS" / "FWD9_ROW_SET_20261005.tsv"
s3 = boto3.client("s3", region_name="us-east-1")


def fwd9_us_keys():
    """The set file's WRITE lines keyed by a bare US ticker (identifier_namespace absent or TICKER)."""
    keys = set()
    for line in FWD9_SET.read_text(encoding="utf-8").splitlines():
        f = line.split("	")
        if len(f) == 5 and f[0] == "WRITE" and json.loads(f[4]).get("identifier_namespace", "TICKER") == "TICKER":
            keys.add(f[1])
    return keys


def get_json(bucket, key, ver=None):
    return json.loads(base.get(bucket, key, ver))


def packet_nodes(rev_manifest, keys, us_keys=frozenset()):
    """Stream every platinum part of one revision; the packet's SECURITY nodes by key and class."""
    by_key = collections.defaultdict(collections.Counter)
    amount = collections.defaultdict(float)
    accounts = set()
    us_held = collections.defaultdict(collections.Counter)
    us_accounts = collections.defaultdict(set)
    parts = 0
    objs = [p["object"] for p in rev_manifest["partitions"]]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(get_json, o["bucket"], o["key"], o.get("version_id")) for o in objs]
        for fut in concurrent.futures.as_completed(futures):
            doc = fut.result()
            parts += 1
            scan(doc, keys, by_key, amount, accounts)
            scan_us(doc, us_keys, us_held, us_accounts)
            del doc
    classes = collections.Counter()
    for c in by_key.values():
        classes.update(c)
    return {"parts_read": parts, "partitions_declared": len(rev_manifest["partitions"]),
            "keys_held": len(by_key), "nodes_by_class": dict(classes),
            "amount_by_class": {k: round(v, 2) for k, v in amount.items()},
            "by_key": {k: dict(v) for k, v in sorted(by_key.items())}, "accounts": sorted(accounts),
            "fwd9_us_held": {k: {"accounts": len(us_accounts[k]), "class_sub_basis": dict(v)}
                             for k, v in sorted(us_held.items())}}


def scan_us(doc, us_keys, us_held, us_accounts):
    """The FWD-9 US WRITE keys held today: class / sub-class / basis per node (display symbol match)."""
    if not us_keys:
        return
    for n in doc.get("nodes") or []:
        if n.get("node_kind") != "SECURITY":
            continue
        sym = (n.get("display") or {}).get("symbol")
        if sym not in us_keys:
            continue
        us_held[sym]["%s | %s | %s" % (n.get("asset_class"), n.get("sub_asset_class"), n.get("asset_class_basis"))] += 1
        us_accounts[sym].add(n["node_id"].split(":")[0])


def scan(doc, keys, by_key, amount, accounts):
    """One part's packet SECURITY nodes (display symbol or security_id in the row set's keys), by class."""
    for n in doc.get("nodes") or []:
        if n.get("node_kind") != "SECURITY":
            continue
        sid = (n.get("security_id") or {}).get("value")
        sym = (n.get("display") or {}).get("symbol")
        hit = sid if sid in keys else sym if sym in keys else None
        if hit is None:
            continue
        cls = n.get("asset_class") or "unclassified"
        by_key[hit][cls] += 1
        amount[cls] += float((n.get("amount") or {}).get("value") or 0.0)
        accounts.add(n["node_id"].split(":")[0])


def deployed_reader():
    lam = boto3.client("lambda", region_name="us-east-1")
    fn = lam.get_function(FunctionName="irpt-holdings")
    sha = fn["Configuration"]["CodeSha256"]
    body = urllib.request.urlopen(fn["Code"]["Location"], timeout=300).read()  # noqa: S310 -- AWS presigned code URL
    tmp = tempfile.mkdtemp(prefix="legv_reader_")
    zipfile.ZipFile(io.BytesIO(body)).extractall(tmp)
    sys.path.insert(0, tmp)
    import snapshot as reader  # noqa: E402 -- the deployed bytes
    return reader, sha, fn["Configuration"]["LastModified"], tmp


def reader_read(reader, firm, as_of, accounts):
    snap = reader.load_snapshot(firm, as_of=as_of, account_ids=accounts)
    # The handler's scope carries the viewer's selection fingerprint and the verified firm; project() copies both into the
    # slice's scope block, which the contract types as strings. This read names itself in the fingerprint.
    sliced = reader.project(snap, {"permitted_account_set": accounts, "selected_account_ids": accounts,
                                   "selected_account_set_fingerprint": "legv-read-%d-accounts" % len(accounts),
                                   "verified_request_firm_id": firm})
    out = {"accounts": len(accounts), "validate": reader.validate_slice(sliced)}
    try:
        reader.require_reconciled(sliced)
        out["reconciled"] = True
    except Exception as exc:  # noqa: BLE001 -- the refusal is the measurement
        out["reconciled"] = False
        out["reconcile_refusal"] = f"{type(exc).__name__}: {exc}"
    totals = {r.get("asset_class"): r for r in (sliced.get("class_totals") or [])}
    out["class_totals_classes"] = sorted(k for k in totals if k)
    ma = totals.get("multi_asset") or {}
    out["multi_asset_row"] = {k: ma.get(k) for k in ("asset_class", "amount", "value", "percent", "of_total") if k in ma}
    out["business_date"] = (sliced.get("clocks") or {}).get("business_date")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("firm", choices=sorted(base.FIRMS))
    ap.add_argument("--max-accounts", type=int, default=25)
    a = ap.parse_args()
    bucket = base.FIRMS[a.firm]
    keys = set(base.row_keys())
    us_keys = fwd9_us_keys()
    head = s3.head_object(Bucket=bucket, Key=f"irpt/{a.firm}/platinum/holdings/current/manifest.json")
    cur = get_json(bucket, f"irpt/{a.firm}/platinum/holdings/current/manifest.json")
    dates = sorted(cur["dates"])
    post = cur["latest_date"]
    pre = dates[dates.index(post) - 1] if dates.index(post) > 0 else None
    out = {"claim": "measured (served platinum, streamed; deployed reader bytes)", "firm": a.firm,
           "current_manifest_last_modified": head["LastModified"].isoformat(), "post_date": post, "pre_date": pre,
           "packet_keys": len(keys)}
    revs = {}
    for label, d in (("post", post), ("pre", pre)):
        if d is None:
            continue
        ref = cur["dates"][d]["manifest"]
        rm = get_json(ref["bucket"], ref["key"], ref.get("version_id"))
        revs[label] = rm
        out[label] = {"revision": rm["revision"], "as_of_timestamp": (rm.get("clocks") or {}).get("as_of_timestamp"),
                      **packet_nodes(rm, keys, us_keys if label == "post" else frozenset())}
        print(label, d, {k: out[label][k] for k in ("parts_read", "keys_held", "nodes_by_class")}, flush=True)
    hdr_ref = revs["post"]["platinum_header"]
    hdr = get_json(hdr_ref["bucket"], hdr_ref["key"], hdr_ref.get("version_id"))
    out["post_reconcile"] = (hdr.get("attribution_holdouts") or {}).get("reconcile")
    out["post_custody_total"] = ((hdr.get("custody_totals") or {}).get("total_market_value") or {}).get("value")
    accounts = out["post"]["accounts"][: a.max_accounts]
    if accounts:
        reader, sha, lm, tmp = deployed_reader()
        out["reader"] = {"code_sha256": sha, "pin_t_match": sha.startswith(PIN_T), "last_modified": lm,
                         **reader_read(reader, a.firm, post, accounts)}
    for side in ("post", "pre"):
        if side in out:
            out[side]["accounts"] = len(out[side]["accounts"])
    path = HERE / f"MULTI_ASSET_LEG_V_{a.firm}_20261005.json"
    path.write_text(json.dumps(out, indent=1, sort_keys=True), encoding="utf-8")
    r = out.get("reader") or {}
    print(f"LEG-V firm={a.firm} post={post} pre={pre} manifest_lm={out['current_manifest_last_modified']} "
          f"post_classes={out['post']['nodes_by_class']} pre_classes={(out.get('pre') or {}).get('nodes_by_class')} "
          f"reconciled={(out['post_reconcile'] or {}).get('reconciled')} reader_pin_t={r.get('pin_t_match')} "
          f"reader_valid={(r.get('validate') or {}).get('valid')} reader_reconciled={r.get('reconciled')} "
          f"reader_multi_asset={'multi_asset' in (r.get('class_totals_classes') or [])} out={path.name}")
    held = out["post"].get("fwd9_us_held") or {}
    print(f"FWD9-US-HELD firm={a.firm} date={post} keys={len(us_keys)} held={len(held)} "
          f"nodes={sum(sum(v['class_sub_basis'].values()) for v in held.values())} keys_held={sorted(held)}")


if __name__ == "__main__":
    main()
