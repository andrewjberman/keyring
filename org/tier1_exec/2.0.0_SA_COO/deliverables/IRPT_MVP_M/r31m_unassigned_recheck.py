#!/usr/bin/env python3
"""r31m_unassigned_recheck.py -- cell IB-mr-311 AMENDMENT 1: E-M2 criterion e2 for the UNASSIGNED case, over every
instance, on the served publication.

The first E-M2 read (laptop @471da6f0b0) tested ONE unassigned account (value 0.0) against "no non-TARGET child", but every
ACCOUNT in the L0 category shape carries a CATEGORY child (49F 7,597 accounts, 7,597 CATEGORY nodes), so that rule cannot
hold for any account. The residual is VISIBLE and NOT REDISTRIBUTED when an unassigned account:
  (a) carries its custody value as an ACCOUNT node (it is present, not dropped),
  (b) its subtree ties (every parent/basis partition sums to its parent within 0.01, TARGET excluded), and
  (c) no model-attribution node (MODEL_LEAF, MODEL_WRAPPER, SLEEVE) sits under it -- its value is not spread into sleeves.
Every unassigned account listed in each firm header is checked; zero-value accounts are counted separately.

Firms: the unassigned case occurs at 49financial and inflection only (laptop read: cottonwood 0); both are readable from dell2
since the NFRA_CTLPLN fence join (probed 10:4xZ). Read-only S3 gets; writes one result file.

    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r31m_unassigned_recheck.py --out <path>.json
    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r31m_unassigned_recheck.py --self-test
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r30m_fwd5_replay_read import account_tie, read_firm, val  # noqa: E402

FIRMS = {"49financial": "opal-data-49financial", "inflection": "opal-data-inflection"}
MODEL_KINDS = {"MODEL_LEAF", "MODEL_WRAPPER", "SLEEVE"}


def check_firm(nodes, header):
    by_id = {n["node_id"]: n for n in nodes}
    kids = {}
    for n in nodes:
        kids.setdefault(n.get("parent_node_id"), []).append(n)
    ids = list(((header.get("attribution_holdouts") or {}).get("unassigned") or {}).get("account_ids") or [])
    out = {"listed": len(ids), "present": 0, "zero_value": 0, "tie": 0, "no_model_node": 0, "pass": 0, "failing": []}
    for aid in ids:
        acc = by_id.get(aid)
        if acc is None or acc.get("node_kind") != "ACCOUNT":
            out["failing"].append({"account": aid, "why": "not served as an ACCOUNT node"})
            continue
        out["present"] += 1
        if (val(acc) or 0.0) == 0.0:
            out["zero_value"] += 1
        stack, model_nodes = [aid], []
        while stack:
            for k in kids.get(stack.pop(), []):
                if k.get("node_kind") in MODEL_KINDS and k.get("basis") != "TARGET":
                    model_nodes.append(k["node_id"])
                stack.append(k["node_id"])
        t = account_tie(nodes, acc)
        ok_tie = t["ties"] or t["partitions"] == 0
        out["tie"] += ok_tie
        out["no_model_node"] += not model_nodes
        if ok_tie and not model_nodes:
            out["pass"] += 1
        elif len(out["failing"]) < 10:
            out["failing"].append({"account": aid, "value": val(acc), "ties": t["ties"],
                                   "model_nodes": model_nodes[:5], "unbalanced": t["partitions_unbalanced"][:3]})
    out["verdict"] = "PASS" if out["listed"] and out["pass"] == out["listed"] else "FAIL"
    return out


def evaluate(pubs):
    res = {"cell": "IB-mr-311", "amendment": 1, "publications": {f: p for f, (p, _, _) in pubs.items()}, "firms": {}}
    for f, (_, header, nodes) in pubs.items():
        res["firms"][f] = check_firm(nodes, header)
    listed = sum(r["listed"] for r in res["firms"].values())
    passed = sum(r["pass"] for r in res["firms"].values())
    res["e2_unassigned"] = {"verdict": "PASS" if listed and passed == listed else "FAIL",
                            "accounts_passing": passed, "accounts_listed": listed,
                            "nonzero_accounts": sum(r["present"] - r["zero_value"] for r in res["firms"].values())}
    return res


def self_test():
    def node(i, p, kind, v, basis="OBSERVED"):
        return {"node_id": i, "parent_node_id": p, "node_kind": kind, "basis": basis, "amount": {"value": v}}
    good = [node("u1", None, "ACCOUNT", 50.0), node("c1", "u1", "CATEGORY", 50.0), node("x1", "c1", "SECURITY", 50.0),
            node("u0", None, "ACCOUNT", 0.0), node("c0", "u0", "CATEGORY", 0.0)]
    hdr = {"attribution_holdouts": {"unassigned": {"account_ids": ["u1", "u0"]}}}
    r = evaluate({"49financial": ({}, hdr, good)})
    assert r["e2_unassigned"]["verdict"] == "PASS" and r["firms"]["49financial"]["zero_value"] == 1, r
    # negative arm: the unassigned account's value spread into a model sleeve FAILs
    bad = good + [node("m1", "c1", "MODEL_LEAF", 50.0)]
    bad = [dict(n, parent_node_id="m1") if n["node_id"] == "x1" else n for n in bad]
    r2 = evaluate({"49financial": ({}, hdr, bad)})
    assert r2["e2_unassigned"]["verdict"] == "FAIL", r2
    # absence arm: an unassigned id not served as an ACCOUNT FAILs
    r3 = evaluate({"49financial": ({}, {"attribution_holdouts": {"unassigned": {"account_ids": ["zz"]}}}, good)})
    assert r3["e2_unassigned"]["verdict"] == "FAIL", r3
    print("SELF-TEST OK: 3 arms (category-shaped unassigned accounts PASS incl. a zero-value one; a model-leaf "
          "redistribution FAILs; a dropped account FAILs)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--date", help="business date to read (default: the index's latest_date); E-M2 pins 2026-10-05")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.out:
        ap.error("--out is required")
    import boto3
    from botocore.config import Config
    s3 = boto3.client("s3", region_name="us-east-1", config=Config(read_timeout=300, retries={"max_attempts": 8, "mode": "adaptive"}))
    if a.date:   # pin the same publication the laptop E-M2 read graded: re-point the index's latest_date
        orig = s3.get_object

        def pinned(**kw):
            r = orig(**kw)
            if kw.get("Key", "").endswith("/platinum/holdings/current/manifest.json"):
                doc = json.loads(r["Body"].read())
                if a.date not in doc["dates"]:
                    raise SystemExit("ERROR: %s not in the index for %s" % (a.date, kw["Key"]))
                doc["latest_date"] = a.date
                import io
                r["Body"] = io.BytesIO(json.dumps(doc).encode())
            return r
        s3.get_object = pinned
    pubs = {f: read_firm(s3, f, b) for f, b in FIRMS.items()}
    res = evaluate(pubs)
    res["reader_identity"] = boto3.client("sts").get_caller_identity()["Arn"]
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, default=str)
    for f, r in res["firms"].items():
        print("%s %s: %s (business_date %s): %d of %d unassigned accounts pass (present %d, zero-value %d, tie %d, "
              "no model node %d)" % (f, r["verdict"], f, res["publications"][f]["business_date"], r["pass"], r["listed"],
                                     r["present"], r["zero_value"], r["tie"], r["no_model_node"]))
    e = res["e2_unassigned"]
    print("e2_unassigned %s: %d of %d" % (e["verdict"], e["accounts_passing"], e["accounts_listed"]))
    return 0 if e["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
