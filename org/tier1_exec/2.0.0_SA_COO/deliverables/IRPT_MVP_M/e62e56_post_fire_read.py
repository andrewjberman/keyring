#!/usr/bin/env python3
"""e62e56_post_fire_read.py -- SC-e-62/56 release: the per-fire pin and NO-WORSE read (CTO half AMENDMENT 2 @a0d336b0ab).

Read-only. Two modes, one per side of each weekday irpt-holdings-snapshot fire (10:15 ET):

    python <this> pin  --out <pins>.json                 # before the fire: each firm's current/manifest.json VersionId
    python <this> read --pins <pins>.json --out <r>.json  # after the fire: Branch A (keep) or B (re-point) per firm

Branch A per firm (all four; CTO AMENDMENT 2.1 @b3f3996a72): reconcile difference <= 0.01; 0 multi_asset; 0 classes
outside the six; no security held at the pin is unclassified after the fire. New positions that serve unclassified
are listed (`unclassified_not_held_at_pin`), not graded. A firm that did not move keeps serving its pin and reads NOT-MOVED. Without --pins the
read uses the first-fire pins recorded in NEVER_WIDEN_IRPT_BCKEND_COO_HALF_SECCLASS_E62_E56_RELEASE_20261007.md.
"""
import argparse
import hashlib
import io
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r30m_fwd5_replay_read import FIRMS, read_firm  # noqa: E402

FIRST_FIRE_PINS = {
    "49financial": {"index_version": "GtsM8pj9VnTwPZH3n5Bzp.oobsgLaja0", "date": "2026-10-06", "revision": "35ea000850f7"},
    "inflection": {"index_version": "a6gP7JDBtaKHr_LMKP0vQsNSegtaQQWc", "date": "2026-10-06", "revision": "acd27f407bbc"},
    "cottonwood": {"index_version": "gF3nGvI1eKu_xPEYZXBaRl7iw55fpmnL", "date": "2026-10-06", "revision": "7f69e500c18f"}}
SIX = {"cash", "fixed_income", "equity", "structured", "alternatives", "commodities"}
TOLERANCE = 0.01


def index_key(firm):
    return "irpt/%s/platinum/holdings/current/manifest.json" % firm


def get_json(s3, bucket, key, ver=None):
    kw = {"Bucket": bucket, "Key": key, **({"VersionId": ver} if ver else {})}
    return json.loads(s3.get_object(**kw)["Body"].read())


def pin_firm(s3, firm, bucket):
    head = s3.head_object(Bucket=bucket, Key=index_key(firm))
    ver = head.get("VersionId")
    cur = get_json(s3, bucket, index_key(firm), ver)
    date = cur["latest_date"]
    man = get_json(s3, bucket, cur["dates"][date]["manifest"]["key"], cur["dates"][date]["manifest"].get("version_id"))
    return {"index_version": ver, "date": date, "revision": (man.get("revision") or "")[:12],
            "index_last_modified": str(head.get("LastModified"))}


def sec_key(n):
    sid = n.get("security_id") or {}
    return (sid.get("namespace"), sid.get("value"))


def pinned_classes(s3, firm, bucket, pin):
    """Security nodes of the publication the pinned index version names (the prior served revision)."""
    import pyarrow.parquet as pq
    cur = get_json(s3, bucket, index_key(firm), pin["index_version"])
    m = cur["dates"][cur["latest_date"]]["manifest"]
    g = get_json(s3, bucket, m["key"], m.get("version_id"))["gold"]
    data = s3.get_object(Bucket=g["bucket"], Key=g["key"], VersionId=g["version_id"])["Body"].read()
    assert hashlib.sha256(data).hexdigest() == g["sha256"], "pinned gold sha256 differs from its manifest"
    nodes = (json.loads(s) for s in pq.read_table(io.BytesIO(data), columns=["node_json"]).column("node_json").to_pylist())
    return [n for n in nodes if n.get("node_kind") == "SECURITY"]


