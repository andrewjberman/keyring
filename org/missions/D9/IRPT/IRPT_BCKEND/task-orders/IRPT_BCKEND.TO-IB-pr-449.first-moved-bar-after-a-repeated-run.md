# TO IRPT_BCKEND.TO-IB-pr-449 -- READ ONLY, counts only: what the second witness's bar is when it MOVES after a repeated run, for the two fund pairs left out, and the six institutional securities' moved days

<to_id>IRPT_BCKEND.TO-IB-pr-449</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~306</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>145</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5624 (PRD v0.40 @6d12b3dd65, both halves current) | **Decomp cell:** `IB-pr-449` (decomposition section 137) | **outcome_ref:** FWD-13

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-306/` (bash `/c/dev/wk-irpt-bckend-306`). Work only there. READ ONLY toward AWS. ONE external source
only: Yahoo Finance through the reader below, ONE PASS (each ticker asked exactly once, at most 50 a call, calls paced and never
in parallel; a ticker or a call that returns nothing is recorded and never asked again). Count the distinct tickers BEFORE
fetching; above 400, STOP, report the number and file a row. NO YCharts call, NO Bloomberg call. Nothing built into the product,
nothing served, no claim re-graded in the product, and NO CLASS IS ADMITTED by this cell. Counts only; no account id, balance
or holding of an account in any output.

**Why.** Read PRD ADDENDUM v0.40 (the last section of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`) and the record
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~303/IB142-1_UNMOVED_BAR_GUARD_READ.md` with its json. The
guard is adopted: the second witness (the reader's unadjusted Close) gives no grade on a day its own bar repeats the prior
trading day's. The institutional share class is NOT admitted: six of its 71 securities outside the first witness repeat their
bar on more than half their days, **and nothing measured says what the bar is when it moves.** This cell measures that: after
a run of repeated bars, is the first MOVED bar the right day's close, or a late one?

**Your instruments** are in your worktree (merged): `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~303/`
(`ib445_measure.py`, `ib445_tickers.py`, and the scripts it copied forward: the overlap table of the 894 securities both
witnesses carry, the type join by CUSIP, the guard, the one-pass fetch, the row grading against the reader's bar). Copy what
you need into YOUR folder; write nothing into another worker's folder. Keep unchanged: the source and anchor addresses, the
price rule, the relative tolerance 1e-4, the trading-day axis, the one-way digest of the account key, the type rule (exactly
one pair = that type), the guard exactly as IB-pr-445 stated it. The reader: `fetch_yahoo` in
`data/assets/scripts/silver/commonwealth_price_basis_census.py` and `read_yahoo_close` in
`data/assets/scripts/silver/commonwealth_daily_valuation.py`; your own cache `C:/dev/_scratch306/yahoo/`; window 2026-06-05 to
2026-10-13. Scratch is OUTSIDE the worktree and deleted file by file at the end.

**The two pairs**, as the transactions table writes them: `Securities Issued by Registered Investment Companies or Business
Development Companies / Inst` and `... / Not Available`.

**Do, in this order:**
1. **Reproduce.** For each of the two pairs, the OVERLAP securities (carried by both witnesses) under the guard: equal,
   one_day_off, neither, no_bar, not_graded_under_the_guard must equal IB-pr-445's `overlap_by_type_under_the_guard` for that
   pair (`reproduces_ib_pr_445_under_the_guard`). If they do not, stop and file a row.
2. **Runs** (state `run_rule_in_words`): for one security, a REPEATED RUN is a maximal sequence of consecutive trading days on
   each of which the reader's bar equals its bar for the prior trading day. Count `securities`,
   `securities_with_a_repeated_run`, `repeated_runs`, `days_in_runs`, and the distribution of run lengths (`run_lengths`:
   length to count).
3. **The first moved day after each run** (state `first_moved_day_rule_in_words`): the first trading day after the run on
   which the reader has a bar that differs from the prior trading day's. Place EVERY run in exactly one outcome
   (`first_moved_day_after_a_run`): `equals_the_anchor_same_day` (the moved bar equals the anchor's close for that day);
   `equals_the_anchor_prior_day` (it equals the anchor's close for the prior trading day and not that day's: a LATE bar);
   `equals_neither`; `no_anchor_that_day`; `no_moved_day_in_window` (the run reaches the window's end). Also, beside it and
   outside the sum: of the runs whose first moved day equals neither, how many equal the anchor's close for a day INSIDE the
   run (`equals_an_anchor_close_inside_the_run`), and, over the days of all runs, on how many the ANCHOR moved while the
   reader did not (`run_days_the_anchor_moved`) against `run_days_the_anchor_also_unmoved`, and `run_days_with_no_anchor`.
4. **The six** (`the_six`, keyed by ticker): ADLYX, BISOX, EIBLX, GPPIX, JSOSX, OLCYX (confirm they are the six IB-pr-445
   names in `inst_under_the_guard.securities_ungraded_on_more_than_half_their_days`). They are OUTSIDE the first witness, so
   no anchor exists for them: state `anchor_carries_it` per ticker from the anchor read. For each: `days_with_a_bar`,
   `days_unmoved`, `days_moved`, `days_with_no_prior_bar` (these sum to days with a bar); `rows_held_on_moved_days` (holdings
   rows of that security on its moved days, all accounts) and each such row's price against the reader's bar
   (`held_rows_on_moved_days`): `equals_the_bar_same_day`, `equals_the_bar_prior_day` (and not the same day's),
   `equals_neither`. And the size of the move: of the moved days, how many moved by less than 0.1 percent
   (`moved_days_under_a_tenth_of_a_percent`). One sentence per ticker on what kind of fund it is ONLY if the transactions
   table or the holdings rows say so (a money-market or stable-value fund holds a constant price by design); otherwise say
   it is not told.
5. **Control** (`control`): plant a five-day series whose bar repeats on days 2 and 3 and moves on day 4 to the anchor's day-4
   close, and a second whose day-4 bar is the anchor's day-3 close; your classifier must read the first as
   `equals_the_anchor_same_day` and the second as `equals_the_anchor_prior_day`; `planted` equals `read`.
6. `not_established`: everything this cannot settle. Do not recommend admitting or refusing the class.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~306/`: `IB145-1_first_moved_bar.json` with
`{run_rule_in_words, first_moved_day_rule_in_words, first_moved_bar_by_pair:{<pair>:{securities,
securities_with_a_repeated_run, repeated_runs, days_in_runs, run_lengths, reproduces_ib_pr_445_under_the_guard:{...},
first_moved_day_after_a_run:{five outcomes}, equals_an_anchor_close_inside_the_run, run_days_the_anchor_moved,
run_days_the_anchor_also_unmoved, run_days_with_no_anchor}}, the_six:{<ticker>:{...}}, fetch:{call_count,
distinct_tickers_asked, tickers_asked_more_than_once, tickers_with_no_bars, counted_before_fetching}, control:{planted, read},
not_established:[...], claims_regraded_in_product:0, classes_admitted_by_this_cell:0, other_sources_asked:0}`; your scripts;
and a one-page `IB145-1_FIRST_MOVED_BAR_READ.md` in plain sentences with the two tables.

