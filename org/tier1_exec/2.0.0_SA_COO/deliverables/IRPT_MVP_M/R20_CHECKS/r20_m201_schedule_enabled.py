"""Round 20 (~M) check IBM20-201-AC1: irpt-holdings-snapshot is ENABLED, targets irpt-holdings-refresh-lambda with
no "qa" in its input, and the enable ledger's A1 and V1 legs carry proof.

Run from the repo (or worktree) root. Prints ENABLED or NOT-ENABLED: <reason>.
"""
import json
import os
import sys

import boto3

LEDGER = "org/critical_paths/.open_deploys/irpt-holdings-schedule-enable-m-20260929.json"


def main():
    s = boto3.client("scheduler", region_name="us-east-1").get_schedule(Name="irpt-holdings-snapshot")
    target = s.get("Target") or {}
    payload = json.loads(target.get("Input") or "{}")
    if s.get("State") != "ENABLED":
        print("NOT-ENABLED: State %s" % s.get("State"))
        return 1
    if not target.get("Arn", "").endswith(":function:irpt-holdings-refresh-lambda") or "qa" in payload:
        print("NOT-ENABLED: target %s input %s" % (target.get("Arn"), payload))
        return 1
    if not os.path.exists(LEDGER):
        print("NOT-ENABLED: ledger sentinel %s absent (it stays open until IB-mr-204)" % LEDGER)
        return 1
    with open(LEDGER, encoding="utf-8") as fh:
        legs = {leg["id"]: leg for leg in json.load(fh)["legs"]}
    unproven = [k for k in ("A1", "V1") if not (legs.get(k) or {}).get("proof")]
    if unproven:
        print("NOT-ENABLED: ledger legs without proof %s" % unproven)
        return 1
    print("ENABLED %s %s" % (s.get("ScheduleExpression"), s.get("ScheduleExpressionTimezone")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
