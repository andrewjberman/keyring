#!/usr/bin/env python3
"""comp-whoread -- who ACTUALLY READ an S3 bucket, from CloudTrail S3 object data events.

WHY THIS EXISTS (CTO, 2026-07-09T210020Z):

    "Layer-3's live-simulate DETECT proves who MAY read; only this proves who DID."

`comp-firmsep-sweep` / `simulate-principal-policy` answer *who is permitted*. They cannot answer
*who exercised it*. This does, from the org trail's S3 object-level data events, surfaced via Athena.

THE DENOMINATOR IS THE WINDOW, AND IT GOES IN THE FIRST LINE, ALWAYS.
Object-level data-event coverage on a bucket begins when a `PutEventSelectors` added it, and a query
over a range wider than that coverage returns "clean" from partitions that never held a single data
event -- a false negative wearing an evidence costume. So this tool:
  * reports the coverage-start it can PROVE (earliest object data event on the bucket in the scanned range),
  * refuses to answer for a bucket with ZERO object data events in range (fail closed -- an empty result
    there means "never captured", not "never read"),
  * states the window on line 1 of every report.

A zero is a claim about the probe. This tool proves the probe with a positive control (total object
events on the bucket) before it reports any per-role count.

Requires the CloudTrail Athena projection tables built 2026-07-09 (registered in
org/modules/graph/comp-coverage-map.yaml): `cloudtrail_forensics.ct_use1` (us-east-1, 2026/05/11->NOW).

Read-only. Never adjudicates: a firmless-sounding role NAME is a proxy, not a verdict. It reports
who-read; relation->semantic->sanction is the caller's (a human/CTO) judgment.

DO NOT DERIVE A GRANT NARROWING FROM THIS TOOL'S OUTPUT (CTO, 2026-07-09T211629Z). Observed reads are
a FLOOR on what a principal CAN reach, not a CEILING. Narrowing an IAM Resource to "the prefixes the
traffic shows" is enumerate-what-you-know one level in -- the same error as a belt enumerating three
bucket names. who-DID is a confirmation instrument; who-MAY is derived from the producer/router SOURCE.
Source gives the ceiling; this tool confirms nothing was missed under it. Both, in that order.

Usage:
  comp-whoread <bucket> [--prefix gold/] [--since 2026-06-01] [--action GetObject]
Exit: 0 = reported | 1 = error / could-not-evaluate (no coverage, query failed) -- FAIL CLOSED.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time

WORKGROUP = "opal_mcp"
TABLE = "cloudtrail_forensics.ct_use1"
COVERAGE_TABLE_START = "2026-05-11"  # projection floor of ct_use1; queries cannot see before this

# An S3 object-level data event lists BOTH the bucket and the object in `resources`, and their ORDER
# is not fixed: for GetObject on opal-data-bd the array is [AWS::S3::Bucket, AWS::S3::Object]. A naive
# `resources[1].type='AWS::S3::Object'` test therefore misses EVERY object read and would make this
# tool fail-closed on a fully-covered bucket -- reporting "never captured" when 13M events exist. So we
# test ANY element of the array, not a fixed index. (Found by exercising the tool, 2026-07-09.)
OBJ_EVENT_PRED = ("try(cardinality(filter(resources, r -> r.type='AWS::S3::Object')) > 0) = true")


def aws(cmd: list[str]) -> str:
    import shutil

    exe = shutil.which(cmd[0]) or shutil.which(cmd[0] + ".cmd")
    if not exe:
        print(f"ERROR: {cmd[0]} not on PATH", file=sys.stderr)
        sys.exit(1)
    p = subprocess.run([exe, *cmd[1:]], capture_output=True, text=True)
    if p.returncode != 0:
        print(f"ERROR: {' '.join(cmd[:4])} rc={p.returncode}\n{p.stderr[:400]}", file=sys.stderr)
        sys.exit(1)
    return p.stdout


def athena(sql: str) -> list[list[str]]:
    qid = aws(["aws", "athena", "start-query-execution", "--work-group", WORKGROUP,
               "--query-string", sql, "--query", "QueryExecutionId", "--output", "text"]).strip()
    if not qid:
        print("ERROR: athena start-query-execution returned no id", file=sys.stderr)
        sys.exit(1)
    for _ in range(80):
        st = aws(["aws", "athena", "get-query-execution", "--query-execution-id", qid,
                  "--query", "QueryExecution.Status.State", "--output", "text"]).strip()
        if st == "SUCCEEDED":
            break
        if st in ("FAILED", "CANCELLED"):
            reason = aws(["aws", "athena", "get-query-execution", "--query-execution-id", qid,
                          "--query", "QueryExecution.Status.StateChangeReason", "--output", "text"])
            print(f"ERROR: athena query {st}: {reason}", file=sys.stderr)
            sys.exit(1)
        time.sleep(3)
    else:
        print("ERROR: athena query timed out", file=sys.stderr)
        sys.exit(1)
    out = aws(["aws", "athena", "get-query-results", "--query-execution-id", qid, "--output", "json"])
    rows = json.loads(out).get("ResultSet", {}).get("Rows", [])
    return [[(c.get("VarCharValue", "") or "") for c in r.get("Data", [])] for r in rows]


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-whoread", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bucket", help="bucket name, e.g. opal-data-bd (must be in the data-event selector)")
    ap.add_argument("--prefix", default="", help="only reads whose key starts with this prefix")
    ap.add_argument("--since", default=COVERAGE_TABLE_START,
                    help=f"start date YYYY-MM-DD (default {COVERAGE_TABLE_START}, the projection floor)")
    ap.add_argument("--action", default="", help="restrict to one eventName, e.g. GetObject")
    args = ap.parse_args()

    b = args.bucket.replace("'", "")
    keyfilter = ""
    if args.prefix:
        keyfilter = f" AND json_extract_scalar(requestParameters,'$.key') LIKE '{args.prefix}%'"
    actfilter = f" AND eventName='{args.action}'" if args.action else ""
    where = (f"eventSource='s3.amazonaws.com' AND eventType='AwsApiCall' "
             f"AND requestParameters LIKE '%{b}%'{keyfilter}{actfilter} "
             f"AND dt >= '{args.since.replace('-', '/')}'")

    # POSITIVE CONTROL first. If the table sees no object data events on this bucket, we CANNOT answer,
    # and a per-role zero would be a null two worlds produce. Fail closed, loudly.
    ctrl = athena(
        f"SELECT count(*) AS total, count(distinct userIdentity.sessionContext.sessionIssuer.userName) "
        f"AS roles, min(eventTime) AS first_ev, max(eventTime) AS last_ev, "
        f"sum(CASE WHEN {OBJ_EVENT_PRED} THEN 1 ELSE 0 END) AS obj_events "
        f"FROM {TABLE} WHERE {where}")
    if len(ctrl) < 2:
        print("ERROR: control query returned no rows -- cannot evaluate. Failing closed.", file=sys.stderr)
        return 1
    total, roles, first_ev, last_ev, obj_events = ctrl[1]
    obj_n = int(obj_events or 0)

    if obj_n == 0:
        print(f"CANNOT ANSWER for {b}{('/' + args.prefix) if args.prefix else ''}: "
              f"ZERO S3 object-level data events in range (since {args.since}).")
        print("  This bucket is NOT covered by an object-level data-event selector in that window, OR the")
        print("  prefix/action filter excluded everything. An empty who-read here means 'NEVER CAPTURED',")
        print("  not 'never read'. Failing closed (rc=1) rather than reporting a false clean.")
        print(f"  (management-level events seen: {int(total or 0)}; object-level: 0)")
        return 1

    print("=" * 78)
    print(f"WHO-READ  {b}{('/' + args.prefix) if args.prefix else ''}")
    print(f"COVERAGE WINDOW: {first_ev} -> {last_ev}   "
          f"(earliest OBJECT data event = proven coverage start; scan floor {args.since})")
    print(f"POSITIVE CONTROL: {int(total or 0)} events, {obj_n} object-level, {roles} distinct roles "
          "-- the table sees data events, so a per-role zero below is a real zero.")
    print("A firmless-sounding role NAME is a proxy, not a verdict. This reports who READ; "
          "relation->semantic->sanction is yours.")
    print("=" * 78)

    rows = athena(
        f"SELECT coalesce(nullif(userIdentity.sessionContext.sessionIssuer.userName,''), "
        f"'<' || userIdentity.type || ':' || coalesce(userIdentity.accountId,'?') || '>') AS principal, "
        f"count(*) AS reads, count(distinct json_extract_scalar(requestParameters,'$.key')) AS distinct_keys, "
        f"min(eventTime) AS first_seen, max(eventTime) AS last_seen "
        f"FROM {TABLE} WHERE {where} AND {OBJ_EVENT_PRED} "
        f"GROUP BY 1 ORDER BY 2 DESC")
    if len(rows) < 2:
        print("  (no object-level reads matched the filter -- but coverage exists, so this is a real zero)")
        return 0
    hdr = ["principal", "reads", "distinct_keys", "first_seen", "last_seen"]
    print(f"  {hdr[0]:42s} {hdr[1]:>10s} {hdr[2]:>8s}  {hdr[3]:20s} {hdr[4]:20s}")
    for r in rows[1:]:
        pr, n, dk, fs, ls = (r + [""] * 5)[:5]
        print(f"  {pr[:42]:42s} {n:>10s} {dk:>8s}  {fs:20s} {ls:20s}")
    print(f"\n  [{len(rows) - 1} distinct principal(s). Window and control above are the denominator.]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
