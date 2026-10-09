"""MDPF_SECHIST round 3, FWD-7: the first SCHEDULED run with SH-t-4 prints the draw beside the ledger remainder.

Read only. Takes the newest s3://opal-data-etfs/bbg/<date>/run_manifest.json with as_of >= 2026-10-09 and run_class "scheduled",
and requires history_backfill_budget to carry the SH-t-4 keys spent_after and remainder (both present; when a backfill drew rows,
both non-null and remainder == max(limit - spent_after, 0)).

Last line: FWD7-READ-OK as_of=<d> recorded=<r> spent_after=<s> remainder=<m>   or   FWD7-READ-BAD <reason>.
"""
from __future__ import annotations

import json
import sys

import boto3

BUCKET = "opal-data-etfs"
FLOOR = "2026-10-09"


def main() -> int:
    s3 = boto3.client("s3")
    dates = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix="bbg/", Delimiter="/"):
        for p in page.get("CommonPrefixes") or []:
            d = p["Prefix"][4:-1]
            if len(d) == 10 and d >= FLOOR:
                dates.append(d)
    print("bbg/ date prefixes >= " + FLOOR + ": " + str(len(dates)))
    for d in sorted(dates, reverse=True):
        try:
            m = json.loads(s3.get_object(Bucket=BUCKET, Key="bbg/" + d + "/run_manifest.json")["Body"].read())
        except s3.exceptions.NoSuchKey:
            continue
        if m.get("run_class") != "scheduled":
            print("skip " + d + " run_class=" + str(m.get("run_class")))
            continue
        b = m.get("history_backfill_budget") or {}
        print("manifest bbg/" + d + " budget=" + json.dumps(b, sort_keys=True))
        if "spent_after" not in b or "remainder" not in b:
            print("FWD7-READ-BAD keys-absent as_of=" + d)
            return 1
        if b.get("recorded"):
            if b["spent_after"] is None or b["remainder"] is None:
                print("FWD7-READ-BAD null-after-draw as_of=" + d)
                return 1
            if b["remainder"] != max(int(b["limit"]) - int(b["spent_after"]), 0):
                print("FWD7-READ-BAD remainder-mismatch as_of=" + d)
                return 1
        print("FWD7-READ-OK as_of=" + d + " recorded=" + str(b.get("recorded")) + " spent_after=" + str(b.get("spent_after"))
              + " remainder=" + str(b.get("remainder")))
        return 0
    print("FWD7-READ-BAD no-scheduled-manifest-since " + FLOOR)
    return 1


if __name__ == "__main__":
    sys.exit(main())
