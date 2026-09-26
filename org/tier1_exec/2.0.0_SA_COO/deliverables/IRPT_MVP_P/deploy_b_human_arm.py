#!/usr/bin/env python3
"""Export deploy (B), the human-read arm (CRO half @f8fc5ff21d + CTO half @b70ede1756): one human Performance request
per firm -- 49F, Cottonwood, and Inflection with its plan UNARMED (plan b is spent) -- before D1 and after D2, compared
on status, reason code and, for an answer with data, the section count and completeness. Any difference is STOP and
roll back in reverse (D3, D2, D1).

    python deploy_b_human_arm.py <before|after> <out.json>
    python deploy_b_human_arm.py compare <before.json> <after.json>

Invokes irpt-performance-adapter directly (IAM-only; the same boundary the edge feeds) with the edge's trusted header
set for a synthetic internal Opal subject, the path API Gateway sends. No render token, so no render port answers.
Records outcomes only -- no report body. A 49F answer retains a report as any human read does (named in the ledger).
"""
from __future__ import annotations

import datetime as dt
import json
import sys

import boto3

ROUTE = "GET /api/scoped/investor-reporting/performance/{accountSetId}"
CASES = [  # (firm, ONE account) -- selected fresh each run through the real selection route (irpt-directory-search),
    # because a stored selection goes stale at each directory refresh ("selection binding changed; select again").
    # The SELECTION# row it writes is content-addressed and identity-free (K3's shape); the same directory gives the
    # same id before and after.
    ("49financial", "acc_0030c178052a2db50d683027"),   # 200 PARTIAL through the served route at 03:2xZ
    ("cottonwood", "acc_d486fc9455d6b2aa18e13af1"),
    ("inflection", "acc_5510a3054a409d548a12c57d"),    # plan b SPENT 03:20:31Z -> the gate refuses: "unarmed"
]
SELECT_ROUTE = "POST /api/scoped/investor-reporting/selections"
HEADERS = {"x-origin-verify": "cloudfront", "x-user-email": "deploy-b-arm@opal.test", "x-user-name": "deploy B arm",
           "x-user-role": "user", "x-user-tier": "internal", "x-firm-id": "opal-capital",
           "x-contract-version": "v1"}


def select(firm, account):
    event = {"version": "2.0", "routeKey": SELECT_ROUTE, "headers": dict(HEADERS, **{"content-type": "application/json"}),
             "queryStringParameters": {"selected_tenant": firm},
             "body": json.dumps({"scope_kind": "ACCOUNT", "scope_ids": [account]}), "isBase64Encoded": False}
    r = boto3.client("lambda").invoke(FunctionName="irpt-directory-search", Payload=json.dumps(event).encode())
    body = json.loads(r["Payload"].read())
    if isinstance(body.get("body"), str):
        body = json.loads(body["body"])
    sel = ((body.get("data") or {}) if isinstance(body.get("data"), dict) else {}).get("account_set_id")
    if not sel:
        raise SystemExit("STOP: selection refused for %s: %s" % (firm, json.dumps(body)[:300]))
    return sel


def outcome(firm, account):
    sel = select(firm, account)
    event = {"version": "2.0", "routeKey": ROUTE, "headers": dict(HEADERS),
             "pathParameters": {"accountSetId": sel},
             "queryStringParameters": {"start": "2026-01-01", "end": "2026-09-24", "selected_tenant": firm}}
    r = boto3.client("lambda").invoke(FunctionName="irpt-performance-adapter", Payload=json.dumps(event).encode())
    body = json.loads(r["Payload"].read())
    if isinstance(body.get("body"), str):
        body = json.loads(body["body"])
    status = body.get("status") or {}
    data = body.get("data") if isinstance(body.get("data"), dict) else None
    return {"firm": firm, "account_set_id": sel, "function_error": r.get("FunctionError"), "ok": body.get("ok"),
            "state": status.get("state"), "reason": status.get("public_reason_code"),
            "sections": sorted(data.keys()) if data else None,
            "section_count": len(data) if data else 0}


def main(argv):
    if argv[1] == "compare":
        a, b = (json.load(open(p, encoding="utf-8"))["results"] for p in argv[2:4])
        diffs = [(x["firm"], k, x[k], y[k]) for x, y in zip(a, b) for k in ("function_error", "ok", "state", "reason",
                                                                             "sections", "section_count") if x[k] != y[k]]
        print("COMPARE %d firms: %s" % (len(a), "IDENTICAL" if not diffs else "DIFFERENT %s" % diffs))
        raise SystemExit(0 if not diffs else 3)
    results = [outcome(f, s) for f, s in CASES]
    for x in results:
        print("%s %s: ok=%s state=%s reason=%s sections=%d fnerr=%s" % (argv[1], x["firm"], x["ok"], x["state"],
                                                                         x["reason"], x["section_count"],
                                                                         x["function_error"]))
    with open(argv[2], "w", encoding="utf-8", newline="\n") as f:
        json.dump({"at": dt.datetime.now(dt.timezone.utc).isoformat(), "phase": argv[1], "results": results}, f,
                  indent=1)


if __name__ == "__main__":
    main(sys.argv)
