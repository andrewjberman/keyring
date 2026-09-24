"""Ruff-clean copy of the AS-RUN script (restore_crosswalk_0924.py.as-run.txt, executed 08:22:33Z); formatting only.

Rollback leg of the never-widen pair (COO @4c7d0b2e7c, CTO @429efcdf30): restore
crosswalk/v1/2026-09-24.json to the signed bytes by server-side copy of the signed S3 VERSION.
GO: 1.0.0_SA_CTO~Z msg 25331. No delete, no local bytes."""
import hashlib
import json

import boto3
B = "opal-data-harvest"
K = "crosswalk/v1/2026-09-24.json"
SIGNED_V = "K1qTvwqiuo3jNvF_bwC94m1P0J5vHtwS"
s3 = boto3.client("s3", region_name="us-east-1")
h = s3.head_object(Bucket=B, Key=K, VersionId=SIGNED_V)
print("PRE signed version", SIGNED_V, "bytes", h["ContentLength"], "ETag", h["ETag"], "mod", h["LastModified"].isoformat())
body = s3.get_object(Bucket=B, Key=K, VersionId=SIGNED_V)["Body"].read()
sha = hashlib.sha256(body).hexdigest()
print("PRE signed version sha256", sha)
assert h["ContentLength"] == 523207 and sha.startswith("9bd953b9"), "signed version does not match receipt -- refuse"
cur = s3.head_object(Bucket=B, Key=K)
print("PRE latest", "bytes", cur["ContentLength"], "VersionId", cur.get("VersionId"), "ETag", cur["ETag"])
r = s3.copy_object(Bucket=B, Key=K, CopySource={"Bucket": B, "Key": K, "VersionId": SIGNED_V},
                   MetadataDirective="COPY", ContentType=h.get("ContentType", "application/json"))
print("COPY new VersionId", r.get("VersionId"), "ETag", r["CopyObjectResult"]["ETag"], "src", r.get("CopySourceVersionId"))
post = s3.head_object(Bucket=B, Key=K)
pb = s3.get_object(Bucket=B, Key=K)["Body"].read()
print("POST latest bytes", post["ContentLength"], "ETag", post["ETag"], "VersionId", post.get("VersionId"), "sha256", hashlib.sha256(pb).hexdigest())
doc = json.loads(pb)
recs = doc.get("records") if isinstance(doc, dict) else doc
if isinstance(recs, dict):
    recs = list(recs.values())
st = {}
for rr in recs or []:
    s = rr.get("status") or rr.get("identity_status") or rr.get("state") or "?"
    st[s] = st.get(s, 0) + 1
print("POST records", len(recs or []), "states", st)
lam = boto3.client("lambda", region_name="us-east-1")
for key in ("ASML_US_Equity", "AAPL_US_Equity", "CAT_US_Equity"):
    ev = {"version": "2.0", "rawPath": "/api/scoped/amgt/security/%s/peers" % key, "rawQueryString": "",
          "headers": {"x-firm-id": "opal", "x-user-role": "admin"},
          "requestContext": {"http": {"method": "GET", "path": "/api/scoped/amgt/security/%s/peers" % key}}}
    resp = lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode("utf-8"))
    p = json.loads(resp["Payload"].read().decode("utf-8"))
    b = json.loads(p.get("body") or "{}")
    ident = b.get("identity") or {}
    print("SERVED", key, "status", p.get("statusCode"), "identity", ident.get("identity_status") or ident.get("status"),
          "basis", b.get("basis"), "members", len(b.get("members") or []), "peer_read", (b.get("peer_read") or {}).get("status"))
