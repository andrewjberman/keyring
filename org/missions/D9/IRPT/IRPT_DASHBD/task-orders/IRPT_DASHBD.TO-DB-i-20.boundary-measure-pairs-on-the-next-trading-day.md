# TO IRPT_DASHBD.TO-DB-i-20 -- the boundary measure pairs each landed day with the next TRADING day (lib/trading_calendar.py), not the next calendar day; tests built on the feed's own writer for a Friday-to-Monday pair and a holiday-eve pair

<to_id>IRPT_DASHBD.TO-DB-i-20</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~320</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>133</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_132_20261019.md` @14e06e4b55 (msg 10703), ruling 1 and enrichment E1: "The boundary pairs on the next TRADING day, from `lib/trading_calendar.py`. A weekend or holiday is not a missing boundary", with "a test that a Friday pairs with the Monday and a holiday-eve with the next open day".

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-320`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~320/`. Never touch a path outside the `<paths>` block below.

**Why.** `measure_boundary` in `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/run_scope_feed_real.py` compares a landed day's end value with the NEXT CALENDAR day's start value (`_next_day`, day + 1). The Scope feed writes the weekend rows ABSENT when the series has no point on them, so the Friday's end value is never compared with the Monday's start value, and a holiday-eve is never compared with the next open day: about one boundary in five goes unmeasured. The measure must pair each landed day with the next TRADING day, taken from `lib/trading_calendar.py`.

**Read first (read only, except where a step below says you edit).**
- `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/run_scope_feed_real.py` (`measure_boundary`, `_next_day`, `run_real`, `chain_check`): the file you edit.
- `lib/trading_calendar.py` (`first_trading_day_on_or_after`, `is_trading_day`, `trading_days_between`; it prints a one-line WARN that it answers from its hardcoded NYSE table: that is expected).
- `data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_real_shape.py` (the file you add tests to; 9 tests today) and the feed's own harness it uses, `data/inf/manual_api/test_scope_feed_daily_factor.py` (`_fixture_s3`, `_run(s3, responses, pull_date=...)`, `_response`, `_group`, `_point`): read only, never edit.
- The checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r133/p133_boundary.py`: its two parts ARE the specification. Read it first and run `python -I <it> --selftest`.

**The cell (`DB-i-20`).**
1. **The module change** (in `run_scope_feed_real.py`, the one module edit of this cell):
   - Add `next_trading_day(day_iso)`: the ISO day of the first trading day STRICTLY after `day_iso` per `lib/trading_calendar.py` (`tc.first_trading_day_on_or_after(day + 1 day)`), or `None` when the calendar finds none. Do not write a weekday helper of your own: weekends AND market holidays come from the library.
   - Change the header to `measure_boundary(silver, next_day=None)`. `next_day(day_iso) -> ISO day or None` chooses a row's partner day; `None` means `next_trading_day`. Every other rule is unchanged: a pair is a RETURNED row of an account on day d with a non-null `end_market_value` and a RETURNED row of the SAME account on the partner day with a non-null `start_market_value`; `diff = |end(d) - start(partner)|`, equal when `diff <= 0.005`, the relative difference in basis points as now, `max_rel_diff_bp` None with no pairs.
   - `run_real` keeps its exact parameter list and uses the default. Update the two docstrings that say `d + 1` (the module's and `measure_boundary`'s). Leave the chain check alone.
