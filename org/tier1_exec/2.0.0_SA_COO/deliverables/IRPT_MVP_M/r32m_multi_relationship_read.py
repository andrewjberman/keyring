#!/usr/bin/env python3
"""r32m_multi_relationship_read.py -- cell IB-mr-321 (E-M3, IRPT_BCKEND round 32 ~M): one TRUE multi-relationship
membership, from the producer's own collapse evidence (CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_31_M_20261007.md).

The relationship grain exists in Cottonwood's custody source (BD fact_holdings "Relationship ID"); the producer collapses equal
relationship duplicates and keeps the evidence in its PRIVATE manifest (`_manifest.actual_custody_controls.original_rows`),
which is never served. So this reader runs the producer's own `build_snapshot("cottonwood", s3, <date>)` -- a pure build: no
upload, no write -- and reads that evidence. Run on a principal permitted on opal-data-cottonwood (the dell2 identity is
refused there). Writes ONE result file:

    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r32m_multi_relationship_read.py --date 2026-10-05 --out <path>.json
    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r32m_multi_relationship_read.py --self-test

Criteria (E-M3):
  m1  name one account that belongs to more than one relationship (>1 distinct Relationship ID across its custody rows), or
      state the absence with the denominator searched
  m2  that account's unique underlying holdings reconcile before and after the overlay: its positions are collapsed to unique
      AccountID/AssetID (no double count), the rebuilt ACCOUNT node's subtree ties, and its value equals the served 2026-10-05
      node's value; no residual redistributed (no partition out of balance)
  m3  the overlap between "more than one MODEL in the subtree" (the round-31 proxy) and "more than one relationship" is printed
      as a 2x2 with its denominator, so the proxy's distance from the case is measured
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from r30m_fwd5_replay_read import account_tie, read_firm  # noqa: E402

PRODUCER = "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py"


def relationships_by_account(controls):
    rel = {}
    for r in controls.get("original_rows") or []:
        rel.setdefault(str(r.get("account_id")), set()).add(str(r.get("relationship_id")))
    return rel


def model_count(nodes, root):
    kids = {}
    for n in nodes:
        kids.setdefault(n.get("parent_node_id"), []).append(n)
    models, stack = set(), [root]
    while stack:
        for k in kids.get(stack.pop(), []):
            models.update(d.get("ref_id") for d in (k.get("drill_refs") or []) if d.get("ref_kind") == "MODEL")
            stack.append(k["node_id"])
    return len(models)


def account_node_for_raw(nodes, raw):
    for n in nodes:
        if n.get("node_kind") == "ACCOUNT" and any(str(d.get("ref_id")) == raw or str(d.get("raw_id", "")) == raw
                                                   for d in (n.get("drill_refs") or [])):
            return n
    return None


def evaluate(snapshot, served_nodes, opaque):
    """snapshot: the producer's rebuilt snapshot (with _manifest); served_nodes: the served publication's nodes;
    opaque: callable raw account id -> the producer's opaque ACCOUNT node id."""
    controls = (snapshot.get("_manifest") or {}).get("actual_custody_controls") or {}
    rel = relationships_by_account(controls)
    multi = sorted(a for a, s in rel.items() if len(s) > 1)
    res = {"cell": "IB-mr-321", "relationship_evidence_present": bool(rel),
           "accounts_with_relationship_rows": len(rel), "accounts_in_more_than_one_relationship": len(multi),
           "relationship_rows_collapsed": controls.get("relationship_rows_collapsed")}
    nodes = snapshot["nodes"]
    by_id = {n["node_id"]: n for n in nodes}
    served = {n["node_id"]: n for n in served_nodes if n.get("node_kind") == "ACCOUNT"}
    if not multi:
        res["m1"] = {"verdict": "PASS" if rel else "FAIL", "found": False,
                     "absence": "0 of %d accounts with relationship rows hold more than one Relationship ID" % len(rel)}
    else:
        raw = multi[0]
        aid = opaque(raw)
        acc = by_id.get(aid)
        res["m1"] = {"verdict": "PASS" if acc else "FAIL", "found": True, "account_node_id": aid,
                     "relationships": sorted(rel[raw]), "instances_total": len(multi)}
        if acc:
            t = account_tie(nodes, acc)
            acct = next((a for a in controls.get("accounts") or [] if str(a.get("account_id")) == raw), {})
            s = served.get(aid)
            same = s is not None and abs((s.get("amount") or {}).get("value", 0.0) - acc["amount"]["value"]) <= 0.01
            res["m2"] = {"verdict": "PASS" if t["ties"] and same else "FAIL", "subtree_ties": t["ties"],
                         "partitions": t["partitions"], "partitions_unbalanced": t["partitions_unbalanced"][:5],
                         "rebuilt_value": acc["amount"]["value"],
                         "served_value": None if s is None else s["amount"]["value"], "matches_served": same,
                         "raw_rows": acct.get("raw_row_count"), "unique_positions": acct.get("unique_position_count"),
                         "duplicate_relationship_rows_collapsed": acct.get("duplicate_relationship_row_count")}
    multi_ids = {opaque(a) for a in multi}
    accts = [n["node_id"] for n in nodes if n.get("node_kind") == "ACCOUNT"]
    by_model = {a for a in accts if model_count(nodes, a) > 1}
    grid = {"multi_model_and_multi_relationship": len(by_model & multi_ids),
            "multi_model_only": len(by_model - multi_ids), "multi_relationship_only": len(multi_ids - by_model),
            "neither": len(set(accts) - by_model - multi_ids), "accounts": len(accts)}
    res["m3"] = {"verdict": "PASS" if grid["accounts"] else "FAIL", "overlap": grid}
    if "m2" not in res:
        res["m2"] = {"verdict": "PASS" if not multi and rel else "FAIL", "note": "no instance to reconcile"}
    return res


