"""TR-t-3 AC3 -- the silver parquet written by the real run is readable back from the bucket, carries the declared
columns, has rows, and sits under the transcripts KMS key (issuer's check; at the base: FAIL as expected).

usage: python r1_silver_check.py <series> <transcript_id> <YYYY-MM-DD>
Prints SILVER-OK rows=N sse=aws:kms, else SILVER-MISSING/SILVER-BAD <reason>.
"""
import io
import sys

COLUMNS = ["transcript_id", "series", "meeting_date", "turn_index", "speaker", "start_utc", "end_utc",
           "start_s", "end_s", "text"]


def main(series, tid, day):
    sys.path.insert(0, ".")
    from lib.opal_naming import address  # noqa: E402
    import boto3  # noqa: E402
    import pyarrow.parquet as pq  # noqa: E402

    addr = address("teams", "transcripts", "silver", series, "date=%s" % day, "%s.parquet" % tid)
    bucket, key = addr[5:].split("/", 1)
    s3 = boto3.client("s3", region_name="us-east-1")
    try:
        head = s3.head_object(Bucket=bucket, Key=key)
    except Exception as e:  # noqa: BLE001
        print("SILVER-MISSING %s (%s)" % (addr, type(e).__name__))
        return 1
    sse = head.get("ServerSideEncryption")
    body = s3.get_object(Bucket=bucket, Key=key)["Body"].read()
    table = pq.read_table(io.BytesIO(body))
    cols = table.column_names
    missing = [c for c in COLUMNS if c not in cols]
    if missing:
        print("SILVER-BAD missing columns %s (have %s)" % (missing, cols))
        return 1
    if table.num_rows < 1:
        print("SILVER-BAD zero rows")
        return 1
    if sse != "aws:kms":
        print("SILVER-BAD sse=%r" % sse)
        return 1
    print("SILVER-OK rows=%d sse=%s key=%s speakers=%d" % (
        table.num_rows, sse, head.get("SSEKMSKeyId", "?")[-12:], len(set(table.column("speaker").to_pylist()))))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("SILVER-BAD usage")
        sys.exit(2)
    sys.exit(main(*sys.argv[1:]))
