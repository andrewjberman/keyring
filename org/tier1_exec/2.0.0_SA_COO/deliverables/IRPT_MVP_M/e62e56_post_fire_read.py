#!/usr/bin/env python3
"""e62e56_post_fire_read.py -- SC-e-62/56 release, Branch A/B read after the first irpt-holdings-snapshot fire on the r4 bundle.

Per firm, read-only: the newest served publication (current/manifest.json -> dated manifest -> gold parquet, sha256 checked
-> platinum header) and compare with the pre-fire pin recorded in
NEVER_WIDEN_IRPT_BCKEND_COO_HALF_SECCLASS_E62_E56_RELEASE_20261007.md. Writes one JSON result.

    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/e62e56_post_fire_read.py --out <path>.json
"""
import argparse
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r30m_fwd5_replay_read import FIRMS, read_firm  # noqa: E402

PINS = {"49financial": {"index_version": "GtsM8pj9VnTwPZH3n5Bzp.oobsgLaja0", "date": "2026-10-06", "revision": "35ea000850f7"},
        "inflection": {"index_version": "a6gP7JDBtaKHr_LMKP0vQsNSegtaQQWc", "date": "2026-10-06", "revision": "acd27f407bbc"},
        "cottonwood": {"index_version": "gF3nGvI1eKu_xPEYZXBaRl7iw55fpmnL", "date": "2026-10-06", "revision": "7f69e500c18f"}}
SIX = {"cash", "fixed_income", "equity", "structured", "alternatives", "commodities"}


def walk_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from walk_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_strings(v)


def firm_read(s3, firm, bucket):
    head = s3.head_object(Bucket=bucket, Key="irpt/%s/platinum/holdings/current/manifest.json" % firm)
    pub, header, nodes = read_firm(s3, firm, bucket)
    secs = [n for n in nodes if n.get("node_kind") == "SECURITY"]
    classes = Counter(n.get("asset_class") for n in secs)
    basis = Counter(n.get("asset_class_basis") for n in secs)
    cusip = sum(1 for n in secs if any(s.startswith("CUSIP:") for s in walk_strings(
        {k: n.get(k) for k in ("classification", "asset_class_source", "class_source", "classification_key", "provenance")})))
    rec = (header.get("attribution_holdouts") or {}).get("reconcile") or {}
    pin = PINS[firm]
    out = {"index_version_now": head.get("VersionId"), "index_last_modified": str(head.get("LastModified")),
           "pin": pin, "publication": pub, "moved": pub["revision"][:12] != pin["revision"],
           "reconcile": rec, "reconciled": rec.get("reconciled") is True,
           "security_nodes": len(secs), "asset_class_counts": dict(classes), "asset_class_basis_counts": dict(basis),
           "multi_asset_nodes": classes.get("multi_asset", 0),
           "classes_outside_six": sorted(str(c) for c in classes if c not in SIX and c not in (None, "unclassified")),
           "cusip_keyed_security_nodes": cusip}
    out["branch_a"] = out["moved"] and out["reconciled"] and out["multi_asset_nodes"] == 0
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    import boto3
    from botocore.config import Config
    s3 = boto3.client("s3", region_name="us-east-1", config=Config(read_timeout=300, retries={"max_attempts": 8, "mode": "adaptive"}))
    res = {f: firm_read(s3, f, b) for f, b in FIRMS.items()}
    res["_identity"] = boto3.client("sts").get_caller_identity()["Arn"]
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, default=str)
    for f in FIRMS:
        r = res[f]
        print("%s: moved=%s %s rev %s (pin %s) reconciled=%s multi_asset=%d cusip_keyed=%d outside_six=%s classes=%s -> %s" % (
            f, r["moved"], r["publication"]["business_date"], r["publication"]["revision"][:12], r["pin"]["revision"],
            r["reconciled"], r["multi_asset_nodes"], r["cusip_keyed_security_nodes"], r["classes_outside_six"],
            r["asset_class_counts"], "BRANCH A" if r["branch_a"] else "CHECK"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
