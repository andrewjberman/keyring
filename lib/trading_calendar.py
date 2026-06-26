"""Shared NYSE trading-day calendar -- the ONE definition of "trading day" / "expected
priced frontier" / "trading days behind" for the whole estate.

Convergence (3.0.0_SA_CVO 2026-06-26, CTO arch-gated): this logic was COPIED inline across
5+ places (bd-49f-freshness-probe, bd-cot-freshness-probe, mdpf-daily-trigger, mdpf-freshness-
checker, + the mdpf-local data/mdpf/scripts/gold/_trading_day_calendar.py) and comp-freshness
content-mode was about to add a 6th (flat-hours) definition. N definitions of "stale" CAN
drift = the gate-green-above-grounding disease at its definitional root. This is the single
source all consumers import: the freshness probes + comp-freshness + COO's served-aua-stale
alarm all agree on "stale" because they share THIS file.

Design (takes the mdpf module's pmc-with-fallback shape -- the best of the copies):
  - Canonical source = NYSE schedule via `pandas_market_calendars` WHEN AVAILABLE.
  - Hardcoded NYSE-holiday FALLBACK (2024-2027) when pmc is absent (the CLI + lambdas that
    don't vendor pmc) -- defense-in-depth, verified against the published NYSE schedule.
  - NO AWS deps; pmc import is OPTIONAL (try/except) -> importable by lambdas (vendored at
    package) AND the local comp-freshness CLI (imported directly). lib/ convention: see
    lib/README.md. FIRM-SEP: a NYSE calendar is a PUBLIC-MARKET primitive, not firm data --
    CTO-blessed cross-firm import (not a firm-data grant).

Public API:
  is_trading_day(date) -> bool
  prev_trading_day(date) -> date
  expected_last_trading_day(now) -> date          # the "expected last-settled priced frontier"
  trading_days_behind(as_of, expected) -> int     # the lag (trading-day count, not flat hours)
  trading_days_between(start, end) -> list[date]   # inclusive
  trading_days_mtd / trading_days_ytd / total_trading_days_in_window
  calendar_source() -> str                         # provenance

Date inputs accept datetime.date, datetime.datetime, or ISO-8601 string.

Refresh NYSE_HOLIDAYS_FALLBACK before 2028 (extend the set when a new year enters scope).
"""
from __future__ import annotations

import datetime as dt

try:
    import pandas_market_calendars as _pmc  # type: ignore[import-not-found]
    _NYSE = _pmc.get_calendar("NYSE")
    _USE_PMC = True
except ImportError:
    _NYSE = None
    _USE_PMC = False

# NYSE official market closures 2024-2027. Verified against the NYSE published holiday
# schedule + pandas_market_calendars NYSE output. UNION of the prior copies (mdpf 2024-2026
# + the freshness probes' 2026-2027). Extend when a new year enters scope (refresh before 2028).
NYSE_HOLIDAYS_FALLBACK: frozenset[str] = frozenset({
    # 2024 -- New Year, MLK, Presidents, Good Friday, Memorial, Juneteenth, July 4, Labor,
    # Thanksgiving, Christmas.
    "2024-01-01", "2024-01-15", "2024-02-19", "2024-03-29", "2024-05-27",
    "2024-06-19", "2024-07-04", "2024-09-02", "2024-11-28", "2024-12-25",
    # 2025 -- + Jan 9 day of mourning for former President Carter.
    "2025-01-01", "2025-01-09", "2025-01-20", "2025-02-17", "2025-04-18",
    "2025-05-26", "2025-06-19", "2025-07-04", "2025-09-01", "2025-11-27",
    "2025-12-25",
    # 2026 -- July 4 falls on Saturday -> NYSE observes Friday July 3.
    "2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25",
    "2026-06-19", "2026-07-03", "2026-09-07", "2026-11-26", "2026-12-25",
    # 2027 -- Juneteenth (Sat) observed Fri 6/18; July 4 (Sun) observed Mon 7/5; Christmas
    # (Sat) observed Fri 12/24.
    "2027-01-01", "2027-01-18", "2027-02-15", "2027-03-26", "2027-05-31",
    "2027-06-18", "2027-07-05", "2027-09-06", "2027-11-25", "2027-12-24",
})

