#!/usr/bin/env python3
"""Is a coerced bronze positions .parquet equal, row for row, to the raw .jsonl.gz of the same date, on the columns the silver
converter reads? (1.0.0_SA_CTO rulings batch 63 item 5; rows IRPT_BCKEND-S216, W99)

    python coerced_positions_equality.py <repo root> [<date> <date> <date>]

The Inflection positions feed has two producers in opal-data-inf bronze/positions/: the raw `<date>.jsonl.gz` and a coerced
`<date>.parquet`. For 2026-09-28 and 2026-09-29 only the parquet exists. Batch 63 item 5 admits the coerced 2026-09-29 parquet for
that ONE date if, and only if, on three dates where BOTH forms exist the columns the silver converter reads are equal row for row.

"The columns the silver converter reads" = `mirror_schemas.DECLARED[("orion", "positions")]` in the converter's own package
(imported from the repo, not retyped). Rows are matched on `id` (the feed's stable key). A value is compared after the converter's
own type law: float64 as float, int64 as int, bool as bool, string as str, a null as a null (a null and an empty string are
DIFFERENT and are counted as unequal). Printed per date: both row counts, the key sets, the columns present in each form, and per
column the number of unequal rows with the denominator. Default dates: the last three on which both forms exist. Reads only.
"""
from __future__ import annotations

import gzip
import io
import json
import math
import sys

import boto3
import pandas as pd

BUCKET = "opal-data-inf"
PREFIX = "bronze/positions/"


def norm(value, kind):
    """One cell under the converter's type law; None for a null of any spelling."""
    if value is None or (isinstance(value, float) and math.isnan(value)) or value is pd.NA or value is pd.NaT:
        return None
    if kind == "float64":
        return float(value)
    if kind == "int64":
        return int(value)
    if kind == "bool":
        return bool(value)
    if isinstance(value, (dict, list)):
        return json.dumps(value, separators=(",", ":"), sort_keys=True)
    return str(value)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = sys.argv[1]
    sys.path.insert(0, root + "/infra/aws/lambda/opal-assets/opal-assets-silver-orion")
    import mirror_schemas

    declared = mirror_schemas.DECLARED[("orion", "positions")]
    s3 = boto3.client("s3", region_name="us-east-1")

    def body(key):
        """The whole object, re-read on a body that times out mid-stream: a date is never compared on a part."""
        for attempt in range(4):
            try:
                return s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()
            except Exception:
                if attempt == 3:
                    raise

    keys = [o["Key"] for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=PREFIX)
            for o in page.get("Contents", [])]
    raw = {k[len(PREFIX):-len(".jsonl.gz")] for k in keys if k.endswith(".jsonl.gz")}
    coerced = {k[len(PREFIX):-len(".parquet")] for k in keys if k.endswith(".parquet")}
    both = sorted(raw & coerced)
    only_coerced = sorted(coerced - raw)
    print("%s%s: %d keys; raw .jsonl.gz dates %d; coerced .parquet dates %d; both forms %d; ONLY coerced %d (last five: %s)"
          % (BUCKET + "/", PREFIX, len(keys), len(raw), len(coerced), len(both), len(only_coerced), only_coerced[-5:]))
    dates = sys.argv[2:] or both[-3:]
    print("converter's declared columns for (orion, positions): %d" % len(declared))
    verdicts = []
    for d in dates:
        if d not in raw or d not in coerced:
            print("== %s: both forms do NOT exist (raw %s, coerced %s)" % (d, d in raw, d in coerced))
            verdicts.append(False)
            continue
        blob = body("%s%s.jsonl.gz" % (PREFIX, d))
        recs = [json.loads(ln) for ln in gzip.decompress(blob).decode("utf-8").splitlines() if ln.strip()]
        pq = pd.read_parquet(io.BytesIO(body("%s%s.parquet" % (PREFIX, d))))
        raw_cols = sorted({k for r in recs for k in r})
        missing_in_pq = [c for c in declared if c not in pq.columns]
        missing_in_raw = [c for c in declared if c not in raw_cols]
        extra_pq = [c for c in pq.columns if c not in declared]
        raw_by = {r["id"]: r for r in recs}
        pq_by = {int(r["id"]): r for r in pq.to_dict("records")}
        shared = sorted(set(raw_by) & set(pq_by))
        print("== %s: raw %d rows (%d distinct id), coerced %d rows (%d distinct id); ids in both %d, only raw %d, only coerced %d"
              % (d, len(recs), len(raw_by), len(pq), len(pq_by), len(shared), len(set(raw_by) - set(pq_by)), len(set(pq_by) - set(raw_by))))
        print("   declared columns absent from the coerced form: %s; absent from the raw form: %s; coerced-only columns: %s"
              % (missing_in_pq or "none", missing_in_raw or "none", extra_pq or "none"))
        unequal = {}
        for col, kind in declared.items():
            if col in missing_in_pq:
                continue
            n = 0
            example = None
            for i in shared:
                a, b = norm(raw_by[i].get(col), kind), norm(pq_by[i].get(col), kind)
                if a != b:
                    n += 1
                    example = example or (i, a, b)
            if n:
                unequal[col] = (n, example)
        compared = len(declared) - len(missing_in_pq)
        print("   columns compared %d of %d declared over %d shared rows: equal on every row %d; unequal %d"
              % (compared, len(declared), len(shared), compared - len(unequal), len(unequal)))
        for col, (n, ex) in sorted(unequal.items(), key=lambda kv: -kv[1][0]):
            print("     %-28s unequal on %6d of %d rows; e.g. id %s raw %r coerced %r" % (col, n, len(shared), ex[0], ex[1], ex[2]))
        ok = (not unequal and not missing_in_pq and len(shared) == len(raw_by) == len(pq_by) == len(recs) == len(pq))
        verdicts.append(ok)
        print("   EQUAL row for row on the converter's columns: %s" % ok)
    print("RESULT: %d of %d dates equal -> the coerced form is %s by the three-date rule"
          % (sum(verdicts), len(verdicts), "ADMISSIBLE" if verdicts and all(verdicts) else "NOT admissible"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
