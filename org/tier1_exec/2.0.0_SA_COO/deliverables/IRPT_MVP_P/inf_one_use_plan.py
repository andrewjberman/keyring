#!/usr/bin/env python3
"""Build the ONE Inflection one-use Performance plan Andrew approved (record
org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_230xZ_INF_ORION_ONE_USE_APPROVED.md @dd8178481e):
one Orion call, one INF account ~P picks, window YTD ending the day of arming. NO VENDOR CALL HERE.

The account is picked by a stated rule, not by hand: in the served INF directory as not terminated, present in
accounts_v2 at the installation's mapping cutoff, is_active, not a sweep or sleeve account, opened before the
window start (so YTD is a full year), and at the 75th percentile of current_value among those. The plan is built
with the SERVED code path's own functions -- the INF mapping loader at the deployed cutoff, the currency binding
retained.py applies, orion_selected.requests_for, repository.digest -- so the gate's recomputation matches.

Output: the plan JSON (the deployed env value), its sha256, and a receipt; no client name is written.
Usage (backend worktree root):
  python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/inf_one_use_plan.py --end 2026-09-25 \
      --mapping-as-of 2026-09-23 --expires-at 2026-09-26T00:00:00Z --out <plan.json> --tfvars <tfvars.json>
"""
from __future__ import annotations

import argparse
import calendar
import copy
import hashlib
import io
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
# --tree <worktree>: build the plan with THAT tree's modules. The plan's requests_sha256 must equal what the DEPLOYED
# adapter computes, so a plan for a not-yet-merged adapter change is cut from the tree the package is built from.
if "--tree" in sys.argv:
    ROOT = Path(sys.argv[sys.argv.index("--tree") + 1]).resolve()
IR = ROOT / "infra/aws/lambda/investor-reporting"
for p in (ROOT / "lib", IR / "_ids", IR / "reports", IR / "performance",
          ROOT / "infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily"):
    sys.path.insert(0, str(p))

import boto3  # noqa: E402
import pandas as pd  # noqa: E402

import orion_account_mapping  # noqa: E402
import orion_selected  # noqa: E402
import tenants  # noqa: E402
from currency_authority import bind_report_currency  # noqa: E402
from ids import opaque_account  # noqa: E402
from repository import digest  # noqa: E402

APPROVAL_REF = ("org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_230xZ_INF_ORION_ONE_USE_APPROVED.md"
                " @dd8178481e")


