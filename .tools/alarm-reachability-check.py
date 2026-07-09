#!/usr/bin/env python3
"""alarm-reachability-check -- can each CloudWatch alarm actually reach a human?

CTO ruling 2026-07-09T210607Z (gate APPROVED):

    "No aws_cloudwatch_metric_alarm may reference an alarm_actions topic with zero
     subscriptions, and no alarm may have empty alarm_actions."

    "A detector whose subject cannot be reached should not exist, not merely be
     silent. A zero-subscriber alarm is the purest form of a control that lies:
     it renders green on every dashboard and cannot speak."

WHY (2026-07-09, found by generalizing a single-topic finding)
-------------------------------------------------------------
The client-facing bd 49F AUA freeze -- $1,837,159,865.68 frozen since 07-06 --
was unheard for TWO INDEPENDENT reasons:
  1. its five `bd-served-vintage-stale-*` alarms were LATCHED in ALARM, so they
     could emit no state transition; and
  2. their topic `opal-bd-49f-cookie-alerts` has ZERO SUBSCRIBERS, so even a
     transition publishes into nothing.

Either alone is sufficient to produce silence. **Remediating one produces a green
finding and an unchanged world.** One cause among several is a proxy for the cause.

Estate at first run: 88 metric alarms, 25 (28.4%) unable to reach a human --
16 whose every alarm_action topic is dead, plus 9 with no alarm_actions at all.
`opal-bd-cot-cookie-alerts` (8 alarms) is in the identical condition and has
simply not fired yet.

Bounded then, and the bound is what makes the census usable: an alarm with no
subscribers could still be caught by an EventBridge rule on `CloudWatch Alarm
State Change`. There is none -- 131 rules scanned; the one `aws.cloudwatch` match
is a CloudTrail API-call rule, not an alarm-transition rule. So SNS is the only
notification path, and for these it terminates nowhere.

NODES, NOT EDGES (the correction that produced this tool's counting rule)
------------------------------------------------------------------------
The first census reported 24 -- but that is the count of alarm->dead-topic
REFERENCES. Eight of those alarms ALSO publish to a live topic and therefore CAN
reach a human. "Publishes into a zero-subscriber topic" and "cannot reach a human"
are different sets. **A count of relationships is not a count of things.** This
tool counts ALARMS (nodes) and always prints its denominator and its unit.

LIVE, NOT DECLARED (Rule 22a, in a gate about delivery)
-------------------------------------------------------
It queries live SNS, never the Terraform-declared subscription set. A subscription
can exist in TF and sit at `PendingConfirmation` -- which reads healthy from a plan
and delivers nothing. And a CONFIRMED subscription still may never deliver: an SMS
endpoint in the SNS sandbox against an unverified number fails every time. So:

  E1  no alarm_actions at all                       -> cannot notify, by construction
  E2  every action topic has ZERO subscriptions     -> publish terminates nowhere
  E3  every action topic has only PENDING subs      -> exists != delivers
  W1  action topic has confirmed subs but has NEVER DELIVERED (delivered==0 and
      failed>0 over the window) -> empirically mute; the sandbox/SMS class
  I1  ok_actions / insufficient_data_actions pointing at dead topics

W1 is the clause that catches `opal-infrastructure-alerts` (0 delivered / 37
failed / 14d) and `ec2-long-running-alerts` (0 delivered / 50 failed / 14d) --
both of which have a CONFIRMED subscriber and have never delivered a single
notification. No subscription-state check can find those; only the delivery
metric can.

THIS IS A CENSUS. IT IS NOT A DELETE-LIST. (CTO 2026-07-09T211337Z)
-------------------------------------------------------------------
An earlier ruling -- "each unreachable alarm gets a subscriber or gets deleted" --
was SUSPENDED once the cause was established:

    2026-07-01T02:46:02Z .. 02:47:05Z   Unsubscribe x7   Andrew_Berman, aws-cli, 63s
      bd-allocation-file-missing   ec2-auto-shutdown-alerts   etfs-reports-alerts
      find-insure-budget-alerts    opal-bd-49f-cookie-alerts  opal-bd-cot-cookie-alerts
      opal-critical-surface-alerts
    DeleteTopic: 0.  SetSubscriptionAttributes: 0.

**The sovereign removed those subscriptions deliberately.** They are not a bug and
not a regression. Acting on this tool's output by deleting alarms would have
destroyed two dozen controls Andrew switched off on purpose, and the evidence of
why. A zero-subscriber topic means "this alarm currently reaches nobody" -- it does
NOT tell you whether that is an accident, a decommission, or an oversight. **This
tool reports reachability. It never adjudicates intent.**

And the loop that closes on it: those topics delivered CLEANLY, zero failures,
until 02:46Z on 07-01 -- **email was the working limb.** LD-0233 recorded the email
decommission as safe because "SMS still reaches him." SMS has never delivered once
(sandbox, Pending number, $1 spend limit). The working limb was removed on the
strength of a fallback that has never carried a message. Six days later the five
`bd-served-vintage-stale-*` alarms fired into a topic that could reach nobody, then
latched, so they could not re-notify even if a subscriber returned. The first topic
unsubscribed was `bd-allocation-file-missing` -- named for the exact failure mode
this all produced.

Read-only. Paginates everything (an unpaginated sweep prints a clean bill of
health it never earned). ASCII only.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta, timezone

try:
    import boto3
except ImportError:  # pragma: no cover
    print("ERROR: boto3 not available", file=sys.stderr)
    raise SystemExit(2)


def topic_health(sns, cw, window_days: int) -> dict:
    """arn -> (total_subs, confirmed_subs, delivered, failed). Fully paginated."""
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=window_days)
    out = {}
    for pg in sns.get_paginator("list_topics").paginate():
        for t in pg["Topics"]:
            arn = t["TopicArn"]
            total = confirmed = 0
            for p2 in sns.get_paginator("list_subscriptions_by_topic").paginate(TopicArn=arn):
                for s in p2["Subscriptions"]:
                    total += 1
                    if s["SubscriptionArn"] != "PendingConfirmation":
                        confirmed += 1
            name = arn.rsplit(":", 1)[-1]

            def _m(metric: str) -> float:
                r = cw.get_metric_statistics(
                    Namespace="AWS/SNS", MetricName=metric,
                    Dimensions=[{"Name": "TopicName", "Value": name}],
                    StartTime=start, EndTime=now, Period=86400, Statistics=["Sum"])
                return sum(p["Sum"] for p in r.get("Datapoints", []))

            out[arn] = (total, confirmed, _m("NumberOfNotificationsDelivered"),
                        _m("NumberOfNotificationsFailed"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Can each CloudWatch alarm reach a human?")
    ap.add_argument("--region", default="us-east-1")
    ap.add_argument("--window-days", type=int, default=14)
    ap.add_argument("--strict", action="store_true", help="exit 1 on any E-class finding")
    args = ap.parse_args()

    sns = boto3.client("sns", region_name=args.region)
    cw = boto3.client("cloudwatch", region_name=args.region)

    topics = topic_health(sns, cw, args.window_days)
    alarms = []
    for pg in cw.get_paginator("describe_alarms").paginate(AlarmTypes=["MetricAlarm"]):
        alarms.extend(pg["MetricAlarms"])

    # THE DENOMINATOR, ALWAYS PRINTED. A gate must print the universe it swept.
    print(f"alarm-reachability-check -- {args.region}, delivery window {args.window_days}d")
    print(f"  swept {len(alarms)} metric alarm(s) and {len(topics)} SNS topic(s), fully paginated")
    print()
    print("  topics swept:")
    for arn, (tot, conf, dlv, fail) in sorted(topics.items()):
        name = arn.rsplit(":", 1)[-1]
        never = " NEVER-DELIVERED" if (conf > 0 and dlv == 0 and fail > 0) else ""
        print(f"    {name:<36} subs={tot:<3} confirmed={conf:<3} delivered={dlv:g} failed={fail:g}{never}")
    print()

    e1, e2, e3, w1, i1 = [], [], [], [], []
    never_delivered = {a for a, (t, c, d, f) in topics.items() if c > 0 and d == 0 and f > 0}

    for a in alarms:
        name, state = a["AlarmName"], a["StateValue"]
        acts = a.get("AlarmActions") or []
        if not acts:
            e1.append((name, state))
            continue
        subs = [topics.get(x, (0, 0, 0, 0)) for x in acts]
        if all(s[0] == 0 for s in subs):
            e2.append((name, state))
        elif all(s[1] == 0 for s in subs):
            e3.append((name, state))
        elif all(x in never_delivered for x in acts):
            w1.append((name, state))
        for extra in ("OKActions", "InsufficientDataActions"):
            for arn in (a.get(extra) or []):
                if topics.get(arn, (0, 0, 0, 0))[0] == 0:
                    i1.append((name, extra, arn.rsplit(":", 1)[-1]))

    def emit(rows, code, title):
        if not rows:
            return
        print(f"{code} ({len(rows)} alarms): {title}")
        for r in sorted(rows):
            mark = "  <- currently in ALARM" if len(r) > 1 and r[1] == "ALARM" else ""
            print(f"    {r[1]:<18} {r[0]}{mark}")
        print()

    emit(e1, "E1", "no alarm_actions at all -- cannot notify by construction")
    emit(e2, "E2", "every action topic has ZERO subscriptions -- publish terminates nowhere")
    emit(e3, "E3", "every action topic has only PENDING subscriptions -- exists != delivers")
    emit(w1, "W1", "confirmed subscriber, but the topic has NEVER DELIVERED (empirically mute)")

    if i1:
        print(f"I1 ({len(i1)}): ok/insufficient_data actions pointing at a zero-subscriber topic")
        for n, kind, t in sorted(i1):
            print(f"    {n}  {kind} -> {t}")
        print()

    # R1 -- SUBSCRIBER REGRESSION. A topic with ZERO subscriptions that nonetheless
    # DELIVERED inside the window cannot always have been subscriberless: its
    # subscribers were REMOVED during the window. This rule exists because the
    # contradiction it names (subs=0, delivered=107) falsified a premise of the very
    # census that produced this tool -- `opal-bd-49f-cookie-alerts` delivered cleanly
    # with ZERO failures until 2026-07-02, then went silent. "Never wired" and
    # "un-wired last week" demand opposite remedies: the first says delete the alarm,
    # the second says find out who removed the subscriber and whether it is still doing it.
    #
    # Deleting an alarm because its topic looks dead, when the topic was killed by a
    # regression, destroys the evidence and the control together.
    r1 = [(arn.rsplit(":", 1)[-1], d) for arn, (t, c, d, f) in topics.items() if t == 0 and d > 0]
    if r1:
        print(f"R1 ({len(r1)} topics): SUBSCRIBERS REMOVED -- zero subscriptions now, but DELIVERED")
        print(f"    inside the {args.window_days}d window. They were removed, not absent.")
        print("    Establish WHO removed them before adjudicating. On 2026-07-01T02:46Z the answer")
        print("    was: the sovereign, deliberately, from the CLI, in 63 seconds. Not a regression.")
        for name, d in sorted(r1):
            print(f"    {name:<36} delivered={d:g} in-window, subscriptions=0 now")
        print()
    print("  THIS IS A CENSUS, NOT A DELETE-LIST. It reports reachability; it never adjudicates")
    print("  intent. A zero-subscriber topic may be an accident, a decommission, or an oversight.")
    print()

    unreachable = len(e1) + len(e2) + len(e3)
    print(f"UNREACHABLE ALARMS (nodes, not edges): {unreachable} of {len(alarms)} "
          f"({unreachable / len(alarms) * 100:.1f}%)")
    print(f"  E1 no-action={len(e1)}  E2 dead-topic={len(e2)}  E3 pending-only={len(e3)}")
    print(f"  W1 never-delivered (has a confirmed subscriber): {len(w1)}")
    print()
    print("  Note: an alarm publishing to BOTH a dead and a live topic CAN reach a human and is")
    print("  not counted here. Publishing into a zero-subscriber topic and being unreachable are")
    print("  different sets -- a count of relationships is not a count of things.")

    if args.strict and unreachable:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
