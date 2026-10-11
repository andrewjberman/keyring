# TO IRPT_BCKEND.TO-IB-pr-454 -- BUILD, nothing served: the date-basis grading instrument's product form, its tests, and one read-only run that returns the fixed window, the distribution in tenths and the rule's cost

<to_id>IRPT_BCKEND.TO-IB-pr-454</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~310</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5800 (PRD v0.43 @44828c43b8, ratified-text half SIGNED @4c07d90a47) | **Decomp cell:** `IB-pr-454` (decomposition section 142) | **outcome_ref:** FWD-13

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-310/` (bash `/c/dev/wk-irpt-bckend-310`). Work only there. You create TWO product files (a module
and its tests) and edit no other product file; nothing imports the module: **nothing is served by this cell.** You then RUN the
module once over the real data, read only: READ ONLY toward AWS; ONE external source, Yahoo Finance through the reader below,
ONE PASS (count the distinct tickers BEFORE fetching; above 1,500 STOP and file a row; each ticker asked exactly once, at most
50 a call, paced, never in parallel; nothing re-asked). NO YCharts call, NO Bloomberg call. No claim re-graded in the product, no
class admitted. Counts only in every output: no account id, balance or holding of an account (write dates with dashes).

**The contract.** Read PRD ADDENDA v0.35 to v0.43 (the date-basis sections at the end of
`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`): the ordered claim rule (`UNGRADEABLE` with its kinds
`ANCHOR_NOT_LANDED`, `OUTSIDE_ANCHOR`, `NO_CUSIP`, `NEITHER_CLOSE`, `NEGATIVE_POSITION`; then `ACCT_PRIOR_DATE`; `ACCT_OWN_DATE`;
`NOTHING_TO_GRADE`), the cash rule, the two witnesses (`SCHWAB_ANCHOR`, `YAHOO_CLOSE`), the type rule (exactly one pair = that
type), the NINE admitted pairs (v0.39 and v0.42), the guard's two sentences (v0.40, v0.41), and v0.43's rule:

> `YAHOO_CLOSE` gives NO grade for a security on any day when, over the days of the grading run on which it has a bar for that
> security, the bar repeats the prior trading day's on MORE THAN HALF of them.

**The defect this cell closes** (the reviewer's note, CTO msg 5800): "the days of the grading run" makes the same security-day
graded in one run and not in another. A served claim that changes with the run's length is not reproducible. So the product
form uses a FIXED window: a count of trailing trading days ENDING AT THE GRADED DAY. You PROPOSE the count, with its reason,
and what is done when fewer bars exist than the window; the CTO writes it into the contract. **Same day, same inputs, same
grade.**

**The instrument today** is measurement scripts, merged in your worktree:
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~308/` (`ib429_claims.py` and `ib429_claims_v035.py`: the row
kinds and the ordered claim rule; `ib442_*`: the type join, the row grade against the reader's bar, the serving rule and the
sizing; `ib445_measure.py`: the guard; `ib452_measure.py`: both guard sentences, the nine pairs, the not-graded list; the
fetchers; record `IB148-1_nine_pair_sizing.json`). The guard itself is already product code:
`data/assets/scripts/gold/irpt_reporting/second_witness_guard.py` (`second_witness_grades(bars, t)`); IMPORT it, do not copy it.

**Build** `data/assets/scripts/gold/irpt_reporting/date_basis_grading.py`: PURE functions over in-memory inputs (no S3, no
network, no pandas requirement in the functions' signatures; standard library, `lib.trading_calendar` and the guard module
only; import `lib` the way `second_witness_guard.py` does). It carries, ported faithfully from the scripts above and each citing
the PRD addendum it implements:
- the constants: the four claims, the five kinds, the two witness names, the nine admitted pairs as the source writes them, the
  relative tolerance, and `REPEATED_SHARE_WINDOW` (an integer count of trading days: your proposal);
