"""Read-only AMGT evidence collection. No invoke, mutation, credential read or vendor request."""

import collections
import datetime
import hashlib
import io
import json
import pathlib
import re
import subprocess
import urllib.request
import zipfile
import boto3
from botocore.config import Config

ROOT = pathlib.Path.cwd()
OUT = ROOT / ".runtime/cro-z-amgt-research-20260923"
OUT.mkdir(parents=True, exist_ok=True)
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = {
    "measured_at": stamp,
    "operations": [
        "git reads",
        "S3 LIST/GET",
        "Lambda LIST/GET",
        "API Gateway GET",
        "Scheduler LIST",
    ],
    "errors": [],
}


def git(*args):
    return subprocess.check_output(["git", *args], text=True, encoding="utf-8").strip()


result["pins"] = {
    "workspace": git("rev-parse", "HEAD"),
    "cloud": git("rev-parse", "origin/CLOUD"),
    "portal": git("-C", "portal", "rev-parse", "HEAD"),
}
projects = {}
for home in sorted((ROOT / "org/missions/D5/AMGT").iterdir()):
    if not (home / "project.json").exists():
        continue
    project = json.loads((home / "project.json").read_text(encoding="utf-8"))
    orders = []
    for p in sorted((home / "task-orders").glob("*.md")):
        txt = p.read_text(encoding="utf-8")

        def field(n):
            m = re.findall(
                r"(?m)^[ \t]*<" + n + r">([^<\r\n]*)</" + n + r">[ \t]*$", txt
            )
            return m[-1].strip() if m else None

        orders.append(
            {
                "path": p.relative_to(ROOT).as_posix(),
                "status": field("status"),
                "issued_to": field("issued_to"),
                "issued_by": field("issued_by"),
            }
        )
    projects[home.name] = {
        "project_sha256": hashlib.sha256(
            (home / "project.json").read_bytes()
        ).hexdigest(),
        "status": project.get("status"),
        "dep_stage": project.get("dep_stage"),
        "orders": orders,
        "status_counts": dict(collections.Counter(o["status"] for o in orders)),
    }
result["projects"] = projects
cfg = Config(connect_timeout=10, read_timeout=30, retries={"max_attempts": 2})
session = boto3.Session(region_name="us-east-1")
s3 = session.client("s3", config=cfg)
all_objects = []
try:
    for page in s3.get_paginator("list_objects_v2").paginate(
        Bucket="opal-data-harvest"
    ):
        all_objects.extend(
            {
                "key": o["Key"],
                "size": o["Size"],
                "modified": o["LastModified"].isoformat(),
            }
            for o in page.get("Contents", [])
        )
    (OUT / "s3_inventory.json").write_text(
        json.dumps(all_objects, indent=2), encoding="utf-8"
    )
    groups = {}
    for o in all_objects:
        parts = o["key"].split("/")
        group = (
            "/".join(parts[:4])
            if len(parts) > 2 and parts[1] == "harvest"
            else "/".join(parts[:2])
        )
        g = groups.setdefault(
            group,
            {
                "objects": 0,
                "bytes": 0,
                "latest": None,
                "extensions": collections.Counter(),
            },
        )
        g["objects"] += 1
        g["bytes"] += o["size"]
        g["latest"] = max(g["latest"] or "", o["modified"])
        g["extensions"][pathlib.PurePosixPath(o["key"]).suffix] += 1
    result["s3"] = {
        "bucket": "opal-data-harvest",
        "objects": len(all_objects),
        "groups": groups,
    }
except Exception as e:
    result["errors"].append({"op": "S3 LIST", "error": str(e)})
