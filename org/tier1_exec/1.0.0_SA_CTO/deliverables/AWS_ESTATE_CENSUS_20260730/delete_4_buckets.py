"""Delete 4 zero-edge buckets per Andrew-direct 2026-07-30 ruling
('if we're not using the opal-cloudfront-logs, get rid of it. the other 3 delete
candidates should be deleted.') -- CF logging verified Enabled:false Bucket:"" first.

Sequence per bucket: archive contents locally (look-before-delete) -> purge all
versions + delete markers -> delete bucket -> head_bucket verify 404.
Positive control at the end: a KEEP bucket still resolves.
"""
from __future__ import annotations

import os

import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3", region_name="us-east-1")
TARGETS = [
    "ajb-workflow",
    "opal-cloudfront-logs-313476888478",
    "opal-data-aaii-v2",
    "opal-analytics-dashboard",
]
ARCHIVE = "deleted_bucket_archives"

for b in TARGETS:
    print(f"--- {b}")
    # 1. archive every current object (all are tiny; verified by hand pre-run)
    n_arch = 0
    resp = s3.list_objects_v2(Bucket=b)
    for o in resp.get("Contents", []):
        dest = os.path.join(ARCHIVE, b, o["Key"].replace("/", "__"))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        s3.download_file(b, o["Key"], dest)
        n_arch += 1
    print(f"  archived {n_arch} objects -> {ARCHIVE}/{b}/")

    # 2. purge all versions + delete markers (versioned buckets refuse delete otherwise)
    n_purged = 0
    paginator = s3.get_paginator("list_object_versions")
    for page in paginator.paginate(Bucket=b):
        batch = [{"Key": v["Key"], "VersionId": v["VersionId"]}
                 for coll in ("Versions", "DeleteMarkers")
                 for v in page.get(coll, [])]
        if batch:
            s3.delete_objects(Bucket=b, Delete={"Objects": batch, "Quiet": True})
            n_purged += len(batch)
    print(f"  purged {n_purged} versions/markers")

    # 3. delete the bucket
    s3.delete_bucket(Bucket=b)
    print("  delete_bucket issued")

    # 4. verify gone
    try:
        s3.head_bucket(Bucket=b)
        print(f"  ERROR: {b} STILL EXISTS")
    except ClientError as e:
        code = e.response["Error"]["Code"]
        print(f"  verified gone: head_bucket -> {code}")

# positive control: a KEEP bucket must still resolve
s3.head_bucket(Bucket="opal-data-mdpf")
print("positive control: opal-data-mdpf head_bucket -> 200 OK")
print(f"bucket count now: {len(s3.list_buckets()['Buckets'])} (was 39)")
