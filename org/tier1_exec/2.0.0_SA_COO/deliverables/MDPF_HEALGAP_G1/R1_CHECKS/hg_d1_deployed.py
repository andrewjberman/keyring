"""MDPF_HEALGAP round 1, deploy order HG-d-1. Read-only AWS (lambda:GetFunction,
lambda:GetFunctionEventInvokeConfig, events:DescribeRule, events:ListTargetsByRule).

  --code      criterion HG1-d1-AC1: the live cot-rebalancer-runner CodeSha256 equals the HG-t-1 build.
              Last line: DEPLOYED-OK or DEPLOYED-BAD <reason>.
  --unchanged criterion HG1-d1-AC2: the deploy moved code only -- retry/age/on_success, the 06:00Z rule and its
              input are what they were at the cut, and cot-bronze-complete still has one target (no re-attempt).
              Last line: UNCHANGED-OK or UNCHANGED-BAD <reason>.
"""
from __future__ import annotations

import json
import sys

import boto3

REGION = "us-east-1"
FN = "cot-rebalancer-runner"
WANT_SHA = "QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk="
SILVER = "opal-assets-silver-blackdiamond"


def code() -> int:
    got = boto3.client("lambda", region_name=REGION).get_function(FunctionName=FN)["Configuration"]
    if got["CodeSha256"] != WANT_SHA:
        print(f"DEPLOYED-BAD CodeSha256={got['CodeSha256']} want={WANT_SHA} LastModified={got['LastModified']}")
        return 1
    print(f"DEPLOYED-OK CodeSha256={WANT_SHA} LastModified={got['LastModified']}")
    return 0


def unchanged() -> int:
    lam = boto3.client("lambda", region_name=REGION)
    ev = boto3.client("events", region_name=REGION)
    bad = []
    cfg = lam.get_function_event_invoke_config(FunctionName=FN)
    dest = ((cfg.get("DestinationConfig") or {}).get("OnSuccess") or {}).get("Destination", "")
    if cfg.get("MaximumRetryAttempts") != 2 or cfg.get("MaximumEventAgeInSeconds") != 21600 or not dest.endswith(":" + SILVER):
        bad.append(f"invoke-config retry={cfg.get('MaximumRetryAttempts')} age={cfg.get('MaximumEventAgeInSeconds')} dest={dest}")
    rule = ev.describe_rule(Name=FN + "-daily")
    if rule.get("State") != "ENABLED" or rule.get("ScheduleExpression") != "cron(0 6 * * ? *)":
        bad.append(f"daily rule state={rule.get('State')} expr={rule.get('ScheduleExpression')}")
    tg = ev.list_targets_by_rule(Rule=FN + "-daily")["Targets"]
    if len(tg) != 1 or json.loads(tg[0].get("Input") or "{}") != {"mode": "pull"}:
        bad.append("daily targets=" + json.dumps([t.get("Input") for t in tg]))
    bc = ev.list_targets_by_rule(Rule="cot-bronze-complete")["Targets"]
    if len(bc) != 1 or any(FN in t["Arn"] for t in bc):
        bad.append("cot-bronze-complete targets=" + json.dumps([t["Id"] for t in bc]))
    if bad:
        print("UNCHANGED-BAD " + "; ".join(bad))
        return 1
    print("UNCHANGED-OK retry=2 age=21600 on_success=" + SILVER + " daily=cron(0 6 * * ? *) input=pull bronze-complete-targets=1")
    return 0


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--code":
        sys.exit(code())
    if arg == "--unchanged":
        sys.exit(unchanged())
    print("USAGE: hg_d1_deployed.py --code | --unchanged")
    sys.exit(2)
