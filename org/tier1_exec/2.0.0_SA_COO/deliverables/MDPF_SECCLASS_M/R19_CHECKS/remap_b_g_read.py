#!/usr/bin/env python3
"""remap_b_g_read.py -- MDPF_SECCLASS multi-asset remap-b ledger leg G: READ-ONLY served read after the COT and BD gold fires.

Leg G of ledger `secclass-multi-asset-remap-b-m-20261007`: "the four Cottonwood clients sum to 1, both firms' firm_composition
gaps close". Reads only (get-object on served JSON; nothing written). Prints shares and sums, never holdings.

  COT clients (the four relationships the SC-e-20 before/after check used): the latest served `mix` point of
    s3://opal-data-cot/gold/entities/clients/<id>.json -- the sum of its class shares and the class names it carries.
  Firm composition (both firms): s3://<bucket>/gold/views/firm_composition.json -- total_market_value against the sum of the
    `mix[]` class market values, the gap, and the class names.

Last line: REMAP-B-G ok=<bool> cot_clients=<n> cot_sum_ok=<n> multi_asset_present=<n> comp_gap_cot=<$> comp_gap_bd=<$>
ok is True when every COT client's latest point sums to 1 within 1e-5, no served class is multi_asset, and each firm's absolute
composition gap is under $1.00.
"""
import json
import sys

import boto3

CLIENTS = ["z09305578", "z09305621", "z09305679", "z09305703"]
NON_CLASS = {"date", "total_mv"}


def _get(s3, bucket, key):
    o = s3.get_object(Bucket=bucket, Key=key)
    return json.loads(o["Body"].read()), o["VersionId"], o["LastModified"]


def main():
    s3 = boto3.client("s3", region_name="us-east-1")
    n_ok, n_multi = 0, 0
    for cid in CLIENTS:
        d, vid, lm = _get(s3, "opal-data-cot", f"gold/entities/clients/{cid}.json")
        pt = max(d.get("mix", []), key=lambda p: p.get("date", ""))
        cls = {k: v for k, v in pt.items() if k not in NON_CLASS and isinstance(v, (int, float))}
        s = sum(cls.values())
        good = abs(s - 1.0) <= 1e-5
        n_ok += good
        n_multi += "multi_asset" in cls
        print(f"COT {cid}: point={pt.get('date')} data_as_of={d.get('data_as_of')} version={vid} modified={lm:%Y-%m-%d %H:%MZ} "
              f"classes={sorted(cls)} sum={s:.6f} sum_ok={good}")
    gaps = {}
    for label, bucket in (("cot", "opal-data-cot"), ("bd", "opal-data-bd")):
        d, vid, lm = _get(s3, bucket, "gold/views/firm_composition.json")
        total = d.get("total_market_value")
        mix = d.get("mix", [])
        csum = sum((m.get("market_value") or 0.0) for m in mix)
        gaps[label] = (total or 0.0) - csum
        names = sorted(m.get("asset_class") for m in mix)
        n_multi += "multi_asset" in names
        print(f"COMP {label}: version={vid} modified={lm:%Y-%m-%d %H:%MZ} data_as_of={d.get('data_as_of')} total={total} "
              f"class_sum={csum:.2f} gap={gaps[label]:.2f} classes={names}")
    ok = n_ok == len(CLIENTS) and n_multi == 0 and all(abs(g) < 1.0 for g in gaps.values())
    print(f"REMAP-B-G ok={ok} cot_clients={len(CLIENTS)} cot_sum_ok={n_ok} multi_asset_present={n_multi} "
          f"comp_gap_cot={gaps['cot']:.2f} comp_gap_bd={gaps['bd']:.2f}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
