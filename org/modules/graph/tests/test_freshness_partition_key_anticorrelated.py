"""NFRA_TOOLCHECK.P4 -- `comp-freshness` partition-key mode. RE-VERDICT: ANTI-CORRELATED.

Owner: 0.4.0_DS_ClientPlatform~B (graph-engine charge, TO 05b2a2c1c section 8).
Lane:  NFRA_TOOLCHECK_P4 -- org/modules/graph/tests/**

TO section 5 ORDERS every seed re-examined against the sharper class before P4 verdicts it,
`comp-freshness (partition-key)` named explicitly. Done. The seed is WRONG IN BOTH DIRECTIONS.

SEED SAID:  "UNDISCRIMINATING -- parses a FILENAME; reads no row, in any mode."
FOUND:
  (a) It does NOT parse the filename. `_DATE_KEY_RE.search(line)` takes the FIRST YYYY-MM-DD
      on an `aws s3 ls` line -- and an `aws s3 ls` line BEGINS with LastModified:
          2026-07-09 21:38:12    1234 2026-07-01.parquet
          ^^^^^^^^^^ returned                ^^^^^^^^^^ the date-key it PROMISES to return
      Its own docstring: "the MAX YYYY-MM-DD parsed from the object FILENAMES (the stamped
      as_of date-key)" ... "the basis is the DATE-KEY (BD's stamped as_of), NEVER MTIME."
      IT READS MTIME. The one thing the docstring swears it never reads.
  (b) "reads no row, in any mode" is FALSE. Content-mode (`as_of_field`) json-loads the doc
      and resolves an internal as-of. The seed accused it of the lesser crime.

WHY `ANTI-CORRELATED`, NOT `UNDISCRIMINATING` (TO section 5's distinction, operational):
      healthy artifact (key == mtime)      -> CORRECT
      plain-stale, never rewritten         -> CORRECT
      THE FROZEN as_of, REWRITTEN DAILY    -> WRONG, and it reads GREEN
                                              ^ the exact failure this mode was implemented
                                                to catch (see _filter_partition_key_entries)
An UNDISCRIMINATING instrument fails a control built from an arbitrary input. THIS ONE PASSES
THAT CONTROL -- it is right on healthy inputs and right on obvious staleness -- and reports
GREEN precisely when the system is broken, BECAUSE THE FAULT DRIVES THE READING: the daily
rewrite that constitutes the freeze is what drags LastModified forward.

    THE TWO DATES COINCIDE EXACTLY WHEN THE PIPELINE IS HEALTHY AND DIVERGE EXACTLY WHEN IT IS
    BROKEN -- AND THE TOOL READS THE WRONG ONE. Its verdict is strongest where it is most wrong.

AND THE FREEZE DETECTOR IS DEAD CODE. `comp-freshness:698` guards on
    result["status"] in ("FAIL","WARN")  AND  mtime_status == "PASS"
and prints "MTIME-FRESH-BUT-PARTITION-STALE ... (stamped-as_of freeze)". Both operands derive
from THE SAME max-LastModified: `age_h = now - last_modified` (:~675), and `stamped_age_h` is
`now - midnight(_max_partition_date(...))` == `now - midnight(last_modified)`. Their difference
is ALWAYS in [0, 24) -- a pure midnight-truncation artifact that a real freeze does not move.
So the guard can fire only when truncation straddles a threshold, i.e. ON A HEALTHY ARTIFACT,
and can NEVER fire on the freeze it names. A correctly-designed detector whose two inputs are
one measurement.

LIVE SCOPE: 5 entries (yaml.safe_load, NOT grep -- `grep -c` says 6; the sixth is a comment,
the same mention-vs-registration error COO made at 033832Z and I then repeated), all under
`data/cot/scripts/gold/gold_freshness_config.yaml`: cot_silver_{holdings, unrealized,
allocations, transactions, realized}. Two are severity=ERROR. cot is a separate firm and IN
SCOPE. No bd/49F/Schwab prefix is read by this fixture, or by me.

NO AWS IS CONTACTED. `_aws` is monkeypatched with recorded `aws s3 ls` line shapes.

WHEN `_max_partition_date` IS FIXED TO READ THE KEY, `test_R1_*` AND `test_freeze_detector_*`
MUST GO RED. That is the acceptance signal, not a regression. Invert them then.
"""
from __future__ import annotations

import datetime
import importlib.machinery
import importlib.util
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
TOOL = REPO / ".tools" / "comp-freshness"
assert TOOL.is_file(), f"repo root misresolved: {REPO}"


def _load():
    """comp-freshness is extensionless; load it by path. Fresh module per call so a
    monkeypatched `_aws` never leaks between tests."""
    ldr = importlib.machinery.SourceFileLoader("comp_freshness_under_test", str(TOOL))
    spec = importlib.util.spec_from_loader(ldr.name, ldr)
    mod = importlib.util.module_from_spec(spec)
    ldr.exec_module(mod)
    return mod


def _max_date(listing: str | None):
    cf = _load()
    cf._aws = lambda *a, **k: listing          # noqa: SLF001 -- the seam under test
    return cf._max_partition_date("s3://opal-data-cot/silver/holdings/")


