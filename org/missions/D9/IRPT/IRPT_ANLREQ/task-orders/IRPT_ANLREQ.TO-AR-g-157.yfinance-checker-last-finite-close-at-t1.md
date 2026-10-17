# TO-AR-g-157 -- the upload door's yfinance checker judges a symbol by its last FINITE close at or before the T-1 trading day (FWD-7 "yfinance, cut at T-1"; CTO msgs 10112 and 10122): a null newest Yahoo row no longer turns a symbol Yahoo holds into NOT_KEPT

<to_id>IRPT_ANLREQ.TO-AR-g-157</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~280</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>54</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-157` (`decompositions/IRPT_ANLREQ_DECOMP_R54_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none. Order: CTO msgs 10112 and 10122. The failure: r34i's V2 at 00:50Z Saturday read SPY NOT_KEPT `LAST_CLOSE_NOT_FINITE` (22 rows) because Yahoo's NEWEST row had a null close; r34h's V2 had read SPY KEPT earlier.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~280`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-280` (branch `wk-IRPT_ANLREQ-280`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~280 <0.9.0_WK_IRPT_ANLREQ~280@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W280-S<k>` (take the next free `<k>`; check the channel file for `W280` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only in the product file. Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-157`, inlined)

File: `infra/aws/lambda/investor-reporting/intake/yfinance_check.py`, class `YfinanceChecker`. Today `_check_one` (lines 221-237) takes `last = sorted(pairs, ...)[-1]` and reads `close = float(last[1])`: a newest row whose close is NaN gives `NOT_KEPT` with reason `LAST_CLOSE_NOT_FINITE` even when the symbol has a month of good history, and a row dated after the T-1 day (the run's own day, or Friday's row on a Saturday) is read as the answer. FWD-7 says Yahoo is read "cut at T-1". The T-1 day here is the trading-calendar frontier: `lib/trading_calendar.py`, `prev_trading_day(expected_last_trading_day(now))` (Saturday 2026-10-17 gives Thursday 2026-10-15; Tuesday 2026-09-08, the day after Labor Day, gives Friday 2026-09-04; Wednesday 2026-10-14 gives Tuesday 2026-10-13).

1. `import datetime` at the top of the module. `YfinanceChecker.__init__` gains a keyword argument `now=None`; `self.now = now if now is not None else (lambda: datetime.datetime.now(datetime.timezone.utc))`. `now` is a callable returning an aware UTC datetime. Every caller that passes nothing keeps the wall clock.
2. In `_check_one`, inside the existing `try` (so that any calendar error becomes `CHECK_FAILED` through the existing `except Exception`, never `NOT_KEPT`), keep the empty-history branch as it is, then:

        import trading_calendar as tc
        frontier = tc.prev_trading_day(tc.expected_last_trading_day(self.now())).isoformat()
        dated = sorted((p for p in pairs if p[0] <= frontier), key=lambda pair: pair[0])
        if not dated:
            return _result(NOT_KEPT, rows=len(pairs), reason=REASON_NO_ROWS)
        finite = [p for p in dated if math.isfinite(float(p[1]))]
        last = finite[-1] if finite else dated[-1]
        close = float(last[1])

   and leave everything after it (`rows = len(pairs)`, the finite and positive tests, the result) as it is: an only-non-finite history still reads `NOT_KEPT` `LAST_CLOSE_NOT_FINITE`, a last finite close of zero or less still reads `LAST_CLOSE_NOT_POSITIVE`, a good history still reads `KEPT` `HISTORY_ROWS` with `rows` = the number of fetched rows. (`import trading_calendar as tc` sits inside the function on purpose: the module stays importable without `lib` on the path; in the resident package `lib/trading_calendar.py` is a member and `lib` is on the path.) Add one paragraph to the module docstring: the rule (last finite close at or before the T-1 trading day of lib/trading_calendar.py, why: a null or same-day newest row is not an answer).
