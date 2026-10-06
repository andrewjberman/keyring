#!/usr/bin/env python3
"""Offline battery: the WEEKLY trading-day-frontier basis in `.tools/comp-freshness` (NFRA_MCPINDEX MX-f-1,
CTO ruling Z-S74) and `lib/trading_calendar.weekly_production_day`.

No AWS, no held-config read: every entry is a fixture dict or a fixture YAML in a temp dir, fed to the PURE
`_evaluate_artifact`. COMP_FRESHNESS_PIPELINE is never set here (and is removed from the environment for the
test) -- the sovereign hold on data/black_diamond/ configs is untouched.

Arms (producer weekday = sunday, the measured BD weekday; 2026-09-27 is a Sunday):
  FRESH   -- every day after the weekly run landed, up to and including the next production day itself
  STALE   -- only once the next production day is PAST with no write on/after it
  CONTROL -- a last write one week past reads STALE
  DAILY   -- a daily entry's flat-hours grading is unchanged (and a weekly entry with no declared weekday too)
  ROLL    -- a Mon-Fri holiday production day rolls back per the calendar
"""
from __future__ import annotations

import datetime as dt
import importlib.machinery
import importlib.util
import os
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "lib"))
import trading_calendar as tcal  # noqa: E402


def _load_cf():
    loader = importlib.machinery.SourceFileLoader("comp_freshness_under_test", str(ROOT / ".tools" / "comp-freshness"))
    spec = importlib.util.spec_from_loader("comp_freshness_under_test", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def cf():
    os.environ.pop("COMP_FRESHNESS_PIPELINE", None)
    return _load_cf()


def utc(y, m, d, hh=0, mm=0):
    return dt.datetime(y, m, d, hh, mm, tzinfo=dt.timezone.utc)


def weekly(weekday="sunday", **kw):
    e = {"artifact_id": "fx_weekly", "s3_key_prefix": "s3://fixture-bucket/silver/fx/", "cadence": "weekly",
         "freshness_basis": "trading-day-frontier", "weekly_production_weekday": weekday,
         "warn_age_hours": 30, "fail_age_hours": 48, "severity": "ERROR"}
    e.update(kw)
    return e


SUN_WRITE = utc(2026, 9, 27, 0, 14)   # the measured production write: Sunday 00:14Z


def status(cf, entry, now, lm):
    return cf._evaluate_artifact(entry, now, lm)["status"]


# ---- FRESH: every day after the weekly producer ran ----------------------------------------------------------------
@pytest.mark.parametrize("now", [
    utc(2026, 9, 27, 6, 0),    # Sunday, hours after the write
    utc(2026, 9, 28, 12, 0),   # Monday
    utc(2026, 9, 30, 12, 0),   # Wednesday -- flat 48h would already FAIL here
    utc(2026, 10, 3, 23, 0),   # Saturday, the day before the next production day
    utc(2026, 10, 4, 0, 5),    # next production day itself, before its run lands: not yet past
])
def test_fresh_after_the_weekly_run(cf, now):
    assert status(cf, weekly(), now, SUN_WRITE) == "PASS"


def test_flat_hours_would_have_failed_midweek(cf):
    """The contrast that justifies the rule: the same Wednesday read under the old daily/flat entry FAILs."""
    flat = {"artifact_id": "fx_flat", "s3_key_prefix": "s3://fixture-bucket/silver/fx/", "cadence": "daily",
            "warn_age_hours": 30, "fail_age_hours": 48, "severity": "ERROR"}
    assert status(cf, flat, utc(2026, 9, 30, 12, 0), SUN_WRITE) == "FAIL"
    assert status(cf, weekly(), utc(2026, 9, 30, 12, 0), SUN_WRITE) == "PASS"


# ---- STALE: only past the next scheduled weekly production day -----------------------------------------------------
@pytest.mark.parametrize("now", [
    utc(2026, 10, 5, 0, 5),    # Monday after the 10-04 production day, no new write
    utc(2026, 10, 7, 12, 0),
])
def test_stale_only_past_the_next_weekly_production_day(cf, now):
    r = cf._evaluate_artifact(weekly(), now, SUN_WRITE)
    assert r["status"] == "FAIL"
    assert r["weekly_due"] == "2026-10-04"


def test_a_write_on_the_next_production_day_clears_it(cf):
    assert status(cf, weekly(), utc(2026, 10, 5, 12, 0), utc(2026, 10, 4, 0, 20)) == "PASS"


def test_warn_severity_stale_is_warn_not_fail(cf):
    assert status(cf, weekly(severity="WARN"), utc(2026, 10, 7, 12, 0), SUN_WRITE) == "WARN"


# ---- positive control: a last write one week past reads STALE ------------------------------------------------------
def test_one_week_past_control_reads_stale(cf):
    now = utc(2026, 10, 5, 12, 0)
    assert status(cf, weekly(), now, now - dt.timedelta(days=7)) == "FAIL"
    # and the same table written inside the week is fresh -- the control discriminates
    assert status(cf, weekly(), now, now - dt.timedelta(days=1)) == "PASS"


# ---- daily grading unchanged ---------------------------------------------------------------------------------------
def _daily(**kw):
    e = {"artifact_id": "fx_daily", "s3_key_prefix": "s3://fixture-bucket/silver/dx/", "cadence": "daily",
         "warn_age_hours": 30, "fail_age_hours": 48, "severity": "ERROR"}
    e.update(kw)
    return e


def test_daily_entry_grading_is_unchanged(cf):
    now = utc(2026, 9, 30, 12, 0)
    assert status(cf, _daily(), now, now - dt.timedelta(hours=10)) == "PASS"
    assert status(cf, _daily(), now, now - dt.timedelta(hours=35)) == "WARN"
    assert status(cf, _daily(), now, now - dt.timedelta(hours=50)) == "FAIL"
    # even a daily entry that carries a weekday key is graded flat: the branch needs cadence: weekly
    d = _daily(freshness_basis="trading-day-frontier", weekly_production_weekday="sunday")
    assert status(cf, d, now, now - dt.timedelta(hours=50)) == "FAIL"
    assert "weekly_due" not in cf._evaluate_artifact(d, now, now - dt.timedelta(hours=50))


def test_weekly_entry_without_a_declared_weekday_is_unchanged(cf):
    now = utc(2026, 9, 30, 12, 0)
    e = weekly()
    del e["weekly_production_weekday"]
    r = cf._evaluate_artifact(e, now, SUN_WRITE)
    assert r["status"] == "FAIL" and "weekly_due" not in r      # flat 48h, exactly as before


# ---- holiday roll + unavailable calendar ---------------------------------------------------------------------------
def test_holiday_production_day_rolls_back(cf):
    # 2026-09-07 (Labor Day) is a Monday; a Monday producer's due day rolls back to Fri 2026-09-04.
    assert tcal.weekly_production_day("2026-09-08", "monday") == dt.date(2026, 9, 4)
    now = utc(2026, 9, 8, 12, 0)
    assert status(cf, weekly("monday"), now, utc(2026, 9, 4, 3, 0)) == "PASS"
    assert status(cf, weekly("monday"), now, utc(2026, 8, 31, 3, 0)) == "FAIL"   # the prior Monday


def test_weekly_production_day_helper(cf):
    f = tcal.weekly_production_day
    assert f("2026-09-27", "sunday") == dt.date(2026, 9, 27)       # on-or-before includes the day itself
    assert f("2026-09-30", 6) == dt.date(2026, 9, 27)
    assert f("2026-09-26", "Sun") == dt.date(2026, 9, 20)
    assert f(dt.datetime(2026, 10, 4, 0, 5), "sunday") == dt.date(2026, 10, 4)
    with pytest.raises(ValueError):
        f("2026-09-27", "funday")


def test_missing_calendar_refuses_rather_than_flat_verdict(cf, monkeypatch):
    monkeypatch.setattr(cf, "_tcal", None)
    r = cf._evaluate_artifact(weekly(), utc(2026, 9, 30, 12, 0), SUN_WRITE)
    assert r["status"] == "UNVERIFIABLE-BASIS"


# ---- fixture CONFIG in a temp dir (the held BD config is never read) -----------------------------------------------
def test_fixture_config_in_a_temp_dir_round_trips(cf, tmp_path):
    cfg = tmp_path / "gold_freshness_config.yaml"
    cfg.write_text(yaml.safe_dump([
        {"artifact_id": "fx_alloc", "s3_key_prefix": "s3://fixture-bucket/silver/allocations/", "cadence": "weekly",
         "freshness_basis": "trading-day-frontier", "weekly_production_weekday": "sunday",
         "warn_age_hours": 30, "fail_age_hours": 48, "severity": "ERROR"},
        {"artifact_id": "fx_daily", "s3_key_prefix": "s3://fixture-bucket/silver/realized/", "cadence": "daily",
         "warn_age_hours": 30, "fail_age_hours": 48, "severity": "ERROR"},
    ]), encoding="utf-8")
    assert not cf._config_is_held(cfg)
    entries = cf._load_config(cfg)
    assert [e["artifact_id"] for e in entries] == ["fx_alloc", "fx_daily"]
    now = utc(2026, 9, 30, 12, 0)
    assert status(cf, entries[0], now, SUN_WRITE) == "PASS"
    assert status(cf, entries[1], now, SUN_WRITE) == "FAIL"
    assert os.environ.get("COMP_FRESHNESS_PIPELINE") != "1"