<criterion id="IB145-1-AC1" cell_refs="IB-pr-449"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r145/p145_cells.py" . IB145-1-AC1</invocation><expect>IB145-1-AC1 PASS</expect></criterion>
<criterion id="IB145-1-AC2" cell_refs="IB-pr-449"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r145/p145_cells.py" . IB145-1-AC2</invocation><expect>IB145-1-AC2 PASS</expect></criterion>
<criterion id="IB145-1-AC3" cell_refs="IB-pr-449"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r145/p145_cells.py" . IB145-1-AC3</invocation><expect>IB145-1-AC3 PASS</expect></criterion>

<expected_criteria>IB145-1-AC1, IB145-1-AC2, IB145-1-AC3</expected_criteria>

The checks grade sums with no remainder, the reproduction against IB-pr-445, the six's identity, the control and the bounds.
Every count is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** if the reproduction fails, a criterion cannot be met as written, or the six are not the six: stop, file a
  row and report. Never weaken a check; do not edit `p145_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W306-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~306" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~306@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~306 <0.9.0_WK_IRPT_BCKEND~306@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~306/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-449.first-moved-bar-after-a-repeated-run.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 137 (round 145, workstream ~P), cell `IB-pr-449`.
<owned_cells>IB-pr-449</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB145-1-AC1, IB145-1-AC2, IB145-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~306/IRPT_BCKEND.TO-IB-pr-449.first-moved-bar-after-a-repeated-run.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the reproduction; per pair the runs, their lengths, and the five outcomes of the first moved
day, with the three side counts; the six, each with its moved days and its held rows' three outcomes; the fetch; the control;
what is not established; each criterion's last line; the proof checker's result; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only measurement written to the worker's own deliverables folder; nothing is edited or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; S3 reads the earlier cells of this chain already made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p145_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~19:2xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The six tickers and the two pair names are read from IB-pr-445's merged record @7d31765674 and the check re-reads them from that record. prd-signoff status read by the issuer: v0.40, both halves current.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
