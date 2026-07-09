#!/usr/bin/env python3
"""alarm-latch-sweep -- find CloudWatch alarms that are LATCHED and therefore blind.

CTO standing rule (2026-07-09T192324Z):

    "A detector that cannot change state cannot detect. No alarm may be left
     latched in ALARM on a component that is dormant by design -- return it to
     OK, or scope evaluation to fire only while the component is enabled. A
     latched alarm is a DISABLED CONTROL THAT STILL LOOKS ARMED, which is worse
     than no control, because it consumes the attention a real one would get."

THE MECHANISM
-------------
CloudWatch notifies on STATE TRANSITION, not on state. An alarm already sitting
in ALARM emits nothing when the failure it watches actually occurs -- there is
no transition to fire on. Its RED is indistinguishable from a real incident's
RED, and a real incident produces silence.

Instances surfaced on 2026-07-09 by four agents, none looking for each other's
findings, all found by ACCIDENT:
  * opal-globgrph-parity-drift-stuck-code_heat_ajb_workspace  latched, PINNED @ 1e6
  * opal-globgrph-parity-drift-stuck-code_heat_portal         latched, PINNED @ 1e6
  * cmtque-worker-down                                        latched, NO DATAPOINTS (dormant by design)
  * bd-served-vintage-stale-bd_platinum_* (x5)                latched 67h, PINNED @ 1

Nothing checks for this.

A MECHANISM I ASSERTED AND HAD TO RETRACT (kept, because it shaped the tool)
---------------------------------------------------------------------------
I first told COO/CVO/CTO the parity alarms latched because the producer published
NO datapoint -> missing-data=breaching. That was INFERRED, and it was FALSE.
Source, freshness_alarm/lambda_function.py:159-166, on any read failure:

    "Value": 1e6,  # UNVERIFIABLE reads as maximally-stuck -- fail LOUD, not silent-current

The metric publishes every hour, pinned at 1000000.0. The alarm latches because
1e6 > threshold, not because data is missing. The author's design is BETTER than
the accident I ascribed to it -- they chose to fail loud.

Consequence for this tool: a starved-only check would have called those alarms
healthy and moved on. Hence L4. The pathology is not always "no signal"; it is
often "the SAME signal forever."

WHAT IT REPORTS
---------------
  L1  latched:  in ALARM longer than <hours> (default 24)
  L2  starved:  latched AND the metric published NO datapoint in the window
                -- a dead producer under missing-data=breaching. Cannot be a real
                incident; it is a broken detector.
  L4  pinned:   latched AND every datapoint in the window is the SAME value
                -- a fail-loud sentinel (1e6) or a stuck flag (1.0). Read the value:
                a latched-and-varying alarm may be a genuine sustained incident,
                but a latched-and-pinned one is reporting one unchanging thing.
  L3  insufficient-data for longer than <hours> (a control that never armed)

THE SWEEP MUST NOT ITSELF LATCH
-------------------------------
It reports its own sweep COUNT (--emit-metric puts Opal/AlarmHealth
LatchedAlarmCount). A stuck sweep then shows as a FLAT LINE in a metric, not as
silence -- because "no alerts" and "the alerter died" must not look identical.
That is the same failure one level up, and it is the one this tool would
otherwise reintroduce.

Read-only by default. --emit-metric is the only write, and it writes a metric,
never an alarm state.

Pagination is explicit: describe_alarms truncates. An unpaginated sweep silently
under-reports and prints a confident all-clear (the F-W4-1 apigatewayv2 class,
and the same truncation I hit enumerating secrets earlier today).
ASCII only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys

try:
    import boto3
except ImportError:  # pragma: no cover
    print("ERROR: boto3 not available", file=sys.stderr)
    raise SystemExit(2)


def _utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def describe_all_alarms(cw) -> list:
    """Fully paginated. An unpaginated describe_alarms silently truncates and
    makes this tool print a clean bill of health it never earned."""
    out = []
    paginator = cw.get_paginator("describe_alarms")
    for page in paginator.paginate(AlarmTypes=["MetricAlarm"]):
        out.extend(page.get("MetricAlarms", []))
    return out


def metric_shape(cw, alarm: dict, since: dt.datetime) -> tuple:
    """Return (has_datapoints, pinned_value) for this alarm's metric since <since>.

    has_datapoints: True / False / None (None = undecidable, e.g. math or
    composite alarms with no single metric). 'Unknown' is never silently
    rendered as 'no' -- a could-not-verify is a finding, not a pass.

    pinned_value: the constant value if EVERY datapoint in the window is
    identical, else None.

    WHY pinned_value EXISTS (I got this wrong first, and the tool is the fix):
    I asserted the leg-5-v2 parity alarms latched because the producer published
    NO datapoint -> missing-data=breaching. FALSE. Source
    (freshness_alarm/lambda_function.py:159-166) publishes Value=1e6 on any read
    failure -- "UNVERIFIABLE reads as maximally-stuck -- fail LOUD, not
    silent-current." The metric IS publishing, pinned at 1000000.0 every hour.
    A starved-only check would call that healthy and move on.

    So the pathology is not always "no signal". It is often "the SAME signal
    forever" -- a detector reporting one unchanging thing, which is
    indistinguishable from a detector that has stopped thinking. Printing the
    pinned value makes a fail-loud sentinel (1e6) or a stuck flag (1.0) visible
    at a glance, instead of inferable only by someone who already suspects it.
    Make the invariant printable, then look at it.
    """
    ns, name = alarm.get("Namespace"), alarm.get("MetricName")
    if not ns or not name:
        return (None, None)
    try:
        r = cw.get_metric_statistics(
            Namespace=ns,
            MetricName=name,
            Dimensions=alarm.get("Dimensions", []),
            StartTime=since,
            EndTime=_utcnow(),
            Period=max(60, int(alarm.get("Period") or 300)),
            Statistics=["Maximum"],
        )
    except Exception:  # noqa: BLE001
        return (None, None)
    pts = r.get("Datapoints", [])
    if not pts:
        return (False, None)
    vals = {round(float(p["Maximum"]), 6) for p in pts}
    return (True, vals.pop() if len(vals) == 1 else None)


def main() -> int:
    ap = argparse.ArgumentParser(description="Find latched / starved CloudWatch alarms")
    ap.add_argument("--hours", type=float, default=24.0, help="latch threshold in hours (default 24)")
    ap.add_argument("--region", default="us-east-1")
    ap.add_argument("--emit-metric", action="store_true", help="publish Opal/AlarmHealth LatchedAlarmCount")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any L1/L2 found")
    ap.add_argument("--quiet", action="store_true", help="only findings")
    args = ap.parse_args()

    cw = boto3.client("cloudwatch", region_name=args.region)
    now = _utcnow()
    cutoff = now - dt.timedelta(hours=args.hours)

    alarms = describe_all_alarms(cw)
    if not args.quiet:
        print(f"alarm-latch-sweep -- {len(alarms)} metric alarm(s) in {args.region} "
              f"(fully paginated), latch threshold {args.hours}h")
        print()

    latched, starved, pinned, insufficient = [], [], [], []
    for a in alarms:
        state = a.get("StateValue")
        ts = a.get("StateUpdatedTimestamp")
        if not ts:
            continue
        age_h = (now - ts).total_seconds() / 3600.0
        if state == "ALARM" and ts < cutoff:
            dp, pin = metric_shape(cw, a, cutoff)
            rec = (a["AlarmName"], age_h, dp, pin)
            latched.append(rec)
            if dp is False:
                starved.append(rec)
            elif pin is not None:
                pinned.append(rec)
        elif state == "INSUFFICIENT_DATA" and ts < cutoff:
            insufficient.append((a["AlarmName"], age_h, None, None))

    def _desc(dp, pin) -> str:
        if dp is None:
            return "undecidable"
        if dp is False:
            return "NO DATAPOINTS"
        if pin is not None:
            return f"PINNED @ {pin:g}"
        return "varying"

    def _fmt(rows, label, note):
        if not rows:
            return
        print(f"{label} ({len(rows)}):")
        print(f"  {note}")
        for name, age_h, dp, pin in sorted(rows, key=lambda r: -r[1]):
            print(f"    {age_h:7.1f}h  {name:<58} metric: {_desc(dp, pin)}")
        print()

    _fmt(latched, "L1 LATCHED (in ALARM past threshold)",
         "cannot transition -> cannot notify on the failure it exists to detect")
    _fmt(starved, "L2 STARVED (latched AND metric published nothing)",
         "a dead producer under missing-data=breaching: a BROKEN DETECTOR, not an incident")
    _fmt(pinned, "L4 PINNED (latched AND metric constant across the window)",
         "one unchanging signal forever. A fail-loud sentinel (e.g. 1e6) or a stuck flag (1.0) "
         "looks identical to a detector that stopped thinking. Read the value.")
    _fmt(insufficient, "L3 INSUFFICIENT_DATA past threshold",
         "a control that never armed")

    if not (latched or insufficient):
        print("OK: no latched, starved, or pinned alarms.")

    if args.emit_metric:
        # Report our own count so a STUCK SWEEP is a flat line, not silence.
        cw.put_metric_data(
            Namespace="Opal/AlarmHealth",
            MetricData=[
                {"MetricName": "LatchedAlarmCount", "Value": float(len(latched)), "Unit": "Count"},
                {"MetricName": "StarvedAlarmCount", "Value": float(len(starved)), "Unit": "Count"},
                {"MetricName": "PinnedAlarmCount", "Value": float(len(pinned)), "Unit": "Count"},
                {"MetricName": "SweepRan", "Value": 1.0, "Unit": "Count"},
            ],
        )
        print("emitted Opal/AlarmHealth: LatchedAlarmCount / StarvedAlarmCount / SweepRan")

    if args.strict and (latched or starved or pinned):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
