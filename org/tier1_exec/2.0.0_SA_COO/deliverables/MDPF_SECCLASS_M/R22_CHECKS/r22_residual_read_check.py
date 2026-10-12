#!/usr/bin/env python3
"""r22_residual_read_check.py -- MDPF_SECCLASS round 22 cell SC-e-95 (rows D1-W83-S5 and D1-W80-S4): the record of the ONE READ exists, carries
its denominators and is internally consistent. Reads one JSON file; writes nothing. A synthetic record with one field broken must fail (the
negative control runs before the real record is graded).

AMENDMENT 1 (issuer, 2026-10-12, answering the worker's row D1-W85-S1): a rebuild from the CURRENT partition also reads the CURRENT reference
inputs (the classifier table, the static tables), so "served vs rebuilt" is two drifts. Each date therefore carries THREE snapshots: the served
one, a rebuild from the partition version that was current when C_06 first built the date (FIRST_BUILD, run through the current classifier and
static tables) and a rebuild from the CURRENT partition. REFERENCE drift = first_build - served; BYTE drift = rebuilt - first_build.

Usage:  python r22_residual_read_check.py <path-to-record.json>

Keys (all required):
  claim (non-empty), read_only (true)
  classes            list of class names the dollars are split by (>= 3)
  dates              list of >= 4 entries, one per retained date 2026-10-06 .. 2026-10-09, each:
                       date, first_build_version{version_id, last_modified}, served_total, first_build_total, rebuilt_total,
                       reference_drift_total, byte_drift_total, delta_total,
                       by_class{<class>:{served, first_build, rebuilt, reference_drift, byte_drift, delta}}
  control_date       one entry of the same shape for a date whose canonical key has exactly ONE version (`versions` == 1), plus `why`,
                       `repeat_delta` (the rebuild run twice: the two rebuilt totals differ by at most 0.01). Its byte_drift_total must be
                       within 1.00 (one version: the harness is not moving); its reference_drift_total is a RESULT, not a failure.
  rederive           list with exactly the N values 1, 3, 5, each: n, trading_days (list of n dates), wall_seconds (>0), peak_mb (>0),
                       relationships_rewritten (int >=0), keys_written (int >=0), bytes_written (int >=0)
  chain_window       launch_to_stop_seconds (>0; a lower bound is allowed and then `lower_bound` is true), c06_wall_seconds_last_fire (>0), source
  canonical_movers   writer (non-empty), dates[ {date, versions >= 1, content_changes >= 0, last_content_change} ], how_far_back_days (int >=0),
                       how_often (non-empty)
  unlisted_unclassified   date (2026-10-09), usd (>= 0), positions (int >= 0), top[ {ticker, name, usd, has_name_row(bool)} ] (<= 20,
                       security level only), why (non-empty): the REBUILT (current) unclassified dollars NOT in any relationship's stored
                       top-10 list, by security
Consistency:
  per entry: the by_class sums equal the totals; reference_drift = first_build - served and byte_drift = rebuilt - first_build and delta =
  rebuilt - served, per class and in total (to the cent).
  rederive is non-decreasing in relationships_rewritten and wall_seconds as n grows.
Prints  R22-RESIDUAL ok=<bool> dates=<n> control_byte_drift=<usd> control_reference_drift=<usd> rederive=<n> movers_dates=<n> control=<ok|BROKEN>
"""
import copy
import json
import sys
from pathlib import Path

CENT = 0.0051


def _entry_ok(e: dict, classes: list) -> bool:
    bc = e["by_class"]
    if set(bc) != set(classes):
        return False
    n = len(classes)
    for tot, key in (("served_total", "served"), ("first_build_total", "first_build"), ("rebuilt_total", "rebuilt")):
        if abs(sum(float(bc[c][key]) for c in classes) - float(e[tot])) > CENT * n:
            return False
    for c in classes:
        v = bc[c]
        if abs(float(v["first_build"]) - float(v["served"]) - float(v["reference_drift"])) > CENT:
            return False
        if abs(float(v["rebuilt"]) - float(v["first_build"]) - float(v["byte_drift"])) > CENT:
            return False
        if abs(float(v["rebuilt"]) - float(v["served"]) - float(v["delta"])) > CENT:
            return False
    s, f, r = float(e["served_total"]), float(e["first_build_total"]), float(e["rebuilt_total"])
    return (abs(f - s - float(e["reference_drift_total"])) <= CENT * n and abs(r - f - float(e["byte_drift_total"])) <= CENT * n
            and abs(r - s - float(e["delta_total"])) <= CENT * n)


