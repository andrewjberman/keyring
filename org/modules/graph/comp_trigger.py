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

sys.path.insert(0, os.path.join(_WS, ".tools"))
import _compbudget  # noqa: E402  -- NFRA_COMPEFFICACY CE-t-9: Rule T's shared carrier (PRD v0.4 s.4.4)

# NFRA_COMPEFFICACY CE-t-9: comp-trigger's v1 scan classes are EventBridge rules + Scheduler
# schedules ONLY; S3 bucket-notification triggers (the mdpf sentinel class) are OUT OF SCOPE ON
# PURPOSE (module docstring :20-21). Every answer line now carries that scope explicitly (never a
# silent "no trigger"), plus the MEASURED delegation this cell found (existing machinery checked
# FIRST, per BOUNDS -- never built here): org/modules/graph/comp_aws_cli.py:273-279 already reads
# S3 GetBucketNotificationConfiguration live and stores event_notifications/notify_sns/notify_sqs
# per S3_BUCKET graph node, queryable today via `comp-find --corpus aws '<bucket-name>'` (measured
# 28/28 S3_BUCKET nodes returned with those three fields present, this cell, 2026-09-03).
SCOPE_LINE = (
    "  scope: EventBridge rules + Scheduler schedules ONLY; S3 bucket notifications NOT scanned "
    "(v1 scope, by design). For an S3-notification/sentinel trigger, delegate to comp-aws's "
    "S3_BUCKET node fields instead: `comp-find --corpus aws '<bucket-name>'` -> "
    "event_notifications/notify_sns/notify_sqs (org/modules/graph/comp_aws_cli.py:273-279, "
    "measured present on 28/28 S3_BUCKET nodes read 2026-09-03)."
)


# ---------------------------------------------------------------------------
# live census (boto3, read-only calls only: list/describe/get-metric-statistics)
# ---------------------------------------------------------------------------
def _clients(region: str, budget_s: float = _compbudget.DEFAULT_BUDGET_S):
    import boto3  # lazy -- self-test runs offline without it
    from botocore.config import Config
    cfg = Config(connect_timeout=budget_s, read_timeout=budget_s) if budget_s > 0 else None
    s = boto3.Session(region_name=region or None)
    return (s.client("events", config=cfg), s.client("scheduler", config=cfg),
            s.client("cloudwatch", config=cfg), s.region_name)


def live_rules(events) -> list:
    """NFRA_COMPEFFICACY CE-t-9: found live, by exercise, that a tiny Rule T budget on this call
    (ConnectTimeoutError) previously crashed the whole tool with a raw traceback -- the WORST form
    of Rule T's KILLED-OUTSIDE hazard, self-inflicted rather than the harness's. Caught and reported
    now, mirroring live_schedules' own existing UNAVAILABLE-sentinel shape (never silent, never a
    crash, never mistaken for a real zero-rules census)."""
    out, token = [], None
    try:
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
    except Exception as e:  # AWS-plane call under Rule T's ceiling -- reported, never a crash
        return [{"kind": "events-rule", "name": "(events census UNAVAILABLE: %s)" % e,
                 "state": "UNKNOWN", "schedule": "", "pattern": "", "arn": "", "census_error": True}]


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


