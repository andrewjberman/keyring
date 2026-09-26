#!/usr/bin/env python3
"""P-REOPEN-01 (CTO 101429) -- the four arms of the reopen-authorization half, before and after the adapter deploy.

    python reopen_authz_arm.py <before|after> <out.json>
    python reopen_authz_arm.py compare <before.json> <after.json>

It invokes irpt-performance-adapter directly (IAM only, on the same boundary the edge feeds) with the edge's
trusted header set, as deploy_b_human_arm.py does. The three synthetic subjects are:
  V1  reopen-arm-1@opal.test  internal Opal viewer (live grant over every firm)
  V2  reopen-arm-2@opal.test  a SECOND internal Opal viewer -- the same live grant, a different principal
  V0  a 49F advisor subject whose advisor id owns no account -- no grant over the account
One 49F account (acc_0030c178..) and one window ending PAST the engine frontier (2026-01-01..2026-09-26; the
frontier is 09-25).

The arms, per phase:
  (1) V2 reopens the report V1 computed: after = the same retained_ref and the same data sha256
      (before = OBJECT_NOT_COVERED, the defect, as the negative control)
  (2) V0 is refused and receives no data
  (3) the retained report's owner row (irpt-requests REPORT#<id>#<rev>) is unchanged
  (4) V1's before and after reads of the past-frontier window: the same ref and data sha256
The after phase adds ONE fresh window (01-01..09-19) as V1, so the phase-timing line (ruling A) fires once.
It records outcomes, refs and digests only -- never a report body or a principal id in clear.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import sys

import boto3

FIRM, ACCOUNT = "49financial", "acc_0030c178052a2db50d683027"
WINDOW = ("2026-01-01", "2026-09-26")
FRESH = ("2026-01-01", "2026-09-19")
ROUTE = "GET /api/scoped/investor-reporting/performance/{accountSetId}"
SELECT_ROUTE = "POST /api/scoped/investor-reporting/selections"
BASE = {"x-origin-verify": "cloudfront", "x-user-role": "user", "x-contract-version": "v1"}
OPAL = {"x-user-tier": "internal", "x-firm-id": "opal-capital"}
SUBJECTS = {
    "V1": dict(BASE, **OPAL, **{"x-user-email": "reopen-arm-1@opal.test", "x-user-name": "reopen arm 1"}),
    "V2": dict(BASE, **OPAL, **{"x-user-email": "reopen-arm-2@opal.test", "x-user-name": "reopen arm 2"}),
    "V0": dict(BASE, **{"x-user-email": "reopen-arm-0@opal.test", "x-user-name": "reopen arm 0",
                        "x-user-tier": "partner", "x-firm-id": FIRM, "x-user-type": "Advisor",
                        "x-advisor-id": "ADV-REOPEN-ARM-NONE", "x-advisor-role": ""}),
}
LAMBDA = boto3.client("lambda", region_name="us-east-1")


def _invoke(function, event):
    r = LAMBDA.invoke(FunctionName=function, Payload=json.dumps(event).encode())
    body = json.loads(r["Payload"].read())
    if isinstance(body.get("body"), str):
        body = json.loads(body["body"])
    return r.get("FunctionError"), body


def select(subject):
    event = {"version": "2.0", "routeKey": SELECT_ROUTE,
             "headers": dict(SUBJECTS[subject], **{"content-type": "application/json"}),
             "queryStringParameters": {"selected_tenant": FIRM},
             "body": json.dumps({"scope_kind": "ACCOUNT", "scope_ids": [ACCOUNT]}), "isBase64Encoded": False}
    _, body = _invoke("irpt-directory-search", event)
    data = body.get("data") if isinstance(body.get("data"), dict) else {}
    return data.get("account_set_id")


def read(subject, selection, window):
    event = {"version": "2.0", "routeKey": ROUTE, "headers": dict(SUBJECTS[subject]),
             "pathParameters": {"accountSetId": selection},
             "queryStringParameters": {"start": window[0], "end": window[1], "selected_tenant": FIRM}}
    started = dt.datetime.now(dt.timezone.utc)
    error, body = _invoke("irpt-performance-adapter", event)
    status = body.get("status") or {}
    data = body.get("data") if isinstance(body.get("data"), dict) else None
    ref = (data or {}).get("retained_ref")
    report = {k: v for k, v in (data or {}).items() if k != "retained_ref"}
    return {"subject": subject, "window": list(window), "at": started.isoformat(), "function_error": error,
            "ok": body.get("ok"), "state": status.get("state"), "reason": status.get("public_reason_code"),
            "retained_ref": ref, "data_sha256": hashlib.sha256(json.dumps(report, sort_keys=True).encode()).hexdigest()
            if data else None, "actual_end": ((data or {}).get("dates") or {}).get("actual_end")}


def owner_row(ref):
    """The retained report's index row owner, as a digest (the principal id never printed)."""
    if not ref:
        return None
    table = boto3.resource("dynamodb", region_name="us-east-1").Table("irpt-requests")
    key = "REPORT#%s#%s" % (ref["report_id"], ref["revision"])
    for tenant in (FIRM, "F-49F", "49F"):
        item = table.get_item(Key={"tenant": tenant, "request_revision": key}, ConsistentRead=True).get("Item")
        if item:
            owner = json.loads(json.dumps(item["owner"], default=str))
            return {"tenant": tenant, "owner_sha256": hashlib.sha256(json.dumps(owner, sort_keys=True).encode())
                    .hexdigest(), "owner_keys": sorted(owner), "owner_accounts": owner.get("account_ids"),
                    "principal_sha12": hashlib.sha256(str(owner.get("principal_id")).encode()).hexdigest()[:12]}
    return {"tenant": None, "owner_sha256": None}