def routed_bucket(firm):
    from opal_naming import lookup
    aliases = [a["spelling"] for a in lookup(firm).get("aliases", [])
               if "bucket" in (a.get("planes") or []) and a.get("routed")]
    return aliases[0] if len(aliases) == 1 else lookup(firm)["bucket"]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--end", required=True)
    ap.add_argument("--mapping-as-of", required=True)
    ap.add_argument("--expires-at", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tfvars", required=True)
    # 2026-09-25 23:0xZ: the 0279 plan picked an account whose directory entry held TWO accounts; the portal
    # selects a whole entry and Performance computes exactly one account, so it was unreachable. A plan is now
    # picked only among entries holding exactly ONE account (the default), and cites the approval it runs under.
    ap.add_argument("--any-entry", action="store_true", help="drop the single-account-entry constraint")
    ap.add_argument("--approval-ref", default=APPROVAL_REF)
    ap.add_argument("--tree", help="worktree whose adapter modules build the plan (default: this workspace)")
    args = ap.parse_args(argv)
    firm = tenants._CANONICAL_INF
    start = "%s-01-01" % args.end[:4]
    s3 = boto3.client("s3", region_name="us-east-1")
    bucket = routed_bucket(firm)

    ptr = json.loads(s3.get_object(Bucket=bucket, Key="investor-reporting/directory/latest.json")["Body"].read())
    art = json.loads(s3.get_object(Bucket=bucket, Key=ptr["key"])["Body"].read())
    active = set()
    names = {}
    for entry in art.get("entries", []):
        accounts = (entry.get("ids") or {}).get("account_ids") or []
        if (entry.get("termination") or {}).get("indicator") != "TERMINATED" and (args.any_entry or len(accounts) == 1):
            active.update(accounts)
            for a in accounts:
                names[a] = "%s %s" % (entry.get("display_name"), entry.get("masked_discriminator"))

    prefix = orion_account_mapping.table_prefix()
    days = sorted(p["Prefix"][len(prefix):].rstrip("/").split("=", 1)[1]
                  for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix, Delimiter="/")
                  for p in page.get("CommonPrefixes", []))
    cut = max(d for d in days if d <= args.mapping_as_of)
    frame = pd.read_parquet(io.BytesIO(s3.get_object(
        Bucket=bucket, Key="%ssnapshot_date=%s/data.parquet" % (prefix, cut))["Body"].read()))
    # Row IRPT_BCKEND-S143 (backend a7e9f51c77): Orion is addressed through the account's HOUSEHOLD, so only an account
    # whose household holds no other account in this snapshot (any status) is reachable; the mapping refuses the rest.
    per_household = frame.groupby("household_id")["account_id"].transform("count")
    frame = frame[per_household == 1]
    frame = frame[frame["is_active"].astype(bool) & ~frame["is_sweep_account"].fillna(False).astype(bool)
                  & ~frame["is_sleeve_account"].fillna(False).astype(bool)]
    frame = frame[pd.to_datetime(frame["account_start_date"], errors="coerce", utc=True)
                  < pd.Timestamp(start, tz="UTC")]
    frame = frame.assign(opaque=[opaque_account(firm, str(int(v))) for v in frame["account_id"]])
    frame = frame[frame["opaque"].isin(active)].sort_values(["current_value", "opaque"])
    pick = frame.iloc[int(0.75 * (len(frame) - 1))]
    account = pick["opaque"]

    load = orion_account_mapping.make_inf_mapping_loader(s3, bucket=bucket, as_of=args.mapping_as_of)
    mapping = copy.deepcopy(load(firm, account))
    mapping.update(bind_report_currency(firm, mapping.get("currency")))      # as retained.compute does
    requests = orion_selected.requests_for(mapping, account, start, args.end)
    expires = calendar.timegm(time.strptime(args.expires_at, "%Y-%m-%dT%H:%M:%SZ"))
    plan = {"schema_version": "irpt-performance-one-use-v1", "approval_ref": args.approval_ref, "firm_id": firm,
            "account_id": account, "vendor_account_id": mapping["vendor_account_id"],
            "vendor_external_id": mapping.get("vendor_external_id"), "mapping_revision": mapping["source_revision"],
            "start": start, "end": args.end, "expires_at": expires, "requests_sha256": digest(requests)}
    plan_json = json.dumps(plan, sort_keys=True, separators=(",", ":"))
    receipt = {"schema_version": "irpt-inf-one-use-plan-v1", "by": "2.0.0_SA_COO~P", "approval_ref": args.approval_ref,
               "rule": ("INF directory not-terminated%s, the Orion household holds only that account (S143), accounts_v2 at cutoff, is_active, not sweep/sleeve, opened "
                        "before the window start, 75th percentile of current_value"
                        % ("" if args.any_entry else ", the entry holds exactly ONE account")),
               "eligible": int(len(frame)), "picked_rank": int(0.75 * (len(frame) - 1)),
               "accounts_v2_cutoff": cut, "directory_as_of": ptr.get("as_of_business_date"),
               "plan": plan, "plan_sha256_of_digest": digest(plan),
               "plan_json_sha256": hashlib.sha256(plan_json.encode("utf-8")).hexdigest(),
               "vendor_call_made": False}
    Path(args.out).write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    Path(args.tfvars).write_text(json.dumps({"approved_performance_plan": plan_json}) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in receipt.items() if k != "plan"}, indent=1))
    print(json.dumps({k: plan[k] for k in ("account_id", "start", "end", "expires_at", "mapping_revision")}, indent=1))
    # The client to search for, printed to the terminal for the operator only -- never written to a file.
    print("SEARCH FOR (terminal only):", names.get(account))
    return 0


if __name__ == "__main__":
    sys.exit(main())
