#!/usr/bin/env python3
"""served-value-freeze-check -- detect a served VALUE that is frozen while its VINTAGE advances.

    A served numeric that is byte-identical across N advancing vintages is FROZEN,
    regardless of how fresh the object or the vintage is.

WHY THIS CLASS IS INVISIBLE TO EVERY EXISTING CHECK
---------------------------------------------------
- object-age monitoring: GREEN (the object is rewritten every morning)
- vintage monitoring:    GREEN-ish (data_as_of advances 07-02 -> 07-06 -> 07-07)
- value:                 DEAD (identical to the cent for three days)

Found 2026-07-09 on `s3://opal-data-bd/platinum/firm/header_metrics.json`:
`total.aua` = 1,837,159,865.68 across **8 consecutive writes** and **3 distinct
data_as_of dates**; last moved 07-04 (+$8,570,986.97). A client-facing $1.837B AUA,
frozen since 07-06T21:26Z, with five `bd-served-vintage-stale-*` alarms latched 67h --
watching OBJECT AGE, not VALUE. **The alarm that was latched was not watching the field
that broke.**

COO's chain (source + live, end to end) shows why no single component is buggy:
    wall-clock-UTC as-of -> BD returns a header-only workbook -> silver/allocations = 0 rows
    C_02:331  certified_aua <= 0 -> SKIP        (BRANCH-A floor: refuses a degenerate cert)
    D_00      no-$0 guard        -> HOLD last-good certified  (refuses to serve $0)
    served    rewritten daily, vintage advances, value = the stale cert
**Every guard did exactly what it was written to do.** The freeze is what CORRECT guards
produce when the input is a stub and the monitoring watches the wrapper instead of the
contents. Do not "fix" C_02 or D_00 on the strength of this tool's output.

THE METHOD (generalizes to any versioned served artifact)
---------------------------------------------------------
S3 object versioning IS a time series. Everyone -- COO included -- had been reading the
CURRENT object and arguing about mechanism. The history was sitting in the bucket. Turn a
point-in-time observation into a series and the series answers it in one look.

Read-only. No writes, no producer touched, no ad-hoc gold run. ASCII only.
"""
from __future__ import annotations

import argparse
import json
import sys

try:
    import boto3
except ImportError:  # pragma: no cover
    print("ERROR: boto3 not available", file=sys.stderr)
    raise SystemExit(2)


