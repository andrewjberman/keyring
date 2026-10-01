"""TR-v-2 AC2 -- every held Teams transcript in bronze has a readable, non-empty silver parquet (issuer's check).

Lists bronze sidecars (<ID>.graph.json) for the three reachable series at the builder's addresses and the silver
parquets beside them; reads each parquet's row count from the bucket. Prints
SILVER-CENSUS bronze=B silver=S missing=M empty=E per_series=<series:b/s,...>, exit 0 only when missing == empty == 0.
Base: FAIL (bronze 30, silver 1). Counts only; never text.
"""
import io
import sys

SERIES = ("monday_meeting", "ocio_ic", "asset_management_ic")


def main():
    sys.path.insert(0, ".")
    import boto3  # noqa: E402
    import pyarrow.parquet as pq  # noqa: E402
    from lib.opal_naming import address  # noqa: E402

    s3 = boto3.client("s3", region_name="us-east-1")

    def prefix(tier, series):
        a = address("teams", "transcripts", tier, series, "date=2000-01-01", "x")
        bucket, key = a[5:].split("/", 1)
        return bucket, key.split("date=")[0]

    def keys(bucket, pfx):
        out, tok = [], None
        while True:
            kw = {"Bucket": bucket, "Prefix": pfx}
            if tok:
                kw["ContinuationToken"] = tok
            r = s3.list_objects_v2(**kw)
            out += [o["Key"] for o in r.get("Contents", [])]
            if not r.get("IsTruncated"):
                return out
            tok = r["NextContinuationToken"]

    b_total = s_total = missing = empty = 0
    per = []
    for series in SERIES:
        bb, bp = prefix("bronze", series)
        sb, sp = prefix("silver", series)
        bronze_ids = {k.rsplit("/", 1)[1][: -len(".graph.json")] for k in keys(bb, bp) if k.endswith(".graph.json")}
        silver = {k.rsplit("/", 1)[1][: -len(".parquet")]: k for k in keys(sb, sp) if k.endswith(".parquet")}
        for tid in bronze_ids:
            if tid not in silver:
                missing += 1
                continue
            body = s3.get_object(Bucket=sb, Key=silver[tid])["Body"].read()
            if pq.read_table(io.BytesIO(body)).num_rows < 1:
                empty += 1
        b_total += len(bronze_ids)
        s_total += len(set(silver) & bronze_ids)
        per.append("%s:%d/%d" % (series, len(bronze_ids), len(set(silver) & bronze_ids)))
    print("SILVER-CENSUS bronze=%d silver=%d missing=%d empty=%d per_series=%s" % (b_total, s_total, missing, empty, ",".join(per)))
    return 0 if (missing == 0 and empty == 0 and b_total > 0) else 1


if __name__ == "__main__":
    sys.exit(main())
