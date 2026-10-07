"""MDPF_HEALGAP TO-HG-d3 restore fallback (owner (2), 2.0.0_SA_COO~G1, at 06:10Z on the exercise date).

Laptop 1.0.0_SA_CTO msg 106484 (relay 0.0.0_AB_MSTR~DELL1 msg 522) names this seat fallback owner (2) for the CTO half's
condition 2: the 06:00Z rule's input back to {"mode":"pull"} between 06:05Z and 06:20Z. Act ONLY if the pre-act read shows
the induce input still live; then re-put THE SAME target (same Id, same Arn) with {"mode":"pull"} -- the order's own second
put-targets -- and read it back.

Prints one of: NOOP-ALREADY-RESTORED, RESTORED-BY-FALLBACK, REFUSED <reason>, FAILED <reason>.
--dry-run reads and reports what it would do, writes nothing.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone

import boto3

REGION = "us-east-1"
RULE = "cot-rebalancer-runner-daily"
WANT = {"mode": "pull"}
INDUCE = {"mode": "pull", "induce": "auth-lapse"}


def main(dry: bool) -> int:
    ev = boto3.client("events", region_name=REGION)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    tg = ev.list_targets_by_rule(Rule=RULE)["Targets"]
    if len(tg) != 1:
        print(f"REFUSED {now} rule {RULE} has {len(tg)} targets (want exactly 1); nothing written")
        return 1
    t = tg[0]
    cur = json.loads(t.get("Input") or "{}")
    print(f"pre-act read {now}: Id={t['Id']} Arn={t['Arn']} Input={json.dumps(cur)}")
    if cur == WANT:
        print(f"NOOP-ALREADY-RESTORED {now}")
        return 0
    if cur != INDUCE:
        print(f"REFUSED {now} input is neither the induce nor the restored form: {json.dumps(cur)}; nothing written")
        return 1
    if dry:
        print(f"DRY-RUN {now} would re-put Id={t['Id']} Arn={t['Arn']} Input={json.dumps(WANT)}")
        return 0
    out = ev.put_targets(Rule=RULE, Targets=[{"Id": t["Id"], "Arn": t["Arn"], "Input": json.dumps(WANT)}])
    if out.get("FailedEntryCount"):
        print(f"FAILED {now} put_targets: {json.dumps(out.get('FailedEntries'))}")
        return 1
    back = ev.list_targets_by_rule(Rule=RULE)["Targets"]
    after = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if len(back) == 1 and json.loads(back[0].get("Input") or "{}") == WANT:
        print(f"RESTORED-BY-FALLBACK put at {now}, read back at {after}: Id={back[0]['Id']} Input={back[0].get('Input')}")
        return 0
    print(f"FAILED {after} read-back: {json.dumps([b.get('Input') for b in back])}")
    return 1


if __name__ == "__main__":
    sys.exit(main("--dry-run" in sys.argv[1:]))