def dig(d, path: str):
    """Fetch a dotted field path; None if absent. Never raises on shape surprises."""
    cur = d
    for part in path.split("."):
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
                continue
            except (ValueError, IndexError):
                return None
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def main() -> int:
    ap = argparse.ArgumentParser(description="Detect a frozen served value under an advancing vintage")
    ap.add_argument("uri", help="s3://bucket/key")
    ap.add_argument("--field", required=True, help="dotted path to the value, e.g. total.aua")
    ap.add_argument("--vintage", default="data_as_of", help="dotted path to the vintage field")
    ap.add_argument("--versions", type=int, default=12, help="how many recent versions to read")
    ap.add_argument("--min-vintages", type=int, default=2,
                    help="FROZEN requires the value constant across at least this many DISTINCT vintages")
    ap.add_argument("--strict", action="store_true", help="exit 1 if FROZEN")
    args = ap.parse_args()

    if not args.uri.startswith("s3://"):
        print("ERROR: uri must be s3://bucket/key", file=sys.stderr)
        return 2
    bucket, _, key = args.uri[5:].partition("/")

    s3 = boto3.client("s3", region_name="us-east-1")
    vs = s3.list_object_versions(Bucket=bucket, Prefix=key).get("Versions", [])
    vs = [v for v in vs if v["Key"] == key]
    if not vs:
        print(f"ERROR: no versions for {args.uri} (is versioning enabled?)", file=sys.stderr)
        return 2
    vs.sort(key=lambda v: v["LastModified"], reverse=True)
    vs = vs[: args.versions]

    rows = []
    for v in vs:
        o = s3.get_object(Bucket=bucket, Key=key, VersionId=v["VersionId"])
        try:
            d = json.loads(o["Body"].read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001 -- surface, never drop
            rows.append((v["LastModified"], f"<unparseable: {type(e).__name__}>", None))
            continue
        rows.append((v["LastModified"], dig(d, args.vintage), dig(d, args.field)))

    print(f"served-value-freeze-check  {args.uri}")
    print(f"  field={args.field}  vintage={args.vintage}  versions={len(rows)}")
    print()
    print(f"  {'written_at (UTC)':<22} {str(args.vintage):<12} {args.field:>22}")
    print("  " + "-" * 60)
    for lm, vin, val in rows:
        shown = f"{val:,.2f}" if isinstance(val, (int, float)) else str(val)
        print(f"  {lm.strftime('%Y-%m-%dT%H:%M:%SZ'):<22} {str(vin):<12} {shown:>22}")
    print()

    values = [r[2] for r in rows if r[2] is not None]
    if not values:
        print("SKIP: field never resolved -- could not verify. That is a finding, not a pass.")
        return 0

    # THE TRAILING RUN IS THE SIGNAL, NOT THE WHOLE WINDOW.
    #
    # My first cut asked "is the value constant across every version in the window?" The
    # POSITIVE CONTROL falsified it: over 9 bd versions there are 2 distinct values,
    # because the window reaches back to 2026-07-04 when AUA last moved. It printed
    # "OK: varies" on the very artifact whose freeze prompted the tool.
    #
    # A freeze is not "never changed". It is "STOPPED changing while vintages kept
    # advancing." So: walk from newest backwards while the value is unchanged, and count
    # the DISTINCT vintages that run spans. The vintage span is what separates a freeze
    # from a quiet series -- a value unchanged within ONE vintage is expected (same data,
    # same answer); unchanged ACROSS advancing vintages is not.
    # Walk newest -> oldest. A row whose field is absent (None -- schema drift; inf's
    # book.json gained `headline.total_aua` partway through its history) carries NO
    # evidence either way: it must not TRUNCATE the run, or one schema gap two writes
    # back would hide a live freeze behind it. Skip it, count it, and never let it
    # extend the vintage span. Only a DIFFERENT resolved value ends the run.
    newest_val = next((r[2] for r in rows if r[2] is not None), None)
    if newest_val is None:
        print("SKIP: field never resolved in any version -- could not verify. That is a finding, not a pass.")
        return 0
    run_rows, unresolved = [], 0
    for lm, vin, val in rows:
        if val is None:
            unresolved += 1
            continue
        if val != newest_val:
            break
        run_rows.append((lm, vin, val))
    run_vintages = sorted({r[1] for r in run_rows if r[1] is not None})
    if unresolved:
        print(f"  NOTE: {unresolved} version(s) did not carry `{args.field}` (schema drift); "
              f"skipped, never used to extend or truncate the run.")

    all_vintages = sorted({r[1] for r in rows if r[1] is not None})
    print(f"  distinct vintages in window : {len(all_vintages)}  {all_vintages}")
    print(f"  trailing constant run       : {len(run_rows)} write(s) at "
          f"{newest_val:,.2f}" if isinstance(newest_val, (int, float)) else
          f"  trailing constant run       : {len(run_rows)} write(s) at {newest_val}")
    print(f"  vintages spanned by that run: {len(run_vintages)}  {run_vintages}")
    print()

    if len(run_vintages) >= args.min_vintages:
        shown = f"{newest_val:,.2f}" if isinstance(newest_val, (int, float)) else newest_val
        oldest_in_run = run_rows[-1][0].strftime("%Y-%m-%dT%H:%M:%SZ")
        print(f"FROZEN: {args.field} = {shown} unchanged across {len(run_rows)} consecutive write(s) "
              f"spanning {len(run_vintages)} DISTINCT vintages (since {oldest_in_run}).")
        print("        A lag shifts a series; it does not flatten it. The vintage advanced and the value did not.")
        print("        This tool reports the SYMPTOM. Mechanism is NOT established here -- do not claim a root cause,")
        print("        and do not 'fix' a downstream guard that may be behaving correctly.")
        return 1 if args.strict else 0

    if len(all_vintages) < args.min_vintages:
        print(f"INCONCLUSIVE: only {len(all_vintages)} distinct vintage(s) in the window. Widen --versions.")
        return 0

    print(f"OK: {args.field} is not frozen -- its trailing constant run spans "
          f"{len(run_vintages)} vintage(s) (< {args.min_vintages}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
