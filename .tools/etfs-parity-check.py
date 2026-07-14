#!/usr/bin/env python3
"""etfs-parity-check -- THE CUTOVER GATE for the ETF net-assets laptop->cloud lift.

    python .tools/etfs-parity-check.py              # every date both producers wrote
    python .tools/etfs-parity-check.py 2026-07-14   # one date

WHAT THIS IS FOR
The cloud producer (`etfs-netassets-daily`, EventBridge 22:00Z) writes SILVER to a
SCRATCH prefix (`_cloudprobe/`). Andrew's laptop (Windows task "ETF NetAssets Daily
Probe", 18:00 ET) is STILL the real producer, writing live `silver/`. Both run daily.

    THE WINDOWS TASK IS DISABLED ONLY AFTER >=3 TRADING DAYS OF VALUE-BY-VALUE
    PARITY *ON THE ARTIFACT* -- never on rc=0, never on a producer's self-report.

This tool is the gate, and it exists as a COMMITTED TOOL rather than a one-off
because the cutover criterion must not live in one agent's head. It reads BOTH
sides from S3 (neither side is a self-report), compares every field the laptop
produces, and REFUSES to print a cutover-ready verdict below the day threshold --
so "day 1 was exact" cannot be talked into "close enough".

WHY A GAP IS THE THING TO FEAR (and two producers running is not)
The history upsert is idempotent on (run_date, key), so both producers writing
briefly is SAFE. Disabling the laptop before the cloud is verified writing LIVE
silver puts a hole in 4 of Opal's 14 AUM cohorts (DIVZ/IDVZ/PFDE/PFOE) -- which is
the exact failure this migration exists to end.

CUTOVER ORDER (do not reorder):
  1. >=3 trading days GREEN here.
  2. Flip `local.silver_root` to "" in infra/aws/terraform/etfs-netassets/main.tf; safe-apply.
  3. VERIFY the cloud is writing LIVE silver (a fresh silver/netassets/{date}.parquet
     carrying the Lambda's stamp, not the laptop's 18:00 stamp).
  4. ONLY THEN disable the Windows task -- and say so out loud in the ledger.

NOTE: a GREEN here is NOT an all-clear for the ETF channel. This lift is the
NUMERATOR (net_assets). LD-0292 -- ~$528mm of 49financial silently reclassified as
public float -- is the SUBTRAHEND (partner_held_etf) and is a DIFFERENT feeder.
A successful migration makes that wrong number FRESHER, not righter.
"""
from __future__ import annotations

import io
import sys

import boto3
import pandas as pd

BUCKET = "opal-data-etfs"
LAPTOP_PREFIX = "silver/netassets"
CLOUD_PREFIX = "_cloudprobe/silver/netassets"
REQUIRED_TRADING_DAYS = 3

# The laptop does not emit staleness_days; the cloud adds it. An ADDED column is
# contract-safe (the consumer reads with no usecols and projects onto its own
# column list). A DROPPED column is a contract violation and fails the gate.
EXPECTED_ADDED = {"staleness_days"}
# Differs by construction -- each producer stamps its own ingest time.
IGNORE = {"_ingested_at"}

s3 = boto3.client("s3")


def _dates(prefix: str) -> set:
    out = set()
    p = s3.get_paginator("list_objects_v2")
    for page in p.paginate(Bucket=BUCKET, Prefix=prefix + "/"):
        for o in page.get("Contents", []):
            name = o["Key"].rsplit("/", 1)[-1]
            if name.endswith(".parquet"):
                out.add(name[: -len(".parquet")])
    return out


def _read(key: str) -> pd.DataFrame:
    raw = s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()
    return pd.read_parquet(io.BytesIO(raw))


def compare(date: str) -> tuple:
    """Returns (ok, fields_compared, [failure strings])."""
    lap = _read(f"{LAPTOP_PREFIX}/{date}.parquet")
    cld = _read(f"{CLOUD_PREFIX}/{date}.parquet")
    fails = []

    dropped = [c for c in lap.columns if c not in cld.columns]
    if dropped:
        fails.append(f"CONTRACT VIOLATION: cloud DROPPED column(s) {dropped}")
    added = {c for c in cld.columns if c not in lap.columns}
    if added - EXPECTED_ADDED:
        fails.append(f"unexpected added column(s) {sorted(added - EXPECTED_ADDED)}")

    if set(lap["key"]) != set(cld["key"]):
        fails.append(f"fund set differs: laptop={sorted(lap['key'])} "
                     f"cloud={sorted(cld['key'])}")

    lo = lap.set_index("key")
    co = cld.set_index("key")
    cols = [c for c in lap.columns if c not in IGNORE and c != "key"]
    compared = 0
    for k in sorted(set(lo.index) & set(co.index)):
        for f in cols:
            lv, cv = lo.loc[k, f], co.loc[k, f]
            compared += 1
            if isinstance(lv, float) and isinstance(cv, float):
                same = (abs(lv - cv) < 0.01) or (pd.isna(lv) and pd.isna(cv))
            else:
                same = str(lv) == str(cv)
            if not same:
                fails.append(f"{k}.{f}: laptop={lv!r} cloud={cv!r}")
    return (not fails), compared, fails


