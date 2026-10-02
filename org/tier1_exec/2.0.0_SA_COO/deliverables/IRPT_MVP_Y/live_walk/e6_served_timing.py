#!/usr/bin/env python3
"""E6 (CTO rulings batch 93 item 8): the served irpt-status reads timed IN REGION, each GET matched to its REPORT line.

    python e6_served_timing.py <tenant> <request-id> <out.json> [--repeat N]

One login as svc-irpt-analysis (the password read by NAME into memory, never printed). Every request is a GET to
irpt-status; nothing is created and no vendor is reached. Calls run one at a time with a gap, and each is matched to
the irpt-status invocation whose START falls inside the call's client window, so the function's own Duration (the
in-region server time) sits beside the client time. Recorded per call: route, HTTP status, state, reason, item count,
client ms, server ms, init ms, max memory. Never a client's values. ASCII only.
"""
import argparse
import json
import os
import re
import sys
import time

import boto3

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svc_principal as sp  # noqa: E402

BASE = "/api/scoped/investor-reporting/"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("tenant")
    ap.add_argument("request_id")
    ap.add_argument("out")
    ap.add_argument("--repeat", type=int, default=2)
    a = ap.parse_args(argv)
    log = []
    password = sp._sm().get_secret_value(SecretId=sp.SECRET)["SecretString"]
    code, login = sp._call("POST", "/auth/login", {"email": sp.EMAIL, "password": password},
                           {"Content-Type": "application/json"}, log)
    del password
    token = login.get("accessToken") if isinstance(login, dict) else None
    print("login HTTP %s token %s" % (code, bool(token)))
    if not token:
        return 1
    h = {"Authorization": "Bearer " + token, "X-Contract-Version": "v1", "Content-Type": "application/json"}
    q = "?selected_tenant=" + a.tenant
    probes = [("status read, dates capability", "status/%s%s" % (a.request_id, q), {"X-IRPT-Status-Dates": "prospect-v1"}),
              ("status read, no capability", "status/%s%s" % (a.request_id, q), {}),
              ("request history list", "analysis/requests" + q, {}),
              ("request read", "analysis/requests/%s%s" % (a.request_id, q), {})]
    calls = []
    for label, path, extra in probes:
        for attempt in range(a.repeat):
            time.sleep(3)
            start = time.time()
            code, resp = sp._call("GET", BASE + path, None, dict(h, **extra), log)
            end = time.time()
            data = resp.get("data") if isinstance(resp, dict) else None
            status = (resp.get("status") if isinstance(resp, dict) else None) or (
                data if isinstance(data, dict) and "state" in data else {})
            calls.append({"route": label, "attempt": attempt + 1, "http": code, "state": status.get("state"),
                          "reason": status.get("public_reason_code"),
                          "items": len(data["items"]) if isinstance(data, dict) and isinstance(data.get("items"), list) else None,
                          "start": start, "end": end, "client_ms": round((end - start) * 1000)})
    del token
    time.sleep(20)
    logs = boto3.client("logs", region_name="us-east-1")
    events = []
    for page in logs.get_paginator("filter_log_events").paginate(
            logGroupName="/aws/lambda/irpt-status", startTime=int(calls[0]["start"] * 1000) - 2000,
            endTime=int(calls[-1]["end"] * 1000) + 15000):
        events.extend(page["events"])
    starts = {}
    reports = {}
    for e in events:
        m = re.match(r"(START|REPORT) RequestId: ([0-9a-f-]+)", e["message"])
        if not m:
            continue
        if m.group(1) == "START":
            starts[m.group(2)] = e["timestamp"] / 1000.0
        else:
            reports[m.group(2)] = e["message"]
    used = set()
    for c in calls:
        hits = [r for r, t in starts.items() if c["start"] - 0.5 <= t <= c["end"] and r not in used]
        c["invocations_in_window"] = len(hits)
        if len(hits) == 1 and hits[0] in reports:
            msg = reports[hits[0]]
            used.add(hits[0])
            c["server_ms"] = round(float(re.search(r"\tDuration: ([\d.]+) ms", msg).group(1)))
            init = re.search(r"Init Duration: ([\d.]+) ms", msg)
            c["init_ms"] = round(float(init.group(1))) if init else 0
            c["max_memory_mb"] = int(re.search(r"Max Memory Used: (\d+)", msg).group(1))
        print("%-30s #%d HTTP %s state %-12s reason %-40s items %-4s client %6d ms server %6s ms init %4s in-window %d" % (
            c["route"], c["attempt"], c["http"], c["state"], c["reason"], c["items"], c["client_ms"],
            c.get("server_ms"), c.get("init_ms"), c["invocations_in_window"]))
    json.dump({"at": sp._now(), "principal": sp.EMAIL, "tenant": a.tenant, "request_id": a.request_id,
               "calls": calls}, open(a.out, "w", encoding="utf-8", newline="\n"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
