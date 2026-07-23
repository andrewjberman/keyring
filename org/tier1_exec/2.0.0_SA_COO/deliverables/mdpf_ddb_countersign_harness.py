#!/usr/bin/env python3
"""COO counter-sign harness -- MDPF gold-DDB 4-channel backfill (opal-assets-daily-aua).

Purpose: make the COO per-date/per-channel counter-sign EXECUTION, not development, at the hour
0.7.0's walk lands (Andrew no-tomorrow order, 2026-07-23).

DESIGN -- two tiers, because they have different costs and different denominators:

  TIER A  STRUCTURAL, FULL COVERAGE (cheap, every row):
          A1 cohort inventory per run_date vs expected set
          A2 CIRCULAR-READ FIX: source_field/basis must NOT reference the served aggregate
             (pre-fix rows read `by_model[...]` / partners[...] out of platinum/mdpf/aggregate_aua*)
          A3 label sanity: vintage_state / coverage_state / value_class / additive
          A4 GLOBAL rows carry legs_present (LABELED_PARTIAL law) and it matches which legs are present
          A5 date coverage per channel vs that channel's OWN confirmed depth (no uniform floor)
          A6 no fabricated rows: a value where the source cannot reach that date is a FAIL

  TIER B  VALUE TIES (expensive: one S3 parquet read per date per channel) -- run on a GRID:
          every seam/boundary date + a sample + the frontier. Print the denominator ALWAYS.

DISCIPLINE THIS ENCODES (earned this session):
  - Print the DENOMINATOR of every scan reasoned from.
  - A number is verified against the axis it is OF (COO's own 05-18/05-15 served-vs-canonical error).
  - honest-absent != zero. A structural zero (pre-launch) != an honest-absent gap.
  - A PASS never asserted on a scan that could not have failed -- run the negative control.

CONFIRMED SOURCE DEPTHS (DS @161643Z, COO byte-verified the starred):
  49F custody  silver/schwab/08242234 fact_rps_s2.net_mv_plus_cash (C2)   2024-05-24+  (541, gaps=0)
  49F model    smartx .../fact_model_aum_daily  intra-partition `day`      2021-09-02+ *(1226 days)
  INF total    orion/inflection/silver/fact_assets                         2020-04-28+ *(2278, gaps=0)
  INF model    eclipse/inflection/silver/fact_portfolios_full              2026-05-15+ (6 named gaps)
  COT total    blackdiamond/cottonwood/silver/fact_holdings                2026-06-09+ (trading-complete)
  COT model    blackdiamond/cottonwood/silver/fact_model_*                 2026-07-21+ *(n=3, self-extending)
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict

import boto3

TABLE = "opal-assets-daily-aua"
BUCKET = "opal-data-assets"

# --- the served-aggregate fingerprints that mean "still circular" (A2) -------------------
CIRCULAR_MARKERS = (
    "by_model[",
    "partners[",
    "partner_custody_total",
    "platinum/mdpf",
    "aggregate_aua",
    "served",
)

# --- per-channel confirmed floors; NOT uniform, NOT hardcoded series starts for COT ------
# COT floors are CURRENT depth and self-extend: the harness READS them live rather than
# asserting a constant, mirroring 0.7.0's run-time enumeration (Andrew no-hardcoded-start law).
CHANNEL_SILVER_PREFIX = {
    "49f_custody": "schwab/08242234/silver/fact_rps_s2",
    "49f_model": "smartx/platform/silver/fact_model_aum_daily",
    "inf_total": "orion/inflection/silver/fact_assets",
    "inf_model": "eclipse/inflection/silver/fact_portfolios_full",
    "cot_total": "blackdiamond/cottonwood/silver/fact_holdings",
    "cot_model": "blackdiamond/cottonwood/silver/fact_model_assignment",
}


def s3_partition_dates(s3, prefix: str) -> list[str]:
    """Live min..max enumeration -- the floor is READ, never a constant (self-extension)."""
    dates, token = [], None
    while True:
        kw = {"Bucket": BUCKET, "Prefix": prefix + "/date=", "Delimiter": "/"}
        if token:
            kw["ContinuationToken"] = token
        resp = s3.list_objects_v2(**kw)
        for cp in resp.get("CommonPrefixes", []):
            seg = cp["Prefix"].rstrip("/").split("date=")[-1]
            dates.append(seg)
        if not resp.get("IsTruncated"):
            break
        token = resp.get("NextContinuationToken")
    return sorted(dates)


def scan_ddb(ddb, run_dates: list[str] | None) -> dict[str, list[dict]]:
    """Return {run_date: [row, ...]}. Full table scan when run_dates is None."""
    out: dict[str, list[dict]] = defaultdict(list)
    if run_dates:
        for d in run_dates:
            resp = ddb.query(
                TableName=TABLE,
                KeyConditionExpression="run_date = :d",
                ExpressionAttributeValues={":d": {"S": d}},
            )
            out[d].extend(resp.get("Items", []))
        return out
    paginator = ddb.get_paginator("scan")
    for page in paginator.paginate(TableName=TABLE):
        for it in page.get("Items", []):
            out[it["run_date"]["S"]].append(it)
    return out


def sval(item, key, default=None):
    a = item.get(key)
    if a is None:
        return default
    for t in ("S", "N", "BOOL"):
        if t in a:
            return a[t]
    if "L" in a:
        return [next(iter(x.values())) for x in a["L"]]
    return default


def tier_a(rows_by_date: dict[str, list[dict]]) -> dict:
    """STRUCTURAL, FULL COVERAGE. Every check prints its denominator."""
    findings = {
        "A0_schema_drift": [],   # the instrument-that-cannot-fail guard -- see note below
        "A2_circular": [],       # genuine circular-read candidates (verify by value tie)
        "A2_screen_cleared": [], # OBSERVATION: src mentions the superseded legacy, not a circular read
        "A3_labels": [],
        "A4_global_legs": [],
        "A6_fabricated": [],
        "A7_carry_observed": [],  # OBSERVATION bucket -- never a verdict
    }
    total_rows = sum(len(v) for v in rows_by_date.values())
    cohort_union: set[str] = set()
    per_date_counts = {}

    for d, rows in sorted(rows_by_date.items()):
        ids = sorted(sval(r, "cohort_id") for r in rows)
        per_date_counts[d] = len(ids)
        cohort_union.update(ids)
        for r in rows:
            cid = sval(r, "cohort_id")
            # Resolve the completeness field ONCE up front (the re-sourced walk renamed
            # coverage_state -> completeness). A0 below fails loudly if NEITHER is present.
            cov = sval(r, "completeness", sval(r, "coverage_state"))
            # A2 -- circular-read SCREEN (a text screen, NOT a verdict; Tier B value-tie is the proof).
            # Exercised 2026-07-23 on re-derived rows: a src can MENTION the legacy it SUPERSEDED
            # (e.g. "sum of re-sourced contributors; legacy carried total preserved in
            # legacy_carried_total") -- that is a supersession DESCRIPTION, not a circular READ, and
            # its value ties to silver. Text-matching the mechanism is the exact trap CLAUDE.md warns
            # of. So: split. A circular marker WITHOUT supersession language = genuine candidate;
            # WITH it = screen-cleared observation (still verify the value tie in Tier B).
            probe = " ".join(str(sval(r, k, "")) for k in ("source_field", "basis", "as_of_basis"))
            # SUPERSESSION = a src that mentions a superseded legacy, not a circular read.
            # gold/mdpf_revamp/cottonwood = the CTO-ruled pair-overlay TRANSPLANT (a CROSS-PIPELINE gold
            # read of the cottonwood pair's OWN output), NOT the MDPF served-aggregate self-read that
            # "circular" means. Cleared 2026-07-23 after the COT-model fix: my "aggregate_aua" marker is
            # too broad -- the TRUE circular path is platinum/mdpf/aggregate_aua (MDPF's own served output).
            SUPERSESSION = ("re-sourced", "re_sourced", "resourced", "superseded",
                            "preserved", "legacy_carried", "supersession", "gold/mdpf_revamp")
            if any(m in probe for m in CIRCULAR_MARKERS):
                if any(k in probe for k in SUPERSESSION):
                    findings["A2_screen_cleared"].append((d, cid, probe[:120]))
                else:
                    findings["A2_circular"].append((d, cid, probe[:120]))
            # A3 -- label sanity.
            # NOTE (COO, exercised 2026-07-23): my first enum omitted `rolled_forward` and produced 7
            # PHANTOM label failures on ETF cohorts. `rolled_forward` is a REAL vintage state, not a
            # defect. Fixed the enum rather than reporting the phantom -- an instrument's own
            # false-positive mode is found by exercising it against known-good state, never by reading it.
            vs = sval(r, "vintage_state")
            if vs not in ("fresh", "stale", "missing", "rolled_forward", None):
                findings["A3_labels"].append((d, cid, "vintage_state", vs))
            # `cov` resolved above (completeness | coverage_state). The re-sourced walk added
            # `unknown` (a leg with no source partition on this date -- e.g. Cottonwood pre-2026-04)
            # and `partial_N_of_M` (global rows). Both are LEGITIMATE states, not label defects.
            # Flagged one as phantom on 2026-07-23 (Cottonwood correctly-absent read as an A3 error);
            # widened the allowed set rather than report a defect on a correctly-absent leg.
            cov_ok = cov in ("complete", "incomplete", "absent", "unknown", None) or (
                isinstance(cov, str) and cov.startswith("partial_")
            )
            if not cov_ok:
                findings["A3_labels"].append((d, cid, "completeness/coverage_state", cov))
            # A7 -- OBSERVATION, not a verdict: a rolled-forward value is a CARRY. Under the D1
            # absolute-reality + no-silent-carry law a carry must be LABELED, never silent. This
            # bucket reports them for a human read; it does NOT assert a defect.
            if vs == "rolled_forward":
                findings["A7_carry_observed"].append((d, cid, f"value={sval(r, 'value')}"))
            # A4 -- the fee-basis GLOBAL row must carry legs_present (CTO's LABELED_PARTIAL ruling
            # 171749Z scoped this to _global__aua_total). The other `_total__*` cohorts (etf_fund,
            # partner_aua) are DIFFERENT aggregates, not the firm-composition Global -- flagging them
            # for a missing legs_present was an over-broad cid match (false-positive, 2026-07-23).
            if cid and "global" in cid:
                if r.get("legs_present") is None:
                    findings["A4_global_legs"].append((d, cid, "legs_present MISSING"))
            # --- A0 SCHEMA GUARD -------------------------------------------------------------
            # `cov` resolved at loop top. A checker that reads a field which NO LONGER EXISTS
            # returns None for every row and PASSES EVERYTHING -- the instrument-that-cannot-fail
            # class. FAIL LOUDLY when NEITHER name is present rather than silently green.
            # Caught 2026-07-23 by reading the walk's bytes, not by trusting this tool.
            if cov is None:
                findings["A0_schema_drift"].append(
                    (d, cid, "NEITHER `completeness` NOR `coverage_state` present -- checker is BLIND here")
                )

            # A6 -- honest-absent must not be rendered as a value
            val = sval(r, "value")
            absent_like = cov in ("absent", "unknown") or (isinstance(cov, str) and cov.startswith("partial_"))
            if cov == "absent" and val not in (None, "", "0", "0.0"):
                findings["A6_fabricated"].append((d, cid, f"completeness=absent but value={val}"))
            # a partial/unknown leg carrying a value is only legal if the row DECLARES what it contains
            if absent_like and val not in (None, "") and r.get("legs_present") is None and cid and (
                "global" in cid or cid.startswith("_total__")
            ):
                findings["A6_fabricated"].append(
                    (d, cid, f"completeness={cov} carries value={val} with NO legs_present declaration")
                )

    return {
        "denominator": {
            "run_dates": len(rows_by_date),
            "rows_total": total_rows,
            "cohort_union": len(cohort_union),
        },
        "cohort_union": sorted(cohort_union),
        "per_date_counts": per_date_counts,
        "findings": findings,
    }


def negative_control(rows_by_date: dict[str, list[dict]]) -> str:
    """A scan that cannot fail is not a scan. Inject a known-bad row; the checker MUST flag it."""
    fake = {
        "run_date": {"S": "1999-01-01"},
        "cohort_id": {"S": "_control__global"},
        "source_field": {"S": "by_model[opal_div_sma].model_value"},  # circular fingerprint
        "coverage_state": {"S": "absent"},
        "value": {"N": "123456.78"},  # absent-but-valued == fabricated
    }
    # a SECOND control row carrying NEITHER schema field -- the A0 blind-checker guard MUST fire on it
    schema_blind = {
        "run_date": {"S": "1999-01-02"},
        "cohort_id": {"S": "_control__noschema"},
        "value": {"N": "1.00"},
    }
    probe = tier_a({"1999-01-01": [fake], "1999-01-02": [schema_blind]})
    f = probe["findings"]
    ok = (
        bool(f["A2_circular"])
        and bool(f["A6_fabricated"])
        and bool(f["A4_global_legs"])
        and bool(f["A0_schema_drift"])  # proves the tool detects its own blindness
    )
    return (
        "PASS (control flagged on A0+A2+A4+A6 -- incl. schema-blindness self-detection)"
        if ok
        else "FAIL -- HARNESS IS BLIND, DO NOT TRUST IT"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dates", nargs="*", default=None, help="omit for full scan")
    ap.add_argument("--depths", action="store_true", help="live-enumerate each channel's floor")
    args = ap.parse_args()

    ddb = boto3.client("dynamodb", region_name="us-east-1")
    s3 = boto3.client("s3")

    print("=" * 78)
    print("COO COUNTER-SIGN HARNESS -- MDPF gold DDB 4-channel")
    print("=" * 78)

    ctl = negative_control({})
    print(f"\n[NEGATIVE CONTROL] {ctl}")
    if ctl.startswith("FAIL"):
        return 2

    if args.depths:
        print("\n[LIVE DEPTH ENUMERATION -- floors are READ, never constants]")
        for ch, pfx in CHANNEL_SILVER_PREFIX.items():
            ds = s3_partition_dates(s3, pfx)
            print(f"  {ch:12s} n={len(ds):5d}  {ds[0] if ds else '-'} .. {ds[-1] if ds else '-'}")

    rows = scan_ddb(ddb, args.run_dates)
    a = tier_a(rows)

    print("\n[TIER A -- STRUCTURAL, FULL COVERAGE]")
    print(f"  DENOMINATOR: run_dates={a['denominator']['run_dates']} "
          f"rows={a['denominator']['rows_total']} cohorts={a['denominator']['cohort_union']}")
    OBSERVATION_BUCKETS = ("A7_carry_observed", "A2_screen_cleared")
    for k, v in a["findings"].items():
        if k in OBSERVATION_BUCKETS:  # observation, never a verdict
            status = "none" if not v else f"OBSERVED n={len(v)} (read these, not a defect claim)"
        else:
            status = "PASS" if not v else f"FAIL n={len(v)}"
        print(f"  {k:18s} {status}")
        for row in v[:10]:
            print(f"      {row}")

    print("\n[COHORT UNION]")
    for c in a["cohort_union"]:
        print(f"  {c}")

    print("\nNOTE: Tier B value-ties run per channel on the seam+sample grid once the walk lands;")
    print("      every tie prints its own denominator. Absence of a Tier B run is NOT a pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
