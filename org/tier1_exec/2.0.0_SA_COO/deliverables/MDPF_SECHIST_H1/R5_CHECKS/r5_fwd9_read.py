"""MDPF_SECHIST round 5, FWD-9 acceptance (CTO msg 2791, round-4 analysis item 3): a money-market first-day null is SERVED BLANK, then the
re-request fills that day and it is SERVED FILLED on the next run.

Read only. Day D defaults to 2026-10-12 (the week's first trading day). Money-market funds: SALXX, FXFXX.

  python r5_fwd9_read.py blank [D]
      bbg/D/run_manifest.json is scheduled; bbg/D/history_topup.parquet carries a NULL DAY_TO_DAY_TOT_RETURN_GROSS_DVDS on D for at
      least one money-market fund; the served page (opal-data-portal-v2 platinum/etfs/positioning_data.json, data_as_of == D) shows that
      fund's returns.1D as null in every portfolio holding it.
      Last line: FWD9-BLANK-OK D=<d> null=<tickers>   or   FWD9-BLANK-BAD <reason>.
  python r5_fwd9_read.py filled [D]
      For the funds null on D (read from bbg/D): a later scheduled partition bbg/E (E > D) carries a NON-NULL value on D for each (the
      gap re-request); the served page with data_as_of == E (E in D's week) shows returns.WTD non-null for each in every holding.
      Last line: FWD9-FILLED-OK D=<d> E=<e> filled=<tickers>   or   FWD9-FILLED-BAD <reason>.
"""
from __future__ import annotations

import io
import json
import sys
from datetime import date

import boto3
import pandas as pd

DATA_BUCKET = "opal-data-etfs"
SERVED_BUCKET = "opal-data-portal-v2"
SERVED_KEY = "platinum/etfs/positioning_data.json"
RET = "DAY_TO_DAY_TOT_RETURN_GROSS_DVDS"
MMF = ("SALXX", "FXFXX")


def _manifest(s3, d):
    try:
        return json.loads(s3.get_object(Bucket=DATA_BUCKET, Key="bbg/" + d + "/run_manifest.json")["Body"].read())
    except s3.exceptions.NoSuchKey:
        return None


def _mmf_on(s3, part, day):
    """ticker -> value of RET on `day` in bbg/<part>/history_topup.parquet (None = null); absent ticker not listed."""
    try:
        df = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=DATA_BUCKET, Key="bbg/" + part + "/history_topup.parquet")["Body"].read()))
    except s3.exceptions.NoSuchKey:
        return None
    df = df[df["date"].astype(str).str[:10] == day]
    out = {}
    for _, r in df.iterrows():
        t = str(r["security"]).split(" ")[0]
        if t in MMF:
            v = r[RET]
            out[t] = None if pd.isna(v) else float(v)
    return out


def _served(s3):
    o = s3.get_object(Bucket=SERVED_BUCKET, Key=SERVED_KEY)
    return json.loads(o["Body"].read()), o["LastModified"].isoformat()


def _served_values(page, ticker, window):
    vals = []
    for code, p in (page.get("portfolios") or {}).items():
        for h in p.get("holdings") or []:
            if h.get("ticker") == ticker:
                vals.append((code, (h.get("returns") or {}).get(window)))
    return vals


def blank(day) -> int:
    s3 = boto3.client("s3")
    m = _manifest(s3, day)
    if not m or m.get("run_class") != "scheduled":
        print("FWD9-BLANK-BAD no-scheduled-partition D=" + day)
        return 1
    vals = _mmf_on(s3, day, day)
    print("bbg/" + day + " history " + RET + " on D: " + json.dumps(vals))
    if vals is None:
        print("FWD9-BLANK-BAD no-history_topup D=" + day)
        return 1
    nulls = sorted(t for t, v in vals.items() if v is None)
    if not nulls:
        print("FWD9-BLANK-BAD no-null-on-D D=" + day + " (organic case: the vendor filled the day; the arm did not occur)")
        return 1
    page, lm = _served(s3)
    print("served data_as_of=" + str(page.get("data_as_of")) + " LastModified=" + lm)
    if page.get("data_as_of") != day:
        print("FWD9-BLANK-BAD served-as_of-not-D served=" + str(page.get("data_as_of")))
        return 1
    for t in nulls:
        sv = _served_values(page, t, "1D")
        print(t + " served 1D: " + json.dumps(sv))
        if not sv or any(v is not None for _, v in sv):
            print("FWD9-BLANK-BAD not-blank " + t)
            return 1
    print("FWD9-BLANK-OK D=" + day + " null=" + ",".join(nulls))
    return 0


def filled(day) -> int:
    s3 = boto3.client("s3")
    base = _mmf_on(s3, day, day) or {}
    nulls = sorted(t for t, v in base.items() if v is None)
    if not nulls:
        print("FWD9-FILLED-BAD no-null-on-D-to-fill D=" + day)
        return 1
    page, lm = _served(s3)
    e = page.get("data_as_of")
    print("served data_as_of=" + str(e) + " LastModified=" + lm + " nulls_on_D=" + ",".join(nulls))
    if not e or e <= day or date.fromisoformat(e).isocalendar()[:2] != date.fromisoformat(day).isocalendar()[:2]:
        print("FWD9-FILLED-BAD served-as_of-not-later-in-week served=" + str(e))
        return 1
    m = _manifest(s3, e)
    if not m or m.get("run_class") != "scheduled":
        print("FWD9-FILLED-BAD no-scheduled-partition E=" + e)
        return 1
    later = _mmf_on(s3, e, day) or {}
    print("bbg/" + e + " history " + RET + " on D: " + json.dumps(later))
    for t in nulls:
        if later.get(t) is None:
            print("FWD9-FILLED-BAD not-re-requested " + t)
            return 1
        sv = _served_values(page, t, "WTD")
        print(t + " served WTD: " + json.dumps(sv))
        if not sv or any(v is None for _, v in sv):
            print("FWD9-FILLED-BAD served-not-filled " + t)
            return 1
    print("FWD9-FILLED-OK D=" + day + " E=" + e + " filled=" + ",".join(nulls))
    return 0


def main(argv) -> int:
    if len(argv) < 2 or argv[1] not in ("blank", "filled"):
        print("FWD9-READ-BAD usage: r5_fwd9_read.py blank|filled [D]")
        return 2
    day = argv[2] if len(argv) > 2 else "2026-10-12"
    return blank(day) if argv[1] == "blank" else filled(day)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
