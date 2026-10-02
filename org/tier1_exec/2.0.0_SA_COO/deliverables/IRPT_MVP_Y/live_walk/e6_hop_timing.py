#!/usr/bin/env python3
"""E6 (CTO rulings batch 93 item 8): time the served irpt-status reads BY HOP, before any change. Reads only.

    python e6_hop_timing.py <irpt-status.zip> <tenant> <request-id> <out.json> [--repeat N]

The LIVE bundle (downloaded by its S3 version) is extracted fresh and FIRST on sys.path; `status_installed.compose_ports`
and `build_boundary` are given REAL clients wrapped so that every AWS call is timed and named (service, operation,
table or bucket, key family). Each route is called as the service principal svc-irpt-analysis with the edge headers the
served boundary reads, N times; for each call the first-party functions' cumulative times come from cProfile. The
laptop adds one round trip per AWS call that the function in us-east-1 does not pay, so CALL COUNTS and the share of
each hop are the measurement; absolute times are an upper bound. Recorded: route, state, reason, wall ms, AWS calls by
shape with count and ms, the top first-party functions by cumulative ms. Never a client's values. ASCII only.
"""
import argparse
import collections
import hashlib
import cProfile
import json
import os
import pstats
import sys
import tempfile
import time
import zipfile

import boto3

CALLS = []


def _target(service, op, kwargs):
    if "TableName" in kwargs:
        return kwargs["TableName"]
    if "Bucket" in kwargs:
        key = kwargs.get("Key") or kwargs.get("Prefix") or ""
        parts = key.split("/")
        family = "/".join(parts[:4]) if len(parts) > 4 else "/".join(parts[:-1])
        return "%s:%s" % (kwargs["Bucket"], family.replace(parts[1] if len(parts) > 1 else "", "<firm>", 1))
    return ""


