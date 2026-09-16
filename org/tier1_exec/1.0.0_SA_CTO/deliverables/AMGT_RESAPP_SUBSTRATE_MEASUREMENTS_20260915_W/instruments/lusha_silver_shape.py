"""Read-only shape census of FIND_INSURE's real Lusha data in s3://opal-data-imo. KEY NAMES and COUNTS only -- no value of any
contact field is printed or written. Silver: which keys the records carry and how often. Gold: how often tenure_years is set."""
import collections
import json

import boto3

B = "opal-data-imo"
s3 = boto3.client("s3")
silver, gold = [], []
for page in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="corp/"):
    for o in page.get("Contents", []):
        k = o["Key"]
        if "/silver/linkedin-scrape/" in k:
            silver.append(k)
        elif "/gold/" in k:
            gold.append(k)
print("silver objects %d, gold objects %d" % (len(silver), len(gold)))
print("silver filename stems:", dict(collections.Counter(k.rsplit("/", 1)[-1].split("_")[0].split(".")[0][:24] for k in silver).most_common(6)))
top = collections.Counter()
nested = collections.Counter()
n = 0
for k in silver:
    d = json.loads(s3.get_object(Bucket=B, Key=k)["Body"].read())
    recs = d if isinstance(d, list) else [d]
    for r in recs:
        if not isinstance(r, dict):
            continue
        n += 1
        for kk, v in r.items():
            if v not in (None, "", [], {}):
                top[kk] += 1
                if isinstance(v, dict):
                    nested.update("%s.%s" % (kk, x) for x, y in v.items() if y not in (None, "", [], {}))
                elif isinstance(v, list) and v and isinstance(v[0], dict):
                    nested.update("%s[].%s" % (kk, x) for x in v[0].keys())
print("silver records:", n)
print("top-level keys with a value (records):", dict(top.most_common(40)))
print("nested keys with a value (records):", dict(nested.most_common(40)))
print("gold filename stems:", dict(collections.Counter(k.rsplit("/", 1)[-1][:30] for k in gold).most_common(8)))
t = collections.Counter()
for k in gold:
    if not k.endswith(".json"):
        continue
    d = json.loads(s3.get_object(Bucket=B, Key=k)["Body"].read())
    stack = [d]
    while stack:
        o = stack.pop()
        if isinstance(o, dict):
            if "tenure_years" in o:
                t["rows with tenure_years key"] += 1
                if o["tenure_years"] is not None:
                    t["rows with tenure_years set"] += 1
            stack.extend(o.values())
        elif isinstance(o, list):
            stack.extend(o)
print("gold tenure census:", dict(t))
