#!/usr/bin/env python3
"""e67_cot_post_fire_read.py -- MDPF_SECCLASS SC-e-67 ledger leg G (CTO condition 3): READ-ONLY post-fire read of Cottonwood.

Over every opal-data-cot platinum/clients/*/concentration.json and gold/entities/clients/*.json (denominator printed):
  - multi_asset: count of holdings whose asset_class is "multi_asset", over EVERY dated entry of every file;
  - rebuilt: files whose LastModified is after the fire start (argv[1], ISO UTC, e.g. 2026-10-09T10:30:00Z);
  - unchanged arm: for each rebuilt file, its previous version is read; on every date both versions carry, every holding
    (keyed by ticker, else asset_name) whose previous class was NOT multi_asset must carry the same class now.
Prints  E67-G ok=<bool> files=<n> rebuilt=<n> multi_asset=<n> compared=<n holdings> moved_other=<n> unread=<n>
ok = every file read, multi_asset == 0 and moved_other == 0 (rebuilt is printed beside files). Writes JSON detail to argv[2] if given.
"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import boto3

BUCKET = "opal-data-cot"
SETS = (("platinum/clients/", "concentration.json"), ("gold/entities/clients/", ".json"))


def _hkey(h):
    return h.get("ticker") or h.get("asset_name") or ""


def _classes(doc):
    out = {}
    for entry in doc.get("concentration") or []:
        out[entry.get("date")] = {_hkey(h): h.get("asset_class") for h in entry.get("holdings") or []}
    return out


def main(argv) -> int:
    fire = datetime.fromisoformat(argv[1].replace("Z", "+00:00"))
    s3 = boto3.client("s3")
    keys = []
    for pre, suf in SETS:
        for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=pre):
            keys += [(o["Key"], o["LastModified"]) for o in pg.get("Contents", []) if o["Key"].endswith(suf)]

    def one(item):
        key, lm = item
        try:
            cur = s3.get_object(Bucket=BUCKET, Key=key)
            doc = json.loads(cur["Body"].read())
            ma = sum(1 for e in doc.get("concentration") or [] for h in e.get("holdings") or []
                     if h.get("asset_class") == "multi_asset")
            res = {"key": key, "rebuilt": lm > fire, "multi_asset": ma, "compared": 0, "moved": []}
            if lm > fire:
                vers = [v for v in s3.list_object_versions(Bucket=BUCKET, Prefix=key).get("Versions", []) if v["Key"] == key]
                vers.sort(key=lambda v: v["LastModified"], reverse=True)
                prev = next((v for v in vers if v["VersionId"] != cur.get("VersionId")), None)
                if prev is not None:
                    pdoc = json.loads(s3.get_object(Bucket=BUCKET, Key=key, VersionId=prev["VersionId"])["Body"].read())
                    now, before = _classes(doc), _classes(pdoc)
                    for d in set(now) & set(before):
                        for hk, pc in before[d].items():
                            if pc == "multi_asset" or hk not in now[d]:
                                continue
                            res["compared"] += 1
                            if now[d][hk] != pc:
                                res["moved"].append({"date": d, "holding": hk, "was": pc, "now": now[d][hk]})
            return res
        except Exception as exc:  # a failed read is a value, never a zero
            return {"key": key, "error": f"{type(exc).__name__}: {exc}"}

    with ThreadPoolExecutor(max_workers=16) as pool:
        rows = list(pool.map(one, keys))
    unread = [r for r in rows if "error" in r]
    good = [r for r in rows if "error" not in r]
    rebuilt = sum(r["rebuilt"] for r in good)
    ma = sum(r["multi_asset"] for r in good)
    compared = sum(r["compared"] for r in good)
    moved = [dict(m, key=r["key"]) for r in good for m in r["moved"]]
    ok = not unread and ma == 0 and not moved  # rebuilt is printed: a relationship no fire rewrites is counted, not graded
    # The half's arm 1 (NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_D04_MULTI_ASSET_20261008.md:53): SGIIX reads equity in both relationships,
    # and branch (B): a fire with no new date moves nothing, which reads as NOT-YET, never as a pass.
    sgiix = {}
    for rid in ("z09305621", "z09305679"):
        doc = json.loads(s3.get_object(Bucket=BUCKET, Key=f"platinum/clients/{rid}/concentration.json")["Body"].read())
        last = (doc.get("concentration") or [{}])[-1]
        sgiix[rid] = (last.get("date"), sorted({h.get("asset_class") for h in last.get("holdings") or [] if h.get("ticker") == "SGIIX"}))
    sg_ok = all(cls == ["equity"] for _, cls in sgiix.values())
    ok = ok and sg_ok
    verdict = "PASS" if ok else ("NOT-YET" if rebuilt == 0 else "FAIL")
    print(f"E67-G ok={ok} verdict={verdict} files={len(keys)} rebuilt={rebuilt} multi_asset={ma} compared={compared} "
          f"moved_other={len(moved)} unread={len(unread)} sgiix={sgiix}")
    if len(argv) > 2:
        with open(argv[2], "w", encoding="utf-8") as fh:
            json.dump({"fire_start": argv[1], "files": len(keys), "rebuilt": rebuilt, "multi_asset": ma,
                       "compared": compared, "moved_other": moved[:200], "unread": unread[:50]}, fh, indent=2)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
