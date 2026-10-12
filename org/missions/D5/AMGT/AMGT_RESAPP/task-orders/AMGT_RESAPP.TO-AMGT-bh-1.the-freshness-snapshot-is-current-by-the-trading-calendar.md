# AMGT_RESAPP task order -- `AMGT-bh-1` -- THE /freshness SNAPSHOT IS CURRENT BY THE TRADING CALENDAR, NOT BY A 24-HOUR CLOCK (A BUILD, NOT YET SERVED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bh-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~398</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bh-1.the-freshness-snapshot-is-current-by-the-trading-calendar</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one module, no schedule is changed (the writer stays cron MON-FRI 12:30 UTC).
comp-iam: DECLARED-NOT-APPLICABLE -- the checks are offline (a stub client, an injected clock); no AWS call.
comp-adversary: RUN at the cut, each ARM AGAINST THE LITERAL STRING WRITTEN BELOW: at the base, r101_snapshot_rule_check.py reads 'arms passed 7 of 11 ... R101 SNAPSHOT RULE: NO' (A1, A2, A3 and A7a FAIL: a Friday snapshot is refused on the weekend and a holiday Monday) and exits 1; the pytest line reads an error (the new test module is absent). Against a throwaway candidate built in a scratch worktree from the edit below: r101_snapshot_rule_check.py reads 11 of 11 / YES (exit 0), and `pytest test_freshness_snapshot.py test_freshness_snapshot_calendar.py` reads 24 passed (the 18 existing and the 6 new).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-398` (branch `wk-AMGT_RESAPP-398`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-398`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bh-1` (round 101, decomposition s.109)

CTO~DELL1 round-100 analysis ADDENDUM 1 (msg 4292): "the snapshot is fresh when written after the latest trading day's scheduled write (lib/trading_calendar T-1), so Friday's covers the
weekend and holidays; 72 h fails three-day weekends and a daily cron writes identical data." The writer is `cron(30 12 ? * MON-FRI *)`; the reader `read_freshness_snapshot` refuses a snapshot
older than 24 hours, so from Saturday 12:30Z to Monday 12:30Z every overlay request after the 60-second hold recomputes the whole coverage view live (4 to 5 s locally, 22 to 28 s on the
live function). Make exactly these edits (the files are LF; ASCII only).

### 1. `lib/research/freshness/snapshot.py`

(a) After the line `MAX_AGE_HOURS = 24.0` add:

    # AMGT-bh-1: the writer is `cron(30 12 ? * MON-FRI *)` (infra/aws/terraform/harvest/freshness-snapshot-schedule.tf). A snapshot is CURRENT
    # when it was written at or after the scheduled write of the latest trading day whose write time has passed (lib.trading_calendar), so
    # Friday's snapshot covers the weekend and a holiday Monday and a weekday past its write with no new snapshot is not current. A calendar
    # that cannot answer leaves the MAX_AGE_HOURS rule above in force.
    WRITE_HOUR_UTC = 12
    WRITE_MINUTE_UTC = 30

(b) Immediately before `def read_freshness_snapshot(` add:

    def latest_scheduled_write(now: datetime.datetime) -> Optional[datetime.datetime]:
        """12:30 UTC of the latest trading day whose 12:30 has passed at `now` (naive UTC); None when the trading calendar cannot say."""
        try:
            from lib import trading_calendar

            day = now.date()
            for _ in range(14):
                at = datetime.datetime.combine(day, datetime.time(WRITE_HOUR_UTC, WRITE_MINUTE_UTC))
                if trading_calendar.is_trading_day(day) and at <= now:
                    return at
                day = day - datetime.timedelta(days=1)
        except Exception:  # noqa: BLE001 -- a calendar that cannot answer leaves the 24-hour rule
            return None
        return None

(c) In the docstring of `read_freshness_snapshot` replace the tail `` `generated_at` is within `max_age_hours` (24, one trading day); `record["age_hours"]` carries its age.""" ``
with:

    `generated_at` is at or after the latest trading day's scheduled write (`latest_scheduled_write`), or within `max_age_hours`
    (24) where the calendar cannot say; `record["age_hours"]` carries its age."""

(d) Replace the final block of `read_freshness_snapshot` -- today:

        if age > max_age_hours:
            record["reason"] = ("the stored snapshot is {0:.1f} hours old, past the {1:g} hour limit".format(age, max_age_hours))
            return None, record
        return document, record

with:

        moment = now or datetime.datetime.utcnow()
        since = latest_scheduled_write(moment)
        if since is not None:
            generated = None
            for form in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%MZ"):
                try:
                    generated = datetime.datetime.strptime(str(record["generated_at"]).strip(), form)
                    break
                except ValueError:
                    continue
            record["required_since"] = since.strftime("%Y-%m-%dT%H:%MZ")
            if generated is None or generated < since:
                record["reason"] = ("the stored snapshot ({0}) is older than the latest scheduled write ({1})".format(
                    record["generated_at"], record["required_since"]))
                return None, record
            return document, record
        if age > max_age_hours:
            record["reason"] = ("the stored snapshot is {0:.1f} hours old, past the {1:g} hour limit".format(age, max_age_hours))
            return None, record
        return document, record

### 2. `lib/research/api/tests/test_freshness_snapshot.py`

The existing tests state the 24-HOUR reading of "current" against the wall clock, which the calendar rule makes clock-dependent. In `_setup(monkeypatch, with_snapshot)` add, directly after
`served_cache.clear()`:

    # AMGT-bh-1: these tests state the 24-HOUR reading of "current" against the wall clock; the trading-calendar rule has its own
    # tests (test_freshness_snapshot_calendar.py) with an injected `now`, so the calendar is held out here.
    monkeypatch.setattr(snapshot, "latest_scheduled_write", lambda now: None)

Nothing else of that file moves.

### 3. NEW `lib/research/api/tests/test_freshness_snapshot_calendar.py`

    """AMGT-bh-1: the /freshness snapshot is current by the TRADING CALENDAR (the writer is cron MON-FRI 12:30 UTC). OFFLINE: a stub client, an injected `now`."""
    import datetime
    import json

    from lib.research.freshness import snapshot


    class _Body:
        def __init__(self, raw):
            self._raw = raw

        def read(self):
            return self._raw


    class _Client:
        def __init__(self, generated_at):
            self._doc = {"rows": [], "generated_at": generated_at}

        def get_object(self, Bucket, Key):  # noqa: N803
            return {"Body": _Body(json.dumps(self._doc).encode("utf-8"))}


    def _served(generated_at, now):
        document, record = snapshot.read_freshness_snapshot(_Client(generated_at), now=datetime.datetime.fromisoformat(now))
        return document is not None, record


    def test_friday_snapshot_covers_the_weekend():
        assert _served("2026-10-09T12:30Z", "2026-10-11T15:00:00")[0] is True
        assert _served("2026-10-09T12:30Z", "2026-10-12T11:00:00")[0] is True


    def test_a_weekday_past_its_write_without_a_new_snapshot_is_not_current():
        got, record = _served("2026-10-09T12:30Z", "2026-10-12T13:00:00")
        assert got is False
        assert "latest scheduled write" in record["reason"] and record["required_since"] == "2026-10-12T12:30Z"


    def test_a_same_day_snapshot_is_current_until_the_next_write():
        assert _served("2026-10-12T12:30Z", "2026-10-12T15:00:00")[0] is True
        assert _served("2026-10-12T12:30Z", "2026-10-13T12:00:00")[0] is True
        assert _served("2026-10-12T12:30Z", "2026-10-13T13:00:00")[0] is False


    def test_a_holiday_monday_is_covered_by_fridays_snapshot():
        assert _served("2026-09-04T12:30Z", "2026-09-08T11:00:00")[0] is True
        assert _served("2026-09-04T12:30Z", "2026-09-08T13:00:00")[0] is False


    def test_a_snapshot_with_no_readable_time_is_not_served():
        got, record = _served("not a time", "2026-10-12T13:00:00")
        assert got is False and "does not say when it was made" in record["reason"]


    def test_a_calendar_that_cannot_answer_leaves_the_24_hour_rule(monkeypatch):
        monkeypatch.setattr(snapshot, "latest_scheduled_write", lambda now: None)
        assert _served("2026-10-12T08:00Z", "2026-10-12T12:00:00")[0] is True
        assert _served("2026-10-10T08:00Z", "2026-10-12T12:00:00")[0] is False

Nothing else moves: no schedule, no writer, no other module, no other test.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W398-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Edit only `lib/research/freshness/snapshot.py` and `lib/research/api/tests/test_freshness_snapshot.py`, and add only `lib/research/api/tests/test_freshness_snapshot_calendar.py`; no other file.
2. No deploy, no store write, no schedule change, no Bloomberg, SEC or model call; no S3 write or delete. The checks are offline.
3. No `bun`, `npm` or `pip install`.
4. Standing: no push of shared branches.
5. The check scripts are the issuer's and read-only: do not edit them; run them as the criteria name.

## 3. SURFACES

<paths>
lib/research/freshness/snapshot.py
lib/research/api/tests/test_freshness_snapshot.py
lib/research/api/tests/test_freshness_snapshot_calendar.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~398/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bh-1"><invocation>cd C:/dev/wk-resapp-398 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round101_prep/checks/r101_snapshot_rule_check.py" | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last two lines read `   arms passed 11 of 11` and `R101 SNAPSHOT RULE: YES`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bh-1"><invocation>cd C:/dev/wk-resapp-398 &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests/test_freshness_snapshot.py lib/research/api/tests/test_freshness_snapshot_calendar.py -q | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last line reads `24 passed` (the 18 existing tests and the 6 new, ANSI colour codes and a warnings count aside); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~398 <0.9.0_WK_AMGT_RESAPP~398@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Write any python or multi-line file with the Write tool. Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~398/AMGT_RESAPP.TO-AMGT-bh-1.the-freshness-snapshot-is-current-by-the-trading-calendar.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- every criterion's output lines (copy each invocation from the order file, never retype it);
- the diff of `snapshot.py` in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-100 analysis ADDENDUM 1 (msg 4292): "(b) yes, by the trading calendar, not cron-daily or 72 h ... Under its own pair, arms: a weekend clock serves the snapshot; a weekday clock past the write with no new snapshot recomputes; bytes equal to the live recompute." This order is the build and the first two arms (A1/A2 and A3/A6 of the rule check); the third arm (bytes equal to the live recompute) is `r101_snapshot_equal.py`, graded on the live pool after Monday 2026-10-12 12:30Z by `AMGT-bh-3` and again at `AMGT-bh-2`'s pair. READ at the cut: the live snapshot is 65 hours old (generated 2026-10-09T12:30Z); with the stored snapshot served in a fresh process, the cold ASML_NA overlay reads 5.8 s against 8.7 s locally; both slow days of rounds 98 to 99 were weekend. The existing 24-hour tests were clock-dependent under the new rule (a snapshot aged 30 hours is current at Monday 06:50Z): the calendar is held out of them and the new rule has its own tests with an injected `now`. The schedule (cron MON-FRI) is unchanged: a weekday holiday still writes, harmlessly.

<status>complete -- 2026-10-12T0xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-398 @20f66b792f merged @7da642c1ff, proof instance VALID; the build is MERGED, NOT SERVED (it reaches the function only through AMGT-bh-2's pair, after AMGT-bh-3's read). Issuer re-run on the merged tree: AC1 `arms passed 11 of 11` / `R101 SNAPSHOT RULE: YES` (exit 0; the base reads 7 of 11, exit 1), AC2 24 passed (the 18 existing and the 6 new). The diff is the order's edit exactly (snapshot.py +41 -1, the existing test module +3, the new calendar test module +59). snapshot.py blob 64fa354a1e1c at 7da642c1ff.</status>
<round>101</round>
<slot>0.9.0_WK_AMGT_RESAPP~398</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
