"""irpt-performance-adapter, the retained-report reopen and the public codes, run on a BEFORE and an AFTER bundle (row IRPT_BCKEND-S247).

Usage: python retained_reopen_before_after.py <aws.cmd> <before bundle dir> <after bundle dir>
       (each dir is an adapter zip extracted flat: the live artifact from `lambda get-function`, a candidate, or the deployed bytes)

LOCAL, service level (not HTTP): each bundle's own runtime._build() composes the retained Performance service with the live
function's environment and this session's credentials. Two things differ from the served path and both are stated in the output:
  - `authorize` is a stub that returns True (the question here is what the REOPEN returns, not who may ask);
  - the vendor transport factory is replaced by a stub that raises the bundle's own VendorEgressRefused, so NO vendor call can
    happen whatever the durable-use table holds.
For each retained non-49F Performance report in opal-data-irpt (read from S3: owner, account set, window, provider), the service
is asked for the same firm, account set and window. Printed per bundle: reopened (and the provider of what came back) or the
refusal's class and the PUBLIC code the bundle's boundary gives it. Then a fresh request for a window no report covers, per firm.
Reads only: S3 GetObject / ListObjectsV2 and DynamoDB GetItem. Nothing is written (a fresh path that would persist is unreachable:
the stub refuses before any calculation).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

PROBE = r'''
import json, os, sys
bundle = sys.argv[1]
cases = json.loads(os.environ["AB_CASES"])
sys.path.insert(0, bundle)
import entry, runtime, transport
captured = {}
_orig = entry.build_entry
def _capture(service):
    captured["service"] = service
    return _orig(service)
entry.build_entry = _capture
import installed
installed.entry = entry
boundary = runtime._build()
service = captured["service"]
def refusing_factory(request, mapping):
    raise transport.VendorEgressRefused("local harness: vendor egress is refused by construction")
service.transport_factory = refusing_factory
out = []
for c in cases:
    principal = {"firm_id": c["firm_id"], "principal_id": "local-harness"}
    owner = {**principal, "account_ids": list(c["account_ids"])}
    scope = {"resolved_scope": {"scope_ids": list(c["account_ids"])}, "selection": c.get("selection") or {},
             "verified_request_firm_id": c.get("verified_request_firm_id"), "permitted_account_set": list(c["account_ids"])}
    row = {"case": c["name"]}
    try:
        ans = service.compute(scope, c["start"], c["end"], principal=principal, owner=owner, authorize=lambda p, o: True)
        rep = ans.get("report") or {}
        row.update(outcome="REOPENED/SERVED", provider=(rep.get("lineage") or {}).get("provider"),
                   report_id=(ans.get("retained_ref") or {}).get("report_id", "")[:16])
    except Exception as exc:
        row.update(outcome="REFUSED", exception=type(exc).__name__, text=str(exc)[:90],
                   public_code=boundary.public_reason_for(exc))
    out.append(row)
print("AB_JSON " + json.dumps(out))
'''


def main() -> None:
    awscmd, before, after = sys.argv[1:4]
    import boto3

    s3 = boto3.client("s3", region_name="us-east-1")
    cases = []
    for firm in ("inflection", "cottonwood"):
        resp = s3.list_objects_v2(Bucket="opal-data-irpt", Prefix="irpt/%s/platinum/performance_reports/" % firm)
        for o in resp.get("Contents", []):
            rec = json.loads(s3.get_object(Bucket="opal-data-irpt", Key=o["Key"])["Body"].read())
            req = (rec.get("provenance") or {}).get("request") or {}
            cases.append({"name": "reopen %s %s (provider %s)" % (firm, o["Key"].rsplit("/", 1)[-1][:16],
                                                                 ((rec.get("report") or {}).get("lineage") or {}).get("provider")),
                          "firm_id": (rec.get("owner") or {}).get("firm_id"), "account_ids": req.get("account_ids"),
                          "start": req.get("start"), "end": req.get("end"), "selection": req.get("selection")})
    print("retained non-49F Performance reports found: %d" % len(cases))
    # POSITIVE CONTROL: the newest 49 Financial report on the holdings basis must still reopen on both bundles.
    control = None
    pag = s3.get_paginator("list_objects_v2")
    objs = [o for page in pag.paginate(Bucket="opal-data-irpt", Prefix="irpt/49financial/platinum/performance_reports/")
            for o in page.get("Contents", [])]
    for o in sorted(objs, key=lambda x: x["LastModified"], reverse=True):
        rec = json.loads(s3.get_object(Bucket="opal-data-irpt", Key=o["Key"])["Body"].read())
        if ((rec.get("report") or {}).get("lineage") or {}).get("provider") == "OPAL_HOLDINGS":
            req = (rec.get("provenance") or {}).get("request") or {}
            control = {"name": "CONTROL reopen 49financial %s (provider OPAL_HOLDINGS)" % o["Key"].rsplit("/", 1)[-1][:16],
                       "firm_id": (rec.get("owner") or {}).get("firm_id"), "account_ids": req.get("account_ids"),
                       "start": req.get("start"), "end": req.get("end"), "selection": req.get("selection")}
            break
    print("49 Financial retained reports listed: %d; holdings-basis control found: %s" % (len(objs), control is not None))
    for c in list(cases):
        cases.append({"name": "fresh %s, a window no report covers" % c["firm_id"], "firm_id": c["firm_id"],
                      "account_ids": c["account_ids"], "start": "1999-01-04", "end": "1999-02-01", "selection": c.get("selection")})
    if control is not None:
        cases.append(control)
    seen, uniq = set(), []
    for c in cases:
        key = (c["name"].split(" ")[0], c["firm_id"], tuple(c["account_ids"] or []), c["start"], c["end"])
        if key not in seen:
            seen.add(key)
            uniq.append(c)
    cfg = json.loads(subprocess.run(["cmd", "/c", awscmd, "lambda", "get-function-configuration", "--function-name",
                                     "irpt-performance-adapter", "--output", "json"], capture_output=True, text=True, check=True).stdout)
    results = {}
    for label, d in (("BEFORE", before), ("AFTER", after)):
        env = dict(os.environ)
        for k, v in ((cfg.get("Environment") or {}).get("Variables") or {}).items():
            env[k] = v.replace("/var/task", d)
        env["AWS_DEFAULT_REGION"] = env["AWS_REGION"] = "us-east-1"
        env["AB_CASES"] = json.dumps(uniq)
        p = subprocess.run([sys.executable, "-c", PROBE, d], capture_output=True, text=True, env=env, timeout=600)
        line = [ln for ln in p.stdout.splitlines() if ln.startswith("AB_JSON ")]
        results[label] = json.loads(line[-1][8:]) if line else [{"case": "PROBE FAILED", "outcome": (p.stderr or p.stdout)[-700:]}]
    for b, a in zip(results["BEFORE"], results["AFTER"]):
        def show(r):
            if r.get("outcome") == "REFUSED":
                return "REFUSED %s -> %s" % (r.get("exception"), r.get("public_code"))
            return "%s provider=%s" % (r.get("outcome"), r.get("provider"))
        print("  %-62s BEFORE %-58s AFTER %s" % (b.get("case", "")[:62], show(b)[:58], show(a)))
    if len(results["BEFORE"]) != len(results["AFTER"]):
        print("RAW", json.dumps(results)[:1500])


if __name__ == "__main__":
    main()
