#!/usr/bin/env python3
"""IRPT_BCKEND-S157 -- ONE corrected Cottonwood Performance read, by direct IAM invoke (no walk principal).

    python cot_direct_read.py <precheck|read|reopen> <out.json>

The same boundary and synthetic internal viewer as reopen_authz_arm.py (V1, reopen-arm-1@opal.test, the edge's
trusted header set), on the COT plan's ONE account and window:
  precheck  plan OFF: expect DEPENDENCY_UNAVAILABLE (the adapter's VendorEgressRefused), no report, no claim
  read      plan ARMED: the ONE use -- READY/PARTIAL with a retained report, or a named refusal; no retry
  reopen    after the read: the same retained report, no vendor call
It records outcomes, refs and dates only -- never a return value, a report body or a client name.
"""
from __future__ import annotations

import datetime as dt
import json
import sys

import boto3

FIRM, ACCOUNT = "cottonwood", "acc_81d92b2b7e971a76bac96cea"
WINDOW = ("2026-01-01", "2026-09-22")
ROUTE = "GET /api/scoped/investor-reporting/performance/{accountSetId}"
SELECT_ROUTE = "POST /api/scoped/investor-reporting/selections"
V1 = {"x-origin-verify": "cloudfront", "x-user-role": "user", "x-contract-version": "v1",
      "x-user-tier": "internal", "x-firm-id": "opal-capital",
      "x-user-email": "reopen-arm-1@opal.test", "x-user-name": "reopen arm 1"}
LAMBDA = boto3.client("lambda", region_name="us-east-1")


def _invoke(function, event):
    r = LAMBDA.invoke(FunctionName=function, Payload=json.dumps(event).encode())
    body = json.loads(r["Payload"].read())
    if isinstance(body.get("body"), str):
        body = json.loads(body["body"])
    return r.get("FunctionError"), body


def select():
    event = {"version": "2.0", "routeKey": SELECT_ROUTE, "headers": dict(V1, **{"content-type": "application/json"}),
             "queryStringParameters": {"selected_tenant": FIRM},
             "body": json.dumps({"scope_kind": "ACCOUNT", "scope_ids": [ACCOUNT]}), "isBase64Encoded": False}
    _, body = _invoke("irpt-directory-search", event)
    data = body.get("data") if isinstance(body.get("data"), dict) else {}
    return data.get("account_set_id")


def read(selection):
    event = {"version": "2.0", "routeKey": ROUTE, "headers": dict(V1), "pathParameters": {"accountSetId": selection},
             "queryStringParameters": {"start": WINDOW[0], "end": WINDOW[1], "selected_tenant": FIRM}}
    started = dt.datetime.now(dt.timezone.utc)
    error, body = _invoke("irpt-performance-adapter", event)
    status = body.get("status") or {}
    data = body.get("data") if isinstance(body.get("data"), dict) else {}
    dates = data.get("dates") or {}
    series = ((data.get("returns") or {}).get("daily_cumulative_series") or [])
    return {"at": started.isoformat(), "function_error": error, "state": status.get("state"),
            "reason": status.get("public_reason_code"), "retained_ref": data.get("retained_ref"),
            "report_id": (data.get("revision") or {}).get("reportId") or data.get("report_id"),
            "requested": [dates.get("requested_start"), dates.get("requested_end")],
            "actual": [dates.get("actual_start"), dates.get("actual_end")],
            "series_points": len(series), "series_first": series[0].get("date") if series else None,
            "series_last": series[-1].get("date") if series else None}


def main(argv):
    if len(argv) != 3 or argv[1] not in ("precheck", "read", "reopen"):
        raise SystemExit(__doc__)
    selection = select()
    if not selection:
        raise SystemExit("STOP: the selection was refused")
    out = {"phase": argv[1], "firm": FIRM, "account": ACCOUNT, "selection": selection, "window": list(WINDOW),
           "result": read(selection)}
    json.dump(out, open(argv[2], "w", encoding="utf-8"), indent=1)
    print(json.dumps(out["result"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
