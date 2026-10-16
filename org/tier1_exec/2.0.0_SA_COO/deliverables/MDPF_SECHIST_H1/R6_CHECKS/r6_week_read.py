"""MDPF_SECHIST FWD-9 DONE WHEN (round-5 ADDENDUM 1 item 2, as corrected): SALXX read each trading day across a week that includes a Monday. Read only.

The served page is overwritten every run, so each day is read from the GOLD partition the run wrote (opal-data-etfs/gold/holding/date=<as_of>/holding.parquet,
which carries the return_* windows and, since the SH-t-24 apply, return_frontier), plus the run manifest's generated_utc.

  python r6_week_read.py <as_of> [<as_of> ...]
Per as_of and per book holding SALXX (or FXFXX) prints one row:  as_of book ticker STATE windows frontier
  STATE = VALUE   every window that the history can compute is a number and 1D is a number
          CARRIED return_frontier is set AND differs from the as_of (the last vendor day's value, labeled); a frontier equal to the as_of is VALUE
          BLANK   1D is null (the day shows no value: the case the DONE WHEN forbids unless the NEXT run fills it)
Last line: WEEK-READ <n> as_of day(s): VALUE=<a> CARRIED=<b> BLANK=<c> ABSENT=<d>   (ABSENT = no gold partition for that as_of)
"""
from __future__ import annotations

import io
import sys

import boto3
import pandas as pd

BUCKET = "opal-data-etfs"
TICKERS = ("SALXX", "FXFXX")
WINDOWS = ("1D", "WTD", "MTD", "1M", "QTD", "1Q", "YTD", "1Y")


def main(days):
    s3 = boto3.client("s3")
    tally = {"VALUE": 0, "CARRIED": 0, "BLANK": 0, "ABSENT": 0}
    for d in days:
        key = "gold/holding/date=" + d + "/holding.parquet"
        try:
            df = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()))
        except s3.exceptions.NoSuchKey:
            print(d + " ABSENT no gold partition (" + key + ")")
            tally["ABSENT"] += 1
            continue
        rows = df[df["ticker"].isin(TICKERS)]
        if rows.empty:
            print(d + " ABSENT no SALXX/FXFXX holding rows")
            tally["ABSENT"] += 1
            continue
        for _, r in rows.sort_values(["ticker", "book"]).iterrows():
            fr = r.get("return_frontier") if "return_frontier" in df.columns else None
            wins = {w: r.get("return_" + w) for w in WINDOWS}
            if pd.isna(wins["1D"]):
                state = "BLANK"
            elif fr is not None and not pd.isna(fr) and str(fr)[:10] != d:
                state = "CARRIED"                  # a frontier equal to the as_of is a reading ON the day: a VALUE, not a carry
            else:
                state = "VALUE"
            tally[state] += 1
            print(d + " " + str(r["book"]) + " " + str(r["ticker"]) + " " + state + " "
                  + "{" + ", ".join(w + "=" + ("None" if pd.isna(v) else str(v)) for w, v in wins.items()) + "}"
                  + " frontier=" + ("-" if fr is None or pd.isna(fr) else str(fr)))
    print("WEEK-READ " + str(len(days)) + " as_of day(s): VALUE=" + str(tally["VALUE"]) + " CARRIED=" + str(tally["CARRIED"])
          + " BLANK=" + str(tally["BLANK"]) + " ABSENT=" + str(tally["ABSENT"]))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: r6_week_read.py <as_of> [<as_of> ...]")
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
