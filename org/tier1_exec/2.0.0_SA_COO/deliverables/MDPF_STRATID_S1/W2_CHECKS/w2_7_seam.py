"""MDPF_STRATID workstream 2, ST-w-7 criterion AC2: the seam on REAL data (read-only S3; writes nothing).

  BUILD    build_cottonwood_mdpf_slice has unidentified_block(gold_by_date) and build_composed sets composed["unidentified_strategies"].
  ARM A    build_composed(s3) in memory: the block carries as_of (= the latest Cottonwood gold value date), firm_id "cottonwood",
           names_scanned > 0, config_source naming the S3 list, and rows each {firm_id, name, dollars, reason}; the composed figures
           (by_model keys, model_aua on the last date) equal the served slice's (the list moves no figure).
  ARM B    planted, on purpose: the latest real gold frame plus one row "Opal Frontier Sleeve" (dollar_value 1234.56, account_count 1)
           through unidentified_block: that name is listed with firm cottonwood, dollars 1234.56, reason NO_MEMBER; the same frame
           without the row does not list it.
W27-SEAM-OK when all hold; else W27-SEAM-BAD with the arm named.
"""
from __future__ import annotations

import copy
import json
import os
import sys

B = "opal-data-assets"
SLICE = "gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json"


def _bad(msg):
    print("W27-SEAM-BAD " + msg)
    return 1


def main():
    sys.path.insert(0, os.path.abspath(os.path.join("data", "assets", "scripts", "gold")))
    sys.path.insert(0, os.path.abspath(os.path.join("data", "assets", "scripts", "silver")))
    import boto3
    import pandas as pd
    import build_cottonwood_mdpf_slice as sl

    if not hasattr(sl, "unidentified_block"):
        return _bad("arm=build no unidentified_block in build_cottonwood_mdpf_slice")
    s3 = boto3.client("s3")
    served = json.loads(s3.get_object(Bucket=B, Key=SLICE)["Body"].read())
    composed = sl.build_composed(s3)
    blk = composed.get("unidentified_strategies")
    if not isinstance(blk, dict):
        return _bad("arm=A composed has no unidentified_strategies block")
    gold, _ = sl.cottonwood_gold_by_date(s3)
    last = max(gold)
    for k, want in (("as_of", last), ("firm_id", "cottonwood")):
        if blk.get(k) != want:
            return _bad("arm=A block %s = %r, want %r" % (k, blk.get(k), want))
    if not (blk.get("names_scanned") or 0) > 0 or "etf_universe.json" not in str(blk.get("config_source")):
        return _bad("arm=A names_scanned %r / config_source %r" % (blk.get("names_scanned"), blk.get("config_source")))
    for r in blk.get("rows", []):
        if set(r) < {"firm_id", "name", "dollars", "reason"}:
            return _bad("arm=A row lacks a field: %r" % r)
    if set(composed["by_model"]) != set(served["by_model"]):
        return _bad("arm=A by_model keys differ from served")
    i, j = composed["dates"].index(served["dates"][-1]), len(served["dates"]) - 1
    if abs((composed["model_aua"][i] or 0) - (served["model_aua"][j] or 0)) > 0.01:
        return _bad("arm=A model_aua %r != served %r" % (composed["model_aua"][i], served["model_aua"][j]))
    print("A as_of %s names_scanned %d rows %d config %s; figures equal served" % (blk["as_of"], blk["names_scanned"], len(blk.get("rows", [])), blk["config_source"]))

    planted = copy.deepcopy(gold)
    row = {c: None for c in planted[last].columns}
    row.update({"model_name": "Opal Frontier Sleeve", "dollar_value": 1234.56, "account_count": 1})
    planted[last] = pd.concat([planted[last], pd.DataFrame([row])], ignore_index=True)
    hit = [r for r in sl.unidentified_block(planted)["rows"] if r["name"] == "Opal Frontier Sleeve"]
    if not hit or hit[0]["firm_id"] != "cottonwood" or abs(hit[0]["dollars"] - 1234.56) > 0.005 or hit[0]["reason"] != "NO_MEMBER":
        return _bad("arm=B planted name not listed as cottonwood/1234.56/NO_MEMBER: %r" % hit)
    if any(r["name"] == "Opal Frontier Sleeve" for r in sl.unidentified_block(gold)["rows"]):
        return _bad("arm=B control lists the planted name without the planted row")
    print("B planted 'Opal Frontier Sleeve' listed %r; control clean" % hit[0])
    print("W27-SEAM-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
