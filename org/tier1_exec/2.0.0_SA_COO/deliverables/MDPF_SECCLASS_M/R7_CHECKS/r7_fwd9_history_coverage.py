#!/usr/bin/env python3
"""
r7_fwd9_history_coverage.py -- MDPF_SECCLASS round 7, cell SC-e-18 (READ-ONLY).

FWD-9's second half: each Rival Funds stock's history (the G4 `security_market` series the holding modal reads) is
filled in back three years, or to its first trading day if younger; none reaches further back than three years.

What it does, and nothing else:
  1. The universe: non-cash `provider_security_type == "Equity"` across every canonical_shape day (newest revision per
     day), one per `security_bloomberg`.
  2. The series: reads `security_market` (columns pruned) and keeps, per security, the first and last `date` with a
     non-null `px_close`. The series is joined to the universe on `security_bloomberg`, then on `security_id`.
  3. One status per stock against the window `[max(run_day - 3 years, first trading day), run_day]`:
       COVERED_3Y  first <= target start
       STARTS_LATE first > target start (the table cannot show the first trading day, so this is never called a gap)
       NO_SERIES   no non-null px_close in any partition
       BEYOND_CAP  first < run_day - 3 years (FWD-9: no history reaches further back than three years)
     A series that reaches the cap exactly is COVERED_3Y; BEYOND_CAP is reported separately and not counted covered.

It writes no series and calls no vendor. Usage: python r7_fwd9_history_coverage.py [--run-day YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import pickle
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import boto3
import pyarrow as pa
import pyarrow.parquet as pq
from botocore.config import Config as BotoConfig
from botocore.exceptions import BotoCoreError, ClientError

ROOT = Path(__file__).resolve().parents[6]  # R7_CHECKS -> MDPF_SECCLASS_M -> deliverables -> 2.0.0_SA_COO -> tier1_exec -> org -> root
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BUCKET = "opal-data-etfs"
CANON = "rivalfunds/etfs/gold/canonical_shape/"
MARKET = "rivalfunds/etfs/gold/security_market/"
OUT = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_FWD9_HISTORY_COVERAGE_20261005.json"
CACHE = ROOT / ".scratch" / "r7_e18_cache"  # per-file reduced results; the key carries the revision, so it never goes stale
THREADS = 8
TRIES = 12

_S3 = boto3.client("s3", region_name="us-east-1", config=BotoConfig(
    retries={"max_attempts": 8, "mode": "standard"}, connect_timeout=15, read_timeout=60, max_pool_connections=THREADS * 2))


class _File:
    def __init__(self, key, size):
        self.path, self.size = key, size


def _retry(fn):
    """The laptop link drops connections and stalls reads: every S3 call is retried with a growing pause."""
    last = None
    for n in range(TRIES):
        try:
            return fn()
        except (BotoCoreError, ClientError, OSError) as exc:
            last = exc
            time.sleep(min(2.0 * (n + 1), 20))
    raise last


def _list(prefix: str):
    def go():
        out = []
        for pg in _S3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=prefix):
            out += [_File(o["Key"], o["Size"]) for o in pg.get("Contents", []) if o["Key"].endswith(".parquet")]
        return out
    return _retry(go)


def _read(path: str, columns):
    """One GET per file (these files are tens of KB, so a ranged column read costs the same bytes), then the
    column prune runs on the local bytes."""
    def go():
        raw = _S3.get_object(Bucket=BUCKET, Key=path)["Body"].read()
        return pq.ParquetFile(pa.BufferReader(raw)).read(columns=columns)
    return _retry(go)


def _cached(path: str, reduce_fn, columns):
    """reduce_fn(table) -> a small picklable value, cached under .scratch keyed by the full S3 key."""
    f = CACHE / (re.sub(r"[^A-Za-z0-9_.=-]", "_", path) + ".pkl")
    if f.exists():
        return pickle.loads(f.read_bytes())
    val = reduce_fn(_read(path, columns))
    CACHE.mkdir(parents=True, exist_ok=True)
    f.write_bytes(pickle.dumps(val))
    return val


def _years_back(day: dt.date, years: int) -> dt.date:
    try:
        return day.replace(year=day.year - years)
    except ValueError:  # Feb 29
        return day.replace(year=day.year - years, day=28)


def _next_trading_day(day: dt.date) -> dt.date:
    from lib.trading_calendar import is_trading_day
    while not is_trading_day(day):
        day += dt.timedelta(days=1)
    return day


def _reduce_canon(tb):
    df = tb.to_pandas()
    eq = df[(df["provider_security_type"] == "Equity") & (df["is_cash_line"] != True)]  # noqa: E712
    eq = eq[eq["security_bloomberg"].notna()]
    return int(len(df)), sorted({(r.security_bloomberg, r.security_id) for r in eq.itertuples()}, key=str)


def universe():
    files = _list(CANON)
    byday = collections.defaultdict(list)
    for i in files:
        m = re.search(r"date=(\d{4}-\d\d-\d\d)/holdings-([^/]+)\.parquet$", i.path)
        if m:
            byday[m.group(1)].append((m.group(2), i.path))
    newest = {d: max(v, key=lambda x: x[0])[1] for d, v in byday.items()}
    cols = ["security_bloomberg", "security_id", "provider_security_type", "is_cash_line"]
    with ThreadPoolExecutor(THREADS) as ex:
        res = list(ex.map(lambda p: _cached(p, _reduce_canon, cols), newest.values()))
    ids = collections.defaultdict(set)
    for _, pairs in res:
        for bbg, sid in pairs:
            ids[bbg].add(sid)
    return (sorted(ids), {k: sorted(x for x in v if x is not None) for k, v in ids.items()},
            {"canonical_files": len(files), "canonical_days": len(byday), "rows": sum(r[0] for r in res)})


def series():
    files = _list(MARKET)
    census = []
    by_bbg, by_sid = {}, {}
    cols = ["security_id", "security_bloomberg", "date", "px_close"]
    for i in sorted(files, key=lambda f: f.path):
        part = re.search(r"date=(\d{4}-\d\d-\d\d)/", i.path).group(1)
        df = _read(i.path, cols).to_pandas()
        census.append({"partition": part, "file": i.path.rsplit("/", 1)[-1], "bytes": i.size, "rows": int(len(df)),
                       "px_close_nonnull": int(df["px_close"].notna().sum())})
        df = df[df["px_close"].notna() & df["date"].notna()]
        for key, target in (("security_bloomberg", by_bbg), ("security_id", by_sid)):
            g = df.groupby(key)["date"].agg(["min", "max"])
            for k, row in g.iterrows():
                lo, hi = row["min"], row["max"]
                cur = target.get(k)
                target[k] = (lo, hi) if cur is None else (min(cur[0], lo), max(cur[1], hi))
    return by_bbg, by_sid, census


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-day", default=dt.date.today().isoformat())
    args = ap.parse_args()
    run_day = dt.date.fromisoformat(args.run_day)
    cap = _years_back(run_day, 3)
    target = _next_trading_day(cap)

    stocks, sids, ucensus = universe()
    by_bbg, by_sid, census = series()

    rows = []
    for s in stocks:
        hit, via = by_bbg.get(s), "security_bloomberg"
        if hit is None:
            for sid in sids.get(s, []):
                if sid in by_sid:
                    hit, via = by_sid[sid], "security_id"
                    break
        if hit is None:
            rows.append({"security_bloomberg": s, "first": None, "last": None, "status": "NO_SERIES", "joined_by": None})
            continue
        first, last = hit
        if first < cap:
            status = "BEYOND_CAP"
        elif first <= target:
            status = "COVERED_3Y"
        else:
            status = "STARTS_LATE"
        rows.append({"security_bloomberg": s, "first": str(first), "last": str(last), "status": status, "joined_by": via})

    n = collections.Counter(r["status"] for r in rows)
    parts = sorted({c["partition"] for c in census})
    doc = {
        "cell": "SC-e-18", "run_day": str(run_day), "window_cap_start": str(cap), "target_start": str(target),
        "target_rule": "max(run_day - 3 years, first trading day); first trading day not knowable from security_market",
        "security_market": {"identity_columns": ["security_id", "security_bloomberg"], "joined_on": "security_bloomberg, then security_id",
                            "partitions": len(parts), "first_partition": parts[0] if parts else None,
                            "last_partition": parts[-1] if parts else None, "files": census},
        "universe_source": ucensus,
        "counts": {"stocks": len(rows), "covered_3y": n["COVERED_3Y"], "starts_late": n["STARTS_LATE"],
                   "no_series": n["NO_SERIES"], "beyond_cap": n["BEYOND_CAP"]},
        "stocks": rows,
    }
    OUT.write_text(json.dumps(doc, indent=1, sort_keys=False) + "\n", encoding="ascii")
    print("FWD9-HISTORY-COVERAGE stocks=%d covered_3y=%d starts_late=%d no_series=%d beyond_cap=%d "
          "security_market_partitions=%d first_partition=%s"
          % (len(rows), n["COVERED_3Y"], n["STARTS_LATE"], n["NO_SERIES"], n["BEYOND_CAP"], len(parts),
             parts[0] if parts else "NONE"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
