#!/usr/bin/env python3
"""Build the ONE Cottonwood one-use Performance plan Andrew approved (call 3 of "yes to all three", record
org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260927_025xZ_YES_TO_ALL_THREE_P_OPEN_CALLS.md @6039c2f680).
NO VENDOR CALL HERE.

The rule (stated, not by hand):
- in the served Cottonwood directory, not terminated, and the entry holds exactly ONE account;
- the served COT mapping loads it at the installation's mapping cutoff without refusal, and bd_selected.requests_for
  accepts it;
- the MEDIAN of those by opaque account id (the COT directory carries no value field, so the pick cannot be
  value-ranked).

The window is YTD. Its end is READ at build from the served COT holdings answer for the picked account (CTO 101756's
rule for INF, applied the same way), so the plan matches the window the page requests. The plan is built with the
SERVED code path's own functions -- make_cot_mapping_loader, the currency binding retained.py applies,
bd_selected.requests_for, repository.digest -- so the gate's recomputation matches.

Usage:
  python cot_one_use_plan.py --tree <backend worktree> --mapping-as-of 2026-09-23 --expires-at <ISO Z> \
      --out <plan.json> --tfvars <tfvars.json>
Output: the receipt (no client name), the plan JSON as the tfvars value, and the client to search for, printed to the
terminal only.
"""
from __future__ import annotations

import argparse
import calendar
import copy
import hashlib
import json
import sys
import time
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parents[5]
if "--tree" in sys.argv:
    ROOT = Path(sys.argv[sys.argv.index("--tree") + 1]).resolve()
IR = ROOT / "infra/aws/lambda/investor-reporting"
for p in (ROOT / "lib", IR / "_ids", IR / "reports", IR / "performance", ROOT / "data/assets/scripts/gold/investor_reporting"):
    sys.path.insert(0, str(p))

import bd_selected  # noqa: E402
import tenants  # noqa: E402
from cot_account_mapping import make_cot_mapping_loader  # noqa: E402
from currency_authority import bind_report_currency  # noqa: E402
from repository import digest  # noqa: E402

APPROVAL_REF = ("Andrew-direct 2026-09-27T02:5xZ (2.0.0_SA_COO~P terminal): 'yes to all three' -- call 3, ONE Cottonwood "
                "one-use Performance plan for one signed-in COT run, record org/tier1_exec/2.0.0_SA_COO/deliverables/"
                "ANDREW_DIRECT_20260927_025xZ_YES_TO_ALL_THREE_P_OPEN_CALLS.md @6039c2f680")
HEADERS = {"x-origin-verify": "cloudfront", "x-user-role": "user", "x-contract-version": "v1",
           "x-user-tier": "internal", "x-firm-id": "opal-capital",
           "x-user-email": "cot-plan-build@opal.test", "x-user-name": "cot plan build"}


def _invoke(function, event):
    lam = boto3.client("lambda", region_name="us-east-1")
    body = json.loads(lam.invoke(FunctionName=function, Payload=json.dumps(event).encode())["Payload"].read())
    return json.loads(body["body"]) if isinstance(body.get("body"), str) else body


def served_entries():
    """The served Cottonwood directory, every browse page (the page's own read path)."""
    out, cursor = [], None
    for _ in range(50):
        q = {"limit": "100", "selected_tenant": "cottonwood"}
        if cursor:
            q["cursor"] = cursor
        data = _invoke("irpt-directory-search", {"version": "2.0",
                       "routeKey": "GET /api/scoped/investor-reporting/directory/browse",
                       "headers": HEADERS, "queryStringParameters": q}).get("data") or {}
        out += data.get("entries") or []
        cursor = data.get("next_cursor")
        if not cursor:
            return out
    raise SystemExit("STOP: the directory browse did not end")