def render(matches: list, query: str, denom: dict, show_fired: bool = False, show_tf: bool = False) -> str:
    """Reads pre-computed enrichment off each match dict (m['fired'], m['tf_desired']) rather than
    taking live-call closures -- NFRA_COMPEFFICACY CE-t-9: enrichment now happens in main() under a
    shared Rule T Clock BEFORE render() is called, so render() itself makes zero AWS/filesystem
    calls and can print the DEFERRED sentinel for a match Rule T's budget skipped. A value of the
    literal string 'DEFERRED' on either key means the budget ran out before this match's call."""
    L = ['comp-trigger -- forensics for: "%s"' % query,
         "  denominator: %(rules)d events-rules + %(schedules)d schedules scanned, region %(region)s"
         % denom,
         SCOPE_LINE]
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
        if tgts == "DEFERRED":
            L.append("      target: DEFERRED -- Rule T budget exhausted before this match's live call")
        else:
            if tgts is None and m["kind"] == "events-rule":
                tgts = []
            for t in (tgts or []):
                L.append("      target: %s" % t)
        if show_fired and m["kind"] == "events-rule" and not m.get("census_error"):
            fired = m.get("fired")
            if fired == "DEFERRED":
                L.append("      LIVE fired-evidence: DEFERRED -- Rule T budget exhausted before this match's live call")
            elif fired is not None:
                L.append("      LIVE fired-evidence: %s" % fired["claim"])
        if show_tf:
            tf = m.get("tf_desired")
            if tf == "DEFERRED":
                L.append("      TF-DESIRED: DEFERRED -- Rule T budget exhausted before this match's local scan")
            else:
                tf = tf or []
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
    m_enriched = [dict(m[0],
                        fired={"claim": "no TriggeredRules datapoints in 7d window -- NOT "
                                        "proof of never-fired (metric absence != event absence)"},
                        tf_desired=[])]
    out = render(m_enriched, "inf-gold", denom, show_fired=True, show_tf=True)
    ck("render.denominator_printed", "2 events-rules + 1 schedules" in out, "")
    ck("render.disabled_is_loud", "DISABLED" in out and "control WORKING" in out, "")
    ck("render.metric_absence_never_claims_neverfired", "NOT proof of never-fired" in out, "")
    ck("render.tf_desired_disclaims_landedness", "cannot tell landed from planned" in out, "")
    out_miss = render([], "zzz", denom)
    ck("render.miss_is_not_proof_of_absence", "not proof no trigger exists" in out_miss, "")

    # NFRA_COMPEFFICACY CE-t-9, T9-AC3: every answer -- hit or miss -- carries the scope it was
    # computed over, and the miss text is never PRESENT_WITH_ZERO_RESULTS-shaped ("no trigger").
    ck("render.scope_line_on_hit", "S3 bucket notifications NOT scanned" in out, "")
    ck("render.scope_line_on_miss", "S3 bucket notifications NOT scanned" in out_miss, "")
    ck("render.scope_names_the_delegation", "comp-find --corpus aws" in out
       and "event_notifications" in out, "")

    # T9-AC4/AC5: Rule T's DEFERRED sentinel renders distinctly for BOTH a skipped target list and
    # a skipped fired-evidence lookup -- never silently absent, never mistaken for a real zero.
    m_deferred = [dict(m[0], targets="DEFERRED", fired="DEFERRED", tf_desired="DEFERRED")]
    out_def = render(m_deferred, "inf-gold", denom, show_fired=True, show_tf=True)
    ck("render.deferred_target_shown", "target: DEFERRED -- Rule T budget exhausted" in out_def, "")
    ck("render.deferred_fired_shown", "LIVE fired-evidence: DEFERRED -- Rule T budget exhausted" in out_def, "")
    ck("render.deferred_tf_shown", "TF-DESIRED: DEFERRED -- Rule T budget exhausted" in out_def, "")

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


def _enrich_matches(matches: list, events, cw, days: int, budget_s: float, budget_source: str,
                    query: str = "") -> dict:
    """NFRA_COMPEFFICACY CE-t-9, Rule T's resumable-per-unit shape: each MATCH (not each call) is
    one unit. Sorted for a deterministic scan order (a real --cursor could resume by name, though
    this tool's match counts are small enough that a cursor flag is not wired this cell -- the
    budget-reached line still names the last-enriched match). Mutates each match dict in place
    (targets/fired/tf_desired), using the literal string 'DEFERRED' once the clock runs out so a
    downstream render/json consumer can never mistake a skipped call for a measured zero. Returns
    the Rule T summary dict main() prints BEFORE the DENOMINATOR block."""
    clock = _compbudget.Clock(budget_s)
    ordered = sorted(matches, key=lambda x: x["name"])
    exhausted_at = None
    for idx, m in enumerate(ordered):
        remaining = clock.remaining()
        if remaining is not None and remaining <= 0:
            exhausted_at = idx
            if m.get("targets") is None and m["kind"] == "events-rule":
                m["targets"] = "DEFERRED"
            m["fired"] = "DEFERRED"
            m["tf_desired"] = "DEFERRED"
            continue
        if m.get("targets") is None and m["kind"] == "events-rule":
            m["targets"] = rule_targets(events, m["name"])
        if m["kind"] == "events-rule" and not m.get("census_error"):
            m["fired"] = rule_fired(cw, m["name"], days)
        m["tf_desired"] = tf_declared(m["name"])
    used_s = round(clock.elapsed(), 2)
    total = len(ordered)
    if exhausted_at is None:
        return {"line": _compbudget.within_budget_line(total, total, "match", budget_s, budget_source, used_s)}
    n_done = exhausted_at
    cursor = ordered[n_done - 1]["name"] if n_done > 0 else None
    if cursor:
        args_repr = "comp-trigger %r" % query
        return {"line": _compbudget.budget_reached_line(budget_s, budget_source, n_done, total, "match",
                                                        args_repr, cursor)}
    return {"line": ("BUDGET REACHED: %s s (%s); scanned 0 of %d match(es); results are a PREFIX, "
                     "not the answer; NO CURSOR YET: no match completed before the budget hit, so "
                     "there is no last-processed unit to resume from; resume: re-run with a larger "
                     "--budget." % (_compbudget.fmt(budget_s), budget_source, total))}