# Back-compat alias for the mdpf-local module's name (so its re-export is a clean rename).
_NYSE_HOLIDAYS_FALLBACK = NYSE_HOLIDAYS_FALLBACK


def _to_date(d: object) -> dt.date:
    if isinstance(d, dt.datetime):
        return d.date()
    if isinstance(d, dt.date):
        return d
    if isinstance(d, str):
        return dt.date.fromisoformat(d[:10])
    raise TypeError(f"unsupported date type: {type(d)!r}")


def is_trading_day(date: object) -> bool:
    """True iff `date` is a NYSE trading day (weekday + not a NYSE holiday)."""
    d = _to_date(date)
    if d.weekday() >= 5:
        return False
    if _USE_PMC:
        assert _NYSE is not None
        sched = _NYSE.valid_days(start_date=d.isoformat(), end_date=d.isoformat())
        return len(sched) == 1
    return d.isoformat() not in NYSE_HOLIDAYS_FALLBACK


def prev_trading_day(date: object) -> dt.date:
    """The NYSE trading day strictly before `date`."""
    c = _to_date(date) - dt.timedelta(days=1)
    while not is_trading_day(c):
        c -= dt.timedelta(days=1)
    return c


def expected_last_trading_day(now: object) -> dt.date:
    """The expected last-SETTLED priced frontier as of `now`: today if today is a trading
    day, else the prior trading day. (Data priced T+1 should be at-or-after this date.)"""
    today = _to_date(now)
    return today if is_trading_day(today) else prev_trading_day(today)


def trading_days_behind(as_of: object, expected: object) -> int:
    """Trading days strictly after `as_of`, up to and including `expected` (0 if caught up).
    The frontier-aware staleness metric: 0 = at frontier, 1 = one trading day behind, etc."""
    a = _to_date(as_of)
    e = _to_date(expected)
    if a >= e:
        return 0
    n, c = 0, e
    while c > a:
        if is_trading_day(c):
            n += 1
        c -= dt.timedelta(days=1)
    return n


def trading_days_between(start: object, end: object) -> list[dt.date]:
    """Inclusive list of NYSE trading days between `start` and `end`."""
    s = _to_date(start)
    e = _to_date(end)
    if s > e:
        return []
    if _USE_PMC:
        assert _NYSE is not None
        days = _NYSE.valid_days(start_date=s.isoformat(), end_date=e.isoformat())
        return [d.date() if hasattr(d, "date") else d for d in days]
    out: list[dt.date] = []
    cur = s
    one_day = dt.timedelta(days=1)
    while cur <= e:
        if is_trading_day(cur):
            out.append(cur)
        cur += one_day
    return out


def trading_days_mtd(date: object) -> list[dt.date]:
    """NYSE trading days from the 1st of `date.month` through `date` inclusive."""
    d = _to_date(date)
    return trading_days_between(dt.date(d.year, d.month, 1), d)


def trading_days_ytd(date: object) -> list[dt.date]:
    """NYSE trading days from Jan 1 of `date.year` through `date` inclusive."""
    d = _to_date(date)
    return trading_days_between(dt.date(d.year, 1, 1), d)


def total_trading_days_in_window(start: object, end: object) -> int:
    """Count of NYSE trading days in `[start, end]` inclusive."""
    return len(trading_days_between(start, end))


def calendar_source() -> str:
    """Provenance string for an artifact's `trading_day_calendar` field."""
    return ("NYSE/pandas_market_calendars" if _USE_PMC
            else "NYSE/hardcoded-fallback-2024-2027")
