# TO-AR-g-161 -- the resident's pricing as_of is lib/trading_calendar.py's T-1 frontier, called, not a local weekday rule (row S163; CTO msg 10257)

<to_id>IRPT_ANLREQ.TO-AR-g-161</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~282</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>56</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-161` (`decompositions/IRPT_ANLREQ_DECOMP_R56_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none (AR-g-159 is merged: `lib` is on the service's path). Order: CTO msg 10257 (as_of is the calendar module's frontier, called; a test pins Saturday, Sunday, a holiday and the day after; it rides the next release that touches `resident_installed.py`; nothing is deployed by this cell).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~282`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-282` (branch `wk-IRPT_ANLREQ-282`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~282 <0.9.0_WK_IRPT_ANLREQ~282@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W282-S<k>` (take the next free `<k>`; check the channel file for `W282` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only in the product file. Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-161`, inlined)

File: `infra/aws/lambda/investor-reporting/reports/resident_installed.py`. Lines 379-385 read:

    def _t_minus_1(epoch):
        """The UTC date of `epoch` (seconds) minus one day, and minus further days while it is a Saturday or Sunday (AR-g-90).
        Never later than the true T-1, so no row of the run's own day is read; a holiday is earlier by a day with no row."""
        day = datetime.datetime.fromtimestamp(epoch, tz=datetime.timezone.utc).date() - datetime.timedelta(days=1)
        while day.weekday() >= 5:
            day -= datetime.timedelta(days=1)
        return day.isoformat()

That is a LOCAL weekday rule. The repository has ONE frontier, `lib/trading_calendar.py`: `prev_trading_day(expected_last_trading_day(day))` (Saturday 2027-01-16 gives Thursday 2027-01-14; the day after a holiday gives the trading day before the holiday).

1. Replace the function body so that `_t_minus_1(epoch)` keeps its name and its one argument and returns the calendar's frontier for the UTC date of `epoch` as an ISO string:

        def _t_minus_1(epoch):
            """The T-1 trading-day frontier of lib/trading_calendar.py as of the UTC date of `epoch` (seconds): prev_trading_day(expected_last_trading_day(day)). One frontier for every reader (row S163)."""
            import trading_calendar as tc
            day = datetime.datetime.fromtimestamp(epoch, tz=datetime.timezone.utc).date()
            return tc.prev_trading_day(tc.expected_last_trading_day(day)).isoformat()

   (the import sits inside the function: `lib` is on the service's `sys.path` since AR-g-159 and the module stays importable without it). Change nothing else in the module; `_pricing_extras` still sets `"as_of": _t_minus_1(clock())`.
2. In `infra/aws/lambda/investor-reporting/reports/tests/test_opal_pricing_binding.py`: the repository's `lib` directory must be on `sys.path` for the calendar (add it near the top of the file the way the file already adds its own directory: the repository root is `Path(__file__).parents[5]`, so `lib` is `Path(__file__).parents[5] / "lib"`; confirm it holds `trading_calendar.py`). Replace the test `test_t_minus_1_skips_weekends` (it pins the old rule: Sunday 2027-01-17 and Monday 2027-01-18, which is Martin Luther King Day, both to 2027-01-15) by `test_t_minus_1_is_the_calendar_frontier` asserting, with the file's `_epoch(day)` helper, these five pairs: `2027-01-16` -> `2027-01-14` (Saturday), `2027-01-17` -> `2027-01-14` (Sunday), `2027-01-18` -> `2027-01-14` (the holiday Monday), `2027-01-19` -> `2027-01-15` (the day after the holiday), `2027-01-20` -> `2027-01-19` (an ordinary Wednesday). The file must hold each of those ten date strings. Leave every other test in the file as it is (the `as_of == "2027-01-14"` test for a Friday clock is still true).
3. Run the three criteria. Commit the code and tests, then the proof and the status flip, as separate commits (code first).
4. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR161-g-AC1" cell_refs="AR-g-161"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g161_checks.py build</invocation><expect>^AR-G161-OK</expect></criterion>

<criterion id="AR161-g-AC2" cell_refs="AR-g-161"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g161_checks.py guard</invocation><expect>^AR-G161-OK</expect></criterion>

<criterion id="AR161-g-AC3" cell_refs="AR-g-161"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g161_checks.py regress</invocation><expect>^AR-G161-REGRESS-OK</expect></criterion>

<expected_criteria>AR161-g-AC1,AR161-g-AC2,AR161-g-AC3</expected_criteria>

- AC1 extracts `_t_minus_1` from the module and runs it against the five pinned dates, and requires that it carries no `weekday() >= 5` and names `trading_calendar`, and that the test file pins the five pairs and no longer pins 2027-01-15 for the Sunday or the holiday. At base it FAILs.
- AC2 holds what must not move: the name and the one argument, a YYYY-MM-DD result, and `_pricing_extras` setting `as_of` from `_t_minus_1(clock())`. At base it PASSes.
- AC3 runs `test_opal_pricing_binding.py`, `test_ycharts_price_tier.py` and `test_resident_installed.py` on their own, then that the branch changed only your files, your folder, the order and the channel file (against the merge-base with `box/dell2`). At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. `lib/trading_calendar.py` is read only; every other file is not yours.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_opal_pricing_binding.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~282/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-161.pricing-as-of-calendar-frontier.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R56_G.md</decomp_doc> round 56, workstream ~G, cell `AR-g-161`.
<owned_cells>AR-g-161</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR161-g-AC1, AR161-g-AC2, AR161-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~282/IRPT_ANLREQ.TO-AR-g-161.pricing-as-of-calendar-frontier.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-161`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR161-g-AC1,AR161-g-AC2,AR161-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 4.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one function of one existing module and one test file; no deploy, no AWS call, no network. It reaches production only through the next resident release that touches resident_installed.py, under its own never-widen pair. The count of reports whose as_of would change is 0 delivered and 0 queued (ASOF_COUNT_20261017.md); from the first priced report, a Saturday, Sunday or weekday-holiday run reads one trading day earlier and the day after a holiday prints a different date with the same close.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the issuer's check `ar_g161_checks.py` was dry-run at the base (build FAIL, guard PASS, regress PASS) and against a scratch copy with a reference fix (build OK, guard OK) and three mutants (the weekday rule, the last trading day without the day before it, a date object instead of an ISO string); each fails build. Traps: the existing test pinned the old rule with a Monday that is a holiday (2027-01-18 is Martin Luther King Day); the calendar import must work in the service (AR-g-159 put lib on the path; r34j's V2 found that missing for the checker) and in the repository tests (they put lib on the path themselves); the fallback calendar covers 2010 to 2027. NOT seen (blind): the live service's calendar (the V2 of the release that carries this reads it); denominator: 7 build arms, 3 guard arms.
</preflight>

- Cut on the CTO's ruling (msg 10257) by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: AR161-g-AC1 FAILs, AR161-g-AC2 PASSes, AR161-g-AC3 PASSes (in the worker's worktree).
