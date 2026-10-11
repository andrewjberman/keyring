# TO IRPT_BCKEND.TO-IB-pr-450 -- BUILD, nothing served: the second witness's guard as one pure function with its tests

<to_id>IRPT_BCKEND.TO-IB-pr-450</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~307</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>146</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5650 (PRD v0.40 and v0.41 both SIGNED) | **Decomp cell:** `IB-pr-450` (decomposition section 138) | **outcome_ref:** FWD-13

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-307/` (bash `/c/dev/wk-irpt-bckend-307`). Work only there. No AWS call, no network call. You create
TWO files and edit no other product file. Nothing imports the new module: nothing is served by this cell.

**The contract** (PRD ADDENDA v0.40 and v0.41, the last two sections of
`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`; read them):

> `YAHOO_CLOSE` gives NO grade for a security on day t when its own bar for t equals its bar for the prior trading day (relative
> 1e-4). Where `YAHOO_CLOSE` has no bar for the trading day before t, it gives NO grade for that security on t. The prior trading
> day is `lib/trading_calendar.py`'s, not the prior row.

**Build** `data/assets/scripts/gold/irpt_reporting/second_witness_guard.py`, one pure function and nothing else:

```python
def second_witness_grades(bars, t) -> bool:
    """bars: a mapping of datetime.date -> the reader's unadjusted Close for ONE security; t: a datetime.date."""
```

It returns `True` only when ALL of these hold, and `False` otherwise:
1. `bars` has a positive bar for `t`;
2. `bars` has a positive bar for `lib.trading_calendar.prev_trading_day(t)` (the calendar's prior trading day; an earlier ROW in
   `bars` is never a substitute);
3. the two bars DIFFER by more than the relative tolerance: equal means `abs(a - b) <= 1e-4 * max(abs(a), abs(b))`, the comparison
   the measurement used (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~303/ib445_measure.py`, line 43).

`t` that is not a trading day raises `ValueError` (the guard is asked about trading days only). The calendar's own
`CalendarCoverageError` is not caught. The tolerance is one module constant. A bar that is `None`, not a number, NaN, zero or
negative counts as no bar. No pandas, no I/O, no other import than `lib.trading_calendar` and the standard library; import the
calendar the way `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` or its neighbours import `lib` modules (read
one and follow it). The docstring quotes the two contract sentences and cites the PRD addenda; ASCII only.

**Tests** `data/assets/scripts/gold/irpt_reporting/tests/test_second_witness_guard.py` (follow a neighbouring test file's import
form): a moved bar grades; an unmoved bar does not; inside and just outside the tolerance; no bar on the day; no bar on the
calendar's prior trading day while an earlier row exists and differs (the v0.41 case); a Monday against the Friday before; a
non-trading day raises; zero, negative, None and NaN bars count as absent. Use real dates in October 2026 (2026-10-02 is a
Friday; 2026-10-05 to 2026-10-09 are trading days).

<criterion id="IB146-1-AC1" cell_refs="IB-pr-450"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r146/p146_cells.py" . IB146-1-AC1</invocation><expect>IB146-1-AC1 PASS</expect></criterion>
<criterion id="IB146-1-AC2" cell_refs="IB-pr-450"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r146/p146_cells.py" . IB146-1-AC2</invocation><expect>IB146-1-AC2 PASS</expect></criterion>
<criterion id="IB146-1-AC3" cell_refs="IB-pr-450"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r146/p146_cells.py" . IB146-1-AC3</invocation><expect>IB146-1-AC3 PASS</expect></criterion>

<expected_criteria>IB146-1-AC1, IB146-1-AC2, IB146-1-AC3</expected_criteria>

AC1 runs your test file; AC2 runs the issuer's ten cases against your function; AC3 reads that no other file under `data/` or
`infra/` names the module.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Do not wire the function into any producer, reader or schema.
- **Refusal clause:** if a criterion cannot be met as written, or the contract sentence and an issuer case disagree, stop, file a
  row and report. Never weaken a check; do not edit `p146_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W307-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- Every `.py` passes `bash .tools/commit-gate.sh <file>` before the commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~307" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~307@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~307 <0.9.0_WK_IRPT_BCKEND~307@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
data/assets/scripts/gold/irpt_reporting/second_witness_guard.py
data/assets/scripts/gold/irpt_reporting/tests/test_second_witness_guard.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~307/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-450.second-witness-guard-function-and-tests.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 138 (round 146, workstream ~P), cell `IB-pr-450`.
<owned_cells>IB-pr-450</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB146-1-AC1, IB146-1-AC2, IB146-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~307/IRPT_BCKEND.TO-IB-pr-450.second-witness-guard-function-and-tests.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the two files and their line counts; how the calendar is imported; the test count; each
criterion's last line; the commit gate's result; the proof checker's result; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; two NEW files, a pure function and its tests; no existing file is edited and no file imports the module (IB146-1-AC3 reads that).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change and no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p146_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~19:3xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no module); commit-gate clean. The issuer read lib/trading_calendar.py prev_trading_day for the check's dates (2026-10-05 -> 2026-10-02; 2026-10-07 -> 2026-10-06) and the measurement's comparison at ib445_measure.py:43. HOME DECISION, the issuer's: the grading instrument is not product code today (comp-find for the claim and witness names over data/, lib/ and infra/: 0 hits in 10,457 files); it exists as the measurement scripts in worker folders. The guard therefore lands as one pure function in IRPT's gold folder, which the instrument's product form will import when the CTO orders it; nothing is wired. prd-signoff: v0.40 and v0.41 SIGNED (CTO msg 5650).
lane: the <paths> block IS the grant. DIRECT-ACT (one cell under 100 product lines, LOCAL: code and tests, nothing served).
</preflight>