def self_test():
    def node(i, p, kind, v, refs=None):
        return {"node_id": i, "parent_node_id": p, "node_kind": kind, "basis": "OBSERVED", "amount": {"value": v},
                "drill_refs": refs or []}
    nodes = [node("acc_A", None, "ACCOUNT", 30.0), node("s1", "acc_A", "SECURITY", 10.0), node("s2", "acc_A", "SECURITY", 20.0),
             node("acc_B", None, "ACCOUNT", 5.0), node("m1", "acc_B", "MODEL_LEAF", 3.0, [{"ref_kind": "MODEL", "ref_id": "x"}]),
             node("m2", "acc_B", "MODEL_LEAF", 2.0, [{"ref_kind": "MODEL", "ref_id": "y"}])]
    controls = {"original_rows": [{"account_id": "A", "relationship_id": "r1"}, {"account_id": "A", "relationship_id": "r2"},
                                  {"account_id": "B", "relationship_id": "r3"}],
                "accounts": [{"account_id": "A", "raw_row_count": 3, "unique_position_count": 2,
                              "duplicate_relationship_row_count": 1}], "relationship_rows_collapsed": 1}
    snap = {"nodes": nodes, "_manifest": {"actual_custody_controls": controls}}
    r = evaluate(snap, nodes, lambda raw: "acc_" + raw)
    assert r["m1"]["verdict"] == r["m2"]["verdict"] == r["m3"]["verdict"] == "PASS", r
    assert r["m3"]["overlap"]["multi_relationship_only"] == 1 and r["m3"]["overlap"]["multi_model_only"] == 1, r
    # negative arm: the served value differs from the rebuild (a double-counted relationship row) -> m2 FAILs
    served = [dict(n, amount={"value": 40.0}) if n["node_id"] == "acc_A" else n for n in nodes]
    assert evaluate(snap, served, lambda raw: "acc_" + raw)["m2"]["verdict"] == "FAIL"
    # absence arm: no account in two relationships -> m1 PASS as a stated absence with its denominator
    one = {"nodes": nodes, "_manifest": {"actual_custody_controls": {"original_rows": controls["original_rows"][1:]}}}
    r3 = evaluate(one, nodes, lambda raw: "acc_" + raw)
    assert r3["m1"]["found"] is False and r3["m1"]["verdict"] == "PASS" and "0 of 2" in r3["m1"]["absence"], r3
    print("SELF-TEST OK: 3 arms (an account in two relationships named, tied, and the 2x2 overlap printed; a served "
          "value that double-counts FAILs m2; no multi-relationship account reads as a stated absence)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--date", default="2026-10-05")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.out:
        ap.error("--out is required")
    root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
    sys.path.insert(0, os.path.join(root, os.path.dirname(PRODUCER)))
    import boto3
    import holdings_snapshot as hs
    producer_sha = hashlib.sha256(open(os.path.join(root, PRODUCER), "rb").read()).hexdigest()
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    s3 = boto3.client("s3", region_name="us-east-1")
    snapshot = hs.build_snapshot("cottonwood", s3, a.date)        # pure build: no publish, no write
    pub, _header, served_nodes = read_firm(s3, "cottonwood", "opal-data-cottonwood")
    res = evaluate(snapshot, served_nodes, lambda raw: hs.opaque_id("account", "cottonwood", str(raw)))
    res.update({"producer": PRODUCER, "producer_sha256": producer_sha, "repo_head": head, "build_date": a.date,
                "served_publication": pub, "reader_identity": boto3.client("sts").get_caller_identity()["Arn"]})
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, default=str)
    print("producer %s sha256 %s at %s; build %s; served %s rev %s" % (PRODUCER, producer_sha[:12], head, a.date,
                                                                      pub["business_date"], str(pub["revision"])[:12]))
    for m in ("m1", "m2", "m3"):
        print("%s %s %s" % (m, res[m]["verdict"], json.dumps({k: v for k, v in res[m].items() if k != "verdict"}, default=str)[:300]))
    return 0 if all(res[m]["verdict"] == "PASS" for m in ("m1", "m2", "m3")) else 1


if __name__ == "__main__":
    sys.exit(main())
