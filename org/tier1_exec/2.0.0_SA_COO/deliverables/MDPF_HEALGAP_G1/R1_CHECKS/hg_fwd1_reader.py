"""MDPF_HEALGAP FWD-1 hop 5 -- the reader's view: what the Model Portfolios page serves for Cottonwood on date D.

The page reads s3://opal-data-portal-v2/platinum/mdpf/cottonwood/aggregate-aua-timeseries.json, published by
opal-assets-mdpf-portal-publisher (13:50Z daily) from the gold slice the 13:30Z mdpf-scheduled-floor run builds off the
newest Cottonwood fact_model_assignment partition (mdpf-daily-dispatch.sh step 6d). The served series runs one trading
day behind the run date: on a normal day D the newest point is prev_trading_day(D) with its model leg measured.

  --date D   READER-OK when the served file was written on D and its newest point is prev_trading_day(D) with
             cohort_provenance.model == "measured" and a non-null model_aua; else READER-BAD <reason>.
Read-only (s3:GetObject on one served key). Control: a normal day (2026-10-07) reads READER-OK.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import boto3

sys.path.insert(0, str(Path(__file__).resolve().parents[6] / "lib"))
from trading_calendar import prev_trading_day  # noqa: E402

KEY = "platinum/mdpf/cottonwood/aggregate-aua-timeseries.json"


def main(d: str) -> int:
    want = prev_trading_day(date.fromisoformat(d)).isoformat()
    s3 = boto3.client("s3", region_name="us-east-1")
    doc = json.loads(s3.get_object(Bucket="opal-data-portal-v2", Key=KEY)["Body"].read())
    written = ((doc.get("_provenance") or {}).get("written_at") or "")
    dates = doc.get("dates") or []
    if not written.startswith(d):
        print(f"READER-BAD served file written_at={written!r}, not on {d}")
        return 1
    if want not in dates:
        print(f"READER-BAD {want} absent from the served axis (last={dates[-1] if dates else None})")
        return 1
    i = dates.index(want)
    model = (doc.get("cohort_provenance") or [None] * len(dates))[i] or {}
    aua = (doc.get("model_aua") or [None] * len(dates))[i]
    if model.get("model") != "measured" or aua is None:
        print(f"READER-BAD point {want}: model={model.get('model')!r} model_aua={aua!r}")
        return 1
    print(f"READER-OK served written {written} point {want} model=measured model_aua={aua:,.2f}")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == "--date":
        sys.exit(main(a[1]))
    print("USAGE: hg_fwd1_reader.py --date YYYY-MM-DD")
    sys.exit(2)
