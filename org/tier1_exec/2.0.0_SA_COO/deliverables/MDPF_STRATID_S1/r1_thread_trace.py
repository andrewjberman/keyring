"""MDPF_STRATID round 1 -- the drain's THREAD TRACE (pre-deploy, in-process, read-only S3; writes only its own JSON).

Hops 1-4 joined on the merged code: the served Cottonwood slice (hop 1), `measure_sma_overlap` on real Rebalancer silver for
the slice's last date (hop 1b), `sma_global_basis_of` (hop 2), `apply_sma_sleeve_overlay` over the served Global timeseries
(hop 3), `_shape_category_views` (hop 4). Prints the FWD-1 acceptance figures and THREAD-OK / THREAD-BAD.

  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/r1_thread_trace.py <out.json>
"""
from __future__ import annotations

import copy
import json
import os
import sys

for p in ("data/assets/scripts/gold", "data/assets/scripts/silver", "data/mdpf/scripts/gold"):
    sys.path.insert(0, os.path.abspath(p))

import boto3  # noqa: E402
import build_cottonwood_mdpf_slice as sl  # noqa: E402
import mdpf_category_registry as reg  # noqa: E402
import mdpf_gold_consolidator as gc  # noqa: E402

B = "opal-data-assets"


def _get(s3, key):
    return json.loads(s3.get_object(Bucket=B, Key=key)["Body"].read())


def main(out_path: str) -> int:
    s3 = boto3.client("s3")
    keys = sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(
        Bucket=B, Prefix="portal/gold/mdpf/global/aggregate-aua-timeseries/") for o in pg.get("Contents", []))
    gkey = keys[-1]
    g = _get(s3, gkey)
    served_cv = _get(s3, gkey.replace("aggregate-aua-timeseries", "category-views"))
    cot = _get(s3, "gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json")
    d = g["dates"][-1]
    ci = cot["dates"].index(d)
    ov = sl.measure_sma_overlap(s3, d)
    basis = reg.sma_global_basis_of("pfde", "cottonwood")
    for m, e in cot["by_model"].items():
        if e.get("cohort_class") == "sma":
            vals = [None] * len(cot["dates"])
            if ov is not None and m in ov:
                vals[ci] = float(ov[m]["overlap_dollars"])
            e["overlap_model_value"] = vals
    out = gc.apply_sma_sleeve_overlay({"global": copy.deepcopy(g), "cottonwood": cot})["global"]
    cv = gc._shape_category_views(out, "global")["nodes"]
    pfde_cot = cot["by_model"]["pfde"]["model_value"][ci]
    pfde_glob = {m["member_id"]: m["aum"] for m in cv["SMA"]["children"]["ETF Strategies"]["members"]}.get("pfde")
    delta = round(out["opal_aggregate_aua"][-1] - g["opal_aggregate_aua"][-1], 2)
    rec = {"global_key": gkey, "date": d, "overlap_measured": ov, "basis_pfde_cottonwood": basis,
           "pfde_cottonwood": pfde_cot, "pfde_global_tree": pfde_glob, "global_total_before": g["opal_aggregate_aua"][-1],
           "global_total_after": out["opal_aggregate_aua"][-1], "delta": delta,
           "client_served": served_cv["nodes"]["Client"]["aum"], "client_after": cv["Client"]["aum"],
           "withheld_on_date": [w for w in out.get("sma_additive_withheld") or [] if w.get("date") == d]}
    ok = (basis == "additive" and pfde_glob is not None and abs(pfde_glob - pfde_cot) < 0.005
          and abs(delta - pfde_cot) < 0.005 and abs(rec["client_after"] - rec["client_served"]) < 0.02)
    rec["verdict"] = "THREAD-OK" if ok else "THREAD-BAD"
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(rec, f, indent=2, default=str)
    print(json.dumps({k: rec[k] for k in ("date", "pfde_cottonwood", "pfde_global_tree", "delta", "client_after",
                                          "verdict")}, default=str))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
