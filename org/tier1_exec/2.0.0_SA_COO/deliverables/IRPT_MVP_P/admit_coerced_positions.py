#!/usr/bin/env python3
"""THE ONE PATH by which a coerced Inflection positions file becomes a silver partition (1.0.0_SA_CTO rulings batch 63 item 5,
batch 81 items 2-5; rows IRPT_BCKEND-S216, S245).

    python admit_coerced_positions.py <repo root> --control <date> [<date> ...]     # reads only; writes nothing
    python admit_coerced_positions.py <repo root> --admit <date> --write            # one ADMITTED date, under both halves

WHAT IT IS FOR. The converter (opal-assets-silver-orion) refuses a `.parquet` under bronze by design, and the mirror never copies
one: a coerced day is not a raw day. Two rulings admit exactly two dates whose raw file never existed, each on a measured
row-for-row equality of the coerced and raw forms on that date's own neighbours (`coerced_positions_equality.py`). Nothing else
takes this path: `--admit` refuses any date not in ADMITTED below, refuses a date whose silver partition already exists, and the
converter and the mirror are not changed and still refuse.

HOW. The coerced file `s3://opal-data-inf/bronze/positions/<date>.parquet` is read with pyarrow (exact python values, nulls as
nulls), re-serialised as the JSON lines the raw file would have carried, and passed through the CONVERTER'S OWN code, imported
from the repo and not retyped: `mirror_conversion._orion_tables` (declared 59-column schema, drift gate, exact dedup, provenance)
and `stream_parquet.stream_to_parquet` (atomic, read-back verified). The partition's `_source_file` is the coerced file's own
name, `<date>.parquet`: that is its provenance, and it is how the one earlier admission in this monolith reads
(fact_assets/date=2026-08-06, written 2026-08-14).

`--control <date>` is the proof the path is exact: for a date whose RAW file exists, the table this path builds from the COERCED
file is compared with the silver partition the converter itself built from the raw file -- every column, every row matched on
`id`. Only `_source_file` may differ. A control that is not equal means the path is not exact and nothing is admitted on it.
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

SOURCE_BUCKET = "opal-data-inf"
SOURCE_PREFIX = "bronze/positions/"
# date -> the ruling that admits it and the controls it was measured on. A date is added here only by a ruling.
ADMITTED = {
    "2026-09-29": "batch 63 item 5 and batch 81 item 1: coerced == raw on 59 of 59 columns at 2026-09-26, 2026-09-27, 2026-09-30",
    "2026-08-06": "batch 81 item 2: coerced == raw on 59 of 59 columns at 2026-08-04, 2026-08-05, 2026-08-07",
}
# NOT admitted, and why, so the absence is a decision and not an oversight (batch 81 item 3):
#   2026-07-01 -- its own control 2026-07-02 differs on 4 of 59 columns (9 rows); it stays a gap and is linked across.
#   2026-07-03, 2026-07-04, 2026-07-05, 2026-09-28 -- not asked about; not trading-day closes the producer needs.


def records_from_coerced(s3, date):
    raw = s3.get_object(Bucket=SOURCE_BUCKET, Key="%s%s.parquet" % (SOURCE_PREFIX, date))["Body"].read()
    table = pq.read_table(io.BytesIO(raw))
    recs = table.to_pylist()
    for r in recs:
        for k, v in r.items():
            if isinstance(v, float) and math.isnan(v):
                r[k] = None
    return recs, len(raw)


def build(mc, recs, date):
    """The converter's own table for these records: declared schema, drift gate, exact dedup, provenance."""
    lines = "\n".join(json.dumps(r, separators=(",", ":"), allow_nan=False) for r in recs)
    body = io.BytesIO(gzip.compress(lines.encode("utf-8")))
    stats, seen = {"rows_in": 0, "dupes": 0}, set()
    tables = mc._orion_tables(body, "%s%s.parquet" % (SOURCE_PREFIX, date), "positions", date, stats, seen)
    return tables, stats


def cell(v):
    return None if isinstance(v, float) and math.isnan(v) else v


def control(s3, mc, date):
    skey = mc._silver_key("orion", "inflection", "positions", date)
    try:
        existing = pq.read_table(io.BytesIO(s3.get_object(Bucket=mc.MONOLITH, Key=skey)["Body"].read()))
    except Exception as exc:
        print("== control %s: NO silver partition built from the raw file (%s) -- not a control" % (date, type(exc).__name__))
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
    src = sorted({r["_source_file"] for r in built.to_pylist()})
    ok = (same_schema and len(a) == len(b) == len(shared) == built.num_rows == existing.num_rows
          and set(unequal) <= {"_source_file"})
    print("== control %s: coerced file %d bytes, %d records, %d exact duplicates removed; built %d rows x %d columns; the "
          "converter's own partition %d rows x %d columns; schema equal %s; ids in both %d"
          % (date, nbytes, stats["rows_in"], stats["dupes"], built.num_rows, len(built.schema), existing.num_rows,
             len(existing.schema), same_schema, len(shared)))
    print("   columns unequal on any row: %s; built _source_file %s; EXACT except _source_file: %s"
          % (unequal or "none", src, ok))
    return ok


def admit(s3, mc, sp, ms, date, write):
    if date not in ADMITTED:
        raise SystemExit("REFUSED: %s is not an admitted date. Admitted: %s. A date is admitted by a ruling, never by this tool."
                         % (date, ", ".join(sorted(ADMITTED))))
    skey = mc._silver_key("orion", "inflection", "positions", date)
    if mc.partition_exists(s3, skey):
        raise SystemExit("REFUSED: s3://%s/%s already exists; this path never overwrites a partition." % (mc.MONOLITH, skey))
    raw_listing = s3.list_objects_v2(Bucket=SOURCE_BUCKET, Prefix="%s%s.jsonl.gz" % (SOURCE_PREFIX, date)).get("Contents", [])
    if raw_listing:
        raise SystemExit("REFUSED: a raw file exists for %s; the converter reads it, this path does not." % date)
    recs, nbytes = records_from_coerced(s3, date)
    tables, stats = build(mc, recs, date)
    print("admit %s (%s): coerced file %d bytes, %d records -> s3://%s/%s" % (date, ADMITTED[date], nbytes, len(recs), mc.MONOLITH, skey))
    if not write:
        built = pa.concat_tables(list(tables))
        print("DRY: would write %d rows x %d columns (%d exact duplicates removed); _source_file %s; nothing written"
              % (built.num_rows, len(built.schema), stats["dupes"], sorted({r["_source_file"] for r in built.to_pylist()})))
        return
    out = sp.stream_to_parquet(tables, ms.arrow_schema("orion", "positions"), s3, mc.MONOLITH, skey)
    print("WRITTEN: %s rows %s (records in %d, exact duplicates removed %d)" % (out.get("key"), out.get("rows"), stats["rows_in"], stats["dupes"]))


def main() -> int:
    if len(sys.argv) < 4 or sys.argv[2] not in ("--control", "--admit"):
        print(__doc__)
        return 2
    root = sys.argv[1]
    sys.path.insert(0, root + "/infra/aws/lambda/opal-assets/opal-assets-silver-orion")
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
