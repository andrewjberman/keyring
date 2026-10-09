#!/usr/bin/env python3
"""e65_shipped_etag_check.py -- MDPF_SECCLASS SC-e-65 explicit deploy: both shipped keys equal the merged cash-token module.

READ-ONLY. Reads md5 of infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py at the repo's HEAD bytes (git show HEAD:,
never the working tree) and requires it to be the signed candidate (3f1e6be8910952f33c88bf100c610ab6, commit 16092a4806). Then reads
head-object's ETag of code/gold/lib/_shared/etf_classification_scheduled.py in opal-data-bd and opal-data-cot (single-part SSE-S3,
so the ETag is the md5). Positive control: the unchanged member etf_classifications_dynamodb.py must match HEAD in both buckets, so a
match is not a broken read. Prints E65-SHIPPED ok=<bool> head=<md5> bd=<etag> cot=<etag> control=<MATCH|DIFF>. Run from the repo
root.
"""
import hashlib
import subprocess
import sys

import boto3

CANDIDATE = sys.argv[1] if len(sys.argv) > 1 else "3f1e6be8910952f33c88bf100c610ab6"  # e65b: pass 40ffa3fa...
KEY = "code/gold/lib/_shared/{}"
SRC = "infra/aws/lambda/v2_portal/_shared/{}"
BUCKETS = ("opal-data-bd", "opal-data-cot")


def head_md5(name):
    out = subprocess.run(["git", "show", "HEAD:" + SRC.format(name)], capture_output=True, check=True).stdout
    return hashlib.md5(out).hexdigest()  # noqa: S324 -- an S3 ETag comparison, not a security use


def etag(s3, bucket, name):
    return s3.head_object(Bucket=bucket, Key=KEY.format(name))["ETag"].strip('"')


def main():
    s3 = boto3.client("s3", region_name="us-east-1")
    head = head_md5("etf_classification_scheduled.py")
    tags = {b: etag(s3, b, "etf_classification_scheduled.py") for b in BUCKETS}
    ctl_src = head_md5("etf_classifications_dynamodb.py")
    control = "MATCH" if all(etag(s3, b, "etf_classifications_dynamodb.py") == ctl_src for b in BUCKETS) else "DIFF"
    ok = head == CANDIDATE and all(t == CANDIDATE for t in tags.values()) and control == "MATCH"
    print(f"E65-SHIPPED ok={ok} head={head} bd={tags['opal-data-bd']} cot={tags['opal-data-cot']} control={control}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
