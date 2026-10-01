#!/usr/bin/env python3
"""The SAME live reads of the two Analysis functions, run before and after a served move, for comparison.

    python served_reads_before_after.py <label> <out.json> [<tenant> <request-id> <report-id>]

One login as svc-irpt-analysis (allowedFirmIds cottonwood; an Opal subject, so an owner read of a Cottonwood request
is admitted). Every request is a GET, or a POST with an empty body that is refused before any write. Nothing is
created and no vendor is reached. The password is read by NAME into memory and never printed; tokens are redacted
in the log. What is recorded per call: HTTP status, `ok`, state, reason code, business date, and the response's
top-level and data keys (never a client's values). ASCII only.

irpt-status:           status-summary, status-job, request history, request read, analysis sections
irpt-ycharts-generate: POST analysis (empty body) for the own firm and for a FOREIGN firm (the service boundary)
"""
import json
import sys

import svc_principal as sp

BASE = "/api/scoped/investor-reporting/"


def shape(resp):
    if not isinstance(resp, dict):
        return {"non_json": str(resp)[:120]}
    status = resp.get("status") if isinstance(resp.get("status"), dict) else {}
    data = resp.get("data")
    out = {"ok": resp.get("ok"), "operation": resp.get("operation"), "state": status.get("state"),
           "reason": status.get("public_reason_code") or resp.get("message") or resp.get("error"),
           "business_date": (status.get("source_dates") or {}).get("business_date"),
           "actions": [a.get("action") for a in status.get("actions") or []],
           "top_keys": sorted(resp)}
    if isinstance(data, dict):
        out["data_keys"] = sorted(data)[:25]
        if out["state"] is None and "state" in data:  # a served answer carries its envelope inside `data`
            out["state"], out["reason"] = data.get("state"), data.get("public_reason_code")
            out["actions"] = [a.get("action") for a in data.get("actions") or [] if isinstance(a, dict)]
        for key in ("sections", "entries", "requests", "items"):
            if isinstance(data.get(key), list):
                out["count_" + key] = len(data[key])
    elif isinstance(data, list):
        out["data_len"] = len(data)
    return out


def main(argv):
    label, out = argv[1], argv[2]
    tenant = argv[3] if len(argv) > 3 else "cottonwood"
    request_id = argv[4] if len(argv) > 4 else "REQ-7ea49c2d9b27957d0ea8888f"
    report_id = argv[5] if len(argv) > 5 else "RPT-2e21b52edcb222205399100e026c2768"
    log = []
    password = sp._sm().get_secret_value(SecretId=sp.SECRET)["SecretString"]
    code, login = sp._call("POST", "/auth/login", {"email": sp.EMAIL, "password": password},
                           {"Content-Type": "application/json"}, log)
    del password
    token = login.get("accessToken") if isinstance(login, dict) else None
    print("%s | login HTTP %s token %s" % (label, code, bool(token)))
    if not token:
        return 1
    h = {"Authorization": "Bearer " + token, "X-Contract-Version": "v1", "Content-Type": "application/json"}
    q = "?selected_tenant=" + tenant
    probes = [
        ("irpt-status", "status-summary", "GET", "status" + q, None),
        ("irpt-status", "status-job", "GET", "status/%s%s" % (request_id, q), None),
        ("irpt-status", "request-history", "GET", "analysis/requests" + q, None),
        ("irpt-status", "request-read", "GET", "analysis/requests/%s%s" % (request_id, q), None),
        ("irpt-status", "sections-by-request", "GET", "analysis/%s/sections%s" % (request_id, q), None),
        ("irpt-status", "sections-by-report", "GET", "analysis/%s/sections%s" % (report_id, q), None),
        ("irpt-ycharts-generate", "analysis-own-firm", "POST", "analysis" + q, {}),
        ("irpt-ycharts-generate", "analysis-foreign-firm", "POST", "analysis?selected_tenant=inflection", {}),
    ]
    rows = []
    for function, name, method, path, body in probes:
        code, resp = sp._call(method, BASE + path, body, h, log)
        row = {"function": function, "probe": name, "http": code}
        row.update(shape(resp))
        rows.append(row)
        print("%-22s %-22s HTTP %s ok %s state %s reason %s date %s %s"
              % (function, name, code, row.get("ok"), row.get("state"), row.get("reason"), row.get("business_date"),
                 " ".join("%s=%s" % (k, row[k]) for k in row if k.startswith(("count_", "data_len")))))
    del token
    json.dump({"label": label, "at": sp._now(), "principal": sp.EMAIL, "rows": rows},
              open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