def main() -> int:
    ap = argparse.ArgumentParser(description="comp-trigger -- EventBridge/Scheduler trigger forensics (read-only)")
    ap.add_argument("query", nargs="?", help="name or target-ARN substring")
    ap.add_argument("--list", action="store_true", help="compact census of every rule + schedule")
    ap.add_argument("--days", type=int, default=7, help="fired-evidence window (default 7)")
    ap.add_argument("--region", default=os.environ.get("AWS_DEFAULT_REGION", "us-east-1"))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true", help="offline fixture suite")
    ap.add_argument("--budget", default=None,
                    help=f"Rule T (PRD s.4.4): seconds for the live AWS-plane calls and the "
                         f"per-match enrichment sweep (carrier: --budget > env "
                         f"{_compbudget.ENV_VAR} > default {_compbudget.fmt(_compbudget.DEFAULT_BUDGET_S)}s); "
                         "a match Rule T could not reach before expiry is DEFERRED, never a hang, "
                         "never a silent zero")
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

    try:
        budget_s, budget_source = _compbudget.resolve_budget(getattr(args, "budget", None))
    except ValueError as exc:
        print(f"REFUSED: --budget {exc}")
        return 2
    print(f"  {_compbudget.disclosure_line(budget_s, budget_source)}")

    events, scheduler, cw, region = _clients(args.region, budget_s)
    list_clock = _compbudget.Clock(budget_s)
    rules = live_rules(events)
    schedules = live_schedules(scheduler)
    denom = {"rules": len([r for r in rules if not r.get("census_error")]),
             "schedules": len([s for s in schedules if not s.get("census_error")]),
             "region": region}

    if args.list:
        # ONE opaque, non-resumable pull (both list calls are already fully paginated above) --
        # same disclosed-non-application shape as comp-iam's attach-census: measured post-hoc,
        # never a fabricated partial census.
        used_s = round(list_clock.elapsed(), 2)
        remaining = list_clock.remaining()
        if remaining is None or remaining > 0:
            print(_compbudget.within_budget_line(1, 1, "census_pull", budget_s, budget_source, used_s))
        else:
            print(f"NOT WITHIN BUDGET: the rules+schedules pull took {_compbudget.fmt(used_s)}s, over "
                  f"the {_compbudget.disclosure_line(budget_s, budget_source)} -- but it already RAN TO "
                  "COMPLETION (both list calls are already fully paginated by the time any budget "
                  "check could run; no internal resumption point to abort at). Disclosed "
                  "non-application of the early-abort half of Rule T for this specific subcommand shape.")
        print(SCOPE_LINE)
        rows = rules + schedules
        if args.json:
            print(json.dumps({"denominator": denom, "scope": SCOPE_LINE.strip(), "triggers": rows},
                             indent=1, default=str))
        else:
            print("comp-trigger census -- %(rules)d events-rules + %(schedules)d schedules, region %(region)s" % denom)
            for r in sorted(rows, key=lambda x: (x["kind"], x["name"])):
                print("  %-10s %-9s %-52s %s" % (r["kind"].replace("events-rule", "rule"),
                                                 r["state"], r["name"], r.get("schedule") or ""))
        return 0

    matches = match_triggers(rules + schedules, args.query, targets_of=lambda n: rule_targets(events, n))

    rule_t = _enrich_matches(matches, events, cw, args.days, budget_s, budget_source, query=args.query)
    print(rule_t["line"])

    if args.json:
        for m in matches:
            m["tf_desired_files"] = m.pop("tf_desired", None)
        print(json.dumps({"query": args.query, "denominator": denom, "scope": SCOPE_LINE.strip(),
                         "matches": matches}, indent=1, default=str))
        return 0

    print(render(matches, args.query, denom, show_fired=True, show_tf=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
