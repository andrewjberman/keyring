#!/usr/bin/env python3
"""The walk window's write-trace censuses in ONE read, before and after (window 18 onward).

    python walk_window_census.py <out.json>
    python walk_window_census.py diff <before.json> <after.json>

Reads only. Counts and keys, never a report value or a client name:
  REPORT# rows per firm (irpt-requests), every 49F irpt-requests key, every object key under the evidence bucket's
  firms/ prefix (bundles, grants, packets, receipts, exr_ pointers), /irpt/render-token/ parameters, tracked
  *.pdf/*.png/*.har in git, and the sha12 of RPT-b5e0a16e's owner principal (reopen-rule arm 3).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import subprocess
import sys

import boto3

FIRMS = ("49financial", "cottonwood", "inflection")
EVIDENCE_BUCKET = "opal-data-ycharts"
ARM3_KEY = ("49financial", "REPORT#RPT-b5e0a16e")


def _table():
    env = boto3.client("lambda").get_function_configuration(FunctionName="irpt-export-render")
    return env["Environment"]["Variables"]["IRPT_REQUESTS_TABLE"]


def _keys(ddb, table, firm, prefix=""):
    out, kw = [], {"TableName": table, "ProjectionExpression": "request_revision",
                   "KeyConditionExpression": "tenant = :t" + (" AND begins_with(request_revision, :p)" if prefix else ""),
                   "ExpressionAttributeValues": dict({":t": {"S": firm}}, **({":p": {"S": prefix}} if prefix else {}))}
    while True:
        r = ddb.query(**kw)
        out += [i["request_revision"]["S"] for i in r.get("Items", [])]
        if "LastEvaluatedKey" not in r:
            return sorted(out)
        kw["ExclusiveStartKey"] = r["LastEvaluatedKey"]


def take():
    ddb, s3, ssm = boto3.client("dynamodb"), boto3.client("s3"), boto3.client("ssm")
    table = _table()
    reports = {f: _keys(ddb, table, f, "REPORT#") for f in FIRMS}
    rows49 = _keys(ddb, table, "49financial")
    objects = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=EVIDENCE_BUCKET, Prefix="firms/"):
        objects += [o["Key"] for o in page.get("Contents", [])]
    tokens = []
    for page in ssm.get_paginator("describe_parameters").paginate(
            ParameterFilters=[{"Key": "Name", "Option": "BeginsWith", "Values": ["/irpt/render-token/"]}]):
        tokens += [p["Name"] for p in page.get("Parameters", [])]
    media = subprocess.run(["git", "ls-files", "*.pdf", "*.png", "*.har"], capture_output=True, text=True).stdout.split()
    owner = None
    for key in reports["49financial"]:
        if key.startswith(ARM3_KEY[1]):
            item = ddb.get_item(TableName=table, Key={"tenant": {"S": "49financial"}, "request_revision": {"S": key}},
                                ConsistentRead=True).get("Item") or {}
            pid = ((item.get("owner") or {}).get("M") or {}).get("principal_id", {}).get("S", "")
            owner = hashlib.sha256(pid.encode()).hexdigest()[:12] if pid else None
    return {"taken_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "table": table,
            "report_rows": {f: len(v) for f, v in reports.items()}, "report_keys": reports,
            "rows_49f": len(rows49), "rows_49f_keys": rows49,
            "evidence_objects": len(objects), "evidence_keys": sorted(objects),
            "exr_pointers": sorted(k for k in objects if "/generations/exr_" in k and k.endswith("/pending.json")),
            "render_tokens": len(tokens), "tracked_media": len(media), "arm3_owner_sha12": owner}


def diff(a, b):
    out = {"report_rows": {f: [a["report_rows"][f], b["report_rows"][f]] for f in FIRMS},
           "report_added": {f: sorted(set(b["report_keys"][f]) - set(a["report_keys"][f])) for f in FIRMS},
           "rows_49f": [a["rows_49f"], b["rows_49f"]],
           "rows_49f_added": sorted(set(b["rows_49f_keys"]) - set(a["rows_49f_keys"])),
           "evidence_objects": [a["evidence_objects"], b["evidence_objects"]],
           "evidence_added": sorted(set(b["evidence_keys"]) - set(a["evidence_keys"])),
           "render_tokens": [a["render_tokens"], b["render_tokens"]],
           "tracked_media": [a["tracked_media"], b["tracked_media"]],
           "arm3_owner_sha12": [a["arm3_owner_sha12"], b["arm3_owner_sha12"]]}
    return out


if __name__ == "__main__":
    if sys.argv[1] == "diff":
        print(json.dumps(diff(json.load(open(sys.argv[2])), json.load(open(sys.argv[3]))), indent=1))
    else:
        snap = take()
        json.dump(snap, open(sys.argv[1], "w"), indent=1)
        print(json.dumps({k: snap[k] for k in ("taken_at", "report_rows", "rows_49f", "evidence_objects",
                                               "exr_pointers", "render_tokens", "tracked_media", "arm3_owner_sha12")}))
