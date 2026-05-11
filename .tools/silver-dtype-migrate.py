"""In-place silver dtype migration — read each silver/* parquet, coerce IDs to Int64, rewrite same key.

ADVI_INFNNA.SILVER-ID-DTYPE-UNIFY alternative path (pending Andrew approval).
~5-10min total vs ~3-4h full rebuild. Same canonical Int64 end-state.

Use only when:
- Silver data values are correct as-is (no transformation changes needed)
- Helper `coerce_silver_ids` is idempotent and dtype-only

Coverage: every silver/* parquet under S3_BUCKET that lives at a per-date or
per-snapshot prefix listed in `MIGRATE_PREFIXES`. Add prefixes as needed.

USAGE:
  python .runtmp/silver-dtype-migrate.py                  # all prefixes
  python .runtmp/silver-dtype-migrate.py --prefix silver/transactions/
  python .runtmp/silver-dtype-migrate.py --dry-run        # list only, no writes
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from io import BytesIO
from threading import Lock

import boto3
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "data", "orion", "scripts", "silver"))
from _orion_api_silver_lib import coerce_silver_ids  # noqa: E402

S3_BUCKET = "opal-data-inf"
MIGRATE_PREFIXES = [
    "silver/transactions/",
    "silver/api_dims/accounts_v2/",
    "silver/api_dims/positions_mv/",
    "silver/api_dims/performance/",
    "silver/api_dims/tax_realized/",
    "silver/api_dims/tax_unrealized/",
    "silver/api_dims/billing/",
    "silver/api_dims/activity/",
    "silver/api_dims/household/",
    "silver/api_dims/household_rep_mapping/",
    "silver/api_dims/assets_v2/",
    "silver/api_dims/representatives/",
]
WORKERS = 32

_log_lock = Lock()
_counter_lock = Lock()


def _log(msg: str) -> None:
    with _log_lock:
        print(f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {msg}", flush=True)


def list_keys(s3, prefix: str) -> list[str]:
    paginator = s3.get_paginator("list_objects_v2")
    out: list[str] = []
    for page in paginator.paginate(Bucket=S3_BUCKET, Prefix=prefix):
        for obj in page.get("Contents", []) or []:
            k = obj["Key"]
            if k.endswith(".parquet"):
                out.append(k)
    return out


def migrate_one(s3, key: str, dry_run: bool) -> tuple[str, str, int, int]:
    """Returns (key, status, before_bytes, after_bytes). status in {'ok', 'skip-no-id-cols', 'dry'}."""
    obj = s3.get_object(Bucket=S3_BUCKET, Key=key)
    raw = obj["Body"].read()
    before_bytes = len(raw)
    df = pd.read_parquet(BytesIO(raw))

    id_cols_present = [c for c in df.columns if c.endswith("_id") or c in ("trans_id",)]
    if not id_cols_present:
        return (key, "skip-no-id-cols", before_bytes, before_bytes)

    df = coerce_silver_ids(df)

    if dry_run:
        return (key, "dry", before_bytes, before_bytes)

    buf = BytesIO()
    df.to_parquet(buf, index=False, engine="pyarrow", compression="snappy")
    buf.seek(0)
    body = buf.getvalue()
    s3.put_object(Bucket=S3_BUCKET, Key=key, Body=body, ServerSideEncryption="AES256")
    return (key, "ok", before_bytes, len(body))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--prefix", default=None,
                   help="single prefix (default: all in MIGRATE_PREFIXES)")
    p.add_argument("--workers", type=int, default=WORKERS)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    s3 = boto3.client("s3", region_name="us-east-1")

    prefixes = [args.prefix] if args.prefix else MIGRATE_PREFIXES

    all_keys: list[str] = []
    for prefix in prefixes:
        keys = list_keys(s3, prefix)
        _log(f"{prefix}: {len(keys):,} parquet keys")
        all_keys.extend(keys)

    _log(f"Total: {len(all_keys):,} keys to migrate (dry_run={args.dry_run}, workers={args.workers})")
    t0 = time.time()

    ok = 0
    skip = 0
    fail = 0
    failures: list[tuple[str, str]] = []
    bytes_before = 0
    bytes_after = 0
    done = 0

    def _worker_one(k: str):
        return migrate_one(s3, k, args.dry_run)

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(_worker_one, k): k for k in all_keys}
        for fut in as_completed(futures):
            k = futures[fut]
            try:
                key, status, bb, ba = fut.result()
                bytes_before += bb
                bytes_after += ba
                if status == "ok" or status == "dry":
                    ok += 1
                else:
                    skip += 1
            except Exception as exc:
                fail += 1
                failures.append((k, f"{type(exc).__name__}: {exc}"))
            with _counter_lock:
                done += 1
            if done % 500 == 0:
                elapsed = time.time() - t0
                rate = done / max(elapsed, 1)
                eta = (len(all_keys) - done) / max(rate, 1e-6) / 60.0
                _log(f"Progress: {done}/{len(all_keys)} "
                     f"({rate:.1f}/s; ETA {eta:.1f} min); fail={fail}")

    elapsed = time.time() - t0
    _log(f"DONE in {elapsed/60:.1f} min — ok={ok} skip={skip} fail={fail} "
         f"size_before={bytes_before/1e6:.1f}MB size_after={bytes_after/1e6:.1f}MB")
    if failures:
        _log("FAILURES:")
        for k, err in failures[:20]:
            _log(f"  {k}: {err}")
        if len(failures) > 20:
            _log(f"  ... +{len(failures)-20} more")

    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
