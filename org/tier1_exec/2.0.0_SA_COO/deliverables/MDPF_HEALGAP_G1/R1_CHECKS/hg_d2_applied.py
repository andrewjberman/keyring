"""MDPF_HEALGAP round 1, deploy order HG-d2. Read-only AWS (events:ListTargetsByRule, lambda:GetPolicy,
lambda:GetFunction, lambda:GetFunctionEventInvokeConfig, events:DescribeRule).

  --wired     criterion HG1-d2-AC1: cot-bronze-complete carries exactly one target invoking cot-rebalancer-runner
              with input {"mode":"pull"}, beside its existing silver-run target, and the runner's resource policy
              admits events.amazonaws.com from that rule.
              Last line: WIRED-OK or WIRED-BAD <reason>.
  --unchanged criterion HG1-d2-AC2: nothing else moved -- the runner's code is the HG-t-1 build, retry/age/on_success,
              the 06:00Z rule and its input are as at the cut.
              Last line: UNCHANGED-OK or UNCHANGED-BAD <reason>.
"""
from __future__ import annotations

import json
import sys

import boto3

REGION = "us-east-1"
FN = "cot-rebalancer-runner"
RULE = "cot-bronze-complete"
WANT_SHA = "QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk="
SILVER = "opal-assets-silver-blackdiamond"


def wired() -> int:
    ev = boto3.client("events", region_name=REGION)
    lam = boto3.client("lambda", region_name=REGION)
    tg = ev.list_targets_by_rule(Rule=RULE)["Targets"]
    runner = [t for t in tg if t["Arn"].endswith(":function:" + FN)]
    others = [t["Id"] for t in tg if t not in runner]
    if len(runner) != 1:
        print(f"WIRED-BAD runner targets on {RULE}={len(runner)} (want 1); all={[t['Id'] for t in tg]}")
        return 1
    if json.loads(runner[0].get("Input") or "{}") != {"mode": "pull"}:
        print("WIRED-BAD runner target input=" + str(runner[0].get("Input")))
        return 1
    if others != ["CotSilverOnBronzeComplete"]:
        print("WIRED-BAD the rule's other targets changed: " + json.dumps(others))
        return 1
    pol = json.loads(lam.get_policy(FunctionName=FN)["Policy"])
    hits = [s for s in pol["Statement"]
            if s.get("Principal", {}).get("Service") == "events.amazonaws.com"
            and json.dumps(s.get("Condition", {})).endswith(f'rule/{RULE}"}}}}')]
    if len(hits) != 1:
        print(f"WIRED-BAD resource-policy statements for rule/{RULE}={len(hits)} (want 1)")
        return 1
    print(f"WIRED-OK target={runner[0]['Id']} input=pull other_targets=CotSilverOnBronzeComplete policy_sid={hits[0]['Sid']}")
    return 0


def unchanged() -> int:
    lam = boto3.client("lambda", region_name=REGION)
    ev = boto3.client("events", region_name=REGION)
    bad = []
    sha = lam.get_function(FunctionName=FN)["Configuration"]["CodeSha256"]
    if sha != WANT_SHA:
        bad.append("CodeSha256=" + sha)
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
    if bad:
        print("UNCHANGED-BAD " + "; ".join(bad))
        return 1
    print("UNCHANGED-OK code=HG-t-1 build retry=2 age=21600 on_success=" + SILVER + " daily=cron(0 6 * * ? *) input=pull")
    return 0


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--wired":
        sys.exit(wired())
    if arg == "--unchanged":
        sys.exit(unchanged())
    print("USAGE: hg_d2_applied.py --wired | --unchanged")
    sys.exit(2)
