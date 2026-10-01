"""Part 6 of the serving prep: the 1.2 producer on a 49 Financial day, row for row against the SERVED partition (reads only).

Usage: python producer_f49_row_compare.py <worktree root> <day> [<day> ...]

The 49 Financial daily gold is written by the live Lambda (producer pinned at 363dc1fda4, emission 1.1). The producer on CLOUD
(emission 1.2) would replace it when the shared artifact is rebuilt. For each day: compute the day with the CLOUD producer (no
write), read the served partition, and compare every shared column on every account. Expected differences: `schema_version`
(1.1 -> 1.2) and one added column, `span_trading_days` = 1.
"""
from __future__ import annotations

import importlib.util
import io
import math
import sys

import boto3
import pandas as pd

root = sys.argv[1]
spec = importlib.util.spec_from_file_location("hp_cloud", root + "/data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py")
hp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hp)
s3 = boto3.client("s3", region_name="us-east-1")
doc = hp.load_declaration()
source = next(s for s in hp.declared_sources(doc) if doc[s]["positions_prefix"].startswith("schwab/"))
firm = hp.firm_scope(doc[source])
orig = hp.read_partition


def retrying(s3c, bucket, prefix, day, columns=None):
    for attempt in range(5):
        try:
            return orig(s3c, bucket, prefix, day, columns=columns)
        except Exception as exc:  # this network drops body reads; the read is repeated whole
            if attempt == 4 or "imeout" not in type(exc).__name__ + str(exc):
                raise


hp.read_partition = retrying
ok_all = True
for day in sys.argv[2:]:
    frame, note = hp.compute_day(s3, doc, source, day, cache=hp.PartitionCache(8), implausible=hp.ImplausibleIndex())
    uri = hp.opal_naming.address("irpt", firm, "gold", hp.TABLE_DAILY, "date=%s" % day)
    bucket, _, key = uri[5:].partition("/")
    served = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=bucket, Key=key + "/data.parquet")["Body"].read()))
    a = frame.set_index("account_id")
    b = served.set_index("account_id")
    shared_cols = [c for c in b.columns if c in a.columns]
    only_new = [c for c in a.columns if c not in b.columns]
    only_old = [c for c in b.columns if c not in a.columns]
    ids = sorted(set(a.index) & set(b.index))
    unequal = {}
    for c in shared_cols:
        n = 0
        for i in ids:
            x, y = a.at[i, c], b.at[i, c]
            if isinstance(x, float) and isinstance(y, float):
                same = (math.isnan(x) and math.isnan(y)) or x == y
            else:
                same = (pd.isna(x) and pd.isna(y)) or x == y
            n += 0 if same else 1
        if n:
            unequal[c] = n
    spans = sorted(int(v) for v in frame["span_trading_days"].unique())
    ok = (set(unequal) <= {"schema_version"} and len(a) == len(b) == len(ids) and only_new == ["span_trading_days"] and not only_old and spans == [1])
    ok_all = ok_all and ok
    print("%s (%s): computed %d rows, served %d rows, accounts in both %d; shared columns %d; unequal on any row: %s; "
          "columns only in the new build %s, only in the served %s; span values %s; note '%s' -> %s"
          % (day, source, len(a), len(b), len(ids), len(shared_cols), unequal or "none", only_new, only_old, spans, note[:60],
             "AS EXPECTED" if ok else "NOT AS EXPECTED"))
print("RESULT: %s" % ("every day as expected" if ok_all else "a day differs beyond schema_version and the added column"))
