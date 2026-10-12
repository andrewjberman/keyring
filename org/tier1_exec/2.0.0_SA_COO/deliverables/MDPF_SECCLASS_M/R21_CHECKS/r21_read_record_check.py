#!/usr/bin/env python3
"""r21_read_record_check.py -- MDPF_SECCLASS round 21 cells SC-e-93 (row D1-W77-S1) and SC-e-94 (row D1-W78-S1): the record of a READ
exists, carries its denominator, and is internally consistent. Reads one JSON file; writes nothing. A synthetic record with one
field broken must fail (the negative control is run inside this script before the real record is graded).

Usage:  python r21_read_record_check.py <w77|w78> <path-to-record.json>

w77 (NAN / NONE ticker count at the latest served partition):
  keys: claim, partition{key,date}, positions_total (>0, the denominator), dollars_total (>0), nan_none{NAN{positions,dollars},
        NONE{positions,dollars}}, nan_none_positions, nan_none_dollars, verdict (NOT_EXPOSED | EXPOSED), read_only (true)
  consistent when nan_none_positions == NAN.positions + NONE.positions, nan_none_dollars == NAN.dollars + NONE.dollars (to the cent),
  and verdict is NOT_EXPOSED exactly when nan_none_positions == 0.
  Prints  W77-RECORD ok=<bool> positions_total=<n> nan_none=<n> verdict=<v> control=<ok|BROKEN>
w78 (the writer that rewrote the 2026-10-06 / 2026-10-07 holdings partitions at 2026-10-10T23:15Z):
  keys: claim, partitions[{date,key,last_modified}] (>=2, naming 2026-10-06 and 2026-10-07), rewrite_window{from,to}, writer{principal,
        identified_by,script_or_lambda}, writer_count (int >= 1, distinct writers of the canonical holdings prefix in the window),
        c06_reserves_dates_next_fire (bool), c06_reason (non-empty), ruling_on_correction_or_drift (null: the ruling follows the read)
  Prints  W78-RECORD ok=<bool> partitions=<n> writer=<principal> writer_count=<n> reserves=<bool> control=<ok|BROKEN>
"""
import copy
import json
import sys
from pathlib import Path


def _w77(d: dict) -> bool:
    try:
        nn = d["nan_none"]
        pos = int(nn["NAN"]["positions"]) + int(nn["NONE"]["positions"])
        usd = float(nn["NAN"]["dollars"]) + float(nn["NONE"]["dollars"])
        return bool(
            d.get("read_only") is True and d.get("claim") and d["partition"]["key"] and d["partition"]["date"]
            and int(d["positions_total"]) > 0 and float(d["dollars_total"]) > 0
            and int(d["nan_none_positions"]) == pos and abs(float(d["nan_none_dollars"]) - usd) < 0.005
            and d["verdict"] == ("NOT_EXPOSED" if pos == 0 else "EXPOSED"))
    except (KeyError, TypeError, ValueError):
        return False


def _w78(d: dict) -> bool:
    try:
        dates = " ".join(str(p.get("date")) for p in d["partitions"])
        w = d["writer"]
        return bool(
            d.get("claim") and len(d["partitions"]) >= 2 and "2026-10-06" in dates and "2026-10-07" in dates
            and all(p.get("key") and p.get("last_modified") for p in d["partitions"])
            and d["rewrite_window"]["from"] and d["rewrite_window"]["to"]
            and w.get("principal") and w.get("identified_by") and w.get("script_or_lambda")
            and int(d["writer_count"]) >= 1 and isinstance(d["c06_reserves_dates_next_fire"], bool)
            and str(d.get("c06_reason", "")).strip() and d.get("ruling_on_correction_or_drift", "MISSING") is None)
    except (KeyError, TypeError, ValueError, AttributeError):
        return False


def _break(which: str, d: dict) -> dict:
    b = copy.deepcopy(d)
    if which == "w77":
        b["nan_none_positions"] = int(b.get("nan_none_positions", 0)) + 1
    else:
        b["writer_count"] = 0
    return b


def main(argv) -> int:
    if len(argv) != 3 or argv[1] not in ("w77", "w78"):
        print("RECORD ok=False error=usage (w77|w78 <path>)")
        return 2
    which, path = argv[1], Path(argv[2])
    tag = "W77-RECORD" if which == "w77" else "W78-RECORD"
    if not path.is_file():
        print(f"{tag} ok=False error=absent")
        return 1
    d = json.loads(path.read_text(encoding="utf-8"))
    fn = _w77 if which == "w77" else _w78
    good = fn(d)
    control = "ok" if (good and not fn(_break(which, d))) else "BROKEN"
    ok = good and control == "ok"
    if which == "w77":
        print(f"{tag} ok={ok} positions_total={d.get('positions_total')} nan_none={d.get('nan_none_positions')} "
              f"verdict={d.get('verdict')} control={control}")
    else:
        w = d.get("writer", {}) or {}
        print(f"{tag} ok={ok} partitions={len(d.get('partitions', []))} writer={w.get('principal')} "
              f"writer_count={d.get('writer_count')} reserves={d.get('c06_reserves_dates_next_fire')} control={control}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
