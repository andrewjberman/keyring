"""MDPF_STRATID FWD-3 mechanism arm (unblock UB-20261009T183753Z-5e37, the CRO's approach): a planted Muni SMA sleeve on the REAL served
bytes routes to ALT Strategies at Global, with exact add / hold-out arithmetic. Read-only S3; writes nothing.

  CONTROL  the served Cottonwood slice folded into the PRE-FOLD Global doc: ALT Strategies has no `muni` dollars (aum None or 0).
  ARM ADD  plant Cottonwood by_model["muni"] = {cohort_class sma, model_value V on every date, overlap 0.0}: Global's total rises by
           exactly V on the last date, the tree's ALT Strategies > muni row equals V, Client does not move, nothing raises.
  ARM HOLD the same sleeve with overlap = V (its dollars already inside a Model, the Opal_Muni_Sleeve case): Global's total does not
           move, and muni is named held out (sma_additive_withheld reason OVERLAP, value V; tree row held_out names it).
  COTTONWOOD the served per-firm Cottonwood artifact, planted the same way, shaped at the Cottonwood scope shows muni under ALT Strategies at V.
R2-MUNI-SEAM-OK when all hold; else R2-MUNI-SEAM-BAD with the arm named. V = 550823.07 (the Opal_Muni_Sleeve figure; synthetic here).
"""
from __future__ import annotations

import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _r2_seam as r2  # noqa: E402

V = 550823.07


def _bad(msg):
    print("R2-MUNI-SEAM-BAD " + msg)
    return 1


def _alt(nodes, mid="muni"):
    for m in nodes["SMA"]["children"].get("ALT Strategies", {}).get("members", []):
        if m["member_id"] == mid:
            return m
    return None


def _plant(cot, overlap):
    c = copy.deepcopy(cot)
    n = len(c["dates"])
    c["by_model"]["muni"] = {"cohort_class": "sma", "model_value": [V] * n, "account_count": [1] * n,
                             "overlap_model_value": [overlap] * n, "display_name": "Muni SMA"}
    return c


def main():
    g, cot = r2.load()
    import mdpf_gold_consolidator as gc

    pre = r2.pre_fold(g)
    i = len(g["dates"]) - 1
    base = gc.apply_sma_sleeve_overlay({"global": copy.deepcopy(pre), "cottonwood": copy.deepcopy(cot)})["global"]
    n0 = gc._shape_category_views(copy.deepcopy(base), "global")["nodes"]
    c0 = _alt(n0)
    if c0 is not None and (c0.get("aum") or 0) != 0:
        return _bad("arm=control ALT > muni already carries %r" % c0.get("aum"))
    t0 = base["opal_aggregate_aua"][i]

    try:
        add = gc.apply_sma_sleeve_overlay({"global": copy.deepcopy(pre), "cottonwood": _plant(cot, 0.0)})["global"]
        na = gc._shape_category_views(copy.deepcopy(add), "global")["nodes"]
    except SystemExit as e:
        return _bad("arm=add raises: %s" % str(e)[:200])
    ma = _alt(na)
    d = round(add["opal_aggregate_aua"][i] - t0, 2)
    if ma is None or abs((ma.get("aum") or 0) - V) > 0.01 or abs(d - V) > 0.01:
        return _bad("arm=add ALT>muni %r, total delta %.2f, want %.2f both" % (ma and ma.get("aum"), d, V))
    if abs(na["Client"]["aum"] - n0["Client"]["aum"]) > 0.02:
        return _bad("arm=add Client moved")

    try:
        hold = gc.apply_sma_sleeve_overlay({"global": copy.deepcopy(pre), "cottonwood": _plant(cot, V)})["global"]
        nh = gc._shape_category_views(copy.deepcopy(hold), "global")["nodes"]
    except SystemExit as e:
        return _bad("arm=hold raises: %s" % str(e)[:200])
    day = g["dates"][-1]
    w = [x for x in hold.get("sma_additive_withheld") or [] if x.get("member_id") == "muni" and x.get("date") == day]
    mh = _alt(nh)
    ho = (mh or {}).get("held_out") or []
    if abs(hold["opal_aggregate_aua"][i] - t0) > 0.01 or not w or w[0].get("reason") != "OVERLAP" or abs(w[0]["value"] - V) > 0.01:
        return _bad("arm=hold total moved or muni not withheld OVERLAP %.2f: %r" % (V, w))
    if not any(h.get("firm_id") == "cottonwood" and abs(h.get("value", 0) - V) < 0.01 for h in ho):
        return _bad("arm=hold ALT>muni row does not name the held-out amount: %r" % ho)

    import json
    import boto3
    s3 = boto3.client("s3")
    keys = []
    for p in s3.get_paginator("list_objects_v2").paginate(Bucket=r2.BUCKET, Prefix="portal/gold/mdpf/cottonwood/aggregate-aua-timeseries/"):
        keys += [o["Key"] for o in p.get("Contents", []) if o["Key"].endswith(".json")]
    pf = json.loads(s3.get_object(Bucket=r2.BUCKET, Key=sorted(keys)[-1])["Body"].read())
    print("per-firm input: %s" % sorted(keys)[-1])
    try:
        nc = gc._shape_category_views(_plant(pf, 0.0), "cottonwood")["nodes"]
    except SystemExit as e:
        return _bad("arm=cottonwood raises: %s" % str(e)[:200])
    mc = _alt(nc)
    if mc is None or abs((mc.get("aum") or 0) - V) > 0.01:
        return _bad("arm=cottonwood ALT>muni %r, want %.2f" % (mc and mc.get("aum"), V))

    print("CONTROL no muni dollars | ADD ALT>muni %.2f, total +%.2f, Client unchanged | HOLD total unchanged, withheld OVERLAP %.2f, "
          "row held_out %r | COTTONWOOD ALT>muni %.2f" % (ma["aum"], d, w[0]["value"], ho, mc["aum"]))
    print("R2-MUNI-SEAM-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
