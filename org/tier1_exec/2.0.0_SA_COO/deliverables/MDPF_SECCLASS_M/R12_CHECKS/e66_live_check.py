"""SC-e-66 push read: the BD silver builder key reads the candidate bytes and the one new test key exists (opal-data-bd).

  python e66_live_check.py
Prints  E66-LIVE ok=<bool> builder_etag=<etag> test_key=<present|absent>
"""
import boto3

BUCKET = "opal-data-bd"
BUILDER = "code/silver/build_bd_assets_dim.py"
TEST = "code/silver/tests/test_assets_dim_union_canonical.py"
CANDIDATE_MD5 = "152374b5797d9cd0d87f768dd40c7f47"

s3 = boto3.client("s3", region_name="us-east-1")
etag = s3.head_object(Bucket=BUCKET, Key=BUILDER)["ETag"].strip('"')
try:
    s3.head_object(Bucket=BUCKET, Key=TEST)
    test = "present"
except s3.exceptions.ClientError as e:
    if e.response.get("Error", {}).get("Code") not in ("404", "NoSuchKey", "NotFound"):
        raise
    test = "absent"
print(f"E66-LIVE ok={etag == CANDIDATE_MD5 and test == 'present'} builder_etag={etag} test_key={test}")
