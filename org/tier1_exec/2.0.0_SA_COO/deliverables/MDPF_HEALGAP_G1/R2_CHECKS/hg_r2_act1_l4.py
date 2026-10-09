"""MDPF_HEALGAP round 2, drain act 1 leg L4: the first scheduled fire under the HG-t-3 runner code. Read-only AWS
(s3:ListBucket/GetObject on opal-data-assets and opal-data-cot, lambda:GetFunctionEventInvokeConfig, logs:FilterLogEvents).

  --date DATE   Ledger healgap-r2-act1-runner-code-20261008 leg L4 proof_required, one line per part:
                  RESULT     meta/DATE-result.json exists, verdict COMPLETE, all three feeds status arrived
                  STAMP      meta/DATE-complete.json exists and names all three feeds, model_detail count > 0
                  SILVER     the runner's on_success destination logged at least one event between 06:00Z and 08:00Z of DATE
                  SATELLITES platinum/satellites/registry.json in opal-data-cot reads as_of DATE
                Last line: L4-OK date=DATE or L4-BAD <the parts that failed>.

Negative arm: --date 2026-10-08 must read L4-BAD (that morning ran the pre-HG-t-3 code and was the induced-failure day;
no result object exists for it).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone

import boto3

REGION = "us-east-1"
BUCKET = "opal-data-assets"
PFX = "blackdiamond/cottonwood/"
FEEDS = ("rebalancer_models", "rebalancer_accounts", "rebalancer_model_detail")
FN = "cot-rebalancer-runner"
SAT_BUCKET = "opal-data-cot"
SAT_KEY = "platinum/satellites/registry.json"


def _ms(date: str, hh: int) -> int:
    return int(datetime.strptime(date, "%Y-%m-%d").replace(hour=hh, tzinfo=timezone.utc).timestamp() * 1000)


def _get_json(s3, bucket: str, key: str):
    try:
        return json.loads(s3.get_object(Bucket=bucket, Key=key)["Body"].read())
    except s3.exceptions.NoSuchKey:
        return None


def check(date: str) -> int:
    s3 = boto3.client("s3", region_name=REGION)
    bad = []

    res = _get_json(s3, BUCKET, f"{PFX}meta/{date}-result.json")
    if res is None:
        bad.append("RESULT absent")
        print(f"RESULT     absent: {PFX}meta/{date}-result.json")
    else:
        feeds = res.get("feeds") or {}
        st = {f: (feeds.get(f) or {}).get("status") for f in FEEDS}
        ok = res.get("verdict") == "COMPLETE" and all(v == "arrived" for v in st.values())
        print(f"RESULT     verdict={res.get('verdict')} feeds={json.dumps(st)}")
        if not ok:
            bad.append("RESULT not COMPLETE/arrived")

    stamp = _get_json(s3, BUCKET, f"{PFX}meta/{date}-complete.json")
    if stamp is None:
        bad.append("STAMP absent")
        print(f"STAMP      absent: {PFX}meta/{date}-complete.json")
    else:
        types = stamp.get("types") or {}
        md = int((types.get("rebalancer_model_detail") or {}).get("count") or 0)
        print(f"STAMP      types={sorted(types)} model_detail_count={md}")
        if set(types) != set(FEEDS) or md <= 0:
            bad.append("STAMP incomplete")

    lam = boto3.client("lambda", region_name=REGION)
    dest = (((lam.get_function_event_invoke_config(FunctionName=FN).get("DestinationConfig") or {})
             .get("OnSuccess") or {}).get("Destination") or "")
    silver = dest.rsplit(":", 1)[-1] if dest else ""
    if not silver:
        bad.append("SILVER no on_success destination")
        print("SILVER     no on_success destination on the runner")
    else:
        logs = boto3.client("logs", region_name=REGION)
        ev = logs.filter_log_events(logGroupName="/aws/lambda/" + silver, startTime=_ms(date, 6),
                                    endTime=_ms(date, 8), limit=1).get("events", [])
        first = datetime.fromtimestamp(ev[0]["timestamp"] / 1000, tz=timezone.utc).isoformat() if ev else None
        print(f"SILVER     destination={silver} first_event_06_08Z={first}")
        if not ev:
            bad.append("SILVER no event 06:00-08:00Z")

    sat = _get_json(s3, SAT_BUCKET, SAT_KEY)
    as_of = (sat or {}).get("as_of")
    print(f"SATELLITES {SAT_BUCKET}/{SAT_KEY} as_of={as_of}")
    if as_of != date:
        bad.append(f"SATELLITES as_of {as_of}")

    print(f"L4-OK date={date}" if not bad else f"L4-BAD date={date} " + "; ".join(bad))
    return 0 if not bad else 1


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "--date":
        print(__doc__)
        sys.exit(2)
    sys.exit(check(sys.argv[2]))
