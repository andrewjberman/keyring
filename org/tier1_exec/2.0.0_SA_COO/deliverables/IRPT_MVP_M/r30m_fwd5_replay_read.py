#!/usr/bin/env python3
"""r30m_fwd5_replay_read.py -- cell IB-mr-301 (E-M1, IRPT_BCKEND round 30 ~M): the FWD-5 replay on the served publication.

Run on a principal permitted on the three firm buckets (row IRPT_BCKEND-S352: the dell2 identity is refused). Read-only:
S3 get-object only; nothing is written to AWS. Writes ONE result file, the FILE the laptop seat delivers to
2.0.0_SA_COO~M2 (1.0.0_SA_CTO~DELL2 ruling msg 191):

    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r30m_fwd5_replay_read.py --out <path>.json
    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r30m_fwd5_replay_read.py --self-test

Criteria (decomposition IRPT_BCKEND_DECOMP_R30_M.md, cell IB-mr-301):
  c1  Inflection account acc_015d15b45d7a8ac71f951a67 (****3282): its subtree ties (every parent/basis partition sums to
      its parent within RECON_TOLERANCE_USD, TARGET excluded -- the producer's rule, holdings_snapshot.py:2746).
  c2  One Cottonwood account holding both SPYI and PSLV: its subtree ties the same way.
  c3  Per firm: unique underlying holdings reconcile before and after the overlay -- the whole node set's partitions
      balance, the ACCOUNT nodes sum to custody_totals.total_market_value, and the served reconcile block (where the
      manifest carries one) reads reconciled; denominators printed.
Each publication is the firm's newest: irpt/<firm>/platinum/holdings/current/manifest.json -> dated manifest -> its gold
parquet, sha256 checked against the manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import sys

RECON_TOLERANCE_USD = 0.01   # holdings_snapshot.py:133
FIRMS = {"49financial": "opal-data-49financial", "inflection": "opal-data-inflection", "cottonwood": "opal-data-cottonwood"}
INF_ACCOUNT = "acc_015d15b45d7a8ac71f951a67"
COT_SYMBOLS = ("SPYI", "PSLV")


def val(n):
    v = (n.get("amount") or {}).get("value")
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) else None


def partitions(nodes, root_id=None):
    """(parent, basis) -> summed child value, TARGET excluded; plus the list of structural faults.
    `root_id` names a subtree's root, whose own parent lies outside the subtree by construction."""
    by_id, faults, parts = {n["node_id"]: n for n in nodes}, [], {}
    if len(by_id) != len(nodes):
        faults.append("duplicate node_id")
    for n in nodes:
        v = val(n)
        if v is None:
            faults.append("non-finite value at %s" % n["node_id"])
            continue
        p = n.get("parent_node_id")
        if p is None or n["node_id"] == root_id:
            continue
        if p not in by_id:
            faults.append("orphan %s" % n["node_id"])
            continue
        if n.get("basis") != "TARGET":
            parts[(p, n.get("basis"))] = parts.get((p, n.get("basis")), 0.0) + v
    bad = [(p, b, round(s, 2), val(by_id[p])) for (p, b), s in parts.items()
           if val(by_id[p]) is None or abs(s - val(by_id[p])) > RECON_TOLERANCE_USD]
    return len(parts), bad, faults


def subtree(nodes, root_id):
    kids = {}
    for n in nodes:
        kids.setdefault(n.get("parent_node_id"), []).append(n)
    out, stack = [], [root_id]
    by_id = {n["node_id"]: n for n in nodes}
    while stack:
        i = stack.pop()
        if i in by_id:
            out.append(by_id[i])
        stack.extend(k["node_id"] for k in kids.get(i, []))
    return out


def find_account(nodes, ref):
    for n in nodes:
        if n.get("node_kind") == "ACCOUNT" and (n["node_id"] == ref or any(
                d.get("ref_id") == ref for d in n.get("drill_refs") or [])):
            return n
    return None


