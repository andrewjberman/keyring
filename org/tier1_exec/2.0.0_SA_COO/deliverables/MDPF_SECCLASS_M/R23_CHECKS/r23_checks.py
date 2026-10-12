#!/usr/bin/env python3
"""r23_checks.py -- MDPF_SECCLASS round 23 (CTO round-22 ruling (a): a ROLLING re-derive over the producer's own correction window).
Run from the repo root being graded.  Reads only; writes nothing.

Usage:  python r23_checks.py <window-read|unlisted> <record.json>
        python r23_checks.py <rederive|wiring>
        python r23_checks.py half <half_request.md>

window-read <record>  (cell SC-e-96)  the record of the ONE READ of the window, its cost and its gap. Keys, all required:
    claim (non-empty), read_only (true)
    producer_rule   {source_file, source_line (int>0), force_recent_days (int>0), anchor_rule (non-empty: how B_00 anchors and
                     cuts the window), runtime_source (non-empty: where C_06 can read the number at build time), readable_at_runtime (bool)}
    window          {anchor_date, cutoff_date, dates[ISO strings, ascending, >= 5]}   the dates B_00's own rule re-processes today
    cost            {dates_rederived (== len(window.dates)), cold_wall_seconds (>0), warm_wall_seconds (>0), peak_mb (>0),
                     relationships_rewritten (int>=0), keys_written (int>=0), bytes_written (int>=0), instrument (non-empty),
                     added_budget_seconds (== 1800), fits (bool: cold_wall_seconds <= added_budget_seconds), largest_n_that_fits (int>=1)}
    per_date        list, one per window date: {date, served_unclassified, rebuilt_unclassified, delta_unclassified (rebuilt - served),
                     relationships_stored_not_in_partition (int>=0), relationships_in_partition_not_stored (int>=0)}
    gap_if_truncated list of {newest_n (1..len), uncorrected_abs_unclassified_usd}: dollars left wrong on the dates NOT re-derived if
                     only the newest `newest_n` window dates are
  Consistency: delta = rebuilt - served per date (to the cent); gap_if_truncated is non-increasing as newest_n grows and 0 at len(window).
  Prints  WINDOW-READ ok=<bool> dates=<n> fits=<bool> control=<ok|BROKEN>

rederive  (cell SC-e-97)  drives the module's OWN pure functions (R23_C06_FILE overrides the file for the issuer's positive control):
    producer_force_recent_days(catalog_text=None) -> int | None     parses the B_00 CATALOG line of gold_dispatch.sh
    rolling_window_dates(cube_dates, force_recent_days) -> list     B_00's arithmetic: anchor = newest date, keep d >= anchor - N days
    restate_window(existing_mix, existing_conc, rederived, window_dates) -> int   replace each window date's entry by the re-derived one
                    (remove it where the partition no longer has the relationship on that date), never touch a date outside the
                    window, return the number of DATES changed; a second identical call returns 0 and changes nothing.
  Prints  ROLLING-REDERIVE ok=<bool> rule=<bool> window=<bool> restated=<bool> outside_untouched=<bool> idempotent=<bool> orphan_removed=<bool>

wiring  (cell SC-e-97)  reads C_06 `build()` and D_04 `build_firm_mix_summary` (R23_C06_FILE / R23_D04_FILE override):
    build() calls producer_force_recent_days, rolling_window_dates and restate_window; the window is computed BEFORE the
    `if not keys_to_process` early return; the string `restated_through` is written by C_06 and passed through by D_04; no literal
    integer is assigned to a name containing RECENT or WINDOW in C_06 (the window is the producer's, never typed again).
  Prints  ROLLING-WIRING ok=<bool> calls=<bool> before_early_return=<bool> c06_restated=<bool> d04_passthrough=<bool> no_typed_window=<bool>

half <file>  (cell SC-e-97)  the never-widen half request: seven `## ` sections (The act, Blast radius, Writers, Both branches,
    Rollback, Expected outcome, Window and gap) and BOTH halves left unsigned (`COO half: UNSIGNED`, `CTO half: UNSIGNED`).
    `Writers` must name D_04 as the writer of platinum/firm/mix_summary.json and C_06 of gold/views/mix_daily_summary.json, with N printed.
  Prints  HALF-REQUEST ok=<bool> sections=<n of 7> unsigned=<bool> writers=<bool>

unlisted <record>  (cell SC-e-98)  the rebuilt Unclassified at 2026-10-09 BY SECURITY with a reason. Keys, all required:
    claim, read_only (true), date ("2026-10-09"), total_unclassified_usd (>0), tolerance_usd (0 < t <= 250)
    reason_codes   list of {code, meaning} (the closed set this read used; each security's code is one of them)
    securities     list of {ticker (string, may be ""), name, usd (>=0), positions (int>=1), reason_code, reason (non-empty),
                    listed_in_stored (bool: inside any relationship's stored top-10 list on that date)}
    unplaced_subset {usd, positions}   the dollars that sit OUTSIDE every stored list (listed_in_stored false), as the CTO's ruling names them
  Consistency: sum(securities.usd) within tolerance of total; unplaced_subset equals the sum over listed_in_stored == false (cent);
  every reason_code is declared; no relationship / account / client key anywhere; <= 400 securities.
  Prints  UNLISTED ok=<bool> securities=<n> total=<usd> unplaced=<usd> control=<ok|BROKEN>
"""
import ast
import copy
import importlib.util
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
GOLD = ROOT / "data/black_diamond/scripts/gold"
C06 = Path(os.environ.get("R23_C06_FILE") or (GOLD / "C_06.client_mix_timeseries.py"))
D04 = Path(os.environ.get("R23_D04_FILE") or (GOLD / "D_04.client_portal_summary.py"))
CENT = 0.0051


