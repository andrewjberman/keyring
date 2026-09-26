#!/usr/bin/env python3
"""Row IRPT_BCKEND-S143 fix proof: the household-scoped Orion request for ONE account, end to end through the
adapter's own code, with one real Orion call (egress CTO 101098, ledgered).

    python orion_household_scope_proof.py --tree <backend worktree> --out <receipt.json>

Loads the mapping with the tree's orion_account_mapping (which now refuses an account sharing its household),
builds the body with the tree's orion_selected.requests_for, sends it ONCE with the estate session token (by name,
never printed), and hands the real reply to orion_selected.calculate through a one-reply transport -- so the parse,
the exact Account-group identity check and the contract validation all run on Orion's actual answer. Records the
status, the report's dates and return, and hashes; never a credential or the raw body.
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
PLAN = HERE / "INF_ONE_USE_PLAN_20260925b.json"
INF_OPAQUE = "fir_b6b200b4395e94aaa604d5fa"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tree", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--mapping-as-of", default="2026-09-23")
    ap.add_argument("--end", default="2026-09-25")
    args = ap.parse_args(argv)
    tree = Path(args.tree).resolve()
    ir = tree / "infra/aws/lambda/investor-reporting"
    for p in (tree / "lib", ir / "_ids", ir / "reports", ir / "performance",
              tree / "infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily", HERE):
        sys.path.insert(0, str(p))
    import boto3
    import orion_account_mapping
    import orion_live
    import orion_selected
    import tenants
    from currency_authority import bind_report_currency
    from inf_one_use_plan import routed_bucket

    plan = json.loads(PLAN.read_text(encoding="utf-8"))["plan"]
    account, start, end = plan["account_id"], plan["start"], args.end
    firm = tenants._CANONICAL_INF
    load = orion_account_mapping.make_inf_mapping_loader(boto3.client("s3", region_name="us-east-1"),
                                                         bucket=routed_bucket(firm), as_of=args.mapping_as_of)
    mapping = copy.deepcopy(load(firm, account))
    mapping.update(bind_report_currency(firm, mapping.get("currency")))
    print("mapping: orion account %s household %s" % (mapping["vendor_account_id"], mapping["vendor_household_id"]))
    token = orion_live.orion_session_jwt()
    sent = []

    def request(route, url, body, label=None):
        if sent:
            raise RuntimeError("one call only")
        sent.append(route)
        req = urllib.request.Request(url, data=json.dumps(body, allow_nan=False).encode(), method="POST")
        for k, v in (("Accept", "application/json"), ("Content-Type", "application/json"),
                     ("Authorization", "Session " + token)):
            req.add_header(k, v)
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                status, raw = r.status, r.read(8_000_000)
        except urllib.error.HTTPError as e:
            status, raw = e.code, e.read(200_000)
        print("orion HTTP %d, %d bytes" % (status, len(raw)))
        return SimpleNamespace(ok=status == 200, status=status, raw_body=raw, response_bytes=len(raw),
                               source_response_sha256=hashlib.sha256(raw).hexdigest())

    scope = {"verified_request_firm_id": INF_OPAQUE, "permitted_account_set": [account],
             "resolved_scope": {"scope_ids": [account]}}
    at = dt.datetime.now(dt.timezone.utc).isoformat()
    receipt = {"at": at, "account_id": account, "orion_account": mapping["vendor_account_id"],
               "orion_household": mapping["vendor_household_id"], "requested": [start, end],
               "egress_ref": "CTO 101098, ledgered irpt-orion-household-scope-proof-20260926"}
    try:
        out = orion_selected.calculate(scope, mapping, start, end, SimpleNamespace(request=request))
        report = out["report"]
        receipt.update({"outcome": "REPORT", "contract_validated": out["contract_validated"],
                        "dates": report["dates"], "account_detail": report["returns"]["account_detail"],
                        "series_points": len(report["returns"].get("daily_cumulative_series") or []),
                        "provider": report["lineage"].get("provider"),
                        "report_sha256": hashlib.sha256(json.dumps(report, sort_keys=True).encode()).hexdigest()})
    except Exception as exc:  # the refusal IS the finding
        receipt.update({"outcome": "REFUSED", "error": "%s: %s" % (type(exc).__name__, exc)})
    Path(args.out).write_text(json.dumps(receipt, indent=1, sort_keys=True), encoding="utf-8", newline="\n")
    print(json.dumps({k: receipt[k] for k in receipt if k not in ("egress_ref",)})[:900])


if __name__ == "__main__":
    main()
