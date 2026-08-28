#!/usr/bin/env python3
"""schedule-check.py -- the SCHEDULED JOBS dashboard. VIEW-TIME COMPILED.

The /directives-check of the estate's schedulers: what is scheduled, when it fires, and whether
its live state matches declared intent. Read-only -- live AWS APIs + org/missions/SCHEDULE.yaml.

*** THERE IS NO GENERATED ARTIFACT AND THAT IS THE ENTIRE POINT. ***
Every value is read at the moment you run it, so nothing here can go stale. The alternative --
emit a file, fingerprint it, add a --check, name a regen owner -- is machinery that exists only
to manage a cache, and the cache is the bug. (Live example the day this was written:
infra/system/06_current_state.json read STALE rc=2 for an entire day because its regen belonged
to a device nobody was sitting at.) Do NOT add a caching layer to this tool.

WHAT THAT COSTS, STATED: the failure mode inverts. A stale file fails by confidently showing OLD
data; this fails by NOT ANSWERING -- throttle, expired creds, an API error. That is strictly
better because it is loud, but ONLY IF a plane that could not be read renders as UNREADABLE
rather than as zero rows. A partial table presented as complete is the one way this tool can lie.
Hence: every plane prints its own status and its own denominator, always.

THE TIMEZONE TRAP THIS TOOL EXISTS TO CLOSE (measured 2026-08-28, both APIs):
    EventBridge RULES      have NO timezone field. Their cron is ALWAYS UTC.
    EventBridge SCHEDULER  carries an explicit ScheduleExpressionTimezone.
So `cron(15 9 * * ? *)` is 09:15 UTC in one plane and 09:15 America/New_York in the other -- a
4-5 hour difference that shifts with DST. Reading a merged timetable off the raw expressions puts
jobs in the WRONG ORDER. Every row is therefore normalised to BOTH utc and et, and any expression
that is not a single fixed time-of-day renders '-' rather than a guess.

ADDING A PLANE: append one reader to PLANES. A reader takes no arguments and returns a
PlaneResult. Nothing else changes -- the render, the join, and the denominators are generic.

Usage:
  schedule-check.py                 the timetable, ordered by fire time
  schedule-check.py --drift         only rows whose live state differs from declared intent
  schedule-check.py --plane rules   one plane
  schedule-check.py --json          machine-readable
  schedule-check.py --no-color      plain output

Exit: 0 rendered; 1 hard error (nothing rendered); 2 rendered but >=1 plane UNREADABLE (partial).
      Drift NEVER changes the exit code -- this is a viewer, not a checker (CLAUDE.md monitor
      moratorium). It reports; it does not alert and it does not gate.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from typing import Callable

try:
    import boto3
except ImportError:
    print("ERROR: boto3 missing -- schedule-check needs it", file=sys.stderr)
    sys.exit(1)

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("ERROR: zoneinfo missing -- needs python 3.9+", file=sys.stderr)
    sys.exit(1)

ET = ZoneInfo("America/New_York")
UTC = datetime.timezone.utc
REGION = os.environ.get("AWS_REGION", "us-east-1")
DECL_PATH = "org/missions/SCHEDULE.yaml"


# --------------------------------------------------------------------------------------------
# Row + plane types
# --------------------------------------------------------------------------------------------

@dataclass
class Row:
    plane: str
    id: str
    state: str                 # ENABLED / DISABLED / other, verbatim from the API
    raw: str = ""              # the schedule expression exactly as the API returned it
    tz: str = "UTC"            # RULES are always UTC; SCHEDULER carries its own
    kind: str = "timed"        # timed | event  (an event-pattern rule has no fire time)
    target: str = ""
    utc_hhmm: str | None = None
    et_hhmm: str | None = None


@dataclass
class PlaneResult:
    name: str
    status: str                # READ | UNREADABLE
    rows: list[Row] = field(default_factory=list)
    error: str = ""
    note: str = ""


# --------------------------------------------------------------------------------------------
# Time normalisation -- never guess
# --------------------------------------------------------------------------------------------

_CRON_RE = re.compile(r"^cron\((.+)\)$", re.I)
_RATE_RE = re.compile(r"^rate\((.+)\)$", re.I)


def _fixed_hhmm(expr: str) -> tuple[int, int] | None:
    """Return (hour, minute) ONLY when the expression is a single fixed time-of-day.

    Anything with a wildcard, list, range or step in the minute/hour fields fires more than once
    a day (or at a shifting time), and collapsing that to one clock time would be a fabricated
    value. Those return None and render '-'. A '-' here means 'not a single daily time', NOT
    'unknown' -- the raw expression is always shown beside it so nothing is hidden.
    """
    m = _CRON_RE.match(expr.strip())
    if not m:
        return None
    parts = m.group(1).split()
    if len(parts) < 2:
        return None
    minute, hour = parts[0], parts[1]
    if not (minute.isdigit() and hour.isdigit()):
        return None
    mi, hh = int(minute), int(hour)
    if not (0 <= mi < 60 and 0 <= hh < 24):
        return None
    return hh, mi


def _normalise(expr: str, tzname: str) -> tuple[str | None, str | None]:
    """Render a fixed daily time in BOTH utc and et. DST-aware via today's date."""
    hm = _fixed_hhmm(expr)
    if hm is None:
        return None, None
    hh, mi = hm
    try:
        src = ZoneInfo(tzname) if tzname and tzname != "UTC" else UTC
    except Exception:
        return None, None
    today = datetime.datetime.now(UTC).date()
    local = datetime.datetime(today.year, today.month, today.day, hh, mi, tzinfo=src)
    return local.astimezone(UTC).strftime("%H:%M"), local.astimezone(ET).strftime("%H:%M")