lam = session.client("lambda", config=cfg)
try:
    functions = []
    scanned = 0
    for page in lam.get_paginator("list_functions").paginate():
        scanned += len(page["Functions"])
        functions.extend(
            f
            for f in page["Functions"]
            if re.search(r"amgt|harvest|research", f["FunctionName"], re.I)
        )
    result["lambda_scanned"] = scanned
    result["functions"] = []
    for f in functions:
        info = lam.get_function(FunctionName=f["FunctionName"])
        c = info["Configuration"]
        env = c.get("Environment", {}).get("Variables", {})
        row = {
            k: c.get(k)
            for k in [
                "FunctionName",
                "Handler",
                "Runtime",
                "CodeSha256",
                "LastModified",
                "State",
                "LastUpdateStatus",
                "Timeout",
                "MemorySize",
                "Role",
            ]
        }
        row["environment_keys"] = sorted(env)
        row["safe_configuration"] = {
            k: v
            for k, v in env.items()
            if re.search(r"BUCKET|PREFIX|TABLE|MODE|POOL_ROOT|MODEL_BLOCK_ROOT", k)
            and not re.search(r"SECRET|TOKEN|KEY|PASSWORD", k)
        }
        if f["FunctionName"] == "opal-amgt-scoped-api":
            raw = urllib.request.urlopen(info["Code"]["Location"], timeout=30).read()
            import base64

            row["download_digest_matches"] = (
                base64.b64encode(hashlib.sha256(raw).digest()).decode()
                == c["CodeSha256"]
            )
            z = zipfile.ZipFile(io.BytesIO(raw))
            row["archive_members"] = len(z.namelist())
            comparisons = []
            for member in z.namelist():
                if member.endswith(".py") and (
                    member.startswith("lib/research/") or member == "lambda_function.py"
                ):
                    local = (
                        ROOT / member
                        if member != "lambda_function.py"
                        else ROOT
                        / "infra/aws/lambda/research/scoped_amgt_api/lambda_function.py"
                    )
                    code = z.read(member)
                    local_b = local.read_bytes() if local.exists() else None
                    comparisons.append(
                        {
                            "path": member,
                            "sha256": hashlib.sha256(code).hexdigest(),
                            "local_exists": local.exists(),
                            "equal_normalized_newlines": local_b is not None
                            and code.replace(b"\r\n", b"\n")
                            == local_b.replace(b"\r\n", b"\n"),
                        }
                    )
            row["source_comparison"] = comparisons
            (OUT / "deployed_scoped_amgt.py").write_bytes(
                z.read("lib/research/api/scoped_amgt.py")
            )
        result["functions"].append(row)
except Exception as e:
    result["errors"].append({"op": "Lambda LIST/GET", "error": str(e)})
try:
    sched = session.client("scheduler", config=cfg)
    found = []
    total = 0
    for page in sched.get_paginator("list_schedules").paginate():
        for r in page.get("Schedules", []):
            total += 1
            if re.search(r"amgt|harvest|research", r["Name"], re.I):
                found.append(
                    {
                        k: r.get(k)
                        for k in ["Name", "GroupName", "State", "LastModificationDate"]
                    }
                )
    result["schedules"] = {"scanned": total, "matched": found}
except Exception as e:
    result["errors"].append({"op": "Scheduler LIST", "error": str(e)})
try:
    api = session.client("apigatewayv2", config=cfg)
    routes = []
    apis = api.get_apis().get("Items", [])
    for a in apis:
        nxt = None
        while True:
            page = api.get_routes(
                ApiId=a["ApiId"], **({"NextToken": nxt} if nxt else {})
            )
            for r in page.get("Items", []):
                if "amgt" in r.get("RouteKey", "").lower():
                    routes.append(
                        {
                            "api_name": a["Name"],
                            "api_id": a["ApiId"],
                            **{
                                k: r.get(k)
                                for k in ["RouteKey", "AuthorizationType", "Target"]
                            },
                        }
                    )
            nxt = page.get("NextToken")
            if not nxt:
                break
    result["api_routes"] = {"apis_scanned": len(apis), "routes": routes}
except Exception as e:
    result["errors"].append({"op": "API Gateway GET", "error": str(e)})
(OUT / "evidence.json").write_text(
    json.dumps(result, indent=2, default=str), encoding="utf-8"
)
print(
    json.dumps(
        {
            "pins": result["pins"],
            "projects": {
                k: {"orders": len(v["orders"]), "status_counts": v["status_counts"]}
                for k, v in projects.items()
            },
            "s3_objects": len(all_objects),
            "functions": [
                {k: r[k] for k in ["FunctionName", "LastModified", "State"]}
                for r in result.get("functions", [])
            ],
            "route_count": len(result.get("api_routes", {}).get("routes", [])),
            "schedules": result.get("schedules"),
            "errors": result["errors"],
        },
        indent=2,
        default=str,
    )
)
