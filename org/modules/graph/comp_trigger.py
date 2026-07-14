"""
comp-trigger -- EventBridge / Scheduler trigger-dispatch FORENSICS (read-only).

THE GAP THIS CLOSES WAS RECORDED 2026-06-30 AND THEN LOST (NFRA_COMPCLOSE Phase C, 2026-07-14):
an agent wrote "Gap: no comp-tool for CloudTrail/EventBridge/SSM trigger-dispatch forensics ->
candidate comp-trigger" into the compiler-tools log; two weeks later a different agent burned a
night re-deriving the same questions from scratch through raw aws calls, because a gap that lives
only in a log line is re-findable only the expensive way. This tool is the loop's proof-of-closure:
detected -> scored -> BUILT -> registered + routed the same pass.

WHAT IT ANSWERS (the questions agents actually asked, from the rail-log miss corpus):
  - "what fires X / is X's trigger enabled or disabled / what schedule runs X?"
  - "what targets does rule R dispatch to?"
  - "did rule R actually fire recently?"  (CloudWatch TriggeredRules -- with the denominator)
  - "does the terraform DECLARE this rule?" (DESIRED vs LIVE, printed separately -- Rule 22a:
    a comp-tool must never conflate landed with planned)

WHAT IT NEVER DOES: writes. No enable/disable, no put-rule, no put-targets, nothing that could
advance a held chain. The inf-gold-trigger rules are this tool's own FALSE-twin spot-check: it
must REPORT them DISABLED; it can never change them. It also never reads S3 -- the mdpf sentinel
class (bucket-notification triggers) is out of v1 scope ON PURPOSE: the sentinel key is Door 6.

HONESTY RULES (each is a lesson this fabric already paid for):
  - Every scan prints its DENOMINATOR (rules scanned, region, metric window).
  - Zero metric datapoints is reported as "no TriggeredRules datapoints in window" -- which is
    NOT proof of never-fired (metrics absence != event absence); the tool says so itself.
  - TF-desired is a TEXT SCAN of infra/aws/terraform (declared-ness only); it cannot tell
    landed from planned, and says so. LIVE state comes from the live API on the same line.

Usage:
    comp-trigger <query>              # match rules + schedules by name substring OR target ARN substring
    comp-trigger <query> --days 7     # last-fired window (default 7)
    comp-trigger --list               # every rule + schedule, compact state census
    comp-trigger <query> --json
    comp-trigger --self-test          # offline: matcher + renderer + honesty invariants on fixtures

Author: 1.0.0_SA_CTO~Z (NFRA_COMPCLOSE Phase C). 2026-07-14. Read-only by construction.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))
_TF_ROOT = os.path.join(_WS, "infra", "aws")


# ---------------------------------------------------------------------------
# live census (boto3, read-only calls only: list/describe/get-metric-statistics)
# ---------------------------------------------------------------------------
def _clients(region: str):
    import boto3  # lazy -- self-test runs offline without it
    s = boto3.Session(region_name=region or None)
    return s.client("events"), s.client("scheduler"), s.client("cloudwatch"), s.region_name


def live_rules(events) -> list:
    out, token = [], None
    while True:
        kw = {"NextToken": token} if token else {}
        resp = events.list_rules(**kw)
        for r in resp.get("Rules", []):
            out.append({
                "kind": "events-rule",
                "name": r.get("Name", ""),
                "state": r.get("State", "?"),
                "schedule": r.get("ScheduleExpression", "") or "(event-pattern)",
                "pattern": r.get("EventPattern", ""),
                "arn": r.get("Arn", ""),
            })
        token = resp.get("NextToken")
        if not token:
            return out


def live_schedules(scheduler) -> list:
    out, token = [], None
    try:
        while True:
            kw = {"NextToken": token} if token else {}
            resp = scheduler.list_schedules(**kw)
            for s in resp.get("Schedules", []):
                out.append({
                    "kind": "scheduler",
                    "name": s.get("Name", ""),
                    "state": s.get("State", "?"),
                    "schedule": s.get("ScheduleExpression", ""),
                    "pattern": "",
                    "arn": s.get("Arn", ""),
                })
            token = resp.get("NextToken")
            if not token:
                return out
    except Exception as e:  # scheduler service absent/unpermissioned -> reported, never silent
        return [{"kind": "scheduler", "name": "(scheduler census UNAVAILABLE: %s)" % e,
                 "state": "UNKNOWN", "schedule": "", "pattern": "", "arn": "", "census_error": True}]


def rule_targets(events, rule_name: str) -> list:
    try:
        resp = events.list_targets_by_rule(Rule=rule_name)
        return [t.get("Arn", "") for t in resp.get("Targets", [])]
    except Exception as e:
        return ["(targets UNREADABLE: %s)" % e]


def rule_fired(cw, rule_name: str, days: int) -> dict:
    """CloudWatch AWS/Events TriggeredRules for one rule. Absence of datapoints is NOT proof of
    never-fired -- the dict says which it is claiming."""
    end = dt.datetime.now(dt.timezone.utc)
    start = end - dt.timedelta(days=days)
    try:
        resp = cw.get_metric_statistics(
            Namespace="AWS/Events", MetricName="TriggeredRules",
            Dimensions=[{"Name": "RuleName", "Value": rule_name}],
            StartTime=start, EndTime=end, Period=86400, Statistics=["Sum"])
        pts = sorted(resp.get("Datapoints", []), key=lambda p: p["Timestamp"])
        total = int(sum(p.get("Sum", 0) for p in pts))
        last = pts[-1]["Timestamp"].strftime("%Y-%m-%d") if pts else None
        return {"window_days": days, "datapoints": len(pts), "fired_total": total,
                "last_datapoint_day": last,
                "claim": ("FIRED %dx in window (last datapoint %s)" % (total, last)) if pts else
                         ("no TriggeredRules datapoints in %dd window -- NOT proof of never-fired "
                          "(metric absence != event absence)" % days)}
    except Exception as e:
        return {"window_days": days, "datapoints": 0, "fired_total": 0, "last_datapoint_day": None,
                "claim": "metric UNREADABLE (%s) -- fired-state UNKNOWN, not 'did not fire'" % e}


# ---------------------------------------------------------------------------
# TF-desired (a text scan -- DECLARED-ness only, never landed-ness; it says so)
# ---------------------------------------------------------------------------
_TF_RULE_RX = re.compile(
    r'resource\s+"(aws_cloudwatch_event_rule|aws_scheduler_schedule)"\s+"([^"]+)"|name\s*=\s*"([^"]+)"')


def tf_declared(name: str, tf_root: str = _TF_ROOT) -> list:
    """Files under infra/aws/**/*.tf whose text carries the trigger name. String-presence only."""
    hits = []
    if not name or len(name) < 3:
        return hits
    for root, _dirs, files in os.walk(tf_root):
        if ".terraform" in root:
            continue  # the plugin cache is not source (and is 685MB of why we check)
        for f in files:
            if not f.endswith(".tf"):
                continue
            p = os.path.join(root, f)
            try:
                with open(p, encoding="utf-8", errors="replace") as fh:
                    if name in fh.read():
                        hits.append(os.path.relpath(p, _WS).replace("\\", "/"))
            except Exception:
                continue
    return hits


# ---------------------------------------------------------------------------
# matching + report
# ---------------------------------------------------------------------------
def match_triggers(rules: list, query: str, targets_of=None) -> list:
    """Name-substring OR target-ARN-substring match (case-insensitive). targets_of is a callable
    (rule_name -> [arns]) so the live path can lazy-load targets and the self-test can inject."""
    ql = (query or "").lower()
    out = []
    for r in rules:
        if r.get("census_error"):
            out.append(dict(r, match="census-error", targets=[]))
            continue
        tgts = None
        hit = ql in r["name"].lower()
        why = "name" if hit else ""
        if not hit and targets_of is not None and r["kind"] == "events-rule":
            tgts = targets_of(r["name"])
            if any(ql in (t or "").lower() for t in tgts):
                hit, why = True, "target-arn"
        if hit:
            out.append(dict(r, match=why, targets=tgts))
    return out


def render(matches: list, query: str, denom: dict, fired_of=None, tf_of=None) -> str:
    L = ['comp-trigger -- forensics for: "%s"' % query,
         "  denominator: %(rules)d events-rules + %(schedules)d schedules scanned, region %(region)s"
         % denom]
    if not matches:
        L.append("  NO MATCH by name or target-ARN substring. (That is a match-miss, not proof no "
                 "trigger exists -- an S3-notification/sentinel trigger would not appear here; v1 "
                 "scans EventBridge rules + Scheduler schedules only.)")
        return "\n".join(L)
    for m in matches:
        L.append("")
        L.append("  %s  [%s]  %s" % (m["name"], m["kind"], m["state"]))
        L.append("      matched by: %s | schedule: %s" % (m.get("match", "?"), m.get("schedule") or "-"))
        tgts = m.get("targets")
        if tgts is None and m["kind"] == "events-rule":
            tgts = []
        if tgts:
            for t in tgts:
                L.append("      target: %s" % t)
        if fired_of is not None and m["kind"] == "events-rule" and not m.get("census_error"):
            L.append("      LIVE fired-evidence: %s" % fired_of(m["name"])["claim"])
        if tf_of is not None:
            tf = tf_of(m["name"])
            L.append("      TF-DESIRED (declared-ness ONLY -- a text hit cannot tell landed from "
                     "planned): %s" % (", ".join(tf) if tf else "not found in infra/aws/**/*.tf"))
        if m["state"] == "DISABLED":
            L.append("      NOTE: DISABLED is a live API fact. If this is a HELD chain (e.g. the "
                     "inf-gold dispatch hold), DISABLED is the control WORKING -- re-enabling is a "
                     "deploy decision, never a comp-trigger action (this tool has no write path).")
    return "\n".join(L)


# ---------------------------------------------------------------------------
# self-test (offline; fixtures) -- the tool must be provable without AWS
# ---------------------------------------------------------------------------
def _self_test() -> tuple:
    checks = []

    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})

    FIX = [
        {"kind": "events-rule", "name": "inf-gold-trigger-nightly", "state": "DISABLED",
         "schedule": "cron(0 6 * * ? *)", "pattern": "", "arn": "arn:aws:events:::rule/inf-gold"},
        {"kind": "events-rule", "name": "bd-gold-nightly", "state": "ENABLED",
         "schedule": "cron(0 5 * * ? *)", "pattern": "", "arn": "arn:aws:events:::rule/bd-gold"},
        {"kind": "scheduler", "name": "cot-snapshot", "state": "ENABLED",
         "schedule": "rate(1 day)", "pattern": "", "arn": "arn:aws:scheduler:::schedule/cot"},
    ]
    tgt = {"inf-gold-trigger-nightly": ["arn:aws:lambda:::function:inf-gold-trigger"],
           "bd-gold-nightly": ["arn:aws:lambda:::function:bd-gold-runner"]}

    m = match_triggers(FIX, "inf-gold", targets_of=lambda n: tgt.get(n, []))
    ck("match.by_name", len(m) == 1 and m[0]["name"] == "inf-gold-trigger-nightly",
       "%d matches" % len(m))
    m2 = match_triggers(FIX, "bd-gold-runner", targets_of=lambda n: tgt.get(n, []))
    ck("match.by_target_arn", len(m2) == 1 and m2[0]["match"] == "target-arn", "")
    m3 = match_triggers(FIX, "zzz-nonexistent", targets_of=lambda n: tgt.get(n, []))
    ck("match.miss_is_empty", m3 == [], "")

    denom = {"rules": 2, "schedules": 1, "region": "fixture"}
    out = render(m, "inf-gold", denom,
                 fired_of=lambda n: {"claim": "no TriggeredRules datapoints in 7d window -- NOT "
                                              "proof of never-fired (metric absence != event absence)"},
                 tf_of=lambda n: [])
    ck("render.denominator_printed", "2 events-rules + 1 schedules" in out, "")
    ck("render.disabled_is_loud", "DISABLED" in out and "control WORKING" in out, "")
    ck("render.metric_absence_never_claims_neverfired", "NOT proof of never-fired" in out, "")
    ck("render.tf_desired_disclaims_landedness", "cannot tell landed from planned" in out, "")
    out_miss = render([], "zzz", denom)
    ck("render.miss_is_not_proof_of_absence", "not proof no trigger exists" in out_miss, "")

    # THE NO-WRITE INVARIANT, structurally: this module never CALLS a mutating API method.
    # Scan for METHOD-CALL syntax (`.verb(`) so the banned-name strings in this very list
    # cannot self-match -- a control that convicts its own definition is a decoration.
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    banned = ("put_rule", "enable_rule", "disable_rule", "put_targets", "remove_targets",
              "delete_rule", "create_schedule", "update_schedule", "delete_schedule",
              "put_object", "start_execution", "invoke")
    offenders = [b for b in banned if re.search(r"\." + re.escape(b) + r"\s*\(", src)]
    ck("nowrite.no_mutating_call_in_source", not offenders, str(offenders))
    # ...and the control CAN fail: the read-only census call IS present as a method call.
    ck("nowrite.control_can_fire", bool(re.search(r"\.list_rules\s*\(", src)),
       "the detector finds real method calls (list_rules present)")

    ok = all(c["pass"] for c in checks)
    return ok, checks


def main() -> int:
    ap = argparse.ArgumentParser(description="comp-trigger -- EventBridge/Scheduler trigger forensics (read-only)")
    ap.add_argument("query", nargs="?", help="name or target-ARN substring")
    ap.add_argument("--list", action="store_true", help="compact census of every rule + schedule")
    ap.add_argument("--days", type=int, default=7, help="fired-evidence window (default 7)")
    ap.add_argument("--region", default=os.environ.get("AWS_DEFAULT_REGION", "us-east-1"))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true", help="offline fixture suite")
    args = ap.parse_args()

    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(errors="replace")
        except Exception:
            pass

    if args.self_test:
        ok, checks = _self_test()
        for c in checks:
            print("  [%s] %s%s" % ("PASS" if c["pass"] else "FAIL", c["check"],
                                   ("   (%s)" % c["detail"]) if c["detail"] else ""))
        print("\n%s" % ("OK: all checks pass" if ok else "ERROR: checks FAILED"))
        return 0 if ok else 1

    if not args.query and not args.list:
        ap.print_help()
        return 2

    events, scheduler, cw, region = _clients(args.region)
    rules = live_rules(events)
    schedules = live_schedules(scheduler)
    denom = {"rules": len(rules), "schedules": len([s for s in schedules if not s.get("census_error")]),
             "region": region}

    if args.list:
        rows = rules + schedules
        if args.json:
            print(json.dumps({"denominator": denom, "triggers": rows}, indent=1, default=str))
        else:
            print("comp-trigger census -- %(rules)d events-rules + %(schedules)d schedules, region %(region)s" % denom)
            for r in sorted(rows, key=lambda x: (x["kind"], x["name"])):
                print("  %-10s %-9s %-52s %s" % (r["kind"].replace("events-rule", "rule"),
                                                 r["state"], r["name"], r.get("schedule") or ""))
        return 0

    matches = match_triggers(rules + schedules, args.query, targets_of=lambda n: rule_targets(events, n))
    # lazy-load targets for name-matched rules too (match_triggers only loads for target-matching)
    for m in matches:
        if m.get("targets") is None and m["kind"] == "events-rule":
            m["targets"] = rule_targets(events, m["name"])

    if args.json:
        for m in matches:
            if m["kind"] == "events-rule" and not m.get("census_error"):
                m["fired"] = rule_fired(cw, m["name"], args.days)
            m["tf_desired_files"] = tf_declared(m["name"])
        print(json.dumps({"query": args.query, "denominator": denom, "matches": matches},
                         indent=1, default=str))
        return 0

    print(render(matches, args.query, denom,
                 fired_of=lambda n: rule_fired(cw, n, args.days),
                 tf_of=tf_declared))
    return 0


if __name__ == "__main__":
    sys.exit(main())
