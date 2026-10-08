"""MDPF_SECHIST round 2, criterion SH2-t3-AC1: the FWD-1 acceptance read on the first unassisted scheduled pull.

Read only. Finds the newest s3://opal-data-etfs/bbg/<date>/run_manifest.json, requires run_class "scheduled" (an adhoc
re-pull is QA only, ruling cb6fb2a52c), takes every security that pull backfilled with rows > 0 as a newly held security,
and reads each on the served Positioning data (s3://opal-data-portal-v2/platinum/etfs/positioning_data.json), which must be
published after the manifest. A security passes when it shows asset class, sector (sub_asset_class), a clean name (no
"/<state>" suffix, the CTO's round-1 analysis 2.2) and all eight windows. At least one must pass. Writes nothing.

Last line: FWD1-ACCEPT-OK as_of=<d> ticker=<t> passed=<n>/<m>  or  FWD1-ACCEPT-BAD <reason>.
"""
from __future__ import annotations

import json
import sys

import boto3

ETF_BUCKET = "opal-data-etfs"
SERVED_BUCKET = "opal-data-portal-v2"
SERVED_KEY = "platinum/etfs/positioning_data.json"
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


def _newest_manifest(s3):
    dates = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=ETF_BUCKET, Prefix="bbg/", Delimiter="/"):
        for p in page.get("CommonPrefixes") or []:
            d = p["Prefix"][4:-1]
            if len(d) == 10 and d[4] == "-" and d[7] == "-":
                dates.append(d)
    print("bbg/ date prefixes: " + str(len(dates)))
    for d in sorted(dates, reverse=True):
        try:
            obj = s3.get_object(Bucket=ETF_BUCKET, Key="bbg/" + d + "/run_manifest.json")
        except s3.exceptions.NoSuchKey:
            continue
        return d, obj["LastModified"], json.loads(obj["Body"].read())
    return None, None, None


def main() -> int:
    s3 = boto3.client("s3")
    d, m_lm, m = _newest_manifest(s3)
    if m is None:
        print("FWD1-ACCEPT-BAD no-manifest")
        return 1
    print("manifest bbg/" + d + " LastModified=" + m_lm.isoformat() + " run_class=" + str(m.get("run_class"))
          + " history_backfill_error=" + str(m.get("history_backfill_error")))
    if m.get("run_class") != "scheduled":
        print("FWD1-ACCEPT-BAD newest-manifest-not-scheduled as_of=" + d + " run_class=" + str(m.get("run_class")))
        return 1
    new = sorted(t for t, v in (m.get("history_backfill") or {}).items() if (v or {}).get("rows", 0) > 0)
    print("backfilled with rows: " + str(len(new)) + " " + ",".join(new))
    if not new:
        print("FWD1-ACCEPT-BAD no-new-security as_of=" + d)
        return 1
    obj = s3.get_object(Bucket=SERVED_BUCKET, Key=SERVED_KEY)
    print("served LastModified=" + obj["LastModified"].isoformat())
    if obj["LastModified"] <= m_lm:
        print("FWD1-ACCEPT-BAD served-not-after-manifest")
        return 1
    want = set(new)
    seen, passed = set(), []
    for b in _books(json.loads(obj["Body"].read())):
        for h in b.get("holdings") or []:
            t = str(h.get("ticker", "")).upper()
            if t not in want:
                continue
            seen.add(t)
            r = h.get("returns") or {}
            n = sum(1 for w in WINDOWS if isinstance(r.get(w), (int, float)))
            name = str(h.get("name") or "")
            ok = bool(h.get("asset_class")) and bool(h.get("sub_asset_class")) and bool(name) and "/" not in name and n == 8
            print(str(b.get("code")) + " " + t + " | " + name + " | " + str(h.get("asset_class")) + " / "
                  + str(h.get("sub_asset_class")) + " | windows " + str(n) + "/8 | " + ("PASS" if ok else "FAIL"))
            if ok:
                passed.append(t)
    if not passed:
        print("FWD1-ACCEPT-BAD none-passed seen=" + str(len(seen)) + "/" + str(len(want)) + " as_of=" + d)
        return 1
    print("FWD1-ACCEPT-OK as_of=" + d + " ticker=" + sorted(set(passed))[0] + " passed=" + str(len(set(passed)))
          + "/" + str(len(want)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
