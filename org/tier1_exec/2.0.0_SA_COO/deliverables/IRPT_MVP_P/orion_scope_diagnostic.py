#!/usr/bin/env python3
"""ONE diagnostic replay of the Orion Scope request the adapter sent at 03:20:31Z for plan 01209afb (which failed
`OrionRequestFailed: provider request failed: HTTPError` with no status logged). Egress: CTO 101098 (Andrew-direct
~03:0xZ "egress is permitted for API calls"), ledgered.

    python orion_scope_diagnostic.py --mapping-as-of <YYYY-MM-DD> --out <receipt.json>

Rebuilds the body exactly as the plan did (orion_selected.requests_for over the same mapping) and REFUSES to send
unless its digest equals the plan's requests_sha256 -- so the replay is the same request, not a new one. Sends it
once with the estate session token (by name, never printed) and records the HTTP status, the response headers minus
cookies, and the body. Prints no credential.
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

ROOT = Path(__file__).resolve().parents[5]
IR = ROOT / "infra/aws/lambda/investor-reporting"
for p in (ROOT / "lib", IR / "_ids", IR / "reports", IR / "performance",
          ROOT / "infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily"):
    sys.path.insert(0, str(p))

import boto3  # noqa: E402

import orion_account_mapping  # noqa: E402
import orion_live  # noqa: E402
import orion_selected  # noqa: E402
import tenants  # noqa: E402
from currency_authority import bind_report_currency  # noqa: E402
from repository import digest  # noqa: E402

PLAN = Path(__file__).with_name("INF_ONE_USE_PLAN_20260925b.json")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--mapping-as-of", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    plan = json.loads(PLAN.read_text(encoding="utf-8"))["plan"]
    firm = tenants._CANONICAL_INF
    sys.path.insert(0, str(Path(__file__).parent))
    from inf_one_use_plan import routed_bucket
    s3 = boto3.client("s3", region_name="us-east-1")
    load = orion_account_mapping.make_inf_mapping_loader(s3, bucket=routed_bucket(firm), as_of=args.mapping_as_of)
    mapping = copy.deepcopy(load(firm, plan["account_id"]))
    mapping.update(bind_report_currency(firm, mapping.get("currency")))
    requests = orion_selected.requests_for(mapping, plan["account_id"], plan["start"], plan["end"])
    got = digest(requests)
    print("requests digest %s ; plan %s ; %s" % (got[:16], plan["requests_sha256"][:16],
                                                 "EQUAL" if got == plan["requests_sha256"] else "DIFFERENT"))
    if got != plan["requests_sha256"]:
        raise SystemExit("STOP: not the planned request")
    token = orion_live.orion_session_jwt()
    route = tenants.route_for("fir_b6b200b4395e94aaa604d5fa")  # inflection opaque id (selection-create reply 03:20Z)
    body = json.dumps(requests["scope"], allow_nan=False).encode()
    req = urllib.request.Request(route.url("scope"), data=body, method="POST")
    req.add_header("Accept", "application/json")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", "Session " + token)
    at = dt.datetime.now(dt.timezone.utc).isoformat()
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            status, headers, raw = r.status, dict(r.headers), r.read(4_000_000)
    except urllib.error.HTTPError as e:
        status, headers, raw = e.code, dict(e.headers or {}), e.read(200_000)
    text = raw.decode("utf-8", "replace").replace(token, "<redacted>")
    headers = {k: v for k, v in headers.items() if k.lower() not in ("set-cookie", "authorization")}
    receipt = {"at": at, "url": route.url("scope"), "requests_sha256": got, "status": status, "headers": headers,
               "body_sha256": hashlib.sha256(raw).hexdigest(), "body": text[:20000],
               "egress_ref": "CTO 101098 (Andrew-direct ~03:0xZ egress permitted for API calls), ledgered"}
    Path(args.out).write_text(json.dumps(receipt, indent=1, sort_keys=True), encoding="utf-8", newline="\n")
    print("HTTP %s ; body %d bytes ; first 300: %s" % (status, len(raw), text[:300].replace("\n", " ")))


if __name__ == "__main__":
    main()