def firm_read(s3, firm, bucket, pin):
    head = s3.head_object(Bucket=bucket, Key=index_key(firm))
    pub, header, nodes = read_firm(s3, firm, bucket)
    secs = [n for n in nodes if n.get("node_kind") == "SECURITY"]
    classes = Counter(n.get("asset_class") for n in secs)
    rec = (header.get("attribution_holdouts") or {}).get("reconcile") or {}
    prior = pinned_classes(s3, firm, bucket, pin)
    prior_classes = Counter(n.get("asset_class") for n in prior)
    placed_at_pin = {sec_key(n) for n in prior if n.get("asset_class") != "unclassified"}
    unclassified_at_pin = {sec_key(n) for n in prior if n.get("asset_class") == "unclassified"}
    now_unclassified = {sec_key(n) for n in secs if n.get("asset_class") == "unclassified"}
    held_at_pin = placed_at_pin | unclassified_at_pin
    out = {"index_version_now": head.get("VersionId"), "index_last_modified": str(head.get("LastModified")),
           "pin": pin, "publication": pub, "moved": head.get("VersionId") != pin["index_version"],
           "reconcile": rec, "security_nodes": len(secs), "asset_class_counts": dict(classes),
           "asset_class_basis_counts": dict(Counter(n.get("asset_class_basis") for n in secs)),
           "multi_asset_nodes": classes.get("multi_asset", 0),
           "classes_outside_six": sorted(str(c) for c in classes if c not in SIX and c not in (None, "unclassified")),
           "unclassified": classes.get("unclassified", 0), "unclassified_at_pin": prior_classes.get("unclassified", 0),
           "placed_at_pin_now_unclassified": sorted(str(k) for k in now_unclassified & (placed_at_pin - unclassified_at_pin)),
           "unclassified_not_held_at_pin": sorted(str(k) for k in now_unclassified - held_at_pin)}
    diff = rec.get("difference")
    checks = {"reconcile": rec.get("reconciled") is True and diff is not None and abs(diff) <= TOLERANCE,
              "multi_asset": out["multi_asset_nodes"] == 0,
              "six_class": not out["classes_outside_six"],
              "no_held_security_lost_class": not out["placed_at_pin_now_unclassified"]}
    out["unclassified_count_no_worse"] = out["unclassified"] <= out["unclassified_at_pin"]  # listed, not graded (2.1)
    out["checks"] = checks
    out["branch"] = ("NOT-MOVED" if not out["moved"] else "A" if all(checks.values()) else "B")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("pin", "read"))
    ap.add_argument("--pins")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    import boto3
    from botocore.config import Config
    s3 = boto3.client("s3", region_name="us-east-1",
                      config=Config(read_timeout=300, retries={"max_attempts": 8, "mode": "adaptive"}))
    ident = boto3.client("sts").get_caller_identity()["Arn"]
    if a.mode == "pin":
        res = {f: pin_firm(s3, f, b) for f, b in FIRMS.items()}
        for f in FIRMS:
            print("PIN %s index %s date %s rev %s" % (f, res[f]["index_version"], res[f]["date"], res[f]["revision"]))
    else:
        pins = json.load(open(a.pins, encoding="utf-8")) if a.pins else FIRST_FIRE_PINS
        res = {f: firm_read(s3, f, b, pins[f]) for f, b in FIRMS.items()}
        for f in FIRMS:
            r = res[f]
            print("%s: moved=%s %s rev %s (pin %s) checks=%s unclassified %d (pin %d) lost_class=%s new_unclassified=%s"
                  " -> BRANCH %s" % (
                      f, r["moved"], r["publication"]["business_date"], r["publication"]["revision"][:12],
                      r["pin"]["revision"], r["checks"], r["unclassified"], r["unclassified_at_pin"],
                      r["placed_at_pin_now_unclassified"], r["unclassified_not_held_at_pin"], r["branch"]))
    res["_identity"] = ident
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, default=str)
    return 0


if __name__ == "__main__":
    sys.exit(main())
