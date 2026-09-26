#!/usr/bin/env python3
"""Row IRPT_BCKEND-S143: which Orion Reporting/Scope `entity` addresses ONE account. Bounded probes under the session
egress permission (CTO 101098), ledgered; each probe is the adapter's own body (orion_selected.requests_for) with only
`entity` / `entityIds` swapped, so a 200 validates the whole body, not a toy.

    python orion_entity_probe.py --out <receipt.json> [--cases 5:381,3:1098,1:1098,2:1098,6:1098]

Case `5:381` is the CONTROL: entity 5 (Household) is the only value a capture pins (HAR 7), and 381 is account 1098's
household in accounts_v2. A 404 on the control says the body, not the entity, is wrong -- stop there.
Records the status, the Orion error text or the top-level keys and the Account-grouping row count; never a credential.
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

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
IR = ROOT / "infra/aws/lambda/investor-reporting"
for p in (ROOT / "lib", IR / "_ids", IR / "reports", IR / "performance",
          ROOT / "infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily", HERE):
    sys.path.insert(0, str(p))

import boto3  # noqa: E402

import orion_account_mapping  # noqa: E402
import orion_live  # noqa: E402
import orion_selected  # noqa: E402
import tenants  # noqa: E402
from currency_authority import bind_report_currency  # noqa: E402
from inf_one_use_plan import routed_bucket  # noqa: E402

PLAN = HERE / "INF_ONE_USE_PLAN_20260925b.json"
INF_OPAQUE = "fir_b6b200b4395e94aaa604d5fa"


def summarize(status, raw):
    text = raw.decode("utf-8", "replace")
    try:
        body = json.loads(text)
    except ValueError:
        return {"text": text[:300]}
    if status != 200:
        return {"error": ((body.get("userException") or {}).get("detail") if isinstance(body, dict) else None)
                or text[:300]}
    out = {"top_keys": sorted(body.keys())[:20] if isinstance(body, dict) else type(body).__name__}
    calcs = body.get("calculations") if isinstance(body, dict) else None
    if isinstance(calcs, list):
        out["calculations"] = [{k: (v if not isinstance(v, (list, dict)) else "%s[%d]" % (type(v).__name__, len(v)))
                                for k, v in c.items()} for c in calcs[:3] if isinstance(c, dict)]
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--cases", default="5:381,3:1098,1:1098,2:1098,6:1098")
    ap.add_argument("--mapping-as-of", default="2026-09-23")
    args = ap.parse_args(argv)
    plan = json.loads(PLAN.read_text(encoding="utf-8"))["plan"]
    firm = tenants._CANONICAL_INF
    s3 = boto3.client("s3", region_name="us-east-1")
    load = orion_account_mapping.make_inf_mapping_loader(s3, bucket=routed_bucket(firm), as_of=args.mapping_as_of)
    mapping = copy.deepcopy(load(firm, plan["account_id"]))
    mapping.update(bind_report_currency(firm, mapping.get("currency")))
    base = orion_selected.requests_for(mapping, plan["account_id"], plan["start"], plan["end"])["scope"]
    token = orion_live.orion_session_jwt()
    url = tenants.route_for(INF_OPAQUE).url("scope")
    results = []
    for case in args.cases.split(","):
        entity, ident = (int(x) for x in case.split(":"))
        body = copy.deepcopy(base)
        body["entity"], body["entityIds"] = entity, [ident]
        req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST")
        for k, v in (("Accept", "application/json"), ("Content-Type", "application/json"),
                     ("Authorization", "Session " + token)):
            req.add_header(k, v)
        at = dt.datetime.now(dt.timezone.utc).isoformat()
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                status, raw = r.status, r.read(8_000_000)
        except urllib.error.HTTPError as e:
            status, raw = e.code, e.read(200_000)
        row = {"at": at, "entity": entity, "entityIds": [ident], "status": status,
               "body_sha256": hashlib.sha256(raw).hexdigest(), "summary": summarize(status, raw)}
        results.append(row)
        print("entity %d ids [%d] -> HTTP %d %s" % (entity, ident, status, json.dumps(row["summary"])[:240]))
        if case == "5:381" and status != 200:
            print("STOP: the control failed -- the body, not the entity, is wrong")
            break
    Path(args.out).write_text(json.dumps({"url": url, "egress_ref": "CTO 101098, ledgered", "results": results},
                                         indent=1), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
