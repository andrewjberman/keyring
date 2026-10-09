"""MDPF_HEALGAP round 2, drain act 3 (2026-10-10): an induced PARTIAL day and its same-day repair (FWD-2, FWD-3; ruling
R2-4, half NEVER_WIDEN_HALF_REQUEST_HEALGAP_R2_ACT3_INDUCED_PARTIAL_AND_REPAIR_20261008.md). Read-only AWS
(s3:ListBucket/GetObject on opal-data-assets, events:ListTargetsByRule). Writes only the local snapshot file named.

  --partial DATE         FWD-2: meta/DATE-result.json verdict PARTIAL; rebalancer_accounts status missing;
                         rebalancer_models and rebalancer_model_detail arrived; no meta/DATE-complete.json.
                         Last line: PARTIAL-OK or PARTIAL-BAD <reason>.
  --keys DATE OUT.json   Snapshot {key: [size, etag]} for the two present feeds under bronze/<feed>/DATE/ (R2-2 before/after).
                         Last line: KEYS-OK n=<count> out=<path>.
  --diff BEFORE AFTER    R2-2: compare two snapshots; a key added, removed, or with a changed size or etag is printed.
                         Last line: DIFF-NONE or DIFF-FOUND n=<count> (ETag changes are expected when a re-land
                         rewrites the same day's state; the half asks for any difference beyond LastModified to be reported).
  --repaired DATE        FWD-3: meta/DATE-result.json verdict COMPLETE, all three feeds arrived; the stamp exists and names all
                         three feeds; rebalancer_accounts healed_at is non-null (R2-1 live since 2026-10-09; C5b of
                         ADHOC.healgap-r2-1).
                         Last line: REPAIRED-OK or REPAIRED-BAD <reason>.
  --restored             The daily rule's single target input reads {"mode":"pull"}.
                         Last line: RESTORED-OK or RESTORED-BAD <input>.
"""
from __future__ import annotations

import json
import sys

import boto3

REGION = "us-east-1"
BUCKET = "opal-data-assets"
PFX = "blackdiamond/cottonwood/"
FEEDS = ("rebalancer_models", "rebalancer_accounts", "rebalancer_model_detail")
DROPPED = "rebalancer_accounts"
PRESENT = ("rebalancer_models", "rebalancer_model_detail")
RULE = "cot-rebalancer-runner-daily"


def _s3():
    return boto3.client("s3", region_name=REGION)


def _get_json(s3, key: str):
    try:
        return json.loads(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read())
    except s3.exceptions.NoSuchKey:
        return None


def _status(res: dict) -> dict:
    feeds = res.get("feeds") or {}
    return {f: (feeds.get(f) or {}).get("status") for f in FEEDS}


def partial(date: str) -> int:
    s3 = _s3()
    res = _get_json(s3, f"{PFX}meta/{date}-result.json")
    if res is None:
        print(f"PARTIAL-BAD no result object meta/{date}-result.json")
        return 1
    st = _status(res)
    stamp = _get_json(s3, f"{PFX}meta/{date}-complete.json")
    print(f"result verdict={res.get('verdict')} feeds={json.dumps(st)} stamp={'present' if stamp else 'absent'}")
    if res.get("verdict") != "PARTIAL" or st[DROPPED] != "missing" or any(st[f] != "arrived" for f in PRESENT):
        print("PARTIAL-BAD result does not read PARTIAL with only rebalancer_accounts missing")
        return 1
    if stamp is not None:
        print("PARTIAL-BAD a complete-stamp exists for a PARTIAL day")
        return 1
    print(f"PARTIAL-OK date={date}")
    return 0


def keys(date: str, out: str) -> int:
    s3 = _s3()
    snap = {}
    for f in PRESENT:
        for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=f"{PFX}bronze/{f}/{date}/"):
            for o in page.get("Contents", []):
                snap[o["Key"]] = [o["Size"], o["ETag"]]
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(snap, fh, indent=1, sort_keys=True)
    print(f"KEYS-OK n={len(snap)} out={out}")
    return 0


def diff(before: str, after: str) -> int:
    with open(before, encoding="utf-8") as fh:
        a = json.load(fh)
    with open(after, encoding="utf-8") as fh:
        b = json.load(fh)
    found = []
    for k in sorted(set(a) | set(b)):
        if k not in b:
            found.append(f"REMOVED {k}")
        elif k not in a:
            found.append(f"ADDED {k}")
        elif a[k] != b[k]:
            found.append(f"CHANGED {k} size {a[k][0]}->{b[k][0]} etag {a[k][1]}->{b[k][1]}")
    for line in found:
        print(line)
    print(f"denominator before={len(a)} after={len(b)}")
    print("DIFF-NONE" if not found else f"DIFF-FOUND n={len(found)}")
    return 0


def repaired(date: str) -> int:
    s3 = _s3()
    res = _get_json(s3, f"{PFX}meta/{date}-result.json")
    if res is None:
        print(f"REPAIRED-BAD no result object meta/{date}-result.json")
        return 1
    st = _status(res)
    stamp = _get_json(s3, f"{PFX}meta/{date}-complete.json")
    healed = ((res.get("feeds") or {}).get(DROPPED) or {}).get("healed_at")
    print(f"result verdict={res.get('verdict')} feeds={json.dumps(st)} accounts.healed_at={healed}")
    if res.get("verdict") != "COMPLETE" or any(v != "arrived" for v in st.values()):
        print("REPAIRED-BAD result is not COMPLETE with every feed arrived")
        return 1
    if healed is None:
        # R2-1 landed 2026-10-09 07:5xZ (ReadOwnRunResult): the repair run must now carry healed_at. This is the EXERCISED
        # allow arm of ADHOC.healgap-r2-1 criterion C5b; a null here means the grant did not reach the runner.
        print("REPAIRED-BAD rebalancer_accounts.healed_at is null (R2-1 GetObject not exercised)")
        return 1
    types = (stamp or {}).get("types") or {}
    if set(types) != set(FEEDS):
        print(f"REPAIRED-BAD stamp missing or incomplete: types={sorted(types)}")
        return 1
    print(f"REPAIRED-OK date={date}")
    return 0


def restored() -> int:
    ev = boto3.client("events", region_name=REGION)
    t = ev.list_targets_by_rule(Rule=RULE).get("Targets", [])
    inputs = [x.get("Input") for x in t]
    if len(t) == 1 and json.loads(inputs[0] or "{}") == {"mode": "pull"}:
        print('RESTORED-OK input={"mode":"pull"}')
        return 0
    print(f"RESTORED-BAD targets={len(t)} inputs={inputs}")
    return 1


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--partial"] and len(a) == 2:
        sys.exit(partial(a[1]))
    if a[:1] == ["--keys"] and len(a) == 3:
        sys.exit(keys(a[1], a[2]))
    if a[:1] == ["--diff"] and len(a) == 3:
        sys.exit(diff(a[1], a[2]))
    if a[:1] == ["--repaired"] and len(a) == 2:
        sys.exit(repaired(a[1]))
    if a == ["--restored"]:
        sys.exit(restored())
    print(__doc__)
    sys.exit(2)
