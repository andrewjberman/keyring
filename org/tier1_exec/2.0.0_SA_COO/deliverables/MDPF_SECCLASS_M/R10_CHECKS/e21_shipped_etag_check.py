#!/usr/bin/env python3
"""e21_shipped_etag_check.py -- MDPF_SECCLASS SC-e-21 explicit deploy: both shipped keys equal the trunk's module.

READ-ONLY. Reads md5 of infra/aws/lambda/v2_portal/_shared/etf_classification.py at the repo's HEAD bytes (git show HEAD:, never the
working tree) and head-object's ETag of code/gold/lib/_shared/etf_classification.py in opal-data-bd and opal-data-cot (single-part
SSE-S3 objects, so the ETag is the md5). Positive control: the unchanged member etf_classifications_dynamodb.py must also match in both
buckets, so a match is not a broken read. Prints E21-SHIPPED ok=<bool> trunk=<md5> bd=<etag> cot=<etag> control=<MATCH|DIFF>.
Run from the repo root.
"""
import hashlib
import subprocess
import sys

import boto3

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
    trunk = head_md5("etf_classification.py")
    tags = {b: etag(s3, b, "etf_classification.py") for b in BUCKETS}
    ctl_src = head_md5("etf_classifications_dynamodb.py")
    control = "MATCH" if all(etag(s3, b, "etf_classifications_dynamodb.py") == ctl_src for b in BUCKETS) else "DIFF"
    ok = all(t == trunk for t in tags.values()) and control == "MATCH"
    print(f"E21-SHIPPED ok={ok} trunk={trunk} bd={tags['opal-data-bd']} cot={tags['opal-data-cot']} control={control}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
