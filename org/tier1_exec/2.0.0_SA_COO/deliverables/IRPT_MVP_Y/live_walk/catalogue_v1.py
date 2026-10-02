#!/usr/bin/env python3
"""Leg V1 of irpt-generate-catalogue-20261002: the served comparison catalogue read as svc-irpt-analysis.

    python catalogue_v1.py <out.json>

One login (the password read by NAME into memory, never printed). GET analysis/comparisons three times for the
principal's own firm, then once for a firm outside its reach; every call is a GET, nothing is created and no vendor is
reached. Each call is matched to the irpt-ycharts-generate invocation whose START falls inside its client window, so
the function's own Duration sits beside it. Recorded: HTTP status, state, reason, catalogue_version, entry count by
name_source, client and server ms. Never an entry's key or label. ASCII only.
"""
import collections
import json
import os
import re
import sys
import time

import boto3

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svc_principal as sp  # noqa: E402

PATH = "/api/scoped/investor-reporting/analysis/comparisons?selected_tenant="


def main(out):
    log = []
    password = sp._sm().get_secret_value(SecretId=sp.SECRET)["SecretString"]
    code, login = sp._call("POST", "/auth/login", {"email": sp.EMAIL, "password": password},
                           {"Content-Type": "application/json"}, log)
    del password
    token = login.get("accessToken") if isinstance(login, dict) else None
    print("login HTTP %s token %s" % (code, bool(token)))
    if not token:
        return 1
    h = {"Authorization": "Bearer " + token, "X-Contract-Version": "v1"}
    calls = []
    for label, tenant in (("own firm #1", "cottonwood"), ("own firm #2", "cottonwood"), ("own firm #3", "cottonwood"),
                          ("foreign firm", "inflection")):
        time.sleep(3)
        start = time.time()
        code, resp = sp._call("GET", PATH + tenant, None, h, log)
        end = time.time()
        data = resp.get("data") if isinstance(resp, dict) else None
        status = (resp.get("status") if isinstance(resp, dict) else None) or {}
        entries = data.get("entries") if isinstance(data, dict) else None
        calls.append({"call": label, "http": code, "state": status.get("state"),
                      "reason": status.get("public_reason_code"),
                      "catalogue_version": data.get("catalogue_version") if isinstance(data, dict) else None,
                      "entries": len(entries) if isinstance(entries, list) else None,
                      "by_source": dict(collections.Counter(e.get("name_source") for e in entries))
                      if isinstance(entries, list) else None,
                      "start": start, "end": end, "client_ms": round((end - start) * 1000)})
    del token
    time.sleep(20)
    logs = boto3.client("logs", region_name="us-east-1")
    events = []
    for page in logs.get_paginator("filter_log_events").paginate(
            logGroupName="/aws/lambda/irpt-ycharts-generate", startTime=int(calls[0]["start"] * 1000) - 2000,
            endTime=int(calls[-1]["end"] * 1000) + 15000):
        events.extend(page["events"])
    starts, reports = {}, {}
    for e in events:
        m = re.match(r"(START|REPORT) RequestId: ([0-9a-f-]+)", e["message"])
        if m and m.group(1) == "START":
            starts[m.group(2)] = e["timestamp"] / 1000.0
        elif m:
            reports[m.group(2)] = e["message"]
    for c in calls:
        hits = [r for r, t in starts.items() if c["start"] - 0.5 <= t <= c["end"]]
        c["invocations_in_window"] = len(hits)
        if len(hits) == 1 and hits[0] in reports:
            msg = reports[hits[0]]
            c["server_ms"] = round(float(re.search(r"\tDuration: ([\d.]+) ms", msg).group(1)))
            init = re.search(r"Init Duration: ([\d.]+) ms", msg)
            c["init_ms"] = round(float(init.group(1))) if init else 0
        print("%-13s HTTP %s state %-11s reason %-14s version %-3s entries %-4s %s client %5d ms server %5s ms init %s"
              % (c["call"], c["http"], c["state"], c["reason"], c["catalogue_version"], c["entries"], c["by_source"],
                 c["client_ms"], c.get("server_ms"), c.get("init_ms")))
    json.dump({"at": sp._now(), "principal": sp.EMAIL, "calls": calls},
              open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