class Timed(object):
    """Every method call on the wrapped client is timed and recorded."""

    def __init__(self, inner, service):
        self._inner, self._service = inner, service

    def __getattr__(self, name):
        attr = getattr(self._inner, name)
        if not callable(attr) or name.startswith("_") or name in ("meta", "exceptions", "get_paginator"):
            return attr

        def call(*args, **kwargs):
            start = time.perf_counter()
            try:
                return attr(*args, **kwargs)
            finally:
                key = kwargs.get("Key")
                CALLS.append({"service": self._service, "op": name, "target": _target(self._service, name, kwargs)
                              or self._service, "ms": (time.perf_counter() - start) * 1000.0,
                              "key": hashlib.sha256(json.dumps(key, sort_keys=True, default=str).encode()).hexdigest()[:16]
                              if key is not None else None})
        return call


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("zip")
    ap.add_argument("tenant")
    ap.add_argument("request_id")
    ap.add_argument("out")
    ap.add_argument("--repeat", type=int, default=3)
    a = ap.parse_args(argv)
    extract = tempfile.mkdtemp(prefix="irpt-status-e6-")
    zipfile.ZipFile(a.zip).extractall(extract)
    sys.path.insert(0, extract)
    os.environ.setdefault("IRPT_DIRECTORY_BUCKET_MAP", json.dumps(
        {"49financial": "opal-data-bd", "cottonwood": "opal-data-cot", "inflection": "opal-data-inf"}))
    import status_installed as si
    from botocore.config import Config
    once = Config(retries={"total_max_attempts": 1, "mode": "standard"}, region_name="us-east-1")
    clients = {"dynamodb": Timed(boto3.client("dynamodb", config=once), "dynamodb"),
               "table": Timed(boto3.resource("dynamodb", config=once).Table("irpt-requests"), "table:irpt-requests"),
               "s3": Timed(boto3.client("s3", config=once), "s3")}
    env = {si.REQUESTS_TABLE_ENV: "irpt-requests", si.JOBS_TABLE_ENV: "irpt-jobs"}
    t0 = time.perf_counter()
    ports = si.compose_ports(clients=clients, clock=time.time, environ=env)
    boundary = si.build_boundary(ports)
    compose_ms = (time.perf_counter() - t0) * 1000.0
    compose_calls = len(CALLS)
    headers = {"x-contract-version": "v1", "x-origin-verify": "cloudfront", "x-user-email": "svc-irpt-analysis@opalinvest.com",
               "x-user-role": "admin", "x-user-type": "service", "x-firm-id": "opal-capital",
               "x-user-name": "IRPT Analysis Service"}
    base = "/api/scoped/investor-reporting"
    routes = [("status read, dates capability", "GET %s/status/{jobId}" % base, {"jobId": a.request_id},
               {"X-IRPT-Status-Dates": "prospect-v1"}),
              ("status read, no capability", "GET %s/status/{jobId}" % base, {"jobId": a.request_id}, {}),
              ("request history list", "GET %s/analysis/requests" % base, None, {}),
              ("request read", "GET %s/analysis/requests/{requestId}" % base, {"requestId": a.request_id}, {})]
    report = {"zip": os.path.basename(a.zip), "tenant": a.tenant, "request_id": a.request_id,
              "compose": {"ms": round(compose_ms), "aws_calls": compose_calls}, "routes": []}
    print("compose_ports + build_boundary: %d ms, %d AWS calls" % (compose_ms, compose_calls))
    for label, route, params, extra in routes:
        for attempt in range(a.repeat):
            event = {"routeKey": route, "headers": dict(headers, **extra),
                     "queryStringParameters": {"selected_tenant": a.tenant}}
            if params:
                event["pathParameters"] = params
            mark = len(CALLS)
            prof = cProfile.Profile()
            t0 = time.perf_counter()
            prof.enable()
            answer = boundary.handle(event)
            prof.disable()
            wall = (time.perf_counter() - t0) * 1000.0
            calls = CALLS[mark:]
            shapes = collections.OrderedDict()
            for c in calls:
                k = "%s %s %s" % (c["service"], c["op"], c["target"])
                s = shapes.setdefault(k, {"count": 0, "ms": 0.0})
                s["count"] += 1
                s["ms"] += c["ms"]
            stats = pstats.Stats(prof)
            fns = []
            for (path, line, fn), (cc, nc, tt, ct, callers) in stats.stats.items():
                if path.startswith(extract):
                    fns.append((ct * 1000.0, nc, "%s:%d %s" % (os.path.relpath(path, extract), line, fn)))
            fns.sort(reverse=True)
            size = len(json.dumps(answer, default=str))
            http = answer.get("statusCode") if isinstance(answer, dict) else None
            if isinstance(answer, dict) and isinstance(answer.get("body"), str):
                answer = json.loads(answer["body"])
            data = answer.get("data")
            # A served answer carries `data` (the status route's data IS the status); a refusal carries `status`.
            status = answer.get("status") or (data if isinstance(data, dict) and "state" in data else {})
            answer = dict(answer, ok=answer.get("ok", "data" in answer))
            row = {"route": label, "attempt": attempt + 1, "http": http, "ok": answer.get("ok"), "state": status.get("state"),
                   "reason": status.get("public_reason_code"), "wall_ms": round(wall), "response_bytes": size,
                   "items": len(data["items"]) if isinstance(data, dict) and isinstance(data.get("items"), list) else None,
                   "aws_calls": len(calls), "aws_ms": round(sum(c["ms"] for c in calls)),
                   "distinct_keys": len({(c["target"], c["key"]) for c in calls if c["key"]}),
                   "keyed_calls": sum(1 for c in calls if c["key"]),
                   "by_shape": {k: {"count": v["count"], "ms": round(v["ms"])} for k, v in shapes.items()},
                   "top_functions": [{"cum_ms": round(ms), "calls": nc, "fn": f} for ms, nc, f in fns[:14]]}
            report["routes"].append(row)
            print("\n%s #%d: http=%s ok=%s state=%s reason=%s wall=%d ms aws=%d calls %d ms items=%s bytes=%d" % (
                label, attempt + 1, http, row["ok"], row["state"], row["reason"], row["wall_ms"], row["aws_calls"],
                row["aws_ms"], row["items"], size))
            for k, v in sorted(row["by_shape"].items(), key=lambda kv: -kv[1]["ms"]):
                print("    %5d ms  x%-4d %s" % (v["ms"], v["count"], k))
            for f in row["top_functions"][:8]:
                print("    fn %6d ms x%-5d %s" % (f["cum_ms"], f["calls"], f["fn"]))
    json.dump(report, open(a.out, "w", encoding="utf-8"), indent=1)
    print("\nwrote", a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
