#!/usr/bin/env python3
"""e75_retained_reclass_diff.py -- MDPF_SECCLASS e75: which BD envelopes had a RETAINED dated entry's holding class changed by the
2026-10-09 04:00Z fire, compared with each key's previous version (READ-ONLY).

For every gold/entities/clients/{rid}.json in opal-data-bd: read the current version and the version before it. For every date present
in BOTH that is NOT the newest date of the current version, compare each holding's asset_class, keyed by (ticker, asset_name). Prints
E75-DIFF envelopes=<n> changed_envelopes=<k> changed_holdings=<h> in_signed_set=<a> outside_signed_set=<b> transitions={old->new: n},
and writes the per-envelope detail to argv[1]. The signed set is the 36 envelope keys of E75_PREFIRE_VERSIONS_20261008.json.
"""
import json
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import boto3

BUCKET = "opal-data-bd"
PREFIX = "gold/entities/clients/"
HERE = Path(__file__).resolve().parent
SIGNED = HERE.parent / "E75_PREFIRE_VERSIONS_20261008.json"


def signed_set():
    d = json.load(open(SIGNED, encoding="utf-8"))
    items = d.get("keys") or d.get("versions") or d
    keys = items.keys() if isinstance(items, dict) else [i.get("key") for i in items]
    return {k for k in keys if k and k.startswith(PREFIX)}


def classes(doc):
    out = {}
    for e in (doc or {}).get("concentration", []):
        out[e.get("date")] = {(h.get("ticker"), h.get("asset_name")): h.get("asset_class") for h in e.get("holdings", [])}
    return out


def main(argv):
    s3 = boto3.client("s3", region_name="us-east-1")
    keys = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=PREFIX):
        keys += [o["Key"] for o in page.get("Contents", []) if o["Key"].endswith(".json")]
    signed = signed_set()

    def one(k):
        vs = s3.list_object_versions(Bucket=BUCKET, Prefix=k).get("Versions", [])
        vs = sorted([v for v in vs if v["Key"] == k], key=lambda v: v["LastModified"], reverse=True)
        if len(vs) < 2:
            return k, []
        cur = json.loads(s3.get_object(Bucket=BUCKET, Key=k, VersionId=vs[0]["VersionId"])["Body"].read())
        prev = json.loads(s3.get_object(Bucket=BUCKET, Key=k, VersionId=vs[1]["VersionId"])["Body"].read())
        c, p = classes(cur), classes(prev)
        newest = max(c) if c else None
        changes = []
        for ds in set(c) & set(p):
            if ds == newest:
                continue
            for hk, cls in c[ds].items():
                if hk in p[ds] and p[ds][hk] != cls:
                    changes.append((ds, hk[0], hk[1], p[ds][hk], cls))
        return k, changes

    with ThreadPoolExecutor(16) as pool:
        res = list(pool.map(one, keys))
    changed = {k: ch for k, ch in res if ch}
    trans = Counter(f"{c[3]}->{c[4]}" for ch in changed.values() for c in ch)
    inside = sum(1 for k in changed if k in signed)
    print(f"E75-DIFF envelopes={len(keys)} changed_envelopes={len(changed)} "
          f"changed_holdings={sum(len(v) for v in changed.values())} in_signed_set={inside} "
          f"outside_signed_set={len(changed) - inside} transitions={dict(trans)}")
    if len(argv) > 1:
        json.dump({k: v for k, v in sorted(changed.items())}, open(argv[1], "w", encoding="utf-8"), indent=1, default=str)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