def _num(x):
    return float(x)


# --------------------------------------------------------------------------- window-read
def _window_ok(d: dict) -> bool:
    try:
        if d.get("read_only") is not True or not str(d.get("claim", "")).strip():
            return False
        r = d["producer_rule"]
        if not (str(r["source_file"]).strip() and int(r["source_line"]) > 0 and int(r["force_recent_days"]) > 0
                and str(r["anchor_rule"]).strip() and str(r["runtime_source"]).strip() and isinstance(r["readable_at_runtime"], bool)):
            return False
        w = d["window"]
        dates = list(w["dates"])
        if len(dates) < 5 or dates != sorted(dates) or len(set(dates)) != len(dates) or not (w["anchor_date"] and w["cutoff_date"]):
            return False
        c = d["cost"]
        if int(c["dates_rederived"]) != len(dates) or min(_num(c["cold_wall_seconds"]), _num(c["warm_wall_seconds"]), _num(c["peak_mb"])) <= 0:
            return False
        if min(int(c["relationships_rewritten"]), int(c["keys_written"]), int(c["bytes_written"])) < 0 or not str(c["instrument"]).strip():
            return False
        if int(c["added_budget_seconds"]) != 1800 or bool(c["fits"]) != (_num(c["cold_wall_seconds"]) <= 1800) or int(c["largest_n_that_fits"]) < 1:
            return False
        pd = {x["date"]: x for x in d["per_date"]}
        if set(pd) != set(dates):
            return False
        for x in pd.values():
            if abs(_num(x["rebuilt_unclassified"]) - _num(x["served_unclassified"]) - _num(x["delta_unclassified"])) > CENT:
                return False
            if min(int(x["relationships_stored_not_in_partition"]), int(x["relationships_in_partition_not_stored"])) < 0:
                return False
        g = sorted(d["gap_if_truncated"], key=lambda t: int(t["newest_n"]))
        if [int(t["newest_n"]) for t in g] != list(range(1, len(dates) + 1)):
            return False
        vals = [_num(t["uncorrected_abs_unclassified_usd"]) for t in g]
        return all(a >= b - CENT for a, b in zip(vals, vals[1:])) and abs(vals[-1]) <= CENT
    except (KeyError, TypeError, ValueError, AttributeError):
        return False


def _record_main(name, grader, mutate, summary):
    if len(sys.argv) != 3:
        print(f"{name} ok=False error=usage (path)")
        return 2
    p = Path(sys.argv[2])
    if not p.is_file():
        print(f"{name} ok=False error=absent")
        return 1
    d = json.loads(p.read_text(encoding="utf-8"))
    good = grader(d)
    bad = copy.deepcopy(d)
    try:
        mutate(bad)
    except (KeyError, TypeError, ValueError, IndexError, AttributeError):
        pass
    control = "ok" if (good and not grader(bad)) else "BROKEN"
    ok = good and control == "ok"
    print(f"{name} ok={ok} {summary(d)} control={control}")
    return 0 if ok else 1


def window_read() -> int:
    def mut(b):
        b["per_date"][0]["delta_unclassified"] = _num(b["per_date"][0]["delta_unclassified"]) + 1000.0
    return _record_main("WINDOW-READ", _window_ok, mut,
                        lambda d: f"dates={len((d.get('window') or {}).get('dates', []))} fits={(d.get('cost') or {}).get('fits')}")


