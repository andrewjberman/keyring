#!/usr/bin/env python3
"""s18_cell_leg_v.py -- MDPF_SECCLASS-S18 class cell, leg V acceptance reads (CTO batch 224 half). READ-ONLY.

1. The QA run's log: A_03 'Liveness:' and Step 3c lines, chain exit, C_06 / D_04 done lines.
2. Cube 09-30 partition before vs after the QA run (history DELTA): row count, account count, content digest.
3. Cube 10-01 partition: the drop set (held 09-30, absent from the S18 run's 10-01 version) -- how many are present now.
4. platinum/firm/mix_summary.json: data_as_of, classes, pct sum, market value vs 09-30's 1,843,114,311.70 (band 2.0 pct).
5. platinum/accounts/z0812888131/summary.json: the 10-01 point.
6. The drop set's 10-01 synthetic_correction sum in gold/entities/accounts/<id>/aua_timeseries.json (the S18 run: -78,504,236.80).
Writes S18_CELL_LEG_V_20261003.json.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from pathlib import Path

import boto3
import pandas as pd

ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "data" / "black_diamond" / "scripts" / "gold"))
from lib.s3_layout import account_aua_timeseries_key, positions_cube_key  # noqa: E402

B = "opal-data-bd"
QA_START = datetime.datetime(2026, 10, 3, 10, 2, tzinfo=datetime.timezone.utc)
OUT = Path(__file__).resolve().parent / "S18_CELL_LEG_V_20261003.json"
s3 = boto3.client("s3", region_name="us-east-1")


def get(key, version=None):
    kw = {"Bucket": B, "Key": key}
    if version:
        kw["VersionId"] = version
    for attempt in range(6):
        try:
            return s3.get_object(**kw)["Body"].read()
        except Exception:  # noqa: BLE001 -- body reads time out on this link; re-read
            if attempt == 5:
                raise


def versions(key):
    return [v for v in s3.list_object_versions(Bucket=B, Prefix=key)["Versions"] if v["Key"] == key]


def before_after(key):
    vs = versions(key)
    after = [v for v in vs if v["IsLatest"]][0]
    before = max((v for v in vs if v["LastModified"] < QA_START), key=lambda v: v["LastModified"])
    return before, after


def cube(key, version):
    df = pd.read_parquet(BytesIO(get(key, version)))
    df["account_id"] = df["account_id"].astype(str)
    dig = hashlib.md5(pd.util.hash_pandas_object(df.sort_values(["account_id", "asset_name"]).reset_index(drop=True),
                                                 index=False).values.tobytes()).hexdigest()
    return df, dig


def main():
    out = {"claim": "measured (served and gold reads after the QA run)"}

    logs = sorted((o for p in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="logs/gold-layer/gold_incremental_2026-10-03")
                   for o in p.get("Contents", []) if o["LastModified"] > QA_START), key=lambda o: o["LastModified"])
    out["logs"] = [o["Key"] for o in logs]
    if logs:
        text = get(logs[-1]["Key"]).decode("utf-8", "replace")
        keep = ("Liveness:", "frontier whole", "REFUSED", "proposed as_of", "COMPLETE (exit code", "A_03 done",
                "C_06 done", "D_04 done", "FATAL", "Mix snapshot", "Global end date")
        out["log_lines"] = [ln.strip()[:300] for ln in text.splitlines() if any(k in ln for k in keep)][:40]

    k930 = positions_cube_key("2026-09-30")
    b930, a930 = before_after(k930)
    d_b, h_b = cube(k930, b930["VersionId"])
    d_a, h_a = cube(k930, a930["VersionId"])
    out["cube_0930"] = {"before": [b930["VersionId"], b930["LastModified"].isoformat(), len(d_b), d_b["account_id"].nunique(), h_b],
                        "after": [a930["VersionId"], a930["LastModified"].isoformat(), len(d_a), d_a["account_id"].nunique(), h_a],
                        "content_equal": h_b == h_a}

    k1001 = positions_cube_key("2026-10-01")
    b1001, a1001 = before_after(k1001)
    s18_1001, _ = cube(k1001, b1001["VersionId"])
    qa_1001, _ = cube(k1001, a1001["VersionId"])
    held930 = set(d_b["account_id"])
    drop = held930 - set(s18_1001["account_id"])
    present = drop & set(qa_1001["account_id"])
    out["cube_1001"] = {"s18_version": [b1001["VersionId"], b1001["LastModified"].isoformat(), s18_1001["account_id"].nunique()],
                        "qa_version": [a1001["VersionId"], a1001["LastModified"].isoformat(), qa_1001["account_id"].nunique()],
                        "drop_set": len(drop), "drop_set_present_now": len(present),
                        "drop_set_still_absent": sorted(drop - present)}

    ms = json.loads(get("platinum/firm/mix_summary.json"))
    mv = sum(v["market_value"] for v in ms["mix"].values())
    out["mix_summary"] = {"data_as_of": ms["data_as_of"], "classes": len(ms["mix"]),
                          "pct_sum": round(sum(v["pct"] for v in ms["mix"].values()), 6), "mv": round(mv, 2),
                          "pct_vs_0930": round(100 * (mv / 1843114311.70 - 1), 3)}

    acct = json.loads(get("platinum/accounts/z0812888131/summary.json"))
    out["z0812888131_tail"] = acct["timeseries"][-2:] if isinstance(acct.get("timeseries"), list) else str(acct.get("timeseries"))[:200]

    def sc(a):
        try:
            ts = json.loads(get(account_aua_timeseries_key(a)))
            pt = [p for p in ts.get("data", []) if p.get("date") == "2026-10-01"]
            return a, (pt[0].get("synthetic_correction", 0.0) or 0.0, pt[0].get("total_aua", 0.0) or 0.0) if pt else None
        except Exception as e:  # noqa: BLE001
            return a, ("unreadable", str(e)[:60])
    with ThreadPoolExecutor(8) as pool:
        res = dict(pool.map(sc, sorted(drop)))
    ok = [v for v in res.values() if v and isinstance(v[0], float)]
    out["drop_set_1001"] = {"read": len(ok), "synthetic_correction_sum": round(sum(v[0] for v in ok), 2),
                            "total_aua_sum": round(sum(v[1] for v in ok), 2),
                            "no_1001_point": sum(1 for v in res.values() if v is None),
                            "unreadable": sum(1 for v in res.values() if v and v[0] == "unreadable")}

    OUT.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    print(json.dumps(out, indent=1, default=str))
    print("WROTE", OUT)


if __name__ == "__main__":
    main()
