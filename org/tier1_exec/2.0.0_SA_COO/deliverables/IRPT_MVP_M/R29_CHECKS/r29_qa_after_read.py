"""r29_qa_after_read.py -- ledger leg H4 reader for the ONE WINDOW (IB-mr-291 + BD_THREAD_R2).

Reads each firm's newest holdings_qa manifest (the QA fire's output), streams its parts, and prints ONE line per firm:
  QA-AFTER <firm> manifest=<key> nodes=<n> securities=<n> unclassified=<n> PHYS=<class/sub|absent> GLD=<..> VXX=<..>
A value is read from the served QA artifact, never from a local census. Exit 1 if any firm cannot be read.
Usage: python r29_qa_after_read.py [firm ...]   (default: all three)
"""
from __future__ import annotations

import json
import sys

import boto3

FIRMS = {"49financial": "opal-data-49financial", "inflection": "opal-data-inflection", "cottonwood": "opal-data-cottonwood"}
TICKERS = ("PHYS", "GLD", "VXX")


def newest_manifest(s3, bucket: str, firm: str) -> str:
    prefix = f"irpt/{firm}/platinum/holdings_qa/date="
    best = None
    token = None
    scanned = 0
    while True:
        kw = {"Bucket": bucket, "Prefix": prefix}
        if token:
            kw["ContinuationToken"] = token
        page = s3.list_objects_v2(**kw)
        for obj in page.get("Contents", []):
            scanned += 1
            if obj["Key"].endswith(".manifest.json") and (best is None or obj["LastModified"] > best["LastModified"]):
                best = obj
        if not page.get("IsTruncated"):
            break
        token = page.get("NextContinuationToken")
    if best is None:
        raise SystemExit(f"ERROR: no QA manifest under {bucket}/{prefix} (objects scanned {scanned})")
    return best["Key"]


def iter_nodes(s3, bucket: str, manifest_key: str):
    # irpt-holdings-manifest-v2: partitions[].object.{bucket,key,version_id}; each part is a JSON document whose
    # SECURITY nodes carry ticker / asset_class / sub_asset_class (the served shape, contract HoldingsSnapshot v1).
    man = json.loads(s3.get_object(Bucket=bucket, Key=manifest_key)["Body"].read())
    for p in man.get("partitions", []):
        obj = p["object"]
        body = json.loads(s3.get_object(Bucket=obj["bucket"], Key=obj["key"], VersionId=obj["version_id"])["Body"].read())
        nodes = body.get("nodes") if isinstance(body, dict) else body
        if isinstance(nodes, dict):
            nodes = list(nodes.values())
        for n in nodes or []:
            yield n


def main(argv):
    firms = argv or list(FIRMS)
    s3 = boto3.client("s3", region_name="us-east-1")
    rc = 0
    for firm in firms:
        bucket = FIRMS[firm]
        try:
            mkey = newest_manifest(s3, bucket, firm)
            nodes = securities = unclassified = 0
            found = {t: "absent" for t in TICKERS}
            for n in iter_nodes(s3, bucket, mkey):
                nodes += 1
                if n.get("kind") != "SECURITY" and n.get("node_type") != "SECURITY":
                    continue
                securities += 1
                ac = n.get("asset_class")
                if ac in (None, "", "unclassified"):
                    unclassified += 1
                t = (n.get("ticker") or (n.get("identity") or {}).get("ticker") or (n.get("display") or {}).get("ticker"))
                if t in found and found[t] == "absent":
                    found[t] = f"{ac}/{n.get('sub_asset_class')}"
            print(f"QA-AFTER {firm} manifest={mkey} nodes={nodes} securities={securities} unclassified={unclassified} "
                  + " ".join(f"{t}={found[t]}" for t in TICKERS))
        except Exception as exc:  # noqa: BLE001 -- one line per firm, never a silent skip
            print(f"QA-AFTER {firm} ERROR {type(exc).__name__}: {exc}")
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
