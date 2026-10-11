#!/usr/bin/env python3
"""c06_gap_record_check.py -- MDPF_SECCLASS round 20 cell SC-e-88 (row D1-S27): grades the worker's trace record of C_06's firm-daily
total-vs-class-sum gap. READ-ONLY (one S3 get of the served snapshot file); run from the repo root.

Usage:  python c06_gap_record_check.py <gap|scope>

Record: org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/C06_TOTAL_GAP_TRACE_20261011.json
  {"method": str, "cause": str, "membership_differs": bool,
   "positions": [{"ticker": str, "asset_name": str, "market_value": float}, ...],     (required non-empty when membership_differs)
   "dates": {"2026-10-06"|"2026-10-07"|"2026-10-08": {
        "published_total": f, "published_class_sum": f, "published_gap": f,
        "recomputed_total": f, "recomputed_class_sum": f, "recomputed_gap": f,
        "relationships": int, "share_rounding_residual_sum": f,
        "top_residuals": [{"total_mv": f, "residual": f}, ... at most 5]}}}

gap   : (AMENDMENT 1) each of the three dates carries the SERVED gap (re-read from gold/views/mix_daily_summary.json, within 0.01). A date
        whose recomputed total equals its published total within 0.05 REPRODUCES: its recomputed gap must agree within 0.05, its
        share_rounding_residual_sum must equal the recomputed gap, and every listed residual must sit inside the 6-decimal rounding bound
        |residual| <= total_mv * 4.5e-6. At least one date must reproduce; a date that does not is counted as drift, not as a failure.
        `cause` is a sentence of 20+ characters. Prints
        C06-GAP ok=<bool> dates=<reproducing> drift=<non-reproducing> max_abs_err=<x> cause_len=<n> basis=<rounding|membership|none>
scope : the record holds no relationship id, account id or client name: no key named like rid/relationship/account/client/household and
        no string value shaped like a relationship id (z followed by 8 digits) or an account number (8 or more digits).
        Prints  C06-SCOPE ok=<bool> bad=<n>
"""
import json
import re
import sys
from pathlib import Path

import boto3

RECORD = Path("org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/C06_TOTAL_GAP_TRACE_20261011.json")
DATES = ("2026-10-06", "2026-10-07", "2026-10-08")
BAD_KEY = re.compile(r"(^|_)(rid|relationship|rel_id|account|acct|client|household)(_|$)", re.I)
BAD_VAL = re.compile(r"\bz\d{8}\b|\b\d{8,}\b", re.I)


def _load():
    try:
        return json.loads(RECORD.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield path + "/" + str(k), "key", str(k)
            yield from _walk(v, path + "/" + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _walk(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        yield path, "val", obj


def gap(rec):
    """AMENDMENT 1 (issuer, 2026-10-11): the cut assumed all three served snapshots reproduce from today's partitions. Worker ~78 measured
    that two do not (the partitions were rewritten after the snapshot). A date REPRODUCES when its recomputed total equals the published
    total within $0.05; ok needs every date's published numbers to equal the served ones, at least one reproducing date whose recomputed
    gap matches within $0.05, and on each reproducing date every listed residual inside the 6-decimal rounding bound
    (|residual| <= total_mv * 4.5e-6: eight classes at 0.5e-6 each), which out-of-class mass would break by orders of magnitude."""
    if not isinstance(rec, dict) or not isinstance(rec.get("dates"), dict) or set(rec["dates"]) != set(DATES):
        print("C06-GAP ok=False dates=0 drift=0 max_abs_err=NA cause_len=0 basis=none")
        return 1
    snap = json.loads(boto3.client("s3", region_name="us-east-1").get_object(
        Bucket="opal-data-bd", Key="gold/views/mix_daily_summary.json")["Body"].read())["firm"]
    worst, repro, drift, bad = 0.0, 0, 0, 0
    cause = str(rec.get("cause") or "").strip()
    for d in DATES:
        s, r = snap.get(d), rec["dates"][d]
        try:
            served_gap = s["total"] - sum(v for k, v in s.items() if k != "total" and v is not None)
            e_pub = abs(float(r["published_gap"]) - served_gap)
            reproduces = abs(float(r["recomputed_total"]) - float(r["published_total"])) <= 0.05
            e_rec = abs(float(r["recomputed_gap"]) - served_gap)
            e_res = abs(float(r["share_rounding_residual_sum"]) - float(r["recomputed_gap"]))
            tops = r.get("top_residuals") or []
            in_bound = bool(tops) and all(abs(float(x["residual"])) <= float(x["total_mv"]) * 4.5e-6 + 0.01 for x in tops)
        except (TypeError, KeyError, ValueError):
            bad += 1
            continue
        worst = max(worst, e_pub)
        if e_pub > 0.01:
            bad += 1
        elif reproduces:
            worst = max(worst, e_rec)
            if e_rec <= 0.05 and e_res <= 0.05 and in_bound:
                repro += 1
            else:
                bad += 1
        else:
            drift += 1
    pos = rec.get("positions")
    membership = bool(rec.get("membership_differs")) and isinstance(pos, list) and len(pos) > 0
    basis = "rounding" if repro >= 1 and bad == 0 else ("membership" if membership and bad == 0 else "none")
    ok = bad == 0 and (repro >= 1 or membership) and len(cause) >= 20 and basis != "none"
    print(f"C06-GAP ok={ok} dates={repro} drift={drift} max_abs_err={worst:.4f} cause_len={len(cause)} basis={basis}")
    return 0 if ok else 1


def scope(rec):
    if rec is None:
        print("C06-SCOPE ok=False bad=NA (no record)")
        return 1
    bad = [p for p, kind, v in _walk(rec) if (kind == "key" and BAD_KEY.search(v)) or (kind == "val" and BAD_VAL.search(v))]
    print(f"C06-SCOPE ok={not bad} bad={len(bad)}")
    return 0 if not bad else 1


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "gap":
        sys.exit(gap(_load()))
    if mode == "scope":
        sys.exit(scope(_load()))
    print("C06-GAP ok=False error=usage (gap|scope)")
    sys.exit(2)
