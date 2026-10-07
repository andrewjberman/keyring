#!/usr/bin/env python3
"""The ASSETS twin of admit_coerced_positions.py (org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/), for ONE date.

    python admit_coerced_assets.py <repo root> --control <date> [<date> ...]     # reads only; writes nothing
    python admit_coerced_assets.py <repo root> --admit 2026-09-29                # DRY: builds, prints, writes nothing
    python admit_coerced_assets.py <repo root> --admit 2026-09-29 --write        # the one put

WHY. Andrew-direct 2026-10-07 ~08:1xZ (ANDREW_DIRECT_20261007_081xZ_INFLECTION_OTHER_AUM_MISSING_0928_SURGICAL_FIX.md): the
Model Portfolios AUM trend shows no "Other AUM" for Inflection on 2026-09-28. Cause: the raw Orion assets pull of 2026-09-29
(`s3://opal-data-inf/bronze/assets/2026-09-29.jsonl.gz`) never landed, so silver `fact_assets/date=2026-09-29` -- the
partition that holds the 2026-09-28 close -- was never built. The coerced file of the same pull, `2026-09-29.parquet`, exists.

HOW. Same path as the positions twin, with the feed changed and nothing else: the coerced file is read with pyarrow,
re-serialised as the JSON lines the raw file would have carried, and passed through the CONVERTER'S OWN code
(`mirror_conversion._orion_tables`, `stream_parquet.stream_to_parquet`), imported from the repo. `_source_file` is the coerced
file's own name. `--control` proves the path exact on dates whose raw file exists. `--admit` refuses any other date, refuses
a partition that already exists, and refuses when a raw file exists.
"""
from __future__ import annotations

import gzip
import io
import json
import math
import sys

import boto3
import pyarrow as pa
import pyarrow.parquet as pq

FEED = "assets"
SOURCE_BUCKET = "opal-data-inf"
SOURCE_PREFIX = "bronze/assets/"
ADMITTED = {
    "2026-09-29": "Andrew-direct 2026-10-07 ~08:1xZ: the true 2026-09-28 Other AUM; controls 2026-09-27, 2026-09-28, 2026-09-30",
}


def records_from_coerced(s3, date):
    raw = s3.get_object(Bucket=SOURCE_BUCKET, Key="%s%s.parquet" % (SOURCE_PREFIX, date))["Body"].read()
    recs = pq.read_table(io.BytesIO(raw)).to_pylist()
    for r in recs:
        for k, v in r.items():
            if isinstance(v, float) and math.isnan(v):
                r[k] = None
    return recs, len(raw)


def build(mc, recs, date):
    lines = "\n".join(json.dumps(r, separators=(",", ":"), allow_nan=False) for r in recs)
    body = io.BytesIO(gzip.compress(lines.encode("utf-8")))
    stats, seen = {"rows_in": 0, "dupes": 0}, set()
    tables = mc._orion_tables(body, "%s%s.parquet" % (SOURCE_PREFIX, date), FEED, date, stats, seen)
    return tables, stats


def cell(v):
    return None if isinstance(v, float) and math.isnan(v) else v


def control(s3, mc, date):
    skey = mc._silver_key("orion", "inflection", FEED, date)
    try:
        existing = pq.read_table(io.BytesIO(s3.get_object(Bucket=mc.MONOLITH, Key=skey)["Body"].read()))
    except Exception as exc:
        print("== control %s: NO silver partition at %s (%s) -- not a control" % (date, skey, type(exc).__name__))
        return False
    recs, nbytes = records_from_coerced(s3, date)
    tables, stats = build(mc, recs, date)
    built = pa.concat_tables(list(tables))
    same_schema = built.schema.equals(existing.schema)
    a = {r["id"]: r for r in built.to_pylist()}
    b = {r["id"]: r for r in existing.to_pylist()}
    shared = sorted(set(a) & set(b))
    unequal = {}
    for col in existing.schema.names:
        n = sum(1 for i in shared if cell(a[i].get(col)) != cell(b[i].get(col)))
        if n:
            unequal[col] = n
    ok = (same_schema and len(a) == len(b) == len(shared) == built.num_rows == existing.num_rows
          and set(unequal) <= {"_source_file"})
    print("== control %s (%s): coerced %d bytes, %d records, %d duplicates removed; built %d rows x %d cols; converter's own "
          "%d rows x %d cols; schema equal %s; ids in both %d; columns unequal: %s; EXACT except _source_file: %s"
          % (date, skey, nbytes, stats["rows_in"], stats["dupes"], built.num_rows, len(built.schema), existing.num_rows,
             len(existing.schema), same_schema, len(shared), unequal or "none", ok))
    return ok


def admit(s3, mc, sp, ms, date, write):
    if date not in ADMITTED:
        raise SystemExit("REFUSED: %s is not an admitted date. Admitted: %s." % (date, ", ".join(sorted(ADMITTED))))
    skey = mc._silver_key("orion", "inflection", FEED, date)
    if mc.partition_exists(s3, skey):
        raise SystemExit("REFUSED: s3://%s/%s already exists; this path never overwrites a partition." % (mc.MONOLITH, skey))
    if s3.list_objects_v2(Bucket=SOURCE_BUCKET, Prefix="%s%s.jsonl.gz" % (SOURCE_PREFIX, date)).get("Contents", []):
        raise SystemExit("REFUSED: a raw file exists for %s; the converter reads it, this path does not." % date)
    recs, nbytes = records_from_coerced(s3, date)
    tables, stats = build(mc, recs, date)
    print("admit %s (%s): coerced file %d bytes, %d records -> s3://%s/%s" % (date, ADMITTED[date], nbytes, len(recs), mc.MONOLITH, skey))
    if not write:
        built = pa.concat_tables(list(tables))
        total = sum(float(r["currentValue"] or 0.0) for r in built.to_pylist())
        print("DRY: would write %d rows x %d columns (%d duplicates removed); _source_file %s; sum(currentValue) %.2f; "
              "nothing written" % (built.num_rows, len(built.schema), stats["dupes"],
                                   sorted({r["_source_file"] for r in built.to_pylist()}), total))
        return
    out = sp.stream_to_parquet(tables, ms.arrow_schema("orion", FEED), s3, mc.MONOLITH, skey)
    print("WRITTEN: %s rows %s (records in %d, duplicates removed %d)" % (out.get("key"), out.get("rows"), stats["rows_in"], stats["dupes"]))


def main() -> int:
    if len(sys.argv) < 4 or sys.argv[2] not in ("--control", "--admit"):
        print(__doc__)
        return 2
    sys.path.insert(0, sys.argv[1] + "/infra/aws/lambda/opal-assets/opal-assets-silver-orion")
    import mirror_conversion as mc
    import mirror_schemas as ms
    import stream_parquet as sp

    s3 = boto3.client("s3", region_name="us-east-1")
    if sys.argv[2] == "--control":
        results = [control(s3, mc, d) for d in sys.argv[3:]]
        print("RESULT: %d of %d controls exact" % (sum(results), len(results)))
        return 0 if all(results) else 1
    admit(s3, mc, sp, ms, sys.argv[3], "--write" in sys.argv[4:])
    return 0


if __name__ == "__main__":
    sys.exit(main())