- `repeated_share(bars, t)` -> `(repeated_days, days_compared)` over the `REPEATED_SHARE_WINDOW` trading days ending at `t`
  (the calendar's days; a day counts as compared when the security has a bar on it and on its prior trading day; it is
  repeated when the guard's first sentence holds);
- `second_witness_grades_security_day(bars, t)` -> bool: true only when `second_witness_grades(bars, t)` is true AND the
  security is not mostly repeating at `t` (repeated more than half of the days compared in the window), with your
  short-history rule applied when fewer days can be compared than the window. It must depend ONLY on bars inside the window
  ending at `t`: bars before the window, and the length of the series handed in, change nothing;
- the row grade and the account-day claim: one function that, given one account-day's rows and the two witnesses' closes for
  the day and the prior trading day, the security types, and the reader's per-security verdict, returns the claim and, for
  `UNGRADEABLE`, the list of every kind present, by the ordered rule; and the serving rule over a sequence of account-day
  claims (served when today and the prior graded day each read `ACCT_OWN_DATE` or `NOTHING_TO_GRADE`);
- a switch (a keyword argument, default on) that turns the repeated-share rule OFF, used by the seam criterion only.
No I/O, no producer, no schema, no entry in any `sources.json`, no scheduled anything.

**Tests** `data/assets/scripts/gold/irpt_reporting/tests/test_date_basis_grading.py`: each claim and each kind from a planted
account-day; the ordered rule's precedence; the cash rule; an admitted and a non-admitted pair outside the first witness; the
guard's two sentences reached through the module; the repeated-share rule on and off; and **the reproducibility test: the same
security-day gives the same grade when the series handed in is the window alone and when it is three windows long.**

**Then run it** (your own driver script in YOUR deliverables folder, reusing the fetchers; cache `C:/dev/_scratch310/`, outside
the worktree, deleted file by file at the end; window 2026-06-05 to 2026-10-13 plus as many EARLIER trading days as your
proposed window needs before the first graded day, 2026-06-10: say how many you fetched and whether the first graded days have
a full window) and write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~310/IB150-1_product_form_run.json`:
1. `seam_rule_off_reproduces_ib_pr_452`: `{reproduces, computed_by: "the product module", read:{account_days, serving_rule,
   freed_and_holding_no_other_ungradeable_kind}}`: with the repeated-share rule OFF, the module over the same 85 graded days
   must give IB-pr-452's `nine_pairs_under_both_guard_sentences` (blank 33,291 of 75,796, never served 247, freed 12,482;
   `account_days` member for member). If it does not, stop and file a row: the port is wrong.
2. `window_proposed`: `{trading_days, reason, when_fewer_bars_than_the_window, candidates:[{trading_days, securities_taken,
   security_days_not_graded, account_days_no_longer_freed}]}`: three or more candidate windows (for example 20, 40, 60 trading
   days, and the whole 85 as the reference), each with how many securities the rule takes on one or more days, how many
   security-days it un-grades beyond the guard, and its cost in freed account-days against the rule-off sizing; and
   `securities_whose_verdict_changes_within_the_run` per candidate (a security graded on some days and not on others: the
   price of a moving window, stated). The reason is yours to give from those counts; state the trade plainly.
3. `securities_by_share_of_repeated_days`: over the securities of the nine pairs OUTSIDE the first witness that have bars,
   the count by share of repeated days at the LAST graded day's window, in tenths: `{securities, over_what, bin_rule_in_words,
   tenths:{"0.0-0.1":n, ..., "0.9-1.0":n}}` (ten bins in that order, summing to `securities`; say where a share exactly on an
   edge goes), and the same for the overlap securities beside it (`overlap_tenths`).
4. `sizing_under_the_rule`: the nine-pair sizing with the rule ON at your proposed window (`account_days`, `serving_rule`,
   `freed_and_holding_no_other_ungradeable_kind`), and `securities_taken_by_the_rule_cost`: `{securities:[tickers],
   the_seven_of_ib_pr_452_all_taken, account_days_no_longer_freed, accounts_no_longer_ever_served, row_days, by_ticker}`
   (IB-pr-452's seven are ADLYX, BISOX, EIBLX, GPPIX, JSOSX, OLCYX, SGOV; if your window takes a different set, list both
   differences; and print the cost of exactly those seven not graded on any day, as `the_seven_whole_run_cost`).
5. `fetch` (`call_count`, `distinct_tickers_asked`, `tickers_asked_more_than_once: 0`, `counted_before_fetching`),
   `not_established`, `claims_regraded_in_product: 0`, `classes_admitted_by_this_cell: 0`, `served_changes: 0`,
   `other_sources_asked: 0`; and a one-page `IB150-1_PRODUCT_FORM_RUN_READ.md` leading with the three returns.

<criterion id="IB150-1-AC1" cell_refs="IB-pr-454"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r150/p150_cells.py" . IB150-1-AC1</invocation><expect>IB150-1-AC1 PASS</expect></criterion>
<criterion id="IB150-1-AC2" cell_refs="IB-pr-454"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r150/p150_cells.py" . IB150-1-AC2</invocation><expect>IB150-1-AC2 PASS</expect></criterion>
<criterion id="IB150-1-AC3" cell_refs="IB-pr-454"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r150/p150_cells.py" . IB150-1-AC3</invocation><expect>IB150-1-AC3 PASS</expect></criterion>

<expected_criteria>IB150-1-AC1, IB150-1-AC2, IB150-1-AC3</expected_criteria>

AC1 is the built behaviour (your tests, and the issuer's two planted series asked in a long and a short run); AC2 is the seam
against the real data (the port reproduces the measured sizing); AC3 is the three returns, the bounds and that nothing imports
the module. The window, the distribution and the cost are UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Do not wire the module into any producer, reader, schema or schedule.
- **Refusal clause:** if the seam does not reproduce, a PRD sentence and a script disagree, or a criterion cannot be met as
  written: stop, file a row and report. Never weaken a check; do not edit `p150_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W310-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- Every `.py` passes `bash .tools/commit-gate.sh <file>` before the commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~310" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~310@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~310 <0.9.0_WK_IRPT_BCKEND~310@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
data/assets/scripts/gold/irpt_reporting/date_basis_grading.py
data/assets/scripts/gold/irpt_reporting/tests/test_date_basis_grading.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~310/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-454.date-basis-grading-product-form.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 142 (round 150, workstream ~P), cell `IB-pr-454`.
<owned_cells>IB-pr-454</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB150-1-AC1, IB150-1-AC2, IB150-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~310/IRPT_BCKEND.TO-IB-pr-454.date-basis-grading-product-form.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the module's functions and line count, the test count; the seam (reproduced or not); the
window you propose, its reason, the short-history rule, and the candidates' counts; the distribution in tenths; the sizing under
the rule and the cost of the securities it takes, and whether they are IB-pr-452's seven; the fetch; what is not established;
each criterion's last line; the commit gate's and the proof checker's results; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; two NEW files, a pure module and its tests; no existing file is edited and no file imports the module (IB150-1-AC3 reads that); the run writes to the worker's own deliverables folder.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; S3 reads the earlier cells of this chain already made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; no producer is built.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p150_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~20:5xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no module); commit-gate clean. prd-signoff status read by the issuer: v0.43, both halves current. The seam target is read by the check from IB-pr-452's merged record @6a7b589f9e. Not DIRECT-ACT: the port is above the direct-act size floor. HOME DECISION, the issuer's, as for IB-pr-450: IRPT's gold folder, a module nothing imports; the producer, the schema and the served change are later cells under their own pair (CTO msgs 5650, 5788, 5800).
lane: the <paths> block IS the grant. LOCAL: code, tests and records; nothing served.
</preflight>
