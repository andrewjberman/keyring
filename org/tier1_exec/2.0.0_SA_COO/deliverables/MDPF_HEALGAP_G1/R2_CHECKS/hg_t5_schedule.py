"""MDPF_HEALGAP round 2, HG-t-5 (FWD-5) criterion AC1: the morning pull fires after the login refresh it depends on, in
both summer and winter time, and still leaves the 13:30Z gold floor room.

Reads the runner's daily `schedule_expression` (UTC cron) from `cot_rebalancer_runner.tf` and the live session schedule
`cot-bd-session-daily-et` (EventBridge Scheduler, cron in America/New_York). For one summer date and one winter date it
converts the session fire to UTC and requires:
  - pull fire >= session fire + 10 min (the session chain wrote its sentinel ~2 min after its fire, 10-01..10-08);
  - pull fire <= 13:30Z - 30 min (the gold floor run reads silver at 13:30Z).
SCHEDULE-OK with both margins printed; else SCHEDULE-BAD <reason>. Reads AWS (scheduler:GetSchedule) read-only.
"""
from __future__ import annotations

import os
import re
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import boto3

TF = os.path.join("infra", "aws", "terraform", "opal-assets", "cot_rebalancer_runner.tf")
DATES = ("2026-07-15", "2026-01-15")  # summer (EDT), winter (EST)


def _cron_hm(expr: str) -> tuple[int, int] | None:
    m = re.match(r"cron\((\d+) (\d+) \* \* \? \*\)$", expr.strip())
    return (int(m.group(2)), int(m.group(1))) if m else None


def main() -> int:
    with open(TF, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r'resource\s+"aws_cloudwatch_event_rule"\s+"cot_rebalancer_runner_daily"\s*\{(.*?)\n\}', text, re.S)
    if not m:
        print("SCHEDULE-BAD rule cot_rebalancer_runner_daily not found in " + TF)
        return 1
    s = re.search(r'schedule_expression\s*=\s*"([^"]+)"', m.group(1))
    pull = _cron_hm(s.group(1)) if s else None
    if not pull:
        print("SCHEDULE-BAD pull schedule %r is not a daily cron(M H * * ? *)" % (s.group(1) if s else None))
        return 1
    sch = boto3.client("scheduler", region_name="us-east-1").get_schedule(Name="cot-bd-session-daily-et")
    sess = _cron_hm(sch["ScheduleExpression"])
    tz = ZoneInfo(sch.get("ScheduleExpressionTimezone") or "UTC")
    if not sess:
        print("SCHEDULE-BAD session schedule %r not a daily cron" % sch["ScheduleExpression"])
        return 1
    bad = []
    for d in DATES:
        y, mo, dd = (int(x) for x in d.split("-"))
        s_utc = datetime(y, mo, dd, sess[0], sess[1], tzinfo=tz).astimezone(timezone.utc)
        p_utc = datetime(y, mo, dd, pull[0], pull[1], tzinfo=timezone.utc)
        floor = datetime(y, mo, dd, 13, 30, tzinfo=timezone.utc)
        after = (p_utc - s_utc) / timedelta(minutes=1)
        room = (floor - p_utc) / timedelta(minutes=1)
        print("%s session %s pull %s: after-session %+d min, before-floor %+d min" % (
            d, s_utc.strftime("%H:%MZ"), p_utc.strftime("%H:%MZ"), after, room))
        if after < 10:
            bad.append("%s pull only %+d min after session" % (d, after))
        if room < 30:
            bad.append("%s pull only %+d min before the 13:30Z floor" % (d, room))
    if bad:
        print("SCHEDULE-BAD " + "; ".join(bad))
        return 1
    print("SCHEDULE-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