def _grade(d: dict) -> bool:
    try:
        classes = list(d["classes"])
        if d.get("read_only") is not True or not str(d.get("claim", "")).strip() or len(classes) < 3:
            return False
        dates = d["dates"]
        want = {"2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09"}
        if len(dates) < 4 or not want <= {x["date"] for x in dates}:
            return False
        if not all(_entry_ok(x, classes) and x["first_build_version"]["version_id"] for x in dates):
            return False
        c = d["control_date"]
        if not _entry_ok(c, classes) or int(c["versions"]) != 1 or c["date"] in want or not str(c.get("why", "")).strip():
            return False
        if abs(float(c["byte_drift_total"])) > 1.00 or abs(float(c["repeat_delta"])) > 0.01:
            return False
        rd = sorted(d["rederive"], key=lambda x: x["n"])
        if [x["n"] for x in rd] != [1, 3, 5]:
            return False
        for x in rd:
            if len(x["trading_days"]) != x["n"] or float(x["wall_seconds"]) <= 0 or float(x["peak_mb"]) <= 0:
                return False
            if min(int(x["relationships_rewritten"]), int(x["keys_written"]), int(x["bytes_written"])) < 0:
                return False
        if not (rd[0]["relationships_rewritten"] <= rd[1]["relationships_rewritten"] <= rd[2]["relationships_rewritten"]):
            return False
        if not (float(rd[0]["wall_seconds"]) <= float(rd[1]["wall_seconds"]) <= float(rd[2]["wall_seconds"])):
            return False
        w = d["chain_window"]
        if float(w["launch_to_stop_seconds"]) <= 0 or float(w["c06_wall_seconds_last_fire"]) <= 0 or not str(w.get("source", "")).strip():
            return False
        m = d["canonical_movers"]
        if not str(m.get("writer", "")).strip() or not str(m.get("how_often", "")).strip() or int(m["how_far_back_days"]) < 0:
            return False
        if not (m["dates"] and all(int(x["versions"]) >= 1 and int(x["content_changes"]) >= 0 for x in m["dates"])):
            return False
        u = d["unlisted_unclassified"]
        if u["date"] != "2026-10-09" or float(u["usd"]) < 0 or int(u["positions"]) < 0 or not str(u.get("why", "")).strip():
            return False
        top = u["top"]
        if len(top) > 20 or not all(isinstance(x["has_name_row"], bool) and x["ticker"] is not None and float(x["usd"]) >= 0 for x in top):
            return False
        banned = ("relationship", "account_id", "client_name", "rid")
        return not any(k in json.dumps(top).lower() for k in banned)
    except (KeyError, TypeError, ValueError, AttributeError):
        return False


def main(argv) -> int:
    if len(argv) != 2:
        print("R22-RESIDUAL ok=False error=usage (path)")
        return 2
    p = Path(argv[1])
    if not p.is_file():
        print("R22-RESIDUAL ok=False error=absent")
        return 1
    d = json.loads(p.read_text(encoding="utf-8"))
    good = _grade(d)
    broken = copy.deepcopy(d)
    try:
        broken["dates"][0]["served_total"] = float(broken["dates"][0]["served_total"]) + 1000.0
    except (KeyError, TypeError, ValueError, IndexError):
        pass
    control = "ok" if (good and not _grade(broken)) else "BROKEN"
    ok = good and control == "ok"
    c = d.get("control_date") if isinstance(d.get("control_date"), dict) else {}
    print(f"R22-RESIDUAL ok={ok} dates={len(d.get('dates', []))} control_byte_drift={c.get('byte_drift_total')} "
          f"control_reference_drift={c.get('reference_drift_total')} rederive={len(d.get('rederive', []))} "
          f"movers_dates={len((d.get('canonical_movers') or {}).get('dates', []))} control={control}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
