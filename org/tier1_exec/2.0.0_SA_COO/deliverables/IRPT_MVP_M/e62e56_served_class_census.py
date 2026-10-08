#!/usr/bin/env python3
"""e62e56_served_class_census.py -- SC-e-62/56 release, e56 acceptance 1 on the served bytes.

Per firm, read-only: the 238 newly placed CUSIPs of E56_PRECHECK_HOLDINGS_CUSIP_NEWLY_PLACED_ON_R2_20261007.json against
the newest served Holdings gold (security_id namespace CUSIP): served class vs the CUSIP row's class, plus basis,
sub-class and producer. Writes one JSON result.

    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/e62e56_served_class_census.py <out>.json
"""
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from r30m_fwd5_replay_read import FIRMS, read_firm  # noqa: E402

PRECHECK = os.path.join(HERE, "E56_PRECHECK_HOLDINGS_CUSIP_NEWLY_PLACED_ON_R2_20261007.json")


def census(s3, firm, bucket, want):
    pub, _header, nodes = read_firm(s3, firm, bucket)
    by = defaultdict(list)
    producers = Counter()
    for n in nodes:
        if n.get("node_kind") != "SECURITY":
            continue
        producers[(n.get("provenance") or {}).get("producer")] += 1
        sid = n.get("security_id") or {}
        if sid.get("namespace") == "CUSIP" and sid.get("value") in want:
            by[sid["value"]].append(n)
    rows = []
    tally = Counter()
    for cusip, r in want.items():
        ns = by.get(cusip, [])
        if not ns:
            tally["not_held_on_served_date"] += 1
            rows.append({"cusip": cusip, "state": "absent"})
            continue
        cls = Counter(n.get("asset_class") for n in ns)
        ok = set(cls) == {r["cusip_row_asset_class"]}
        tally["match" if ok else "MISMATCH"] += 1
        rows.append({
            "cusip": cusip, "expected": r["cusip_row_asset_class"], "expected_sub": r.get("cusip_row_sub_asset_class"),
            "served": dict(cls), "basis": dict(Counter(n.get("asset_class_basis") for n in ns)),
            "sub": {str(k): v for k, v in Counter(n.get("sub_asset_class") for n in ns).items()},
            "producers": dict(Counter((n.get("provenance") or {}).get("producer") for n in ns)),
            "nodes": len(ns), "ok": ok})
    return {"pub": pub, "listed": len(want), "tally": dict(tally),
            "producers_all": {str(k): v for k, v in producers.items()}, "rows": rows}


def main():
    import boto3
    pre = json.load(open(PRECHECK, encoding="utf-8"))
    s3 = boto3.client("s3", region_name="us-east-1")
    out = {}
    for firm, bucket in FIRMS.items():
        want = {r["cusip"]: r for r in pre["firms"].get(firm, [])}
        res = census(s3, firm, bucket, want)
        out[firm] = res
        basis = Counter()
        for r in res["rows"]:
            basis.update(r.get("basis", {}))
        print(firm, res["pub"]["business_date"], res["pub"]["revision"][:12], "listed", res["listed"], res["tally"],
              "basis_of_listed:", dict(basis))
    with open(sys.argv[1], "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, default=str)
    return 0


if __name__ == "__main__":
    sys.exit(main())
