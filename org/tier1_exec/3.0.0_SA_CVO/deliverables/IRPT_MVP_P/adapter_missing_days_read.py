#!/usr/bin/env python3
"""Read-only run of the DEPLOYED irpt-performance-adapter package's holdings calculation for ONE Inflection account,
2026 year to date (1.0.0_SA_CTO msgs 106081 item 2 and 106097 item 1; ledger irpt-inf-performance-serving-20261002 leg A1).

    python adapter_missing_days_read.py <dir holding the unpacked deployed zip> <dir holding the unpacked irpt-common layer> <out.json>

It imports the package's own modules from the unpacked zip (never the repo's), composes the Inflection holdings source the
way installed.py does, and calls holdings_gold.calculate(). The only S3 calls are the source's own list and get. It writes
no S3 object, no DynamoDB item and no log group; the output is one local JSON file. The account's raw key is not written:
the output carries the opaque account id the package itself computes.
"""
from __future__ import annotations

import json
import os
import sys


def main() -> int:
    pkg, layer, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    # the layer goes LAST: its jsonschema carries a Linux-only native wheel (rpds), so this box's own jsonschema validates
    sys.path.append(os.path.join(layer, "python"))
    for p in (os.path.join(pkg, "_vendor"), os.path.join(pkg, "lib"),
              os.path.join(pkg, "data", "assets", "scripts", "gold", "runners_49f"), pkg):
        sys.path.insert(0, p)
    os.environ.setdefault("IRPT_CONTRACTS_DIR", pkg)
    os.environ.setdefault("IRPT_FIRM_REGISTRY", os.path.join(pkg, "firm_registry.json"))
    os.environ.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    import boto3
    import holdings_gold
    import installed
    import tenants
    import trading_calendar as tc
    from ids import opaque_account

    for name in ("holdings_gold", "installed", "tenants", "trading_calendar"):
        mod = sys.modules[name]
        print("module %s <- %s" % (name, os.path.relpath(mod.__file__, pkg) if mod.__file__.startswith(pkg) else mod.__file__))
    s3 = boto3.client("s3", region_name="us-east-1")
    canonical = tenants._CANONICAL_INF
    source = installed._holdings_source_for(s3, canonical)
    print("source:", source.describe(), "| calendar:", tc.calendar_source())
    available = source.partition_dates()
    end = available[-1]
    import f49_engine
    import parity_period_returns as ppr
    ytd = [w for w in f49_engine.RULED_WINDOWS if str(w).upper() in ("YTD", "YEAR_TO_DATE")]
    if len(ytd) != 1:
        raise SystemExit("no single year-to-date ruled window; RULED_WINDOWS = %r" % (list(f49_engine.RULED_WINDOWS),))
    window = ppr.period_window(ytd[0], end)
    start = window[0].isoformat()
    print("ruled window %s at %s: %s .. %s" % (ytd[0], end, start, window[1].isoformat()))
    # the opaque firm id the boundary binds on: the tenant whose route resolves to the canonical Inflection id
    firm = None
    for cand in tenants.ROUTES:
        try:
            if holdings_gold._canonical_firm_for(cand) == canonical:
                firm = cand
        except Exception:
            pass
    if firm is None:
        raise SystemExit("could not resolve the request firm id for %s; tenants attrs: %s"
                         % (canonical, [a for a in dir(tenants) if not a.startswith("__")]))
    raw = sorted(source.account_keys(end))[0]
    account = opaque_account(canonical, raw)
    scope = {"resolved_scope": {"scope_ids": [account]}, "permitted_account_set": [account],
             "verified_request_firm_id": firm}
    result = holdings_gold.calculate(scope, start, end, source)
    ev = result.get("evidence") or {}
    record = {
        "function": "irpt-performance-adapter", "window": [start, end], "firm": canonical, "opaque_account": account,
        "partitions": {"n": len(available), "first": available[0], "last": available[-1],
                       "in_window": sum(1 for d in available if start <= d <= end)},
        "claim": result.get("claim"),
        "evidence_missing_trading_days": ev.get("missing_trading_days"),
        "absences": result.get("absences"),
        "refusals": result.get("refusals"),
        "evidence_keys": sorted(ev),
    }
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(record, fh, indent=1, sort_keys=True, default=str)
    print(json.dumps({k: record[k] for k in ("window", "partitions", "claim", "evidence_missing_trading_days")}, default=str))
    for a in record["absences"] or []:
        print("ABSENCE:", json.dumps(a, default=str)[:700])
    return 0


if __name__ == "__main__":
    sys.exit(main())
