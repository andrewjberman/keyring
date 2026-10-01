#!/usr/bin/env python3
"""The Inflection serving packet's pre-condition (1.0.0_SA_CTO rulings batch 92 items 3-4): no partition under the three gap days.

    python stale_gap_days_precondition.py

Lists, for 2026-05-11, 2026-06-30 and 2026-08-10, every object and every version or delete marker under the daily and the
manifest tables of the Inflection holdings gold. PASS only when the three dates hold NO current object in either table. Prints the
denominator (prefixes listed) and one positive control (a date that must still hold its partition). Reads only: this script
deletes nothing and restores nothing.
"""
from __future__ import annotations

import sys

import boto3

BUCKET = "opal-data-inflection"
TABLES = ("irpt/inflection/gold/holdings_performance_daily/", "irpt/inflection/gold/holdings_performance_manifest/")
GAP_DAYS = ("2026-05-11", "2026-06-30", "2026-08-10")
CONTROL = "2026-05-12"


def main() -> int:
    s3 = boto3.client("s3", region_name="us-east-1")
    current_total = 0
    for day in GAP_DAYS + (CONTROL,):
        for table in TABLES:
            prefix = "%sdate=%s/" % (table, day)
            cur = s3.list_objects_v2(Bucket=BUCKET, Prefix=prefix).get("Contents", [])
            ver = s3.list_object_versions(Bucket=BUCKET, Prefix=prefix)
            n_versions, n_markers = len(ver.get("Versions", [])), len(ver.get("DeleteMarkers", []))
            print("%s %-62s current objects %d | versions %d | delete markers %d"
                  % ("CONTROL" if day == CONTROL else "GAP    ", prefix, len(cur), n_versions, n_markers))
            for o in cur:
                print("          %s %d bytes %s" % (o["Key"].rsplit("/", 1)[-1], o["Size"], o["LastModified"].strftime("%Y-%m-%dT%H:%M:%SZ")))
            if day != CONTROL:
                current_total += len(cur)
            elif not cur:
                print("ERROR: the control date holds nothing under %s -- the listing cannot be trusted" % prefix)
                return 2
    print("prefixes listed: %d gap-day and %d control; current objects under the three gap days: %d"
          % (len(GAP_DAYS) * len(TABLES), len(TABLES), current_total))
    print("PRE-CONDITION %s" % ("PASS: no partition under the three gap days" if current_total == 0
                                else "FAIL: %d object(s) still present" % current_total))
    return 0 if current_total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
