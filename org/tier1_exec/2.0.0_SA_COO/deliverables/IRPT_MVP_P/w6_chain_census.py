#!/usr/bin/env python3
"""Window 6 (packet fffdca65) -- the Analysis chain's row and object census, before and after, keys only.

    python w6_chain_census.py <out.json>
    python w6_chain_census.py diff <before.json> <after.json>

Reads, never writes: the cottonwood partitions of irpt-requests and irpt-jobs by sort-key prefix, the `_opal`
irpt-jobs partition (the vendor session lease), the opal-data-irpt cottonwood prefixes K5 writes, and the
irpt-generation queue depth. `diff` prints every new key per store -- each must trace to K4 or K5.
"""
from __future__ import annotations

import datetime as dt
import json
import sys

import boto3

REGION = "us-east-1"
TABLES = {"irpt-requests": ("tenant", "request_revision", ["cottonwood"]),
          "irpt-jobs": ("tenant", "job", ["cottonwood", "_opal"])}
BUCKET = "opal-data-irpt"
PREFIXES = ["irpt/cottonwood/state/original_holdings/", "irpt/cottonwood/state/normalized_portfolios/",
            "irpt/cottonwood/state/request_compositions/", "irpt/cottonwood/state/vendor_documents/",
            "irpt/cottonwood/state/extraction_evidence/", "irpt/cottonwood/platinum/analysis_reports/"]
QUEUE = "https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation"


def keys_of(table, pk, sk, tenant):
    ddb = boto3.client("dynamodb", region_name=REGION)
    out, kw = [], dict(TableName=table, KeyConditionExpression="#p = :t", ExpressionAttributeNames={"#p": pk, "#s": sk},
                       ExpressionAttributeValues={":t": {"S": tenant}}, ProjectionExpression="#s")
    while True:
        page = ddb.query(**kw)
        out += [i[sk]["S"] for i in page.get("Items", [])]
        if "LastEvaluatedKey" not in page:
            return sorted(out)
        kw["ExclusiveStartKey"] = page["LastEvaluatedKey"]


def objects(prefix):
    s3 = boto3.client("s3", region_name=REGION)
    out = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=prefix):
        out += [o["Key"] for o in page.get("Contents", [])]
    return sorted(out)


def census():
    rows = {}
    for table, (pk, sk, tenants) in TABLES.items():
        for tenant in tenants:
            rows["%s/%s" % (table, tenant)] = keys_of(table, pk, sk, tenant)
    objs = {p: objects(p) for p in PREFIXES}
    q = boto3.client("sqs", region_name=REGION).get_queue_attributes(
        QueueUrl=QUEUE, AttributeNames=["ApproximateNumberOfMessages", "ApproximateNumberOfMessagesNotVisible"])
    return {"at": dt.datetime.now(dt.timezone.utc).isoformat(), "rows": rows, "objects": objs,
            "queue": q["Attributes"]}


def summary(c):
    for k, v in c["rows"].items():
        prefixes = {}
        for key in v:
            head = key.split("#", 1)[0] if "#" in key else key.split("-", 1)[0]
            prefixes[head] = prefixes.get(head, 0) + 1
        print("%s: %d %s" % (k, len(v), dict(sorted(prefixes.items()))))
    for p, v in c["objects"].items():
        print("%s: %d objects" % (p, len(v)))
    print("queue:", c["queue"])


def main(argv):
    if argv[1] == "diff":
        b, a = (json.load(open(p, encoding="utf-8")) for p in argv[2:4])
        for k in a["rows"]:
            new = sorted(set(a["rows"][k]) - set(b["rows"].get(k, [])))
            gone = sorted(set(b["rows"].get(k, [])) - set(a["rows"][k]))
            print("%s: +%d -%d" % (k, len(new), len(gone)))
            for key in new:
                print("   + " + key[:140])
        for p in a["objects"]:
            new = sorted(set(a["objects"][p]) - set(b["objects"].get(p, [])))
            print("%s: +%d" % (p, len(new)))
            for key in new:
                print("   + " + key[:160])
        print("queue before", b["queue"], "after", a["queue"])
        return
    c = census()
    summary(c)
    json.dump(c, open(argv[1], "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main(sys.argv)
