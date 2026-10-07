#!/usr/bin/env python3
"""r31m_fwd5_proof_cases_read.py -- cell IB-mr-311 (E-M2, IRPT_BCKEND round 31 ~M): FWD-5's four PROOF cases on the
served publication (CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_30_M_20261007.md @e252251fbe).

Run on a principal permitted on the three firm buckets (the dell2 identity is refused until the NFRA_CTLPLN fence join).
Read-only: S3 get-object only. Writes ONE result file, the FILE delivered to 2.0.0_SA_COO~M2:

    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r31m_fwd5_proof_cases_read.py --out <path>.json
    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r31m_fwd5_proof_cases_read.py --self-test

The four cases, each defined on what the served publication carries (the producer's private _manifest is not served):
  unassigned       an ACCOUNT node listed in the header's attribution_holdouts.unassigned.account_ids
  unmatched_join   a firm whose header coverage reads nodes_resolved < nodes_attempted, or whose
                   attribution_holdouts.assigned_without_custody.account_count > 0
  blended_model    an ACCOUNT whose subtree holds a MODEL_WRAPPER node, or a node whose classification capability_facts
                   name a blend weight ("blend_weight=")
  multi_membership an ACCOUNT whose subtree references more than one distinct MODEL (drill_refs ref_kind MODEL)
Criteria (the analysis's E-M2):
  e1  each case: one real instance found at any firm and named, or its absence at all three stated with the denominator
  e2  each found instance reconciles: the account's subtree ties (TARGET excluded); for unassigned, the account carries its
      full value with no non-TARGET child (the residual is VISIBLE, not redistributed); for unmatched_join, the firm's
      before/after reconcile holds and the remainder is stated
  e3  per firm: coverage (resolved / attempted, remainder) and the join-exception counts printed with denominators
Also printed per firm, as evidence for any case read ABSENT: the node-kind census and the capability-fact vocabulary.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r30m_fwd5_replay_read import FIRMS, account_tie, firm_reconcile, read_firm  # noqa: E402

CASES = ("unassigned", "unmatched_join", "blended_model", "multi_membership")
BLEND = re.compile(r"blend_weight=")


def facts(n):
    return ((n.get("classification") or {}).get("capability_facts")) or []


def children_index(nodes):
    kids = {}
    for n in nodes:
        kids.setdefault(n.get("parent_node_id"), []).append(n)
    return kids


def subtree_ids(kids, root):
    out, stack = [], [root]
    while stack:
        i = stack.pop()
        out.append(i)
        stack.extend(k["node_id"] for k in kids.get(i, []))
    return out


def firm_cases(nodes, header):
    by_id = {n["node_id"]: n for n in nodes}
    kids = children_index(nodes)
    accounts = [n for n in nodes if n.get("node_kind") == "ACCOUNT"]
    hold = (header.get("attribution_holdouts") or {})
    un_ids = set((hold.get("unassigned") or {}).get("account_ids") or [])
    cov = header.get("coverage") or {}
    awc = hold.get("assigned_without_custody") or {}
    found = {c: [] for c in CASES}
    for acc in accounts:
        sub = [by_id[i] for i in subtree_ids(kids, acc["node_id"]) if i in by_id]
        if acc["node_id"] in un_ids:
            found["unassigned"].append(acc["node_id"])
        if any(n.get("node_kind") == "MODEL_WRAPPER" or any(BLEND.search(f) for f in facts(n)) for n in sub):
            found["blended_model"].append(acc["node_id"])
        models = {d.get("ref_id") for n in sub for d in (n.get("drill_refs") or []) if d.get("ref_kind") == "MODEL"}
        if len(models) > 1:
            found["multi_membership"].append(acc["node_id"])
    attempted, resolved = cov.get("nodes_attempted"), cov.get("nodes_resolved")
    unmatched = (attempted - resolved) if isinstance(attempted, int) and isinstance(resolved, int) else None
    if (unmatched or 0) > 0 or (awc.get("account_count") or 0) > 0:
        found["unmatched_join"].append("firm")
    census = {
        "accounts": len(accounts),
        "node_kinds": dict(Counter(n.get("node_kind") for n in nodes)),
        "fact_vocabulary": dict(Counter(re.sub(r"[=:].*", "", f)[:60] for n in nodes for f in facts(n)).most_common(25)),
        "coverage": {"nodes_resolved": resolved, "nodes_attempted": attempted, "unmatched": unmatched,
                     "remainder": cov.get("remainder")},
        "assigned_without_custody": {k: awc.get(k) for k in ("account_count", "denominator")},
        "unassigned_block": {k: (hold.get("unassigned") or {}).get(k) for k in ("account_count", "value")},
        "unassigned_ids_listed": len(un_ids),
        "unassigned_ids_present_as_accounts": len(un_ids & {a["node_id"] for a in accounts}),
    }
    return found, census, by_id


def instance_check(case, nodes, by_id, ref, header):
    if case == "unmatched_join":
        r = firm_reconcile(nodes, header)
        return {"reconciles": r["reconciled"], "arms": r["arms"], "remainder": (header.get("coverage") or {}).get("remainder")}
    acc = by_id[ref]
    t = account_tie(nodes, acc)
    out = {"account_node_id": ref, "account_value": acc.get("amount", {}).get("value"), "ties": t["ties"],
           "partitions": t["partitions"], "partitions_unbalanced": t["partitions_unbalanced"][:5]}
    if case == "unassigned":
        live_kids = [n for n in nodes if n.get("parent_node_id") == ref and n.get("basis") != "TARGET"]
        out["non_target_children"] = len(live_kids)
        # visible and not redistributed: the account stands at its own value with nothing allocated beneath it
        out["ties"] = not live_kids or t["ties"]
        out["residual_visible"] = acc.get("node_kind") == "ACCOUNT" and not live_kids
    return out


def evaluate(pubs):
    res = {"cell": "IB-mr-311", "publications": {f: p for f, (p, _, _) in pubs.items()}, "firms": {}, "cases": {}}
    per_firm = {}
    for f, (_, header, nodes) in pubs.items():
        found, census, by_id = firm_cases(nodes, header)
        per_firm[f] = (found, by_id, header, nodes)
        res["firms"][f] = {"census": census, "found_counts": {c: len(v) for c, v in found.items()}}
    for c in CASES:
        hits = [(f, ref) for f in FIRMS for ref in per_firm[f][0][c]]
        if not hits:
            res["cases"][c] = {"found": False, "searched": {f: res["firms"][f]["census"]["accounts"] for f in FIRMS}}
            continue
        f, ref = hits[0]
        _, by_id, header, nodes = per_firm[f]
        chk = instance_check(c, nodes, by_id, ref, header)
        res["cases"][c] = {"found": True, "firm": f, "instance": ref, "instances_total": len(hits), "check": chk}
    e1 = all(res["cases"][c]["found"] or res["cases"][c].get("searched") for c in CASES)
    e2 = all(res["cases"][c]["check"].get("reconciles", res["cases"][c]["check"].get("ties")) is True
             and res["cases"][c]["check"].get("residual_visible", True) is not False
             for c in CASES if res["cases"][c]["found"])
    e3 = all(res["firms"][f]["census"]["coverage"]["nodes_attempted"] is not None
             and res["firms"][f]["census"]["assigned_without_custody"]["account_count"] is not None for f in FIRMS)
    res["criteria"] = {"e1": "PASS" if e1 else "FAIL", "e2": "PASS" if e2 else "FAIL", "e3": "PASS" if e3 else "FAIL",
                       "cases_found": [c for c in CASES if res["cases"][c]["found"]],
                       "cases_absent_at_all_three": [c for c in CASES if not res["cases"][c]["found"]]}
    return res


def self_test():
    def node(i, p, kind, v, basis="OBSERVED", refs=None, fx=None):
        return {"node_id": i, "parent_node_id": p, "node_kind": kind, "basis": basis, "amount": {"value": v},
                "drill_refs": refs or [], "classification": {"capability_facts": fx or []}, "display": {}}
    nodes = [node("u1", None, "ACCOUNT", 10.0),
             node("a1", None, "ACCOUNT", 100.0), node("w1", "a1", "MODEL_WRAPPER", 100.0, refs=[{"ref_kind": "MODEL", "ref_id": "m1"}]),
             node("l1", "w1", "MODEL_LEAF", 60.0, fx=["blend_weight=0.6"]), node("l2", "w1", "MODEL_LEAF", 40.0,
                                                                                 refs=[{"ref_kind": "MODEL", "ref_id": "m2"}])]
    header = {"attribution_holdouts": {"unassigned": {"account_ids": ["u1"], "account_count": 1},
                                       "assigned_without_custody": {"account_count": 2, "denominator": "2 of 9"},
                                       "reconcile": {"reconciled": True}},
              "coverage": {"nodes_resolved": 8, "nodes_attempted": 9, "remainder": {"amount": 0.0}},
              "custody_totals": {"total_market_value": {"value": 110.0}}}
    pubs = {f: ({}, header, nodes) for f in FIRMS}
    r = evaluate(pubs)
    assert r["criteria"]["cases_found"] == list(CASES) and all(r["criteria"][e] == "PASS" for e in ("e1", "e2", "e3")), r
    # negative arm: an unassigned account whose value was spread into a child sleeve that does not tie FAILs e2
    bad = nodes + [node("s9", "u1", "SLEEVE", 4.0)]
    r2 = evaluate({f: ({}, header, bad) for f in FIRMS})
    assert r2["criteria"]["e2"] == "FAIL", r2["cases"]["unassigned"]
    # absence arm: no holdouts and full coverage -> the case reads absent with its denominator, e1 still PASS
    h3 = json.loads(json.dumps(header))
    h3["attribution_holdouts"]["unassigned"]["account_ids"] = []
    h3["attribution_holdouts"]["assigned_without_custody"]["account_count"] = 0
    h3["coverage"]["nodes_resolved"] = 9
    r3 = evaluate({f: ({}, h3, nodes) for f in FIRMS})
    assert set(r3["criteria"]["cases_absent_at_all_three"]) == {"unassigned", "unmatched_join"} and r3["criteria"]["e1"] == "PASS", r3
    print("SELF-TEST OK: 3 arms (all four cases found and reconciled; a redistributed unassigned account FAILs e2;"
          " absent cases read with their denominators)")
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
    pubs = {f: read_firm(s3, f, b) for f, b in FIRMS.items()}
    for f, (p, _, nodes) in pubs.items():
        print("PUBLICATION %s: %s revision %s nodes %d" % (f, p["business_date"], str(p["revision"])[:12], len(nodes)), flush=True)
    res = evaluate(pubs)
    res["reader_identity"] = boto3.client("sts").get_caller_identity()["Arn"]
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, default=str)
    for c in CASES:
        print("case %s: %s" % (c, "FOUND at %s (%s)" % (res["cases"][c]["firm"], res["cases"][c]["instance"])
                                   if res["cases"][c]["found"] else "ABSENT at 3 of 3 firms"))
    for e in ("e1", "e2", "e3"):
        print("%s %s" % (e, res["criteria"][e]))
    return 0 if all(res["criteria"][e] == "PASS" for e in ("e1", "e2", "e3")) else 1


if __name__ == "__main__":
    sys.exit(main())
