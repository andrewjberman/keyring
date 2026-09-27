"""The /analysis composition, proved WITHOUT a principal (CTO 101355): the deployed generate code, in-process.

    python offline_submit_proof.py --zip <generate.zip> [--overlay <dir>] --tenant cottonwood --input-id portfolio_...

What runs: the served zip's own modules (optionally with overlay files copied over them: the fix under test), loaded
from a fresh extract that is FIRST on sys.path. The real `generate_installed.compose_ports` and `build_boundary`, and
the real served Entry, handle one API-Gateway-shaped POST /analysis for an Opal viewer (verified-edge headers), with
report_title null, on a REAL normalized input.

Clients:
- Every READ goes to the live table or bucket (get_item, query, get_object, head_object; read-only).
- Every WRITE is captured in memory and never leaves the process (put_item, update_item, transact_write_items,
  put_object, send_message).
- Any other SDK method raises.

The one seeded fact is the viewer's canonical user profile, because a walk principal is deleted after its window.

Stages are recorded by a call tracer over functions defined in the extract. The run STOPS at the queue send. This
Lambda makes no vendor call; the first YCharts write is the resident's holdings_upload, which consumes the captured
message. The census at the end prints where every loaded first-party module came from: all must be the extract.
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

STAGES = ("submit", "validate_public_request", "current", "authorize_current", "read_input", "capture_title_source",
          "resolve_profile_fields", "resolve_comparison_fields", "capture_configuration", "admit", "validate_bindings",
          "accept", "dispatch", "put", "publish", "reserve", "send")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--overlay", help="a directory whose files replace the zip's same-named files")
    ap.add_argument("--tenant", default="cottonwood")
    ap.add_argument("--input-id", required=True)
    ap.add_argument("--viewer", default="irpt-offline-proof@opal.test")
    ap.add_argument("--out", help="directory to write the captured composition and queue message (for a resident replay)")
    ap.add_argument("--comparison-keys", default="",
                    help="comma-separated catalogue keys: 1 selects the Comparison variant, 2-5 Multi-Comp (none: Overview)")
    a = ap.parse_args(argv)

    extract = tempfile.mkdtemp(prefix="irpt-proof-")
    zipfile.ZipFile(a.zip).extractall(extract)
    overlaid = []
    if a.overlay:
        for name in sorted(os.listdir(a.overlay)):
            if os.path.isfile(os.path.join(a.overlay, name)):  # files only; a __pycache__ dir is not an overlay
                shutil.copyfile(os.path.join(a.overlay, name), os.path.join(extract, name))
                overlaid.append(name)
    sys.path.insert(0, extract)
    os.environ.setdefault("IRPT_DIRECTORY_BUCKET_MAP", json.dumps({"49financial": "opal-data-bd", "cottonwood": "opal-data-cot", "inflection": "opal-data-inf"}))
    print("extract", extract, "| overlay", overlaid or "none")

    writes = rt.Writes()
    region = "us-east-1"
    seeded = {a.viewer: rt.typed({"PK": "USER#" + a.viewer, "SK": "PROFILE", "email": a.viewer, "firmId": "opal-capital",
                                  "status": "active", "name": "Offline Proof Viewer",
                                  "createdAt": "2026-09-26T00:00:00Z", "updatedAt": "2026-09-26T00:00:00Z"})}
    ddb = rt.Dynamo(boto3.client("dynamodb", region_name=region), writes, seeded)
    table = rt.Table(ddb, "irpt-requests")
    s3 = rt.S3(boto3.client("s3", region_name=region), writes)
    sqs = rt.Sqs(writes)

    reached = []

    def tracer(frame, event, arg):
        if event == "call":
            code = frame.f_code
            if code.co_filename.startswith(extract) and code.co_name in STAGES:
                label = "%s.%s" % (os.path.basename(code.co_filename)[:-3], code.co_name)
                if not reached or reached[-1] != label:
                    reached.append(label)
        return None

    import generate_installed as gi
    import composition_admission as _ca
    _validate = _ca.CompositionAdmission.validate

    def validate_reporting_cause(self, document):
        # Diagnostic only: print the chained cause of a CLOSED_COMPOSITION_REQUIRED, then re-raise it unchanged.
        try:
            return _validate(self, document)
        except Exception as exc:
            cause = exc.__cause__
            print("ADMISSION REFUSED:", type(exc).__name__, exc, "| cause:", type(cause).__name__ if cause else None,
                  str(cause)[:700] if cause else "",
                  "| at", list(getattr(cause, "absolute_path", []))[:12], "| schema", list(getattr(cause, "absolute_schema_path", []))[:14])
            raise
    _ca.CompositionAdmission.validate = validate_reporting_cause
    env = {gi.QUEUE_URL_ENV: "https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation",
           gi.REQUESTS_TABLE_ENV: "irpt-requests", gi.JOBS_TABLE_ENV: "irpt-jobs"}
    ports = gi.compose_ports(clients={"dynamodb": ddb, "table": table, "s3": s3, "sqs": sqs}, environ=env,
                             clock=time.time)
    boundary = gi.build_boundary(ports)
    keys = [k for k in a.comparison_keys.split(",") if k]
    variant = "overview" if not keys else "comparison" if len(keys) == 1 else "multicomp"
    body = {"request_id": "y-offline-proof-%d" % int(time.time()), "client_id": None, "account_ids": [],
            "snapshot_id": None, "variant": variant, "comparison_keys": keys, "report_title": None,
            "prepared_for": "IRPT offline proof", "input_id": a.input_id}
    headers = {"x-contract-version": "v1", "x-origin-verify": "cloudfront", "x-user-email": a.viewer,
               "x-user-role": "admin", "x-user-type": "Dev", "x-firm-id": "opal-capital", "x-user-name": "Offline Proof Viewer"}
    event = {"routeKey": "POST /api/scoped/investor-reporting/analysis", "headers": headers,
             "queryStringParameters": {"selected_tenant": a.tenant}, "body": json.dumps(body)}

    sys.settrace(tracer)
    try:
        answer = boundary.handle(event)
    finally:
        sys.settrace(None)

    print("\nANSWER:", json.dumps({k: answer.get(k) for k in ("ok", "status", "operation")}, default=str)[:600])
    data = answer.get("data")
    print("DATA keys:", sorted(data) if isinstance(data, dict) else data)
    print("\nSTAGES REACHED (%d):" % len(reached))
    for i, s in enumerate(reached, 1):
        print("  %2d %s" % (i, s))
    print("\nCAPTURED WRITES (%d; none left this process):" % len(writes.log))
    for w in writes.log:
        print("  ", json.dumps(w)[:230])
    composition = None
    for (bucket, key), (_, blob) in s3.mem.items():
        if "/request_compositions/" in key:
            composition = json.loads(blob)
    if composition:
        resolved = composition.get("resolved", {})
        prof, prov = resolved.get("profile", {}), resolved.get("profile_provenance", {})
        title_src = prov.get("report_title", {}).get("source_id")
        print("\nCOMPOSITION: report_title=%r from source %r (kind %s); prepared_by=%r; organization=%r"
              % (prof.get("report_title"), title_src, resolved.get("source_descriptors", {}).get(title_src, {}).get("source_kind"),
                 prof.get("prepared_by"), prof.get("organization")))
        print("COMPARISONS: variant=%r catalog=%s" % (composition.get("browser", {}).get("variant"), json.dumps(
            {k: [v.get("vendor_id"), v.get("name"), v.get("security_type")]
             for k, v in (resolved.get("comparison_catalog") or {}).items()})))
    print("QUEUE MESSAGES:", [json.loads(m).get("kind") for m in sqs.sent])
    if a.out and composition:
        os.makedirs(a.out, exist_ok=True)
        json.dump(composition, open(os.path.join(a.out, "composition.json"), "w", encoding="utf-8"), sort_keys=True)
        json.dump([json.loads(m) for m in sqs.sent], open(os.path.join(a.out, "messages.json"), "w", encoding="utf-8"))
        rt.dump(os.path.join(a.out, "state.json"), ddb, s3, sqs)
        json.dump(seeded, open(os.path.join(a.out, "seeded_users.json"), "w", encoding="utf-8"))
        print("WROTE", os.path.join(a.out, "composition.json"), "messages.json, state.json, seeded_users.json")
    loaded = {m.__name__: getattr(m, "__file__", None) for m in list(sys.modules.values()) if getattr(m, "__file__", None)}
    first_party = {n: f for n, f in loaded.items() if os.path.exists(os.path.join(extract, n + ".py"))}
    # Compare by file identity: Windows reports the same directory as a short (ANDREW~1) or long path.
    outside = {n: f for n, f in first_party.items() if not os.path.samefile(os.path.dirname(f), extract)}
    print("\nMODULE CENSUS: %d first-party modules loaded, %d from the extract, %d from elsewhere %s"
          % (len(first_party), len(first_party) - len(outside), len(outside), sorted(outside) or ""))
    for n, f in sorted(outside.items()):
        print("   OUTSIDE %s <- %s" % (n, f))
    print("   sys.path head:", [p for p in sys.path[:8]])
    refused = not isinstance(data, dict) or answer.get("ok") is False
    print("\nRESULT:", "REFUSED" if refused else "ACCEPTED", "| stopped at the queue send; no vendor call is made by this Lambda")
    return 1 if refused or outside else 0


if __name__ == "__main__":
    sys.exit(main())