def account_tie(nodes, acc):
    sub = subtree(nodes, acc["node_id"])
    count, bad, faults = partitions(sub, acc["node_id"])
    secs = [n for n in sub if n.get("node_kind") == "SECURITY" and n.get("basis") != "TARGET"]
    return {"account_node_id": acc["node_id"], "account_value": val(acc), "subtree_nodes": len(sub),
            "securities": len(secs), "partitions": count, "partitions_unbalanced": bad, "faults": faults,
            "ties": count > 0 and not bad and not faults}


def ancestor_account(nodes, node):
    by_id = {n["node_id"]: n for n in nodes}
    while node is not None and node.get("node_kind") != "ACCOUNT":
        node = by_id.get(node.get("parent_node_id"))
    return node


def firm_reconcile(nodes, manifest):
    count, bad, faults = partitions(nodes)
    accounts = [n for n in nodes if n.get("node_kind") == "ACCOUNT"]
    after = round(sum(val(n) or 0.0 for n in accounts), 2)
    ct = ((manifest.get("custody_totals") or {}).get("total_market_value") or {}).get("value")
    served = ((manifest.get("attribution_holdouts") or {}).get("reconcile")) or manifest.get("reconcile")
    ok = count > 0 and not bad and not faults and (ct is None or abs(after - ct) <= RECON_TOLERANCE_USD) and (
        served is None or served.get("reconciled") is True)
    return {"nodes": len(nodes), "accounts": len(accounts),
            "securities": sum(1 for n in nodes if n.get("node_kind") == "SECURITY"),
            "partitions": count, "partitions_unbalanced": bad[:20], "partitions_unbalanced_count": len(bad),
            "faults": faults[:20], "account_sum": after, "custody_total_served": ct,
            "served_reconcile_block": served, "reconciled": ok}


def read_firm(s3, firm, bucket):
    def get_json(key, ver=None):
        kw = {"Bucket": bucket, "Key": key, **({"VersionId": ver} if ver else {})}
        return json.loads(s3.get_object(**kw)["Body"].read())
    import pyarrow.parquet as pq
    cur = get_json("irpt/%s/platinum/holdings/current/manifest.json" % firm)
    date = cur["latest_date"]
    m = cur["dates"][date]["manifest"]
    man = get_json(m["key"], m.get("version_id"))
    g = man["gold"]
    data = s3.get_object(Bucket=g["bucket"], Key=g["key"], VersionId=g["version_id"])["Body"].read()
    sha = hashlib.sha256(data).hexdigest()
    assert sha == g["sha256"], "gold parquet sha256 differs from the manifest"
    nodes = [json.loads(s) for s in pq.read_table(io.BytesIO(data), columns=["node_json"]).column("node_json").to_pylist()]
    pub = {"business_date": date, "revision": man.get("revision"), "manifest_key": m["key"],
           "manifest_version": m.get("version_id"), "gold_key": g["key"], "gold_version": g["version_id"], "gold_sha256": sha}
    return pub, man, nodes


