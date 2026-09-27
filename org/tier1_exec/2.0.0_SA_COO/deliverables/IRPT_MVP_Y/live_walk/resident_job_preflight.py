"""Hops 5-7 offline: the DEPLOYED resident package runs the analysis_generate job that phase 1 captured, to a terminal.

    python resident_job_preflight.py --package <extracted resident tarball> --state <phase-1 out dir>
        --pdf <synthetic.pdf> --census <synthetic_census.json> [--overlay <dir>]

The package is copied fresh; --overlay replaces same-named modules in the copy. The run starts as the host starts:
- sys.path is the package root plus resident_main's own additions;
- the factory is resident_installed.build_resident_runtime, and poll_once runs one delivery.
It differs from the host in four stated places:
1. Clients: readthrough doubles loaded with phase 1's captured world. Reads go to live AWS; writes stay in memory.
2. The vendor: deadline_transport._run_child answers from the package's recorded HAR fixtures (the connected harness's
   script). The holdings-upload echo is built from what the resident SENDS, and the download is a synthetic PDF. No
   vendor call leaves the process.
3. The census: a synthetic census consistent with that PDF. The pinned production census describes a real vendor PDF
   this run cannot obtain without a vendor call; a local bindings file pins the synthetic one by sha256, as verify_pins
   requires.
4. The session secret: the replay bundle, from a fake secretsmanager. Writes are captured.
Everything else is the package's own code: current_authority, the lease, the frozen composition's admission, the
recipe, the holdings upload built from the v2 template input, certification, retention and publication.
"""
import argparse
import base64
import hashlib
import json
import os
import shutil
import sys
import tempfile
import time
from types import SimpleNamespace

import boto3

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import readthrough as rt  # noqa: E402

