#!/usr/bin/env python3
"""Goal criterion 2 census: is every ACTIVE account in each firm's served directory resolvable in Performance?

Read-only, no vendor call. Per firm, the served directory (investor-reporting/directory/latest.json on the
firm's routed bucket) is the denominator: every account id under an entry not known TERMINATED (ACTIVE or UNKNOWN,
the indicator census printed). Each is tested by the SAME identity rule the served path uses:
  cottonwood   cot_account_mapping's source (blackdiamond/<firm>/silver/fact_model_assignment at the cutoff):
               opaque_account(firm, external_id) must match once, external_id z09 + the 8-digit BD id.
  49financial  f49_engine: the engine key (twr_daily, latest partition) by opaque_account, then the engine
               lane's own YTD cell (parity_period_returns) -- COMPUTED or its UNAVAILABLE-* outcome.
  inflection   orion_account_mapping: opaque_account(firm, str(accounts_v2.account_id)) at the cutoff.
"Resolvable" is the identity half only for COT and INF: a live number there also needs a worded one-use plan.
Output: counts per firm and outcome; no account id is written.

Usage (backend worktree root):
  python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/performance_resolvability_census.py \
      --as-of 2026-09-23 --ytd-end 2026-09-24 --out <receipt.json>
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
IR = ROOT / "infra/aws/lambda/investor-reporting"
for p in (ROOT / "lib", IR / "_ids", IR / "reports", IR / "performance", ROOT / "data/assets/scripts/gold/runners_49f",
          ROOT / "data/assets/scripts/gold/investor_reporting", ROOT / "data/assets/scripts/silver"):
    sys.path.insert(0, str(p))

import boto3  # noqa: E402
import pandas as pd  # noqa: E402

import orion_account_mapping  # noqa: E402
import parity_period_returns as ppr  # noqa: E402
import tenants  # noqa: E402
from f49_engine import TABLE_DAILY  # noqa: E402
from ids import opaque_account  # noqa: E402
from opal_naming import lookup  # noqa: E402
from rebalancer_conversion import silver_key  # noqa: E402


def routed_bucket(firm):
    aliases = [a["spelling"] for a in lookup(firm).get("aliases", [])
               if "bucket" in (a.get("planes") or []) and a.get("routed")]
    return aliases[0] if len(aliases) == 1 else lookup(firm)["bucket"]


def active_accounts(s3, firm):
    bucket = routed_bucket(firm)
    ptr = json.loads(s3.get_object(Bucket=bucket, Key="investor-reporting/directory/latest.json")["Body"].read())
    art = json.loads(s3.get_object(Bucket=bucket, Key=ptr["key"])["Body"].read())
    # Every account not known TERMINATED: the COT directory states UNKNOWN on all entries (its source
    # carries no termination), so ACTIVE alone would empty COT's denominator. The indicator census rides
    # beside the count so the reader sees which statuses the denominator holds.
    ids, indicators = set(), {}
    for entry in art.get("entries", []):
        indicator = (entry.get("termination") or {}).get("indicator")
        indicators[str(indicator)] = indicators.get(str(indicator), 0) + 1
        if indicator != "TERMINATED":
            ids.update((entry.get("ids") or {}).get("account_ids") or [])
    return ptr.get("as_of_business_date"), len(art.get("entries", [])), ids, indicators


def latest_partition(s3, bucket, prefix, token, as_of):
    days = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix, Delimiter="/"):
        for child in page.get("CommonPrefixes", []):
            t = child["Prefix"][len(prefix):].rstrip("/")
            if t.startswith(token) and t[len(token):] <= as_of:
                days.append(t[len(token):])
    return max(days) if days else None


def census_cot(s3, as_of, active):
    firm = tenants._CANONICAL_COT
    probe = silver_key("model_assignment", as_of)
    prefix = probe.rsplit("/", 2)[0] + "/"
    day = latest_partition(s3, "opal-data-assets", prefix, "date=", as_of)
    frame = pd.read_parquet(io.BytesIO(s3.get_object(Bucket="opal-data-assets", Key=silver_key("model_assignment", day))["Body"].read()))
    minted = {}
    for row in frame[["account_id", "external_id"]].to_dict("records"):
        ok = (isinstance(row["external_id"], str) and str(row["account_id"]).isdigit()
              and row["external_id"] == "z09" + str(int(row["account_id"])))
        minted.setdefault(opaque_account(firm, row["external_id"]), []).append(ok)
    out = {"source_date": day, "RESOLVED": 0, "UNMAPPED": 0, "DUPLICATE": 0, "IDENTITY_INVALID": 0}
    for a in active:
        hits = minted.get(a, [])
        out["UNMAPPED" if not hits else "DUPLICATE" if len(hits) > 1 else "RESOLVED" if hits[0] else "IDENTITY_INVALID"] += 1
    return out


def census_inf(s3, as_of, active):
    firm = tenants._CANONICAL_INF
    bucket = routed_bucket(firm)
    prefix = orion_account_mapping.table_prefix()
    day = latest_partition(s3, bucket, prefix, "snapshot_date=", as_of)
    frame = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=bucket, Key="%ssnapshot_date=%s/data.parquet" % (prefix, day))["Body"].read()))
    minted = {opaque_account(firm, str(int(v))) for v in frame["account_id"].dropna()}
    resolved = sum(1 for a in active if a in minted)
    return {"source_date": day, "RESOLVED": resolved, "UNMAPPED": len(active) - resolved}


def census_49f(s3, ytd_end, active):
    firm = tenants._CANONICAL_49F
    info = lookup(firm)
    bucket, prefix = info["bucket"], "%s/%s/" % (info["trees"]["advi"]["gold_root"], TABLE_DAILY)
    parts = sorted(p["Prefix"][len(prefix) + 5:].rstrip("/") for page in s3.get_paginator("list_objects_v2").paginate(
        Bucket=bucket, Prefix=prefix, Delimiter="/") for p in page.get("CommonPrefixes", []))
    start = "%s-01-01" % ytd_end[:4]
    before = [d for d in parts if d < start]
    read = ([before[-1]] if before else []) + [d for d in parts if start <= d <= ytd_end]

    def one(day):
        raw = s3.get_object(Bucket=bucket, Key="%sdate=%s/data.parquet" % (prefix, day))["Body"].read()
        return pd.read_parquet(io.BytesIO(raw), columns=["account_id", "business_date", "r_net", "r_gross", "status"])
    with ThreadPoolExecutor(max_workers=16) as pool:
        daily = pd.concat(list(pool.map(one, read)), ignore_index=True)
    latest_keys = set(daily.loc[daily["business_date"].astype(str).str[:10] == read[-1], "account_id"].astype(str))
    by_canonical = {opaque_account(firm, k): k for k in latest_keys}
    spine = {date.fromisoformat(d) for d in read}
    out = {"engine_latest_partition": read[-1], "UNMAPPED": 0}
    for a in active:
        key = by_canonical.get(a)
        if key is None:
            out["UNMAPPED"] += 1
            continue
        cell = ppr.link_account_period(daily, key, "YTD", ytd_end, spine, earliest_partition=parts[0])
        out[cell["outcome"]] = out.get(cell["outcome"], 0) + 1
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--as-of", required=True)
    ap.add_argument("--ytd-end", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--firms", nargs="*", default=None)
    args = ap.parse_args(argv)
    s3 = boto3.client("s3", region_name="us-east-1")
    receipt = {"schema_version": "irpt-performance-resolvability-census-v1", "by": "2.0.0_SA_COO~P",
               "criterion": "goal (2): every active client account at each firm resolvable in Performance",
               "as_of": args.as_of, "ytd_end": args.ytd_end, "firms": {}}
    for firm, fn, arg in ((tenants._CANONICAL_COT, census_cot, args.as_of),
                          (tenants._CANONICAL_49F, census_49f, args.ytd_end),
                          (tenants._CANONICAL_INF, census_inf, args.as_of)):
        if args.firms and firm not in args.firms:
            continue
        dir_as_of, entries, active, indicators = active_accounts(s3, firm)
        row = {"directory_as_of": dir_as_of, "directory_entries": entries, "entry_indicators": indicators,
               "accounts_not_terminated": len(active)}
        row.update(fn(s3, arg, active))
        receipt["firms"][firm] = row
    Path(args.out).write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
