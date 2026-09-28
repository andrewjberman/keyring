"""Record every AWS read an irpt-status zip makes for window 15's status read (portal header), then simulate each against
irpt-status-role (CTO 102269: the original_holdings grant). Read-only: live reads through the readthrough doubles, and
iam simulate-principal-policy.

    python status_role_sim.py <scratch dir holding w15state/> <irpt-status zip>

Why: an offline READY on the operator's credentials hid that the ROLE cannot read state/original_holdings/ (window 20,
5fSyChId). This grades the same reads against the role that will make them."""
import json
import os
import subprocess
import sys
import tempfile
import time
import zipfile

import boto3

LIVE = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\org\tier1_exec\2.0.0_SA_COO\deliverables\IRPT_MVP_Y\live_walk"
sys.path.insert(0, LIVE)
import readthrough as rt  # noqa: E402

S, ZIP = sys.argv[1], sys.argv[2]
RID, TENANT = "REQ-67e12718b0ba7c0c70ebb45b", "cottonwood"
ROLE = "arn:aws:iam::313476888478:role/irpt-status-role"
extract = tempfile.mkdtemp(prefix="irpt-status-sim-")
zipfile.ZipFile(ZIP).extractall(extract)
sys.path.insert(0, extract)
os.environ.setdefault("IRPT_DIRECTORY_BUCKET_MAP", json.dumps({"49financial": "opal-data-bd", "cottonwood": "opal-data-cot",
                                                                "inflection": "opal-data-inf"}))
writes = rt.Writes()
ddb = rt.Dynamo(boto3.client("dynamodb", region_name="us-east-1"), writes,
                json.load(open(S + "/w15state/seeded_users.json", encoding="utf-8")))
s3 = rt.S3(boto3.client("s3", region_name="us-east-1"), writes)
import status_installed as si  # noqa: E402
ports = si.compose_ports(clients={"dynamodb": ddb, "table": rt.Table(ddb, "irpt-requests"), "s3": s3}, clock=time.time,
                         environ={si.REQUESTS_TABLE_ENV: "irpt-requests", si.JOBS_TABLE_ENV: "irpt-jobs"})
boundary = si.build_boundary(ports)
headers = {"x-contract-version": "v1", "x-origin-verify": "cloudfront", "x-user-email": "irpt-offline-proof@opal.test",
           "x-user-role": "admin", "x-user-type": "Dev", "x-firm-id": "opal-capital", "x-user-name": "Offline Proof Viewer",
           "X-IRPT-Status-Dates": "prospect-v1"}
answer = boundary.handle({"routeKey": "GET /api/scoped/investor-reporting/status/{jobId}", "headers": headers,
                          "queryStringParameters": {"selected_tenant": TENANT}, "pathParameters": {"jobId": RID}})
print("answer state:", (answer.get("data") or {}).get("state"), (answer.get("data") or {}).get("public_reason_code"))
pairs = set()
for r in writes.reads:
    kind = r.get("kind", "")
    if kind.startswith("s3:"):
        action = "s3:GetObjectVersion" if r.get("version") else "s3:GetObject"
        pairs.add((action, "arn:aws:s3:::%s/%s" % (r.get("bucket"), r.get("key"))))
    elif kind.startswith("dynamodb:"):
        pairs.add((kind, "arn:aws:dynamodb:us-east-1:313476888478:table/%s%s"
                   % (r.get("table"), "/index/" + r["index"] if r.get("index") else "")))
print("distinct (action, resource) reads:", len(pairs))
denied = []
for action, resource in sorted(pairs):
    out = subprocess.run([r"C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\aws.cmd", "iam", "simulate-principal-policy",
                          "--policy-source-arn", ROLE, "--action-names", action, "--resource-arns", resource,
                          "--query", "EvaluationResults[0].EvalDecision", "--output", "text"], capture_output=True, text=True)
    decision = out.stdout.strip() or ("ERROR " + out.stderr.strip()[:80])
    short = resource.split(":::")[-1] if ":::" in resource else resource.split(":table/")[-1]
    prefix = "/".join(short.split("/")[:5])
    print("%-8s %-24s %s" % (decision[:8], action, prefix))
    if decision != "allowed":
        denied.append((action, prefix))
print("DENIED:", len(denied), sorted(set(denied)))