# --------------------------------------------------------------------------- unlisted
def _unlisted_ok(d: dict) -> bool:
    try:
        if d.get("read_only") is not True or not str(d.get("claim", "")).strip() or d["date"] != "2026-10-09":
            return False
        tol = _num(d["tolerance_usd"])
        if not (0 < tol <= 250) or _num(d["total_unclassified_usd"]) <= 0:
            return False
        codes = {c["code"] for c in d["reason_codes"] if str(c.get("meaning", "")).strip()}
        secs = d["securities"]
        if not codes or not secs or len(secs) > 400:
            return False
        for s in secs:
            if s["ticker"] is None or _num(s["usd"]) < 0 or int(s["positions"]) < 1 or s["reason_code"] not in codes \
                    or not str(s["reason"]).strip() or not isinstance(s["listed_in_stored"], bool):
                return False
        total = sum(_num(s["usd"]) for s in secs)
        if abs(total - _num(d["total_unclassified_usd"])) > tol:
            return False
        un = [s for s in secs if not s["listed_in_stored"]]
        u = d["unplaced_subset"]
        if abs(sum(_num(s["usd"]) for s in un) - _num(u["usd"])) > CENT or sum(int(s["positions"]) for s in un) != int(u["positions"]):
            return False
        blob = json.dumps(secs).lower()
        return not any(k in blob for k in ("relationship_id", "account_id", "client_name", "\"rid\""))
    except (KeyError, TypeError, ValueError, AttributeError):
        return False


def unlisted() -> int:
    def mut(b):
        b["securities"][0]["usd"] = _num(b["securities"][0]["usd"]) + 1000.0
    return _record_main("UNLISTED", _unlisted_ok, mut,
                        lambda d: f"securities={len(d.get('securities', []))} total={d.get('total_unclassified_usd')} "
                                  f"unplaced={(d.get('unplaced_subset') or {}).get('usd')}")


# --------------------------------------------------------------------------- rederive
CATALOG = ("A_03|A_03.positions_cube.py|--upload\nB_00|B_00.canonical_holdings.py|--upload --force-recent-days {n}\n"
           "B_01|B_01.holdings_lots.py|--upload\n")


def _load_c06():
    sys.path.insert(0, str(GOLD))
    for m in [m for m in sys.modules if m == "lib" or m.startswith("lib.")]:
        del sys.modules[m]
    spec = importlib.util.spec_from_file_location("c06_r23_under_test", str(C06))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def rederive() -> int:
    try:
        mod = _load_c06()
    except Exception as e:  # an import failure is a FAIL with its reason, never a crash
        print(f"ROLLING-REDERIVE ok=False error=import:{type(e).__name__}")
        return 1
    fn_rule = getattr(mod, "producer_force_recent_days", None)
    fn_win = getattr(mod, "rolling_window_dates", None)
    fn_rest = getattr(mod, "restate_window", None)
    rule = window = restated = outside = idem = orphan = False
    if fn_rule:
        try:
            rule = (fn_rule(catalog_text=CATALOG.format(n=21)) == 21 and fn_rule(catalog_text=CATALOG.format(n=9)) == 9
                    and fn_rule(catalog_text="B_00|B_00.canonical_holdings.py|--upload\n") is None
                    and fn_rule(catalog_text="") is None)
        except Exception:
            rule = False
    dates = ["2026-09-30", "2026-10-01", "2026-10-02", "2026-10-05", "2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09"]
    if fn_win:
        try:
            w14 = list(fn_win(list(dates), 14))   # anchor 10-09, cutoff 09-25: every date
            w5 = list(fn_win(list(dates), 5))     # cutoff 10-04: 10-05 .. 10-09
            w7 = list(fn_win(list(dates), 7))     # cutoff 10-02 is INCLUDED (>=): 10-02 .. 10-09
            window = (w14 == dates and w5 == dates[3:] and w7 == dates[2:])
        except Exception:
            window = False
    if fn_rest:
        try:
            ds_in, ds_old, ds_gone = "2026-10-08", "2026-10-02", "2026-10-09"
            mix = {ds_old: {"date": ds_old, "equity": 0.5, "unclassified": 0.5, "total_mv": 10.0},
                   ds_in: {"date": ds_in, "equity": 0.5, "unclassified": 0.5, "total_mv": 100.0},
                   ds_gone: {"date": ds_gone, "equity": 1.0, "unclassified": 0.0, "total_mv": 50.0}}
            conc = {ds: {"date": ds, "holdings": [{"ticker": "X", "asset_class": "unclassified", "market_value": 1.0}]} for ds in mix}
            new_in = {"mix": {"equity": 0.9, "unclassified": 0.1}, "total_mv": 100.0,
                      "conc": [{"ticker": "X", "asset_class": "equity", "market_value": 90.0}]}
            before_old = copy.deepcopy((mix[ds_old], conc[ds_old]))
            n = fn_rest(mix, conc, {ds_in: new_in}, [ds_in, ds_gone])
            restated = (n == 2 and abs(mix[ds_in]["equity"] - 0.9) < 1e-9 and mix[ds_in]["total_mv"] == 100.0
                        and conc[ds_in]["holdings"][0]["asset_class"] == "equity")
            outside = (mix[ds_old], conc[ds_old]) == before_old
            orphan = ds_gone not in mix and ds_gone not in conc
            snap = copy.deepcopy((mix, conc))
            again = fn_rest(mix, conc, {ds_in: new_in}, [ds_in, ds_gone])
            idem = again == 0 and (mix, conc) == snap
        except Exception:
            restated = outside = idem = orphan = False
    ok = rule and window and restated and outside and idem and orphan
    print(f"ROLLING-REDERIVE ok={ok} rule={rule} window={window} restated={restated} outside_untouched={outside} "
          f"idempotent={idem} orphan_removed={orphan}")
    return 0 if ok else 1


