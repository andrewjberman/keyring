import base64
import collections
import datetime
import hashlib
import io
import json
import pathlib
import re
import sys
import urllib.request
import zipfile
import boto3
import pyarrow.parquet as pq


def main():
    root = next(
        p for p in pathlib.Path(__file__).resolve().parents if (p / ".git").exists()
    )
    sys.path.insert(0, str(root))
    from lib.research.harvest import store
    from lib.research.coverage import pool_reader
    from lib.research.metrics import chatter_axis

    out = root / "org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST"
    runtime = root / ".runtime/h03-leadpanel"
    runtime.mkdir(exist_ok=True)
    record = {
        "captured_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "AWS reads only; no Lambda invocation; local gold replay uses write_fn=None",
    }
    session = boto3.Session(region_name="us-east-1")
    lam, s3, iam = [session.client(x) for x in ("lambda", "s3", "iam")]
    response = lam.get_function(FunctionName="amgt-resapp-chatter-axis")
    config = response["Configuration"]
    record["lambda"] = {
        k: config.get(k)
        for k in (
            "FunctionName",
            "Role",
            "Runtime",
            "CodeSize",
            "CodeSha256",
            "LastModified",
            "Handler",
            "Timeout",
            "MemorySize",
            "Layers",
            "Architectures",
            "RevisionId",
        )
    }
    record["lambda"]["environment_keys"] = sorted(
        config.get("Environment", {}).get("Variables", {})
    )
    raw = urllib.request.urlopen(response["Code"]["Location"]).read()
    assert (
        base64.b64encode(hashlib.sha256(raw).digest()).decode() == config["CodeSha256"]
    )
    (runtime / "deployed.zip").write_bytes(raw)
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        record["zip"] = {
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
            "pyarrow_members": sum(n.startswith("pyarrow/") for n in z.namelist()),
            "sources": {
                n: {
                    "bytes": len(z.read(n)),
                    "sha256": hashlib.sha256(z.read(n)).hexdigest(),
                }
                for n in (
                    "lambda_function.py",
                    "lib/research/metrics/chatter_axis.py",
                    "lib/research/metrics/generation_writer.py",
                    "lib/research/coverage/pool_reader.py",
                )
            },
        }
    role = config["Role"].rsplit("/", 1)[-1]
    record["role"] = {"name": role, "inline": {}, "attached": []}
    for p in iam.get_paginator("list_role_policies").paginate(RoleName=role):
        for name in p["PolicyNames"]:
            record["role"]["inline"][name] = iam.get_role_policy(
                RoleName=role, PolicyName=name
            )["PolicyDocument"]
    for p in iam.get_paginator("list_attached_role_policies").paginate(RoleName=role):
        for policy in p["AttachedPolicies"]:
            meta = iam.get_policy(PolicyArn=policy["PolicyArn"])["Policy"]
            record["role"]["attached"].append(
                {
                    "arn": policy["PolicyArn"],
                    "document": iam.get_policy_version(
                        PolicyArn=policy["PolicyArn"],
                        VersionId=meta["DefaultVersionId"],
                    )["PolicyVersion"]["Document"],
                }
            )
    schedule = session.client("scheduler").get_schedule(
        Name="amgt-resapp-chatter-axis-daily"
    )
    record["schedule"] = {
        k: schedule[k]
        for k in (
            "Name",
            "State",
            "ScheduleExpression",
            "ScheduleExpressionTimezone",
            "Target",
        )
    }
    table = session.resource("dynamodb").Table("opal-harvest-security-metrics")
    items = []
    args = {"ConsistentRead": True}
    while True:
        page = table.scan(**args)
        items.extend(page["Items"])
        if "LastEvaluatedKey" not in page:
            break
        args["ExclusiveStartKey"] = page["LastEvaluatedKey"]
    record["table_scan_items"] = len(items)
    record["chatter_items"] = [
        r
        for r in items
        if any(
            str(v).startswith(("TRENDING_CHATTER", "BREAKOUT_CHATTER"))
            for v in r.values()
        )
    ]
    logs = session.client("logs")
    record["run_lines"] = []
    for stream in logs.describe_log_streams(
        logGroupName="/aws/lambda/amgt-resapp-chatter-axis",
        orderBy="LastEventTime",
        descending=True,
        limit=3,
    )["logStreams"]:
        events = logs.get_log_events(
            logGroupName="/aws/lambda/amgt-resapp-chatter-axis",
            logStreamName=stream["logStreamName"],
            limit=150,
            startFromHead=False,
        )["events"]
        record["run_lines"].extend(
            e for e in events if "names_with_links=" in e["message"]
        )
    prefix = store.table_prefix("amgt", "gold", "chatter_daily")
    keys = []
    for page in s3.get_paginator("list_objects_v2").paginate(
        Bucket=store.HARVEST_BUCKET, Prefix=prefix
    ):
        keys.extend(
            o["Key"] for o in page.get("Contents", []) if o["Key"].endswith(".parquet")
        )
    date_re = re.compile(r"date=([0-9]{4}-[0-9]{2}-[0-9]{2})")
    key = sorted(
        keys, key=lambda k: (date_re.search(k).group(1) if date_re.search(k) else "", k)
    )[-1]
    obj = s3.get_object(Bucket=store.HARVEST_BUCKET, Key=key)
    gold = obj["Body"].read()
    rows = pq.read_table(io.BytesIO(gold)).to_pylist()
    (runtime / "gold.parquet").write_bytes(gold)
    record["gold"] = {
        "bucket": store.HARVEST_BUCKET,
        "prefix": prefix,
        "key": key,
        "objects": len(keys),
        "etag": obj["ETag"],
        "sha256": hashlib.sha256(gold).hexdigest(),
        "rows": len(rows),
        "states": dict(collections.Counter(r.get("data_status") for r in rows)),
        "securities": len({r["security_key"] for r in rows}),
    }
    # Replay the producer's actual reader over the single captured snapshot. No writer or vendor call.
    pool_reader._gold_latest_snapshot_rows = lambda *a, **kw: rows
    summary = chatter_axis.compute_chatter_axis(
        as_of_date="2026-09-24",
        count_fn=chatter_axis.gold_daily_mention_scores,
        write_fn=None,
        run_id="h03-baseline-read-only",
    )
    record["replay"] = {
        k: summary[k]
        for k in (
            "universe",
            "input_coverage",
            "states",
            "incomplete_names",
            "rows_ranked",
            "rows_written",
        )
        if k in summary
    }
    record["replay"]["products"] = [
        {
            k: p.get(k)
            for k in (
                "axis",
                "state",
                "rows_ranked",
                "pointer_written",
                "reason_code",
                "failure_reason",
                "generation",
            )
        }
        for p in summary["products"]
    ]
    record["replay"]["names_with_stored_days"] = sum(
        v.get("store_item_count", 0) > 0
        for v in summary.get("read_detail", {}).values()
    )
    record["limits"] = [
        "Host pyarrow 24 is not Lambda runtime proof.",
        "Replay uses reviewed isolated source, not deployed ZIP.",
        "Gold store_item_count counts day records, not publication links.",
        "No served route or authenticated browser invocation.",
    ]
    (out / "LEADPANEL_BASELINE.json").write_text(
        json.dumps(record, indent=2, default=str) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "lambda": record["lambda"],
                "gold": record["gold"],
                "replay": record["replay"],
                "run_lines": record["run_lines"],
            },
            default=str,
        )
    )


if __name__ == "__main__":
    main()
