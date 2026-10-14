"""MDPF_SECHIST round 6, cell SH-t-24 (CTO ADDENDUM 2 of round 5 @d3206f14a8, msg 5564): the closed-market frontier, read on the REAL history.

Read only (get_object / list_objects_v2 through a guarded client; no S3 write, no served write, local stdout only).
Needs `frontier_returns` in data/etfs/scripts/gold/etf_positioning_gold.py (this check FAILS at the base: the function does not exist yet).

  python r6_closed_market_real.py
Interface under test (fixed by the order):
  frontier_returns(tkr, as_of, hist, gap_record=None) -> (windows: dict[str, float|None], frontier: date|None)
  - a reading ON as_of (a NULL reading counts as a reading): frontier == as_of, windows == compute_returns(tkr, as_of, ...)
  - no reading on as_of, the security's last vendor day f <= as_of is at most CARRY_MAX_CALENDAR_DAYS (4) back, and the gap record
    carries the security with absent_count == 0: frontier == f, windows == compute_returns(tkr, f, ...)
  - otherwise: all windows None, frontier None.
Arms on real data, D = 2026-10-13 history:
  e  every ticker with a reading on a book as_of (10-12, 10-13) -> windows equal compute_returns at that as_of, frontier == as_of
  a  SALXX at book as_of 2026-10-12 (Columbus Day, no vendor day) -> frontier 2026-10-09, windows == compute_returns at 10-09, 1D populated
  b  SALXX with every row after 2026-10-07 removed, as_of 10-12 -> blank (the 4-day bound)
  c  SALXX with absent_count set to 1 in a copy of the gap record -> blank
  d  FXFXX at 2026-10-12 (a NULL reading ON as_of) -> frontier 10-12, every window None (C-MMF unchanged)
Prints the MOVED set (tickers whose windows differ from compute_returns at the book as_of): the served keys the pair must name.
Last line: CM-REAL-OK ... or CM-REAL-BAD <reason>.
"""
from __future__ import annotations

import copy
import datetime as dt
import subprocess
import sys
from pathlib import Path

import boto3

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "data" / "etfs" / "scripts" / "gold"))
sys.path.insert(0, str(ROOT / "data" / "etfs" / "scripts" / "silver"))
import etf_positioning_gold as M  # noqa: E402

D = dt.date(2026, 10, 13)
BOOK_DAYS = (dt.date(2026, 10, 12), dt.date(2026, 10, 13))
ALLOWED = ("get_object", "list_objects_v2", "head_object", "exceptions", "meta")


class ReadOnlyS3:
    def __init__(self, real):
        self._real = real

    def __getattr__(self, name):
        if name not in ALLOWED:
            raise RuntimeError("READ-ONLY GUARD: refused S3 call " + name)
        return getattr(self._real, name)


def main():
    if not hasattr(M, "frontier_returns"):
        print("CM-REAL-BAD frontier_returns-missing-in-etf_positioning_gold")
        return 1
    guard = ReadOnlyS3(boto3.client("s3"))
    M._s3 = lambda: guard
    gap = M.load_gap_record(D)
    hist = M.load_history(D)
    bad = []
    fr = M.frontier_returns

    # e: every ticker with a reading on the book as_of is unchanged
    same, moved = 0, []
    for t in sorted(hist["tkr"].unique()):
        have = set(hist.loc[hist["tkr"] == t, "date"])
        for a in BOOK_DAYS:
            old = M.compute_returns(t, a, hist, gap)
            w, f = fr(t, a, hist, gap)
            if a in have:
                if w != old or f != a:
                    bad.append("e:" + t + "@" + a.isoformat() + " moved though it has a reading")
                same += 1
            elif w != old:
                moved.append(t + "@" + a.isoformat() + "->" + (f.isoformat() if f else "blank"))
    print("arm e: " + str(same) + " (ticker, book as_of) pairs with a reading are unchanged")
    print("MOVED (no reading on the book as_of): " + ", ".join(moved))

    # a: SALXX on Columbus Day carries Friday, with its date
    w, f = fr("SALXX", dt.date(2026, 10, 12), hist, gap)
    exp = M.compute_returns("SALXX", dt.date(2026, 10, 9), hist, gap)
    print("arm a: SALXX@2026-10-12 frontier=" + str(f) + " windows=" + str(w))
    if f != dt.date(2026, 10, 9) or w != exp or w.get("1D") is None:
        bad.append("a:SALXX@10-12 frontier=" + str(f) + " windows=" + str(w))

    # b: the 4-day bound
    hb = hist[~((hist["tkr"] == "SALXX") & (hist["date"] > dt.date(2026, 10, 7)))]
    w, f = fr("SALXX", dt.date(2026, 10, 12), hb, gap)
    print("arm b: SALXX@2026-10-12 with rows after 10-07 removed frontier=" + str(f))
    if f is not None or any(v is not None for v in w.values()):
        bad.append("b:bound not applied frontier=" + str(f))

    # c: absent_count > 0 blocks the carry
    gc = copy.deepcopy(gap)
    gc["securities"]["SALXX"]["absent_count"] = 1
    w, f = fr("SALXX", dt.date(2026, 10, 12), hist, gc)
    print("arm c: SALXX@2026-10-12 with absent_count=1 frontier=" + str(f))
    if f is not None or any(v is not None for v in w.values()):
        bad.append("c:absent_count>0 still carried frontier=" + str(f))

    # d: a NULL reading ON as_of stays blank
    w, f = fr("FXFXX", dt.date(2026, 10, 12), hist, gap)
    print("arm d: FXFXX@2026-10-12 frontier=" + str(f) + " windows=" + str(w))
    if f != dt.date(2026, 10, 12) or any(v is not None for v in w.values()):
        bad.append("d:FXFXX NULL reading not blank frontier=" + str(f))

    if bad:
        print("CM-REAL-BAD " + "; ".join(bad))
        return 1
    print("CM-REAL-OK D=" + D.isoformat() + " session_equal=" + str(same) + " moved=" + str(len(moved)) + " arms=a,b,c,d,e")
    return 0


if __name__ == "__main__":
    sys.exit(main())
