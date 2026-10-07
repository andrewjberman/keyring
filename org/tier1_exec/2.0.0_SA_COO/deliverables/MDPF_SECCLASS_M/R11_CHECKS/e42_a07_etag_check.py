#!/usr/bin/env python3
"""e42_a07_etag_check.py -- MDPF_SECCLASS SC-e-42 deploy: the live a07 equals the candidate commit's bytes.

READ-ONLY. md5 of data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py at candidate commit 88c7018366 (git show, never the
working tree) against head-object's ETag of s3://opal-data-49financial/_code/a07_dim_asset_classification.py (single-part SSE-S3, so the
ETag is the md5). Runs only from a principal the 49financial bucket admits (dell1's does not). Prints E42-A07 ok=<bool> candidate=<md5>
live=<etag>. Run from the repo root of a checkout that holds 88c7018366.
"""
import hashlib
import subprocess
import sys

import boto3

CANDIDATE = "88c7018366"
SRC = "data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py"
BUCKET, KEY = "opal-data-49financial", "_code/a07_dim_asset_classification.py"


def main():
    body = subprocess.run(["git", "show", f"{CANDIDATE}:{SRC}"], capture_output=True, check=True).stdout
    cand = hashlib.md5(body).hexdigest()  # noqa: S324 -- an S3 ETag comparison, not a security use
    live = boto3.client("s3", region_name="us-east-1").head_object(Bucket=BUCKET, Key=KEY)["ETag"].strip('"')
    ok = live == cand
    print(f"E42-A07 ok={ok} candidate={cand} live={live}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