def evaluate(pubs):
    """pubs: firm -> (publication record, manifest, nodes). Returns the result document."""
    res = {"cell": "IB-mr-301", "criteria": {}, "publications": {f: p for f, (p, _, _) in pubs.items()}}
    _, _, inf = pubs["inflection"]
    acc = find_account(inf, INF_ACCOUNT)
    c1 = account_tie(inf, acc) if acc else {"ties": False, "reason": "account %s not served" % INF_ACCOUNT}
    res["criteria"]["c1"] = {"verdict": "PASS" if c1["ties"] else "FAIL", **c1}
    _, _, cot = pubs["cottonwood"]
    holders = {}
    for n in cot:
        sym = ((n.get("display") or {}).get("symbol") or "").upper()
        if n.get("node_kind") == "SECURITY" and sym in COT_SYMBOLS:
            a = ancestor_account(cot, n)
            if a:
                holders.setdefault(a["node_id"], set()).add(sym)
    both = sorted(a for a, s in holders.items() if s == set(COT_SYMBOLS))
    if both:
        c2 = account_tie(cot, next(n for n in cot if n["node_id"] == both[0]))
        c2["accounts_holding_both"] = len(both)
    else:
        c2 = {"ties": False, "reason": "no Cottonwood account holds both %s" % "/".join(COT_SYMBOLS),
              "accounts_holding_either": len(holders)}
    res["criteria"]["c2"] = {"verdict": "PASS" if c2["ties"] else "FAIL", **c2}
    c3 = {f: firm_reconcile(nodes, man) for f, (_, man, nodes) in pubs.items()}
    res["criteria"]["c3"] = {"verdict": "PASS" if all(r["reconciled"] for r in c3.values()) else "FAIL",
                             "firms_denominator": len(c3), "firms": c3}
    return res


def self_test():
    def node(i, p, kind, v, basis="OBSERVED", sym=None, refs=None):
        return {"node_id": i, "parent_node_id": p, "node_kind": kind, "basis": basis, "amount": {"value": v},
                "display": {"symbol": sym}, "drill_refs": refs or []}
    good = [node("acc_015d15b45d7a8ac71f951a67", None, "ACCOUNT", 100.0), node("s1", "acc_015d15b45d7a8ac71f951a67", "SECURITY", 60.0),
            node("s2", "acc_015d15b45d7a8ac71f951a67", "SECURITY", 40.0),
            node("t1", "acc_015d15b45d7a8ac71f951a67", "SECURITY", 999.0, basis="TARGET")]
    cot = [node("a2", None, "ACCOUNT", 50.0), node("x1", "a2", "SECURITY", 20.0, sym="SPYI"), node("x2", "a2", "SECURITY", 30.0, sym="PSLV")]
    man = {"custody_totals": {"total_market_value": {"value": 100.0}}}
    pubs = {"inflection": ({}, man, good), "cottonwood": ({}, {"custody_totals": {"total_market_value": {"value": 50.0}}}, cot),
            "49financial": ({}, man, good)}
    r = evaluate(pubs)
    assert [r["criteria"][c]["verdict"] for c in ("c1", "c2", "c3")] == ["PASS"] * 3, r
    # negative arm: a value redistributed out of a security breaks the tie even though the account total is unchanged
    bad = [dict(n, amount={"value": 70.0}) if n["node_id"] == "s1" else n for n in good]
    r2 = evaluate({**pubs, "inflection": ({}, man, bad)})
    assert r2["criteria"]["c1"]["verdict"] == "FAIL" and r2["criteria"]["c3"]["verdict"] == "FAIL", r2
    print("SELF-TEST OK: 2 arms (green 3 of 3 PASS; redistributed security FAILs c1 and c3)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.out:
        ap.error("--out is required")
    import boto3
    from botocore.config import Config
    s3 = boto3.client("s3", region_name="us-east-1", config=Config(read_timeout=300, retries={"max_attempts": 8, "mode": "adaptive"}))
    pubs = {}
    for firm, bucket in FIRMS.items():
        pubs[firm] = read_firm(s3, firm, bucket)
        print("PUBLICATION %s: %s revision %s nodes %d" % (firm, pubs[firm][0]["business_date"],
                                                           str(pubs[firm][0]["revision"])[:12], len(pubs[firm][2])), flush=True)
    res = evaluate(pubs)
    res["reader_identity"] = boto3.client("sts").get_caller_identity()["Arn"]
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1, default=str)
    for c in ("c1", "c2", "c3"):
        print("%s %s" % (c, res["criteria"][c]["verdict"]))
    return 0 if all(res["criteria"][c]["verdict"] == "PASS" for c in ("c1", "c2", "c3")) else 1


if __name__ == "__main__":
    sys.exit(main())
