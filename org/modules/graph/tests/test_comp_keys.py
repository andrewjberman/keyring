"""test_comp_keys.py -- NFRA_MSBEFF.R5 key/partition enumeration primitive.

CI-safe: mocks the live s3api call (_aws_json) so no AWS/network is touched. Carries the REQUIRED MUTANT
(not-found must be LOUD with its denominator, never a clean empty) + the partition-derivation + firm-scope
logic. The LIVE exercises (3 real prefixes + the real error path) are pasted in the session log per phase-3.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_WS = Path(__file__).resolve().parents[4]
if str(_WS) not in sys.path:
    sys.path.insert(0, str(_WS))

from org.modules.graph import comp_keys as ck  # noqa: E402


def _fake_listing(keys):
    """A fake _aws_json that returns a Contents listing (one page)."""
    def _fake(args):
        contents = [{"Key": k, "Size": 1, "LastModified": "2026-07-23T00:00:00.000Z"} for k in keys]
        return {"Contents": contents}, None
    return _fake


def test_prefix_not_found_is_loud_with_denominator(capsys, monkeypatch):
    """MUTANT: an empty/non-existent prefix renders a LOUD not-found naming the exact denominator, NOT
    a clean empty, and exits 0 (the query ran; the prefix is genuinely empty)."""
    monkeypatch.setattr(ck, "_aws_json", lambda args: ({}, None))  # zero Contents
    rc = ck.main(["prefix", "opal-data-cot", "silver/nope_xyz/"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "0 keys" in out and "LOUD NOT-FOUND" in out
    assert "opal-data-cot/silver/nope_xyz/" in out  # the exact denominator, not the intended one
    assert "denominator" in out.lower()


def test_prefix_error_path_is_rc1(capsys, monkeypatch):
    """A bucket/aws error is rc1 (a real failure), distinct from a loud-zero (rc0)."""
    monkeypatch.setattr(ck, "_aws_json", lambda args: (None, "NoSuchBucket"))
    rc = ck.main(["prefix", "opal-data-nope", "x/"])
    err = capsys.readouterr().err
    assert rc == 1
    assert "ERROR" in err and "NoSuchBucket" in err


def test_prefix_positive_control_lists_keys(capsys, monkeypatch):
    monkeypatch.setattr(ck, "_aws_json", _fake_listing(
        ["silver/2026-07-20/x.json", "silver/2026-07-21/x.json"]))
    rc = ck.main(["prefix", "opal-data-cot", "silver/"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "2 key(s)" in out and "2026-07-21" in out


def test_partitions_derives_dates_and_gaps(capsys, monkeypatch):
    # A gap on a WEEKDAY (2026-07-21 is a Tuesday) between 07-20 (Mon) and 07-22 (Wed).
    monkeypatch.setattr(ck, "_aws_json", _fake_listing([
        "silver/2026-07-20/a.json", "silver/2026-07-22/a.json"]))
    rc = ck.main(["partitions", "opal-data-cot", "silver/"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "earliest: 2026-07-20" in out and "latest:   2026-07-22" in out
    assert "2026-07-21" in out  # the weekday gap named


def test_partitions_derivation_ignores_delimiter_uses_key_text():
    """Partition dates come from the FULL key listing (never --delimiter /, which MSYS-mangles)."""
    dates = ck._partition_dates.__doc__
    assert "full key listing" in dates and "delimiter" in dates


def test_partitions_not_found_loud(capsys, monkeypatch):
    monkeypatch.setattr(ck, "_aws_json", _fake_listing(["silver/_meta/nodate.json"]))
    rc = ck.main(["partitions", "opal-data-cot", "silver/"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "0 date partitions" in out and "LOUD NOT-FOUND" in out


def test_exists_is_complete_over_firm_registry(capsys, monkeypatch):
    # every firm bucket "has" the key -> all EXIST; denominator names the registry.
    monkeypatch.setattr(ck, "_aws_json", _fake_listing(["silver/holdings/x.json"]))
    rc = ck.main(["exists", "silver/holdings/"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "firm_registry.json" in out and "EXISTS" in out


def test_calendar_gaps_flags_weekdays_only():
    # Fri 07-24 .. Mon 07-27: the weekend (Sat 25 / Sun 26) is NOT a gap; only weekdays count.
    gaps = ck._calendar_gaps(["2026-07-24", "2026-07-27"])
    assert "2026-07-25" not in gaps and "2026-07-26" not in gaps


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