def holdings_as_of(account):
    """The served holdings business_date for ONE account: the date the page ends Performance windows on."""
    sel = _invoke("irpt-directory-search", {"version": "2.0", "routeKey": "POST /api/scoped/investor-reporting/selections",
                  "headers": dict(HEADERS, **{"content-type": "application/json"}), "isBase64Encoded": False,
                  "queryStringParameters": {"selected_tenant": "cottonwood"},
                  "body": json.dumps({"scope_kind": "ACCOUNT", "scope_ids": [account]})})
    ref = (sel.get("data") or {}).get("account_set_id")
    if not ref:
        raise SystemExit("STOP: the selection was refused: %s" % json.dumps(sel.get("status"))[:200])
    h = _invoke("irpt-holdings", {"version": "2.0", "routeKey": "GET /api/scoped/investor-reporting/holdings/{accountSetId}",
                "headers": HEADERS, "pathParameters": {"accountSetId": ref},
                "queryStringParameters": {"selected_tenant": "cottonwood"}})
    dates = (h.get("status") or {}).get("source_dates") or {}
    if (h.get("status") or {}).get("state") not in ("READY", "PARTIAL") or not dates.get("business_date"):
        raise SystemExit("STOP: the holdings are not READY for the pick: %s" % json.dumps(h.get("status"))[:200])
    return dates["business_date"], ref


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mapping-as-of", required=True)
    ap.add_argument("--expires-at", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tfvars", required=True)
    ap.add_argument("--approval-ref", default=APPROVAL_REF)
    ap.add_argument("--tree")
    args = ap.parse_args(argv)
    firm = tenants._CANONICAL_COT
    s3 = boto3.client("s3", region_name="us-east-1")
    load = make_cot_mapping_loader(s3, as_of=args.mapping_as_of)

    entries = served_entries()
    names, candidates = {}, []
    for e in entries:
        accounts = (e.get("ids") or {}).get("account_ids") or []
        if (e.get("termination") or {}).get("indicator") == "TERMINATED" or len(accounts) != 1:
            continue
        names[accounts[0]] = "%s %s" % (e.get("display_name"), e.get("masked_discriminator"))
        candidates.append(accounts[0])
    eligible, refused = [], 0
    for account in sorted(candidates):
        try:
            mapping = copy.deepcopy(load(firm, account))
            mapping.update(bind_report_currency(firm, mapping.get("currency")))
            bd_selected.requests_for(mapping, account, "2026-01-01", "2026-01-02")
            eligible.append(account)
        except Exception:  # a refused mapping is not eligible; the count is reported
            refused += 1
    if not eligible:
        raise SystemExit("STOP: no eligible Cottonwood account")
    rank = (len(eligible) - 1) // 2
    account = eligible[rank]

    end, selection = holdings_as_of(account)
    start = "%s-01-01" % end[:4]
    mapping = copy.deepcopy(load(firm, account))
    mapping.update(bind_report_currency(firm, mapping.get("currency")))       # as retained.compute does
    requests = bd_selected.requests_for(mapping, account, start, end)
    expires = calendar.timegm(time.strptime(args.expires_at, "%Y-%m-%dT%H:%M:%SZ"))
    plan = {"schema_version": "irpt-performance-one-use-v1", "approval_ref": args.approval_ref, "firm_id": firm,
            "account_id": account, "vendor_account_id": mapping["vendor_account_id"],
            "vendor_external_id": mapping.get("vendor_external_id"), "mapping_revision": mapping["source_revision"],
            "start": start, "end": end, "expires_at": expires, "requests_sha256": digest(requests)}
    plan_json = json.dumps(plan, sort_keys=True, separators=(",", ":"))
    receipt = {"schema_version": "irpt-cot-one-use-plan-v1", "by": "2.0.0_SA_COO~P", "approval_ref": args.approval_ref,
               "rule": ("served COT directory not-terminated, the entry holds exactly ONE account, the served COT "
                        "mapping loads it at the cutoff and bd_selected.requests_for accepts it; the MEDIAN by opaque "
                        "account id (the directory carries no value field)"),
               "directory_entries": len(entries), "single_account_candidates": len(candidates),
               "mapping_refused": refused, "eligible": len(eligible), "picked_rank": rank,
               "end_source": "served irpt-holdings source_dates.business_date for selection %s" % selection,
               "mapping_as_of": args.mapping_as_of, "plan": plan, "plan_sha256_of_digest": digest(plan),
               "plan_json_sha256": hashlib.sha256(plan_json.encode("utf-8")).hexdigest(), "vendor_call_made": False}
    Path(args.out).write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    Path(args.tfvars).write_text(json.dumps({"approved_performance_plan": plan_json}) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in receipt.items() if k != "plan"}, indent=1))
    print(json.dumps({k: plan[k] for k in ("account_id", "start", "end", "expires_at", "mapping_revision")}, indent=1))
    print("SEARCH FOR (terminal only):", names.get(account))
    return 0


if __name__ == "__main__":
    sys.exit(main())
