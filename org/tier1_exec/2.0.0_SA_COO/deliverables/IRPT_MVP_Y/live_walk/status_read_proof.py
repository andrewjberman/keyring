"""Hops 8-9 offline: the served irpt-status code answers an Opal viewer's reads of the job phase 2 took to READY.

    python status_read_proof.py --zip <irpt-status.zip> --state <phase-2 out dir> [--overlay <dir>]

The served zip is extracted fresh and FIRST on sys.path (`--overlay` copies fixed files over it). The real
`status_installed.compose_ports` + `build_boundary` + served Entry handle four API-Gateway-shaped GETs, with
verified-edge Opal headers and selected_tenant from the job:
1. sections: GET .../analysis/{jobId}/sections (hop 8);
2. job: GET .../status/{jobId};
3. history: GET .../analysis/requests (hop 9);
4. read: GET .../analysis/requests/{requestId}.
Clients are the phase-2 world (live reads, captured writes). The module census proves every first-party module came from
the extract.
"""
import argparse
import json
import os
import shutil
import sys
import tempfile
import time
import zipfile

import boto3

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import readthrough as rt  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--state", required=True)
    ap.add_argument("--overlay")
    ap.add_argument("--viewer", default="irpt-uiwalk-1790442753@opal.test")
    ap.add_argument("--reads-out", help="write every read call (for the IAM pairs)")
    a = ap.parse_args(argv)
    extract = tempfile.mkdtemp(prefix="irpt-status-proof-")
    zipfile.ZipFile(a.zip).extractall(extract)
    overlaid = []
    for name in sorted(os.listdir(a.overlay)) if a.overlay else []:
        if os.path.isfile(os.path.join(a.overlay, name)):
            shutil.copyfile(os.path.join(a.overlay, name), os.path.join(extract, name))
            overlaid.append(name)
    sys.path.insert(0, extract)
    os.environ.setdefault("IRPT_DIRECTORY_BUCKET_MAP", json.dumps({"49financial": "opal-data-bd", "cottonwood": "opal-data-cot", "inflection": "opal-data-inf"}))
    print("extract", extract, "| overlay", overlaid or "none")

    job = json.load(open(os.path.join(a.state, "job.json"), encoding="utf-8"))
    writes = rt.Writes()
    seeded = json.load(open(os.path.join(a.state, "seeded_users.json"), encoding="utf-8"))
    ddb = rt.Dynamo(boto3.client("dynamodb", region_name="us-east-1"), writes, seeded)
    s3 = rt.S3(boto3.client("s3", region_name="us-east-1"), writes)
    rt.load(os.path.join(a.state, "state.json"), ddb, s3)

    import status_installed as si
    env = {si.REQUESTS_TABLE_ENV: "irpt-requests", si.JOBS_TABLE_ENV: "irpt-jobs"}
    ports = si.compose_ports(clients={"dynamodb": ddb, "table": rt.Table(ddb, "irpt-requests"), "s3": s3},
                             clock=time.time, environ=env)
    boundary = si.build_boundary(ports)
    headers = {"x-contract-version": "v1", "x-origin-verify": "cloudfront", "x-user-email": a.viewer,
               "x-user-role": "admin", "x-user-type": "Dev", "x-firm-id": "opal-capital", "x-user-name": "Offline Proof Viewer"}
    base = "/api/scoped/investor-reporting"
    rid, tenant = job["request_id"], job["tenant"]
    calls = [("sections (hop 8)", "GET %s/analysis/{jobId}/sections" % base, {"jobId": rid}),
             ("job status", "GET %s/status/{jobId}" % base, {"jobId": rid}),
             ("history (hop 9)", "GET %s/analysis/requests" % base, None),
             ("request read (hop 9)", "GET %s/analysis/requests/{requestId}" % base, {"requestId": rid})]
    results = []
    for label, route, params in calls:
        event = {"routeKey": route, "headers": headers, "queryStringParameters": {"selected_tenant": tenant}}
        if params:
            event["pathParameters"] = params
        answer = boundary.handle(event)
        status = answer.get("status") or {}
        data = answer.get("data")
        summary = sorted(data)[:10] if isinstance(data, dict) else data
        if isinstance(data, dict) and "sections" in data:
            summary = {"sections": len(data["sections"]), "keys": sorted(data)[:10]}
        ok = isinstance(data, dict) and answer.get("ok") is not False
        results.append(ok)
        print("%-22s %-8s state=%-12s reason=%-22s data=%s" % (label, "OK" if ok else "REFUSED", status.get("state"),
              status.get("public_reason_code"), json.dumps(summary, default=str)[:260]))
    loaded = {m.__name__: getattr(m, "__file__", None) for m in list(sys.modules.values()) if getattr(m, "__file__", None)}
    first_party = {n: f for n, f in loaded.items() if os.path.exists(os.path.join(extract, n + ".py"))}
    outside = {n: f for n, f in first_party.items() if not os.path.samefile(os.path.dirname(f), extract)}
    print("\nMODULE CENSUS: %d first-party modules loaded, %d from the extract, %d from elsewhere %s"
          % (len(first_party), len(first_party) - len(outside), len(outside), sorted(outside) or ""))
    print("CAPTURED WRITES:", len(writes.log))
    distinct = sorted({(r["kind"], r.get("table") or r.get("bucket"), r.get("index") or "",
                        "/".join((r.get("key") or "").split("/")[:4]) if isinstance(r.get("key"), str) else "",
                        r.get("version", "")) for r in writes.reads}, key=str)
    print("READS MADE (%d calls, %d distinct shapes):" % (len(writes.reads), len(distinct)))
    for d in distinct:
        print("   ", d)
    if a.reads_out:
        json.dump(writes.reads, open(a.reads_out, "w", encoding="utf-8"), default=str)
    print("RESULT: %d of %d reads answered" % (sum(results), len(results)))
    return 0 if all(results) and not outside else 1


if __name__ == "__main__":
    sys.exit(main())
