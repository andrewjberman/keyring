"""MDPF_HEALGAP round 1, the one real run of FWD-1 (order HG-d3). Read-only AWS (s3:ListBucket on
opal-data-assets, s3:GetObject on the stamp, events:ListTargetsByRule, logs:FilterLogEvents).

  --failed DATE    HG1-d3-AC1: the morning pull of DATE failed as induced: the runner's log between 06:00Z and 06:30Z
                   of DATE carries the INDUCED auth-lapse line, and no bronze key of DATE was written before 11:00Z.
                   Last line: FAILED-OK or FAILED-BAD <reason>.
  --healed DATE    HG1-d3-AC2: DATE healed the same day with nobody acting: the complete-stamp for DATE exists, was
                   written after 11:00Z of DATE, and names all three feeds with model_detail count > 0, and each
                   feed has non-empty keys under bronze/<feed>/DATE/.
                   Last line: HEALED-OK or HEALED-BAD <reason>.
  --restored       HG1-d3-AC3: the 06:00Z rule's single target is back to input {"mode":"pull"}.
                   Last line: RESTORED-OK or RESTORED-BAD <reason>.
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


def _ms(date: str, hh: int, mm: int = 0) -> int:
    d = datetime.strptime(date, "%Y-%m-%d").replace(hour=hh, minute=mm, tzinfo=timezone.utc)
    return int(d.timestamp() * 1000)


def _keys(s3, prefix: str) -> list:
    out = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=prefix):
        out.extend(o for o in page.get("Contents", []) if o.get("Size", 0) > 0)
    return out


def failed(date: str) -> int:
    logs = boto3.client("logs", region_name=REGION)
    ev = logs.filter_log_events(logGroupName="/aws/lambda/" + FN, startTime=_ms(date, 6),
                                endTime=_ms(date, 6, 30), filterPattern='"INDUCED auth-lapse"')
    n = len(ev.get("events", []))
    if n == 0:
        print(f"FAILED-BAD no INDUCED auth-lapse line in the runner log {date} 06:00-06:30Z")
        return 1
    s3 = boto3.client("s3", region_name=REGION)
    cutoff = datetime.strptime(date, "%Y-%m-%d").replace(hour=11, tzinfo=timezone.utc)
    early = [o["Key"] for f in FEEDS for o in _keys(s3, f"{PFX}bronze/{f}/{date}/") if o["LastModified"] < cutoff]
    if early:
        print(f"FAILED-BAD {len(early)} bronze key(s) of {date} written before 11:00Z, e.g. {early[0]}")
        return 1
    print(f"FAILED-OK induced lines={n} bronze keys before 11:00Z=0 date={date}")
    return 0


def healed(date: str) -> int:
    s3 = boto3.client("s3", region_name=REGION)
    stamp_key = f"{PFX}meta/{date}-complete.json"
    listed = [o for o in _keys(s3, stamp_key) if o["Key"] == stamp_key]
    if len(listed) != 1:
        print(f"HEALED-BAD no complete-stamp {stamp_key}")
        return 1
    cutoff = datetime.strptime(date, "%Y-%m-%d").replace(hour=11, tzinfo=timezone.utc)
    end = datetime.strptime(date, "%Y-%m-%d").replace(hour=23, minute=59, tzinfo=timezone.utc)
    if not (cutoff <= listed[0]["LastModified"] <= end):
        print(f"HEALED-BAD stamp LastModified {listed[0]['LastModified'].isoformat()} outside {date} 11:00Z-23:59Z")
        return 1
    stamp = json.loads(s3.get_object(Bucket=BUCKET, Key=stamp_key)["Body"].read())
    types = stamp.get("types") or {}
    if set(types) != set(FEEDS) or int((types.get("rebalancer_model_detail") or {}).get("count") or 0) <= 0:
        print("HEALED-BAD stamp types=" + json.dumps(types)[:300])
        return 1
    counts = {f: len(_keys(s3, f"{PFX}bronze/{f}/{date}/")) for f in FEEDS}
    if min(counts.values()) == 0:
        print("HEALED-BAD empty feed: " + json.dumps(counts))
        return 1
    print(f"HEALED-OK date={date} stamp_at={listed[0]['LastModified'].isoformat()} keys={json.dumps(counts)}")
    return 0


def restored() -> int:
    tg = boto3.client("events", region_name=REGION).list_targets_by_rule(Rule=FN + "-daily")["Targets"]
    if len(tg) != 1 or json.loads(tg[0].get("Input") or "{}") != {"mode": "pull"}:
        print("RESTORED-BAD daily targets=" + json.dumps([t.get("Input") for t in tg]))
        return 1
    print('RESTORED-OK daily target input={"mode":"pull"}')
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--failed"] and len(a) == 2:
        sys.exit(failed(a[1]))
    if a[:1] == ["--healed"] and len(a) == 2:
        sys.exit(healed(a[1]))
    if a == ["--restored"]:
        sys.exit(restored())
    print("USAGE: hg_fwd1_exercise.py --failed YYYY-MM-DD | --healed YYYY-MM-DD | --restored")
    sys.exit(2)