def run(phase):
    selection = select("V1")
    if not selection:
        raise SystemExit("STOP: selection refused for V1")
    rows = {"selection": selection, "V1": read("V1", selection, WINDOW)}
    rows["V2"] = read("V2", selection, WINDOW)
    rows["V0_selection"] = select("V0")
    rows["V0"] = read("V0", selection, WINDOW)
    rows["owner"] = owner_row(rows["V1"]["retained_ref"])
    if phase == "after":
        rows["fresh"] = read("V1", selection, FRESH)
    return rows


def compare(before, after):
    checks = []
    b1, a1, a2, a0 = before["V1"], after["V1"], after["V2"], after["V0"]
    checks.append(("(1) V2 reopens V1's report", a2["ok"] is True and a2["retained_ref"] == a1["retained_ref"]
                   and a2["data_sha256"] == a1["data_sha256"]))
    checks.append(("(1) negative control: before, V2 answered OBJECT_NOT_COVERED", before["V2"]["reason"] ==
                   "OBJECT_NOT_COVERED" and before["V2"]["ok"] is False))
    checks.append(("(2) V0 refused, no data", a0["ok"] is False and a0["data_sha256"] is None))
    checks.append(("(3) owner row unchanged", before["owner"] == after["owner"] and after["owner"]["owner_sha256"]))
    checks.append(("(4) past-frontier read identical before/after", b1["ok"] is True and a1["ok"] is True
                   and b1["retained_ref"] == a1["retained_ref"] and b1["data_sha256"] == a1["data_sha256"]))
    for name, ok in checks:
        print("%s %s" % ("PASS" if ok else "FAIL", name))
    return all(ok for _, ok in checks)


def main(argv):
    if argv[1] == "compare":
        before, after = (json.load(open(p, encoding="utf-8"))["rows"] for p in argv[2:4])
        raise SystemExit(0 if compare(before, after) else 3)
    rows = run(argv[1])
    for key in ("V1", "V2", "V0") + (("fresh",) if argv[1] == "after" else ()):
        r = rows[key]
        print("%s %s %s..%s ok=%s state=%s reason=%s end=%s ref=%s data=%s" % (
            argv[1], key, r["window"][0], r["window"][1], r["ok"], r["state"], r["reason"], r["actual_end"],
            (r["retained_ref"] or {}).get("report_id"), (r["data_sha256"] or "")[:12]))
    print("%s owner %s" % (argv[1], json.dumps(rows["owner"])))
    with open(argv[2], "w", encoding="utf-8", newline="\n") as f:
        json.dump({"at": dt.datetime.now(dt.timezone.utc).isoformat(), "phase": argv[1], "rows": rows}, f, indent=1)


if __name__ == "__main__":
    main(sys.argv)