# Recorded `aws s3 ls <prefix>/` line shape: "<LastModified> <time> <size> <key>"
HEALTHY = "2026-07-09 21:38:12       1234 2026-07-09.parquet"
FREEZE = "2026-07-09 21:38:12       1234 2026-07-01.parquet"   # as_of frozen, rewritten today
STALE = "2026-07-01 03:10:00       1234 2026-07-01.parquet"    # never rewritten
FREEZE_MULTI = ("2026-07-09 21:38:12  1 2026-07-01.parquet\n"
                "2026-07-09 21:38:13  1 2026-06-30.parquet")


def test_R3_positive_healthy_artifact_reads_the_right_date() -> None:
    """A healthy artifact returns the correct date -- BY COINCIDENCE, because key == mtime.
    This GREEN is why nobody noticed. It is also what makes R1's RED evidence."""
    assert _max_date(HEALTHY) == datetime.date(2026, 7, 9)


def test_R3_positive_plain_stale_artifact_reads_the_right_date() -> None:
    """Obvious staleness is caught: nothing rewrote the file, so mtime IS the key."""
    assert _max_date(STALE) == datetime.date(2026, 7, 1)


def test_R1_negative_the_frozen_as_of_returns_MTIME_not_the_date_key() -> None:
    """THE DEFECT. The docstring promises the date-key. It returns LastModified.

    MUST GO RED when `_max_partition_date` is fixed to parse the object key.
    That failure is the acceptance signal for the fix, not a regression.
    """
    got = _max_date(FREEZE)
    assert got == datetime.date(2026, 7, 9), (
        "partition-key mode now returns something other than LastModified -- if it returns "
        "2026-07-01 (the date-key), THE FIX LANDED. Invert this test."
    )
    assert got != datetime.date(2026, 7, 1), "this is the date-key it promised and did not return"


def test_R1_negative_multi_file_freeze_also_returns_MTIME() -> None:
    """Not an artifact of a single line: max over lines is still max-LastModified."""
    assert _max_date(FREEZE_MULTI) == datetime.date(2026, 7, 9)


def test_R2_variance_the_recorder_is_not_a_constant() -> None:
    """R1's wrong answer is evidence only because this recorder CAN return other values.
    It is not stuck; it is reading the wrong column."""
    got = {_max_date(HEALTHY), _max_date(STALE), _max_date(FREEZE)}
    assert len(got) > 1, "recorder returns a constant -- it would be broken, not anti-correlated"
    assert None not in got


def test_it_is_ANTI_CORRELATED_not_UNDISCRIMINATING() -> None:
    """TO section 5's operational distinction, asserted as one proposition.

    UNDISCRIMINATING fails a control built from an arbitrary input.
    ANTI-CORRELATED passes that control and is wrong precisely where the fault lives.
    """
    right_on_healthy = _max_date(HEALTHY) == datetime.date(2026, 7, 9)
    right_on_stale = _max_date(STALE) == datetime.date(2026, 7, 1)
    wrong_on_freeze = _max_date(FREEZE) != datetime.date(2026, 7, 1)

    assert right_on_healthy and right_on_stale, (
        "an arbitrary-input control must PASS -- otherwise the seed's UNDISCRIMINATING stands"
    )
    assert wrong_on_freeze, "it must be wrong on the fault, or it is simply correct"


def test_freeze_detector_branch_cannot_fire_on_a_freeze() -> None:
    """`comp-freshness:698` alarms when the date-key is stale but mtime is fresh.
    Both operands are the same max-LastModified; the key one is merely truncated to midnight.

    Proven here: on the FREEZE listing, `_max_partition_date` returns exactly the mtime's
    DATE. So `stamped_dt == midnight(mtime)` and `stamped_age_h - age_h` is the truncation
    delta, always in [0, 24), and a real freeze moves neither. The guard is dead for its
    stated purpose, and alive only as a false-positive generator near a threshold.
    """
    mtime = datetime.datetime(2026, 7, 9, 21, 38, 12, tzinfo=datetime.timezone.utc)
    assert _max_date(FREEZE) == mtime.date(), "the two operands are no longer one quantity"

    now = datetime.datetime(2026, 7, 10, 3, 40, tzinfo=datetime.timezone.utc)
    age_h = (now - mtime).total_seconds() / 3600.0
    stamped_dt = datetime.datetime(mtime.year, mtime.month, mtime.day,
                                   tzinfo=datetime.timezone.utc)
    stamped_age_h = (now - stamped_dt).total_seconds() / 3600.0

    delta = stamped_age_h - age_h
    assert 0 <= delta < 24, f"truncation delta escaped [0,24): {delta}"
    # ...and it is ENTIRELY truncation: no staleness contributed it.
    assert stamped_age_h > age_h, "stamped age must be the older of the two, by construction"


def test_R5_disclosure_denied_prefix_is_indistinguishable_from_empty() -> None:
    """`_aws(..., check_aws=False)` returns None on ANY failure -- credentials, 403, timeout.
    `_max_partition_date` maps that to None, identical to an empty prefix. The consumer then
    prints "PARTITION-KEY UNCHECKED (no YYYY-MM-DD date-key object under prefix)" --
    NAMING ONE CAUSE FOR TWO CONDITIONS. A denied read is reported as an absent object.

    A gate must NAME WHAT IT SKIPPED, and it must not name the wrong reason (R5, COO 033832Z).
    """
    assert _max_date(None) is None      # aws failed / denied / no credentials
    assert _max_date("") is None        # prefix genuinely empty
    # POSITIVE CONTROL: the recorder CAN return a date, so these Nones are the seam, not a stub.
    assert _max_date(HEALTHY) is not None
