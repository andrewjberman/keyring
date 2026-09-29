"""Round 22 (~M) check IBM22-222-AC1: the three Holdings packages are re-minted under a CLOSED ledger, and the next
scheduled publication SERVES the L0 shape at every firm.

Reads the cell's read-back JSON. For each firm: the package head-object carries the recorded members-sha256 (and it is
not the pre-change 94f2e3433d9e); the served Holdings object named by key + VersionId is downloaded and read -- it
holds CATEGORY nodes named only Models / SMAs / Client, carries source_vendor_keys, and (cottonwood) at least one
ACCOUNT with an assigned_strategy. The re-mint ledger entry is CLOSED.

Run from the repo (or worktree) root. Prints SERVED-L0 <firm=categories...> or NOT-SERVED: <reason>.
"""
import glob
import json
import os
import sys

import boto3

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R22_L0_REMINT_READBACK.json"
LEDGER = "org/critical_paths/change_management/*_irpt-holdings-l0-remint-m-*_deploy_completion.md"
FIRMS = ("49financial", "inflection", "cottonwood")
OLD_MEMBERS = "94f2e3433d9e"


def walk(obj):
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v)


def main():
    if not os.path.exists(PATH):
        print("NOT-SERVED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        rows = {r.get("firm"): r for r in json.load(fh).get("firms") or []}
    if set(rows) != set(FIRMS):
        print("NOT-SERVED: firms %s" % sorted(rows))
        return 1
    s3 = boto3.client("s3", region_name="us-east-1")
    out = []
    for firm in FIRMS:
        r = rows[firm]
        bucket, key = r.get("package_bucket", ""), r.get("package_key", "")
        meta = s3.head_object(Bucket=bucket, Key=key).get("Metadata") or {}
        got = meta.get("members-sha256", "")
        if not got or got != r.get("members_sha256") or got.startswith(OLD_MEMBERS):
            print("NOT-SERVED: %s package members-sha256 %r vs recorded %r" % (firm, got[:12], (r.get("members_sha256") or "")[:12]))
            return 1
        body = s3.get_object(Bucket=r.get("served_bucket", ""), Key=r.get("served_key", ""),
                             VersionId=r.get("served_version", ""))["Body"].read()
        doc = json.loads(body)
        nodes = [d for d in walk(doc) if "node_kind" in d]
        cats = sorted({str(d.get("name") or d.get("display_name") or (d.get("display") or {}).get("label"))
                       for d in nodes if d.get("node_kind") == "CATEGORY"})
        if not cats or not set(cats) <= {"Models", "SMAs", "Client"}:
            print("NOT-SERVED: %s served CATEGORY names %s" % (firm, cats))
            return 1
        if not any("source_vendor_keys" in d for d in walk(doc)):
            print("NOT-SERVED: %s served document carries no source_vendor_keys" % firm)
            return 1
        if firm == "cottonwood" and not any(d.get("node_kind") == "ACCOUNT" and d.get("assigned_strategy")
                                            for d in nodes):
            print("NOT-SERVED: cottonwood served ACCOUNT nodes carry no assigned_strategy")
            return 1
        out.append("%s=%s" % (firm, "/".join(cats)))
    entries = glob.glob(LEDGER)
    if len(entries) != 1:
        print("NOT-SERVED: %d re-mint ledger entries" % len(entries))
        return 1
    with open(entries[0], encoding="utf-8") as fh:
        if "**Status:** CLOSED" not in fh.read():
            print("NOT-SERVED: re-mint ledger not CLOSED")
            return 1
    print("SERVED-L0 " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
