"""Read-only, bounded follow-up: existing object metadata/aggregates and deployed code/IAM."""

import collections
import datetime
import difflib
import hashlib
import io
import json
import pathlib
import urllib.request
import zipfile
import boto3
import pyarrow.parquet as pq

P = pathlib.Path(".runtime/cro-z-amgt-research-20260923")
inv = json.loads((P / "s3_inventory.json").read_text())
out = {
    "measured_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "objects": [],
    "errors": [],
}
session = boto3.Session(region_name="us-east-1")
s3 = session.client("s3")
lam = session.client("lambda")
iam = session.client("iam")
prefixes = [
    "universe/v1/",
    "crosswalk/v1/",
    "amgt/harvest/gold/research-backlog/",
    "amgt/harvest/gold/chatter_daily/",
    "amgt/harvest/silver/research-report/",
    "amgt/harvest/state/pull_log/",
]
for o in inv:
    if not any(o["key"].startswith(p) for p in prefixes):
        continue
    try:
        raw = s3.get_object(Bucket="opal-data-harvest", Key=o["key"])["Body"].read()
        r = {**o, "sha256": hashlib.sha256(raw).hexdigest()}
        if o["key"].endswith(".json"):
            d = json.loads(raw)
            r["top_keys"] = list(d) if isinstance(d, dict) else None
            r["shape"] = (
                {
                    k: len(v) if isinstance(v, (dict, list)) else v
                    for k, v in d.items()
                    if k not in ("description", "reason", "notes")
                }
                if isinstance(d, dict)
                else {"length": len(d)}
            )
            for k, v in d.items() if isinstance(d, dict) else []:
                if isinstance(v, list) and v and isinstance(v[0], dict):
                    r.setdefault("list_fields", {})[k] = sorted(
                        set(x for row in v for x in row)
                    )
                    for field in [
                        "status",
                        "resolution",
                        "state",
                        "resolved",
                        "security_key",
                        "step",
                        "outcome",
                    ]:
                        if any(field in row for row in v):
                            r.setdefault("distributions", {})[k + "." + field] = dict(
                                collections.Counter(str(row.get(field)) for row in v)
                            )
        elif o["key"].endswith(".parquet"):
            t = pq.read_table(io.BytesIO(raw))
            r["rows"] = t.num_rows
            r["columns"] = t.column_names
            r["distinct"] = {
                k: len(set(str(x) for x in t[k].to_pylist()))
                for k in [
                    "security_key",
                    "publisher",
                    "source",
                    "date",
                    "day",
                    "folder_name",
                    "report_id",
                ]
                if k in t.column_names
            }
        out["objects"].append(r)
    except Exception as e:
        out["errors"].append({"key": o["key"], "error": str(e)})
out["deployment"] = []
for name in ["opal-amgt-scoped-api", "amgt-resapp-chatter-axis"]:
    try:
        g = lam.get_function(FunctionName=name)
        c = g["Configuration"]
        z = zipfile.ZipFile(
            io.BytesIO(urllib.request.urlopen(g["Code"]["Location"], timeout=30).read())
        )
        role = c["Role"].split("/")[-1]
        policies = []
        for page in iam.get_paginator("list_role_policies").paginate(RoleName=role):
            for n in page["PolicyNames"]:
                doc = iam.get_role_policy(RoleName=role, PolicyName=n)["PolicyDocument"]
                policies.append({"name": n, "document": doc})
        managed = iam.list_attached_role_policies(RoleName=role)["AttachedPolicies"]
        row = {
            "name": name,
            "modified": c["LastModified"],
            "code_sha256": c["CodeSha256"],
            "inline_policies": policies,
            "attached_policies": managed,
            "diffs": {},
        }
        for path in [
            "lambda_function.py",
            "lib/research/metrics/chatter_axis.py",
            "lib/research/coverage/pool_reader.py",
            "lib/research/identity/crosswalk.py",
        ]:
            if path not in z.namelist():
                continue
            raw = z.read(path).decode("utf-8")
            target = pathlib.Path(path)
            if path == "lambda_function.py":
                target = (
                    pathlib.Path("infra/aws/lambda/research")
                    / (
                        "scoped_amgt_api"
                        if name == "opal-amgt-scoped-api"
                        else "chatter_axis"
                    )
                    / path
                )
            (P / (name + "__" + path.replace("/", "__"))).write_text(
                raw, encoding="utf-8"
            )
            if target.exists():
                row["diffs"][path] = "".join(
                    difflib.unified_diff(
                        raw.splitlines(True),
                        target.read_text(encoding="utf-8").splitlines(True),
                        fromfile="deployed",
                        tofile=str(target),
                    )
                )
        out["deployment"].append(row)
    except Exception as e:
        out["errors"].append({"lambda": name, "error": str(e)})
(P / "supplement.json").write_text(
    json.dumps(out, indent=2, default=str), encoding="utf-8"
)
print(json.dumps(out, indent=2, default=str))