2. **The tests** (added to `test_inflection_scope_feed_real_shape.py`; the 9 existing tests stay and pass). At least three new tests whose names contain `boundary`:
   - one naming `friday` and `monday`: partitions written by the FEED'S OWN `run()` through its harness, in TWO runs on one fake S3 (first `pull_date` = a Friday with a series point on that Friday; then `pull_date` = the following Monday with a series point on that Monday; the second run's window starts after the Friday, so the Saturday and Sunday rows are written ABSENT). Assert `measure_boundary` finds 1 pair with a max relative difference of 1000.0 basis points (the harness's start value 100 against end value 110), and that `run_real` over the same partitions (through the file's existing fake reader) reports `boundary.pairs` 1;
   - one naming `holiday`: a Tuesday run and a Thursday run (a point on each), with a calendar double passed as `next_day=` that treats the Wednesday between them as a closed day: 1 pair;
   - one named `...mutant...`: the SAME frames as the Friday-Monday test with `next_day=` the old calendar rule (day + 1) must find `== 0` pairs.
   Also assert `next_trading_day` for a Friday (the Monday) and for the day before the observed July market holiday (the next open Monday). Build NO feed frame by hand: every frame comes from the feed's `run()` through its harness (no `pd.DataFrame([` for feed rows).
3. **Do not touch** the harness, the wrapper, the adapter, the feed script, `lib/`, or any other module. If the harness cannot make a scenario above, that is a result: report it with a surprise row, do not hand-shape a frame.

<criterion id="DBI133-1-AC1" cell_refs="DB-i-20"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r133/p133_boundary.py" . DBI133-1-AC1</invocation><expect>DBI133-1-AC1 PASS</expect></criterion>
`DBI133-1-AC1` -- the behaviour, graded on partitions the checker writes with the feed's own `run()`: a Friday pairs with the Monday (1 pair, 1000.0 basis points) and the calendar rule on the same frames finds 0; a Monday that is not RETURNED is not paired; a holiday-eve pairs with the next open day under a calendar double; an ordinary Tuesday still pairs with the Wednesday; `next_trading_day` answers the real holiday table; `run_real` keeps its signature and counts the Friday-to-Monday pair. Base: FAIL (no `next_trading_day`).

<criterion id="DBI133-1-AC2" cell_refs="DB-i-20"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r133/p133_boundary.py" . DBI133-1-AC2</invocation><expect>DBI133-1-AC2 PASS</expect></criterion>
`DBI133-1-AC2` -- the tests: at least three tests named `*boundary*` (one naming Friday and Monday, one naming a holiday, one named `*mutant*` that passes the calendar rule as `next_day=` and asserts 0 pairs), the boundary tests call `measure_boundary` and drive the feed's `run()`, no hand-built feed frame, and the file passes with at least 12 tests. Base: FAIL (fewer than three boundary tests).

<expected_criteria>DBI133-1-AC1, DBI133-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the harness, the wrapper, the adapter, the feed script, `lib/`, `infra/` and every issuer check.
- **No AWS, no network, no vendor call, no secret, no push, no deploy.** The feed's harness runs offline against its own fake S3 and fake transport.
- **No client data.** Every account and value in a fixture is the harness's synthetic one.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W320-S<k>`, `surfaced_at` from `date -u +%FT%TZ` at filing; append as BYTES. Commit with `.tools/safe-commit.sh`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~320/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/run_scope_feed_real.py
data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_real_shape.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-20.boundary-measure-pairs-on-the-next-trading-day.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 19, cell `DB-i-20`.
<owned_cells>DB-i-20</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI133-1-AC1, DBI133-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~320/IRPT_DASHBD.TO-DB-i-20.boundary-measure-pairs-on-the-next-trading-day.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI133-1-AC1 DBI133-1-AC2` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the files you changed; the number of tests in the file and how many are new; the pair count and basis-point value the Friday-to-Monday test asserts; row ids. No token, no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one local module edit and a test file; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; the feed's harness runs against its own fake S3.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; AC1 and AC2 FAIL at base, and the checker's self-test feeds a reference module (PASS) and four mutants (the default stays calendar d+1; weekends only with no holidays; the partner is the day itself; the next_day argument ignored), each FAIL, plus a reference test file (PASS) and five mutants (no holiday test, no mutant test, fewer than 12 tests, a failing test, a hand-built feed frame), each FAIL.
</preflight>
