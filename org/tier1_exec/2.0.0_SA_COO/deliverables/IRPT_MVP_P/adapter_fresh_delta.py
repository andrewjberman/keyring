#!/usr/bin/env python3
"""S147 fix M, DELTA=0 on the FRESH path (CTO 101490): one adapter zip, in-process, computing fixed 49F windows fresh.

    python adapter_fresh_delta.py --zip <irpt-performance-adapter.zip> --selection sel_<64 hex> --out <json> \
        --window 2026-01-01:2026-09-16 [--window ...]

A window computes only ONCE on the served path: after that its pointer reopens it. So byte identity of a FRESH report
across two builds is measured here, in-process. It uses no principal and changes nothing live:
- the zip is extracted fresh and FIRST on sys.path; its own runtime.lambda_handler handles one API-Gateway-shaped GET
  per window, with the edge's trusted headers for a synthetic internal Opal subject (as reopen_authz_arm.py sends);
- every READ goes to the live table and buckets. Every WRITE is captured in memory and never leaves the process
  (IRPT_MVP_Y/live_walk/readthrough.py, 2.0.0_SA_COO~Y's doubles); any other SDK method raises;
- each window must take the FRESH path (its irpt_retained_phases line says path=fresh), or the run stops.
Records, per window: state, reason, actual_end, and sha256 of the report JSON (the retained_ref excluded, since it
names this run's captured object version). No report body is written out.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import sys
import tempfile
import zipfile

import boto3

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "IRPT_MVP_Y", "live_walk"))
import readthrough as rt  # noqa: E402

ROUTE = "GET /api/scoped/investor-reporting/performance/{accountSetId}"
HEADERS = {"x-origin-verify": "cloudfront", "x-user-role": "user", "x-contract-version": "v1",
           "x-user-tier": "internal", "x-firm-id": "opal-capital",
           "x-user-email": "reopen-arm-1@opal.test", "x-user-name": "reopen arm 1"}
ENV = {"IRPT_REQUESTS_TABLE": "irpt-requests", "IRPT_PERFORMANCE_MAPPING_AS_OF": "2026-09-23",
       "IRPT_EVIDENCE_BUCKET": "opal-data-ycharts",
       "IRPT_DIRECTORY_BUCKET_MAP": '{"49financial":"opal-data-bd","cottonwood":"opal-data-cot","inflection":"opal-data-inf"}'}


class _S3(rt.S3):
    """~Y's S3 double plus the ONE read the engine makes that it lacks: listing the partitions (list_objects_v2)."""

    def get_paginator(self, operation):
        if operation != "list_objects_v2":
            raise AttributeError("offline s3 paginates list_objects_v2 only, not " + operation)
        self.writes.read("s3:ListBucket")
        return self.real.get_paginator(operation)


class _Resource:
    def __init__(self, dynamo):
        self.dynamo = dynamo

    def Table(self, name):  # noqa: N802 -- boto3's own spelling
        table = rt.Table(self.dynamo, name)
        table.__dict__["meta"] = type("Meta", (), {"client": self.dynamo})()
        return table


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--selection", required=True)
    ap.add_argument("--window", action="append", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)

    root = tempfile.mkdtemp(prefix="adapter-delta-")
    with zipfile.ZipFile(a.zip) as z:
        z.extractall(root)
    sys.path.insert(0, root)
    os.environ.update(ENV, IRPT_CONTRACTS_DIR=root, IRPT_FIRM_REGISTRY=os.path.join(root, "firm_registry.json"),
                      IRPT_BD_HELPERS_PATH=os.path.join(root, "bd_helpers.py"), AWS_DEFAULT_REGION="us-east-1")

    real_ddb, real_s3 = boto3.client("dynamodb"), boto3.client("s3")
    writes = rt.Writes()
    dynamo, s3 = rt.Dynamo(real_ddb, writes), _S3(real_s3, writes)
    boto3.client = lambda name, *args, **kw: {"dynamodb": dynamo, "s3": s3}[name]
    boto3.resource = lambda name, *args, **kw: _Resource(dynamo)

    import runtime  # noqa: E402  -- the extract's own module
    results = []
    for window in a.window:
        start, end = window.split(":")
        event = {"version": "2.0", "routeKey": ROUTE, "headers": dict(HEADERS),
                 "pathParameters": {"accountSetId": a.selection},
                 "queryStringParameters": {"start": start, "end": end, "selected_tenant": "49financial"}}
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            answer = runtime.lambda_handler(event, None)
        if isinstance(answer.get("body"), str):
            answer = json.loads(answer["body"])
        lines = [json.loads(x) for x in captured.getvalue().splitlines() if x.startswith("{")]
        paths = [x.get("path") for x in lines if x.get("event") == "irpt_retained_phases"]
        data = answer.get("data") if isinstance(answer.get("data"), dict) else None
        report = {k: v for k, v in (data or {}).items() if k != "retained_ref"}
        timing = next((x for x in lines if x.get("event") == "irpt_performance_timing"), {})
        row = {"window": [start, end], "retained_path": paths, "state": (answer.get("status") or {}).get("state"),
               "reason": (answer.get("status") or {}).get("public_reason_code"),
               "actual_end": ((data or {}).get("dates") or {}).get("actual_end"),
               "report_sha256": hashlib.sha256(json.dumps(report, sort_keys=True).encode()).hexdigest() if data else None,
               "authorize_calls": timing.get("authorize_calls"), "authorize_ms_sum": timing.get("authorize_ms_sum"),
               "full_releases": sum(1 for ms in timing.get("authorize_ms") or [] if ms >= 50.0)}
        print("%s..%s path=%s state=%s end=%s report=%s authorize_calls=%s authorize_ms_sum=%s full(>=50ms)=%s" % (
            start, end, paths, row["state"], row["actual_end"], (row["report_sha256"] or "")[:12],
            row["authorize_calls"], row["authorize_ms_sum"], row["full_releases"]))
        if paths != ["fresh"]:
            for x in captured.getvalue().splitlines():
                if "irpt_error" in x or "internal" in x or "Error" in x:
                    print("  captured:", x[:400])
            raise SystemExit("STOP: %s did not take the fresh path (%s)" % (window, paths))
        results.append(row)
    live_writes = [w for w in writes.log]
    json.dump({"zip": os.path.basename(a.zip), "zip_sha256": hashlib.sha256(open(a.zip, "rb").read()).hexdigest(),
               "selection": a.selection, "results": results, "captured_writes": len(live_writes)},
              open(a.out, "w", encoding="utf-8"), indent=1)
    print("captured writes (never sent):", len(live_writes))


if __name__ == "__main__":
    main()
