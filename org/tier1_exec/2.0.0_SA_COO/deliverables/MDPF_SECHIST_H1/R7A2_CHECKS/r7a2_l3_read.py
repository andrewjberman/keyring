#!/usr/bin/env python3
"""Ledger mdpf-sechist-a2-backfill-cap-62-sitez-20261015, leg L3: read one scheduled run's manifest against the A2 acceptance.

Usage: python r7a2_l3_read.py <as_of YYYY-MM-DD>     reads s3://opal-data-etfs/bbg/<as_of>/run_manifest.json (read only, one key).
Prints  A2-L3-OK as_of=.. planned=.. capped=.. spent_before=.. estimate=.. limit=.. remainder=..  when every clause holds,
        A2-L3-BAD <the first clause that failed>  otherwise, and A2-L3-ABSENT when the manifest key does not exist.
Clauses: run_class scheduled; objects_failed empty; history_backfill_budget present with its keys; spent_before + estimate <= limit;
planned names <= 62; and a binding cap is read as such: when history_backfill_capped is non-empty, planned must equal 62.
What it cannot read: the pull's exit code and the run log (relayed by the site-Z lane), and whether the run used the new constant when the
cap did not bind (the manifest does not carry the constant; the site-Z blob read is leg L2). Plain ASCII, stdlib plus boto3, terminates.
"""
import json
import sys

BUCKET = "opal-data-etfs"
CAP = 62
BUDGET_KEYS = ("estimate", "limit", "spent_before", "recorded", "spent_after", "remainder")


def read(as_of):
    import boto3
    from botocore.exceptions import ClientError
    try:
        body = boto3.client("s3").get_object(Bucket=BUCKET, Key="bbg/%s/run_manifest.json" % as_of)["Body"].read()
    except ClientError as exc:
        if exc.response.get("Error", {}).get("Code") in ("NoSuchKey", "404"):
            return None
        raise
    return json.loads(body)


def grade(m):
    """PURE: (ok, text)."""
    if m.get("run_class") != "scheduled":
        return False, "run_class=%r (want scheduled)" % m.get("run_class")
    if m.get("objects_failed"):
        return False, "objects_failed=%r" % (m.get("objects_failed"),)
    b = m.get("history_backfill_budget")
    if not isinstance(b, dict) or any(k not in b for k in BUDGET_KEYS):
        return False, "history_backfill_budget missing or short: %r" % (b,)
    if b["spent_before"] is None or b["estimate"] is None or b["limit"] is None:
        return False, "budget fields null: %r" % (b,)
    if b["spent_before"] + b["estimate"] > b["limit"]:
        return False, "spent_before + estimate > limit: %r" % (b,)
    planned = len(m.get("history_backfill") or {})
    capped = len(m.get("history_backfill_capped") or [])
    if planned > CAP:
        return False, "planned=%d > %d" % (planned, CAP)
    if capped and planned != CAP:
        return False, "capped=%d but planned=%d (a binding cap plans exactly %d)" % (capped, planned, CAP)
    return True, "planned=%d capped=%d spent_before=%s estimate=%s limit=%s remainder=%s" % (
        planned, capped, b["spent_before"], b["estimate"], b["limit"], b["remainder"])


def main(argv):
    if len(argv) != 2:
        print("A2-L3-BAD usage: r7a2_l3_read.py <as_of YYYY-MM-DD>")
        return 2
    m = read(argv[1])
    if m is None:
        print("A2-L3-ABSENT bbg/%s/run_manifest.json" % argv[1])
        return 3
    ok, text = grade(m)
    print(("A2-L3-OK as_of=%s " % m.get("as_of") if ok else "A2-L3-BAD ") + text)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
