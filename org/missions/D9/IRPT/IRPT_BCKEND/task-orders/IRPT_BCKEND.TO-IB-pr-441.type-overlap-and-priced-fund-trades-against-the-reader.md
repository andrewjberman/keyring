# TO IRPT_BCKEND.TO-IB-pr-441 -- READ ONLY: both witnesses per instrument type (type joined from the transactions table), and each priced fund trade beside the reader's bars

<to_id>IRPT_BCKEND.TO-IB-pr-441</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~299</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>138</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5376 (ruling on IB-pr-439's read; row IRPT_BCKEND-D2-W297-S1) | **Decomp cell:** `IB-pr-441` (decomposition section 130) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-299/` (bash `/c/dev/wk-irpt-bckend-299`). Work only there. READ ONLY toward AWS. ONE external source
only: Yahoo Finance through the reader below, ONE PASS over BOTH tables together (each ticker asked exactly once, at most 50 a
call, calls paced and never in parallel; a ticker or a call that returns nothing is recorded and never asked again). If the
distinct tickers come to more than 1,500, STOP before fetching, report the number and file a row. NO YCharts call, NO Bloomberg
call. Nothing built into the product, nothing served, no claim re-graded, and NO CLASS IS ADMITTED by this cell: it produces two
tables; the CTO writes an addendum on them or does not.

**Why.** Read PRD ADDENDUM v0.38 whole first (the LAST section of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`). A
second witness of the date basis (the reader's unadjusted Close) may grade only a class of security whose DATE LABELS have been
measured: a witness that labels a value one day late passes days systematically. IB-pr-439 found the holdings source states no
instrument type, so no class is admitted and 58.2 percent of eligible account-days stay blank. It also found that the
transactions table beside the holdings table carries `SEC Asset Type` and `Share Class Type` by CUSIP, and dated trade prices.
Those give the two tables v0.38 lacks.

**Your instruments** are in your worktree if IB-pr-439 has merged into your base, otherwise on branch `wk-IRPT_BCKEND-297`
(commit e6462bdd4a): folder `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~297/` (`ib439_measure.py`: the
count of securities both witnesses carry, the one-day-off classifier and its control, the transactions read, the nine-fund trade
count; read with `MSYS_NO_PATHCONV=1 git show wk-IRPT_BCKEND-297:<path>` if absent, with a positive control beside any "absent"
reading). Earlier cells' folders `~288`, `~293`, `~294`, `~296` are in your worktree. Copy what you need into YOUR folder; write
nothing into another worker's folder. Keep unchanged: the source and anchor addresses, the price rule, the tolerance (relative
1e-4), the trading-day axis, the one-way digest of the account key. The reader: `fetch_yahoo` in
`data/assets/scripts/silver/commonwealth_price_basis_census.py` and `read_yahoo_close` in
`data/assets/scripts/silver/commonwealth_daily_valuation.py`, used as `~296` used them; your own cache `C:/dev/_scratch299/yahoo/`;
window 2026-06-05 to 2026-10-13 (you need the bar of the trading day before the first and after the last date compared; say what
you had at the edges). Scratch is OUTSIDE the worktree and deleted file by file at the end.

**Table 1 -- the overlap by type.** The securities both witnesses carry (IB-pr-439 counted 894: held by a Cottonwood account,
carried by the Schwab anchor, with a ticker in the source; 890 distinct tickers). Join each BY CUSIP to the transactions table's
`SEC Asset Type` and `Share Class Type`: say how the type of a security is taken when its transaction rows disagree
(`found_more_than_one_type`: list the combinations, put the security under `MIXED`), and how many find NO transaction row at all
(`found_no_type`; they go under `NO_TYPE`). The type key of the table is the pair, written `<SEC Asset Type> / <Share Class
Type>`. For each security and each of the 85 trading days: the reader's bar for day t against the anchor's close for day t:
`equal` (within the tolerance); `one_day_off` (not equal for t, and the reader's bar for t equals the anchor's close for the prior
OR the next trading day); `neither`; `no_bar`. Per type: `securities`, `security_days`, the four counts (summing to
`security_days`), `equal_on_days_the_close_moved` (the `equal` days on which the anchor's close differs from its prior day's:
only those can tell a right date label from a shifted one), `securities_with_any_one_day_off`. List
`types_with_an_empty_one_day_off_column` (those with `one_day_off` 0 and `equal` above 0). For every type whose column is NOT
empty, list the securities and dates behind it (up to 80 lines; tickers and dates are not client data), and say for each
whether the same date is `one_day_off` for many securities at once (a calendar or holiday effect) or for one security (a
corporate action or a bad bar).

**Table 2 -- the fund check v0.38 names.** The priced fund trades: rows of the transactions table that are a Buy or a Sale with
a Price above 0, for securities whose `SEC Asset Type` is the registered-investment-company value and whose `Share Class Type` is
neither the ETF value nor not-available (IB-pr-439 counted 1,099 fund-dates over 103 funds, 1,044 inside the 85 days, on that
basis; use the same basis, state it in `how_a_fund_is_recognised`, and say if your count differs and why). A mutual-fund purchase
or redemption is struck at the trade date's net asset value, so the trade's Price is an independent dated value. State
`unit_counted`: count TRADES (rows, de-duplicated by transaction id) and also the distinct fund-dates. For each trade, its Price
beside the reader's bar for the trade date, the prior trading day and the next trading day, exactly ONE outcome:
`same_day_only`, `prior_day_only`, `next_day_only`, `more_than_one` (the bar did not move between the days it matches),
`none`, `no_bar` (the reader has no bar for the trade date or the fund's ticker returned nothing). Which date is the "trade
date": the table may carry a trade date and a settle date; use the TRADE date, name the column, and print the same six counts
with the settle date as a second line if a settle-date column exists. Tolerance: a fund's NAV is quoted to the cent and a trade
price may carry more decimals: use the instrument's relative tolerance AND report the six counts again under "equal to the cent".
Per fund (`by_fund`): ticker, trades, and the six counts. Say whether `prior_day_only` or `next_day_only` trades concentrate in
particular funds, dates or transaction kinds (for example an exchange between funds, a reinvestment booked as a buy).

**Control.** A planted fixture: one security whose reader series is shifted by one day and one that is not (the first must read
`one_day_off` on the days its price moved); and three planted trades, at the same day's bar, the prior day's and a price matching
none. `control.planted` must equal `control.read`, with `shifted_series_reads_one_day_off: true` and
`trade_on_the_prior_bar_reads_prior_day_only: true` in both.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~299/`: `IB138-2_type_overlap_and_fund_check.json`
with `{type_join:{type_fields, securities_both_witnesses_carry, found_a_type, found_no_type, found_more_than_one_type,
how_a_type_is_taken}, overlap_by_type:{<type>:{securities, security_days, equal, one_day_off, neither, no_bar,
equal_on_days_the_close_moved, securities_with_any_one_day_off}}, one_day_off_rule, unchanged_price_rule,
types_with_an_empty_one_day_off_column, one_day_off_detail, fund_trades:{how_a_fund_is_recognised, unit_counted, date_column,
tolerance, trades, fund_dates, funds, same_day_only, prior_day_only, next_day_only, more_than_one, none, no_bar, to_the_cent:{...},
by_settle_date:{...}, by_fund:[...], concentration}, fetch:{calls:[{tickers}], distinct_tickers_asked,
tickers_asked_more_than_once:0}, control:{planted, read}, claims_regraded_in_product:false, other_sources_asked:0,
classes_admitted_by_this_cell:0}`; and a one-page `IB138-2_TYPE_OVERLAP_AND_FUND_CHECK_READ.md` holding both tables. Counts only:
no account id, no balance, no single account's holding or trade.

<criterion id="IB138-2-AC1" cell_refs="IB-pr-441"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r138/p138_cells.py" . IB138-2-AC1</invocation><expect>IB138-2-AC1 PASS</expect></criterion>
<criterion id="IB138-2-AC2" cell_refs="IB-pr-441"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r138/p138_cells.py" . IB138-2-AC2</invocation><expect>IB138-2-AC2 PASS</expect></criterion>
<criterion id="IB138-2-AC3" cell_refs="IB-pr-441"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r138/p138_cells.py" . IB138-2-AC3</invocation><expect>IB138-2-AC3 PASS</expect></criterion>

<expected_criteria>IB138-2-AC1, IB138-2-AC2, IB138-2-AC3</expected_criteria>

The checks grade sums, the join's completeness, that the listed empty-column types are those the table shows, the one-pass bound
and the control. Every count is UNMEASURED by the issuer. A non-empty one-day-off column or a pile of prior-day trades is a
FINDING, not a failure: do not make a number fit.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file, no PRD, no `sources.json`, no gold script, no ADVI_COTBKF file.
- **Refusal clause:** the 1,500-ticker stop; a whole fetch call that fails is recorded, not repeated. If a criterion cannot be
  met as written, stop, file a row and report. Never weaken a check; do not edit `p138_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W299-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's existing line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~299" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~299@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~299 <0.9.0_WK_IRPT_BCKEND~299@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Write no firm name as a literal in any file, and no token beginning `z09` in the two outputs (write a prefix's scope segment as `<scope>`).

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~299/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-441.type-overlap-and-priced-fund-trades-against-the-reader.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 130 (round 138, workstream ~P), cell `IB-pr-441`.
<owned_cells>IB-pr-441</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB138-2-AC1, IB138-2-AC2, IB138-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~299/IRPT_BCKEND.TO-IB-pr-441.type-overlap-and-priced-fund-trades-against-the-reader.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the join (found a type, none, more than one); table 1 in full, with the one-day-off column
and what is behind every non-empty entry; table 2's six counts by trade date, by settle date and to the cent, with the funds or
dates the off-day trades concentrate in; the number of fetch calls and tickers; the control; each criterion's last line; the
proof checker's result; scratch deleted; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read-only measurement written to the worker's own deliverables folder; no product file, route, function or served byte.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; S3 reads and public market-data fetches through a reader the estate already runs.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p138_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~16:5xZ: IB138-2-AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The figures named on the face (894 securities, 890 tickers, 1,099 and 1,044 fund-dates, 103 funds) are IB-pr-439's worker's, re-run by the issuer only as that cell's three criteria; the face tells this worker to state its own and say if they differ.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only). Egress: Yahoo Finance through ADVI_COTBKF's existing reader, one pass, bounded at 1,500 tickers.
</preflight>