# --------------------------------------------------------------------------------------------
# Plane readers -- add one function to add a plane
# --------------------------------------------------------------------------------------------

def read_eventbridge_rules() -> PlaneResult:
    """EventBridge Rules. PAGINATE -- a bare list_rules returns ONE page and the count off that
    page is the page size, not the estate. Same class as the `--query length()` trap."""
    try:
        c = boto3.client("events", region_name=REGION)
        rows: list[Row] = []
        token = None
        while True:
            kw = {"Limit": 100}
            if token:
                kw["NextToken"] = token
            resp = c.list_rules(**kw)
            for r in resp.get("Rules", []):
                expr = r.get("ScheduleExpression", "") or ""
                kind = "timed" if expr else "event"
                # RULES HAVE NO TIMEZONE FIELD. Always UTC. Do not invent one.
                u, e = _normalise(expr, "UTC") if expr else (None, None)
                rows.append(Row(plane="rules", id=r["Name"], state=r.get("State", "?"),
                                raw=expr, tz="UTC", kind=kind, utc_hhmm=u, et_hhmm=e,
                                target=r.get("EventBusName", "")))
            token = resp.get("NextToken")
            if not token:
                break
        return PlaneResult("EventBridge Rules", "READ", rows)
    except Exception as exc:
        return PlaneResult("EventBridge Rules", "UNREADABLE", [], error=str(exc)[:160])


def read_eventbridge_scheduler() -> PlaneResult:
    """EventBridge Scheduler. A SEPARATE API AND A SEPARATE PLANE: list_rules above structurally
    CANNOT see these, so omitting this reader silently undercounts the estate."""
    try:
        c = boto3.client("scheduler", region_name=REGION)
        rows: list[Row] = []
        token = None
        while True:
            kw = {"MaxResults": 100}
            if token:
                kw["NextToken"] = token
            resp = c.list_schedules(**kw)
            for s in resp.get("Schedules", []):
                name = s["Name"]
                expr = s.get("ScheduleExpression", "") or ""
                tz = s.get("ScheduleExpressionTimezone") or "UTC"
                tgt = (s.get("Target") or {}).get("Arn", "")
                if not expr:
                    # The summary omits it on some shapes; fetch the one schedule rather than
                    # rendering a blank that reads as 'no schedule'.
                    try:
                        full = c.get_schedule(Name=name, GroupName=s.get("GroupName", "default"))
                        expr = full.get("ScheduleExpression", "") or ""
                        tz = full.get("ScheduleExpressionTimezone") or tz
                        tgt = tgt or (full.get("Target") or {}).get("Arn", "")
                    except Exception:
                        pass
                u, e = _normalise(expr, tz) if expr else (None, None)
                rows.append(Row(plane="scheduler", id=name, state=s.get("State", "?"),
                                raw=expr, tz=tz, kind="timed" if expr else "event",
                                utc_hhmm=u, et_hhmm=e, target=tgt.split(":")[-1] if tgt else ""))
            token = resp.get("NextToken")
            if not token:
                break
        return PlaneResult("EventBridge Scheduler", "READ", rows)
    except Exception as exc:
        return PlaneResult("EventBridge Scheduler", "UNREADABLE", [], error=str(exc)[:160])


# Append a reader here to add a plane. Nothing else needs to change.
PLANES: list[tuple[str, Callable[[], PlaneResult]]] = [
    ("rules", read_eventbridge_rules),
    ("scheduler", read_eventbridge_scheduler),
]


# --------------------------------------------------------------------------------------------
# Declared intent -- EXCEPTIONS ONLY
# --------------------------------------------------------------------------------------------

