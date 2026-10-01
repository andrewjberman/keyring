"""Leg Q reader for irpt-inf-split-positions-m-20261001: QA publication vs served publication, per firm.

Prints, per namespace: business date, revision, accounts and their total, security rows and their total, accounts whose
security rows do not sum to the account, positions carrying part=NOT_STATED, DRILL WITHHELD notes, class lines; then the
per-account comparison QA vs served (signature = sorted descendants (kind, basis, value, class)).
"""
import json
import sys
from collections import defaultdict

import boto3

FIRMS = {"49financial": "opal-data-49financial", "inflection": "opal-data-inflection", "cottonwood": "opal-data-cottonwood"}
s3 = boto3.client("s3", region_name="us-east-1")


def get(bucket, key, ver=None):
    kw = {"Bucket": bucket, "Key": key}
    if ver:
        kw["VersionId"] = ver
    return json.loads(s3.get_object(**kw)["Body"].read())


def newest_qa_manifest(bucket, firm):
    prefix = f"irpt/{firm}/platinum/holdings_qa/date="
    best, token = None, None
    while True:
        kw = {"Bucket": bucket, "Prefix": prefix}
        if token:
            kw["ContinuationToken"] = token
        page = s3.list_objects_v2(**kw)
        for o in page.get("Contents", []):
            if o["Key"].endswith(".manifest.json") and (best is None or o["LastModified"] > best["LastModified"]):
                best = o
        if not page.get("IsTruncated"):
            break
        token = page["NextContinuationToken"]
    return best["Key"], str(best["LastModified"])


def served_manifest(bucket, firm, date):
    cur = get(bucket, f"irpt/{firm}/platinum/holdings/current/manifest.json")
    m = cur["dates"][date]["manifest"]
    return m["key"], m["version_id"]


def nodes_of(bucket, man):
    out = []
    for p in man["partitions"]:
        o = p["object"]
        out.extend(get(o["bucket"], o["key"], o.get("version_id"))["nodes"])
    return out


def census(nodes):
    by_id = {n["node_id"]: n for n in nodes}

    def root(nid):
        seen = 0
        while nid is not None and seen < 64:
            n = by_id.get(nid)
            if n is None:
                return None
            if n.get("node_kind") == "ACCOUNT":
                return nid
            nid = n.get("parent_node_id")
            seen += 1
        return None

    accts = {n["node_id"]: n for n in nodes if n.get("node_kind") == "ACCOUNT"}
    sec_by_acct = defaultdict(float)
    sig = defaultdict(list)
    classes = defaultdict(float)
    not_stated, not_stated_val, not_stated_accts = 0, 0.0, set()
    sec_n, sec_v = 0, 0.0
    withheld = 0
    for n in nodes:
        txt = json.dumps(n)
        if "DRILL WITHHELD" in txt:
            withheld += 1
        r = root(n["node_id"])
        if n.get("node_kind") != "ACCOUNT" and r is not None:
            sig[r].append((n.get("node_kind"), n.get("basis"), round(n["amount"]["value"], 2), n.get("asset_class")))
        if n.get("node_kind") == "SECURITY" and n.get("basis") != "TARGET":
            v = n["amount"]["value"]
            sec_n += 1
            sec_v += v
            classes[n.get("asset_class")] += v
            if r is not None:
                sec_by_acct[r] += v
            if "NOT_STATED" in txt:
                not_stated += 1
                not_stated_val += v
                not_stated_accts.add(r)
    acct_total = sum(a["amount"]["value"] for a in accts.values())
    off = [a for a in accts if abs(sec_by_acct.get(a, 0.0) - accts[a]["amount"]["value"]) > 0.01]
    off_val = sum(accts[a]["amount"]["value"] - sec_by_acct.get(a, 0.0) for a in off)
    return {
        "accounts": len(accts), "account_total": round(acct_total, 2), "security_rows": sec_n,
        "security_total": round(sec_v, 2), "accounts_secs_not_summing": len(off), "their_gap": round(off_val, 2),
        "not_stated_positions": not_stated, "not_stated_value": round(not_stated_val, 2),
        "not_stated_accounts": len(not_stated_accts), "drill_withheld_nodes": withheld,
        "classes": {k: round(v, 2) for k, v in sorted(classes.items(), key=lambda kv: str(kv[0]))},
        "_sig": {a: sorted(map(str, v)) for a, v in sig.items()}, "_accts": accts,
    }


def main(firms):
    for firm in firms:
        bucket = FIRMS[firm]
        qkey, qmod = newest_qa_manifest(bucket, firm)
        qman = get(bucket, qkey)
        date = qman["business_date"]
        skey, sver = served_manifest(bucket, firm, date)
        sman = get(bucket, skey, sver)
        q, s = census(nodes_of(bucket, qman)), census(nodes_of(bucket, sman))
        print(f"== {firm} business_date {date}")
        print(f"   QA     {qkey} (written {qmod}) revision {qman['revision'][:12]}")
        print(f"   SERVED {skey} revision {sman['revision'][:12]}")
        for label, c in (("SERVED", s), ("QA", q)):
            print("   %-6s %s" % (label, json.dumps({k: v for k, v in c.items() if not k.startswith("_")})))
        # account identity across revisions: the account node's own label/ids, matched by node_id
        common = set(q["_accts"]) & set(s["_accts"])
        diff = [a for a in common if q["_sig"].get(a) != s["_sig"].get(a)]
        amt = [a for a in common if abs(q["_accts"][a]["amount"]["value"] - s["_accts"][a]["amount"]["value"]) > 0.005]
        print(f"   accounts in both {len(common)} (QA only {len(set(q['_accts']) - common)}, served only "
              f"{len(set(s['_accts']) - common)}); account amount differs {len(amt)}; descendant signature differs {len(diff)}")
        sys.stdout.flush()


if __name__ == "__main__":
    main(sys.argv[1:] or list(FIRMS))
