"""MDPF_HEALGAP round 1, criterion HG1-t2-AC2: the seam against the REAL neighbour. The rule the new
Terraform targets is live and ENABLED, and its live event pattern matches the newest real
`_BRONZE_COMPLETE.json` sentinel in opal-data-cot (positive arm) and refuses the same event with a
non-sentinel key (negative arm). Read-only AWS (events:DescribeRule, s3:ListBucket); no invoke, no
vendor call. events:TestEventPattern is denied to the dell1 agent user (measured 2026-10-07), so the LIVE
pattern is evaluated here: exact-value lists and the prefix/suffix operators; any other operator fails
closed (SEAM-BAD unsupported-operator), never silently matches.

Last line: SEAM-OK <detail> or SEAM-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone

import boto3

TF = os.path.join("infra", "aws", "terraform", "opal-assets", "cot_rebalancer_reattempt.tf")
REGION = "us-east-1"


class Unsupported(Exception):
    pass


def _event(bucket: str, key: str) -> dict:
    return {"source": "aws.s3", "detail-type": "Object Created",
            "detail": {"bucket": {"name": bucket}, "object": {"key": key}}}


def _match(pattern, event) -> bool:
    for field, want in pattern.items():
        if field not in event:
            return False
        have = event[field]
        if isinstance(want, dict):
            if not isinstance(have, dict) or not _match(want, have):
                return False
            continue
        ok = False
        for w in want:
            if isinstance(w, dict):
                if set(w) - {"prefix", "suffix"}:
                    raise Unsupported(json.dumps(w))
                ok = ok or (isinstance(have, str) and have.startswith(w.get("prefix", ""))
                            and have.endswith(w.get("suffix", "")))
            else:
                ok = ok or have == w
        if not ok:
            return False
    return True


def main() -> int:
    if not os.path.isfile(TF):
        print("SEAM-BAD no file " + TF)
        return 1
    with open(TF, encoding="utf-8") as fh:
        m = re.search(r'rule\s*=\s*"([^"]+)"', fh.read())
    if not m:
        print("SEAM-BAD no rule name in " + TF)
        return 1
    rule = m.group(1)
    ev = boto3.client("events", region_name=REGION)
    d = ev.describe_rule(Name=rule)
    if d.get("State") != "ENABLED":
        print("SEAM-BAD rule {} state={}".format(rule, d.get("State")))
        return 1
    pattern = d["EventPattern"]
    bucket = json.loads(pattern)["detail"]["bucket"]["name"][0]
    s3 = boto3.client("s3", region_name=REGION)
    newest = None
    for back in range(8):
        day = (datetime.now(timezone.utc) - timedelta(days=back)).strftime("%Y-%m-%d")
        for o in s3.list_objects_v2(Bucket=bucket, Prefix=f"bronze/{day}/").get("Contents", []):
            if o["Key"].endswith("_BRONZE_COMPLETE.json"):
                newest = o["Key"]
        if newest:
            break
    if not newest:
        print(f"SEAM-BAD no _BRONZE_COMPLETE.json in {bucket} over the last 8 days")
        return 1
    try:
        pos = _match(json.loads(pattern), _event(bucket, newest))
        neg = _match(json.loads(pattern), _event(bucket, newest.replace("_BRONZE_COMPLETE.json", "other.json")))
    except Unsupported as e:
        print("SEAM-BAD unsupported-operator " + str(e))
        return 1
    if pos is not True or neg is not False:
        print(f"SEAM-BAD rule={rule} pos={pos} neg={neg} key={newest}")
        return 1
    print(f"SEAM-OK rule={rule} state=ENABLED key={newest} pos=True neg=False")
    return 0


if __name__ == "__main__":
    sys.exit(main())
