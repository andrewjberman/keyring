"""Census: on the LIVE opal-amgt-scoped-api, which served peer members carry a minor-unit currency code (GBp, GBX, ZAc, ILA, ILs)
beside their price? Reads every subject under s3://opal-data-harvest/peers/v1/ and invokes GET /security/<S>/peers. Read only."""
import json
from concurrent.futures import ThreadPoolExecutor

import boto3

MINOR = {"GBp", "GBX", "ZAc", "ZAC", "ILA", "ILs"}
s3 = boto3.client("s3", region_name="us-east-1")
lam = boto3.client("lambda", region_name="us-east-1")
subs = []
for page in s3.get_paginator("list_objects_v2").paginate(Bucket="opal-data-harvest", Prefix="peers/v1/", Delimiter="/"):
    subs += [p["Prefix"].split("/")[2] for p in page.get("CommonPrefixes", [])]


def one(s):
    ev = {"rawPath": "/api/scoped/amgt/security/%s/peers" % s, "queryStringParameters": None,
          "requestContext": {"http": {"method": "GET"}}, "headers": {"x-firm-id": "opal"}}
    r = json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read())
    if r.get("statusCode") != 200:
        return s, r.get("statusCode"), []
    body = json.loads(r.get("body") or "{}")
    mem = (body.get("peers") or body).get("members") or []
    return s, 200, mem


cfg = lam.get_function_configuration(FunctionName="opal-amgt-scoped-api")
print("function CodeSha256", cfg["CodeSha256"], "LastModified", cfg["LastModified"])
with ThreadPoolExecutor(8) as ex:
    res = list(ex.map(one, subs))
ok = [r for r in res if r[1] == 200]
members = [(s, m) for s, _, mem in ok for m in mem]
cur = [(s, m) for s, m in members if m.get("price_currency")]
minor = [(s, m) for s, m in cur if m.get("price_currency") in MINOR]
uniq = {}
for s, m in minor:
    uniq.setdefault((m.get("ticker"), m.get("name")), (m.get("price"), m.get("price_currency"), m.get("price_currency_claim"), s))
print("DENOMINATOR subjects listed %d, served 200 %d, members %d, members serving a price_currency %d" % (
    len(subs), len(ok), len(members), len(cur)))
print("members serving a MINOR-unit code: %d rows, %d distinct securities" % (len(minor), len(uniq)))
for (t, n), (p, c, cl, s) in sorted(uniq.items(), key=lambda kv: str(kv[0])):
    print("   %-10s %-40s price %-10s %s (%s) e.g. under %s" % (t, (n or "")[:40], p, c, cl, s))