# --------------------------------------------------------------------------- wiring
def _call_name(c):
    return getattr(c.func, "id", getattr(c.func, "attr", ""))


def wiring() -> int:
    calls = before = c06_rt = d04_rt = no_typed = False
    try:
        t = ast.parse(C06.read_text(encoding="utf-8"))
        build = next((n for n in t.body if isinstance(n, ast.FunctionDef) and n.name == "build"), None)
        if build is not None:
            names = {}
            for c in ast.walk(build):
                if isinstance(c, ast.Call):
                    names.setdefault(_call_name(c), c.lineno)
            calls = all(k in names for k in ("producer_force_recent_days", "rolling_window_dates", "restate_window"))
            early = [n.lineno for n in ast.walk(build) if isinstance(n, ast.If) and isinstance(n.test, ast.UnaryOp)
                     and isinstance(n.test.op, ast.Not) and isinstance(n.test.operand, ast.Name) and n.test.operand.id == "keys_to_process"]
            before = bool(calls and early and names["rolling_window_dates"] < min(early))
        c06_rt = any(isinstance(n, ast.Constant) and n.value == "restated_through" for n in ast.walk(t))
        typed = []
        for n in ast.walk(t):
            if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, int) \
                    and not isinstance(n.value.value, bool):
                for tg in n.targets:
                    if isinstance(tg, ast.Name) and re.search(r"RECENT|WINDOW", tg.id, re.I):
                        typed.append(tg.id)
        no_typed = not typed or all(x.upper().startswith("ROLLING_MAX") for x in typed)  # a CAP constant is the one allowed literal
    except (OSError, SyntaxError):
        pass
    try:
        d = ast.parse(D04.read_text(encoding="utf-8"))
        f = next((n for n in d.body if isinstance(n, ast.FunctionDef) and n.name == "build_firm_mix_summary"), None)
        d04_rt = bool(f is not None and any(isinstance(n, ast.Constant) and n.value == "restated_through" for n in ast.walk(f)))
    except (OSError, SyntaxError):
        pass
    ok = calls and before and c06_rt and d04_rt and no_typed
    print(f"ROLLING-WIRING ok={ok} calls={calls} before_early_return={before} c06_restated={c06_rt} "
          f"d04_passthrough={d04_rt} no_typed_window={no_typed}")
    return 0 if ok else 1


# --------------------------------------------------------------------------- half
SECTIONS = ["the act", "blast radius", "writers", "both branches", "rollback", "expected outcome", "window and gap"]


def half() -> int:
    if len(sys.argv) != 3:
        print("HALF-REQUEST ok=False error=usage (path)")
        return 2
    p = Path(sys.argv[2])
    if not p.is_file():
        print("HALF-REQUEST ok=False error=absent")
        return 1
    t = p.read_text(encoding="utf-8")
    heads = [h.strip().lower() for h in re.findall(r"^##\s+(.+)$", t, re.M)]
    found = [s for s in SECTIONS if any(h.startswith(s) for h in heads)]
    unsigned = bool(re.search(r"^COO half: UNSIGNED\s*$", t, re.M) and re.search(r"^CTO half: UNSIGNED\s*$", t, re.M))
    body = t.lower()
    wi = body.find("writers")
    sect = body[wi:wi + 4000] if wi >= 0 else ""
    writers = bool("platinum/firm/mix_summary.json" in sect and "d_04" in sect and "gold/views/mix_daily_summary.json" in sect
                   and "c_06" in sect and re.search(r"\bn\s*=\s*\d+", sect))
    ok = len(found) == len(SECTIONS) and unsigned and writers
    print(f"HALF-REQUEST ok={ok} sections={len(found)} of {len(SECTIONS)} unsigned={unsigned} writers={bool(writers)}")
    return 0 if ok else 1


if __name__ == "__main__":
    cmds = {"window-read": window_read, "unlisted": unlisted, "rederive": rederive, "wiring": wiring, "half": half}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print("R23 ok=False error=usage (window-read|unlisted|rederive|wiring|half)")
        sys.exit(2)
    sys.exit(cmds[sys.argv[1]]())
