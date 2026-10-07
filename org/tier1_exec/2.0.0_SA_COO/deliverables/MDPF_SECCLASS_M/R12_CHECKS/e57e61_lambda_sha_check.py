#!/usr/bin/env python3
"""e57e61_lambda_sha_check.py -- MDPF_SECCLASS SC-e-57 + SC-e-61 release: the live FWD-10 producer runs the new artifact.

READ-ONLY. Reads the function's CodeSha256 and the artifact object's `content-sha256` metadata. ok when they are equal and both differ
from the pre-port sha (f0zhRV1F..., read 2026-10-07T15:4xZ), so the live function runs the rebuilt artifact. Prints E57E61-LIVE
ok=<bool> live=<sha> artifact=<sha> prior=<sha>.
"""
import sys

import boto3

FUNCTION = "mdpf-secclass-new-security-lambda"
BUCKET = "opal-313476888478-lambda-artifacts"
KEY = "mdpf-secclass/mdpf-secclass-new-security-lambda.zip"
PRIOR = "f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ="


def main():
    live = boto3.client("lambda", region_name="us-east-1").get_function_configuration(FunctionName=FUNCTION)["CodeSha256"]
    meta = boto3.client("s3", region_name="us-east-1").head_object(Bucket=BUCKET, Key=KEY).get("Metadata", {})
    art = meta.get("content-sha256", "")
    ok = live == art and live != PRIOR
    print(f"E57E61-LIVE ok={ok} live={live} artifact={art} prior={PRIOR}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
