"""MDPF_STRATID round 1, ST-t-3 criterion AC2: the seam probe against the REAL neighbours (read-only S3).

Inputs, read live: the served Global aggregate timeseries and category view (portal/gold/mdpf/global/..., latest dated
key) and the Cottonwood slice the fold consumes (gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json).
Runs `mdpf_gold_consolidator.apply_sma_sleeve_overlay` and `_shape_category_views` in-process; writes nothing.

  CONTROL  the served Global category view reshaped from the served timeseries, no fold: Client and SMA equal served.
  ARM A    the slice as served (no `overlap_model_value` measured yet): Global's total does not move, and PFDE at
           Cottonwood is named in `sma_additive_withheld` with reason OVERLAP_UNMEASURED.
  ARM B    the slice with `overlap_model_value` = 0.0 on every date for pfde: Global's total rises by exactly
           Cottonwood's PFDE value on Global's last date (date-joined), by_model['pfde'] carries it as additive, the
           Global tree shows it under SMA > ETF Strategies, and Client does not move (FWD-1's acceptance, simulated).

SEAM-OK when all three hold; else SEAM-BAD with the arm named.
"""
from __future__ import annotations

import copy
import json
import os
import sys

BUCKET = "opal-data-assets"
GOLD = os.path.join("data", "mdpf", "scripts", "gold")
COT_KEY = "gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json"


def _bad(msg: str) -> int:
    print("SEAM-BAD " + msg)
    return 1


def _latest(s3, prefix: str) -> str:
    keys = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=prefix):
        keys += [o["Key"] for o in page.get("Contents", []) if o["Key"].endswith(".json")]
    if not keys:
        raise SystemExit("SEAM-BAD no key under " + prefix)
    return sorted(keys)[-1]


def _get(s3, key: str) -> dict:
    return json.loads(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read())


def main() -> int:
    sys.path.insert(0, os.path.abspath(GOLD))
    import boto3
    import mdpf_gold_consolidator as gc

    if not hasattr(gc, "apply_sma_sleeve_overlay"):
        return _bad("arm=build no apply_sma_sleeve_overlay in mdpf_gold_consolidator")
    s3 = boto3.client("s3")
    gkey = _latest(s3, "portal/gold/mdpf/global/aggregate-aua-timeseries/")
    ckey = gkey.replace("aggregate-aua-timeseries", "category-views")
    g, served_cv, cot = _get(s3, gkey), _get(s3, ckey), _get(s3, COT_KEY)
    print("inputs: %s | %s | %s (cot last %s)" % (gkey, ckey, COT_KEY, cot["dates"][-1]))

    cv0 = gc._shape_category_views(copy.deepcopy(g), "global")
    sn = served_cv["nodes"]
    if abs(cv0["nodes"]["Client"]["aum"] - sn["Client"]["aum"]) > 0.02 or abs(cv0["nodes"]["SMA"]["aum"] - sn["SMA"]["aum"]) > 0.02:
        return _bad("arm=control reshape != served (Client/SMA)")

    gd = g["dates"][-1]
    if gd not in cot["dates"]:
        return _bad("arm=input Global last date %s not on the Cottonwood axis (carry case; re-run on a covered day)" % gd)
    ci = cot["dates"].index(gd)
    pfde = (cot["by_model"].get("pfde") or {}).get("model_value", [None] * (ci + 1))[ci]
    if pfde is None:
        return _bad("arm=input Cottonwood PFDE has no value on %s" % gd)
    total0 = g["opal_aggregate_aua"][-1]

    # ARM A -- as served
    outa = gc.apply_sma_sleeve_overlay({"global": copy.deepcopy(g), "cottonwood": copy.deepcopy(cot)})["global"]
    wa = [w for w in (outa.get("sma_additive_withheld") or []) if w.get("member_id") == "pfde"
          and w.get("firm_id") == "cottonwood" and w.get("reason") == "OVERLAP_UNMEASURED"]
    if abs(outa["opal_aggregate_aua"][-1] - total0) > 0.005 or not wa:
        return _bad("arm=A total moved or PFDE not withheld as OVERLAP_UNMEASURED")

    # ARM B -- overlap measured at zero
    cotb = copy.deepcopy(cot)
    cotb["by_model"]["pfde"]["overlap_model_value"] = [0.0] * len(cotb["dates"])
    outb = gc.apply_sma_sleeve_overlay({"global": copy.deepcopy(g), "cottonwood": cotb})["global"]
    delta = round(outb["opal_aggregate_aua"][-1] - total0, 2)
    bm = outb.get("by_model", {}).get("pfde") or {}
    if abs(delta - pfde) > 0.005:
        return _bad("arm=B total delta %.2f != Cottonwood PFDE %.2f" % (delta, pfde))
    if bm.get("source_basis") != "additive" or abs((bm.get("model_value") or [0])[-1] - pfde) > 0.005:
        return _bad("arm=B by_model['pfde'] not additive with the PFDE value")
    cvb = gc._shape_category_views(outb, "global")["nodes"]
    etf = {m["member_id"]: m["aum"] for m in cvb["SMA"]["children"]["ETF Strategies"]["members"]}
    if etf.get("pfde") is None or abs(etf["pfde"] - pfde) > 0.005:
        return _bad("arm=B tree ETF Strategies > PFDE = %r, want %.2f" % (etf.get("pfde"), pfde))
    if abs(cvb["Client"]["aum"] - sn["Client"]["aum"]) > 0.02:
        return _bad("arm=B Client moved")
    print("CONTROL ok | A total %.2f unchanged, PFDE withheld | B PFDE %.2f on %s, total +%.2f, Client unchanged"
          % (total0, pfde, gd, delta))
    print("SEAM-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