3. Tests, added to `infra/aws/lambda/investor-reporting/intake/tests/test_yfinance_check.py` (offline; the file needs the repository's `lib` directory on `sys.path` for the calendar: add it at the top of the test file the way the file already adds the intake directory). Build the checker with `make_checker`-style fakes and pass `now=lambda: datetime.datetime(..., tzinfo=datetime.timezone.utc)`:
   - a NULL newest row on a Saturday run (`now` 2026-10-17 00:50Z; rows 2026-10-14 100.0, 2026-10-15 101.0, 2026-10-16 NaN): `KEPT`, `last_close` 101.0;
   - a Saturday run with Friday's close finite (2026-10-16 102.0): still `last_close` 101.0 (Thursday is the frontier);
   - a weekday run never reads the run's own day (`now` 2026-10-14 15:00Z; rows 10-12 97.0, 10-13 98.0, 10-14 99.0): `last_close` 98.0;
   - a HOLIDAY: `now` 2026-09-08 15:00Z (the day after Labor Day 2026-09-07), rows 2026-09-03 49.0, 2026-09-04 50.0, 2026-09-08 NaN: `KEPT`, `last_close` 50.0; and with 2026-09-08 51.0 also 50.0;
   - a null row ON the frontier day (`now` 2026-10-14 15:00Z; rows 10-09 96.0, 10-12 97.0, 10-13 NaN, 10-14 99.0): `last_close` 97.0;
   - every row after the frontier (`now` 2026-10-15 15:00Z; one row 2026-10-16): `NOT_KEPT` `NO_ROWS`;
   - the existing tests are not weakened or edited except where one needs `now`, and none should.
4. Run the three criteria. Commit the code and tests, then the proof and the status flip, as separate commits (code first).
5. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR157-g-AC1" cell_refs="AR-g-157"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g157_checks.py build</invocation><expect>^AR-G157-OK</expect></criterion>

<criterion id="AR157-g-AC2" cell_refs="AR-g-157"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g157_checks.py guard</invocation><expect>^AR-G157-OK</expect></criterion>

<criterion id="AR157-g-AC3" cell_refs="AR-g-157"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g157_checks.py regress</invocation><expect>^AR-G157-REGRESS-OK</expect></criterion>

<expected_criteria>AR157-g-AC1,AR157-g-AC2,AR157-g-AC3</expected_criteria>

- AC1 runs the real checker over fake histories and fake clocks: a Saturday run with a null Friday row reads Thursday's close; a Saturday run with a finite Friday row still reads Thursday's; a weekday run never reads its own day; the day after a holiday reads the trading day before it; a null row on the frontier day is dropped; only rows after the frontier read NOT_KEPT NO_ROWS; `YfinanceChecker` takes `now=`. At base it FAILs.
- AC2 holds what must not move: a good history reads KEPT with the last close; an empty history NOT_KEPT NO_ROWS; a last close of zero NOT_KEPT LAST_CLOSE_NOT_POSITIVE; an only-null history NOT_KEPT LAST_CLOSE_NOT_FINITE; a raising history CHECK_FAILED; the cap. At base it PASSes.
- AC3 runs the checker's, the resolver's, the decision tree's and the broker's existing test files on their own, then that the branch changed only your files, your folder, the order and the channel file (against the merge-base with `box/dell2`). At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. The resolver, the provider port, the cache keys, the checker's cap and pacing, `default_history`, `lib/trading_calendar.py` and every file not listed are not yours; `lib/trading_calendar.py` is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/intake/yfinance_check.py
infra/aws/lambda/investor-reporting/intake/tests/test_yfinance_check.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~280/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-157.yfinance-checker-last-finite-close-at-t1.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R54_G.md</decomp_doc> round 54, workstream ~G, cell `AR-g-157`.
<owned_cells>AR-g-157</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR157-g-AC1, AR157-g-AC2, AR157-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~280/IRPT_ANLREQ.TO-AR-g-157.yfinance-checker-last-finite-close-at-t1.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-157`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR157-g-AC1,AR157-g-AC2,AR157-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 5.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one existing product module and its test file; no deploy, no AWS call, no network. The change reaches production only through the r34j resident release under its own never-widen pair. It changes what the door reads for a symbol whose newest Yahoo row is null or dated after the T-1 frontier (KEPT on the last finite close instead of NOT_KEPT); no other branch of the checker moves. The calendar is read, never edited.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the issuer's check `ar_g157_checks.py` was dry-run at the base (build FAIL, guard PASS) and against a scratch copy with a reference fix (build OK, guard OK) and five mutants (no T-1 cut, no null drop, a weekday rule instead of the calendar, the last trading day instead of the day before it, a zero close skipped); the first four fail build and the fifth fails guard. Traps: Saturday (the calendar frontier is Thursday, a weekday rule says Friday), the day after a holiday, the run's own day, a null row ON the frontier day, the calendar's fallback coverage (2010 to 2027: a date outside it raises, which the existing handler reads as CHECK_FAILED, never NOT_KEPT). NOT seen (blind): the live Yahoo frame at the time the symbol is checked, and whether pandas_market_calendars is present on the host (the fallback answers either way); denominator: 8 build arms, 6 guard arms.
</preflight>

- Cut on the CTO's rulings (msgs 10112 and 10122) by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: AR157-g-AC1 FAILs, AR157-g-AC2 PASSes, AR157-g-AC3 PASSes (in the worker's worktree).
