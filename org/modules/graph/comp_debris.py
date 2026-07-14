"""
comp-debris -- coldest-first cloud-resource INVOCATION-coldness ledger (advisory; NEVER deletes).

WHY (NFRA_INSTDRILL Part 3, Andrew-direct, 2026-07-14; refined verbatim x3 in the CVO~Z brief).
Keyed to the opal-data-assets monolith cutover: "checking cloudtrail and organizing resources by
oldest last invocation" -- the cold tail, ranked coldest-down, so a human can see what has gone
dormant. v1 is DELIBERATELY PLAIN (Andrew: "that is just obvious and easy to do"); the fusion
signals (comp-heat federated, comp-dups, comp-deadgrant, comp-trigger) are a SEPARATE CONFIRMATION
PASS you run ON the cold tail -- a pipeline, not machinery inside this tool.

THE THREE BINDING REFINEMENTS (Andrew, verbatim, in-brief):
  1. NEVER-INVOKED != COLD. The coldest-first rank covers ONLY resources WITH prior-activity
     evidence (dormancy AFTER activity). A zero-history resource is NOT ranked cold -- it is split
     by CREATION age into TOO-YOUNG (younger than the window) and STILLBORN-OR-GUARD (older, never
     invoked). Verification Law 4 cuts both ways: an old never-invoked thing is either an abandoned
     half-build OR a rare-event control (a guard that fires monthly/on-incident), and the ranking
     CANNOT TELL THEM APART -- so it refuses to, and routes it to a purpose review instead.
  2. UNKNOWN IS A BAND, not cold. CloudWatch Lambda Invocations only exist when invoked, and the
     window is finite -- a row we could not read, or whose whole history predates the window, is
     UNKNOWN (the anti-correlation trap: a blind row is not a dead row).
  3. ADVISORY, NEVER DELETES. The reap verb stays human + never-widen-gated; hold-aware (INF-chain
     / frozen / sovereign resources are excluded from the REAP output entirely).

CREATION TIME IS REQUIRED PER ROW -- it is the only thing that disambiguates "no events in the
lookback" for a resource older than the window, and the only basis for the TOO-YOUNG vs
STILLBORN-OR-GUARD split.

v1 scope: Lambda functions (the clearest coldness signal -- CloudWatch Invocations + LastModified).
Read-only: list_functions + get_metric_statistics only.

Usage:
    comp-debris [--days 30] [--hot-days 7] [--json]     # the coldest-first ledger
    comp-debris --self-test                             # offline: the band mutants (no AWS)

Author: 1.0.0_SA_CTO~Z (NFRA_INSTDRILL Part 3). 2026-07-14. Read-only, advisory-never-deletes.
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

# HOLD-AWARE: resources whose NAME matches a held/frozen/sovereign class are EXCLUDED from the reap
# output. The INF-chain hold is live + separate from the (lifted) 49F/Schwab block; a frozen-guard
# lambda must never appear on a reap list. Conservative: exclude the INF dispatch/guard chain + any
# sentinel/guard/freeze naming. (A held resource is not a debris candidate; it is load-bearing.)
_HELD_RX = re.compile(r"(inf-gold|inf-canonical|inf-.*(dispatch|freshness|sentinel|guard)|"
                      r"pipeline-complete|frozen|freeze|-hold-|sovereign)", re.I)

BANDS = ("HOT", "COLD-DORMANT", "TOO-YOUNG", "STILLBORN-OR-GUARD", "UNKNOWN")


def _clients(region: str):
    import boto3
    s = boto3.Session(region_name=region or None)
    return s.client("lambda"), s.client("cloudwatch"), s.region_name


def list_lambdas(lam) -> list:
    out, token = [], None
    while True:
        kw = {"Marker": token} if token else {}
        resp = lam.list_functions(**kw)
        for f in resp.get("Functions", []):
            out.append({"name": f.get("FunctionName", ""),
                        "last_modified": f.get("LastModified", "")})
        token = resp.get("NextMarker")
        if not token:
            return out


def invocation_history(cw, name: str, days: int) -> dict:
    """CloudWatch Invocations for one function. Returns {datapoints, total, last_invoked_day} or a
    read-error marker. A function NEVER invoked has NO datapoints (the metric only exists on invoke),
    so 'no datapoints' is genuine within CloudWatch's retention -- but the CALLER still splits it by
    creation age, because within-window absence != never-existed."""
    end = dt.datetime.now(dt.timezone.utc)
    start = end - dt.timedelta(days=days)
    try:
        resp = cw.get_metric_statistics(
            Namespace="AWS/Lambda", MetricName="Invocations",
            Dimensions=[{"Name": "FunctionName", "Value": name}],
            StartTime=start, EndTime=end, Period=86400, Statistics=["Sum"])
        pts = sorted(resp.get("Datapoints", []), key=lambda p: p["Timestamp"])
        nonzero = [p for p in pts if p.get("Sum", 0) > 0]
        total = int(sum(p.get("Sum", 0) for p in pts))
        last = nonzero[-1]["Timestamp"].date().isoformat() if nonzero else None
        return {"read": True, "datapoints": len(pts), "total": total, "last_invoked_day": last}
    except Exception as e:  # noqa: BLE001 -- a read failure is UNKNOWN, never assumed-cold
        return {"read": False, "error": str(e)[:80]}


def _parse_created(last_modified: str):
    try:
        return dt.datetime.strptime(last_modified[:19], "%Y-%m-%dT%H:%M:%S").replace(
            tzinfo=dt.timezone.utc).date()
    except Exception:  # noqa: BLE001
        return None


def classify(row: dict, hist: dict, now_date, days: int, hot_days: int) -> dict:
    """Assign a BAND. Requires the creation date (LastModified) to disambiguate zero-history rows.
    THE INVARIANTS: never-invoked is NEVER 'cold'; an unreadable/blind row is UNKNOWN; a held name
    is not classified here (filtered upstream)."""
    created = _parse_created(row.get("last_modified", ""))
    window_start = now_date - dt.timedelta(days=days)
    r = {"name": row["name"], "created": created.isoformat() if created else "UNKNOWN"}

    if not hist.get("read"):
        return dict(r, band="UNKNOWN", why="metric read failed (%s) -- BLIND, not cold "
                    "(a row we cannot read is not a dead row)" % hist.get("error", "?"))

    last = hist.get("last_invoked_day")
    if last:
        last_d = dt.date.fromisoformat(last)
        age_days = (now_date - last_d).days
        if age_days <= hot_days:
            return dict(r, band="HOT", last_invoked=last, dormant_days=age_days,
                        why="invoked within %dd" % hot_days)
        return dict(r, band="COLD-DORMANT", last_invoked=last, dormant_days=age_days,
                    invocations=hist.get("total"),
                    why="had activity, last invocation %dd ago (dormancy AFTER activity -- reapable)")

    # ZERO invocations in the window -> split by CREATION age (never ranked cold).
    if created is None:
        return dict(r, band="UNKNOWN", why="no invocations in window AND creation date unknown "
                    "-- cannot split TOO-YOUNG from STILLBORN; UNKNOWN, not cold")
    if created >= window_start:
        return dict(r, band="TOO-YOUNG", why="created %s (within the %dd window) -- insufficient "
                    "history to call it dormant" % (created.isoformat(), days))
    return dict(r, band="STILLBORN-OR-GUARD", why="created %s, ZERO invocations in window and "
                "older than it -- either an abandoned half-build OR a rare-event guard; the ranking "
                "CANNOT tell them apart (Verification Law 4). PURPOSE REVIEW, never a coldness rank"
                % created.isoformat())


def build_ledger(rows: list, hists: dict, now_date, days: int, hot_days: int) -> dict:
    held, classified = [], []
    for row in rows:
        if _HELD_RX.search(row["name"]):
            held.append(row["name"])
            continue
        classified.append(classify(row, hists.get(row["name"], {"read": False, "error": "no hist"}),
                                    now_date, days, hot_days))
    by_band = {b: [c for c in classified if c["band"] == b] for b in BANDS}
    # the REAP RANK = COLD-DORMANT only, coldest (largest dormant_days) first. NOTHING else is ranked.
    reap = sorted(by_band["COLD-DORMANT"], key=lambda c: -c.get("dormant_days", 0))
    return {"window_days": days, "hot_days": hot_days,
            "n_total": len(rows), "n_held_excluded": len(held), "held_excluded": sorted(held),
            "counts": {b: len(by_band[b]) for b in BANDS},
            "reap_rank_cold_dormant": reap,
            "purpose_review_stillborn_or_guard": by_band["STILLBORN-OR-GUARD"],
            "too_young": by_band["TOO-YOUNG"], "unknown": by_band["UNKNOWN"], "hot": by_band["HOT"]}


def _render(led: dict) -> str:
    L = ["comp-debris -- coldest-first invocation ledger (ADVISORY -- NEVER deletes; hold-aware)",
         "  window: %dd (hot: last %dd) | %d lambdas | %d held/frozen EXCLUDED from reap"
         % (led["window_days"], led["hot_days"], led["n_total"], led["n_held_excluded"]),
         "  bands: " + " ".join("%s=%d" % (b, led["counts"][b]) for b in BANDS),
         "",
         "  REAP RANK -- COLD-DORMANT only (dormancy AFTER activity; coldest first). This is the",
         "  ONLY ranked list; never-invoked resources are NOT here (see purpose-review below):"]
    if not led["reap_rank_cold_dormant"]:
        L.append("    (none dormant-after-activity in window)")
    for c in led["reap_rank_cold_dormant"][:40]:
        L.append("    %4dd dormant  last=%s  created=%s  %s"
                 % (c.get("dormant_days", 0), c.get("last_invoked"), c["created"], c["name"]))
    sob = led["purpose_review_stillborn_or_guard"]
    if sob:
        L += ["", "  PURPOSE REVIEW -- STILLBORN-OR-GUARD (%d): older than the window, ZERO"
              % len(sob), "  invocations. NOT reap candidates -- an abandoned build looks identical",
              "  to a rare-event guard here. A human decides, per resource:"]
        for c in sob[:20]:
            L.append("    created=%s  %s" % (c["created"], c["name"]))
    if led["counts"]["UNKNOWN"]:
        L += ["", "  UNKNOWN (%d): could not read the metric / no creation date -- BLIND, not cold."
              % led["counts"]["UNKNOWN"]]
    L += ["", "  CONFIRMATION PASS (run ON this cold tail; NOT part of this tool): comp-heat "
          "federated, comp-dups, comp-deadgrant, comp-trigger. Reaping is a human, never-widen act."]
    return "\n".join(L)


def _self_test() -> int:
    """Offline band mutants (no AWS). Every case is one of Andrew's three refinements as a control."""
    results = []
    def ck(name, ok, detail=""):
        results.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))

    now = dt.date(2026, 7, 14)
    days, hot = 30, 7
    def lm(d):  # a LastModified string for a creation date
        return "%sT00:00:00.000+0000" % d

    rows = [
        {"name": "hot-fn", "last_modified": lm("2026-01-01")},
        {"name": "cold-dormant-fn", "last_modified": lm("2026-01-01")},
        {"name": "guard-never-invoked-fn", "last_modified": lm("2025-01-01")},  # OLD, zero invokes
        {"name": "brand-new-fn", "last_modified": lm("2026-07-12")},            # within window, zero
        {"name": "blind-fn", "last_modified": lm("2026-01-01")},                # metric read fails
        {"name": "inf-gold-trigger", "last_modified": lm("2026-01-01")},        # HELD -> excluded
    ]
    hists = {
        "hot-fn": {"read": True, "datapoints": 30, "total": 900, "last_invoked_day": "2026-07-13"},
        "cold-dormant-fn": {"read": True, "datapoints": 30, "total": 5, "last_invoked_day": "2026-06-20"},
        "guard-never-invoked-fn": {"read": True, "datapoints": 0, "total": 0, "last_invoked_day": None},
        "brand-new-fn": {"read": True, "datapoints": 0, "total": 0, "last_invoked_day": None},
        "blind-fn": {"read": False, "error": "AccessDenied"},
        "inf-gold-trigger": {"read": True, "datapoints": 0, "total": 0, "last_invoked_day": None},
    }
    led = build_ledger(rows, hists, now, days, hot)

    # (Andrew refinement 1) NEVER-INVOKED != COLD: the guard is STILLBORN-OR-GUARD, NOT in reap.
    reap_names = {c["name"] for c in led["reap_rank_cold_dormant"]}
    ck("refine1.guard_not_in_reap", "guard-never-invoked-fn" not in reap_names)
    ck("refine1.guard_is_stillborn",
       any(c["name"] == "guard-never-invoked-fn" for c in led["purpose_review_stillborn_or_guard"]))
    # a within-window zero-history fn is TOO-YOUNG, also not reap.
    ck("refine1.new_is_too_young",
       any(c["name"] == "brand-new-fn" for c in led["too_young"]) and "brand-new-fn" not in reap_names)

    # (Andrew refinement 2) UNKNOWN IS A BAND: the blind fn is UNKNOWN, never cold.
    ck("refine2.blind_is_unknown",
       any(c["name"] == "blind-fn" for c in led["unknown"]) and "blind-fn" not in reap_names)

    # (Andrew refinement 3) HOLD-AWARE: the INF-held fn is EXCLUDED entirely, in no band.
    ck("refine3.held_excluded", "inf-gold-trigger" in led["held_excluded"]
       and all("inf-gold-trigger" not in {c["name"] for c in led[k]}
               for k in ("reap_rank_cold_dormant", "purpose_review_stillborn_or_guard", "unknown", "too_young", "hot")))

    # KNOWN-HOT ranks hot (the positive control): the hot fn is HOT, not reap.
    ck("control.known_hot_is_hot",
       any(c["name"] == "hot-fn" for c in led["hot"]) and "hot-fn" not in reap_names)
    # and the one genuine dormant-after-activity fn IS the reap rank.
    ck("control.dormant_is_reap",
       reap_names == {"cold-dormant-fn"} and led["reap_rank_cold_dormant"][0]["dormant_days"] == 24,
       f"reap={reap_names}")

    ok = all(results)
    print("\n" + ("OK: never-invoked!=cold, UNKNOWN-is-a-band, hold-aware, never-deletes -- all held"
                  if ok else "ERROR: comp-debris self-test FAILED"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-debris",
                                 description="coldest-first cloud-resource invocation ledger (advisory; NEVER deletes)")
    ap.add_argument("--days", type=int, default=30, help="coldness window (default 30)")
    ap.add_argument("--hot-days", type=int, default=7, help="recent-enough-to-be-HOT window (default 7)")
    ap.add_argument("--region", default=os.environ.get("AWS_DEFAULT_REGION", "us-east-1"))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass

    if args.self_test:
        return _self_test()

    lam, cw, region = _clients(args.region)
    rows = list_lambdas(lam)
    hists = {r["name"]: invocation_history(cw, r["name"], args.days) for r in rows}
    now_date = dt.datetime.now(dt.timezone.utc).date()
    led = build_ledger(rows, hists, now_date, args.days, args.hot_days)
    led["region"] = region
    if args.json:
        print(json.dumps(led, indent=1, default=str))
    else:
        print(_render(led))
    return 0


if __name__ == "__main__":
    sys.exit(main())