STAGES = ("poll_once", "execute", "decide", "claim", "prepare", "validate", "consume_configuration", "recipe_inputs",
          "normalized_input", "upload_rows", "submit", "renew", "record_checkpoint", "record_intent", "download",
          "certify", "extract", "put", "publish", "reserve", "transition", "finish", "resolve_upload")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--state", required=True)
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--census", required=True)
    ap.add_argument("--overlay")
    ap.add_argument("--out", help="directory to dump the post-job world (for the hop 8-10 read-path proof)")
    ap.add_argument("--waf-read", type=int, default=0,
                    help="after the calculating answers, N WAF-challenge answers (the research-measured 202 from "
                         "decision_branches.json), then available")
    ap.add_argument("--waf-shape", choices=("research", "window8"), default="research",
                    help="research: the decision_branches 202 (body says calculating); window8: the live 202 whose "
                         "body carried no status (the journal's portfolio_status=-)")
    ap.add_argument("--capture-stub", action="store_true",
                    help="stand in for the Linux-only host browser capture: bump the session generation and fence")
    ap.add_argument("--status-calculating", type=int, default=0,
                    help="answer the portfolio status `calculating` N times before `available` (window 7 live)")
    a = ap.parse_args(argv)

    root = os.path.join(tempfile.mkdtemp(prefix="irpt-resident-job-"), "pkg")
    shutil.copytree(a.package, root)
    overlaid = []
    for name in sorted(os.listdir(a.overlay)) if a.overlay else []:
        src = os.path.join(a.overlay, name)
        if os.path.isfile(src):
            for dp, _, fn in os.walk(root):
                # Test and fixture trees are recorded evidence, never code: an overlay never lands there.
                if name in fn and not {"tests", "fixtures"} & set(dp.split(os.sep)):
                    shutil.copyfile(src, os.path.join(dp, name))
                    overlaid.append(os.path.relpath(os.path.join(dp, name), root))
    print("resident package copy", root, "| overlay", overlaid or "none")
    sys.path.insert(0, root)
    sys.path.insert(0, os.path.join(root, "ycharts", "generate"))
    for rel in ("intake", "ops", "reports", "_keys", "_authz", "_gate", "ycharts/session", "ycharts/extract"):
        if os.path.isdir(os.path.join(root, rel)):
            sys.path.insert(0, os.path.join(root, rel))

    from transport import ReplayTransport, validate_pdf
    import deadline_transport
    from resident_worker import poll_once
    import resident_installed

    # Recorded vendor answers: the connected harness's script, the package's own fixtures.
    folder = os.path.join(root, "ycharts", "generate", "fixtures", "har")

    def fixture(name):
        return json.load(open(os.path.join(folder, name + ".json"), encoding="utf-8"))
    upload = fixture("upload_ok")
    script = {
        ("GET", "/custom_pdf_reports/generate/14141822"): {"status": 200, "body": fixture("templates")["14141822"]},
        ("POST", "/model_portfolios/fixed/holdings_upload/client"): upload,
        ("POST", "/model_portfolios/fixed/"): fixture("create_201"),
        ("GET", "/model_portfolios/2332060/status"): (
            [{"status": 200, "body": {"status": "calculating"}}] * a.status_calculating
            + [fixture("decision_branches")["WAF_REFRESH_REQUIRED"] if a.waf_shape == "research" else
               {"status": 202, "body": {}, "content_type": "application/json", "waf_action": "challenge"}] * a.waf_read
            + [fixture("status_ok")]),
        ("POST", "/custom_pdf_reports/validate_report_securities/14141822"): fixture("validate_200"),
        ("POST", "/custom_pdf_reports/14141822"): fixture("generate_201")}
    replay = ReplayTransport(script)
    bundle = json.loads(json.dumps(replay.bundle))
    bundle["fence"] = 1
    pdf = open(a.pdf, "rb").read()
    vendor_sent = []

    def child(command, frame, deadline, **kw):
        if frame["mode"] == "download":
            vendor_sent.append(("DOWNLOAD", frame["url"][:60]))
            return {"body": base64.b64encode(pdf).decode(), "evidence": validate_pdf(pdf, 200, "application/pdf", [])}
        payload = None if frame["payload"] is None else base64.b64decode(frame["payload"])
        if frame["path"].startswith("/model_portfolios/fixed/holdings_upload"):
            # The upload is a FILE upload (not JSON): record what the resident SENDS, verbatim-excerpted.
            text = payload.decode("utf-8", "replace") if payload else ""
            vendor_sent.append(("HOLDINGS_UPLOAD", "carries AAPL/10.01/VNQ/2.02: %s" % all(
                t in text for t in ("AAPL", "10.01", "VNQ", "2.02")), text[:160].replace("\r", " ").replace("\n", " | ")))
        else:
            vendor_sent.append((frame["method"], frame["path"]))
        info, body = replay.request(frame["path"], frame["method"], payload, frame["content_type"])
        return {"info": info, "body": base64.b64encode(body).decode(), "cookies": frame["bundle"]["cookies"]}
    deadline_transport._run_child = child

    # Bindings: the deployed file's own values, with the census and enrolled identity swapped (stated in the docstring).
    deployed = json.load(open(os.path.join(root, "reports", "resident_bindings.json"), encoding="utf-8"))
    census_bytes = open(a.census, "rb").read()
    bindings = dict(deployed)
    bindings["capture"] = {
        "wrapper_path": os.path.join(root, "ycharts-host", "run-ycharts-session.sh"),
        "wrapper_sha256": deployed["capture"]["wrapper_sha256"],
        "library_path": os.path.join(root, "ycharts-host", "ycharts_session.js"),
        "library_sha256": deployed["capture"]["library_sha256"]}
    bindings["census"] = {"path": os.path.abspath(a.census), "sha256": hashlib.sha256(census_bytes).hexdigest()}
    bindings["schema_directory"] = os.path.join(root, "docs", "contracts", "investor-reporting", "v1")
    bindings["enrolled_user_id"] = bundle["identity"]["user_id"]
    bindings_path = os.path.join(os.path.dirname(root), "resident_bindings.json")
    json.dump(bindings, open(bindings_path, "w", encoding="utf-8"), indent=1)

    writes = rt.Writes()
    seeded = json.load(open(os.path.join(a.state, "seeded_users.json"), encoding="utf-8"))
    ddb = rt.Dynamo(boto3.client("dynamodb", region_name="us-east-1"), writes, seeded)
    s3 = rt.S3(boto3.client("s3", region_name="us-east-1"), writes)
    messages = rt.load(os.path.join(a.state, "state.json"), ddb, s3)
    # The recorded echo carries the frozen input's rows, as the connected harness seeds it (the vendor echoes the upload).
    frozen = json.load(open(os.path.join(a.state, "composition.json"), encoding="utf-8"))
    upload["body"]["rows"] = [{"security_id": r["security_id"], "display_security_id": r["security_id"],
                               "display_name": "Fixture " + r["security_id"], "weighting": r["dollars"]}
                              for r in frozen["resolved"]["document"]["holdings"]["rows"]]
    job_messages = [m for m in messages if json.loads(m).get("kind") == "analysis_generate"]
    sqs = rt.Sqs(writes, inbox=job_messages)
    secrets = SimpleNamespace(
        get_secret_value=lambda **kw: {"SecretString": json.dumps(bundle), "VersionId": "offline"},
        put_secret_value=lambda **kw: writes.add("secrets.put") or {"VersionId": "offline-2"})
    clients = {"dynamodb": ddb, "table": rt.Table(ddb, "irpt-requests"), "s3": s3, "secretsmanager": secrets, "sqs": sqs}
    runtime = resident_installed.build_resident_runtime(bindings_path, clients=clients, clock=time.time)
    captures = []
    if a.capture_stub:
        def capture():
            captures.append(time.time())
            bundle.update(generation="offline-recaptured-%d" % len(captures), fence=bundle["fence"] + 1)
        runtime["assembly"].session.capture_workflow = SimpleNamespace(capture=capture)
    print("runtime built: assembly %s | queue %s | delivering %d analysis_generate message(s)"
          % (type(runtime["assembly"]).__name__, runtime["queue_url"].rsplit("/", 1)[-1], len(job_messages)))

    reached = []

    def tracer(frame, event, arg):
        if event == "call" and frame.f_code.co_name in STAGES:
            filename = frame.f_code.co_filename
            if os.path.abspath(filename).lower().startswith(os.path.abspath(root).lower()):
                label = "%s.%s" % (os.path.basename(filename)[:-3], frame.f_code.co_name)
                if not reached or reached[-1] != label:
                    reached.append(label)
        return None
    sys.settrace(tracer)
    try:
        handled = poll_once(**runtime)
        error = None
    except Exception as exc:  # noqa: BLE001 -- the pre-flight reports the refusal by name
        handled, error = None, exc
    finally:
        sys.settrace(None)

    message = json.loads(job_messages[0]) if job_messages else {}
    row = ddb.current("irpt-jobs", {"tenant": {"S": message.get("tenant", "")}, "job": {"S": message.get("request_id", "")}})
    print("\nHANDLED:", handled, "| EXCEPTION:", "%s %s | cause %r" % (type(error).__name__, error, error.__cause__) if error else None)
    if row:
        detail = row.get("job_detail", {}).get("S")
        print("JOB ROW: state=%s | checkpoints=%s | intents=%s" % (row.get("state", {}).get("S"),
              sorted(k for k in row if k.startswith("checkpoint_")), sorted(k for k in row if k.startswith("intent_"))))
        print("JOB DETAIL:", (detail or "")[:600])
    print("\nSTAGES REACHED (%d):" % len(reached))
    for i, s in enumerate(reached, 1):
        print("  %2d %s" % (i, s))
    print("\nVENDOR (replayed, nothing left the process):")
    for v in vendor_sent:
        print("  ", v)
    print("\nCAPTURED WRITES (%d):" % len(writes.log))
    for w in writes.log:
        print("  ", json.dumps(w, default=str)[:220])
    reports = [k for k in ddb.mem if k[0] == "irpt-requests" and '"S": "REPORT#' in k[2]]
    print("\nREPORT# rows published:", len(reports))
    state = row.get("state", {}).get("S") if row else None
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        rt.dump(os.path.join(a.out, "state.json"), ddb, s3, sqs)
        shutil.copyfile(os.path.join(a.state, "seeded_users.json"), os.path.join(a.out, "seeded_users.json"))
        report = [k[2] for k in reports]
        json.dump({"tenant": message.get("tenant"), "request_id": message.get("request_id"), "report_keys": report,
                   "job_state": state}, open(os.path.join(a.out, "job.json"), "w", encoding="utf-8"))
        print("WROTE", a.out)
    print("CAPTURES (stubbed host re-capture):", len(captures))
    print("\nRESULT:", state or "NO JOB ROW", "| handled", handled)
    return 0 if state == "READY" else 1


if __name__ == "__main__":
    sys.exit(main())