def verdict(green: int, total: int,
            required: int = REQUIRED_TRADING_DAYS) -> tuple:
    """THE EXIT-CODE CONTRACT. Returns (exit_code, [lines to print]).

    PURE -- no S3, no network, no I/O -- so it can be EXERCISED, which is the
    entire point. This logic used to live inline in main(), reachable only by
    running the whole tool against real S3. That made "does this gate actually
    block?" a question you could only answer by re-deriving it at the shell --
    and the obvious way to do that (`python parity-check.py | tail; echo $?`)
    reads TAIL'S exit code, not this one. I did exactly that on 2026-07-14 and
    got a meaningless 0. The claim happened to be true; THE CHECK COULD NOT HAVE
    TOLD ME EITHER WAY.

    So the contract is now a function with a test (tests/test_etfs_parity_contract.py):

        EXIT 0 IS REACHABLE ONLY ON all-green AND green >= required.
        EVERY other outcome exits 1.

    A gate whose blocking behaviour can only be confirmed by a human running it
    correctly is one careless pipe away from being an advisory.
    """
    if green == total and green >= required:
        return 0, [
            "  VERDICT: CUTOVER-READY on the DATA.",
            "  Cutover is still a 4-STEP ORDER, and step 4 is LAST:",
            "    1. (this) >=3 trading days green",
            '    2. flip local.silver_root to "" -> safe-apply',
            "    3. VERIFY the cloud writes LIVE silver (fresh stamp, not 18:00)",
            "    4. ONLY THEN disable the Windows task; say so in the ledger",
            "  A GREEN HERE IS NOT AN ALL-CLEAR FOR THE ETF CHANNEL:",
            "  this is the NUMERATOR. LD-0292 ($528mm, partner_held_etf) is the",
            "  SUBTRAHEND, a different feeder, and it stays OPEN.",
        ]

    if green < total:
        return 1, [
            "  VERDICT: NOT CUTOVER-READY -- a day is RED. DO NOT CUT OVER.",
            "  THE LAPTOP STAYS ON.",
        ]

    return 1, [
        f"  VERDICT: NOT CUTOVER-READY -- only {green} of "
        f"{required} required trading days.",
        "  THE LAPTOP STAYS ON. An exact day-1 is not parity; that is the",
        "  whole reason the threshold exists.",
    ]


def main() -> int:
    if len(sys.argv) > 1:
        dates = sorted(sys.argv[1:])
    else:
        dates = sorted(_dates(LAPTOP_PREFIX) & _dates(CLOUD_PREFIX))

    if not dates:
        print("NO OVERLAPPING DATES -- the cloud producer has not yet written a "
              "day the laptop also wrote. Parity: 0 days.")
        print("VERDICT: NOT CUTOVER-READY (0/%d trading days)"
              % REQUIRED_TRADING_DAYS)
        return 1

    print("=" * 78)
    print("ETF NET-ASSETS PARITY -- laptop (live silver/) vs cloud (_cloudprobe/)")
    print("both sides read from S3; neither is a producer self-report")
    print("=" * 78)

    green = 0
    for d in dates:
        try:
            ok, n, fails = compare(d)
        except Exception as e:  # noqa: BLE001
            print(f"  {d}  ERROR: {e}")
            continue
        if ok:
            green += 1
            print(f"  {d}  GREEN   {n} fields compared, 0 mismatches")
        else:
            print(f"  {d}  RED     {n} fields compared, {len(fails)} problem(s)")
            for f in fails:
                print(f"             {f}")

    print()
    print(f"  GREEN DAYS: {green} / {len(dates)} compared "
          f"(threshold: {REQUIRED_TRADING_DAYS})")
    print()

    code, lines = verdict(green, len(dates))
    for ln in lines:
        print(ln)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
