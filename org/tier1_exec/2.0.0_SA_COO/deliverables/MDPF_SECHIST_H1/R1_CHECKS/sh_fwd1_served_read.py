"""MDPF_SECHIST FWD-1 real-run read: what an analyst sees for named securities on the Positioning page's served data.

Reads s3://opal-data-portal-v2/platinum/etfs/positioning_data.json (the publisher's one served key), read only, and prints for each
named ticker in each Opal ETF book: name, asset class, sub-asset class, industry group and the eight return windows, plus how many
windows are populated. Writes nothing.

Usage: python sh_fwd1_served_read.py CSCO BX [MORE ...]
Last line: FWD1-READ data_as_of=<..> tickers=<n> rows=<n> full_windows=<n> (a row is full when all eight windows are numbers).
"""
from __future__ import annotations

import json
import sys

import boto3

BUCKET = "opal-data-portal-v2"
KEY = "platinum/etfs/positioning_data.json"
WINDOWS = ("1D", "WTD", "MTD", "1M", "QTD", "1Q", "YTD", "1Y")


def _books(doc):
    if isinstance(doc, dict):
        if "holdings" in doc and "code" in doc:
            yield doc
            return
        for v in doc.values():
            yield from _books(v)
    elif isinstance(doc, list):
        for v in doc:
            yield from _books(v)


def main(argv: list[str]) -> int:
    want = {t.upper() for t in argv} or {"CSCO", "BX"}
    obj = boto3.client("s3").get_object(Bucket=BUCKET, Key=KEY)
    doc = json.loads(obj["Body"].read())
    print("served " + BUCKET + "/" + KEY + " LastModified=" + obj["LastModified"].isoformat())
    rows = full = 0
    as_of = set()
    for b in _books(doc):
        as_of.add(str(b.get("data_as_of")))
        for h in b.get("holdings") or []:
            t = str(h.get("ticker", "")).upper()
            if t not in want:
                continue
            r = h.get("returns") or {}
            vals = [r.get(w) for w in WINDOWS]
            n = sum(1 for v in vals if isinstance(v, (int, float)))
            rows += 1
            full += n == len(WINDOWS)
            print(b.get("code") + " " + t + " | " + str(h.get("name")) + " | " + str(h.get("asset_class")) + " / "
                  + str(h.get("sub_asset_class")) + " / " + str(h.get("industry_group")) + " | windows "
                  + str(n) + "/8 " + " ".join(w + "=" + str(v) for w, v in zip(WINDOWS, vals)))
    print("FWD1-READ data_as_of=" + ",".join(sorted(as_of)) + " tickers=" + str(len(want)) + " rows=" + str(rows)
          + " full_windows=" + str(full))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