def load_declarations(root: str) -> tuple[dict[str, dict], str]:
    """SCHEDULE.yaml holds ONLY what no API can answer.

    Measured 2026-08-28: 18 of 157 jobs are not ENABLED. So `expect` DEFAULTS TO ENABLED and the
    file records exceptions only -- ~18 rows, not 157. Anything derivable (cron, state, target)
    is deliberately absent: writing a queryable value down creates a second carrier that drifts,
    which is the disease this tool cures.
    """
    path = os.path.join(root, DECL_PATH)
    if not os.path.exists(path):
        return {}, "ABSENT (every job defaults to expect=ENABLED)"
    try:
        import yaml
    except ImportError:
        return {}, "PyYAML MISSING -- declarations NOT loaded"
    try:
        with open(path, encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        out = {}
        for e in (data.get("exceptions") or []):
            if isinstance(e, dict) and e.get("id"):
                out[e["id"]] = e
        return out, "loaded"
    except Exception as exc:
        return {}, f"UNPARSEABLE: {str(exc)[:80]}"


# --------------------------------------------------------------------------------------------
# Render
# --------------------------------------------------------------------------------------------

def git_head(root: str) -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short=10", "HEAD"], cwd=root,
                              capture_output=True, text=True, timeout=10).stdout.strip() or "?"
    except Exception:
        return "?"


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--drift", action="store_true", help="only rows whose state differs from intent")
    ap.add_argument("--plane", help="restrict to one plane key")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--events", action="store_true", help="include event-driven (untimed) rules")
    args = ap.parse_args()

    root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                          text=True).stdout.strip() or os.getcwd()

    results = [fn() for key, fn in PLANES if not args.plane or args.plane == key]
    if not results:
        print(f"ERROR: no plane matches --plane {args.plane!r}", file=sys.stderr)
        return 1

    decls, decl_status = load_declarations(root)
    now = datetime.datetime.now(UTC)

    all_rows: list[Row] = []
    for r in results:
        all_rows.extend(r.rows)

    def expect_of(rid: str) -> str:
        return (decls.get(rid) or {}).get("expect", "ENABLED")

    drift = [r for r in all_rows if r.state != expect_of(r.id)]

    if args.json:
        print(json.dumps({
            "compiled_at": now.isoformat(),
            "head": git_head(root),
            "declarations": decl_status,
            "planes": [{"name": p.name, "status": p.status, "count": len(p.rows),
                        "error": p.error} for p in results],
            "rows": [vars(r) for r in all_rows],
            "drift": [{"id": r.id, "plane": r.plane, "applied": r.state,
                       "expect": expect_of(r.id),
                       "declared": r.id in decls} for r in drift],
        }, indent=2))
        return 2 if any(p.status != "READ" for p in results) else 0

    print(f"SCHEDULE-CHECK   compiled {now.strftime('%Y-%m-%dT%H:%M:%SZ')}   "
          f"@HEAD {git_head(root)}   region={REGION}")
    print("  A RENDER, NOT A FILE. Nothing cached. A PASTED COPY IS A SNAPSHOT AND AGES IMMEDIATELY.")
    print(f"  declarations: {DECL_PATH} -- {decl_status}")
    print()

    print("PLANE                       STATUS      ROWS   TIMED  ENABLED")
    for p in results:
        timed = sum(1 for r in p.rows if r.kind == "timed")
        en = sum(1 for r in p.rows if r.state == "ENABLED")
        cnt = "-" if p.status != "READ" else str(len(p.rows))
        print(f"  {p.name:<26}{p.status:<11}{cnt:>5}{(timed if p.status=='READ' else '-'):>8}"
              f"{(en if p.status=='READ' else '-'):>9}")
        if p.error:
            print(f"      ERROR: {p.error}")
    unread = [p for p in results if p.status != "READ"]
    if unread:
        print()
        print("  WARN: " + ", ".join(p.name for p in unread) + " could NOT be read.")
        print("        These render as UNREADABLE, never as zero -- the table below is PARTIAL.")
    print()

    if not args.drift:
        shown = [r for r in all_rows if args.events or r.kind == "timed"]
        # Order by fire time -- this is what makes it a TIMETABLE and not a list. Rows with no
        # single daily time sort last rather than being dropped.
        shown.sort(key=lambda r: (r.utc_hhmm is None, r.utc_hhmm or "", r.id))
        print(f"TIMETABLE ({len(shown)} rows, ordered by fire time)")
        print("  UTC    ET     STATE     PLANE      JOB                                   EXPRESSION (tz)")
        for r in shown:
            u = r.utc_hhmm or "  -  "
            e = r.et_hhmm or "  -  "
            st = "ok " if r.state == "ENABLED" else "OFF"
            tzs = "" if r.tz == "UTC" else f" [{r.tz}]"
            print(f"  {u:<6} {e:<6} {st:<9} {r.plane:<10} {r.id[:36]:<37} {r.raw}{tzs}")
        print()

    print(f"DRIFT ({len(drift)}) -- live state differs from declared intent")
    if not drift:
        print("  none")
    for r in sorted(drift, key=lambda x: x.id):
        d = decls.get(r.id)
        who = (d or {}).get("owner", "UNDECLARED")
        note = (d or {}).get("note", "")
        print(f"  {r.id[:44]:<45} expect {expect_of(r.id):<9} applied {r.state:<9} {who}")
        if note:
            print(f"      {note}")
    print()

    total = len(all_rows)
    timed = sum(1 for r in all_rows if r.kind == "timed")
    print(f"SCHEDULE-CHECK-RESULT planes={len(results)} read={len(results)-len(unread)} "
          f"unreadable={len(unread)} jobs={total} timed={timed} "
          f"declared={len(decls)} drift={len(drift)}")
    return 2 if unread else 0


if __name__ == "__main__":
    sys.exit(main())
